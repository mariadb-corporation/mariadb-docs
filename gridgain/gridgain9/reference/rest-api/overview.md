---
description: >-
  Use the GridGain 9 REST API to monitor and manage a cluster over HTTP, run SQL
  statements and scripts, page through results, and generate a Java client.
---

# REST API

The GridGain 9 clusters provide an [OpenAPI](https://www.openapis.org/) specification that can be used to work with GridGain 9 by standard REST methods.

## OpenAPI Specification

You can access [online specification](https://www.gridgain.com/sdk/gridgain9/latest/openapi.html) in the API section. The OpenAPI documentation provides extended information on all REST endpoints you can access and the required payloads.

## REST Connector Configuration

By [default](../configuration/node-configuration-parameters.md), rest connector starts on port 10300. THis port can be configured in the `ignite.rest` [node configuration](../configuration/node-configuration-parameters.md#rest-configuration).

## Using HTTP Tools

Once the cluster is started, you can use external tools to monitor the cluster over http, or manage the cluster. In this example, we will use [curl](https://curl.se/) to get cluster status:

```bash
curl 'http://localhost:10300/management/v1/cluster/state'
```

You are not limited to only monitoring, as GridGain REST API provides endpoints that can be used to manage the cluster as well. For example, you can create a [snapshot](../../gridgain9-management/snapshots/data-snapshots.md) via REST:

```bash
curl -H "Content-Type: application/json" -d '{"snapshotType": "FULL","tableNames": "table1,table2","startTimeEpochMilli": 0}' http://localhost:10300/management/v1/snapshot/create
```

You can also rename an already-initialized cluster. The new name is sent as a plain-text body to the `cluster/rename` endpoint:

```bash
curl -X POST -H "Content-Type: text/plain" -d 'newClusterName' http://localhost:10300/management/v1/cluster/rename
```

On success, the endpoint returns the updated `ClusterTag` as JSON, including the new name and the unchanged cluster ID. The request fails with `400` if the supplied name is empty. The same operation is available from the CLI tool as [`cluster rename`](../cli-tool.md#cluster-rename).

## Running SQL

You can execute SQL statements over the management REST API. Send a single statement to the `sql/execute` endpoint:

```bash
curl -H "Content-Type: application/json" -d '{"statement": "SELECT id, name FROM Person"}' http://localhost:10300/management/v1/sql/execute
```

To run SQL, a caller needs the cluster-level `EXECUTE_SQL` privilege, and the object privileges the statement
itself requires, such as `SELECT_FROM_TABLE` or `INSERT_INTO_TABLE`. A caller that lacks either gets `403`.
For the full list, see [User Permissions and Roles](../../security/user-permissions-and-roles.md).

One response shape covers every kind of statement. `hasRowSet` reports whether the statement produced rows;
when it did, `meta` describes the columns and `rows` holds the first page, each row ordered as in `meta`.
A DML statement reports `affectedRows`, and a conditional DDL or DCL statement reports `wasApplied`.

This endpoint runs exactly one statement and holds no session. It rejects transaction control statements such
as `START TRANSACTION` and `COMMIT` with `400`. To run several statements in one transaction, use
[a script](#running-a-script).

Besides `statement`, the request accepts `arguments`, a `defaultSchema` to resolve unqualified
names against, a `timeZone` (UTC unless set), a `queryTimeoutMillis` (no timeout when zero or absent),
and a `pageSize`.

### Passing Parameters

Each entry in `arguments` is an object with a required `type` and a `value`. A bare value is rejected with
`400`. Entries are positional, so the first entry fills the first `?` in the statement:

```bash
curl -H "Content-Type: application/json" -d '{"statement": "SELECT name FROM Person WHERE id = ?", "arguments": [{"type": "INT32", "value": 1}]}' http://localhost:10300/management/v1/sql/execute
```

The `type` names a column type rather than a SQL type, as described in [Value Encoding](#value-encoding). A `value` that is
`null` or absent passes a SQL `NULL`. The `sql/script` endpoint takes `arguments` in the same form.

### Paging Through a Result

By default, a page holds up to 1000 rows. Set `pageSize` on the request to ask for a different size. A request
for more than the configured maximum of 10000 rows is rejected with `400`, rather than reduced to the maximum.
Both limits are configurable, as described in [REST Configuration](../configuration/node-configuration-parameters.md#rest-configuration).

When rows remain beyond the returned page, the response sets `hasMore` to `true` and includes a `cursorId`. Pass it to the `sql/cursors` endpoint to read the next page:

```bash
curl 'http://localhost:10300/management/v1/sql/cursors/{cursorId}'
```

All pages of a result are read in a single read-only transaction. Paging through a result therefore gives you
a consistent snapshot of the data.

Reading the last page closes the cursor for you. Close a cursor explicitly when you stop reading early:

```bash
curl -X DELETE 'http://localhost:10300/management/v1/sql/cursors/{cursorId}'
```

An open cursor holds its read-only transaction open, which pins a read timestamp and blocks garbage
collection of older row versions. By default, a cursor left untouched for 5 minutes is released, and a later
request for its next page gets `410`. Run the statement again to get a fresh cursor.

By default, a node holds at most 100 open cursors at a time. While a node is at that limit, an `sql/execute`
request that needs a cursor gets `429`.

{% hint style="warning" %}
A `cursorId` is valid only on the node that returned it. Send every page request to that same node, and do not route paging requests through a load balancer that may choose a different one.
{% endhint %}

### Running a Script

To run several statements in one request, send them to the `sql/script` endpoint as a semicolon-separated `script`, optionally with `arguments`:

```bash
curl -H "Content-Type: application/json" -d '{"script": "CREATE TABLE IF NOT EXISTS Person (id INT PRIMARY KEY, name VARCHAR); INSERT INTO Person VALUES (1, '\''Ada'\'');"}' http://localhost:10300/management/v1/sql/script
```

The statements run in order. The endpoint returns no content, so use `sql/execute` when you need results back.

A script manages its own transactions. Transaction control statements such as `START TRANSACTION` and `COMMIT`
are accepted here, which makes a script the only way to run a multi-statement transaction over REST.

A script takes no execution options. It has no `defaultSchema`, `timeZone` or `queryTimeoutMillis`, and always
runs with the cluster defaults. A script that targets another schema must qualify the names itself.

What a failure leaves behind depends on when the failure happens:

- The whole script is parsed before anything runs. A syntax error anywhere in the script leaves the cluster untouched, and the request fails with `400`.
- A statement that fails while running stops the script at that point. Whatever already committed keeps its effects, so the cluster can be left partly migrated.

### Value Encoding

Parameter and result values are named by their `ColumnType` constant rather than by their SQL name, so a
32-bit integer is `INT32` and not `INT`. Column metadata travels with every result page, so a client always
knows which encoding applies to a value and can restore it exactly.

Values whose full range a JSON number cannot carry are sent and returned as strings:

| Type | Wire form |
| --- | --- |
| `DECIMAL`, `INT64` | String. A JSON number would round a decimal fraction away, and an `INT64` above 2^53 loses its low bits in any consumer that parses JSON numbers as doubles. |
| Temporal types, `UUID` | String, in the type's textual form. |
| `BYTE_ARRAY` | Base64 string. |
| `FLOAT`, `DOUBLE` | Number while finite. `NaN`, `Infinity` and `-Infinity` are strings, spelled as the SQL engine spells them in a cast such as `'NaN'::DOUBLE`. On input, `+Infinity` is also accepted. |

A finite number too large for the type it is sent as is rejected rather than saturated to infinity, so a value can never read back as something the caller did not send.

{% hint style="warning" %}
`TIMESTAMP` names an instant here, while the SQL type of that name is `DATETIME`. See [Data Types](../sql/data-types.md) for the full correspondence between SQL types and column types.
{% endhint %}

### Status Codes

A failed request returns its details as `application/problem+json`, with one of the following codes:

| Code | Meaning |
| --- | --- |
| `400` | The request is malformed, the statement or script is invalid, or the requested `pageSize` is above the configured maximum. `sql/execute` also returns `400` for a transaction control statement. |
| `403` | The caller may not execute SQL, or lacks a privilege that the statement requires. |
| `404` | No such cursor on this node. A cursor that belongs to another user is also reported as absent. |
| `409` | Another request is already fetching from this cursor. |
| `410` | The cursor was already released, either because it sat idle too long or because the transaction carrying it expired. Run the statement again. |
| `429` | This node already holds the maximum number of open cursors. |
| `500` | A statement in a script failed for a reason that the engine does not attribute to the request. |

## Java Project Configuration

If you want to integrate GridGain REST API closer into your application, we recommend using an [OpenAPI generator](https://github.com/OpenAPITools/openapi-generator) to generate a Java client. Once the client is generated, you can use it to work with REST API from code, for example:

```java
ApiClient client = Configuration.getDefaultApiClient();
// Set base URL
client.setBasePath("http://localhost:10300");

// Get cluster configuration.
ClusterConfigurationApi clusterConfigurationApi = new ClusterConfigurationApi(client);
String configuration = clusterConfigurationApi.getClusterConfiguration();
```
