---
description: >-
  The tools and resources of GridGain MCP Server: what each tool does, how results are paged and limited, which SQL statements the server accepts, and the error codes.
---

# Tools and Resources

GridGain MCP Server gives the assistant tools to work with the cluster and resources to read.
The assistant decides when to use them. You do not call them yourself.

All tools only read data. The server marks them as read-only, so a host can tell the assistant that they are safe to use.
See [Security](security.md) for the limits of this guarantee.

## Tools

The server has eight tools. One checks the connection, five list objects and their columns, and two run queries.

| Tool | Arguments | What it does |
| ---- | --------- | ------------ |
| `check_database_connection` | None | Connects to the cluster and runs `SELECT 1`. Use it to check the setup. |
| `list_caches` | `limit`, `offset` | Lists the user caches with their mode and SQL schema. `sqlReadable` is `false` for a cache that has no table. |
| `list_tables` | `limit`, `offset` | Lists the SQL tables with their schema, cache, key and value types, and affinity key. |
| `describe_table` | `table`, `limit`, `offset` | Lists the columns of a table with their type, key flags, nullability, precision, scale, and default value. It includes the hidden `_KEY` and `_VAL` columns. |
| `list_system_views` | `limit`, `offset` | Lists the system views of the `SYS` schema. |
| `describe_system_view` | `view`, `limit`, `offset` | Lists the columns of a system view. |
| `execute_select_sql` | `sql` | Runs one read-only query and returns the columns and rows. |
| `get_query_execution_plan` | `sql` | Returns the execution plan of a query without running it. |

## Checking the Connection

`check_database_connection` connects to the cluster if needed and runs `SELECT 1`.
It confirms that the server can reach the cluster with the configured account.
A successful check returns the following information:

```json
{
  "message": "GridGain cluster answered SELECT 1",
  "elapsedMillis": 12,
  "addresses": ["localhost:10800"],
  "username": "mcp_reader",
  "clusterVersion": "8.10.0#20261002-sha1:0123abcd"
}
```

- `username` is present only if you set it. The password is never returned.
- `clusterVersion` is the version of one cluster node. The server leaves it out if the cluster cannot report it.

If the check fails, the result is marked as an error and has `error` and `code` instead of `message`.
The code is `TIMEOUT`, `CONNECTION_ERROR`, `QUERY_ERROR`, or `BUSY`.
A failed check does not close the session.

## Listing Objects

The `list_caches`, `list_tables`, `describe_table`, `list_system_views`, and `describe_system_view` tools show the assistant what the cluster contains.
With them, the assistant can find the tables and columns to query.

### Paged Results

The tools that list objects return the result in pages.
Each result is a JSON object with the following fields:

| Field | Description |
| ----- | ----------- |
| `items` | The rows of the page. |
| `hasMore` | `true` if there are more rows. |
| `nextOffset` | The value to pass as `offset` to get the next page, or `null` on the last page. |

The `describe_table` and `describe_system_view` tools also return the resolved `schema` and `name`.

The `limit` argument sets the page size. The server never returns more rows than `MCP_MAX_ROWS` allows, even if `limit` is larger.
The rows are sorted in a fixed order, so the pages do not overlap as long as the schema does not change between calls.

The following example is the result of `list_tables`:

```json
{
  "items": [
    {
      "schema": "PUBLIC",
      "name": "PERSON",
      "cache": "SQL_PUBLIC_PERSON",
      "keyType": "java.lang.Long",
      "valueType": "SQL_PUBLIC_PERSON_3f2a9c4e_8b1d_4e6f_a7c2_5d9e0b1f6a83",
      "affinityKey": null
    }
  ],
  "hasMore": false,
  "nextOffset": null
}
```

### Table and View Names

The `table` and `view` arguments take a name with an optional schema.
Without a schema, the server uses `PUBLIC` for tables and `SYS` for system views.

- Names without quotes are not case sensitive. `person`, `PERSON`, and `PUBLIC.person` are the same table.
- To keep the case of a name, or to use spaces and dots in it, put the name in double quotes, such as `"My Schema"."my table"`. To write a quote character in a name, double it.

