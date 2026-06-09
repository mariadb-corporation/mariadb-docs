---
description: >-
  All structures and type definitions for the Binglog/Replication API are
  defined in include/mariadb_rpl.h.
---

# Binlog/API Data Structures

The following structures are used by the Binlog/Replication API:

| Structure           | Description                                                                                                      |
| ------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `MARIADB_STRING`    | Stores a string together with its length.                                                                        |
| `MARIADB_TIMESTAMP` | Stores a timestamp value used in `MYSQL_TYPE_TIMESTAMP` and `MYSQL_TYPE_TIMESTAMP2` columns.                     |
| `MARIADB_GTID`      | Stores a global transaction ID (domain ID, server ID, and sequence number).                                      |
| `MARIADB_RPL`       | Opaque replication handle representing a replication connection.                                                 |
| `MARIADB_RPL_EVENT` | Contains a common event header and a union of all event-specific structures returned by `mariadb_rpl_fetch()`.   |

## MARIADB\_STRING

`MARIADB_STRING` is a simple structure that stores a string together with its length. It is equivalent to `MYSQL_STRING` and `MYSQL_LEX_STRING.`

```sql
typedef struct {
  char *str;
  size_t length;
} MARIADB_STRING;
```

* `str` → Pointer to the character data.
* `length` → Length of the string in bytes.

## MARIADB\_TIMESTAMP

`MARIADB_TIMESTAMP` stores timestamp values for `MYSQL_TYPE_TIMESTAMP` and `MYSQL_TYPE_TIMESTAMP2` column data. It was introduced in MariaDB Connector/C 3.3.19 and 3.4.9 versions.

```sql
typedef struct {
  uint32_t second;
  uint32_r second_part;
} MARIADB_STRING;
```

* `second` → Represents the whole seconds portion of the timestamp.
* `second_part` → Represents the fractional seconds (microseconds).

## MARIADB\_GTID

`MARIADB_GTID` represents a Global Transaction ID (GTID).. A GTID uniquely specifies a transaction across a replication topology and is defined by three components: domain ID, server ID, and sequence number.

```sql
typedef struct st_mariadb_gtid {
  unsigned int domain_id;
  unsigned int server_id;
  unsigned long long sequence_nr;
} MARIADB_GTID;
```

* `domain_id` → The replication domain identifier.
* `server_id` → The ID of the server that originally committed the transaction.
* `sequence_nr` → The transaction’s sequence number within the domain.

## MARIADB\_RPL

`MARIADB_RPL` is the generic replication handle. It represents a replication connection and is passed to all Binlog/Replication API calls.&#x20;

* The `MARIADB_RPL` structure is **opaque.** Its internal members should not be accessed directly.
* To configure replication options, use `mariadb_rpl_optionsv()`.
* To retrieve replication options, use `mariadb_rpl_get_optionsv()`.

## Events

### MARIADB\_RPL\_EVENT

`MARIADB_RPL_EVENT` is the structure returned by `mariadb_rpl_fetch()` API function. It contains a common event header followed by a union of event-specific structures. The active union member is determined by the value of `event_type`. &#x20;

```sql
typedef struct st_mariadb_rpl_event
{
  /* common header */
  MA_MEM_ROOT memroot;
  unsigned int checksum;
  char ok;
  enum mariadb_rpl_event event_type;
  unsigned int timestamp;
  unsigned int server_id;
  unsigned int event_length;
  unsigned int next_event_pos;
  unsigned short flags;
  /****************/
  union {
    struct st_mariadb_rpl_rotate_event rotate;
    struct st_mariadb_rpl_query_event query;
    struct st_mariadb_rpl_format_description_event format_description;
    struct st_mariadb_rpl_gtid_list_event gtid_list;
    struct st_mariadb_rpl_checkpoint_event checkpoint;
    struct st_mariadb_rpl_xid_event xid;
    struct st_mariadb_rpl_gtid_event gtid;
    struct st_mariadb_rpl_annotate_rows_event annotate_rows;
    struct st_mariadb_rpl_table_map_event table_map;
    struct st_mariadb_rpl_rand_event rand;
    struct st_mariadb_rpl_encryption_event encryption;
    struct st_mariadb_rpl_intvar_event intvar;
    struct st_mariadb_rpl_uservar_event uservar;
    struct st_mariadb_rpl_rows_event rows;
    struct st_mariadb_rpl_heartbeat_event heartbeat;
    /* The following events were added in version 3.3.5 */
    struct st_mariadb_rpl_xa_prepare_log_event xa_prepare_log;
    struct st_mariadb_begin_load_query_event begin_load_query;
    struct st_mariadb_execute_load_query_event execute_load_query;
    struct st_mariadb_gtid_log_event gtid_log;
    struct st_mariadb_start_encryption_event start_encryption;
    struct st_mariadb_rpl_previous_gtid_event previous_gtid;
  } event;
} MARIADB_RPL_EVENT;
```

