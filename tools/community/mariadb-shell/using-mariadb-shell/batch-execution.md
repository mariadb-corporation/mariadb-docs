---
description: >-
  Run SQL and Python non-interactively with MariaDB Shell: script files,
  standard input, -e, -c, and --pym, script arguments, error handling, and
  exit codes.
---

# Batch Execution

MariaDB Shell runs scripts without a prompt as well as interactively. Use batch execution in cron jobs, deployment scripts, and CI pipelines, or anywhere you would otherwise run the `mariadb` client with a file.

| Method | Example | Mode |
| --- | --- | --- |
| Script file | `mariadb-shell <URI> -f load.sql` | From the file extension. |
| Standard input | `mariadb-shell <URI> --sql < load.sql` | The starting mode. |
| One statement | `mariadb-shell <URI> -e "SELECT ..."` | The starting mode. |
| One Python command | `mariadb-shell <URI> -c "print(...)"` | Python. |
| Python module | `mariadb-shell <URI> --pym mymodule` | Python. |

The starting mode is SQL unless you add `--py`, or persist the `defaultMode` option. See [SQL and Python Modes](sql-and-python-modes.md#choosing-the-mode).

## Running a Script File

`-f` (`--file`) runs a file and exits. The file extension selects the mode:

| Extension | Mode |
| --- | --- |
| `.sql` | SQL |
| `.py` | Python |
| Any other | The starting mode, SQL unless you add `--py`, or set `defaultMode`. |

```sh
mariadb-shell mariadb://dba@db1.example.com/shop -f /opt/scripts/nightly_cleanup.sql
mariadb-shell mariadb://dba@db1.example.com/shop -f /opt/scripts/price_report.py
```

SQL files can contain several statements, comments, and `DELIMITER` changes for stored programs.

{% hint style="warning" %}
`-f` must be the last shell option. Everything after the file name is passed to the script as arguments, including words that look like shell options. Put the URI and all other options before `-f`.
{% endhint %}

### Script Arguments

Arguments after the file name are available to a Python script in `sys.argv`. `sys.argv[0]` is the script name:

{% code title="price_report.py" %}
```python
import sys

threshold = float(sys.argv[1]) if len(sys.argv) > 1 else 0
res = session.run_sql("SELECT name, price FROM product WHERE price > ?", [threshold])
for row in res.fetch_all():
    print(f"{row.name}\t{row.price}")
```
{% endcode %}

```sh
mariadb-shell mariadb://dba@localhost/shop -f price_report.py 20 --verbose
```

Here `sys.argv` is `['price_report.py', '20', '--verbose']`. SQL files don't receive arguments.

## Reading from Standard Input

When standard input isn't a terminal, the shell reads statements from it and exits at the end of the input. Choose the mode with `--sql` or `--py`, because no file name tells the shell which one to use:

```sh
mariadb-shell mariadb://dba@localhost/shop --sql < schema_changes.sql
gunzip -c shop_backup.sql.gz | mariadb-shell mariadb://dba@localhost/shop --sql
```

Python code works the same way, including compound statements, which end at the first line that isn't indented:

```sh
mariadb-shell mariadb://dba@localhost/shop --py < housekeeping.py
```

## Running One Statement

`-e` (`--execute`) runs the given text and exits. The text runs in the starting mode, so it's SQL by default. Add `--py` for Python:

```sh
mariadb-shell mariadb://dba@localhost/shop -e "SELECT COUNT(*) AS products FROM product"
mariadb-shell mariadb://dba@localhost/shop --py -e "print(session.get_server_vendor())"
```

The text can contain several SQL statements separated by `;`. `-e` can't be combined with `-f` or `--pym`.

## Running Python Commands and Modules

`-c` (`--pyc`) runs a Python command and exits, like `python -c`. Arguments after the command are passed in `sys.argv`, with `sys.argv[0]` set to `-c`:

```sh
mariadb-shell mariadb://dba@localhost/shop -c "import sys; print(sys.argv[1:])" alpha beta
```

`--pym` runs a Python module as a script, like `python -m`. The module is searched on the shell's Python path, which includes the modules bundled with the shell and the directories in `PYTHONPATH`. Arguments after the module name are passed in `sys.argv`, with `sys.argv[0]` set to the module name. If you also give a URI, the module can use the global `session`:

```sh
mariadb-shell --pym pip list
PYTHONPATH=/opt/dbtools mariadb-shell mariadb://dba@localhost/shop --pym shopreport --since 2026-01-01
```

As with `-f`, put all shell options before `-c` or `--pym`. See [Python Module Search Paths](../customizing/python-module-search-paths.md).

## Output in Batch Mode

In batch mode, results are printed in the `tabbed` format: a header line with the column names, then one line per row with tab-separated values. Row counts, timings, and warnings aren't printed, so other tools can process the output directly:

```sh
$ mariadb-shell mariadb://dba@localhost/shop -e "SELECT id, name FROM product"
id	name
1	Desk lamp
2	Office chair
3	Notebook
```

Use `--table`, `-E` (`--vertical`), `--json`, or `--result-format` to choose another format. Errors and messages go to standard error, results to standard output. See [Output Formats](output-formats.md).

## Shell Commands in Scripts

Batch input is passed to SQL or Python as it is: shell commands such as `\use` or `\option` aren't processed, and an SQL script that contains one fails at that line with a syntax error. The statement terminators `\G` and `\g` are an exception and work in batch mode. In SQL mode, the `source` and `DELIMITER` lines of the `mariadb` client are also processed.

To process shell commands, add `-i` (`--interactive`). The shell then handles each line as if you had typed it at the prompt: shell commands work, results are printed in table format with row counts, and warnings are shown. With `--interactive=full`, the shell also prints the prompt and echoes each line, which produces a transcript of the session:

```sh
mariadb-shell mariadb://dba@localhost/shop --interactive=full -f session_demo.sql
```

To change options in a non-interactive Python script, use `shell.options` instead of `\option`, for example `shell.options["resultFormat"] = "json"`.

## Error Handling

By default, an SQL script stops at the first statement that fails. The error, including the line number, goes to standard error:

```text
ERROR: 1146 (42S02) at line 2: Table 'shop.nosuch' doesn't exist
```

`--force` makes the shell report the error and continue with the next statement. It applies to SQL in files and on standard input:

```sh
mariadb-shell mariadb://dba@localhost/shop --force -f optional_indexes.sql
```

In Python scripts, an uncaught exception stops the script and prints the traceback. Use `try` and `except` to handle errors in Python.

## Exit Codes

| Exit code | Meaning |
| --- | --- |
| `0` | Success. With `--force`, also when SQL statements failed. |
| `1` | An error stopped the script, the connection failed, or the file couldn't be opened. |
| *n* | A Python script ended with `sys.exit(n)` or `raise SystemExit(n)`. |
| `10` | Invalid arguments in a [command line integration](command-line-integration.md) call. |
| `130` | Interrupted with **Ctrl+C**. On Linux and macOS, the shell ends through `SIGINT`, which the calling shell reports as `130`. |

```sh
if ! mariadb-shell mariadb://dba@localhost/shop -f migrate.sql; then
  echo "Migration failed" >&2
  exit 1
fi
```

## Passwords in Batch Mode

A batch job can't answer a password prompt. Use one of these methods instead of putting the password on the command line, where other users can see it in the process list:

* Store the password in the credential store. See [Credential Store](../connecting/credential-store.md).
* Put the password in an option file in the `[mariadb-shell]` or `[client]` group, readable only by the job's user.
* Use `--passwords-from-stdin`. The shell then reads each password it needs as one line from standard input instead of the terminal, and reads the rest of the input as statements:

```sh
printf '%s\n' "$DB_PASSWORD" | mariadb-shell dba@db1.example.com:3306 \
  --passwords-from-stdin --save-passwords=never --sql -e "SELECT CURRENT_USER()"
```

With `--save-passwords=never`, the shell doesn't offer to store the password in the credential store.

## Startup Messages

In interactive and `-i` sessions, the shell prints a welcome banner and connection details at startup. `--quiet-start` removes them:

| Value | Effect |
| --- | --- |
| `--quiet-start` or `--quiet-start=1` | Omits the version and copyright banner, keeps the connection messages. |
| `--quiet-start=2` | Omits everything except errors. |
