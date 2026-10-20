---
description: >-
  The tools and resources of GridGain MCP Server: what each tool does, how results are paged and limited, which SQL statements the server accepts, and the error codes.
---

# Tools and Resources

The server gives the assistant tools to work with the cluster and resources to read.
The assistant decides when to use them. You do not call them yourself.

All tools only read data. The server marks them as read-only, so a host can tell the assistant that they are safe to use.
See [Security](security.md) for the limits of this guarantee.

## Tools

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
The rows are sorted in a fixed order, so the pages do not overlap.

The following example is the result of `list_tables`:

```json
{
  "items": [
    {
      "schema": "PUBLIC",
      "name": "PERSON",
      "cache": "SQL_PUBLIC_PERSON",
      "keyType": "SQL_PUBLIC_PERSON_KEY",
      "valueType": "SQL_PUBLIC_PERSON_VALUE",
      "affinityKey": "ID"
    }
  ],
  "hasMore": false,
  "nextOffset": null
}
```

### Table and View Names

The `table` and `view` arguments take a name with an optional schema.
Without a schema, the server uses `PUBLIC` for tables and `SYS` for system views.

- Names that are not in quotes are not case-sensitive: `person`, `PERSON`, and `PUBLIC.person` are the same table.
- Put a name in double quotes to keep its case or to use spaces and dots: `"My Schema"."my table"`. To write a quote character in a name, double it.

{% hint style="info" %}
The tools expect the system schema to be named `SYS`. A cluster that you start with `IGNITE_SQL_SYSTEM_SCHEMA_NAME_IGNITE=true` names it `IGNITE`, and the server does not support such a cluster.
{% endhint %}

### Running Queries

`execute_select_sql` runs a query, and `get_query_execution_plan` shows how the cluster runs it.
Both take one argument, `sql`.

The server checks every statement before it sends it to the cluster.
It accepts one `SELECT` or `WITH ... SELECT` statement, with an optional `EXPLAIN` before it and an optional `;` after it.
`get_query_execution_plan` adds `EXPLAIN` if it is missing.
The server refuses any other statement with the `REJECTED` code and one of these reasons:

| Reason | Statement |
| ------ | --------- |
| `NOT_SELECT` | Anything that is not a plain query: data changes, schema changes, commands, a `WITH` that ends in a data change, a query in parentheses, `VALUES`, and `TABLE`. |
| `MULTIPLE_STATEMENTS` | There is text after the first statement. |
| `EXPLAIN_ANALYZE` | `EXPLAIN ANALYZE`, because it runs the query. |
| `FOR_UPDATE` | `FOR UPDATE`, at any level of the query. |
| `UNSUPPORTED_SYNTAX` | A comment (`--`, `/* */`, `//`), or any character other than ASCII letters, digits, `_`, white space, and `(),.*+-/%=<>!\|:?` outside quoted strings and quoted names. The server refuses `$`, backticks, brackets, braces, `&`, `^`, `~`, `@`, `#`, and non-ASCII letters, among others. |
| `UNTERMINATED` | A string, a quoted name, or a parenthesis is not closed. |
| `SYSTEM_SCHEMA` | The query uses `INFORMATION_SCHEMA`, `IGNITE`, or a system view other than `CACHES`, `INDEXES`, `SCHEMAS`, `STATISTICS_LOCAL_DATA`, `TABLES`, `TABLE_COLUMNS`, `VIEWS`, and `VIEW_COLUMNS`. |
| `EMPTY` | The statement has only white space and a `;`. |

The server refuses the words `SYS`, `INFORMATION_SCHEMA`, and `IGNITE` as the name of anything, including a column or an alias.
`EXPLAIN PLAN` and `EXPLAIN PLAN FOR` work like `EXPLAIN`.

The check protects against mistakes of the assistant. It is not a full SQL parser, so it refuses a statement when it does not understand its form.
The account of the server is the real protection. See [Security](security.md).

The server looks up unqualified table names in the `PUBLIC` schema. Use `schema.table` for other schemas.

{% hint style="info" %}
Distributed joins are not enabled. A join of tables that are not colocated can miss rows.
{% endhint %}

#### Query Result

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

The server keeps integers, floating-point numbers, booleans, and null as JSON values.
All other types are returned as text. This includes decimals, large integers, `NaN`, `Infinity`, dates, times, and UUIDs.
Binary values are returned as lower-case hexadecimal text, and arrays as text such as `[a, b]`.

The server shortens long values and marks the end of the value:

- Text longer than 8192 characters ends with `...[truncated, total N chars]`.
- A binary value longer than 4096 bytes ends with `...[truncated, total N bytes]`.
- A column name longer than 256 characters ends with `...`.

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

#### Query Errors

If a query fails, the result is marked as an error and has the `error`, `code`, and `elapsedMillis` fields.
A refused statement also has `reason`, except when `sql` is missing.
A `QUERY_ERROR` also has `serverCode`.

| Code | Meaning |
| ---- | ------- |
| `REJECTED` | The server refused the statement, or `sql` is missing. Nothing was sent to the cluster. |
| `TIMEOUT` | The cluster cancelled the query after `MCP_OPERATION_TIMEOUT`, or the server stopped waiting for the answer. |
| `CONNECTION_ERROR` | There is no connection, the connection was lost, the cluster rejected the credentials, or the server is shutting down. |
| `AUTHORIZATION` | The account has no permission that the query needs. |
| `QUERY_ERROR` | The cluster rejected the query or it failed. `error` has the first line of the cluster message, cut to 1000 characters. |
| `RESULT_TOO_LARGE` | The column names and the fixed fields of the result are already larger than `MCP_MAX_RESPONSE_BYTES`. |
| `BUSY` | Too many calls are waiting to run. Try again later. |
| `RATE_LIMITED` | The tool reached its [rate limit](operations.md#rate-limit). |

The texts of all other errors are fixed. The server writes the details of the failure to its log.

### Result Limits

The server limits every result that a tool returns:

- A result has at most `MCP_MAX_ROWS` rows. A result with exactly that many rows is not marked as truncated.
- A result is at most `MCP_MAX_RESPONSE_BYTES` bytes in size. The server counts the result twice, because it returns it as structured data and as text.
- When a limit cuts the result, `truncated` is `true`, and `truncationReason` tells which limit it was.
- A single row that is larger than the size limit gives an empty result with `BYTE_LIMIT`, not an error.
- A listing entry that cannot fit on a page alone is an error. The server does not drop it silently.

The limits only restrict what the server returns.
They do not reduce the work of the cluster. A query that sorts or groups data runs to the end, until `MCP_OPERATION_TIMEOUT`.

When a result is truncated, the assistant should narrow the query with `WHERE` or `LIMIT`, or aggregate the data.

### Connection Check

`check_database_connection` connects to the cluster if needed and runs `SELECT 1`.
It returns the following information:

```json
{
  "message": "GridGain cluster answered SELECT 1",
  "elapsedMillis": 12,
  "addresses": ["localhost:10800"],
  "username": "mcp_reader",
  "clusterVersion": "8.10.127#20261002-sha1:0123abcd"
}
```

- `username` is present only if you set it. The password is never returned.
- `clusterVersion` is the version of one cluster node. The server leaves it out if the cluster cannot report it.

If the check fails, the result is marked as an error and has `error` and `code` instead of `message`.
The code is `TIMEOUT`, `CONNECTION_ERROR`, `QUERY_ERROR`, or `BUSY`.
A failed check does not close the session.

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
