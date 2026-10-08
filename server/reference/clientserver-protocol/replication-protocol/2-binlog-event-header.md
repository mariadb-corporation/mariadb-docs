---
description: >-
  Every binary log event starts with a standardized header containing metadata
  such as the timestamp, event type, server ID, and event size.
---

# 2-Binlog Event Header

All the [binlog events](1-binlog-events.md) stored in a [binary log file](../../../server-management/server-monitoring-logs/binary-log/) have a common structure:

* An event header;
* Event data.

## Event Header Structure, 19 Bytes

* [uint<4>](../protocol-data-types.md#fixed-length-bytes) Timestamp (creation time).
* [uint<1>](../protocol-data-types.md#fixed-length-bytes) [Event Type](2-binlog-event-header.md#event-type) (type\_code).
* [uint<4>](../protocol-data-types.md#fixed-length-bytes) Server\_id (server which created the event).
* [uint<4>](../protocol-data-types.md#fixed-length-bytes) Event Length (header + data).
* [uint<4>](../protocol-data-types.md#fixed-length-bytes) Next Event position.
* [uint<2>](../protocol-data-types.md#fixed-length-bytes) [Event flags](2-binlog-event-header.md#event-flag).

{% hint style="info" %}
**Note**: if `CRC32` is in use, the Event Length is 4 bytes bigger in size. The 4 bytes `CRC32` are written at the end of the event (just after the last 'data' byte).
{% endhint %}

## Encrypted Binlog Events

For encrypted binlog events, only the event length is in plaintext, and everything else is encrypted.

To decrypt the binlog event:

* Store the event length in memory;
* Move the timestamp into the event length position;
* Decrypt the whole payload except the first four bytes;
* Move the timestamp back to its original position;
* Copy the original event length back to its position.

Regardless of the cipher used to encrypt the binlogs, the encrypted data are the same size as the original unencrypted event. For events that are encrypted in CBC mode, and whose length is not a multiple of the cipher block size, the final partial block is encrypted using a form of [residual block termination](https://en.wikipedia.org/wiki/Residual_block_termination):

* Encrypt the current IV of the binlog file in ECB mode;
* `XOR` the remaining bytes with the encrypted IV.

## Event Type

| Hex  | Event type description                                                      |
| ---- | --------------------------------------------------------------------------- |
| 0x02 | [QUERY\_EVENT](query_event.md)                                              |
| 0x03 | [STOP\_EVENT](stop_event.md)                                                |
| 0x04 | [ROTATE\_EVENT](rotate_event.md)                                            |
| 0x10 | [XID\_EVENT](xid_event.md)                                                  |
| 0x0d | [RAND\_EVENT](rand_event.md)                                                |
| 0x0e | [USER\_VAR\_EVENT](user_var_event.md)                                       |
| 0x0f | [FORMAT\_DESCRIPTION\_EVENT](format_description_event.md)                   |
| 0x13 | [TABLE\_MAP\_EVENT](table_map_event.md)                                     |
| 0x1b | [HEARTBEAT\_LOG\_EVENT](heartbeat_log_event.md)                             |
| 0xa0 | [ANNOTATE\_ROWS\_EVENT](annotate_rows_event.md)                             |
| 0xa1 | [BINLOG\_CHECKPOINT\_EVENT](binlog_checkpoint_event.md)                     |
| 0xa2 | [GTID\_EVENT](gtid_event.md)                                                |
| 0xa3 | [GTID\_LIST\_EVENT](gtid_list_event.md)                                     |
| 0xa4 | [START\_ENCRYPTION\_EVENT](start_encryption_event.md)                       |
| 0xa5 | [QUERY\_COMPRESSED\_EVENT](query_event.md)                                  |
| 0xa6 | [WRITE\_ROWS\_COMPRESSED\_V1](rows_event_v1v2-rows_compressed_event_v1.md)  |
| 0xa7 | [UPDATE\_ROWS\_COMPRESSED\_V1](rows_event_v1v2-rows_compressed_event_v1.md) |
| 0xa8 | [DELETE\_ROWS\_COMPRESSED\_V1](rows_event_v1v2-rows_compressed_event_v1.md) |
| 0xa9 | [WRITE\_ROWS\_V1](rows_event_v1v2-rows_compressed_event_v1.md)              |
| 0xaa | [UPDATE\_ROWS\_V1](rows_event_v1v2-rows_compressed_event_v1.md)             |
| 0xab | [DELETE\_ROWS\_V1](rows_event_v1v2-rows_compressed_event_v1.md)             |

## Fake Events

These are generated on the fly, never written:

| Hex  | Event type description                             |
| ---- | -------------------------------------------------- |
| 0x04 | [FAKE\_ROTATE\_EVENT](fake-rotate_event.md)        |
| 0xa3 | [FAKE\_GTID\_LIST\_EVENT](fake-gtid_list-event.md) |

## Event Flag

| Hex    | Event flag description                                                                                                                                                                                                                                                                                                                              |
| ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0x0001 | `LOG_EVENT_BINLOG_IN_USE_F` This flag only makes sense for `Format_description_log_event`. It is set when the event is written, and _reset_ when a binlog file is closed (yes, it's the only case when MySQL modifies already written part of binlog). Thus it is a reliable indicator that binlog was closed correctly.                            |
| 0x0002 | `LOG_EVENT_FORCED_ROTATE_F` (unused).                                                                                                                                                                                                                                                                                                               |
| 0x0004 | `LOG_EVENT_THREAD_SPECIFIC_F` If the query depends on the thread (for example: `TEMPORARY TABLE`).                                                                                                                                                                                                                                                  |
| 0x0008 | `LOG_EVENT_SUPPRESS_USE_F` Suppress the generation of 'USE' statements before the actual statement. This flag should be set for any events that does not need the current database set to function correctly. Most notable cases are '`CREATE DATABASE`' and '`DROP DATABASE`'.                                                                     |
| 0x0010 | `LOG_EVENT_UPDATE_TABLE_MAP_VERSION_F` (unused).                                                                                                                                                                                                                                                                                                    |
| 0x0020 | `LOG_EVENT_ARTIFICIAL_F` Artificial events are created arbitrarily and not written to binary log.These events should not update the master log position when slave SQL thread executes them.                                                                                                                                                        |
| 0x0040 | `LOG_EVENT_RELAY_LOG_F` Events with this flag set are created by slave IO thread and written to relay log.                                                                                                                                                                                                                                          |
| 0x0080 | `LOG_EVENT_IGNORABLE_F` For an event, 'e', carrying a type code, that a slave,'s', does not recognize, 's' will check 'e' for `LOG_EVENT_IGNORABLE_F`, and if the flag is set, then 'e'is ignored. Otherwise, 's' acknowledges that it has found an unknown event in the relay log.                                                                 |
| 0x0100 | `LOG_EVENT_NO_FILTER_F` (no description yet).                                                                                                                                                                                                                                                                                                       |
| 0x0200 | `LOG_EVENT_MTS_ISOLATE_F` (no description yet).                                                                                                                                                                                                                                                                                                     |
| 0x8000 | `LOG_EVENT_SKIP_REPLICATION_F` Flag set by application creating the event (with `@@skip_replication`);the replica skips replication of such events, if `--replicate-events-marked-for-skip` is not set to `REPLICATE`. This is a MariaDB flag; we allocate it from the end of the available values to reduce risk of conflict with new MySQL flags. |

### Event Header Example of FORMAT\_DESCRIPTION\_EVENT

This is the first event in the binlog file at pos 4:

```
a4 85 9e 59 0f 8c 27 00  00 f5 00 00 00 f9 00 00  ...Y..'.........
00 00 00 04 00 31 30 2e  31 2e 32 34 2d 4d 61 72  .....10.1.24-Mar
69 61 44 42 00 6c 6f 67  00 00 00 00 00 00 00 00  iaDB.log....
...
...
```

### Interpretation of First 19 Bytes of the Event (the Event Header)

* a4 85 9e 59 \[4] Timestamp => 59 9e 85 a4 => 1503561124 = 2017-08-24 09:52:04
* 0f \[1] Event Type = 0x0f = FORMAT\_DESCRIPTION\_EVENT
* 8c 27 00 00 \[4] Server\_id => 00 00 27 8c = 10124
* f5 00 00 00 \[4] Event length => 00 00 00 f5 => 245
* f9 00 00 00 \[4] Next Event pos => 00 00 00 f9 => 249 (pos 4 + event size)
* 00 00 \[2] Event flags = 0

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
