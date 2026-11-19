#!/usr/bin/env python3
"""Turn the GitHub alerts in the generated Plugin API pages into GitBook hints.

`generate_plugin_api_docs.sh` runs moxygen with `--flavour=github`, so a
Doxygen `@note` or `@warning` comes out as a GitHub alert:

    > [!WARNING]
    > Status variables are not automatically prefixed ...

GitBook has no alert syntax. It renders the block as a plain quote that
starts with the literal text "[!WARNING]", and when it exports the page back
to Git it escapes the marker to `> \\[!WARNING]` and joins the first body line
onto it (DOCS-7041). This step rewrites each alert as a hint:

    {% hint style="warning" %}
    Status variables are not automatically prefixed ...
    {% endhint %}

Both marker forms are recognized, `[!X]` and `\\[!X]`, indented by up to
three spaces as Markdown allows, with the body on the
following `>` lines, on the marker line itself, or both. The body is copied
unchanged apart from its `> ` quote prefix, so code fences inside a note keep
their content. An alert with no body is removed: a Doxygen `@note` followed by
a blank line ends the note before its text, and moxygen then emits an empty
alert with the text as an ordinary paragraph below it. Lines inside fenced
code blocks outside a quote are never touched.

Usage: fix_plugin_api_alerts.py [base_dir]
  base_dir defaults to "." (the mariadb-docs repo root).
"""
import pathlib
import re
import sys

STYLES = {
    'NOTE': 'info',
    'TIP': 'success',
    'IMPORTANT': 'info',
    'WARNING': 'warning',
    'CAUTION': 'danger',
}
MARKER = re.compile(
    r'^( {0,3})>[ \t]?\\?\[!(' + '|'.join(STYLES) + r')\\?\][ \t]*(.*)$')
QUOTE = re.compile(r'^ {0,3}>')
FENCE = re.compile(r'^[ \t]*(```|~~~)')


def unquote(line):
    """Strip one blockquote level: '  > x' -> 'x', '>' -> ''."""
    line = line.lstrip(' ')[1:]
    return line[1:] if line.startswith(' ') else line


def convert(text):
    lines = text.split('\n')
    out = []
    in_fence = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if FENCE.match(line):
            in_fence = not in_fence
        # A marker only opens an alert on the first line of a blockquote.
        starts_quote = i == 0 or not QUOTE.match(lines[i - 1])
        m = None if in_fence or not starts_quote else MARKER.match(line)
        if not m:
            out.append(line)
            i += 1
            continue

        style = STYLES[m.group(2)]
        body = [m.group(3)] if m.group(3) else []
        i += 1
        while i < len(lines) and QUOTE.match(lines[i]):
            body.append(unquote(lines[i]))
            i += 1
        while body and not body[0].strip():
            body.pop(0)
        while body and not body[-1].strip():
            body.pop()
        body = [b.rstrip() for b in body]

        if body:
            out.append(f'{{% hint style="{style}" %}}')
            out.extend(body)
            out.append('{% endhint %}')
        elif out and not out[-1].strip() and i < len(lines) \
                and not lines[i].strip():
            # Empty alert between two blank lines: drop one blank line too,
            # so the paragraphs around it stay one blank line apart.
            i += 1
    return '\n'.join(out)


def fix_file(page):
    text = page.read_text()
    fixed = convert(text)
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
        print(f'converted alerts: {page}')
    print(f'{len(changed)} file(s) changed')


if __name__ == '__main__':
    main()
