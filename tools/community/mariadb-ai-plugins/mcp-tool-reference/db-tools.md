---
description: >-
  Reference for the db tools of the mariadb-shell MCP server, which list connections and schemas, describe database objects, and run SQL.
---

# db Tools

The `db.*` tools open connections to configured MariaDB servers, describe their schemas, and run SQL.

## Overview

| Tool | Description |
| --- | --- |
| `db.list_connections` | Lists the configured connection URIs. |
| `db.connect` | Opens and caches a connection, and returns a `connection_id`. |
| `db.list_schemas` | Lists the schemas visible to the connection's account. |
| `db.list_objects` | Lists the objects of one type in a schema. |
| `db.get_object_details` | Returns structured details of an object: columns, keys, indexes, and constraints. |
| `db.execute_sql` | Runs one statement on the connection's session. |
| `db.execute_sql_script` | Runs a multi-statement script. |
| `db.close` | Closes a connection. |

## db.list_connections

Lists the configured connection URIs.

This tool takes no arguments.

The list is derived from MariaDB Shell's secret store, so a connection registered by a sandbox appears here too. Call it first.

## db.connect

Opens and caches a connection, and returns a `connection_id`.

| Argument | Description |
| --- | --- |
| `uri` | A configured connection URI. |

The URI is normalized before matching. A URI that asks for more than was configured, such as a default schema or an option, is refused. See [Security Model](../security-model.md#connections).

## db.list_schemas

Lists the schemas visible to the connection's account.

| Argument | Description |
| --- | --- |
| `connection_id` | A connection ID returned by `db.connect`. |

A missing schema usually means the account lacks privileges on it.

## db.list_objects

Lists the objects of one type in a schema.

| Argument | Description |
| --- | --- |
| `connection_id` | A connection ID returned by `db.connect`. |
| `schema_name` | The schema to list. |
| `object_type` | One of `table` (default), `view`, `procedure`, `function`, `trigger`, or `event`. |

## db.get_object_details

Returns structured details of an object: columns, keys, indexes, and constraints.

| Argument | Description |
| --- | --- |
| `connection_id` | A connection ID returned by `db.connect`. |
| `schema_name` | The object's schema. |
| `object_name` | The object's name. |
| `object_type` | The object type. Default: `table`. |

The result is returned as structured data rather than as a `CREATE` statement. The agent calls this tool before it proposes a schema change.

## db.execute_sql

Runs one statement on the connection's session.

| Argument | Description |
| --- | --- |
| `connection_id` | A connection ID returned by `db.connect`. |
| `sql` | One SQL statement. |
| `params` | Optional values for the statement's placeholders. |

Use it for a single statement, in particular one that takes parameters or whose result rows the agent needs.

## db.execute_sql_script

Runs a multi-statement script.

| Argument | Description |
| --- | --- |
| `connection_id` | A connection ID returned by `db.connect`. |
| `sql_script` | The script text. Pass either `sql_script` or `file_path`. |
| `file_path` | A script file. Must be in an allowed path. |
| `stop_on_error` | Whether the script stops at the first failed statement. Default: `True`. With `False`, every statement runs and each failure is reported. |
| `limit` | Optional. The maximum number of rows that each `SELECT` without its own `LIMIT` returns. |
| `column_metadata` | Whether each result set also includes column metadata. Default: `False`. |

The statements run in order on the session of the connection, so session state carries over from one statement to the next. This includes user variables set with `SET @var`, the current schema set with `USE`, open transactions, and the current REST service and REST schema of MariaDB REST Service statements.

The tool returns one entry for each statement that ran. A failed statement doesn't raise an error: its entry contains the error message and the statement text instead of result sets, so the agent must check every entry. A script isn't a transaction, and statements that ran before a failure keep their effect.

{% hint style="info" %}
If the connection's session was closed because it was idle or lost, the MCP server opens a new session before it runs the script, and the first entry contains `session_restarted: true`. In this case, state from earlier tool calls, such as temporary tables, user variables, the current schema, and an open transaction, no longer exists.
{% endhint %}

## db.close

Closes a connection.

| Argument | Description |
| --- | --- |
| `connection_id` | A connection ID returned by `db.connect`. |

Idle connections are closed automatically, but close a sandbox's connection before deleting the sandbox.
