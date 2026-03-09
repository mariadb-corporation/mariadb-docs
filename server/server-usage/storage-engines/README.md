---
description: >-
  Understand MariaDB Server's storage engines. Explore the features and use
  cases of InnoDB, Aria, MyISAM, and other engines to choose the best option for
  your specific data needs.
---

# Storage Engines

{% columns %}
{% column %}
{% content-ref url="storage-engines-storage-engines-overview.md" %}
[storage-engines-storage-engines-overview.md](storage-engines-storage-engines-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An introduction to MariaDB's pluggable storage engine architecture, highlighting key engines like InnoDB, MyISAM, and Aria for different workloads.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="choosing-the-right-storage-engine.md" %}
[choosing-the-right-storage-engine.md](choosing-the-right-storage-engine.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A guide to selecting the appropriate storage engine based on data needs, comparing features of general-purpose, columnar, and specialized engines.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="archive.md" %}
[archive.md](archive.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The Archive storage engine is optimized for high-speed insertion and compression of large amounts of data, suitable for logging and auditing.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="aria/" %}
[aria](aria/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about the Aria storage engine in MariaDB Server. Understand its features, advantages, and use cases, particularly for crash-safe operations and transactional workloads.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="blackhole.md" %}
[blackhole.md](blackhole.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The BLACKHOLE storage engine discards all data written to it but records operations in the binary log, useful for replication filtering and testing.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="connect/" %}
[connect](connect/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The CONNECT storage engine has been deprecated.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="csv/" %}
[csv](csv/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The CSV storage engine stores data in text files using comma-separated values format, allowing easy data exchange with other applications.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="federatedx-storage-engine/" %}
[federatedx-storage-engine](federatedx-storage-engine/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
FederatedX is a storage engine that allows access to tables on remote MariaDB or MySQL servers as if they were local tables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb/" %}
[innodb](innodb/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Discover InnoDB, the default storage engine for MariaDB Server. Learn about its transaction-safe capabilities, foreign key support, and high performance for demanding workloads.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="memory-storage-engine.md" %}
[memory-storage-engine.md](memory-storage-engine.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The MEMORY storage engine stores tables in RAM for fast access, but data is lost upon server restart.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="merge.md" %}
[merge.md](merge.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The MERGE storage engine allows a collection of identical MyISAM tables to be treated as a single logical table, useful for managing large datasets.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mroonga/" %}
[mroonga](mroonga/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Mroonga (formerly named Groonga Storage Engine) is a storage engine that provides fast CJK-ready full text searching using column store.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="myisam-storage-engine/" %}
[myisam-storage-engine](myisam-storage-engine/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore the MyISAM storage engine in MariaDB Server. Understand its characteristics, including suitability for read-heavy workloads, and its role in specific use cases.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="myrocks/" %}
[myrocks](myrocks/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about the MyRocks storage engine in MariaDB Server. Discover its advantages for flash storage, high write throughput, and compression efficiency in modern database deployments.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="oqgraph-storage-engine/" %}
[oqgraph-storage-engine](oqgraph-storage-engine/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore the OQGRAPH storage engine in MariaDB Server. Learn how to efficiently manage hierarchical and complex graph data structures, perfect for social networks and bill of materials.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="performance_schema-storage-engine.md" %}
[performance\_schema-storage-engine.md](performance_schema-storage-engine.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
While technically a storage engine, PERFORMANCE\_SCHEMA provides a way to inspect internal server execution details at a low level.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sequence-storage-engine.md" %}
[sequence-storage-engine.md](sequence-storage-engine.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The Sequence engine generates virtual tables of number sequences on the fly, useful for generating series of integers without storing data.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="s3-storage-engine/" %}
[s3-storage-engine](s3-storage-engine/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Integrate MariaDB Server with Amazon S3 using the S3 Storage Engine. Learn how to store and retrieve data directly from cloud object storage for scalability and cost efficiency.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sphinx-storage-engine/" %}
[sphinx-storage-engine](sphinx-storage-engine/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Integrate MariaDB Server with Sphinx for advanced full-text search. The Sphinx storage engine allows you to query external Sphinx indexes directly from your database.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spider/" %}
[spider](spider/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore the Spider storage engine in MariaDB Server. Learn how to shard data across multiple MariaDB and MySQL servers, enabling horizontal scaling and distributed database solutions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="videx-storage-engine.md" %}
[videx-storage-engine.md](videx-storage-engine.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The VIDEX storage engine is an aggregated, extensible engine suitable for what-if analyses in MariaDB. The name is derived from \[VI]rtual in\[DEX].
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="converting-tables-from-myisam-to-innodb.md" %}
[converting-tables-from-myisam-to-innodb.md](converting-tables-from-myisam-to-innodb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This guide outlines the benefits and process of migrating tables from MyISAM to InnoDB, highlighting key differences like transaction support and foreign keys.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="machine-learning-with-mindsdb.md" %}
[machine-learning-with-mindsdb.md](machine-learning-with-mindsdb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn how to integrate MindsDB with MariaDB to train and query machine learning models directly using standard SQL commands.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="legacy-storage-engines/" %}
[legacy-storage-engines](legacy-storage-engines/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore legacy storage engines in MariaDB Server. This section provides information on older engines, their historical context, and considerations for migration or compatibility.
{% endcolumn %}
{% endcolumns %}