**Field Validation**

* `memroot` → Internal memory pool used to allocate event data.&#x20;
* `checksum` → CRC32 checksum of the event (if binlog checksums are enabled).
* `ok` → Non-zero if the event was received without error.
* `event_type` → Identifies the event type and determines which union member is active.
* `timestamp` → Unix timestamp (seconds since epoch) when the event was created.
* `server_id` → Server ID of the server that generated the event.
* `event_length` → Total length of the event in bytes, including the header.
* `next_event_pos` → Binary log position of the next event.
* flags → Bitmask of event flags (see Replication API types and definitions for flag values).

#### Event Union Behavior

The `event` union defines one member for each supported replication event type. Only the member that corresponds to the current `event_type` value contains valid data. \
The following sections describe each event type and its associated structure:

**ANNOTATE\_ROWS\_EVENT**

`event_type` value= 160 (`0xA0`)

This event contains the statement that produced the subsequent row‑change event in the binary log stream. It is only generated if the client connects with the `MARIADB_RPL_BINLOG_SEND_ANNOTATE_ROWS` flag enabled.

```sql
struct st_mariadb_rpl_annotate_rows_event {
  MARIADB_STRING statement;
};
```

* `statement` → The SQL statement that triggered the row‑change event.

**Notes**

* `ANNOTATE_ROWS_EVENT` is sent only when the replication handle was opened with the `MARIADB_RPL_BINLOG_SEND_ANNOTATE_ROWS` flag, set through `mariadb_rpl_optionsv()`.
* If the flag is not set, this event will not be included in the binary log stream.

**BINLOG\_CHECKPOINT\_EVENT**

`event_type` value= 161 (`0xA1`)

Written to the binary log to record the oldest binary log file that is still required for recovery. This event ensures that replication and recovery processes know which binary log files must be retained to guarantee consistency.

```sql
struct st_mariadb_rpl_checkpoint_event {
  MARIADB_STRING filename;
};
```

* `filename` → The name of the oldest binary log file needed for crash recovery and replication consistency.

**START\_ENCRYPTION\_EVENT**

`event_type` value= 164 (`0xA4`)

Written to the binary log when encryption is enabled on the source server. This event records the encryption scheme and key version used for subsequent event

```sql
struct st_mariadb_rpl_encryption_event {
  char scheme;
  unsigned int key_version;
  char *nonce;
};
```

* `scheme` → Encryption scheme identifier.
* `key_version` → Version of the encryption key used for encrypted log data.
* `nonce` → Nonce (number used once) used in the encryption process.

{% hint style="info" %}
- Encrypted event data is available only when reading directly from a binary log file.
- When a client connects to a live source server, the server always sends **unencrypted events**, even if encryption is enabled at rest.
{% endhint %}

**FORMAT\_DESCRIPTION\_EVENT**

`event_type` value= 15 (`0x0F`)

Written at the beginning of every binary log file, at position 4. This event describes the format of all subsequent events in the file. For MariaDB 10.0 and later, the format field is always set to `4`.

```
struct st_mariadb_rpl_format_description_event
{
  uint16_t format;
  char *server_version;
  uint32_t timestamp;
  uint8_t header_len;
  /* Added in 3.3.5 */
  MARIADB_STRING post_header_lengths;
};
```

* `format` → Binary log format version. Always `4` for MariaDB 10.0 and later.
* `server_version` → Version string of the server that created the binary log.
* `timestamp` → Unix timestamp of when the binary log file was created.
* `header_len` → Length of the fixed event header in bytes.
* `post_header_lengths` → Array of post‑header lengths for each event type. Added in Connector/C 3.3.5.

{% hint style="info" %}
- This event always appears at the start of a binary log file (position 4).
- It defines the structure and header lengths for all subsequent events, ensuring compatibility between server and client replication components.
{% endhint %}

**GTID\_EVENT**

`event_type` value= 162 (`0xA2`)

Marks the start of a new global transaction event group. This event is written to the binary log before the events belonging to the transaction.

```sql
struct st_mariadb_rpl_gtid_event {
  uint64_t sequence_nr;
  uint32_t domain_id;
  uint8_t flags;
  uint64_t commit_id;
};
```

