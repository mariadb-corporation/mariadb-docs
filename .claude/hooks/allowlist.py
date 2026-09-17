#!/usr/bin/env python3
"""allowlist.py — the checked-in acknowledgment register for doc-lint's two
acknowledgeable guards, and the ONLY parser for it.

WHY A FILE AND NOT AN ENVIRONMENT VARIABLE
    The orphaned-page guard (navcheck.py) and the net line-loss guard
    (shrinkcheck.py) both have legitimate exceptions -- a `hidden: true` page is
    correctly unlisted, and a landing page whose children were retired correctly
    loses most of its lines -- so both are meant to be ACKNOWLEDGED rather than
    disabled. Until now the only way to acknowledge one was DOC_LINT_ALLOW_ORPHAN
    or DOC_LINT_ALLOW_SHRINK, which is fine for a local hook and useless in CI:
    no PR author can set an environment variable on a workflow from a branch.
    That is what blocked the two CI gates in DOCS-6586 for ten days.

    Decided on the ticket (Daniel Bartholomew, 2026-09-14): a checked-in
    allowlist file, because it puts the acknowledgment where review already
    happens -- it is a diff line a reviewer sees, with the reason next to it --
    and because doc-lint.sh already asked for "say why in the commit message",
    which a file makes structural instead of advisory. The environment variables
    are KEPT for local use and are unioned with this file; nothing that worked
    before stops working.

FORMAT
    Two sections, because a page can be legitimately unlisted without being
    gutted and vice versa. Every entry needs a `reason`, and the ticket it
    traces to where one exists:

        orphan:
          - path: release-notes/enterprise-server/12.3/whats-new.md
            reason: "unreleased, hidden until beta ships -- DOCS-6391"

        shrink:
          - path: tools/debian/README.md
            reason: "3 of 5 child pages retired -- DOCS-5976"

WHY A HAND-WRITTEN PARSER AND NOT PyYAML
    Every checker in .claude/hooks/ is standard library only, deliberately: they
    run from a pre-commit hook on a contributor's laptop and from a runner that
    installs nothing. PyYAML is not in the standard library, so importing it
    would make the gates depend on a pip install -- and a `try: import yaml`
    with a fallback would mean TWO parsers that can disagree about the same
    file, which is the drift this file exists to avoid.

    So this accepts exactly the shape above and REJECTS everything else with a
    line number, rather than accepting a wider YAML dialect it only half
    understands. Strictness is the safe direction here: a silently misparsed
    entry would mean an acknowledgment that a reviewer can see in the diff and
    the gate cannot, which is worse than a loud error. The file is valid YAML,
    so editors and GitHub still highlight it; it is just a subset.

WHAT IS DELIBERATELY NOT ACCEPTED
    * `all`. The environment variables take it (a local escape hatch for a
      one-off run), but in a checked-in file it would be a permanent, global
      disable of the guard -- exactly what the ticket says this must not become.
    * absolute paths, `..`, backslashes, a leading `./`, and duplicates: all of
      them are ways for an entry to look like it covers a page while matching
      nothing, since both consumers compare against repo-relative posix paths.
    * an entry with no reason, or an empty one. The reason is the whole point.

STALE ENTRIES
    Not handled here -- each guard prunes its own section, because only the
    guard knows what "still true" means. navcheck.py fails on an orphan entry
    whose page is now listed in SUMMARY.md (Daniel's self-pruning requirement)
    or whose page is gone; shrinkcheck.py fails on a shrink entry whose page is
    gone. There is no "un-shrink" signal, so that half cannot self-prune
    further.

MODES
    allowlist.py validate [<file>]   parse and report the counts (exit 2 if bad)
    allowlist.py paths <section>     the paths of one section, one per line
    allowlist.py entries <section>   `<path>\treason` per line, for reporting

Exit: 0 = fine, 2 = the file is malformed or the arguments are.
"""

import os
import pathlib
import sys

REL_PATH = os.path.join('.claude', 'hooks', 'doc-lint-allow.yml')
SECTIONS = ('orphan', 'shrink')


class AllowlistError(Exception):
    """A malformed allowlist. Always carries the line number."""


