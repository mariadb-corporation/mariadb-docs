#!/usr/bin/env python3

import sys
import csv
import itertools
import re

# Markdown metacharacters that occur in practice in MXS summaries and that
# GitBook's own normalizer escapes: identifiers like admin_ssl_*, and bracketed
# module names like [readwritesplit]. Escaping them here keeps the generated
# page byte-identical to what GitBook would save, so the first edit in the web
# app does not produce a spurious GITBOOK-XXX diff.
_MD_SPECIALS = re.compile(r"[_*\[]")

# Escape Markdown metacharacters in free-form text (e.g. Jira summaries) so they
# render literally instead of as Markdown formatting. Code spans are left alone:
# backticks in MXS summaries are deliberate, and a backslash inside a code span
# renders as a literal backslash rather than escaping anything.
def md_escape(s):
    # MXS summaries occasionally carry leading/trailing whitespace (e.g. MXS-6886
    # ends with a space). Left in place it becomes trailing whitespace on the
    # generated bullet, which every subsequent editor then has to clean by hand.
    s = s.strip()
    # Splitting on backticks alternates outside/inside: even indices are outside
    # a code span, odd indices inside.
    parts = s.split("`")
    for i in range(0, len(parts), 2):
        parts[i] = _MD_SPECIALS.sub(lambda m: "\\" + m.group(), parts[i])
    return "`".join(parts)

# The advisory databases whose ids the SBOM scanner puts in the labels of the
# tickets it files, e.g. MXS-7727 carries GHSA-mrv2-3pqr-j5jr. A label without
# the dash, such as the plain 'CVE' every SBOM ticket has, is not an id.
ADVISORY_URLS = [
    (re.compile(r"CVE-\d{4}-\d+", re.I), 'https://www.cve.org/CVERecord?id='),
    (re.compile(r"GHSA(-[0-9a-z]{4}){3}", re.I), 'https://github.com/advisories/'),
    (re.compile(r"GO-\d{4}-\d+", re.I), 'https://pkg.go.dev/vuln/'),
]

def advisory_url(label):
    for pattern, base in ADVISORY_URLS:
        if pattern.fullmatch(label):
            return base + label

    return None

# The description of an SBOM ticket begins with a line such as
#   Package type {{npm}}, name {{axios}}, affected version {{1.13.6}}, fix version {{1.15.1}}.
# and its summary only repeats the advisory id, so the package is taken from
# here. The fix version is the lowest that closes the advisory, not necessarily
# the one MaxScale moved to, so only the affected version is used.
_SBOM_PACKAGE = re.compile(r"name \{\{(.+?)\}\}, affected version \{\{(.+?)\}\}")

def advisory_text(issue):
    m = _SBOM_PACKAGE.search(issue.get('Description', ''))

    if m:
        return md_escape("Vulnerability in " + m.group(1) + " " + m.group(2))

    return md_escape(issue['Summary'])

# Loop over issues. If an issue has a label that is the id of an advisory in
# one of the databases above, it is listed with a link to that advisory. If an
# issue has multiple such labels, the issue will be added multiple times (by
# design).
#
def find_cves(issues):
    cves=[]

    for i in issues:
        labels_field = i.get('Labels')
        if labels_field:
            labels=labels_field.split(',')
            for label in labels:
                url = advisory_url(label)
                if url:
                    cve = {};
                    cve['Id'] = label
                    cve['Url'] = url
                    cve['Issue'] = i
                    cves.append(cve)

    return cves

def print_cves(header, cves):
    print(header)
    print()

    for cve in cves:
        id = cve['Id']
        i = cve['Issue']
        print("* [" + id + "](" + cve['Url'] + ") Fixed by [" + i['Issue key'] + "](https://jira.mariadb.org/browse/" + i['Issue key'] + ") " + advisory_text(i))

    print()


bugs = []
new_features = []
tasks = []
skipped = []

reader = csv.reader(sys.stdin.readlines())
field_names = next(reader)

for row in reader:
    # In case there are multiple values of a particular field, collect
    # all values separated by a ','.
    groups = itertools.groupby(zip(field_names, row), key=lambda x: x[0])
    row = dict([(k, ','.join([v[1] for v in g])) for k, g in groups])

    # Only issues actually resolved as 'Fixed' belong in the release notes. An
    # issue can be Closed with some other resolution - 'Not a Bug' is common for
    # SBOM tasks that turn out not to apply to MaxScale - and listing those would
    # claim a fix that was never made. Particularly bad for the CVE sections.
    if row.get('Resolution') != 'Fixed':
        skipped.append((row['Issue key'], row.get('Resolution') or 'unresolved'))
        continue

    if row['Issue Type'] == 'Bug':
        bugs.append(row)
    elif row['Issue Type'] == 'New Feature':
        new_features.append(row)
    elif row['Issue Type'] == 'Task':
        tasks.append(row)

# Check if some bug-fix fixes a CVE. These are assumed to be CVEs of MaxScale.
cves = find_cves(bugs)

if len(cves) > 0:
    print_cves("## CVEs resolved.", cves)

# If there are tasks, check if any of them fixes a vulnerability, which is
# assumed to be a non-MaxScale one; e.g. a CVE or GHSA of an external library.
if len(tasks) > 0:
    cves = find_cves(tasks)

    if len(cves) > 0:
        print_cves("## External vulnerabilities resolved.", cves)

if len(new_features) > 0:
    print("## New Features")
    print()

    for f in new_features:
        print("* [" + f['Issue key'] + "](https://jira.mariadb.org/browse/" + f['Issue key'] + ") " + md_escape(f['Summary']))
    print()


print("## Bug fixes")
print()

for b in bugs:
    print("* [" + b['Issue key'] + "](https://jira.mariadb.org/browse/" + b['Issue key'] + ") " + md_escape(b['Summary']))

print()

# Diagnostics go to stderr; generate_release_notes.sh captures stdout only, so
# this is visible to whoever runs it without ending up on the page.
if skipped:
    print("Not listed, closed with a resolution other than 'Fixed':", file=sys.stderr)
    for key, resolution in skipped:
        print("  %s [%s]" % (key, resolution), file=sys.stderr)
