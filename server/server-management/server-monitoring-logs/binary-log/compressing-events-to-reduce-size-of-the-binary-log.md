---
description: >-
  Guide to using the `log_bin_compress` system variable to compress binary log
  events, reducing storage usage and network bandwidth during replication.
---

# Compressing Events to Reduce Size of the Binary Log

Selected events in the [binary log](./) can be optionally compressed, to save space in the binary log on disk (or, from MariaDB 12.3, in InnoDB tablespaces) and in network transfers.

Events that can be compressed are those that can be of significant size:&#x20;

* Query events (for DDL[^1] and DML[^2] in [statement-based](binary-log-formats.md#statement-based) [replication](../../../ha-and-performance/standard-replication/)), and&#x20;
* Row events (for DML[^2] in [row-based](binary-log-formats.md#row-based) [replication](../../../ha-and-performance/standard-replication/)).

Compression is fully transparent. Events are compressed on the primary before being written to the binary log, and are uncompressed by the I/O thread on the replica before being written to the relay log. The [mariadb-binlog](../../../clients-and-utilities/logging-tools/mariadb-binlog/) command will likewise uncompress events for its output.

The `zlib` compression algorithm is used to compress events.

Compression has the greatest impact when events are of a non-negligible size, as each event is compressed individually – like batch `INSERT` statements that add many rows or large values, or row-based events that affect a number of rows in one query.

The [log\_bin\_compress](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin_compress) option is used to enable compression of events. Only events with data (query text or row data) above a certain size are compressed; the limit is set with the [log\_bin\_compress\_min\_len](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin_compress_min_len) option.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}

[^1]: DDL (Data Definition Language): The subset of SQL commands used to create, modify, or destroy the structure of database objects (like tables, indexes, and databases) rather than the data itself.

[^2]: DML (Data Manipulation Language): The subset of SQL commands used to add, modify, retrieve, or delete data within existing database tables.
