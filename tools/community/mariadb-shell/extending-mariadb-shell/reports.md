---
description: >-
  Run the built-in reports with the show and watch commands, call them from Python, and
  write your own reports with shell.register_report().
---

# Reports

A report is a named function that collects information from the server and hands it to the shell for display. You run a report once with `\show`, or repeatedly with `\watch`, which refreshes the screen until you press Ctrl+C. MariaDB Shell ships three reports, `query`, `thread`, and `threads`, and you can register your own in Python.

## Running Reports

The `\show` and `\watch` commands work in both SQL and Python mode and need an open global session.

```text
\show <report> [options] [arguments]
\watch <report> [options] [arguments]
```

* Report names are case-insensitive, and `-` and `_` are interchangeable, so `\show table-sizes` runs the `table_sizes` report.
* Put the options before the arguments. Everything after the first argument is treated as an argument.
* Without a report name, both commands list the available reports.
* `\show <report> --help` displays the options and arguments of a report.

The following options apply to every report:

| Option | Command | Description |
| --- | --- | --- |
| `--help`, `-h` | `\show`, `\watch` | Displays the help of the report. |
| `--vertical`, `-E` | `\show`, `\watch` | Displays the rows of a `list` report vertically, one line per column. |
| `--interval=<seconds>`, `-i <seconds>` | `\watch` | The time between refreshes. The default is 2 seconds, and the allowed range is 0.1 to 86400. |
| `--nocls` | `\watch` | Keeps the previous output instead of clearing the screen before each refresh. |

For example, to watch the number of open connections every half second without clearing the screen:

```text
MariaDB localhost:3306 ssl  SQL > \watch query --interval=0.5 --nocls SHOW GLOBAL STATUS LIKE 'Threads_connected'
```

## Calling Reports from Python

Every report, built-in or registered, is also a method of the `shell.reports` object. The method takes the session, a list of arguments, and a dictionary of options, and returns a dictionary whose `report` key holds the data:

```text
MariaDB localhost:3306 ssl  Py > shell.reports.query(session, ["SELECT COUNT(*) AS n FROM sakila.film"])
{
    "report": [
        [
            "n"
        ],
        [
            1000
        ]
    ]
}
```

When you call a report as a function, use the long option names as dictionary keys, with underscores instead of dashes, for example `{"prep_stmts": True}`. The short forms such as `-P` work only with `\show` and `\watch`. To read the help of a report, run `shell.reports.help("thread")` or `\? shell.reports.thread`.

## Built-in Reports

### query

The `query` report runs the SQL statement that you pass as its arguments and displays the result as a table. It's most useful with `\watch`, to rerun a monitoring query at a fixed interval:

```text
MariaDB localhost:3306 ssl  SQL > \watch query -i 5 SELECT id, user, time, state FROM information_schema.processlist WHERE command <> 'Sleep'
```

The report accepts `--vertical` and, with `\watch`, the refresh options.

### thread

The `thread` report displays information about one server thread, by default the thread of the current connection. It reads `performance_schema` tables and `sys` schema functions.

{% hint style="warning" %}
MariaDB Server starts with the Performance Schema disabled. When `performance_schema` is `OFF`, the `thread` report fails with `The specified thread does not exist.` Enable the Performance Schema with `performance_schema=ON` in the server option file and restart the server.
{% endhint %}

| Option | Short | Description |
| --- | --- | --- |
| `--tid=<id>` | `-t` | Reports on the thread with this Performance Schema thread ID. |
| `--cid=<id>` | `-c` | Reports on the thread of this connection ID, the ID that `SHOW PROCESSLIST` and `CONNECTION_ID()` return. |
| `--general` | `-G` | Basic information: user, host, command, state, transaction state, and the current and previous statement. This is the default when you give no other option. |
| `--brief` | `-B` | A one-line summary of the thread. |
| `--client` | `-C` | The client program, its connection attributes, the protocol, the socket, and the TLS cipher and version. |
| `--innodb` | `-I` | The InnoDB transaction of the thread. |
| `--locks` | `-L` | InnoDB and metadata locks that block the thread or that the thread blocks. |
| `--prep-stmts` | `-P` | The prepared statements that the thread has allocated. |
| `--status[=<prefixes>]` | `-S` | Session status variables, optionally only those whose names start with one of the comma-separated prefixes. |
| `--user-vars[=<prefixes>]` | `-U` | User-defined variables, optionally filtered by prefix. |
| `--vars[=<prefixes>]` | `-V` | Session system variables, optionally filtered by prefix. |
| `--raw-locks` | `-R` | Low-level lock information. |
| `--all` | `-A` | All of the above. |

On MariaDB Server, `--vars`, `--raw-locks`, and `--all` fail, because they read the `performance_schema.variables_by_thread` and `performance_schema.data_locks` tables, which MariaDB Server doesn't have. Use the other options individually instead.

