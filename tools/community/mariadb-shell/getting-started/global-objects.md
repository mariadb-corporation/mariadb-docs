---
description: >-
  The objects that MariaDB Shell makes available in Python mode: shell,
  session, db, mysql, util, sandbox, plugins, msm, and mcp.
---

# Global Objects

When the shell starts in Python mode, or when you switch to it with `\py`, a set of global objects is ready for use without an import. To list them, run `\?`. For the members of an object, run `\? <object>` or call its `help()` method, for example `util.help()`.

| Object | Purpose |
| --- | --- |
| `shell` | General shell functions: connections, configuration options, credentials, reports, output, and extensions. |
| `session` | The global session, or `None` when the shell is not connected. |
| `db` | Defined for compatibility with scripts written for MySQL Shell. Its value is always `None`. |
| `mysql` | Functions for opening classic sessions and for parsing SQL and quoting identifiers. |
| `util` | The dump, load, copy, export, import, password change, and diagnostics utilities. |
| `sandbox` | Deploys and manages local MariaDB and MySQL test servers. |
| `plugins` | Installs, lists, updates, and removes shell plugins. |
| `msm` | Develops, releases, and deploys versioned database schemas with [Schema Management](../schema-management/README.md). Included in the release packages. |
| `mcp` | Configures and starts the [MCP server](../mcp-server/README.md). Included in the release packages. |

Plugins and the [extension object](../extending-mariadb-shell/extension-objects.md) API can register additional global objects.

## shell

The `shell` object provides functions that don't belong to a particular session or utility:

* Session management: `connect()`, `open_session()`, `get_session()`, `set_session()`, `reconnect()`, `disconnect()`, `set_current_schema()`, and `status()`. See [Sessions](sessions.md).
* URI handling: `parse_uri()` splits a connection URI into a dictionary, and `unparse_uri()` builds a URI from one.
* Configuration: the `shell.options` property reads and changes [configuration options](../customizing/configuration-options.md).
* Credentials and secrets: `store_credential()`, `list_credentials()`, `delete_credential()`, `list_credential_helpers()`, and the corresponding functions for arbitrary secrets. See [Credential Store](../connecting/credential-store.md).
* SSH tunnels: `list_ssh_connections()` lists the active tunnels. See [SSH Tunnels](../connecting/ssh-tunnels.md).
* Output: `print()`, `dump_rows()`, `enable_pager()`, and `disable_pager()`. See [Pager](../using-mariadb-shell/pager.md).
* User interaction and logging: `prompt()` asks the user for input, and `log()` writes to the [shell log](../logging-and-debugging.md).
* Extensions: the `shell.reports` property and `register_report()` ([Reports](../extending-mariadb-shell/reports.md)), `create_extension_object()`, `add_extension_object_member()`, and `register_global()` ([Extension Objects](../extending-mariadb-shell/extension-objects.md)), and `register_sql_handler()` ([SQL Handlers](../extending-mariadb-shell/sql-handlers.md)).

## session

`session` is the `ClassicSession` object of the global session. Use it to run SQL from Python:

```text
MariaDB localhost:3306 ssl  Py > session.run_sql("SELECT name, population FROM world.city ORDER BY population DESC LIMIT 3")
```

The variable changes when you connect, reconnect, call `shell.set_session()`, or disconnect. For its properties and methods, see [ClassicSession Methods](sessions.md#classicsession-methods).

## db

MariaDB Shell defines the `db` variable but never assigns a schema object to it, so its value is always `None`, even after `\use`. To read the default schema of the global session, query the server, or check the `Current schema` line of `\status`:

```python
session.run_sql("SELECT DATABASE()").fetch_one()[0]
```

## mysql

The `mysql` module provides functions for working with classic sessions and SQL text. It is loaded automatically in interactive mode.

| Function | Description |
| --- | --- |
| `get_session(connectionData[, password])` | Opens and returns a new session. |
| `get_classic_session(connectionData[, password])` | Same as `get_session()`. |
| `quote_identifier(name)` | Encloses a name in backticks, doubling any backticks inside it, so that it can be used as an identifier. |
| `unquote_identifier(name)` | Removes identifier quoting. |
| `make_account(user, host)` | Builds a quoted account name, for example `'app'@'%'`. |
| `split_account(account)` | Splits an account name into user and host. |
| `split_script(script[, options])` | Splits an SQL script into individual statements. |
| `tokenize_statement(statement[, options])` | Splits a statement into tokens. |
| `parse_statement_ast(statements[, options])` | Parses statements and returns their syntax tree. |

The module also provides the `ErrorCode` constants for server error codes.

## util

The `util` object groups the shell's utilities:

| Functions | Purpose |
| --- | --- |
| `dump_instance()`, `dump_schemas()`, `dump_tables()`, `load_dump()` | Parallel logical dump and load. See [Dump and Load](../utilities/dump-and-load/). |
| `copy_instance()`, `copy_schemas()`, `copy_tables()` | Copy data directly between two servers. See [Copy Utilities](../utilities/dump-and-load/copy-utilities.md). |
| `export_table()`, `import_table()` | Export a table to a delimited file, or import delimited files into a table. See [Table Export and Import](../utilities/table-export-and-import.md). |
| `change_password()` | Change the password of an account. See [Password Change Utility](../utilities/password-change-utility.md). |
| `util.debug.collect_diagnostics()`, `collect_high_load_diagnostics()`, `collect_slow_query_diagnostics()` | Gather diagnostic information into an archive. See [Diagnostics Utilities](../utilities/diagnostics-utilities.md). |

All of these functions are also available from the operating system shell through [command line integration](../using-mariadb-shell/command-line-integration.md).

## sandbox

The `sandbox` object deploys, starts, stops, kills, and deletes local server instances for testing and development. It works with MariaDB and MySQL server binaries and detects the vendor automatically. For example, `sandbox.deploy(3310)` creates and starts an instance on port 3310. See [Sandbox Instances](../sandbox-instances.md).

## plugins

The `plugins` object manages plugins that extend the shell: `list()`, `install()`, `update()`, `uninstall()`, `details()`, and the `repositories` property for plugin repositories. `plugins.about()` describes how to write a plugin. See [Plugins](../extending-mariadb-shell/plugins.md).

## Using Global Objects in Python Modules

In code that the shell runs directly, such as interactive input, script files, and startup scripts, the global objects are already defined. A Python module that you import doesn't see them automatically. Import them from the `mysqlsh` package instead:

```python
from mysqlsh import globals

def table_count(schema):
    return globals.session.run_sql(
        "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = ?",
        [schema]).fetch_one()[0]
```
