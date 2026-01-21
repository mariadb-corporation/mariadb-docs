---
description: >-
  Best practices for configuring MariaDB server variables like
  `innodb_buffer_pool_size`, `aria_pagecache_buffer_size`, and `thread_handling`
  to maximize resource utilization on dedicated servers.
---

# Configuring MariaDB for Optimal Performance

This article will help you configure MariaDB for optimal performance.

By default, MariaDB is configured to work on a desktop system and therefore use relatively few resources. To optimize installation for a dedicated server, you have to do a few minutes of work.

For this article we assume that you are going to run MariaDB on a dedicated server.

Feel free to update this article if you have more ideas.

## [my.cnf](../configuring-mariadb-with-option-files.md) Files

MariaDB is normally configured by editing the [my.cnf](../configuring-mariadb-with-option-files.md) file. In the next section you have a list of variables that you may want to configure for dedicated MariaDB servers.

## [InnoDB](../../../../server-usage/storage-engines/innodb/) Storage Engine

InnoDB is normally the default storage engine with MariaDB.

* You should set [innodb\_buffer\_pool\_size](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size) to about 80% of your memory. The goal is to ensure that 80 % of your working set is in memory.

The other most important InnoDB variables are:

* [innodb\_log\_file\_size](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_log_file_size)
* [innodb\_flush\_method](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_flush_method)
* [innodb\_thread\_sleep\_delay](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_thread_sleep_delay)

Some other important InnoDB variables:

* [innodb\_max\_dirty\_pages\_pct\_lwm](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_max_dirty_pages_pct_lwm)
* [innodb\_read\_ahead\_threshold](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_read_ahead_threshold)
* [innodb\_buffer\_pool\_instances](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_instances). Deprecated and ignored from [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1051-release-notes).
* [innodb\_adaptive\_max\_sleep\_delay](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_max_sleep_delay). Deprecated and ignored from [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1055-release-notes).
* [innodb\_thread\_concurrency](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_thread_concurrency). Deprecated and ignored from [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1055-release-notes).

## [Aria](../../../../server-usage/storage-engines/aria/aria-storage-engine.md) Storage Engine

* MariaDB uses by default the Aria storage engine for internal temporary files. If you have many temporary files, you should set [aria\_pagecache\_buffer\_size](../../../../server-usage/storage-engines/aria/aria-system-variables.md) to a reasonably large value so that temporary overflow data is not flushed to disk. The default is 128M.

You can check if Aria is configured properly by executing:

```sql
MariaDB [test]> show global status like "Aria%";
```

```
+-----------------------------------+-------+
| Variable_name                     | Value |
+-----------------------------------+-------+
| Aria_pagecache_blocks_not_flushed | 0     |
| Aria_pagecache_blocks_unused      | 964   |
| Aria_pagecache_blocks_used        | 232   |
| Aria_pagecache_read_requests      | 9598  |
| Aria_pagecache_reads              | 0     |
| Aria_pagecache_write_requests     | 222   |
| Aria_pagecache_writes             | 0     |
| Aria_transaction_log_syncs        | 0     |
+-----------------------------------+-------+
```

If `Aria_pagecache_reads` is much smaller than `Aria_pagecache_read_request` and`Aria_pagecache_writes` is much smaller than Aria\_pagecache\_write\_request#, then your setup is good. If the [aria\_pagecache\_buffer\_size](../../../../server-usage/storage-engines/aria/aria-system-variables.md) is big enough, the two variables should be 0, like above.

## [MyISAM](../../../../server-usage/storage-engines/myisam-storage-engine/)

* If you don't use MyISAM tables explicitly (true for most [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)+ users), you can set [key\_buffer\_size](../../../../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size) to a very low value, like 64K.

## Using in memory temporary tables

Using memory tables for internal temporary results can speed up execution.\
However, if the memory table gets full, then the memory table will be moved to\
disk, which can hurt performance.

You can check how the internal memory tables are performing by executing:

```sql
MariaDB [test]> show global status like "Created%tables%";
```

```
+-------------------------+-------+
| Variable_name           | Value |
+-------------------------+-------+
| Created_tmp_disk_tables | 1     |
| Created_tmp_tables      | 2     |
+-------------------------+-------+
```

`Created_tmp_tables` is the total number of internal temporary tables created as part of executing queries like SELECT.`Created_tmp_disk_tables` shows how many of these did hit the storage.

You can increase the storage for internal temporary tables by setting [max\_heap\_table\_size](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_heap_table_size) and [tmp\_memory\_table\_size](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tmp_memory_table_size) high enough. These values are per connection.

## Lots of Connections

### A Lot of Fast Connections + Small Set of Queries + Disconnects

* If you are doing a lot of fast connections / disconnects, you should increase [back\_log](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#back_log) and if you are running [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1) or below [thread\_cache\_size](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#thread_cache_size).
* If you have a lot (> 128) of simultaneous running fast queries, you should consider setting [thread\_handling](../../../../ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables.md) to `pool_of_threads`.

### Connecting From a Lot of Different Machines

* If you are connecting from a lot of different machines you should increase [host\_cache\_size](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#host_cache_size) to the max number of machines (default 128) to cache the resolving of hostnames. If you don't connect from a lot of machines, you can set this to a very low value!

## See Also

* [MariaDB Memory Allocation](../../../../ha-and-performance/mariadb-memory-allocation.md)
* [Full List of MariaDB Options, System and Status Variables](../../../../reference/full-list-of-mariadb-options-system-and-status-variables.md)
* [Server system variables](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md)
* [mysqld options](../../../starting-and-stopping-mariadb/mariadbd-options.md)
* [Performance schema](../../../../reference/system-tables/performance-schema/) helps you understand what is taking time and resources.
* [Slow query log](../../../server-monitoring-logs/slow-query-log/) is used to find queries that are running slow.
* [OPTIMIZE TABLE](../../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md) helps you defragment tables.

## External Links

* [what-to-tune-in-mysql-56-after-installation.html](https://www.tocker.ca/2013/09/17/what-to-tune-in-mysql-56-after-installation.html)
* [optimizing-mysql-configuration-percona-mysql-university-montevideo](https://www.percona.com/resources/technical-presentations/optimizing-mysql-configuration-percona-mysql-university-montevideo)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
