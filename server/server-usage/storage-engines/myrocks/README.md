---
description: >-
  Learn about the MyRocks storage engine in MariaDB Server. Discover its
  advantages for flash storage, high write throughput, and compression
  efficiency in modern database deployments.
---

# MyRocks

{% columns %}
{% column %}
{% content-ref url="about-myrocks-for-mariadb.md" %}
[about-myrocks-for-mariadb.md](about-myrocks-for-mariadb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MyRocks is a storage engine based on RocksDB, optimized for high-write workloads and flash storage, offering superior compression and reduced write amplification.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="building-myrocks-in-mariadb.md" %}
[building-myrocks-in-mariadb.md](building-myrocks-in-mariadb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn how to build the MyRocks storage engine from source within the MariaDB Server build process, including necessary dependencies and configuration options.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="differences-between-myrocks-variants.md" %}
[differences-between-myrocks-variants.md](differences-between-myrocks-variants.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Differences between variants of the MyRocks storage engine.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="getting-started-with-myrocks.md" %}
[getting-started-with-myrocks.md](getting-started-with-myrocks.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A guide to installing and configuring MyRocks, including enabling the plugin, setting up basic tables, and understanding key configuration parameters.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="loading-data-into-myrocks.md" %}
[loading-data-into-myrocks.md](loading-data-into-myrocks.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Best practices and methods for efficiently loading large datasets into MyRocks tables, including using bulk loading features to improve performance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="myrocks-and-bloom-filters.md" %}
[myrocks-and-bloom-filters.md](myrocks-and-bloom-filters.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn how to configure and use Bloom filters in MyRocks to speed up point lookups by probabilistically determining if a key exists in a data file.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="myrocks-and-check-table.md" %}
[myrocks-and-check-table.md](myrocks-and-check-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Details on using the CHECK TABLE statement with MyRocks to verify the integrity of tables and indexes, and how it differs from other engines.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="myrocks-and-data-compression.md" %}
[myrocks-and-data-compression.md](myrocks-and-data-compression.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore the data compression options available in MyRocks, including different algorithms (Zstd, LZ4, etc.) and how to configure them per column family.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="myrocks-and-group-commit-with-binary-log.md" %}
[myrocks-and-group-commit-with-binary-log.md](myrocks-and-group-commit-with-binary-log.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand how MyRocks implements group commit to coordinate with the binary log, ensuring data consistency and crash safety for replicated transactions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="myrocks-and-index-only-scans.md" %}
[myrocks-and-index-only-scans.md](myrocks-and-index-only-scans.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MyRocks storage engine scans that only use indexes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="myrocks-and-replication.md" %}
[myrocks-and-replication.md](myrocks-and-replication.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This page details how MyRocks integrates with MariaDB replication, specifically addressing limitations with statement-based replication and lack of Gap Lock support.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="myrocks-and-start-transaction-with-consistent-snapshot.md" %}
[myrocks-and-start-transaction-with-consistent-snapshot.md](myrocks-and-start-transaction-with-consistent-snapshot.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MyRocks storage engine transactions with consistent snapshot.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="myrocks-column-families.md" %}
[myrocks-column-families.md](myrocks-column-families.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about MyRocks column families, a mechanism for grouping data similar to tablespaces, to optimize compression and Bloom filter settings per family.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="myrocks-performance-troubleshooting.md" %}
[myrocks-performance-troubleshooting.md](myrocks-performance-troubleshooting.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A guide to diagnosing and resolving performance issues in MyRocks using status variables, `SHOW ENGINE ROCKSDB STATUS`, and RocksDB performance context.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="optimizer-statistics-in-myrocks.md" %}
[optimizer-statistics-in-myrocks.md](optimizer-statistics-in-myrocks.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MyRocks storage engine statistics for the query optimizer.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="myrocks-transactional-isolation.md" %}
[myrocks-transactional-isolation.md](myrocks-transactional-isolation.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MyRocks storage engine transactional isolatioin.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="myrocks-status-variables.md" %}
[myrocks-status-variables.md](myrocks-status-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A list of MyRocks-specific status variables providing metrics on cache hits, compaction statistics, block cache usage, and other internal operations.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="myrocks-system-variables.md" %}
[myrocks-system-variables.md](myrocks-system-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A comprehensive reference for MyRocks system variables, allowing fine-tuning of performance, memory usage, compaction, and other internal behaviors.
{% endcolumn %}
{% endcolumns %}
