---
description: >-
  A guide to diagnosing and resolving performance issues in MyRocks using status
  variables, `SHOW ENGINE ROCKSDB STATUS`, and RocksDB performance context.
---

# MyRocks Performance Troubleshooting

MyRocks exposes its performance metrics through several interfaces:

* Status variables
* `SHOW ENGINE ROCKSDB STATUS`
* RocksDB's perf context

the contents slightly overlap, but each source has its own unique information, so be sure to check all three.

### Status Variables

Check the output of

```sql
SHOW STATUS LIKE 'Rocksdb%'
```

See [MyRocks Status Variables](myrocks-status-variables.md) for more information.

### SHOW ENGINE ROCKSDB STATUS

This produces a lot of information.

One particularly interesting part is compaction statistics. It shows the amount of data on each SST level and other details:

```
*************************** 4. row ***************************
  Type: CF_COMPACTION
  Name: default
Status: 
** Compaction Stats [default] **
Level    Files   Size     Score Read(GB)  Rn(GB) Rnp1(GB) Write(GB) Wnew(GB) Moved(GB) W-Amp Rd(MB/s) Wr(MB/s) Comp(sec) Comp(cnt) Avg(sec) KeyIn KeyDrop
----------------------------------------------------------------------------------------------------------------------------------------------------------
  L0      3/0   30.16 MB   1.0      0.0     0.0      0.0      11.9     11.9       0.0   1.0      0.0     76.6       159       632    0.251       0      0
  L1      5/0   247.54 MB   1.0      0.7     0.2      0.5       0.5      0.0      11.6   2.6     58.5     44.1        12         4    2.926     30M    10M
  L2    112/0    2.41 GB   1.0      0.6     0.0      0.6       0.5     -0.1      11.4  43.4     55.2     45.9        11         1   10.827     21M  3588K
  L3    466/0    8.91 GB   0.4      0.0     0.0      0.0       0.0      0.0       8.9   0.0      0.0      0.0         0         0    0.000       0      0
 Sum    586/0   11.59 GB   0.0      1.3     0.2      1.0      12.8     11.8      32.0   1.1      7.1     72.6       181       637    0.284     52M    13M
 Int      0/0    0.00 KB   0.0      0.9     0.1      0.8       0.8      0.0       0.1  20.5     48.4     45.3        19         6    3.133     33M  3588K
```

### Performance Context

RocksDB has an internal mechanism called "perf context". The counter values are exposed through two tables:

* [INFORMATION\_SCHEMA.ROCKSDB\_PERF\_CONTEXT\_GLOBAL](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-myrocks-tables/information-schema-rocksdb_perf_context_global-table.md) - global counters
* [INFORMATION\_SCHEMA.ROCKSDB\_PERF\_CONTEXT](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-myrocks-tables/information-schema-rocksdb_perf_context-table.md) - Per-table/partition counters

By default statistics are NOT collected. One needs to set [rocksdb\_perf\_context\_level](myrocks-system-variables.md#rocksdb_perf_context_level) to some value (e.g. 3) to enable collection.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
