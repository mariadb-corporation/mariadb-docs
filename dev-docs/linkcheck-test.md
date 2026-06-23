# Link check test

This page deliberately contains no links of any kind. It exists only to verify
that the PR link checker no longer fails with "No links were found" when a
changed Markdown file has nothing to link-check.

Expected: the link-check check passes (green) thanks to failIfEmpty: false.

Delete this file before merging — DOCS-6272 test.
