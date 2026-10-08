# Cookbook: Claude Code status line

Claude Code can render a one-line **status line** under the prompt. Roel's script shows, at a
glance, where you are and what a session is costing:

```
~/mariadb-docs | 298aa97a | 150k/1M | Opus 4.8 (high) | $1.23
```

Left to right: **current directory** (with `~` for home) · **session id** (first 8 chars) ·
**context used / window size** · **model (reasoning effort)** · **session cost**. The
context figure changes color as it fills — orange past 300k, red past 500k, bold red past
750k — so you notice you're approaching a compaction before it happens.

This is a **per-machine** setup: the status line is a local Claude Code setting, not something
that syncs through the repo or Google Drive. Each person installs it once per machine. The
script originated in the internal Claude-at-MariaDB wiki quickstart appendix (thanks, Roel).

## Install

Two steps, both under `~/.claude/`.

### 1. Save the script

Save the following as `~/.claude/claude_statusline.py`:

```python
#!/usr/bin/env python3
# Claude Code status line: cwd | session | context used/max | model (effort) | cost
# Example output: ~/mariadb-docs | 298aa97a | 150k/1M | Opus 4.8 (high) | $1.23
# Install in ~/.claude/settings.json:
#   "statusLine": { "type": "command", "command": "python3 ~/.claude/claude_statusline.py" }

import json
import os
import sys

def tokens(n):
  if n >= 1000000:
    return f'{n / 1000000:.1f}'.rstrip('0').rstrip('.') + 'M'
  if n >= 1000:
    return f'{round(n / 1000)}k'
  return str(n)

try:
  data = json.load(sys.stdin)
except Exception:
  sys.exit(0)

parts = []

cwd = data.get('workspace', {}).get('current_dir') or data.get('cwd') or ''
home = os.path.expanduser('~')
if cwd == home:
  cwd = '~'
elif cwd.startswith(home + os.sep):
  cwd = '~' + cwd[len(home):]
if cwd:
  parts.append(cwd)

session = (data.get('session_id') or '')[:8]
if session:
  parts.append(session)

ctx = data.get('context_window') or {}
used = ctx.get('total_input_tokens')
size = ctx.get('context_window_size')
if used is not None and size:
  text = f'{tokens(used)}/{tokens(size)}'
  if used > 750000:
    text = f'\033[1;38;5;196m{text}\033[0m'  # bold red
  elif used > 500000:
    text = f'\033[38;5;196m{text}\033[0m'  # red
  elif used > 300000:
    text = f'\033[38;5;208m{text}\033[0m'  # orange
  parts.append(text)

model = (data.get('model') or {}).get('display_name', '')
effort = (data.get('effort') or {}).get('level')
if model:
  parts.append(f'{model} ({effort})' if effort else model)

cost = (data.get('cost') or {}).get('total_cost_usd')
if cost is not None:
  parts.append(f'${cost:.2f}')

print(' | '.join(parts))
```

It reads Claude Code's status JSON from stdin, needs only the Python 3 standard library, and
prints nothing (exits cleanly) if the input isn't what it expects — so a Claude Code change
never breaks your prompt.

### 2. Point Claude Code at it

Add this block to `~/.claude/settings.json` (merge it in; don't clobber existing keys):

```json
{
  "statusLine": {
    "type": "command",
    "command": "python3 ~/.claude/claude_statusline.py"
  }
}
```

Restart Claude Code (or start a new session). The status line appears under the prompt.

## Notes

- **Per machine.** Repeat both steps on each machine you use. Nothing here is synced.
- **`python3` must be on `PATH`.** It is on stock macOS; on Linux install the `python3`
  package if it's missing. No third-party modules are required.
- **Customizing.** The output is just the `' | '.join(parts)` at the end — drop a field by
  removing its `parts.append(...)`, or reorder them. The color thresholds are the `used > …`
  numbers in the context block.
- **Field reference.** For the full list of fields Claude Code passes on stdin (and other
  `statusLine` options), see the Claude Code status-line docs:
  <https://code.claude.com/docs/en/statusline>.

## Checklist

- [ ] `~/.claude/claude_statusline.py` saved.
- [ ] `statusLine` block added to `~/.claude/settings.json` (existing keys preserved).
- [ ] `python3` resolves on `PATH`.
- [ ] New session started; status line shows cwd · session · context · model · cost.
- [ ] Repeated on each machine you use.
