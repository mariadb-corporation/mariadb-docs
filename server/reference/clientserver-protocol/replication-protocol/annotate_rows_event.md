---
description: >-
  This event accompanies row-based events to provide the original SQL query
  text, which is useful for auditing and debugging replication.
---

# ANNOTATE\_ROWS\_EVENT

`ANNOTATE_ROWS_EVENT` events accompany row events and describe the query which caused the row event.

You can enable this with [--binlog-annotate-row-events](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) (default on).

In the binary log, each `ANNOTATE_ROWS` event precedes the corresponding Table map event.

For additional information refer to the [annotate\_rows\_log\_event](../../../clients-and-utilities/logging-tools/mariadb-binlog/annotate_rows_log_event.md) documentation.

{% hint style="info" %}
The master server sends `ANNOTATE_ROWS_EVENT` events only if the replica server connects with the `BINLOG_SEND_ANNOTATE_ROWS_EVENT` flag (value is 2) in the `COM_BINLOG_DUMP` replica registration phase.
{% endhint %}

## Header

* Event Type is 160 (0xa0).

## Fields

* [string](../protocol-data-types.md#fixed-length-bytes) The SQL statement (not null-terminated).

## Complete Example with CRC32

```
ee b7 15 5a a0 01 00 00  00 36 00 00 00 80 0b 00  ...Z.....6......
00 00 00 69 6e 73 65 72  74 20 69 6e 74 6f 20 74  ...insert into t
65 73 74 2e 74 34 20 76  61 6c 75 65 73 28 31 30  est.t4 values(10
30 29 6d 4c 42 33                                 0)mLB3
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
