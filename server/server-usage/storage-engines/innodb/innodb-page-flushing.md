---
description: >-
  Learn about the background processes that flush dirty pages from the buffer
  pool to disk, including adaptive flushing algorithms to optimize I/O.
---

# InnoDB Page Flushing

## Page Flushing with InnoDB Page Cleaner Threads

InnoDB page cleaner threads flush dirty pages from the [InnoDB buffer pool](innodb-buffer-pool.md). These dirty pages are flushed using a least-recently used (LRU) algorithm.

### innodb\_max\_dirty\_pages\_pct

The [innodb\_max\_dirty\_pages\_pct](innodb-system-variables.md#innodb_max_dirty_pages_pct) variable specifies the maximum percentage of unwritten (dirty) pages in the [buffer pool](innodb-buffer-pool.md). If this percentage is exceeded, flushing will take place.

### innodb\_max\_dirty\_pages\_pct\_lwm

The [innodb\_max\_dirty\_pages\_pct\_lwm](innodb-system-variables.md#innodb_max_dirty_pages_pct_lwm) variable determines the low-water mark percentage of dirty pages that will enable preflushing to lower the dirty page ratio. The value 0 (the default) means that there are no separate background flushing so long as:

* the share of dirty pages does not exceed [innodb\_max\_dirty\_pages\_pct](innodb-system-variables.md#innodb_max_dirty_pages_pct)
* the last checkpoint age (LSN difference since the latest checkpoint) does not exceed [innodb\_log\_file\_size](innodb-system-variables.md#innodb_log_file_size) (minus some safety margin)
* the [buffer pool](innodb-buffer-pool.md) is not running out of space, which could trigger eviction flushing

To make flushing more eager, set to a higher value, for example `SET GLOBAL innodb_max_dirty_pages_pct_lwm=0.001;`

### Page Flushing with Multiple InnoDB Page Cleaner Threads

The [innodb\_page\_cleaners](innodb-system-variables.md#innodb_page_cleaners) system variable makes it possible to use multiple InnoDB page cleaner threads. It is deprecated and ignored now as the original reasons for splitting the buffer pool have mostly gone away.

The number of InnoDB page cleaner threads can be configured by setting the [innodb\_page\_cleaners](innodb-system-variables.md#innodb_page_cleaners) system variable. The system variable can be set in a server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server:

```
[mariadb]
...
innodb_page_cleaners=8
```

The system variable can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET GLOBAL innodb_page_cleaners=8;
```

This system variable's default value is either `4` or the configured value of the [innodb\_buffer\_pool\_instances](innodb-system-variables.md#innodb_buffer_pool_instances) system variable, whichever is lower.

### Page Flushing with a Single InnoDB Page Cleaner Thread

Since the original reasons for splitting the buffer pool have mostly gone away, only a single InnoDB page cleaner thread is supported.

## Page Flushing with Multi-threaded Flush Threads

InnoDB's multi-thread flush feature can be enabled by setting the [innodb\_use\_mtflush](innodb-system-variables.md#innodb_use_mtflush) system variable. The number of threads cane be configured by setting the [innodb\_mtflush\_threads](innodb-system-variables.md#innodb_mtflush_threads) system variable. This system variable can be set in a server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server:

```
[mariadb]
...
innodb_use_mtflush = ON
innodb_mtflush_threads = 8
```

The [innodb\_mtflush\_threads](innodb-system-variables.md#innodb_mtflush_threads) system variable's default value is `8`. The maximum value is `64`. In multi-core systems, it is recommended to set its value close to the configured value of the [innodb\_buffer\_pool\_instances](innodb-system-variables.md#innodb_buffer_pool_instances) system variable. However, it is also recommended to use your own benchmarks to find a suitable value for your particular application.

#### Note

InnoDB's multi-thread flush feature is deprecated. Use multiple InnoDB page cleaner threads instead.

## Configuring the InnoDB I/O Capacity

Increasing the amount of I/O capacity available to InnoDB can also help increase the performance of page flushing.

The amount of I/O capacity available to InnoDB can be configured by setting the [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity) system variable. This system variable can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET GLOBAL innodb_io_capacity=20000;
```

This system variable can also be set in a server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server:

```
[mariadb]
...
innodb_io_capacity=20000
```

The maximum amount of I/O capacity available to InnoDB in an emergency defaults to either `2000` or twice [innodb\_io\_capacity](innodb-system-variables.md#innodb_io_capacity), whichever is higher, or can be directly configured by setting the [innodb\_io\_capacity\_max](innodb-system-variables.md#innodb_io_capacity_max) system variable. This system variable can be changed dynamically with [SET GLOBAL](../../../reference/sql-statements/administrative-sql-statements/set-commands/set.md#global-session):

```sql
SET GLOBAL innodb_io_capacity_max=20000;
```

This system variable can also be set in a server [option group](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md#option-groups) in an [option file](../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) prior to starting up the server:

```
[mariadb]
...
innodb_io_capacity_max=20000
```

## See Also

* [Significant performance boost with new MariaDB page compression on FusionIO](https://blog.mariadb.org/significant-performance-boost-with-new-mariadb-page-compression-on-fusionio/)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
