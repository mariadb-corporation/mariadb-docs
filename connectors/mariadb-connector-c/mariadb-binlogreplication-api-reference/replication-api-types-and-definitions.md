---
description: >-
  All enumerations and preprocessor definitions for the Binglog/Replication API
  are defined in include/mariadb_rpl.h.
---

# Replication API Types and Definitions

The following API types and definitions are used by the Binlog/Replication API:

| Type or Definition       | Description                                                                                                                   |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| `mariadb_rpl_option`     | Options for configuring a `MARIADB_RPL` replication handle. Used by `mariadb_rpl_optionsv()` and `mariadb_rpl_get_optionsv()` |
| `mariadb_rpl_event`      | Event type identifiers returned in the `event_type` field of `MARIADB_RPL_EVENT`.                                             |
| `mariadb_row_event_type` | Row operation type for write, update, and delete row events.                                                                  |
| `Flags`                  | Bitmask constants for controlling binary log dump behaviour. Passed via the `MARIADB_RPL_FLAGS` option.                       |

## mariadb\_rpl\_option

`mariadb_rpl_option` is the enumeration of options accepted by `mariadb_rpl_optionsv()` and `mariadb_rpl_get_optionsv()`. Options are used to configure a `MARIADB_RPL` handle before opening a binary log stream.

```sql
enum mariadb_rpl_option {
  MARIADB_RPL_FILENAME,       /* Filename and length */
  MARIADB_RPL_START,          /* Start position */
  MARIADB_RPL_SERVER_ID,      /* Server ID */
  MARIADB_RPL_FLAGS,          /* Protocol flags */
  MARIADB_RPL_GTID_CALLBACK,  /* GTID callback function */
  MARIADB_RPL_GTID_DATA,      /* GTID data */
  MARIADB_RPL_BUFFER
};
```

**Option descriptions**

* `MARIADB_RPL_FILENAME` → Name of the binary log file to open, and its length in bytes.
* `MARIADB_RPL_START` → Binary log position from which to start reading events.
* `MARIADB_RPL_SERVER_ID` → The server ID to use when registering this client as a replica.
* `MARIADB_RPL_FLAGS` → Bitmask of protocol flags controlling binary log dump behavior. See Flags for valid values.
* `MARIADB_RPL_GTID_CALLBACK` → Pointer to a GTID callback function, called when a GTID event is received.
* `MARIADB_RPL_GTID_DATA` → User data pointer passed to the GTID callback function.
* `MARIADB_RPL_BUFFER` → Pre‑allocated buffer for event data, and its size.

## mariadb\_rpl\_event

`mariadb_rpl_event` is the enumeration of all binary log event types. The `event_type` field of `MARIADB_RPL_EVENT` is set to one of these values to indicate which event structure is active in the event union.