def repo_root(start='.'):
    """Nearest ancestor that looks like this repo.

    Spelled the same way as navcheck.py and fragcheck.py, and for the same
    reason: the checkers are invoked from the repo root in every real call, but
    the test suite runs them from a sandbox.
    """
    d = pathlib.Path(start).resolve()
    for cand in [d] + list(d.parents):
        if (cand / '.codespellignore').is_file() or (cand / '.git').exists():
            return cand
    return d


def allowlist_path(root=None):
    return pathlib.Path(root or repo_root()) / REL_PATH


def _unquote(value, lineno):
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in '"\'':
        return value[1:-1]
    if value[:1] in '"\'':
        raise AllowlistError(f'line {lineno}: unterminated quote')
    # A bare value must not contain a `#`, which YAML would read as a trailing
    # comment. Rejecting it is cheaper than guessing which half was meant.
    if '#' in value:
        raise AllowlistError(
            f'line {lineno}: `#` in an unquoted value -- quote the value if the '
            f'`#` is part of it, or move the comment to its own line')
    return value


def _check_path(value, lineno, section, seen):
    if not value:
        raise AllowlistError(f'line {lineno}: empty path')
    if value == 'all':
        raise AllowlistError(
            f'line {lineno}: `all` is not accepted in the allowlist file -- it '
            f'would disable the {section} guard for the whole repository, '
            f'permanently. Name the individual paths. (DOC_LINT_ALLOW_'
            f'{section.upper()}=all still works for a one-off local run.)')
    if value.startswith('/') or (len(value) > 2 and value[0].isalpha()
                                 and value[1] == ':'):
        raise AllowlistError(f'line {lineno}: {value!r} is absolute; paths are '
                             f'repo-relative')
    if '\\' in value:
        raise AllowlistError(f'line {lineno}: {value!r} uses backslashes; paths '
                             f'are posix, with `/`')
    if value.startswith('./') or '..' in value.split('/'):
        raise AllowlistError(f'line {lineno}: {value!r} is not normalized; write '
                             f'the plain repo-relative path')
    if value in seen:
        raise AllowlistError(f'line {lineno}: {value!r} is listed twice in the '
                             f'`{section}` section')
    return value


def parse(text):
    """The allowlist as {section: [{'path':..., 'reason':..., 'line': n}]}.

    Raises AllowlistError on anything this does not accept.
    """
    out = {s: [] for s in SECTIONS}
    seen = {s: set() for s in SECTIONS}
    section = None
    entry = None
    # Tracked separately from `out`, because a section that appears twice with
    # no entries the first time would leave `out[name]` empty and slip past a
    # check that looked there.
    opened = set()

    def close():
        if entry is None:
            return
        if not entry.get('reason'):
            raise AllowlistError(
                f'line {entry["line"]}: the entry for {entry["path"]!r} has no '
                f'`reason`. Every acknowledgment needs one, and the ticket it '
                f'traces to where there is one.')
        out[section].append(entry)

    for lineno, raw in enumerate(text.splitlines(), 1):
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        if line.endswith(':') and not line.startswith((' ', '\t', '-')):
            name = line[:-1].strip()
            if name not in SECTIONS:
                raise AllowlistError(
                    f'line {lineno}: unknown section {name!r} (expected '
                    f'{" or ".join(SECTIONS)})')
            if name in opened:
                raise AllowlistError(f'line {lineno}: section {name!r} appears twice')
            close()
            opened.add(name)
            entry, section = None, name
            continue
        if section is None:
            raise AllowlistError(f'line {lineno}: content before any section header')
        if '\t' in line:
            raise AllowlistError(f'line {lineno}: tab indentation; YAML needs spaces')

        stripped = line.lstrip(' ')
        if stripped.startswith('- '):
            close()
            entry = None
            body = stripped[2:].strip()
            key, _, value = body.partition(':')
            if key.strip() != 'path' or not _:
                raise AllowlistError(
                    f'line {lineno}: an entry must start `- path: <repo-relative '
                    f'path>`')
            path = _check_path(_unquote(value, lineno), lineno, section, seen[section])
            seen[section].add(path)
            entry = {'path': path, 'reason': '', 'line': lineno}
            continue

        key, _, value = stripped.partition(':')
        key = key.strip()
        if not _:
            raise AllowlistError(f'line {lineno}: expected `key: value`, got {line.strip()!r}')
        if entry is None:
            raise AllowlistError(f'line {lineno}: `{key}` outside an entry -- an '
                                 f'entry starts with `- path:`')
        if key != 'reason':
            raise AllowlistError(f'line {lineno}: unknown key {key!r} (an entry '
                                 f'takes `path` and `reason`)')
        if entry['reason']:
            raise AllowlistError(f'line {lineno}: duplicate `reason`')
        reason = _unquote(value, lineno)
        if not reason:
            raise AllowlistError(f'line {lineno}: empty `reason`')
        entry['reason'] = reason

    close()
    return out


