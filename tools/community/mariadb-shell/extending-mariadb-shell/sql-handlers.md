---
description: >-
  Intercept SQL statements by prefix with shell.register_sql_handler() and
  answer them with results built by shell.create_result().
---

# SQL Handlers

An SQL handler is a Python function that MariaDB Shell calls instead of sending a statement to the server. You register it with a list of statement prefixes. When a statement starts with one of them, the shell passes the statement to your function, which either returns a result for the shell to display or returns nothing to let the statement go to the server.

SQL handlers let you add statements of your own, such as `SHOW SIZES`, or wrap existing statements with extra checks or logging.

## Registering a Handler

```python
shell.register_sql_handler(name, description, prefixes, callback)
```

| Parameter | Description |
| --- | --- |
| `name` | A unique name for the handler. It can't be empty. |
| `description` | A short description of the statements the handler provides. It can't be empty. |
| `prefixes` | A non-empty list of statement prefixes, such as `["SHOW SIZES"]`. A prefix can't be blank, and it can't overlap with a prefix of another registered handler. |
| `callback` | The function to call for a matching statement. |

To see which handlers are registered, call `shell.list_sql_handlers()`. It returns a list of dictionaries with the keys `name` and `description`.

```text
MariaDB localhost:3306 ssl  Py > shell.list_sql_handlers()
[
    {
        "description": "Adds SHOW SIZES [schema]",
        "name": "tableSizes"
    }
]
```

A handler stays registered until the shell exits. To make it permanent, register it in a file in the `init.d` directory of the user configuration directory, in a [plugin](plugins.md), or in the [startup script](../customizing/startup-scripts.md).

## How Statements Are Matched

* Matching ignores leading white space and comments, treats a run of white space as a single space, and ignores letter case. `show   sizes sakila` and `/* check */ SHOW SIZES` both match the prefix `SHOW SIZES`.
* A prefix matches the start of the text, not whole words: the prefix `SHOW SIZES` also matches `SHOW SIZESX`. Check the statement in your callback if that matters.
* Handlers apply to statements in SQL mode and to statements that Python code runs through a session, such as `session.run_sql()`, including sessions opened with `mysql.get_session()`.

## The Callback

```python
def callback(session, sql):
    ...
```

The shell calls the function with two arguments:

| Argument | Description |
| --- | --- |
| `session` | The session that received the statement. Use it to run other statements on the same connection. |
| `sql` | The statement text as the user typed it, without the delimiter. |

The return value decides what happens next:

* A result object, created with `shell.create_result()`: the statement is complete, and the shell displays the result.
* `None`: the shell sends the original statement to the server as usual.

If the callback raises an exception, the shell reports it as an error for that statement.

## Building Results

```python
shell.create_result([data])
```

`shell.create_result()` builds a result object from a dictionary, or a multi-result object from a list of dictionaries. Called with no argument or with an empty dictionary, it returns an OK result with no rows.

| Key | Type | Description |
| --- | --- | --- |
| `data` | list | The rows. Each row is either a dictionary that maps column names to values, or, when `columns` is given, a list of values in column order. All rows must have the same form. |
| `columns` | list | The column definitions. Each entry is a column name, or a dictionary with `name` (required), `type`, `length`, and `flags`. Without `columns`, the shell takes the columns from the keys of the first row. |
| `info` | string | An information message, shown after the rows. |
| `executionTime` | float | The execution time in seconds, shown in the row count line. It can't be negative. |
| `affectedItemsCount` | integer | The number of affected rows, shown for results without rows. |
| `autoIncrementValue` | integer | The last generated auto-increment value. |
| `warnings` | list | Warnings, each a dictionary with `level` (`warning` or `note`), `message`, and `code`. `level` and `message` are mandatory. |

The `type` of a column is one of `string`, `integer`, `float`, `double`, `json`, `date`, `time`, `datetime`, or `bytes`. The `flags` value is a string with any of `BLOB`, `TIMESTAMP`, `UNSIGNED`, `ZEROFILL`, `BINARY`, `ENUM`, and `SET`, separated by spaces or commas. When you leave out the type or length, the shell derives them from the value in the first row. Python `datetime.date`, `datetime.time`, and `datetime.datetime` values are displayed as dates and times.

When you pass a list of dictionaries, each one becomes a separate result, the way a multi-statement call returns several result sets. An entry with an `error` key stops the sequence with an error. It takes the error message in `error`, the error number in `code`, and optionally an SQLSTATE in `sqlstate`:

```python
shell.create_result([
    {"data": [{"step": "validate", "status": "ok"}]},
    {"error": "Disk quota exceeded", "code": 50001, "sqlstate": "HY000"},
])
```

You can also use `shell.create_result()` outside SQL handlers, for example to display rows computed in Python with `shell.dump_rows()`.

## Example: SHOW SIZES

The following handler adds a `SHOW SIZES [schema]` statement that lists the tables of a schema by size. Without a schema name, it uses the default schema.

{% code title="~/.mariadb-shell/init.d/show_sizes.py" %}
```python
def show_sizes(session, sql):
    words = sql.split()
    if len(words) > 2:
        schema = words[2].strip("`")
    else:
        schema = session.run_sql("SELECT DATABASE()").fetch_one()[0]
    if schema is None:
        raise Exception("No schema given and no default schema selected.")

    result = session.run_sql(
        "SELECT table_name, engine, "
        "       COALESCE(data_length + index_length, 0) / 1048576 "
        "FROM information_schema.tables "
        "WHERE table_schema = ? AND table_type = 'BASE TABLE' "
        "ORDER BY 3 DESC", [schema])
    rows = [[name, engine or "", round(float(size), 2)]
            for name, engine, size in result.fetch_all()]

    return shell.create_result({
        "columns": ["Table", "Engine", {"name": "Size_MiB", "type": "double"}],
        "data": rows,
        "info": f"Sizes for schema {schema} are estimates.",
    })


shell.register_sql_handler("tableSizes", "Adds SHOW SIZES [schema]",
                           ["SHOW SIZES"], show_sizes)
```
{% endcode %}

```text
MariaDB localhost:3306 ssl  sakila  SQL > SHOW SIZES;
+---------------+--------+----------+
| Table         | Engine | Size_MiB |
+---------------+--------+----------+
| rental        | InnoDB |     2.52 |
| payment       | InnoDB |     2.08 |
| inventory     | InnoDB |     0.34 |
...
16 rows in set (0.0000 sec)

Sizes for schema sakila are estimates.
```

## Example: Guarding a Statement

A handler can also inspect a statement and let it through. The following handler refuses `DROP DATABASE` on a server whose host name is listed in the `PROD_HOSTS` environment variable, and returns `None` everywhere else, so the server runs the statement as usual.

```python
import os


def guard_drop(session, sql):
    host = session.run_sql("SELECT @@hostname").fetch_one()[0]
    if host in os.environ.get("PROD_HOSTS", "").split(","):
        raise Exception(f"DROP DATABASE is disabled on {host}.")
    return None


shell.register_sql_handler("dropGuard", "Blocks DROP DATABASE on production hosts",
                           ["DROP DATABASE", "DROP SCHEMA"], guard_drop)
```

{% hint style="info" %}
SQL handlers run only inside MariaDB Shell. They don't protect the server from other clients; use privileges for that.
{% endhint %}
