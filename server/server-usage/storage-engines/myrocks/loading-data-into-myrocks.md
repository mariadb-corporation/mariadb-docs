---
description: >-
  Best practices and methods for efficiently loading large datasets into MyRocks
  tables, including using bulk loading features to improve performance.
---

# Loading Data Into MyRocks

Being a write-optimized storage engine, MyRocks has special ways to load data much faster than normal INSERTs would.

See:

* the section about "Migrating from InnoDB to MyRocks in production" has some clues.
* [Data-Loading](https://github.com/facebook/mysql-5.6/wiki/Data-Loading) covers the topic in greater detail.

{% hint style="info" %}
When loading data with [rocksdb\_bulk\_load=1](myrocks-system-variables.md#rocksdb_bulk_load) and the data conflicts with the data already in the database, one may get non-trivial errors, for example:
{% endhint %}

```sql
ERROR 1105 (HY000): [./.rocksdb/test.t1_PRIMARY_2_0.bulk_load.tmp] bulk load error: 
  Invalid argument: External file requires flush
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
