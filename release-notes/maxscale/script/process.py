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

def has_label(issue, label):
    return label in issue.get('Labels', '').split(',')

def issue_number(issue):
    return int(issue['Issue key'].split('-')[1])

# The text of a bullet is the 'Release Note Summary' of the issue.
# If it is missing, the Jira summary is used and the issue is reported.
def bullet_text(issue):
    text = ' '.join(issue.get('Custom field (Release Note Summary)', '').split())

    if not text:
        text = issue['Summary']
        without_release_note.append(issue['Issue key'])

    return md_escape(text)

def print_issues(header, issues):
    if len(issues) > 0:
        print(header)
        print()

        for i in issues:
            key = i['Issue key']
            print("* " + bullet_text(i) + " ([" + key + "](https://jira.mariadb.org/browse/" + key + "))")

        print()

# Returns the bug category, or an empty string if the bug does not have one.
def bug_category(bug):
    return bug.get('Custom field (Bug Category)', '')

# The anchor GitBook generates for a heading.
def heading_anchor(heading):
    return "#" + heading.lower().replace(' ', '-')

# A CVE of MaxScale is fixed by a bug, which is described under the fixed
# issues. Hence only the ids are listed, with a link to the category heading
# the bug is listed under.
def maxscale_cve_bullet(cve):
    id = cve['Id']
    key = cve['Issue']['Issue key']
    category = bug_category(cve['Issue'])
    return "* [" + id + "](" + cve['Url'] + ") ([" + key + "](https://jira.mariadb.org/browse/" + key + "), see [" + category + "](" + heading_anchor(category) + "))"

# An external vulnerability is fixed by a task, which is not listed anywhere
# else. Hence the bullet also tells what the vulnerability was in.
def external_vulnerability_bullet(cve):
    id = cve['Id']
    i = cve['Issue']
    return "* [" + id + "](" + cve['Url'] + ") Fixed by [" + i['Issue key'] + "](https://jira.mariadb.org/browse/" + i['Issue key'] + ") " + advisory_text(i)

def print_cves(header, cves, bullet_of):
    if len(cves) > 0:
        print(header)
        print()

        for cve in cves:
            print(bullet_of(cve))

        print()

# Bugs with these categories are intentionally left out of the release notes.
NOT_FOR_RELEASE_NOTES = ['Not for Release Notes', 'Not for ES Release Notes']

# Bugs with these categories are listed in a section of their own, before
# the fixed issues.
CATEGORIES_WITH_OWN_SECTION = ['Backports', 'Notable changes']

# The categories listed under 'Issues Fixed', in the order they appear.
FIXED_CATEGORIES = [
    'Can result in data loss',
    'Can result in hang or crash',
    'Can result in unexpected behaviour',
    'Related to install and upgrade',
    'Related to performance',
    'Unexpected results',
]

KNOWN_CATEGORIES = NOT_FOR_RELEASE_NOTES + CATEGORIES_WITH_OWN_SECTION + FIXED_CATEGORIES

# Returns the bugs that belong in the release notes, the others are reported.
def bugs_for_release_notes(bugs):
    included = []

    for b in bugs:
        category = b.get('Custom field (Bug Category)')

        if category in NOT_FOR_RELEASE_NOTES:
            not_for_release_notes.append(b)
        else:
            included.append(b)

    return included

# Returns a dict from bug category to the bugs of that category.
def bugs_by_category(bugs):
    categories = {}

    for b in bugs:
        categories.setdefault(bug_category(b), []).append(b)

    return categories


bugs = []
new_features = []
tasks = []
skipped = []
without_release_note = []
not_for_release_notes = []

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

bugs.sort(key=issue_number)
new_features.sort(key=issue_number)
tasks.sort(key=issue_number)

without_category = [b['Issue key'] for b in bugs if not bug_category(b)]
unknown_categories = [(b['Issue key'], bug_category(b)) for b in bugs if bug_category(b) and bug_category(b) not in KNOWN_CATEGORIES]

if without_category:
    print("error: No 'Bug Category', must be set in Jira:", file=sys.stderr)
    for key in without_category:
        print("  %s" % key, file=sys.stderr)

if unknown_categories:
    print("error: Unknown 'Bug Category', process.py must be updated:", file=sys.stderr)
    for key, category in unknown_categories:
        print("  %s [%s]" % (key, category), file=sys.stderr)

if without_category or unknown_categories:
    sys.exit(1)

# A bug whose category excludes it from the release notes is left out of the
# CVE section as well. A serious CVE may intentionally not be announced when
# the release is made, as that would expose those who have not yet upgraded.
bugs = bugs_for_release_notes(bugs)

# Check if some bug-fix fixes a CVE. These are assumed to be CVEs of MaxScale.
print_cves("## CVEs resolved", find_cves(bugs), maxscale_cve_bullet)

# Check if some task fixes a vulnerability, which is assumed to be a
# non-MaxScale one; e.g. a CVE or GHSA of an external library.
print_cves("## External vulnerabilities resolved", find_cves(tasks), external_vulnerability_bullet)

deprecated_features = [t for t in tasks if has_label(t, 'maxscale-deprecate')]
dropped_features = [t for t in tasks if has_label(t, 'maxscale-drop')]

print_issues("## New Features", new_features)
print_issues("## Deprecated Features", deprecated_features)
print_issues("## Dropped Features", dropped_features)

categories = bugs_by_category(bugs)

for category in CATEGORIES_WITH_OWN_SECTION:
    print_issues("## " + category, categories.get(category, []))

print("## Issues Fixed")
print()

for category in FIXED_CATEGORIES:
    print_issues("### " + category, categories.get(category, []))

# Diagnostics go to stderr; generate_release_notes.sh captures stdout only, so
# this is visible to whoever runs it without ending up on the page.
if skipped:
    print("Not listed, closed with a resolution other than 'Fixed':", file=sys.stderr)
    for key, resolution in skipped:
        print("  %s [%s]" % (key, resolution), file=sys.stderr)

if not_for_release_notes:
    print("Not listed, bug category excludes it from the release notes:", file=sys.stderr)
    for b in not_for_release_notes:
        print("  %s [%s]" % (b['Issue key'], bug_category(b)), file=sys.stderr)

withheld_cves = find_cves(not_for_release_notes)

if withheld_cves:
    print("WARNING: CVE report suppressed due to the bug category:", file=sys.stderr)
    for cve in withheld_cves:
        print("  %s %s [%s]" % (cve['Id'], cve['Issue']['Issue key'], bug_category(cve['Issue'])), file=sys.stderr)

if without_release_note:
    print("No 'Release Note Summary', Jira summary used instead:", file=sys.stderr)
    for key in without_release_note:
        print("  %s" % key, file=sys.stderr)
