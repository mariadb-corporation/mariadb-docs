---
description: Differences between variants of the MyRocks storage engine.
---

# Differences Between MyRocks Variants

MyRocks is available in

* Facebook's (FB) MySQL branch (originally based on MySQL 5.6)
* MariaDB (from 10.2 and 10.3)
* Percona Server from 5.7

This page lists differences between these variants.

This is a work in progress. The contents are not final

## RocksDB Data Location

FB and Percona store RocksdDB files in $datadir/`.rocksdb`. MariaDB puts them in $datadir/`#rocksdb`. This is more friendly for packaging and OS scripts.

## Compression Algorithms

* FB's branch doesn't provide binaries. One needs to compile it with appropriate compression libraries.
* In MariaDB, available compression algorithms can be seen in the [rocksdb\_supported\_compression\_types](myrocks-system-variables.md#rocksdb_supported_compression_types) variable. From [MariaDB 10.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107), algorithms can be [installed as a plugin](../../../ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins.md). In earlier versions, the set of supported compression algorithms depends on the platform.
  * On Ubuntu 16.04 (current LTS) it is `Snappy,Zlib,LZ4,LZ4HC` .
  * On CentOS 7.4 it is `Snappy,Zlib`.
  * In the bintar tarball it is `Snappy,Zlib`.
* Percona Server supports: `Zlib, ZSTD, LZ4 (the default), LZ4HC`. Unsupported algorithms: `Snappy, BZip2, XPress`.

## RocksDB Version Information

* FB's branch provides the `rocksdb_git_hash` _status_ variable.
* MariaDB provides the `@@rocksdb_git_hash` _system_ variable.
* Percona Server doesn't provide either.

## RocksDB Version

* Facebook's branch uses RocksDB 5.10.0 (the version number can be found in `include/rocksdb/version.h`)

```
commit ba295cda29daee3ffe58549542804efdfd969784
Author: Andrew Kryczka <andrewkr@fb.com>
Date:   Fri Jan 12 11:03:55 2018 -0800
```

* MariaDB currently uses 5.8.0

```
commit 9a970c81af9807071bd690f4c808c5045866291a
Author: Yi Wu <yiwu@fb.com>
Date:   Wed Sep 13 17:21:35 2017 -0700
```

* Percona Server uses 5.8.0

```
commit ab0542f5ec6e7c7e405267eaa2e2a603a77d570b
Author: Maysam Yabandeh <myabandeh@fb.com>
Date:   Fri Sep 29 07:55:22 2017 -0700
```

## Binlog Position in information\_schema.rocksdb\_global\_info

* FB branch provides information\_schema.rocksdb\_global\_info type=BINLOG, NAME={FILE, POS, GTID}.
* Percona Server doesn't provide it.
* MariaDB doesn't provide it.

One use of that information is to take the output of `myrocks_hotbackup` and make it a new master.

## Gap Lock Detector

* FB branch has a "Gap Lock Detector" feature. It is at the SQL layer. It can be controlled with `gap_lock_XXX` variables and is disabled by default (gap-lock-raise-error=false, gap-lock-write-lock=false).
* Percona Server has gap lock checking ON but doesn't seem to have any way to control it?\
  Queries that use Gap Lock on MyRocks fail with an error like this:

```sql
INSERT INTO tbl2 SELECT * FROM tbl1;
ERROR 1105 (HY000): Using Gap Lock without full unique key in multi-table or multi-statement transactions
is not allowed. You need to either rewrite queries to use all unique key columns in WHERE equal conditions,
or rewrite to single-table, single-statement transaction.  Query: insert into tbl2 select * from tbl1
```

* MariaDB doesn't include the Gap Lock Detector.

## Generated Columns

* Both MariaDB and Percona Server support [generated columns](../../../reference/sql-statements/data-definition/create/generated-columns.md), but neither one supports them for the MyRocks storage engine (attempts to create a table will produce an error).
* [Invisible columns](../../../reference/sql-statements/data-definition/create/invisible-columns.md) in [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103) are supported (as they are an SQL layer feature).

## rpl\_skip\_tx\_api

Facebook's branch has a performance feature for replication slaves, `rpl_skip_tx_api`. It is not available in MariaDB or in Percona Server.

## Details

The above comparison was made using

* FB/MySQL 5.6.35
* Percona Server 5.7.20-19-log
* [MariaDB 10.2.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-10213-release-notes) (MyRocks is beta)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