{% hint style="info" %}
The tools expect the system schema to be named `SYS`. A cluster that you start with `IGNITE_SQL_SYSTEM_SCHEMA_NAME_IGNITE=true` names it `IGNITE`, and the server does not support such a cluster.
{% endhint %}

## Running Queries

`execute_select_sql` runs a query, and `get_query_execution_plan` shows how the cluster runs it.
Both take one argument, `sql`.

The server looks up unqualified table names in the `PUBLIC` schema. Use `schema.table` for other schemas.

{% hint style="info" %}
Distributed joins are not enabled. A join of tables that are not colocated can miss rows.
{% endhint %}

### Statement Check

The server checks every statement before it sends it to the cluster.
It accepts one `SELECT` or `WITH ... SELECT` statement, with an optional `EXPLAIN` before it and an optional `;` after it.
`EXPLAIN PLAN` and `EXPLAIN PLAN FOR` work like `EXPLAIN`.
`get_query_execution_plan` adds `EXPLAIN` if it is missing.

The server refuses any other statement with the `REJECTED` code and one of the following reasons:

| Reason | Refused statement |
| ------ | ----------------- |
| `NOT_SELECT` | Anything that is not a plain query: data changes, schema changes, commands, a `WITH` that ends in a data change, a query in parentheses, `VALUES`, and `TABLE`. |
| `MULTIPLE_STATEMENTS` | The statement contains a `;` other than one `;` at the end, such as `SELECT 1; SELECT 2` or `SELECT 1;;`. |
| `EXPLAIN_ANALYZE` | `EXPLAIN ANALYZE`, because it runs the query. |
| `FOR_UPDATE` | `FOR UPDATE`, at any level of the query. |
| `UNSUPPORTED_SYNTAX` | A comment (`--`, `/* */`, `//`), or any character other than ASCII letters, digits, `_`, white space (space, tab, line feed, and carriage return), and `(),.*+-/%=<>!\|:?` outside quoted strings and quoted names. The server refuses `$`, backticks, brackets, braces, `&`, `^`, `~`, `@`, `#`, and non-ASCII letters, among others. |
| `UNTERMINATED` | A string, a quoted name, or a parenthesis is not closed, or a `)` has no matching `(`. |
| `SYSTEM_SCHEMA` | The query uses `INFORMATION_SCHEMA`, `IGNITE`, or a system view other than `CACHES`, `INDEXES`, `SCHEMAS`, `STATISTICS_LOCAL_DATA`, `TABLES`, `TABLE_COLUMNS`, `VIEWS`, and `VIEW_COLUMNS`. |
| `EMPTY` | The statement is empty or has only white space, with or without a `;`. |

The server also refuses the words `SYS`, `INFORMATION_SCHEMA`, and `IGNITE` as the name of anything, including a column or an alias.

The check protects against the assistant's mistakes. It is not a full SQL parser, so it refuses a statement when it does not understand its form.
The server's account is the real protection. See [Security](security.md).

### Query Result

The result of a query is one JSON object with the following fields:

| Field | Description |
| ----- | ----------- |
| `columns` | The column names. |
| `rows` | The rows. Each row is a list of values in the order of the columns. |
| `rowCount` | The number of rows in the result. |
| `truncated` | `true` if the server cut the result because of a limit. |
| `truncationReason` | `ROW_LIMIT` or `BYTE_LIMIT`. Present only if `truncated` is `true`. |
| `hint` | Advice on how to narrow the query. Present only if `truncated` is `true`. |
| `rowLimit` | The row limit that applies, from `MCP_MAX_ROWS`. |
| `byteLimit` | The size limit that applies, from `MCP_MAX_RESPONSE_BYTES`. |
| `elapsedMillis` | The time in milliseconds that the call took, including the connection and any repeated attempts to connect. |

```json
{
  "columns": ["ID", "NAME"],
  "rows": [[1, "Ann"], [2, "Bob"]],
  "rowCount": 2,
  "truncated": false,
  "rowLimit": 1000,
  "byteLimit": 102400,
  "elapsedMillis": 14
}
```