```sql
enum mariadb_rpl_event {
  UNKNOWN_EVENT= 0,
  START_EVENT_V3= 1,
  QUERY_EVENT= 2,
  STOP_EVENT= 3,
  ROTATE_EVENT= 4,
  INTVAR_EVENT= 5,
  LOAD_EVENT= 6,
  SLAVE_EVENT= 7,
  CREATE_FILE_EVENT= 8,
  APPEND_BLOCK_EVENT= 9,
  EXEC_LOAD_EVENT= 10,
  DELETE_FILE_EVENT= 11,
  NEW_LOAD_EVENT= 12,
  RAND_EVENT= 13,
  USER_VAR_EVENT= 14,
  FORMAT_DESCRIPTION_EVENT= 15,
  XID_EVENT= 16,
  BEGIN_LOAD_QUERY_EVENT= 17,
  EXECUTE_LOAD_QUERY_EVENT= 18,
  TABLE_MAP_EVENT = 19,

  PRE_GA_WRITE_ROWS_EVENT = 20, /* deprecated */
  PRE_GA_UPDATE_ROWS_EVENT = 21, /* deprecated */
  PRE_GA_DELETE_ROWS_EVENT = 22, /* deprecated */

  WRITE_ROWS_EVENT_V1 = 23,
  UPDATE_ROWS_EVENT_V1 = 24,
  DELETE_ROWS_EVENT_V1 = 25,
  INCIDENT_EVENT= 26,
  HEARTBEAT_LOG_EVENT= 27,
  IGNORABLE_LOG_EVENT= 28,
  ROWS_QUERY_LOG_EVENT= 29,
  WRITE_ROWS_EVENT = 30,
  UPDATE_ROWS_EVENT = 31,
  DELETE_ROWS_EVENT = 32,
  GTID_LOG_EVENT= 33,
  ANONYMOUS_GTID_LOG_EVENT= 34,
  PREVIOUS_GTIDS_LOG_EVENT= 35,
  TRANSACTION_CONTEXT_EVENT= 36,
  VIEW_CHANGE_EVENT= 37,
  XA_PREPARE_LOG_EVENT= 38,

  /*
    Add new events here - right above this comment!
    Existing events (except ENUM_END_EVENT) should never change their numbers
  */

  /* New MySQL/Sun events are to be added right above this comment */
  MYSQL_EVENTS_END,

  MARIA_EVENTS_BEGIN= 160,
  ANNOTATE_ROWS_EVENT= 160,
  BINLOG_CHECKPOINT_EVENT= 161,
  GTID_EVENT= 162,
  GTID_LIST_EVENT= 163,
  START_ENCRYPTION_EVENT= 164,
  QUERY_COMPRESSED_EVENT = 165,
  WRITE_ROWS_COMPRESSED_EVENT_V1 = 166,
  UPDATE_ROWS_COMPRESSED_EVENT_V1 = 167,
  DELETE_ROWS_COMPRESSED_EVENT_V1 = 168,
  WRITE_ROWS_COMPRESSED_EVENT = 169,
  UPDATE_ROWS_COMPRESSED_EVENT = 170,
  DELETE_ROWS_COMPRESSED_EVENT = 171,

  /* Add new MariaDB events here - right above this comment!  */

  ENUM_END_EVENT /* end marker */
};
```

## mariadb\_row\_event\_type

`mariadb_row_event_type` identifies the row operation performed by a `WRITE_ROWS_EVENT`, `UPDATE_ROWS_EVENT`, or `DELETE_ROWS_EVENT`.

```sql
enum mariadb_row_event_type {
  WRITE_ROWS= 0,
  UPDATE_ROWS= 1,
  DELETE_ROWS= 2
};
```

<table><thead><tr><th width="173.44439697265625">Value</th><th>Constant</th><th>Description</th></tr></thead><tbody><tr><td><code>0</code></td><td><code>WRITE_ROWS</code></td><td>A row was inserted. The <code>row_data</code> field contains the new row image.</td></tr><tr><td><code>1</code></td><td><code>UPDATE_ROWS</code></td><td>A row was updated.</td></tr><tr><td><code>2</code></td><td><code>DELETE_ROWS</code></td><td>A row was deleted. The <code>row_data</code> field contains the deleted row image. </td></tr></tbody></table>

## Flags

The following flags are passed as a bitmask to the `MARIADB_RPL_FLAGS` option via `mariadb_rpl_optionsv()`. Multiple flags can be combined using the bitwise OR operator (`|`) to control binary log dump behavior.

```sql
#define MARIADB_RPL_BINLOG_DUMP_NON_BLOCK 1
#define MARIADB_RPL_BINLOG_SEND_ANNOTATE_ROWS 2
#define MARIADB_RPL_IGNORE_HEARTBEAT (1 << 17)
```

## See Also

* [MariaDB Binlog/Replication API Reference](./)
* [Binlog/API Data Structures](binlog-api-data-structures.md)
* [Replication API Function Reference](replication-api-function-reference/)
