#!/usr/bin/env python3
"""Rebuild the Plugin API Documentation section of server/SUMMARY.md.

The generated pages are listed under the "Plugin API Documentation" entry, which
the workflow inserts right after "Plugin Overview" and points at README.md (the
renamed generated mainpage). Everything already nested under that entry is
replaced, so the section always matches the generated set.

The nav follows the doxygen group tree. Moxygen puts a breadcrumb under each
group page's title -- `> [`Plugin API`](plugin_api.md#...) / [`Plugin
Types`](plugin_types.md#...)` -- whose last link is the page's parent group,
and the page is nested under that parent. Since MDBF-1224 there are about 80
generated pages, and a flat list of them is unusable; before it, the same rule
nests the PSI groups under "Instrumentation Interface".

Pages without a breadcrumb sit directly under the landing page, in this order:

1. the doxygen pages (page-*.md), in the order the landing page links them,
   then any others by title;
2. the top-level groups, by title;
3. api.md ("API Reference"), which since MDBF-1224 only indexes the groups.

Siblings are ordered by title, byte-wise, so the order is the same on every
platform. GitBook builds a page's URL from its nav position, so nesting moves
the URLs of the pages that used to be flat; their old URLs equal their file
paths, which GitBook answers with a 307 to the nav URL.

Usage: add_server_plugin_api_to_summary.py [base_dir]
  base_dir defaults to "." (the mariadb-docs repo root).
"""
import pathlib
import re
import sys

SUMMARY_DIR = 'reference/plugins/api-plugin'
PARENT_TITLE = 'Plugin API Documentation'
PARENT_PAGE = 'README.md'
ANCHOR_ENTRY = '* [Plugin Overview](reference/plugins/plugin-overview.md)'
PARENT_INDENT = 4
STEP = 2
MD_LINK = re.compile(r'\]\(([A-Za-z0-9_.-]+\.md)')


def title_of(path):
    for line in path.read_text().split('\n'):
        if line.startswith('# '):
            return line[2:].strip()
    return path.stem


def parent_of(path, names):
    """The parent group named by the page's breadcrumb, or None.

    The breadcrumb is the first non-blank line after the H1 title; the
    frontmatter step has already run, so it is not at a fixed line number.
    """
    lines = path.read_text().split('\n')
    after_title = next((i + 1 for i, line in enumerate(lines)
                        if line.startswith('# ')), None)
    if after_title is None:
        return None
    line = next((l for l in lines[after_title:] if l.strip()), '')
    if not line.startswith('> ['):
        return None
    links = [t for t in MD_LINK.findall(line) if t in names and t != path.name]
    return links[-1] if links else None


def build_tree(dest_dir):
    """Returns (titles, children, roots) for the generated pages."""
    pages = sorted(p for p in dest_dir.glob('*.md') if p.name != PARENT_PAGE)
    names = {p.name for p in pages}
    titles = {p.name: title_of(p) for p in pages}
    children = {name: [] for name in names}
    roots = []
    for p in pages:
        parent = parent_of(p, names)
        (children[parent] if parent else roots).append(p.name)

    def by_title(name):
        return (titles[name], name)

    for kids in children.values():
        kids.sort(key=by_title)

    landing = dest_dir / PARENT_PAGE
    linked = MD_LINK.findall(landing.read_text()) if landing.exists() else []
    doc_pages = [n for n in roots if n.startswith('page-')]
    doc_pages.sort(key=lambda n: (linked.index(n) if n in linked
                                  else len(linked), titles[n], n))
    groups = sorted((n for n in roots
                     if not n.startswith('page-') and n != 'api.md'),
                    key=by_title)
    tail = ['api.md'] if 'api.md' in roots else []
    return titles, children, doc_pages + groups + tail


def nav_lines(titles, children, roots):
    out = []

    def emit(name, depth):
        indent = ' ' * (PARENT_INDENT + STEP * depth)
        out.append(f'{indent}* [{titles[name]}]({SUMMARY_DIR}/{name})')
        for kid in children[name]:
            emit(kid, depth + 1)

    for name in roots:
        emit(name, 1)
    return out


def rewrite_summary(summary_text, block):
    """Replace (or insert) the section; raises if the anchor entry is gone."""
    parent_line = (' ' * PARENT_INDENT +
                   f'* [{PARENT_TITLE}]({SUMMARY_DIR}/{PARENT_PAGE})')
    lines = summary_text.split('\n')

    # Drop an existing section: its entry plus every line nested deeper.
    out, skipping = [], False
    for line in lines:
        if skipping:
            stripped = line.lstrip(' ')
            if stripped.startswith('* ') and \
                    len(line) - len(stripped) > PARENT_INDENT:
                continue
            skipping = False
        if f'[{PARENT_TITLE}]' in line:
            skipping = True
            continue
        out.append(line)

    for i, line in enumerate(out):
        if line.strip() == ANCHOR_ENTRY:
            return '\n'.join(out[:i + 1] + [parent_line] + block +
                             out[i + 1:])
    raise SystemExit('Could not find the Plugin Overview entry in SUMMARY.md')


def main():
    base_dir = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
    dest_dir = base_dir / 'server' / 'reference' / 'plugins' / 'api-plugin'
    summary = base_dir / 'server' / 'SUMMARY.md'
    assert dest_dir.is_dir(), f'not a directory: {dest_dir}'
    assert summary.is_file(), f'not a file: {summary}'

    titles, children, roots = build_tree(dest_dir)
    block = nav_lines(titles, children, roots)
    assert block, f'no generated pages in {dest_dir}'
    summary.write_text(rewrite_summary(summary.read_text(), block))
    print(f'Plugin API Documentation: {len(block)} nav entries, '
          f'{len(roots)} at the top level')


if __name__ == '__main__':
    main()