The server returns each value in one of the following forms:

| Value | Returned as |
| ----- | ----------- |
| Integers, floating-point numbers, booleans, and `NULL` | JSON values |
| Decimals, large integers, `NaN`, `Infinity`, and UUIDs | Text |
| Dates and times | SQL literals in UTC, such as `2026-10-06`, `03:04:05`, or `2026-10-06 00:30:00.123456` |
| Binary values | Lowercase hexadecimal text |
| Arrays | Text, such as `[a, b]` |

Dates and times do not depend on the time zone of the server or the cluster.

The server shortens long values and marks the end of the value:

- Text longer than 8192 characters ends with `...[truncated, total N chars]`.
- A binary value longer than 4096 bytes ends with `...[truncated, total N bytes]`.
- A column name longer than 256 characters ends with `...`.

### Query Errors

If a query fails, the result is marked as an error and has the `error`, `code`, and `elapsedMillis` fields.
Some codes add or remove fields:

- A refused statement also has `reason`.
- A `QUERY_ERROR` also has `serverCode` if the cluster reports one. Otherwise, `error` is the fixed text `GridGain cluster failed the query`.
- A `RATE_LIMITED` result is text only. It has the `error`, `code`, and `retryAfterMs` fields, and no `elapsedMillis`.

| Code | Meaning |
| ---- | ------- |
| `REJECTED` | The server refused the statement. Nothing was sent to the cluster. |
| `TIMEOUT` | The cluster cancelled the query after `MCP_OPERATION_TIMEOUT`, the server stopped waiting for the answer, or the call waited for a free worker longer than `MCP_OPERATION_TIMEOUT`. |
| `CONNECTION_ERROR` | There is no connection, the connection was lost, the cluster rejected the credentials, or the server is shutting down. |
| `AUTHORIZATION` | The account has no permission that the query needs. |
| `QUERY_ERROR` | The cluster rejected the query or it failed. `error` has the first line of the cluster message. A message longer than 1000 characters is truncated and ends with `...`. |
| `RESULT_TOO_LARGE` | The column names and the fixed fields of the result are already larger than `MCP_MAX_RESPONSE_BYTES`. |
| `BUSY` | Too many calls are waiting to run. Try again later. |
| `RATE_LIMITED` | The tool reached its [rate limit](operations.md#rate-limit). |

Other errors have fixed texts. The server writes the details of the failure to its log.

## Result Limits

The server limits the number of rows and the size of every result that a tool returns.
You set the limits with `MCP_MAX_ROWS` and `MCP_MAX_RESPONSE_BYTES`, as described in [Result Limits](configuration.md#result-limits).

The limits work as follows:

- A result has at most `MCP_MAX_ROWS` rows. A result with exactly that many rows is not marked as truncated.
- A result is at most `MCP_MAX_RESPONSE_BYTES` bytes in size. The server counts the result twice, because it returns it as structured data and as text.
- When a limit cuts the result, `truncated` is `true`, and `truncationReason` names the limit.
- A single row that is larger than the size limit gives an empty result with `BYTE_LIMIT`, not an error.
- A listing entry that cannot fit on a page alone is an error. The server does not drop it silently.

The limits only restrict what the server returns.
They do not reduce the work of the cluster. A query that sorts or groups data runs to the end, until `MCP_OPERATION_TIMEOUT`.

When a result is truncated, the assistant should narrow the query with `WHERE` or `LIMIT`, or aggregate the data.

## Resources

Resources are reference documents that the assistant can read.
They are part of the server, so the assistant can read them even when the cluster is not reachable.

| Resource | Content |
| -------- | ------- |
| `gridgain://sql-dialect` | The GridGain SQL dialect: names, the relation between caches and tables, affinity and colocation, types, functions, unsupported syntax, and queries to the system views. |
| `gridgain://sql-dialect-reference` | Reference tables: reserved words, functions, and system views. |
| `gridgain://query-optimization-guide` | How to read a query plan and how to fix slow queries. |

Each resource is a Markdown document.
Some hosts do not show resources to the user and let the assistant read them when it needs them.