* `sequence_nr` → Sequence number of the transaction within the replication domain.
* `domain_id` → Identifier of the replication domain.
* `flags` → Bitmask of event flags.
* `commit_id` → Commit ID used to coordinate parallel replication.

**Notes**:

* The `GTID_EVENT` ensures that each transaction is uniquely identified across the replication topology.
* It captures all events belonging to the transaction, ensuring replication consumers can group and track them consistently.

**GTID\_LIST\_EVENT**

`event_type` value= 163 (`0xA3`)

Written at the start of every binary log file to record the current replication state. This event contains the last GTID seen for each replication domain, allowing replicas to determine where to resume replication after a reconnect.

```sql
struct st_mariadb_rpl_gtid_list_event {
  uint32_t gtid_cnt;
  MARIADB_GTID *gtid;
};
```

* `gtid_cnt` → Number of GTID entries in the `gtid` array.
* `gtid` → Array of `MARIADB_GTID` structures, one per replication domain.

{% hint style="info" %}
- The `GTID_LIST_EVENT` provides a snapshot of the replication state at the beginning of a binary log file.
- By recording the last GTID for each domain, it ensures replicas can safely resume replication after interruptions.
{% endhint %}

**HEARTBEAT\_LOG\_EVENT**

`event_type` value= 27 (`0x1B`)

Sent over the network by the source server to replicas when there are no binary log events to transmit. This event confirms that the source server is still alive. It is never written to the binary log file itself.

```sql
struct st_mariadb_rpl_heartbeat_event {
  uint32_t timestamp;
  uint32_t next_position;
  uint8_t type;
  uint16_t flags;
};
```

* `timestamp` → Always `0` for heartbeat events.
* `next_position` → Always points to the last known binary log position.
* `type` → Always `0x1B`, the constant identifying heartbeat events.
* `flags` → Always `LOG_EVENT_ARTIFICIAL_F (0x20)`, marking the event as artificial.

**INTVAR\_EVENT**

`event_type` value=5 (`0x05`)

Written to the binary log immediately before a `QUERY_EVENT` whenever the statement uses an `AUTO_INCREMENT` value or the `LAST_INSERT_ID()` function.

```sql
struct st_mariadb_rpl_intvar_event {
  unsigned long long value;
  uint8_t type;
};
```

* `value` → The integer value, either the next auto‑increment value or the result of `LAST_INSERT_ID()`.
* `type` → Indicates the variable type.

Valid values for `type` are:

| Value  | Constant         | Description                                |
| ------ | ---------------- | ------------------------------------------ |
| `0x01` | `LAST_INSERT_ID` | Value is the result of `LAST_INSERT_ID()`. |
| `0x02` | `INSERT_ID`      | Value is the next `AUTO_INCREMENT` value.  |

**QUERY\_EVENT**

`event_type` value=2 (`0x02`)

Contains a SQL statement. This event is written to the binary log when:

* The server `binlog_format` is set to `STATEMENT` (statement‑based replication).
* A `DDL` statement is executed.
* A `COMMIT` is issued for a non‑transactional storage engine.

```sql
struct st_mariadb_rpl_query_event {
  uint32_t thread_id;
  uint32_t seconds;
  MARIADB_STRING database;
  uint32_t errornr;
  MARIADB_STRING status;
  MARIADB_STRING statement;
};
```

* `thread_id` → ID of the client thread that executed the statement on the source server.
* `seconds` → Time in seconds that the statement took to execute.
* `database` → Name of the default database at the time the statement was executed.
* `errornr` → Error number if the statement produced an error; `0` on success.
* `status` → Status variables blob (encoded server status at the time of execution).
* `statement` → The SQL statement text.

{% hint style="info" %}
- `QUERY_EVENT` is central to **statement‑based replication**, ensuring that SQL statements are replayed consistently on replicas.
- Even in row‑based replication, certain operations (like DDL or non‑transactional commits) still generate `QUERY_EVENT` entries.
{% endhint %}

**RAND\_EVENT**

`event_type` value=13 (`0x0D`)

Written to the binary log immediately before a `QUERY_EVENT` that uses the `RAND()` function. This event records the seed values so that replicas can reproduce the same pseudo‑random sequence.

```sql
struct st_mariadb_rpl_rand_event {
  unsigned long long first_seed;
  unsigned long long second_seed;
};
```

* `first_seed` → First seed value for the `RAND()` function.
* `second_seed` → Second seed value for the `RAND()` function.

{% hint style="info" %}
- The `RAND_EVENT` ensures deterministic replication of statements that rely on pseudo‑random values.
- By recording both seed values, replicas can generate the same sequence of random numbers as the source server, maintaining consistency across the replication topology.
{% endhint %}

