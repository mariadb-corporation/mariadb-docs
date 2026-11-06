#!/usr/bin/env python3
"""Give every generated Plugin API page the standard license line and form.

Every other page in the docs ends with a license line and the Marketo
feedback form (DOCS-7067). These pages can't be given them by hand: the sync
deletes the folder and regenerates it from the MariaDB/server headers on every
run, so this step appends them instead (DOCS-7073):

    <last line of the page>

    <sub>_This page is licensed: GPLv2_</sub>

    {% @marketo/form formId="4316" %}

The license is GPLv2 because the content comes from the server source. The
line is the one other GPLv2 pages in the Server space already use.

A page that already ends with the footer is left unchanged, so a rerun, or a
sync that only regenerated some pages, never stacks a second footer. Trailing
blank lines are trimmed before the footer, so the page ends the same way
however moxygen finished it.

Runs after the frontmatter step, so it sees the page as published.

Usage: add_footer_to_server_plugin_api.py [base_dir]
  base_dir defaults to "." (the mariadb-docs repo root).
"""
import pathlib
import sys

LICENSE = '<sub>_This page is licensed: GPLv2_</sub>'
FORM = '{% @marketo/form formId="4316" %}'
FOOTER = f'{LICENSE}\n\n{FORM}'


def add_footer(text):
    body = text.rstrip()
    if body.endswith(FOOTER):
        return text
    return f'{body}\n\n{FOOTER}\n'


def fix_file(page):
    text = page.read_text()
    fixed = add_footer(text)
    if fixed != text:
        page.write_text(fixed)
        return True
    return False


def fix_dir(dest_dir):
    return [page for page in sorted(dest_dir.rglob('*.md')) if fix_file(page)]


def main():
    base_dir = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
    dest_dir = base_dir / 'server' / 'reference' / 'plugins' / 'api-plugin'
    assert dest_dir.is_dir(), f'not a directory: {dest_dir}'
    changed = fix_dir(dest_dir)
    for page in changed:
        print(f'added footer: {page}')
    print(f'{len(changed)} file(s) changed')


if __name__ == '__main__':
    main()
