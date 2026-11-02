#!/usr/bin/env python3
"""Stop publishing the generated api.md and repoint every link into it.

Moxygen emits `api.md`, one page holding every class, macro, typedef and
function of the plugin headers. It repeats the group pages and renders as about
20 MB of HTML (DOCS-6625). Until MDBF-1224 (MariaDB/server#5617) it was also the
only home of the entries that no doxygen group covered, so it had to stay; since
then every one of its entries is also on a group page, and it goes.

The group pages link into it, though -- 958 links on 26 pages when this was
written, mostly from `Group_PSI_v1.md`. Each one is repointed to the group page
that documents the same entry:

* `api.md#frag` names one of api.md's headings: the fragment is resolved
  against api.md's own published anchors. That heading is matched to the
  headings of the other generated pages by its exact TEXT and LEVEL, not by
  its slug, because slugs collide: `MARIA_DECLARE_PLUGIN__` and
  `maria_declare_plugin` both publish as `#maria_declare_plugin`, and the
  `my_bool` typedef shares its name with a struct member one level down.
  When api.md holds a heading N times and the other pages hold it exactly N
  times too -- `PSI_table_io_operation` is both an enum and a typedef -- the
  k-th occurrence in api.md maps to the k-th elsewhere, in page and line
  order. Any other count is unresolved.
* `api.md` or `api.md#` with no fragment -- the landing page's "API reference"
  bullet -- goes to `plugin_api.md`, the top of the group tree.
* Anything else is unresolved: the link becomes its plain text, and is reported
  on stderr. That drops one link rather than publishing a dead one, and, like
  the other fixers, does not block the daily sync over it.

Runs after the link fixers, so the anchors it reads are the published ones, and
before the frontmatter and SUMMARY.md steps, so neither ever sees api.md. When
the generator stops emitting api.md, this is a no-op.

Usage: drop_plugin_api_md.py [base_dir]
  base_dir defaults to "." (the mariadb-docs repo root).
"""
import collections
import importlib.util
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
API = 'api.md'
TOP = 'plugin_api.md'
LINK = re.compile(r'\[([^\]\n]*)\]\((?:\./)?api\.md(?:#([^)\s]*))?\)')


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def entries(page, published_anchors, fragcheck):
    """[(text, level, anchor)] for the anchored headings, in document order."""
    levels = {n: (level, text) for n, level, text, _ in
              fragcheck.headings_of(page)}
    return [(levels[n][1], levels[n][0], anchor)
            for n, _, anchor in published_anchors(page, fragcheck)
            if n in levels]


def build_map(dest_dir, published_anchors, fragcheck):
    """api.md anchor -> 'page.md#anchor' for every heading that maps cleanly."""
    api = entries(dest_dir / API, published_anchors, fragcheck)
    elsewhere = collections.defaultdict(list)
    for page in sorted(dest_dir.glob('*.md')):
        if page.name == API:
            continue
        for text, level, anchor in entries(page, published_anchors,
                                           fragcheck):
            elsewhere[(text, level)].append(f'{page.name}#{anchor}')
    in_api = collections.Counter((text, level) for text, level, _ in api)
    seen = collections.Counter()
    mapping = {}
    for text, level, anchor in api:
        k = seen[(text, level)]
        seen[(text, level)] += 1
        hits = elsewhere.get((text, level), [])
        if len(hits) == in_api[(text, level)]:
            mapping[anchor] = hits[k]
    return mapping


def resolve(frag, mapping, names):
    """The new link target for `api.md#frag`, or None."""
    if not frag:
        return TOP if TOP in names else None
    return mapping.get(frag)


def repoint(page, mapping, names):
    """Rewrites one page in place; returns (rewritten, unresolved)."""
    rewritten, unresolved = 0, []
    out, fence = [], False
    for line_no, line in enumerate(page.read_text().split('\n'), 1):
        if line.lstrip().startswith('```'):
            fence = not fence
        if fence or 'api.md' not in line:
            out.append(line)
            continue

        def sub(m):
            nonlocal rewritten
            target = resolve(m.group(2), mapping, names)
            if target is None:
                unresolved.append((line_no, m.group(0)))
                return m.group(1)
            rewritten += 1
            if target.startswith(f'{page.name}#'):
                target = target[len(page.name):]      # same page: `#anchor`
            return f'[{m.group(1)}]({target})'

        out.append(LINK.sub(sub, line))
    page.write_text('\n'.join(out))
    return rewritten, unresolved


def drop(dest_dir, fragcheck, published_anchors):
    """Repoints the links, removes api.md; returns (rewritten, unresolved).

    `unresolved` is [(page name, line, link)]. None when there is no api.md.
    """
    api = dest_dir / API
    if not api.exists():
        return None
    mapping = build_map(dest_dir, published_anchors, fragcheck)
    names = {p.name for p in dest_dir.glob('*.md')} - {API}
    total, failed = 0, []
    for page in sorted(dest_dir.glob('*.md')):
        if page.name == API:
            continue
        rewritten, unresolved = repoint(page, mapping, names)
        total += rewritten
        failed += [(page.name, n, link) for n, link in unresolved]
    api.unlink()
    return total, failed


def main():
    base_dir = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
    dest_dir = base_dir / 'server' / 'reference' / 'plugins' / 'api-plugin'
    assert dest_dir.is_dir(), f'not a directory: {dest_dir}'
    fragcheck = load(base_dir / '.claude' / 'hooks' / 'fragcheck.py',
                     'fragcheck')
    published_anchors = load(HERE / 'fix_plugin_api_member_anchors.py',
                             'member_anchors').published_anchors
    result = drop(dest_dir, fragcheck, published_anchors)
    if result is None:
        print(f'{API} was not generated; nothing to do')
        return
    total, failed = result
    for name, line_no, link in failed:
        print(f'{name}:{line_no}: {link} -> plain text (no unique target)',
              file=sys.stderr)
    print(f'repointed {total} link(s) into {API}; {len(failed)} became plain '
          f'text; removed {API}')


if __name__ == '__main__':
    main()