**ROTATE\_EVENT**

`event_type` value=4 (`0x04`)

Written at the end of a binary log file to indicate that the next event will appear in a new binary log file.

```sql
struct st_mariadb_rpl_rotate_event {
  unsigned long long position;
  MARIADB_STRING filename;
};
```

* `position` → Starting position in the new binary log file.
* `filename` → Name of the new binary log file.

**Notes**:

* The `ROTATE_EVENT` signals the transition between binary log files, ensuring replication clients know where to continue reading.
* It is always written at the end of a binary log file and points to the beginning of the next file.

\
**WRITE\_ROWS\_EVENT\_V1, UPDATE\_ROWS\_EVENT\_V1, DELETE\_ROWS\_EVENT\_V1**

**Event Types** with value&#x73;**:**

* `WRITE_ROWS_EVENT_V1` → `23 (0x17)`
* `UPDATE_ROWS_EVENT_V1` → `24 (0x18)`
* `DELETE_ROWS_EVENT_V1` → `25 (0x19)`

Row events are written to the binary log when the server `binlog_format` is set to **ROW**. All three event types share the same structure; the `type` field distinguishes the specific row operation (insert, update, or delete).

```sql
struct st_mariadb_rpl_rows_event {
  enum mariadb_row_event_type type;
  uint64_t table_id;
  uint16_t flags;
  uint32_t column_count;
  char *column_bitmap;
  char *column_update_bitmap;
  size_t row_data_size;
  void *row_data;
};
```

* `type` → Row operation type: write (insert), update, or delete. See Replication API Types and Definitions.
* `table_id` → References the table mapped by the preceding `TABLE_MAP_EVENT`.
* `flags` → Row event flags bitmask.
* `column_count` → Number of columns in the table.
* `column_bitmap` → Bitmap of columns present in the row image; one bit per column.
* `column_update_bitmap` → For `UPDATE_ROWS_EVENT`: bitmap of columns present in the after‑image. `NULL` for write and delete events.
* `row_data_size` → Size in bytes of `row_data`.
* `row_data` → Raw encoded row data. Use `mariadb_rpl_extract_rows()` to decode.

\
**TABLE\_MAP\_EVENT**

`event_type` value=`19 (0x13)`&#x20;

Written before each row event (in row‑based replication) to map a table ID to a fully qualified table name and provide column metadata for the rows that follow.

```sql
struct st_mariadb_rpl_table_map_event {
  unsigned long long table_id;
  MARIADB_STRING database;
  MARIADB_STRING table;
  unsigned int column_count;
  MARIADB_STRING column_types;
  MARIADB_STRING metadata;
  char *null_indicator;
};
```

* `table_id` → Numeric table ID used in subsequent row events to reference this table.
* `database` → Name of the database containing the table.
* `table` → Name of the table.
* `column_count` → Number of columns in the table.
* `column_types` → Array of column type identifiers, one byte per column.
* `metadata` → Type‑specific metadata for each column (length varies by column type).
* `null_indicator` → Bitmap indicating which columns are nullable; one bit per column.

**USERVAR\_EVENT**

`event_type` value=`14 (0x0E)`&#x20;

Written to the binary log before a `QUERY_EVENT` that references a user variable. This event records the variable’s name, type, and value so the replica can set it before executing the statement.

```sql
struct st_mariadb_rpl_uservar_event {
  MARIADB_STRING name;
  uint8_t is_null;
  uint8_t type;
  uint32_t charset_nr;
  MARIADB_STRING value;
  uint8_t flags;
};
```

* `name` → Name of the user variable.
* `is_null` → Non‑zero if the variable’s value is `NULL`.
* `type` → Data type of the variable value.
* `charset_nr` → Collation ID for string values.
* `value` → Encoded value of the variable. Empty if `is_null` is non‑zero.
* `flags` → Reserved flags field.

**XID\_EVENT**

`event_type` value=`16 (0x10)`

Written to the binary log when a transactional storage engine commits a transaction. This event records the XA transaction number and signals the end of the transaction’s event group.

```
struct st_mariadb_rpl_xid_event {
  uint64_t transaction_nr;
};
```

* `transaction_nr` → The XA transaction number for this commit.

**Notes:**

* The `XID_EVENT` marks the successful commit of a transaction in engines that support XA transactions.
* It serves as the boundary marker for the transaction’s event group, ensuring replicas apply the transaction atomically.

## See Also

* [MariaDB Binlog/Replication API Reference](./)
* [Replication API Types and Definitions](replication-api-types-and-definitions.md)
* [Replication API Function Reference](replication-api-function-reference/)
