#!/usr/bin/env python3
"""Retarget generated Plugin API links whose fragment is a raw doxygen ID.

Since MDBF-1224 (MariaDB/server#5617) the plugin headers and `index.dox` use
`@ref` to point at `@section`s of the conceptual pages and at individual enum
values. Moxygen writes those references with doxygen's internal ID as the
fragment -- `page-concepts.md#concepts_1concept_plugin_api` for a section,
`plugin_status_vars.md#group__plugin__status__vars_1gga31d3...` for an enum
value -- and no heading GitBook publishes ever carries such an ID, so every one
of them is dead. They are a different class from the two the earlier steps fix
(page-title breadcrumbs, `-N` member suffixes), which is why this runs after
them, as the last link fixer.

For a fragment that resolves to nothing on its target page, three strategies
are tried in order, and a link is rewritten only when a strategy yields exactly
one candidate on that page:

1. Same letters: a published anchor that equals the fragment once both are
   reduced to letters and digits (fragcheck's `squash()`). This is the
   punctuation class -- `#operatorstructst_mysql_const_lex_string` against a
   heading GitBook publishes as `#operator-struct-st_mysql_const_lex_string`.
2. Link text: `@ref` renders the target's title as the link text
   (`[Plugin Library](page-concepts.md#concepts_1concept_plugin_library)`), so
   the anchor GitBook derives from that text is where the link meant to go.
3. Enum value: the value is not a heading but a row of its enum's table
   (`| `SHOW_FUNC` | ... |` under `### enum_mysql_show_type`), so the link is
   pointed at the heading of the section that holds that row.

Anything else is reported on stderr and left as it was. Like the other fixers,
it does not fail the step: fragcheck gates the bot PR and shows the reviewer
whatever is left.

Usage: fix_plugin_api_doxygen_refs.py [base_dir]
  base_dir defaults to "." (the mariadb-docs repo root).
"""
import collections
import importlib.util
import pathlib
import re
import sys

LINK = re.compile(r'\[((?:[^\[\]]|`[^`]*`)*)\]\(([^)\s]+)\)')
TABLE_CELL = re.compile(r'^\|\s*`([^`]+)`\s*\|')


def load_fragcheck(repo_root):
    spec = importlib.util.spec_from_file_location(
        'fragcheck', repo_root / '.claude' / 'hooks' / 'fragcheck.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Page:
    """The published anchors of one page, with the line each heading is on."""

    def __init__(self, path, fragcheck):
        self.path = path
        self.lines = path.read_text().split('\n')
        seen = collections.Counter()
        self.anchors = []                    # [(line_no, base, anchor)]
        for line_no, text, explicit in fragcheck.anchor_sources(path):
            base = explicit if explicit else fragcheck.gitbook_slug(text)
            if not base:
                continue
            n = seen[base]
            seen[base] += 1
            self.anchors.append(
                (line_no, base, base if n == 0 else f'{base}-{n}'))
        self.live = {anchor for _, _, anchor in self.anchors}


def resolve(frag, text, page, fragcheck):
    """The anchor a dead fragment should point at on `page`, or None."""
    squashed = fragcheck.squash(frag)
    same = [a for _, _, a in page.anchors if fragcheck.squash(a) == squashed]
    if len(same) == 1:
        return same[0]

    plain = fragcheck.strip_inline(text).strip()
    if plain:
        want = fragcheck.gitbook_slug(plain)
        by_text = [a for _, base, a in page.anchors if base == want]
        if len(by_text) == 1:
            return by_text[0]

    rows = [n for n, line in enumerate(page.lines, 1)
            if (m := TABLE_CELL.match(line)) and m.group(1) == plain]
    if len(rows) == 1:
        above = [a for a in page.anchors if a[0] < rows[0]]
        if above:
            return above[-1][2]
    return None


def fix_dir(dest_dir, fragcheck):
    """Returns (rewrites, unresolved), rewriting pages in place."""
    pages = {p.name: Page(p, fragcheck) for p in sorted(dest_dir.glob('*.md'))}
    rewrites, unresolved = [], []
    for name, page in pages.items():
        changed = False
        for i, line in enumerate(page.lines):
            def repl(m):
                nonlocal changed
                text, target = m.group(1), m.group(2)
                if '#' not in target or '://' in target:
                    return m.group(0)
                fname, frag = target.split('#', 1)
                if not frag:
                    return m.group(0)       # `api.md#` -- nothing to retarget
                dest = pages.get(fname or name)
                if dest is None or frag in dest.live:
                    return m.group(0)       # elsewhere, or already resolves
                anchor = resolve(frag, text, dest, fragcheck)
                if anchor is None:
                    unresolved.append((name, i + 1, target))
                    return m.group(0)
                changed = True
                rewrites.append((name, i + 1, target, anchor))
                return f'[{text}]({fname}#{anchor})'
            page.lines[i] = LINK.sub(repl, line)
        if changed:
            page.path.write_text('\n'.join(page.lines))
    return rewrites, unresolved


def main():
    base_dir = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
    dest_dir = base_dir / 'server' / 'reference' / 'plugins' / 'api-plugin'
    assert dest_dir.is_dir(), f'not a directory: {dest_dir}'

    rewrites, unresolved = fix_dir(dest_dir, load_fragcheck(base_dir))
    for name, line_no, target, anchor in rewrites:
        print(f'{name}:{line_no}: {target} -> #{anchor}')
    for name, line_no, target in unresolved:
        print(f'{name}:{line_no}: {target} LEFT ALONE', file=sys.stderr)
    print(f'retargeted {len(rewrites)} doxygen-ID fragment(s); '
          f'{len(unresolved)} left alone')


if __name__ == '__main__':
    main()
