#!/usr/bin/env python3
"""Retarget same-page member links whose moxygen disambiguation suffix is wrong.

A generated struct page lists a struct's fields in a "Public Attributes" table
and links each one to that field's own heading further down the same page. When
a field name repeats -- `m_flags`, `m_psi`, `m_thread` and friends appear in
dozens of PSI locker-state structs -- moxygen disambiguates with a `-N` suffix
counted over its own doxygen XML model. GitBook counts occurrences of the
*rendered heading* instead, and the two disagree whenever moxygen's model holds
an occurrence that never becomes a heading on this page (a sibling
struct/version-group that lands on a different page, or a node filtered at
render time). Moxygen's counter then runs ahead and the link points at an anchor
that does not exist: `#m_rwlock-1` where the page publishes only `#m_rwlock`.
It is not a slug-format disagreement -- that was the h5/h6 and breadcrumb
classes, both already fixed upstream and in this workflow -- so nothing about
heading depth or anchor markers repairs it.

The same mechanism repairs one punctuation case: a link written `#_thd_wait_
type_e` against a heading GitBook publishes as `#thdwait_type_e`.

The fix resolves each dead fragment by DOCUMENT POSITION, not by arithmetic.
A blind "clamp the suffix down to the highest one that exists" would be wrong:
`Thread_instrumentation.md` asks for `#m_psi-4` and `#m_psi-5` from two
different structs, and clamping both to the page's highest `m_psi` anchor would
point them at one heading, right for neither. Instead, for a fragment that
resolves to nothing, look for the heading of that base name inside the link's
own struct section (the nearest enclosing heading of level 3 or shallower) and,
failing that, on the page as a whole. Retarget only when exactly one candidate
exists; anything ambiguous is left alone and reported, so a future generator
change that breaks this assumption shows up as a skip rather than as a
plausible-looking wrong link. Links that already resolve are never touched, and
neither is any cross-page link.

One exception, from MDBF-1224 (DOCS-6988): a struct with two fields of the same
name. `sql_service_st` has two `length` fields; moxygen links them as
`#length-1` and `#length-2`, GitBook publishes `#length` and `#length-1`. The
second link is dead and has two candidates, and the first resolves -- to the
wrong field. When the section holds as many links of that name as headings,
they are paired in document order (the attribute table lists the fields in the
order of their headings), and all of them are rewritten, the live one too.

An unresolved fragment is reported on stderr and left as it was, but does NOT
fail the step: blocking the whole daily sync -- frontmatter, SUMMARY.md, the
pull request -- over an in-page navigation nit would be out of proportion, and
the dead anchor is caught anyway by the fragcheck gate that DOCS-6675 wired
into this workflow, which posts its verdict onto the bot PR where a reviewer
sees it.

Usage: fix_plugin_api_member_anchors.py [base_dir]
  base_dir defaults to "." (the mariadb-docs repo root).
"""
import collections
import importlib.util
import pathlib
import re
import sys

SUFFIX = re.compile(r'-\d+$')


def load_fragcheck(repo_root):
    spec = importlib.util.spec_from_file_location(
        'fragcheck', repo_root / '.claude' / 'hooks' / 'fragcheck.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def published_anchors(page, fragcheck):
    """[(line_no, slug_base, published_anchor)] in document order.

    Mirrors fragcheck.anchors_of(), which drops the line numbers this needs to
    tell one repeated field name from another by position.
    """
    seen = collections.Counter()
    out = []
    for line_no, text, explicit in fragcheck.anchor_sources(page):
        base = explicit if explicit else fragcheck.gitbook_slug(text)
        if not base:
            continue
        n = seen[base]
        seen[base] += 1
        out.append((line_no, base, base if n == 0 else f'{base}-{n}'))
    return out


def section_bounds(page, fragcheck, line_no):
    """(start, end) lines of the level<=3 section containing line_no.

    Struct sections are `###` on these pages and their members are `####`, so a
    heading of level 3 or shallower is the boundary between one struct and the
    next.
    """
    tops = [n for n, level, _, _ in fragcheck.headings_of(page) if level <= 3]
    start = max((n for n in tops if n <= line_no), default=0)
    end = min((n for n in tops if n > start), default=1 << 30)
    return start, end


def pair_by_order(links, line_no, frag, want, in_section, fragcheck, start, end):
    """[(line_no, frag, anchor)] for a section whose repeated name can't resolve.

    When a struct has two fields of the same name, the links in its attribute
    table and the field headings below come in the same order, so the k-th link
    belongs to the k-th heading. Only used when the counts match; every link of
    that name in the section is paired, because a link whose suffix happens to
    resolve may resolve to the wrong field (`#length-1` asked for the first
    `length` of `sql_service_st`, which GitBook publishes as `#length`).
    """
    same = [(n, t[1:]) for t, n in links
            if t.startswith('#') and start < n < end and
            fragcheck.gitbook_slug(SUFFIX.sub('', t[1:])) == want]
    if len(same) != len(in_section) or (line_no, frag) not in same:
        return None
    return [(n, f, in_section[k][2]) for k, (n, f) in enumerate(same)]


def fix_page(page, fragcheck):
    """Returns (rewrites, unresolved) for one page, rewriting it in place."""
    anchors = published_anchors(page, fragcheck)
    live = {anchor for _, _, anchor in anchors}
    lines = page.read_text().split('\n')
    links = fragcheck.links_of(page)

    rewrites, unresolved, paired = [], [], set()
    for target, line_no in links:
        if not target.startswith('#'):
            continue                      # cross-page; not this defect
        frag = target[1:]
        if frag in live or (line_no, frag) in paired:
            continue                      # already resolves; leave it alone
        want = fragcheck.gitbook_slug(SUFFIX.sub('', frag))
        matches = [a for a in anchors if a[1] == want]
        start, end = section_bounds(page, fragcheck, line_no)
        in_section = [a for a in matches if start < a[0] < end]
        candidates = in_section or matches
        if len(candidates) == 1:
            todo = [(line_no, frag, candidates[0][2])]
        else:
            todo = pair_by_order(links, line_no, frag, want, in_section,
                                 fragcheck, start, end)
            if todo is None:
                unresolved.append((line_no, frag, len(candidates)))
                continue
        for n, f, anchor in todo:
            paired.add((n, f))
            if f == anchor:
                continue
            old, new = f'](#{f})', f'](#{anchor})'
            if old not in lines[n - 1]:
                unresolved.append((n, f, -1))
                continue
            lines[n - 1] = lines[n - 1].replace(old, new, 1)
            rewrites.append((n, f, anchor))

    if rewrites:
        page.write_text('\n'.join(lines))
    return rewrites, unresolved


def main():
    base_dir = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
    dest_dir = base_dir / 'server' / 'reference' / 'plugins' / 'api-plugin'
    assert dest_dir.is_dir(), f'not a directory: {dest_dir}'

    fragcheck = load_fragcheck(base_dir)
    total, failed = 0, 0
    for page in sorted(dest_dir.glob('*.md')):
        rewrites, unresolved = fix_page(page, fragcheck)
        total += len(rewrites)
        failed += len(unresolved)
        for line_no, frag, anchor in rewrites:
            print(f'{page.name}:{line_no}: #{frag} -> #{anchor}')
        for line_no, frag, count in unresolved:
            reason = ('the link text moved' if count < 0
                      else f'{count} candidate headings')
            print(f'{page.name}:{line_no}: #{frag} LEFT ALONE ({reason})',
                  file=sys.stderr)
    print(f'retargeted {total} dead member anchor(s); {failed} left alone')


if __name__ == '__main__':
    main()