```text
MariaDB localhost:3306 ssl  SQL > \show thread --cid 42 --client --status=Bytes,Ssl
```

### threads

The `threads` report lists the threads of the current user, or all foreground or background threads, with selectable columns (`--format`), sorted by any of them (`--order-by`, `--desc`) and limited in number (`--limit`). Run `\show threads --help` for the columns.

```text
MariaDB localhost:3306 ssl  SQL > \show threads --all --format=tid,name,type --limit=3
```

`--where` keeps the rows that match a condition. A condition compares a column with a value or another column, using `=`, `!=`, `<>`, `<`, `<=`, `>`, `>=`, `LIKE` or `NOT LIKE`, and combines comparisons with `AND`, `OR`, `NOT` and parentheses. `NOT` applies to the whole comparison that follows it, as in SQL. Keywords are case-insensitive, and strings are quoted with `'` or `"`:

```text
MariaDB localhost:3306 ssl  SQL > \show threads --all --where "tid > 10 AND name LIKE '%innodb%'"
```

Other operators, such as `IS`, `IN` or `BETWEEN`, are refused with `Disallowed operator`, and a name that isn't a column of the report with `Unknown column name`.

{% hint style="warning" %}
* The report reads `performance_schema`, which is off by default in MariaDB Server. Without `performance_schema=ON`, it returns no rows.
* The `system.<variable>` columns need `performance_schema.variables_by_thread`, which MariaDB Server doesn't have, so requesting one fails.
* Without `--foreground`, `--background` or `--all`, the report lists the threads whose user and host match the ones the session connected with. A session that connected to `127.0.0.1` lists nothing when the server records the connection as coming from `localhost`.
{% endhint %}

## Writing a Report

You register a report with `shell.register_report()`:

```python
shell.register_report(name, type, report, description)
```

| Parameter | Description |
| --- | --- |
| `name` | The report name. It must be a valid Python identifier, and unique without regard to case. |
| `type` | `list`, `report`, or `print`. The type defines what the function returns and how `\show` displays it. |
| `report` | The Python function that produces the report. |
| `description` | Optional. A dictionary with the help text, options, and arguments of the report. |

After registration, the report is available to `\show` and `\watch` and as `shell.reports.<name>()`. Registering a name that already exists raises an error.

### Report Types

| Type | The function returns | `\show` displays |
| --- | --- | --- |
| `list` | `{"report": [header, row, row, ...]}`, where `header` is a list of column names and each row is a list of values. | A table, or vertical output with `--vertical`. |
| `report` | `{"report": [document]}`, a list with a single dictionary or list. | The document as YAML. |
| `print` | `{"report": []}`. The function prints its own output. | Nothing beyond what the function prints. |

### The Report Function

The shell calls the function with up to three positional arguments: the session, the list of arguments, and the dictionary of options. It passes the argument list only when the report accepts arguments or options, and the options dictionary only when the report defines options. To write a function that works in every case, give the last two parameters default values:

```python
def my_report(session, argv=None, options=None):
    ...
```

The function must return a dictionary with a `report` key. If it raises an exception, `\show` prints the exception message.

### The Description Dictionary

| Key | Type | Description |
| --- | --- | --- |
| `brief` | string | A one-line description, shown in the help. |
| `details` | list of strings | Paragraphs of detailed help. |
| `argc` | string | The number of arguments the report accepts: an exact number such as `"1"`, `"*"` for any number, a range such as `"0-2"`, or an open range such as `"1-*"`. Without `argc`, the report accepts no arguments. |
| `options` | list of dictionaries | The options of the report. Without `options`, the report accepts none. |
| `examples` | list of dictionaries | Usage examples for the help. Each has a `description` and, optionally, `args` (a list of strings) and `options` (a dictionary of strings). |

Each option dictionary accepts these keys:

| Key | Type | Description |
| --- | --- | --- |
| `name` | string | Required. The long option name (`--name`), and the dictionary key when the report is called as a function. It must be a valid identifier. |
| `shortcut` | string | A single alphanumeric character for the short form (`-n`), available only with `\show` and `\watch`. |
| `brief` | string | A one-line description. |
| `details` | list of strings | Additional help paragraphs. |
| `type` | string | `string` (default), `integer`, `float`, or `bool`. A `bool` option is a switch: it's `False` unless given, and takes no value on the `\show` command line. |
| `required` | bool | Whether the option must be given. A `bool` option can't be required. |
| `values` | list of strings | The allowed values of a `string` option. |
| `empty` | bool | Whether a `string` option accepts an empty value. The default is `False`. |

## Loading Reports at Startup

To have a report in every session, register it in a [plugin](plugins.md). Create a directory for it in the `plugins` directory of the user configuration directory, and put the registration code in its `init.py` file:

