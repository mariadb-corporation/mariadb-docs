# Setting Innodb Buffer Pool Size Dynamically

Resizing the buffer pool is performed in chunks determined by the size of the [innodb\_buffer\_pool\_chunk\_size](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_chunk_size) variable.

The resize operation waits until all active transactions and operations are completed, and new transactions and operations that need to access the buffer pool must wait until the resize is complete (although when decreasing the size, access is permitted when defragmenting and withdrawing pages).

Nested transactions may fail if started after the buffer pool resize has begun.

The new buffer pool size must be a multiple of [innodb\_buffer\_pool\_chunk\_size](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_chunk_size) \* [innodb\_buffer\_pool\_instances](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_instances) (note that `innodb_buffer_pool_instances` is ignored from [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), and removed in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106), as the buffer pool is no longer split into multiple instances). If you attempt to set a different figure, the value is automatically adjusted to a multiple of at least the attempted size. Note that adjusting the [innodb\_buffer\_pool\_chunk\_size](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_chunk_size) setting can result in a change in the buffer pool size.

The number of chunks as calculated by [innodb\_buffer\_pool\_size](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size) / [innodb\_buffer\_pool\_chunk\_size](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_chunk_size) should not exceed 1000 in order to avoid performance issues.

A background thread performs the resizing operation. The [Innodb\_buffer\_pool\_resize\_status](innodb-status-variables.md#innodb_buffer_pool_resize_status) status variable shows the progress of the resizing operation, for example:

```sql
SHOW STATUS LIKE 'Innodb_buffer_pool_resize_status';
+----------------------------------+----------------------------------+
| Variable_name                    | Value                            |
+----------------------------------+----------------------------------+
| Innodb_buffer_pool_resize_status | Resizing also other hash tables. |
+----------------------------------+----------------------------------+
```

or

```sql
SHOW STATUS LIKE 'Innodb_buffer_pool_resize_status';
+----------------------------------+----------------------------------------------------+
| Variable_name                    | Value                                              |
+----------------------------------+----------------------------------------------------+
| Innodb_buffer_pool_resize_status | Completed resizing buffer pool at 161103 16:26:54. |
+----------------------------------+----------------------------------------------------+
```

Progress is also logged in the [error log](../../../server-management/server-monitoring-logs/error-log.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