def load(root=None):
    """The parsed allowlist, or empty sections when the file is absent.

    An absent file means "nothing is acknowledged", which is the fail-closed
    direction and keeps the test sandboxes and a partial checkout working. A
    file that EXISTS and is malformed is an error -- the alternative is reading
    a broken register as an empty one and failing a PR that had acknowledged
    its finding correctly.
    """
    p = allowlist_path(root)
    if not p.is_file():
        return {s: [] for s in SECTIONS}
    return parse(p.read_text(encoding='utf-8', errors='replace'))


def paths(section, root=None):
    """Just the paths of one section, as a set."""
    return {e['path'] for e in load(root)[section]}


def reasons(section, root=None):
    """{path: reason} for one section."""
    return {e['path']: e['reason'] for e in load(root)[section]}


def env_paths(section):
    """The legacy DOC_LINT_ALLOW_* escape hatch, still honoured locally.

    Kept space/comma-separated and still accepts `all`, unlike the file: it is a
    one-off for an interactive run, not a checked-in decision.
    """
    import re
    raw = os.environ.get(f'DOC_LINT_ALLOW_{section.upper()}', '')
    return {t for t in re.split(r'[\s,]+', raw) if t}


def acknowledged(section, root=None):
    """Everything exempt from `section`: the file plus the environment variable.

    Returns (paths, all_flag). `all` can only come from the environment.
    """
    env = env_paths(section)
    return (paths(section, root) | (env - {'all'})), ('all' in env)


def main(argv):
    if len(argv) < 2 or argv[1] in ('-h', '--help'):
        print(__doc__.rstrip(), file=sys.stderr)
        return 2
    mode = argv[1]
    # Named for the error message: `validate <file>` is how the test suite and
    # the workflows point this at a file that is not the repo's own, so the
    # message has to name the file that was actually read.
    target = allowlist_path()
    try:
        if mode == 'validate':
            if len(argv) > 2:
                target = pathlib.Path(argv[2])
                data = parse(target.read_text(encoding='utf-8', errors='replace'))
            else:
                data = load()
            print('allowlist: ' + ', '.join(
                f'{len(data[s])} {s} entr' + ('y' if len(data[s]) == 1 else 'ies')
                for s in SECTIONS))
            return 0
        if mode in ('paths', 'entries'):
            if len(argv) < 3 or argv[2] not in SECTIONS:
                print(f'allowlist: `{mode}` needs a section '
                      f'({" or ".join(SECTIONS)})', file=sys.stderr)
                return 2
            data = load()[argv[2]]
            for e in data:
                if mode == 'paths':
                    print(e['path'])
                else:
                    print(f'{e["path"]}\t{e["reason"]}')
            return 0
    except AllowlistError as exc:
        print(f'allowlist: {target} is malformed -- {exc}', file=sys.stderr)
        print('           The accepted shape is in this script\'s header; it is '
              'a strict\n           subset of YAML, so a wider dialect is a '
              'hard error rather than a\n           half-understood '
              'acknowledgment.', file=sys.stderr)
        return 2
    except OSError as exc:
        print(f'allowlist: {exc}', file=sys.stderr)
        return 2
    print(f'allowlist: unknown mode {mode!r} (expected validate, paths or entries)',
          file=sys.stderr)
    return 2


if __name__ == '__main__':
    sys.exit(main(sys.argv))