```text
~/.mariadb-shell/plugins/
└── table_sizes/
    └── init.py
```

On Windows, the directory is `%AppData%\MariaDB\mariadb-shell\plugins\`. The shell loads the plugin at every startup, whatever the mode, so the report is also available to `\show` and `\watch` in SQL mode. A plugin directory can be shared with other users as it is, or installed from a repository with the `plugins` global object. See [Plugins](plugins.md).

As an alternative, the shell runs every `.py` file in the `init.d` directory of the user configuration directory (`~/.mariadb-shell/init.d/`, or `%AppData%\MariaDB\mariadb-shell\init.d\` on Windows) at startup, before it loads plugins. Each file runs in its own namespace, and the files also run when you start the shell with `--disable-plugins`. If a file fails, the shell prints a warning at startup and writes the details to the [log file](../logging-and-debugging.md).

## Example: Largest Tables

The following `list` report shows the largest tables of a schema. It accepts an optional schema name and a `--limit` option.

{% code title="~/.mariadb-shell/plugins/table_sizes/init.py" %}
```python
def table_sizes(session, argv=None, options=None):
    """Lists the largest tables of a schema."""
    schema = argv[0] if argv else session.run_sql("SELECT DATABASE()").fetch_one()[0]
    if schema is None:
        raise Exception("Name a schema or select a default schema first.")
    limit = (options or {}).get("limit") or 10

    result = session.run_sql(
        "SELECT table_name, engine, table_rows, "
        "       COALESCE(data_length + index_length, 0) "
        "FROM information_schema.tables "
        "WHERE table_schema = ? AND table_type = 'BASE TABLE' "
        "ORDER BY 4 DESC LIMIT ?", [schema, limit])

    rows = [["table", "engine", "rows", "size"]]
    for name, engine, n, size in result.fetch_all():
        rows.append([name, engine, n, f"{int(size) / 1048576:.2f} MiB"])
    return {"report": rows}


shell.register_report(
    "table_sizes", "list", table_sizes,
    {
        "brief": "Lists the largest tables of a schema.",
        "details": ["Sizes come from information_schema.tables and are estimates.",
                    "Without an argument, the report uses the default schema."],
        "argc": "0-1",
        "options": [
            {"name": "limit", "shortcut": "l", "type": "integer",
             "brief": "Maximum number of tables to list (default 10)."}
        ],
        "examples": [
            {"description": "List the five largest tables in sakila.",
             "args": ["sakila"], "options": {"limit": "5"}}
        ],
    })
```
{% endcode %}

After you restart the shell, run the report:

```text
MariaDB localhost:3306 ssl  SQL > \show table_sizes -l 3 sakila
+-----------+--------+-------+----------+
| table     | engine | rows  | size     |
+-----------+--------+-------+----------+
| rental    | InnoDB | 16008 | 2.52 MiB |
| payment   | InnoDB | 16086 | 2.08 MiB |
| inventory | InnoDB | 4581  | 0.34 MiB |
+-----------+--------+-------+----------+
```

From Python, call the same report with an options dictionary:

```python
shell.reports.table_sizes(session, ["sakila"], {"limit": 3})
```

## Example: Report and Print Types

A `report` report returns one document, which `\show` renders as YAML with the keys sorted. A `print` report prints its own output and returns an empty list. Neither of the following reports takes arguments or options, so the shell calls them with the session only.

```python
def server_summary(session, argv=None, options=None):
    row = session.run_sql(
        "SELECT @@hostname, @@port, VERSION(), @@innodb_buffer_pool_size, "
        "       (SELECT COUNT(*) FROM information_schema.schemata)").fetch_one()
    return {"report": [{
        "host": row[0],
        "port": row[1],
        "version": row[2],
        "innodb": {"buffer_pool_mib": int(row[3]) // 1048576},
        "schemas": row[4],
    }]}


def uptime(session, argv=None, options=None):
    seconds = int(session.run_sql("SHOW GLOBAL STATUS LIKE 'Uptime'").fetch_one()[1])
    days, rest = divmod(seconds, 86400)
    hours, rest = divmod(rest, 3600)
    minutes, seconds = divmod(rest, 60)
    print(f"Up {days}d {hours:02}:{minutes:02}:{seconds:02}")
    return {"report": []}


shell.register_report("server_summary", "report", server_summary,
                      {"brief": "Shows a short summary of the server."})
shell.register_report("uptime", "print", uptime,
                      {"brief": "Prints the server uptime."})
```

```text
MariaDB localhost:3306 ssl  SQL > \show server_summary
---
host: db1
innodb:
  buffer_pool_mib: 128
port: 3306
schemas: 6
version: 11.8.3-MariaDB
MariaDB localhost:3306 ssl  SQL > \show uptime
Up 3d 04:17:52
```
