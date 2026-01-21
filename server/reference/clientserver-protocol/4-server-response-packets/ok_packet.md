---
description: >-
  The OK_Packet is sent by the server to indicate the successful completion of a
  command, conveying affected row counts and server status flags.
---

# OK\_Packet

`OK_Packet` is sent by the server to the client and indicates a successful completion of a command sent by the client before.

## Direction

Server to client.

## Fields

* [int<1>](../protocol-data-types.md#fixed-length-integers) 0x00 : `OK_Packet` header or (`0xFE` if `CLIENT_DEPRECATE_EOF` is set).
* [int](../protocol-data-types.md#length-encoded-integers) affected rows.
* [int](../protocol-data-types.md#length-encoded-integers) last insert id.
* [int<2>](../protocol-data-types.md#fixed-length-integers) [server status](ok_packet.md#server-status-flag).
* [int<2>](../protocol-data-types.md#fixed-length-integers) warning count.
* If packet has more data:
  * [string](../protocol-data-types.md#length-encoded-strings) info.
  * If (status flags & `SERVER_SESSION_STATE_CHANGED`) and `session_tracking_supported` (see [CLIENT\_SESSION\_TRACK](../1-connecting/connection.md)):
    * [string](../protocol-data-types.md#length-encoded-strings) [session state info](ok_packet.md#session-state-info).

The length-encoded info string is not always included in the packet. Check the length of the packet to detect if there is data after the warning count. For the first `OK_Packet` in the connection it contains (if present) the [SSL certificate verification signature](https://mariadb.org/mission-impossible-zero-configuration-ssl/). For the following `OK_Packets` it contains (if present) various human-readable information.

## Server status flag

Values of server status flags:

| Flag                                   | Value | Details                                                                                                                                                         |
| -------------------------------------- | ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| SERVER\_STATUS\_IN\_TRANS              | 1     | A transaction is currently active.                                                                                                                              |
| SERVER\_STATUS\_AUTOCOMMIT             | 2     | Autocommit mode is set.                                                                                                                                         |
| SERVER\_MORE\_RESULTS\_EXISTS          | 8     | More results exists (more packets will follow).                                                                                                                 |
| SERVER\_QUERY\_NO\_GOOD\_INDEX\_USED   | 16    | Set if [EXPLAIN](../../sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain.md) would've shown Range checked for each record.    |
| SERVER\_QUERY\_NO\_INDEX\_USED         | 32    | The query did not use an index.                                                                                                                                 |
| SERVER\_STATUS\_CURSOR\_EXISTS         | 64    | When using `COM_STMT_FETCH`, indicate that current cursor still has result.                                                                                     |
| SERVER\_STATUS\_LAST\_ROW\_SENT        | 128   | When using `COM_STMT_FETCH`, indicate that current cursor has finished to send results.                                                                         |
| SERVER\_STATUS\_DB\_DROPPED            | 1<<8  | Database has been dropped.                                                                                                                                      |
| SERVER\_STATUS\_NO\_BACKSLASH\_ESCAPES | 1<<9  | Current escape mode is "no backslash escape".                                                                                                                   |
| SERVER\_STATUS\_METADATA\_CHANGED      | 1<<10 | A DDL change did have an impact on an existing `PREPARE` (an automatic re-prepare has been executed).                                                           |
| SERVER\_QUERY\_WAS\_SLOW               | 1<<11 | The query was slower than [long\_query\_time](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#long_query_time). |
| SERVER\_PS\_OUT\_PARAMS                | 1<<12 | This result set contains stored procedure output parameter.                                                                                                     |
| SERVER\_STATUS\_IN\_TRANS\_READONLY    | 1<<13 | Current transaction is a read-only transaction.                                                                                                                 |
| SERVER\_SESSION\_STATE\_CHANGED        | 1<<14 | Session state change. See [session change type](ok_packet.md#session-change-type) for more information.                                                         |

## Session state info

* While packet has remaining data:
  * [int<1>](../protocol-data-types.md#fixed-length-integers) [session change type](ok_packet.md#session-change-type).
  * If (session-change-type != `SESSION_TRACK_STATE_CHANGE`):
    * [int](../protocol-data-types.md#length-encoded-integers) total length.
  * [string](../protocol-data-types.md#length-encoded-strings) session data change.

## Session change type

| Change Type | Flag                                         |
| ----------- | -------------------------------------------- |
| 0           | SESSION\_TRACK\_SYSTEM\_VARIABLES            |
| 1           | SESSION\_TRACK\_SCHEMA                       |
| 2           | SESSION\_TRACK\_STATE\_CHANGE                |
| 3           | SESSION\_TRACK\_GTIDS                        |
| 4           | SESSION\_TRACK\_TRANSACTION\_CHARACTERISTICS |
| 5           | SESSION\_TRACK\_TRANSACTION\_STATE           |

### Session Data Change

Each type of data has its own kind of format:

#### **SESSION\_TRACK\_SCHEMA**

* [string](../protocol-data-types.md#length-encoded-strings) new current schema.

#### **SESSION\_TRACK\_SYSTEM\_VARIABLES**

While there is remaining data:

* [string](../protocol-data-types.md#length-encoded-strings) variable data.

For each variable data:

* [string](../protocol-data-types.md#length-encoded-strings) variable name.
* [string](../protocol-data-types.md#length-encoded-strings) variable value.

{% hint style="info" %}
Possible tracked variables list is tracked by [session\_track\_system\_variables](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md) special variable value description:

* [redirect\_url](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#redirect_url): format is `mariadb/mysql:[<user>[:<password>]@]<host>[:<port>]/[<db>[?<opt1>=<value1>[&<opt2>=<value2>]]]`. Possible options:
  * `ttl` : cache timeout in ms to remember redirection, in order to reconnect directly to new host. 0=no caching
{% endhint %}

#### **SESSION\_TRACK\_STATE\_CHANGE**

Indicates if session state changes occurred. The value is represented as `1`.

* [string](../protocol-data-types.md#length-encoded-strings) `1` if session state tracking was enabled.

#### **SESSION\_TRACK\_GTIDS**

This tracker is not implemented by MariaDB.

#### **SESSION\_TRACK\_TRANSACTION\_CHARACTERISTICS**

* [string](../protocol-data-types.md#length-encoded-strings) Transaction characteristics.

Transaction characteristics is the set of SQL statements that reproduce the type and state of the current transaction. It can consist of the following SQL statements:

```sql
SET TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;
SET TRANSACTION ISOLATION LEVEL READ COMMITTED;
SET TRANSACTION ISOLATION LEVEL REPEATABLE READ;
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
START TRANSACTION;
START TRANSACTION WITH CONSISTENT SNAPSHOT;
START TRANSACTION WITH CONSISTENT SNAPSHOT, READ ONLY;
START TRANSACTION WITH CONSISTENT SNAPSHOT, READ WRITE;
SET TRANSACTION READ ONLY;
SET TRANSACTION READ WRITE;
XA START <XA specification>;
```

#### **SESSION\_TRACK\_TRANSACTION\_STATE**

* [string](../protocol-data-types.md#length-encoded-strings) Transaction state string.

The transaction state string is always 8 characters long. The characters, in order, are:

1. No transaction: `_` Explicit transaction: `T` Implicit transaction: `I`
2. Transaction read safe: `_` Transaction read unsafe: `r`
3. Unknown transaction type: `_` Read-only transaction: `R`
4. Transaction write safe: `_` Transaction write unsafe: `w`
5. Unknown transaction type: `_` Read-write transaction: `W`
6. Transaction statement safe: `_` Transaction statement unsafe: `s`
7. Transaction does not have resultsets: `_` Transaction with result sets: `S`
8. No locked tables: `_` Tables have been locked: `L`

## Notes

* To determine if session tracking is enabled, check if the [CLIENT\_SESSION\_TRACK](../1-connecting/connection.md) flag is set in `server_capabilities`.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
