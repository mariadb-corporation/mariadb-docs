---
description: >-
  The cached statistics the TideSQL engine keeps, how they feed the MariaDB
  cost model, and how the engine estimates the number of rows in a key range.
---

# TideSQL Statistics and the Optimizer

TideSQL feeds MariaDB's cost-based optimizer from statistics it caches per table and from range estimates it asks the TidesDB library for at plan time. This page describes what is cached, how the cost methods use it, and how `records_in_range()` estimates cardinality.

## Cached Statistics

The engine keeps cached statistics that are refreshed at most every two seconds:

* The total key count, from the SSTable entries plus the keys still in the memtable.
* The total data size of the data column family and of the secondary-index column families.
* The mean record length, from the average key and value sizes.
* The LSM-tree read amplification factor.
* A sampled `rec_per_key` selectivity for each secondary index.

These are atomic variables on the shared table descriptor, and they feed the optimizer through `info()`, `scan_time()`, `keyread_time()`, `rnd_pos_time()`, and `records_in_range()`.

## Automatic Index Sampling

Secondary-index `rec_per_key` is measured automatically. The first time a populated table, one that has reached 1,024 rows, is asked for constant statistics, the engine samples the distinct index prefixes of each non-unique secondary index. It reads up to 100,000 entries per index on its own short `READ COMMITTED` transaction and caches the result, once per table share. Concurrent first queries produce a single sampling scan. A table below 1,024 rows is not sampled; it is sampled the first time it is planned against after it reaches 1,024 rows.

A workload never has to run `ANALYZE TABLE` to get real selectivity. Until the sample lands, a non-unique index falls back to a coarse estimate of the row count divided by 10, which overestimates a high-cardinality index and can steer the optimizer into scanning an `IN` list or a range rather than using the index. An explicit `ANALYZE TABLE` refreshes the same figures on demand. See [TideSQL Table Maintenance](tidesql-table-maintenance.md).

## Read Amplification in the Cost Model

The cost model accounts for an LSM read consulting several levels. The read amplification factor, from the library's statistics, scales the cost of point lookups and random-position reads. A higher read amplification nudges the optimizer toward sequential scans, and when the data is well compacted and the amplification is low, index lookups are cheap.

## Cost Methods

* `scan_time()` starts from the base `handler::scan_time()` row-count cost and adds an LSM surcharge for the SSTable overlap the scan has to merge across. The surcharge is the count of overlapping SSTables weighted 90% as I/O and 10% as CPU, so the same row count costs more to scan when it is spread across many overlapping SSTables than when it sits in a compacted shape. The surcharge reflects overlap only, not compression or merge policy, and the overlap count is cached on the same two-second interval as the other statistics.
* `keyread_time()` models index reads as `rows * 0.00003 * read_amp + ranges * 0.0001`, since each point lookup touches `read_amp` levels and a range scan amortizes the merge-heap setup across rows.
* `rnd_pos_time()` models random-position lookups as `rows * 0.00005 * read_amp`, reflecting that each random fetch is a point lookup through the full LSM stack.

`keyread_time()` and `rnd_pos_time()` charge everything to CPU and report no I/O cost.

At execution, a range read opens a range-bounded iterator that only visits the SSTables overlapping the range. An equality range, such as each value of an `IN` list, instead reuses one unbounded iterator for the statement and seeks it, as long as the handler has not written in that statement, since an iterator does not see writes made after it was opened. The scan iterator is freed at the end of every statement.

## Range-Aware Cardinality

`records_in_range()` takes one of two paths.

### Point Equality

A point equality is a predicate such as `WHERE k = 5`, where both bounds convert to identical comparable bytes. A unique or primary key carries its `rec_per_key` for the key parts given, which is one row when the full key is given, and a non-unique index that `ANALYZE TABLE` or the automatic sampling pass has already sampled carries a trustworthy `rec_per_key`, so both read that cached estimate directly.

Only a non-unique index with no sample yet needs more. There, the value bytes encode the index value without its primary-key suffix, so every matching row stores a key with that value as a prefix, and the matching rows are exactly the half-open range from the value to its successor. The engine probes that span with `tidesdb_range_stats`, which counts the rows carrying that one value and is accurate for a low- or high-cardinality index alike. A never-analyzed table therefore gets a real estimate, clamped between one and the table's row count, rather than the row count divided by 10.

The successor is the value with its last byte below `0xFF` incremented and the trailing bytes dropped. An all-`0xFF` value has no finite successor and falls back to the cached estimate.

### Range Predicates

For a range predicate, the engine asks the library for the range's live key count through `tidesdb_range_stats` and returns it as an absolute cardinality:

* The count is memtable-aware, so a range whose data has not been flushed yet reports its real cardinality.
* A range small enough to walk is counted exactly.
* A wider range is estimated from SSTable metadata without walking, taking each SSTable's keys in proportion to the share of its key span that the range covers.

The estimate is then clamped to the table's cached row count, so the optimizer never prices a range wider than the whole table. When the library cannot produce an estimate, the engine falls back to a quarter of the table's rows plus one.

A narrow range returns a small estimate and a wide one a proportionally larger estimate, which lets the optimizer choose indexes and join order sensibly.

## See Also

* [TideSQL Storage Internals](tidesql-storage-internals.md)
* [TideSQL Write-Path Optimizations](tidesql-write-path-optimizations.md)
* [TideSQL Data Model](tidesql-data-model.md)
* [TideSQL Glossary](tidesql-glossary.md)

<sub>_This page is licensed: GPLv2_</sub>
