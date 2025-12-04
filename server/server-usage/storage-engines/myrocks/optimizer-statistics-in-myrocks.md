---
description: MyRocks storage engine statistics for the query optimizer.
---

# Optimizer Statistics in MyRocks

This article describes how MyRocks storage engine provides statistics to the query optimizer.

There are three kinds of statistics:

* Table statistics (number of rows in the table, average row size)
* Index cardinality (how distinct values are in the index)
* records-in-range estimates (how many rows are in a certain range "const1 < tbl.key < const2".

## How MyRocks computes statistics

MyRocks (actually RocksDB) uses LSM files which are written once and never updated. When an LSM file is written, MyRocks will compute index cardinalities and number-of-rows for the data in the file. (The file generally has rows, index records and/or tombstones for multiple tables/indexes).

For performance reasons, statistics are computed based on a fraction of rows in the LSM file. The percentage of rows used is controlled by [rocksdb\_table\_stats\_sampling\_pct](myrocks-system-variables.md#rocksdb_table_stats_sampling_pct); the default value is 10%.

Before the data is dumped into LSM file, it is stored in the MemTable. MemTable doesn't allow computing index cardinalities, but it can provide an approximate number of rows in the table. Use of MemTable data for statistics is controlled by [rocksdb\_force\_compute\_memtable\_stats](myrocks-system-variables.md#rocksdb_force_compute_memtable_stats); the default value is `ON`.

### Are index statistics predictable?

Those who create/run MTR tests, need to know whether EXPLAIN output is deterministic.\
For MyRocks tables, the answer is NO (just like for InnoDB).

Statistics are computed using sampling and GetApproximateMemTableStats() which means that the #rows column in the EXPLAIN output may vary slightly.

### Records-in-range estimates

MyRocks uses RocksDB's GetApproximateSizes() call to produce an estimate for the number of rows in the certain range. The data in MemTable is also taken into account by issuing a GetApproximateMemTableStats call.

## ANALYZE TABLE

ANALYZE TABLE will possibly flush the MemTable (depending on the [rocksdb\_flush\_memtable\_on\_analyze](myrocks-system-variables.md#rocksdb_flush_memtable_on_analyze) and [rocksdb\_pause\_background\_work](myrocks-system-variables.md#rocksdb_pause_background_work) settings).

After that, it will re-read statistics from the SST files and re-compute the summary numbers\
(TODO: and if the data was already on disk, the result should not be different from the one we had before ANALYZE?)

## Debugging helper variables

There are a few variables that will cause MyRocks to report certain pre-defined estimate numbers to the optimizer:

* @@rocksdb\_records\_in\_range - if not 0, report that any range has this many rows
* @@rocksdb\_force\_index\_records\_in\_range - if not 0, and FORCE INDEX hint is used, report that any range has this many rows.
* @@rocksdb\_debug\_optimizer\_n\_rows - if not 0, report that any MyRocks table has this many rows.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
