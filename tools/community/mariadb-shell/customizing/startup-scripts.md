---
description: >-
  Run Python code each time MariaDB Shell enters Python mode with
  mariadb-shellrc.py: where the shell looks for it, when it runs, and what to
  put in it.
---

# Startup Scripts

A startup script is a Python file named `mariadb-shellrc.py` that MariaDB Shell runs when it initializes Python mode. Use it to import modules you always need, define helper functions for interactive work, and adjust settings for your Python sessions.

## Where the Shell Looks

The shell checks three locations, in this order, and runs every script it finds. A script that runs later can override what an earlier one defined.

| Order | Location | Purpose |
| --- | --- | --- |
| 1 | `/etc/mysql/mariadb-shell/mariadb-shellrc.py` | System-wide script for all users of the machine. Linux and macOS only. |
| 2 | `share/mariadb-shell/mariadb-shellrc.py` in the installation directory | Script for all users of one installation. |
| 3 | `mariadb-shellrc.py` in the user configuration directory: `~/.mariadb-shell/` on Linux and macOS, `%AppData%\MariaDB\mariadb-shell\` on Windows | Your personal script. |

Notes on these locations:

* On Windows, the shell ignores a system-wide script in `%ProgramData%\MariaDB\mariadb-shell\` and prints a warning, because that directory is writable by all users.
* The installation directory is the parent of the `bin` directory that holds `mariadb-shell`, or the directory that `MARIADB_SHELL_HOME` names. When the executable isn't in a `bin` directory and `MARIADB_SHELL_HOME` isn't set, the shell looks for the script next to the executable instead.
* `MARIADB_SHELL_USER_CONFIG_HOME` changes the user configuration directory, and with it the location of your personal script.
* Empty files are skipped.

## When the Script Runs

The shell runs the startup scripts once per shell process, the first time Python mode is initialized:

* At startup, when the shell starts in Python mode, for example with `--py`, with `-f script.py`, or because the `defaultMode` option is `py`.
* Otherwise, at the first `\py` command.

A session that stays in SQL mode never runs the startup scripts. Code that must be available in every session, such as [reports](../extending-mariadb-shell/reports.md) that you run with `\show` from SQL mode, or [SQL handlers](../extending-mariadb-shell/sql-handlers.md), belongs in the `init.d` directory of the user configuration directory or in a [plugin](../extending-mariadb-shell/plugins.md). Those load at every startup, whatever the mode.

The script runs in the global namespace of the interactive Python session, so the modules it imports and the functions and variables it defines are available at the prompt. This is the main difference from files in `init.d`, which each run in a private namespace.

If the script raises an exception, the shell prints the error and continues to start.

## What to Put in the Script

Good candidates for a startup script:

* Imports you use often, such as `json`, `os`, or `datetime`.
* Small helper functions for interactive use.
* Additions to `sys.path`, so you can import your own modules. See [Python Module Search Paths](python-module-search-paths.md).
* Session-only option changes with `shell.options.set()`. Settings you want everywhere, also in SQL mode, are better stored with `\option --persist`. See [Configuration Options](configuration-options.md).

Avoid opening connections or running long queries in the script: it runs before you get a prompt, and every start would wait for it.

## Example

{% code title="~/.mariadb-shell/mariadb-shellrc.py" %}
```python
import json
import os
import sys

# Make modules in ~/dba-scripts importable.
sys.path.append(os.path.expanduser("~/dba-scripts"))


def q(sql, *args):
    """Runs a statement on the global session and returns all rows."""
    return shell.get_session().run_sql(sql, list(args)).fetch_all()


def show_json(value):
    """Pretty-prints a value as JSON."""
    print(json.dumps(value, indent=2, default=str))


# Show column type information in this shell process, without persisting it.
shell.options.set("showColumnTypeInfo", True)
```
{% endcode %}

With the script in place, the helpers are ready as soon as you switch to Python mode:

```text
MariaDB localhost:3306 ssl  SQL > \py
Switching to Python mode...
MariaDB localhost:3306 ssl  Py > q("SELECT COUNT(*) FROM sakila.rental WHERE return_date IS NULL")
[
    [
        183
    ]
]
```
