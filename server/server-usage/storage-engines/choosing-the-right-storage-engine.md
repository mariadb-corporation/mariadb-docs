---
description: >-
  A guide to selecting the appropriate storage engine based on data needs,
  comparing features of general-purpose, columnar, and specialized engines.
---

# Choosing the Right Storage Engine

A high-level overview of the main reasons for choosing a particular storage engine:

## Topic List

### General Purpose

* [InnoDB](innodb/) is a good general transaction storage engine, and the best choice in most cases. It is the default storage engine.
* [Aria](aria/), MariaDB's more modern improvement on [MyISAM](myisam-storage-engine/), has a small footprint and allows for easy copying between systems.
* [MyISAM](myisam-storage-engine/) has a small footprint and allows for easy copying between systems. MyISAM is MySQL's oldest storage engine. There is usually little reason to use it except for legacy purposes. Aria is MariaDB's more modern improvement.
* [XtraDB](innodb/) is no longer available. It was a performance-enhanced fork of InnoDB and was MariaDB's default engine until [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1).

### Scaling, Partitioning

When you want to split your database load on several servers or optimize for scaling. We also suggest looking at [Galera](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/readme/mariadb-galera-cluster-usage-guide), a synchronous multi-master cluster.

* [Spider](spider/) uses partitioning to provide data sharding through multiple servers.
* [ColumnStore](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/columnstore) utilizes a massively parallel distributed data architecture and is designed for big data scaling to process petabytes of data.
* The [MERGE](merge.md) storage engine is a collection of identical [MyISAM](myisam-storage-engine/) tables that can be used as one. "Identical" means that all tables have identical column and index information.

### Compression / Archive

* [MyRocks](myrocks/) enables greater compression than InnoDB, as well as less write amplification giving better endurance of flash storage and improving overall throughput.
* The [Archive](archive.md) storage engine is, unsurprisingly, best used for archiving.

### Connecting to Other Data Sources

When you want to use data not stored in a MariaDB database.

* The [CSV](csv/) storage engine can read and append to files stored in CSV (comma-separated-values) format. However, since MariaDB 10.0, CONNECT is a better choice and is more flexibly able to read and write such files.

### Search Optimized

Search engines optimized for search.

* [SphinxSE](sphinx-storage-engine/) is used as a proxy to run statements on a remote Sphinx database server (mainly useful for advanced fulltext searches).
* [Mroonga](mroonga/) provides fast CJK-ready full text searching using column store.

### Cache, Read-only

* [MEMORY](memory-storage-engine.md) does not write data on-disk (all rows are lost on crash) and is best-used for read-only caches of data from other tables, or for temporary work areas. With the default [InnoDB](innodb/) and other storage engines having good caching, there is less need for this engine than in the past.

### Other Specialized Storage Engines

* [S3 Storage Engine](s3-storage-engine/) is a read-only storage engine that stores its data in Amazon S3.
* [Sequence](sequence-storage-engine.md) allows the creation of ascending or descending sequences of numbers (positive integers) with a given starting value, ending value and increment, creating virtual, ephemeral tables automatically when you need them.
* The [BLACKHOLE](blackhole.md) storage engine accepts data but does not store it and always returns an empty result. This can be useful in [replication](../../ha-and-performance/standard-replication/replication-overview.md) environments, for example, if you want to run complex filtering rules on a slave without incurring any overhead on a master.
* [OQGRAPH](oqgraph-storage-engine/) allows you to handle hierarchies (tree structures) and complex graphs (nodes having many connections in several directions).
* The [VIDEX](videx-storage-engine.md) storage engine is an aggregated, extensible engine suitable for what-if analyses in MariaDB. The name is derived from \[VI]rtual in\[DEX]. Using VIDEX, you can evaluate how potential indexes (and optimizer decisions such as join orders) would change query plans _without creating real indexes on production data_.

## Alphabetical List

* The [Archive](archive.md) storage engine is, unsurprisingly, best used for archiving.
* [Aria](aria/), MariaDB's more modern improvement on MyISAM, has a small footprint and allows for easy copy between systems.
* The [BLACKHOLE](blackhole.md) storage engine accepts data but does not store it and always returns an empty result. This can be useful in [replication](../../ha-and-performance/standard-replication/replication-overview.md) environments, for example, if you want to run complex filtering rules on a slave without incurring any overhead on a master.
* [ColumnStore](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/columnstore) utilizes a massively parallel distributed data architecture and is designed for big data scaling to process petabytes of data.
* [CONNECT](connect/) allows access to different kinds of text files and remote resources as if they were regular MariaDB tables.
* The [CSV](csv/csv-overview.md) storage engine can read and append to files stored in CSV (comma-separated-values) format. However, since MariaDB 10.0, CONNECT is a better choice and is more flexibly able to read and write such files.
* [InnoDB](innodb/) is a good general transaction storage engine, and the best choice in most cases. It is the default storage engine.
* The [MERGE](merge.md) storage engine is a collection of identical MyISAM tables that can be used as one. "Identical" means that all tables have identical column and index information.
* [MEMORY](memory-storage-engine.md) does not write data on-disk (all rows are lost on crash) and is best-used for read-only caches of data from other tables, or for temporary work areas. With the default [InnoDB](innodb/) and other storage engines having good caching, there is less need for this engine than in the past.
* [Mroonga](mroonga/) provides fast CJK-ready full text searching using column store.
* [MyISAM](myisam-storage-engine/) has a small footprint and allows for easy copying between systems. MyISAM is MySQL's oldest storage engine. There is usually little reason to use it except for legacy purposes. Aria is MariaDB's more modern improvement.
* [MyRocks](myrocks/) enables greater compression than InnoDB, as well as less write amplification giving better endurance of flash storage and improving overall throughput.
* [OQGRAPH](oqgraph-storage-engine/) allows you to handle hierarchies (tree structures) and complex graphs (nodes having many connections in several directions).
* [S3 Storage Engine](s3-storage-engine/) is a read-only storage engine that stores its data in Amazon S3.
* [Sequence](sequence-storage-engine.md) allows the creation of ascending or descending sequences of numbers (positive integers) with a given starting value, ending value and increment, creating virtual, ephemeral tables automatically when you need them.
* [SphinxSE](sphinx-storage-engine/) is used as a proxy to run statements on a remote Sphinx database server (mainly useful for advanced fulltext searches).
* [Spider](spider/) uses partitioning to provide data sharding through multiple servers.
* The [VIDEX](videx-storage-engine.md) storage engine is an aggregated, extensible engine suitable for what-if analyses in MariaDB.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
