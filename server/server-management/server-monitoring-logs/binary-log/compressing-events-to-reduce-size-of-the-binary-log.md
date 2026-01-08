---
description: >-
  Guide to using the `log_bin_compress` system variable to compress binary log
  events, reducing storage usage and network bandwidth during replication.
---

# Compressing Events to Reduce Size of the Binary Log

Selected events in the [binary log](./) can be optionally compressed, to save space in the binary log on disk and in network transfers.

The events that can be compressed are the events that normally can be of a significant size: Query events (for DDL and DML in [statement-based](binary-log-formats.md#statement-based) [replication](../../../ha-and-performance/standard-replication/)), and row events (for DML in [row-based](binary-log-formats.md#row-based) [replication](../../../ha-and-performance/standard-replication/)).

Compression is fully transparent. Events are compressed on the primary before being written into the binary log, and are uncompressed by the I/O thread on the replica before being written into the relay log. The [mariadb-binlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/) command will likewise uncompress events for its output.

Currently, the zlib compression algorithm is used to compress events.

Compression will have the most impact when events are of a non-negligible size, as each event is compressed individually. For example, batch INSERT statements that insert many rows or large values, or row-based events that touch a number of rows in one query.

The [log\_bin\_compress](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin_compress) option is used to enable compression of events. Only events with data (query text or row data) above a certain size are compressed; the limit is set with the [log\_bin\_compress\_min\_len](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin_compress_min_len) option.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
