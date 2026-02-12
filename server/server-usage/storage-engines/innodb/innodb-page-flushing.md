---
description: >-
  Learn about the background processes that flush dirty pages from the buffer
  pool to disk, including adaptive flushing algorithms to optimize I/O.
---

# InnoDB Page Flushing

## Page Flushing with InnoDB Page Cleaner Threads

InnoDB Page Cleaner Threads flush dirty pages, modified pages that have not yet been written to data files, from the [InnoDB buffer pool](innodb-buffer-pool.md). These dirty pages are flushed using a least-recently used (LRU) algorithm, which manages memory efficiently by prioritizing the eviction of older, less frequently accessed pages.

### innodb\_max\_dirty\_pages\_pct

The [innodb\_max\_dirty\_pages\_pct](innodb-system-variables.md#innodb_max_dirty_pages_pct) variable specifies the target maximum percentage of unwritten (dirty) pages in the [buffer pool](innodb-buffer-pool.md). If this percentage is exceeded, flushing will take place.

### innodb\_max\_dirty\_pages\_pct\_lwm

The [innodb\_max\_dirty\_pages\_pct\_lwm](innodb-system-variables.md#innodb_max_dirty_pages_pct_lwm) variable determines the low-water mark percentage of dirty pages that will enable preflushing to lower the dirty page ratio. The default value is `0`.&#x20;

{% hint style="success" %}
To make flushing more eager and ensure more consistent background I/O, you can set `innodb_max_dirty_pages_pct_lwm` to a very low value, such as `0.001`:

`SET GLOBAL innodb_max_dirty_pages_pct_lwm=0.001;`
{% endhint %}

## Single Page Cleaner Thread

InnoDB employs a streamlined I/O subsystem with just one cleaner thread dedicated to page flushing, regardless of the number of buffer pool instances.

{% hint style="info" %}
**For versions prior to MariaDB 10.5**

InnoDB utilized multiple page cleaner threads to flush dirty pages from the buffer pool to reduce internal mutex contention during high-concurrency workloads. This behavior was controlled by the `innodb_page_cleaners` [system variable](innodb-system-variables.md#innodb_page_cleaners), which could be configured with a default value of either `4` or the [configured number](innodb-system-variables.md#innodb_buffer_pool_instances) of `innodb_buffer_pool_instances`, whichever was lower.

Architectural improvements in MariaDB 10.5—such as splitting the [buffer pool mutex](innodb-buffer-pool.md) and implementing read-write locks for the page hash—rendered these multiple partitions and threads unnecessary. Consequently, the architecture was simplified to improve system resource efficiency and reduce context-switching overhead.

Please note the following status for legacy parameters:

* [innodb\_page\_cleaners](innodb-system-variables.md#innodb_page_cleaners): Deprecated and ignored since [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/changelogs/changelogs-mariadb-105-series/mariadb-1051-changelog); removed entirely in MariaDB 10.6.
* [innodb\_buffer\_pool\_instances](innodb-system-variables.md#innodb_buffer_pool_instances): Parameter removed in [MariaDB 10.5 ](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105)as the buffer pool now runs in a single instance.
* [innodb\_mtflush\_threads](innodb-system-variables.md#innodb_mtflush_threads): This [Fusion-io](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/changelogs/changelogs-mariadb-100-series/mariadb-10015-fusion-io-changelog) specific parameter was removed in MariaDB [10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/changelogs/11.3/mariadb-11-3-2-changelog).
{% endhint %}

## Configuring the InnoDB I/O Capacity

increasing the amount of I/O capacity available to InnoDB can help increase the performance of page flushing. The unit of [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity) is the number of data pages (of the size [defined by](innodb-system-variables.md#innodb_page_size) `innodb_page_size`) that can be written per second.

### Scope of Throttling

It is critical to understand the restricted scope of this variable in modern versions of MariaDB:

* Checkpoint Flushing Only: `innodb_io_capacity` only throttles checkpoint flushing (background or idle flushing). It does not throttle LRU eviction flushing, which handles the removal of pages when the buffer pool is at capacity.
* No Throttling for Buffer Pool Loading: As of MariaDB 10.5.19, 10.6.12, 10.11.2, and later, this parameter no longer throttles the loading of buffer pool dumps at startup (MDEV-25417). Startup loads are now performed at best-effort speed.
* Interaction with `innodb_flush_sync`: The `innodb_io_capacity` limit is only effective when [innodb\_flush\_sync](innodb-system-variables.md#innodb_flush_sync) is set to `OFF`. When `innodb_flush_sync=ON` (the default), InnoDB may ignore this limit during aggressive "furious flushing" if a log checkpoint is urgently required to prevent the redo log from filling up.
* Shared Storage Consideration: If the InnoDB redo log resides on the same physical storage as the data files, ensure you leave some spare capacity for log writes so they are not blocked by background page flushing.

### Adjusting I/O Capacity

The amount of I/O capacity available to InnoDB can be configured by setting the [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity) system variable. This system variable can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET GLOBAL innodb_io_capacity=20000;
```

The maximum amount of I/O capacity available to InnoDB in an emergency defaults to either `2000` or twice `innodb_io_capacity`, whichever is higher, or can be directly configured by setting the [innodb\_io\_capacity\_max](https://www.google.com/search?q=innodb-system-variables.md%23innodb_io_capacity_max) system variable.

#### Device-Specific Recommendations

When setting these variables, consider the physical limits of your storage hardware:

| Storage Device Type | Typical IOPS Capability | Recommended innodb\_io\_capacity |
| ------------------- | ----------------------- | -------------------------------- |
| SATA HDD            | \~100 – 200             | 100 – 200                        |
| SATA SSD            | \~50,000 – 100,000      | 2,000 – 20,000                   |
| NVMe SSD            | 500,000+                | 20,000 – 80,000+                 |

For high-speed NVMe storage, a sensible value for `innodb_io_capacity` may be as high as 80,000.

## See Also

* [Significant performance boost with new MariaDB page compression on FusionIO](https://blog.mariadb.org/significant-performance-boost-with-new-mariadb-page-compression-on-fusionio/)
* [InnoDB Redo Log](innodb-redo-log.md)
* [InnoDB Buffer Pool](innodb-buffer-pool.md)
* [InnoDB Background Thread Pool](innodb-architecture-for-mariadb-enterprise-server/mariadb-enterprise-server-innodb-background-thread-pool.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
