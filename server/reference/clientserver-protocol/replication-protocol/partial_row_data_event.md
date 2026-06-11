---
description: >-
  Carries a fragment of a Rows event that exceeded the replica's
  slave_max_allowed_packet; reassembled on the replica before execution.
---

# PARTIAL\_ROW\_DATA\_EVENT

When a [`ROWS_EVENT`](rows_event_v1v2-rows_compressed_event_v1.md) (for example `WRITE_ROWS_EVENT_V1`) is too large to be sent to a replica — that is, larger than the replica's `slave_max_allowed_packet` — the rows event is fragmented into sub-events of type `PARTIAL_ROW_DATA_EVENT` so that it can still be transmitted. The replica takes the content of each `PARTIAL_ROW_DATA_EVENT` in a group and joins them together into the original rows event, which is then executed as normal.

`PARTIAL_ROW_DATA_EVENT`s are written to the binary log sequentially, and the replica assembles them in the order they were binlogged. The maximum size of each `PARTIAL_ROW_DATA_EVENT` is determined by the system variable `binlog_row_event_fragment_threshold`.

The event is referred to as `Partial_rows_log_event` in the server source.

Added in MariaDB 12.3 ([MDEV-32570](https://jira.mariadb.org/browse/MDEV-32570)).

## Header

* `PARTIAL_ROW_DATA_EVENT`: Event Type is 172 (0xAC).

## Fields

* [uint<4>](../protocol-data-types.md#fixed-length-integers) Total number of fragments in the group.
* [uint<4>](../protocol-data-types.md#fixed-length-integers) Sequence number of this fragment within the group (1-based).
* [uint<1>](../protocol-data-types.md#fixed-length-integers) Flags.
* If (flags & `FL_ORIG_EVENT_SIZE`):
  * [uint<8>](../protocol-data-types.md#fixed-length-integers) Size of the original underlying rows event when reassembled on the replica.
* [string\<EOF>](../protocol-data-types.md#end-of-file-length-strings) Chunk of the original rows event data carried by this fragment. Runs to the end of the event body.

### Flags

| Flag                 | Value | Details                                                                                                                                              |
| -------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `FL_ORIG_EVENT_SIZE` | 0x01  | Set when the original rows-event size is included in this event. Set only for the first fragment in a group (i.e. the fragment with sequence number 1). |

## Notes

* The current binary log format supports a maximum rows-event size of 4 GB. Even if `slave_max_allowed_packet` is later raised above its present 1 GB cap, the per-fragment size of a `PARTIAL_ROW_DATA_EVENT` would not exceed 4 GB.
* When `mariadb-binlog` replays a group of `PARTIAL_ROW_DATA_EVENT`s, the [`TABLE_MAP_EVENT`](table_map_event.md) from the start of the group is re-emitted before the last fragment. The server treats each `BINLOG` base64 statement as standalone and closes tables after each one, so the table-map context must be re-established immediately before the final fragment — that is the fragment whose execution reassembles and runs the original rows event.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
