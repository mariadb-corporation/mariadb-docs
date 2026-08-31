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
    # Splitting on backticks alternates outside/inside: even indices are outside
    # a code span, odd indices inside.
    parts = s.split("`")
    for i in range(0, len(parts), 2):
        parts[i] = _MD_SPECIALS.sub(lambda m: "\\" + m.group(), parts[i])
    return "`".join(parts)

# Loop over issues. If an issue has a label that starts with 'CVE-',
# assume the label is a CVE id. If an issue has multiple CVE labels,
# the issue will be added multiple times (by design).
#
def find_cves(issues):
    cves=[]

    for i in issues:
        labels_field = i.get('Labels')
        if labels_field:
            labels=labels_field.split(',')
            for label in labels:
                if label[0:4].upper() == 'CVE-':
                    cve = {};
                    cve['Id'] = label
                    cve['Issue'] = i
                    cves.append(cve)

    return cves

def print_cves(header, cves):
    print(header)
    print()

    for cve in cves:
        id = cve['Id']
        i = cve['Issue']
        print("* [" + id + "](https://www.cve.org/CVERecord?id=" + id + ") Fixed by [" + i['Issue key'] + "](https://jira.mariadb.org/browse/" + i['Issue key'] + ") " + md_escape(i['Summary']))

    print()


bugs = []
new_features = []
tasks = []

reader = csv.reader(sys.stdin.readlines())
field_names = next(reader)

for row in reader:
    # In case there are multiple values of a particular field, collect
    # all values separated by a ','.
    groups = itertools.groupby(zip(field_names, row), key=lambda x: x[0])
    row = dict([(k, ','.join([v[1] for v in g])) for k, g in groups])

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

# If there are tasks, check if any of them fixes a CVE, which is assumed
# to be a non-MaxScale one; e.g. a CVE of an external library.
if len(tasks) > 0:
    cves = find_cves(tasks)

    if len(cves) > 0:
        print_cves("## External CVEs resolved.", cves)

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
