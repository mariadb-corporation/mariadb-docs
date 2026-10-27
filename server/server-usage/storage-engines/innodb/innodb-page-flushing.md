---
description: >-
  Learn about the background processes that flush dirty pages from the buffer
  pool to disk, including adaptive flushing algorithms to optimize I/O.
---

# InnoDB Page Flushing

InnoDB uses a single `buf_flush_page_cleaner` thread to flush dirty pages—modified pages that have not yet been written to data files—from the [InnoDB buffer pool](innodb-buffer-pool.md) to disk. The page cleaner writes pages in two ways:

* **Checkpoint flushing** writes the pages with the oldest changes first, so that the [checkpoint](innodb-redo-log.md#checkpoints) can advance and the [redo log](innodb-redo-log.md) space they occupy can be reused. The settings on this page control mainly this kind of flushing.
* **LRU flushing** writes and evicts the least recently used pages when the buffer pool needs free pages.

The page cleaner works in cycles of about one second. It stays idle until one of the conditions described below makes flushing necessary.

## When Flushing Starts

### innodb\_max\_dirty\_pages\_pct

The [innodb\_max\_dirty\_pages\_pct](innodb-system-variables.md#innodb_max_dirty_pages_pct) variable specifies the target maximum percentage of unwritten (dirty) pages in the [buffer pool](innodb-buffer-pool.md). If this percentage is exceeded, flushing will take place.

### innodb\_max\_dirty\_pages\_pct\_lwm

The [innodb\_max\_dirty\_pages\_pct\_lwm](innodb-system-variables.md#innodb_max_dirty_pages_pct_lwm) variable determines the low-water mark percentage of dirty pages that will enable preflushing to lower the dirty page ratio. The default value is `0`.&#x20;

{% hint style="success" %}
To make flushing more eager and ensure more consistent background I/O, you can set `innodb_max_dirty_pages_pct_lwm` to a very low value, such as `0.001`:

`SET GLOBAL innodb_max_dirty_pages_pct_lwm=0.001;`
{% endhint %}

### innodb\_adaptive\_flushing\_lwm

The [innodb\_adaptive\_flushing\_lwm](innodb-system-variables.md#innodb_adaptive_flushing_lwm) variable sets a low-water mark for the [redo log](innodb-redo-log.md), as a percentage of its capacity (default `10`). When the [checkpoint age](innodb-redo-log.md#determining-the-checkpoint-age), the amount of redo log written since the last checkpoint, exceeds this percentage, the page cleaner starts flushing to advance the checkpoint, even if the dirty page percentage is below both limits above. This applies whether [innodb\_adaptive\_flushing](innodb-system-variables.md#innodb_adaptive_flushing) is `ON` or `OFF`.

## Adaptive Flushing

Adaptive flushing decides how many pages the page cleaner writes in each cycle once flushing has started. It is controlled by the [innodb\_adaptive\_flushing](innodb-system-variables.md#innodb_adaptive_flushing) variable.

* With `innodb_adaptive_flushing=ON` (the default), the page cleaner adjusts the number of pages it writes to how quickly the workload creates redo log and dirty pages. It weighs [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity) scaled by how close the redo log or the dirty page percentage is to its limit, the average number of pages written in recent cycles, and the number of pages that must be written to keep up with the rate of redo log writes. The result never exceeds [innodb\_io\_capacity\_max](innodb-system-variables.md#innodb_io_capacity_max). The [innodb\_flushing\_avg\_loops](innodb-system-variables.md#innodb_flushing_avg_loops) variable sets how many cycles the averages cover, so a higher value makes the flushing rate change more smoothly.
* With `innodb_adaptive_flushing=OFF`, flushing still starts under the same conditions, including the [innodb\_adaptive\_flushing\_lwm](#innodb_adaptive_flushing_lwm) low-water mark, but the page cleaner writes a fixed `innodb_io_capacity` pages per cycle. `OFF` therefore does not turn flushing off; it only makes the rate fixed.

When the redo log is about to run out of space, InnoDB writes pages faster than adaptive flushing would, regardless of this setting. See [Scope of Throttling](#scope-of-throttling) for how [innodb\_flush\_sync](innodb-system-variables.md#innodb_flush_sync) affects this.

To see how many pages each kind of flushing has written, enable the `buffer_flush_adaptive_total_pages` and `buffer_flush_background_total_pages` counters in the [INFORMATION\_SCHEMA.INNODB\_METRICS](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md) table, which are disabled by default:

```sql
SET GLOBAL innodb_monitor_enable = 'buffer_flush_adaptive_total_pages';
SET GLOBAL innodb_monitor_enable = 'buffer_flush_background_total_pages';

SELECT name, count FROM information_schema.INNODB_METRICS
  WHERE name IN ('buffer_flush_adaptive_total_pages',
                 'buffer_flush_background_total_pages');
```

## Configuring the InnoDB I/O Capacity

increasing the amount of I/O capacity available to InnoDB can help increase the performance of page flushing. The unit of [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity) is the number of data pages (of the size [defined by](innodb-system-variables.md#innodb_page_size) `innodb_page_size`) that can be written per second.

### Scope of Throttling

It is critical to understand the restricted scope of this variable in modern versions of MariaDB:

* Checkpoint Flushing Only: [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity) only throttles checkpoint flushing (background or idle flushing). It does not throttle LRU eviction flushing, which handles the removal of pages when the buffer pool is at capacity.
* Interaction with `innodb_flush_sync`: The `innodb_io_capacity` limit is only effective when [innodb\_flush\_sync](innodb-system-variables.md#innodb_flush_sync) is set to `OFF`. When `innodb_flush_sync=ON` (the default), InnoDB may ignore this limit during aggressive "furious flushing" if a log checkpoint is urgently required to prevent the redo log from filling up.
* No Throttling for Buffer Pool Loading: As of MariaDB [10.6.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/changelogs/10.6/10.6.12), [10.11.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/changelogs/10.11/10.11.2), and later, this parameter no longer throttles the loading of buffer pool dumps at startup ([MDEV-25417](https://jira.mariadb.org/browse/MDEV-25417)). Startup loads are now performed at best-effort speed.
* Shared Storage Consideration: If the InnoDB redo log resides on the same physical storage as the data files, ensure you leave some spare capacity for log writes so they are not blocked by background page flushing.

### Adjusting I/O Capacity

The amount of I/O capacity available to InnoDB can be configured by setting the [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity) system variable. This system variable can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET GLOBAL innodb_io_capacity=20000;
```

The maximum amount of I/O capacity available to InnoDB in an emergency defaults to either `2000` or twice `innodb_io_capacity`, whichever is higher, or can be directly configured by setting the [innodb\_io\_capacity\_max](innodb-system-variables.md#innodb_io_capacity_max) system variable.

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
