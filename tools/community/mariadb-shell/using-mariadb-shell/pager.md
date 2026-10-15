---
description: >-
  Page long query results and help text in MariaDB Shell through less, more,
  or another program with --pager, the pager command, the PAGER variable, and
  shell.enable_pager.
---

# Pager

A pager is a program, such as `less` or `more`, that shows long output one screen at a time. MariaDB Shell can send output to a pager so that a wide or long result doesn't scroll past. The pager is off by default and works only in interactive sessions.

## What Goes Through the Pager

When a pager is set, the shell sends it:

* The results of SQL statements that return rows, in SQL mode and from `\sql <statement>` in Python mode.
* The output of `\help`.
* All text output in Python mode, but only after you call `shell.enable_pager()`. See [Paging Python Output](#paging-python-output).

Each statement or help request is paged separately. When you quit the pager, the shell shows the prompt again.

## Setting the Pager

The pager command is held in the `pager` shell option. Its value is a command line, so it can include options for the pager program. An empty value means no pager.

| Method | Scope |
| --- | --- |
| `PAGER` environment variable | Sets the pager at startup when neither `--pager` nor a persisted `pager` option sets it. |
| `--pager=<command>` | Sets the pager for the session. |
| `\option --persist pager <command>` | Sets the pager for this and future sessions. |
| `\pager <command>` or `\P <command>` | Changes the pager during the session. |
| `\nopager` | Turns the pager off for the rest of the session. |

```sh
mariadb-shell --pager="less -SFX" mariadb://dba@localhost/shop
```

For results, `less -SFX` works well: `-S` keeps long lines unwrapped so that table rows stay aligned and you can scroll sideways with the arrow keys, `-F` exits right away when the output fits on one screen, and `-X` leaves the output on the screen after you quit.

## Changing the Pager During a Session

`\pager` (or `\P`) takes the pager command as the rest of the line. Quotes are optional:

```text
MariaDB localhost:3306 ssl  shop  SQL > \pager less -S
Pager has been set to 'less -S'.
MariaDB localhost:3306 ssl  shop  SQL > \pager "more -10"
Pager has been set to 'more -10'.
```

`\pager` without an argument, or with an empty string (`\pager ""`), restores the pager that was in effect when the shell started. `\nopager` turns paging off:

```text
MariaDB localhost:3306 ssl  shop  SQL > \nopager
Pager has been disabled.
```

Both commands change the `pager` option for the current session only. To keep a pager, persist the option:

```text
MariaDB localhost:3306 ssl  shop  SQL > \option --persist pager "less -SFX"
```

The pager can be any program that reads standard input. For example, `\pager cat -n` numbers the output lines, and `\pager tee -a /tmp/session.log` appends results to a file while still showing them:

```text
MariaDB localhost:3306 ssl  shop  SQL > \pager cat -n
Pager has been set to 'cat -n'.
MariaDB localhost:3306 ssl  shop  SQL > SELECT name FROM product\G
     1	*************************** 1. row ***************************
     2	name: Desk lamp
     3	*************************** 2. row ***************************
     4	name: Office chair
     5	*************************** 3. row ***************************
     6	name: Notebook
     7	3 rows in set (0.0002 sec)
```

## Paging Python Output

In Python mode, output isn't paged automatically, because scripts often print progress messages line by line. To page the output of a long report or a loop, turn the pager on with `shell.enable_pager()` and off with `shell.disable_pager()`:

```python
shell.enable_pager()
for row in session.run_sql("SELECT table_schema, table_name, table_rows "
                           "FROM information_schema.tables "
                           "ORDER BY table_rows DESC").fetch_all():
    print(f"{row[0]}.{row[1]}: {row[2]}")
shell.disable_pager()
```

Between the two calls, all text output except prompts goes to the pager in the `pager` option. Notes:

* If you change the `pager` option while paging is on, the new pager is used from then on.
* If the `pager` option is empty, `enable_pager()` has no visible effect until you set a pager.
* Switching to SQL mode turns Python paging off, as if you had called `disable_pager()`.
* `disable_pager()` doesn't change the `pager` option, so SQL results are still paged.
* Both functions have no effect in batch mode.
