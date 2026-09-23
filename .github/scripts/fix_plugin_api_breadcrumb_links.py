#!/usr/bin/env python3
"""Strip dead page-title fragments from the generated Plugin API breadcrumb links.

Moxygen emits cross-page "breadcrumb" navigation as `[Title](Other.md#slug)`,
where `slug` is `Other.md`'s own `#` page title turned into an anchor (the
parent-group blockquote pointing at each child page, and each child's
blockquote pointing back at its parent). GitBook never anchors an <h1> page
title, so every one of these links is dead by construction -- no marker,
heading-depth, or moxygen-flag change can fix it, because it isn't a heading
anchor problem: it's a link pointing at an anchor that will never exist.

The fix: for any link `(Page.md#frag)`, if `frag` -- letters and digits only,
case-folded -- matches `Page.md`'s own first `#` heading reduced the same way,
drop the fragment: `(Page.md)` lands on the same page (the intended
navigation), and unlike the fragment form, it resolves. Matching has to be
this loose because moxygen's title-anchor convention strips ALL separators
("Instrumentation Interface" -> "instrumentationinterface"), not GitBook's
own hyphenated slug ("instrumentation-interface") -- the two never agree for
a multi-word title, which is *why* the link is dead in the first place, and
is exactly what fragcheck.py's own `squash()` helper is for (reused here, not
reimplemented). A working cross-page link (e.g. `Group_PSI_v1.md#psi_mutex_
info_v1-1`, a real anchored member) is never touched: squash-matching only
fires against the target's OWN title, and only when that title is genuinely
what the link's fragment reduces to. Same-page links (bare `#frag`, no
filename) are untouched; only `file.md#frag` cross-page links are candidates
at all. This is a pointer fix, not a reinterpretation of moxygen's headings
or prose.

Usage: fix_plugin_api_breadcrumb_links.py [base_dir]
  base_dir defaults to "." (the mariadb-docs repo root).
"""
import importlib.util
import pathlib
import re
import sys

LINK = re.compile(r'\]\(([^)#]+\.md)#([^)]+)\)')


def load_fragcheck(repo_root):
    spec = importlib.util.spec_from_file_location(
        'fragcheck', repo_root / '.claude' / 'hooks' / 'fragcheck.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def own_title_squashes(dest_dir, fragcheck):
    """{filename: squash(that file's own H1 title)}."""
    squashes = {}
    for page in sorted(dest_dir.glob('*.md')):
        h1 = next((text for _, level, text, _ in fragcheck.headings_of(page)
                   if level == 1), None)
        if h1:
            squashes[page.name] = fragcheck.squash(fragcheck.strip_inline(h1))
    return squashes


def fix_file(page, title_squash, fragcheck):
    text = page.read_text()

    def repl(m):
        fname, frag = m.group(1), m.group(2)
        if fname in title_squash and fragcheck.squash(frag) == title_squash[fname]:
            return f']({fname})'
        return m.group(0)

    fixed = LINK.sub(repl, text)
    if fixed != text:
        page.write_text(fixed)
        return True
    return False


def main():
    base_dir = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else '.')
    dest_dir = base_dir / 'server' / 'reference' / 'plugins' / 'api-plugin'
    assert dest_dir.is_dir(), f'not a directory: {dest_dir}'

    fragcheck = load_fragcheck(base_dir)
    title_squash = own_title_squashes(dest_dir, fragcheck)

    for page in sorted(dest_dir.glob('*.md')):
        if fix_file(page, title_squash, fragcheck):
            print(f'stripped dead breadcrumb fragment(s): {page.name}')


if __name__ == '__main__':
    main()
