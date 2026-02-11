---
description: >-
  Learn about the background processes that flush dirty pages from the buffer
  pool to disk, including adaptive flushing algorithms to optimize I/O.
---

# InnoDB Page Flushing

## Page Flushing with InnoDB Page Cleaner Threads

InnoDB page cleaner threads flush dirty pages, modified pages that have not yet been written to data files, from the [InnoDB buffer pool](innodb-buffer-pool.md). These dirty pages are flushed using a least-recently used (LRU) algorithm, which manages memory efficiently by prioritizing the eviction of older, less frequently accessed pages.

### innodb\_max\_dirty\_pages\_pct

The [innodb\_max\_dirty\_pages\_pct](innodb-system-variables.md#innodb_max_dirty_pages_pct) variable specifies the target maximum percentage of unwritten (dirty) pages in the [buffer pool](innodb-buffer-pool.md). If this percentage is exceeded, flushing will take place.

### innodb\_max\_dirty\_pages\_pct\_lwm

The [innodb\_max\_dirty\_pages\_pct\_lwm](innodb-system-variables.md#innodb_max_dirty_pages_pct_lwm) variable determines the low-water mark percentage of dirty pages that will enable preflushing to lower the dirty page ratio. The value 0 (the default) means that there are no separate background flushing so long as:

* the share of dirty pages does not exceed [innodb\_max\_dirty\_pages\_pct](innodb-system-variables.md#innodb_max_dirty_pages_pct)
* the last checkpoint age (LSN difference since the latest checkpoint) does not exceed [innodb\_log\_file\_size](innodb-system-variables.md#innodb_log_file_size) (minus some safety margin)
* the [buffer pool](innodb-buffer-pool.md) is not running out of space, which could trigger eviction flushing

{% hint style="success" %}
To make flushing more eager and ensure more consistent background I/O, you can set `innodb_max_dirty_pages_pct_lwm` to a very low value, such as `0.001`.

`SET GLOBAL innodb_max_dirty_pages_pct_lwm=0.001;`
{% endhint %}

## Single Page Cleaner Thread

InnoDB employs a streamlined I/O subsystem with just one cleaner thread dedicated to page flushing, regardless of the number of buffer pool instances.

{% hint style="info" %}
**For versions prior to MariaDB 10.5**

InnoDB utilized multiple page cleaner threads to flush dirty pages from the buffer pool to reduce internal mutex contention during high-concurrency workloads. This behavior was controlled by the `innodb_page_cleaners` system variable, which could be configured with a default value of either `4` or the configured number of `innodb_buffer_pool_instances`, whichever was lower.

Architectural improvements in MariaDB 10.5—such as splitting the buffer pool mutex and implementing read-write locks for the page hash—rendered these multiple partitions and threads unnecessary. The architecture was simplified to improve system resource efficiency and reduce context-switching overhead. The `innodb_page_cleaners` variable is now deprecated and ignored.
{% endhint %}

## Page Flushing with Multi-threaded Flush Threads

InnoDB's multi-thread flush feature can be enabled by setting the [innodb\_use\_mtflush](innodb-system-variables.md#innodb_use_mtflush) system variable. The number of threads cane be configured by setting the [innodb\_mtflush\_threads](innodb-system-variables.md#innodb_mtflush_threads) system variable. This system variable can be set in a server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server:

```ini
[mariadb]
...
innodb_use_mtflush = ON
innodb_mtflush_threads = 8
```

The [innodb\_mtflush\_threads](innodb-system-variables.md#innodb_mtflush_threads) system variable's default value is `8`. The maximum value is `64`. In multi-core systems, it is recommended to set its value close to the configured value of the [innodb\_buffer\_pool\_instances](innodb-system-variables.md#innodb_buffer_pool_instances) system variable. However, it is also recommended to use your own benchmarks to find a suitable value for your particular application.

{% hint style="info" %}
InnoDB's multi-thread flush feature is deprecated. Use multiple InnoDB page cleaner threads instead.
{% endhint %}

## Configuring the InnoDB I/O Capacity

Increasing the amount of I/O capacity available to InnoDB can also help increase the performance of page flushing.

### Scope of Throttling

It is critical to understand the restricted scope of this variable in modern versions of MariaDB:

* Throttles Background Flushing Only: `innodb_io_capacity` primarily throttles the submitted page writes during "background" or "idle" flushing.
* No Throttling for Buffer Pool Loading: As of MariaDB [10.5.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/changelogs/10.6/10.6.12), [10.6.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/changelogs/10.6/10.6.12), [10.11.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/changelogs/10.11/10.11.2), and later, this parameter no longer throttles the loading of buffer pool dumps at startup ([MDEV-25417](https://jira.mariadb.org/browse/MDEV-25417)). Startup loads are now performed at best-effort speed to ensure the server reaches full performance as quickly as possible.
* Interaction with `innodb_flush_sync`: The `innodb_io_capacity` limit is only effective when [innodb\_flush\_sync](https://www.google.com/search?q=innodb-system-variables.md%23innodb_flush_sync) is set to `OFF`. When `innodb_flush_sync=ON` (the default), InnoDB may ignore this limit during aggressive "furious flushing" if a log checkpoint is urgently required.

### Adjusting I/O Capacity

The amount of I/O capacity available to InnoDB can be configured by setting the [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity) system variable. This system variable can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET GLOBAL innodb_io_capacity=20000;
```

This system variable can also be set in a server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server:

```ini
[mariadb]
...
innodb_io_capacity=20000
```

The maximum amount of I/O capacity available to InnoDB in an emergency defaults to either `2000` or twice [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity), whichever is higher, or can be directly configured by setting the [innodb\_io\_capacity\_max](innodb-system-variables.md#innodb_io_capacity_max) system variable. This system variable can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET GLOBAL innodb_io_capacity_max=20000;
```

This system variable can also be set in a server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server:

```ini
[mariadb]
...
innodb_io_capacity_max=20000
```

## See Also

* [Significant performance boost with new MariaDB page compression on FusionIO](https://blog.mariadb.org/significant-performance-boost-with-new-mariadb-page-compression-on-fusionio/)
* [InnoDB Redo Log](innodb-redo-log.md)
* [InnoDB Buffer Pool](innodb-buffer-pool.md)
* [InnoDB Background Thread Pool](innodb-architecture-for-mariadb-enterprise-server/mariadb-enterprise-server-innodb-background-thread-pool.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
