# InnoDB Server Status Variables

See [Server Status Variables](server-status-variables.md) for a complete list of status variables that can be viewed with [SHOW STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-status.md).

Much of the [InnoDB](../../../server-usage/storage-engines/innodb/) information here can also be seen with a [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) statement.

See also the [Full list of MariaDB options, system and status variables](../../../reference/full-list-of-mariadb-options-system-and-status-variables.md).

#### `Innodb_adaptive_hash_cells`

* Description: As shown in the INSERT BUFFER AND ADAPTIVE HASH INDEX section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5), this status variable is present in XtraDB.
  * In [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1) and later, this status variable is not present.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)
* Removed: [MariaDB 10.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.0)

#### `Innodb_adaptive_hash_hash_searches`

* Description: Hash searches as shown in the INSERT BUFFER AND ADAPTIVE HASH INDEX section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * Before the variable was introduced in [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0), use the `adaptive_hash_searches` counter in the [information\_schema.INNODB\_METRICS](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md) table instead.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_adaptive_hash_heap_buffers`

* Description: As shown in the INSERT BUFFER AND ADAPTIVE HASH INDEX section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5), this status variable is present in XtraDB.
  * In [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1) and later, this status variable is not present.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)
* Removed: [MariaDB 10.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.0)

#### `Innodb_adaptive_hash_non_hash_searches`

* Description: Non-hash searches as shown in the INSERT BUFFER AND ADAPTIVE HASH INDEX section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output. From [MariaDB 10.6.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1062-release-notes), not updated if [innodb\_adaptive\_hash\_index](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_hash_index) is not enabled (the default).
  * In [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present. Use the `adaptive_hash_searches_btree` counter in the [information\_schema.INNODB\_METRICS](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md) table instead.
  * From [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable is present.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_async_reads_pending`

* Description: Number of async read I/O operations currently in progress (from SUBMITTED to COMPLETED). See [InnoDB Asynchronous I/O](../../../server-usage/storage-engines/innodb/innodb-asynchronous-io.md).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115)

#### `Innodb_async_reads_queue_size`

* Description: Current size of the async I/O read queue. See [InnoDB Asynchronous I/O Queuing Mechanism](innodb-status-variables.md#queuing-mechanism).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115)

#### `Innodb_async_reads_tasks_running`

* Description: Number of async read I/O operations currently in the EXECUTING\_COMPLETION\_TASK state. See [InnoDB Asynchronous I/O](../../../server-usage/storage-engines/innodb/innodb-asynchronous-io.md).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115)

#### `Innodb_async_reads_total_count`

* Description: Total number of async read completion tasks that have finished execution. See [InnoDB Asynchronous I/O](../../../server-usage/storage-engines/innodb/innodb-asynchronous-io.md).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115)

#### `Innodb_async_reads_total_enqueues`

* Description: Total number of async read operations that were queued. Includes those still waiting and making up [innodb\_async\_reads\_queue\_size](innodb-status-variables.md#innodb_async_reads_queue_size). See [InnoDB Asynchronous I/O](../../../server-usage/storage-engines/innodb/innodb-asynchronous-io.md).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115)

#### `Innodb_async_reads_wait_slot_sec`

* Description: Total wait time for a free I/O slot (see Waiting for IO Slots). See [InnoDB Asynchronous I/O Waiting for IO Slots](../../../server-usage/storage-engines/innodb/innodb-asynchronous-io.md#waiting-for-io-slots).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115)

#### `Innodb_async_writes_pending`

* Description: Number of async write I/O operations currently in progress (from SUBMITTED to COMPLETED). See [InnoDB Asynchronous I/O](../../../server-usage/storage-engines/innodb/innodb-asynchronous-io.md).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115)

#### `Innodb_async_writes_queue_size`

* Description: Current size of the async I/O write queue. See [InnoDB Asynchronous I/O Queuing Mechanism](../../../server-usage/storage-engines/innodb/innodb-asynchronous-io.md#queuing-mechanism).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115)

#### `Innodb_async_writes_tasks_running`

* Description: Number of async write I/O operations currently in the EXECUTING\_COMPLETION\_TASK state. See [InnoDB Asynchronous I/O](../../../server-usage/storage-engines/innodb/innodb-asynchronous-io.md).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115)

#### `Innodb_async_writes_total_count`

* Description: Total number of async write completion tasks that have finished execution. See [InnoDB Asynchronous I/O](../../../server-usage/storage-engines/innodb/innodb-asynchronous-io.md).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115)

#### `Innodb_async_writes_total_enqueues`

* Description: Total number of async write operations that were queued. Includes those still waiting and making up [innodb\_async\_writes\_queue\_size](innodb-status-variables.md#innodb_async_writes_queue_size). See [InnoDB Asynchronous I/O](../../../server-usage/storage-engines/innodb/innodb-asynchronous-io.md).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115)

#### `Innodb_async_writes_wait_slot_sec`

* Description: See [InnoDB Asynchronous I/O](../../../server-usage/storage-engines/innodb/innodb-asynchronous-io.md).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.5/what-is-mariadb-115)

#### `Innodb_available_undo_logs`

* Description: Total number available InnoDB [undo logs](../../../server-usage/storage-engines/innodb/innodb-undo-log.md). Differs from the [innodb\_undo\_logs](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_undo_logs) system variable, which specifies the number of active undo logs.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_background_log_sync`

* Description: As shown in the BACKGROUND THREAD section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5), this status variable is present in XtraDB.
  * In [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_buffer_pool_bytes_data`

* Description: Number of bytes contained in the [InnoDB buffer pool](../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md), both dirty (modified) and clean (unmodified). See also [Innodb\_buffer\_pool\_pages\_data](innodb-status-variables.md#innodb_buffer_pool_pages_data), which can contain pages of different sizes in the case of compression.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_buffer_pool_bytes_dirty`

* Description: Number of dirty (modified) bytes contained in the [InnoDB buffer pool](../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md). See also [Innodb\_buffer\_pool\_pages\_dirty](innodb-status-variables.md#innodb_buffer_pool_pages_dirty), which can contain pages of different sizes in the case of compression.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_buffer_pool_dump_status`

* Description: A text description of the progress or final status of the last Innodb buffer pool dump.
* Scope: Global
* Data Type: `string`
* Introduced: [MariaDB 10.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.0)

#### `Innodb_buffer_pool_load_incomplete`

* Description: Whether or not the loaded buffer pool is incomplete, for example after a shutdown or abort during innodb buffer pool load from file caused an incomplete save.
* Scope: Global
* Data Type: `boolean`
* Introduced: [MariaDB 10.3.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.5)

#### `Innodb_buffer_pool_load_status`

* Description: A text description of the progress or final status of the last Innodb buffer pool load.
* Scope: Global
* Data Type: `string`
* Introduced: [MariaDB 10.0.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.0)

#### `Innodb_buffer_pool_pages_data`

* Description: Number of [InnoDB buffer pool](../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md) pages which contain data, both dirty (modified) and clean (unmodified). See also [Innodb\_buffer\_pool\_bytes\_data](innodb-status-variables.md#innodb_buffer_pool_bytes_data).
* Scope: Global
* Data Type: `numeric`

#### `Innodb_buffer_pool_pages_dirty`

* Description: Number of [InnoDB buffer pool](../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md) pages which contain dirty (modified) data. See also [innodb\_buffer\_pool\_bytes\_dirty](innodb-status-variables.md#innodb_buffer_pool_bytes_dirty).
* Scope: Global
* Data Type: `numeric`

#### `Innodb_buffer_pool_pages_flushed`

* Description: Number of [InnoDB buffer pool](../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md) pages which have been flushed.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_buffer_pool_pages_LRU_flushed`

* Description: Flush list as shown in the INSERT BUFFER AND ADAPTIVE HASH INDEX section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_buffer_pool_pages_LRU_freed`

* Description: Monitor the number of pages that were freed by a buffer pool LRU eviction scan, without flushing.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1060-release-notes)

#### `Innodb_buffer_pool_pages_free`

* Description: Number of free [InnoDB buffer pool](../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md) pages.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_buffer_pool_pages_made_not_young`

* Description: Pages not young as shown in the INSERT BUFFER AND ADAPTIVE HASH INDEX section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_buffer_pool_pages_made_young`

* Description: Pages made young as shown in the INSERT BUFFER AND ADAPTIVE HASH INDEX section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_buffer_pool_pages_misc`

* Description: Number of [InnoDB buffer pool](../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md) pages set aside for internal use.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_buffer_pool_pages_old`

* Description: Old database page, as shown in the BUFFER POOL AND MEMORY section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present for XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_buffer_pool_pages_total`

* Description: Total number of [InnoDB buffer pool](../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md) pages.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_buffer_pool_read_ahead`

* Description: Number of pages read into the [InnoDB buffer pool](../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md) by the read-ahead background thread.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_buffer_pool_read_ahead_evicted`

* Description: Number of pages read into the [InnoDB buffer pool](../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md) by the read-ahead background thread that were evicted without having been accessed by queries.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_buffer_pool_read_ahead_rnd`

* Description: Number of random read-aheads.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_buffer_pool_read_requests`

* Description: Number of requests to read from the [InnoDB buffer pool](../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md) .
* Scope: Global
* Data Type: `numeric`

#### `Innodb_buffer_pool_reads`

* Description: Number of reads that could not be satisfied by the [InnoDB buffer pool](../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md) and had to be read from disk.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_buffer_pool_resize_status`

* Description: Progress of the dynamic [InnoDB buffer pool](../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md) resizing operation. See [Setting Innodb Buffer Pool Size Dynamically](setting-innodb-buffer-pool-size-dynamically.md).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.2)

#### `Innodb_buffer_pool_wait_free`

* Description: Number of times InnoDB waited for a free page before reading or creating a page. Normally, writes to the [InnoDB buffer pool](../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md) happen in the background. When no clean pages are available, dirty pages are flushed first in order to free some up. This counts the numbers of wait for this operation to finish. If this value is not small, look at increasing [innodb\_buffer\_pool\_size](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size).
* Scope: Global
* Data Type: `numeric`

#### `Innodb_buffer_pool_write_requests`

* Description: Number of requests to write to the [InnoDB buffer pool](../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md) .
* Scope: Global
* Data Type: `numeric`

#### `Innodb_buffered_aio_submitted`

* Description:
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_bulk_operations`

* Description: Number of bulk insert operations to InnoDB tables.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.6.19](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-19-release-notes), [MariaDB 10.11.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-9-release-notes), [MariaDB 11.1.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/11.1.6), [MariaDB 11.2.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.2/11.2.5), [MariaDB 11.4.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-3-release-notes)

#### `Innodb_checkpoint_age`

* Description: The amount of data written to the InnoDB redo log since the last checkpoint, as shown in the LOG section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output. (This is equivalent to subtracting "Last checkpoint at" from "Log sequence number", cf the [RedoLog details](../../../server-usage/storage-engines/innodb/innodb-redo-log.md)). Despite the name ("age"), the value is not a duration, but really an amount of data (in bytes) !
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_checkpoint_max_age`

* Description: Max checkpoint age, as shown in the LOG section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_checkpoint_target_age`

* Description: Checkpoint age target, as shown in the LOG section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output. XtraDB only. Removed in [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0) and replaced with MySQL 5.6's flushing implementation.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0)

#### `Innodb_current_row_locks`

* Description: Number of current row locks on InnoDB tables as shown in the TRANSACTIONS section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output. Renamed from [InnoDB\_row\_lock\_numbers](innodb-status-variables.md#innodb_row_lock_numbers) in XtraDB 5.5.8-20.1.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)

#### `Innodb_data_fsyncs`

* Description: Number of InnoDB fsync (sync-to-disk) calls. fsync call frequency can be influenced by the [innodb\_flush\_method](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_flush_method) configuration option.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_data_pending_fsyncs`

* Description: Number of pending InnoDB fsync (sync-to-disk) calls. fsync call frequency can be influenced by the [innodb\_flush\_method](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_flush_method) configuration option.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_data_pending_reads`

* Description: Number of pending InnoDB reads.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_data_pending_writes`

* Description: Number of pending InnoDB writes.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_data_read`

* Description: Number of InnoDB bytes read since server startup (not to be confused with [Innodb\_data\_reads](innodb-status-variables.md#innodb_data_reads)).
* Scope: Global
* Data Type: `numeric`

#### `Innodb_data_reads`

* Description: Number of InnoDB read operations (not to be confused with [Innodb\_data\_read](innodb-status-variables.md#innodb_data_read)).
* Scope: Global
* Data Type: `numeric`

#### `Innodb_data_writes`

* Description: Number of InnoDB write operations.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_data_written`

* Description: Number of InnoDB bytes written since server startup. From [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.1), no longer includes writes to the redo log file `ib_logfile0`, which continue to be counted by [Innodb\_os\_log\_written](innodb-status-variables.md#innodb_os_log_written). An error in counting was introduced in [MariaDB 10.5.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.7) until [MariaDB 10.5.20](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.20), [MariaDB 10.6.13](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-10-6-13-release-notes), [MariaDB 10.8.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/10.8.8), [MariaDB 10.9.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.9/10.9.6), [MariaDB 10.10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/10.10.4) and [MariaDB 10.11.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10-11-3-release-notes) ([MDEV-31124](https://jira.mariadb.org/browse/MDEV-31124)) in which writes via the doublewrite buffer started to be counted incorrectly, without multiplying them by innodb\_page\_size. A workaround for the error could be the following formulae: real\_data\_written = Innodb\_data\_written + (innodb\_page\_size - 1) \* Innodb\_dblwr\_pages\_writteninnodb\_written = real\_data\_written + Innodb\_os\_log\_written
* Scope: Global
* Data Type: `numeric`

#### `Innodb_dblwr_pages_written`

* Description: Number of pages written to the [InnoDB doublewrite buffer](../../../server-usage/storage-engines/innodb/innodb-doublewrite-buffer.md).
* Scope: Global
* Data Type: `numeric`

#### `Innodb_dblwr_writes`

* Description: Number of writes to the [InnoDB doublewrite buffer](../../../server-usage/storage-engines/innodb/innodb-doublewrite-buffer.md).
* Scope: Global
* Data Type: `numeric`

#### `Innodb_deadlocks`

* Description: Total number of InnoDB deadlocks. Deadlocks occur when at least two transactions are waiting for the other to finish, creating a circular dependency. InnoDB usually detects these quickly, returning an error.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_defragment_compression_failures`

* Description: Number of defragment re-compression failures. See [Defragmenting InnoDB Tablespaces](../optimizing-tables/defragmenting-innodb-tablespaces.md).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.1)

#### `Innodb_defragment_count`

* Description: Number of defragment operations. See [Defragmenting InnoDB Tablespaces](../optimizing-tables/defragmenting-innodb-tablespaces.md).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.1)

#### `Innodb_defragment_failures`

* Description: Number of defragment failures. See [Defragmenting InnoDB Tablespaces](../optimizing-tables/defragmenting-innodb-tablespaces.md).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.1)

#### `Innodb_dict_tables`

* Description: Number of entries in the XtraDB data dictionary cache. This Percona XtraDB variable was removed in MariaDB 10/XtraDB 5.6 as it was replaced with MySQL 5.6's [table\_definition\_cache](server-system-variables.md#table_definition_cache) implementation.
* Scope: Global
* Data Type: `numeric`
* Introduced: XtraDB 5.0.77-b13
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0)

#### `Innodb_encryption_n_merge_blocks_decrypted`

* Description:
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.1.28](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.28), [MariaDB 10.2.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.9), [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.2)

#### `Innodb_encryption_n_merge_blocks_encrypted`

* Description:
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.1.28](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.28), [MariaDB 10.2.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.9), [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.2)

#### `Innodb_encryption_n_rowlog_blocks_decrypted`

* Description:
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.1.28](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.28), [MariaDB 10.2.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.9), [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.2)

#### `Innodb_encryption_n_rowlog_blocks_encrypted`

* Description:
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.1.28](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.28), [MariaDB 10.2.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.9), [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.2)

#### `Innodb_encryption_n_temp_blocks_decrypted`

* Description:
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.26), [MariaDB 10.3.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.17), [MariaDB 10.4.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.7)

#### `Innodb_encryption_n_temp_blocks_encrypted`

* Description:
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.26), [MariaDB 10.3.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.17), [MariaDB 10.4.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/10.4.7)

#### `Innodb_encryption_num_key_requests`

* Description: Was not present in [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.2).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.4)

#### `Innodb_encryption_rotation_estimated_iops`

* Description: See [Table and Tablespace Encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview.md).
* Scope: Global
* Data Type: `numeric`
* Removed: [MariaDB 10.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.3)

#### `Innodb_encryption_rotation_pages_flushed`

* Description: See [Table and Tablespace Encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview.md).
* Scope: Global
* Data Type: `numeric`
* Removed: [MariaDB 10.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.3)

#### `Innodb_encryption_rotation_pages_modified`

* Description: See [Table and Tablespace Encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview.md).
* Scope: Global
* Data Type: `numeric`
* Removed: [MariaDB 10.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.3)

#### `Innodb_encryption_rotation_pages_read_from_cache`

* Description: See [Table and Tablespace Encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview.md).
* Scope: Global
* Data Type: `numeric`
* Removed: [MariaDB 10.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.3)

#### `Innodb_encryption_rotation_pages_read_from_disk`

* Description: See [Table and Tablespace Encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview.md).
* Scope: Global
* Data Type: `numeric`
* Removed: [MariaDB 10.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.3)

#### `Innodb_have_atomic_builtins`

* Description: Whether the server has been built with atomic instructions, provided by the CPU ensuring that critical low-level operations can't be interrupted. XtraDB only.
* Scope: Global
* Data Type: `boolean`

#### `Innodb_have_bzip2`

* Description: Whether the server has the bzip2 compression method available. See [InnoDB/XtraDB Page Compression](../../../server-usage/storage-engines/innodb/innodb-page-compression.md).
* Scope: Global
* Data Type: `boolean`
* Introduced: [MariaDB 10.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.0)

#### `Innodb_have_lz4`

* Description: Whether the server has the lz4 compression method available. See [InnoDB/XtraDB Page Compression](../../../server-usage/storage-engines/innodb/innodb-page-compression.md).
* Scope: Global
* Data Type: `boolean`
* Introduced: [MariaDB 10.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.0)

#### `Innodb_have_lzma`

* Description: Whether the server has the lzma compression method available. See [InnoDB/XtraDB Page Compression](../../../server-usage/storage-engines/innodb/innodb-page-compression.md).
* Scope: Global
* Data Type: `boolean`
* Introduced: [MariaDB 10.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.0)

#### `Innodb_have_lzo`

* Description: Whether the server has the lzo compression method available. See [InnoDB/XtraDB Page Compression](../../../server-usage/storage-engines/innodb/innodb-page-compression.md).
* Scope: Global
* Data Type: `boolean`
* Introduced: [MariaDB 10.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.0)

#### `Innodb_have_punch_hole`

* Description:
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.4)

#### `Innodb_have_snappy`

* Description: Whether the server has the snappy compression method available. See [InnoDB/XtraDB Page Compression](../../../server-usage/storage-engines/innodb/innodb-page-compression.md).
* Scope: Global
* Data Type: `boolean`
* Introduced: [MariaDB 10.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.3)

#### `Innodb_history_list_length`

* Description: History list length as shown in the TRANSACTIONS section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output. XtraDB only until introduced in [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_ibuf_discarded_delete_marks`

* Description: As shown in the INSERT BUFFER AND ADAPTIVE HASH INDEX section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_ibuf_discarded_deletes`

* Description: As shown in the INSERT BUFFER AND ADAPTIVE HASH INDEX section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_ibuf_discarded_inserts`

* Description: As shown in the INSERT BUFFER AND ADAPTIVE HASH INDEX section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_ibuf_free_list`

* Description: As shown in the INSERT BUFFER AND ADAPTIVE HASH INDEX section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_ibuf_merged_delete_marks`

* Description: As shown in the INSERT BUFFER AND ADAPTIVE HASH INDEX section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_ibuf_merged_deletes`

* Description: As shown in the INSERT BUFFER AND ADAPTIVE HASH INDEX section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_ibuf_merged_inserts`

* Description: As shown in the INSERT BUFFER AND ADAPTIVE HASH INDEX section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_ibuf_merges`

* Description: As shown in the INSERT BUFFER AND ADAPTIVE HASH INDEX section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_ibuf_segment_size`

* Description: As shown in the INSERT BUFFER AND ADAPTIVE HASH INDEX section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_ibuf_size`

* Description: As shown in the INSERT BUFFER AND ADAPTIVE HASH INDEX section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_instant_alter_column`

* Description: See [Instant ADD COLUMN for InnoDB](../../../server-usage/storage-engines/innodb/innodb-online-ddl/instant-add-column-for-innodb.md).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.3.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.2)

#### `Innodb_log_waits`

* Description: Number of times InnoDB was forced to wait for log writes to be flushed due to the log buffer being too small.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_log_write_requests`

* Description: Number of requests to write to the InnoDB redo log.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_log_writes`

* Description: Number of writes to the InnoDB redo log.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_lsn_current`

* Description: Log sequence number as shown in the LOG section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_lsn_flushed`

* Description: Flushed up to log sequence number as shown in the LOG section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_lsn_last_checkpoint`

* Description: Log sequence number last checkpoint as shown in the LOG section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_master_thread_1_second_loops`

* Description: As shown in the BACKGROUND THREAD section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5), this status variable is present in XtraDB.
  * In [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1) and later, this status variable is not present.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0)

#### `Innodb_master_thread_10_second_loops`

* Description: As shown in the BACKGROUND THREAD section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5), this status variable is present in XtraDB.
  * In [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1) and later, this status variable is not present
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0)

#### `Innodb_master_thread_active_loops`

* Description: As shown in the BACKGROUND THREAD section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.0.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.9) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0):

#### `Innodb_master_thread_background_loops`

* Description: As shown in the BACKGROUND THREAD section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5), this status variable is present in XtraDB.
  * In [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1) and later, this status variable is not present
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0)

#### `Innodb_master_thread_idle_loops`

* Description: As shown in the BACKGROUND THREAD section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.0.9](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.9) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0):

#### `Innodb_master_thread_main_flush_loops`

* Description: As shown in the BACKGROUND THREAD section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5), this status variable is present in XtraDB.
  * In [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1) and later, this status variable is not present
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0)

#### `Innodb_master_thread_sleeps`

* Description: As shown in the BACKGROUND THREAD section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine.md) output. XtraDB only.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5), this status variable is present in XtraDB.
  * In [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present. Use the `innodb_master_thread_sleeps` counter in the [information\_schema.INNODB\_METRICS](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_metrics-table.md) table instead.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)
* Removed: [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0)

#### `Innodb_max_trx_id`

* Description: As shown in the TRANSACTIONS section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_mem_adaptive_hash`

* Description: As shown in the BUFFER POOL AND MEMORY section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_mem_dictionary`

* Description: As shown in the BUFFER POOL AND MEMORY section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102), [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), and [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104), this status variable is not present.
  * In [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105), this status variable was reintroduced.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) (XtraDB-only), [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.0)

#### `Innodb_mem_total`

* Description: As shown in the BUFFER POOL AND MEMORY section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102) and later, this status variable is not present.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)

#### `Innodb_mutex_os_waits`

* Description: Mutex OS waits as shown in the SEMAPHORES section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102) and later, this status variable is not present.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)

#### `Innodb_mutex_spin_rounds`

* Description: Mutex spin rounds as shown in the SEMAPHORES section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102) and later, this status variable is not present.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)

#### `Innodb_mutex_spin_waits`

* Description: Mutex spin waits as shown in the SEMAPHORES section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102) and later, this status variable is not present.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)

#### `Innodb_num_index_pages_written`

* Description:
* Scope:
* Data Type: `numeric`
* Introduced: [MariaDB 10.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.0)

#### `Innodb_num_non_index_pages_written`

* Description:
* Scope:
* Data Type: `numeric`
* Introduced: [MariaDB 10.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.0)

#### `Innodb_num_open_files`

* Description: Number of open files held by InnoDB. InnoDB only.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_num_page_compressed_trim_op`

* Description: Number of trim operations performed.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_num_page_compressed_trim_op_saved`

* Description: Number of trim operations not done because of an earlier trim.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_num_pages_decrypted`

* Description: Number of pages page decrypted. See [Table and Tablespace Encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview.md).
* Scope: Global
* Data Type: `numeric`

#### `Innodb_num_pages_encrypted`

* Description: Number of pages page encrypted. See [Table and Tablespace Encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview.md).
* Scope: Global
* Data Type: `numeric`

#### `Innodb_num_pages_page_compressed`

* Description: Number of pages that are page compressed.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_num_pages_page_compression_error`

* Description: Number of compression errors.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_num_pages_page_decompressed`

* Description: Number of pages compressed with page compression that are decompressed.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_num_pages_page_encryption_error`

* Description: Number of page encryption errors. See [Table and Tablespace Encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview.md).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.3)
* Removed: [MariaDB 10.1.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.4)

#### `Innodb_oldest_view_low_limit_trx_id`

* Description: As shown in the TRANSACTIONS section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102) and later, this status variable is not present.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)
* Removed: [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102)

#### `Innodb_onlineddl_pct_progress`

* Description: Shows the progress of in-place alter table. It might be not so accurate because in-place alter is highly dependent on disk and buffer pool status. See [Monitoring progress and temporal memory usage of Online DDL in InnoDB](https://blog.mariadb.org/monitoring-progress-and-temporal-memory-usage-of-online-ddl-in-innodb).
* Scope: Global
* Data Type: `numeric`

#### `Innodb_onlineddl_rowlog_pct_used`

* Description: Shows row log buffer usage in 5-digit integer (10000 means 100.00%). See [Monitoring progress and temporal memory usage of Online DDL in InnoDB](https://blog.mariadb.org/monitoring-progress-and-temporal-memory-usage-of-online-ddl-in-innodb).
* Scope: Global
* Data Type: `numeric`

#### `Innodb_onlineddl_rowlog_rows`

* Description: Number of rows stored in the row log buffer. See [Monitoring progress and temporal memory usage of Online DDL in InnoDB](https://blog.mariadb.org/monitoring-progress-and-temporal-memory-usage-of-online-ddl-in-innodb).
* Scope: Global
* Data Type: `numeric`

#### `Innodb_os_log_fsyncs`

* Description: Number of InnoDB log fsync (sync-to-disk) requests.
* Scope: Global
* Data Type: `numeric`
* Removed: [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/what-is-mariadb-108)

#### `Innodb_os_log_pending_fsyncs`

* Description: Number of pending InnoDB log fsync (sync-to-disk) requests.
* Scope: Global
* Data Type: `numeric`
* Removed: [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/what-is-mariadb-108)

#### `Innodb_os_log_pending_writes`

* Description: Number of pending InnoDB log writes.
* Scope: Global
* Data Type: `numeric`
* Removed: [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/what-is-mariadb-108)

#### `Innodb_os_log_written`

* Description: Number of bytes written to the InnoDB log.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_page_compression_saved`

* Description: Number of bytes saved by page compression.
* Scope:
* Data Type:

#### `Innodb_page_compression_trim_sect512`

* Description: Number of TRIM operations performed for the page-compression/NVM Compression workload for the 512 byte block-size.
* Scope:
* Data Type: `numeric`
* Introduced: [MariaDB 10.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.0), [MariaDB 10.0.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.15) Fusion-io
* Removed: [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.4)

#### `Innodb_page_compression_trim_sect1024`

* Description: Number of TRIM operations performed for the page-compression/NVM Compression workload for the 1K block-size.
* Scope:
* Data Type: `numeric`
* Introduced: [MariaDB 10.1.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/changelogs/changelogs-mariadb-101-series/mariadb-10120-changelog), [MariaDB 10.0.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.15) Fusion-io
* Removed: [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.4)

#### `Innodb_page_compression_trim_sect2048`

* Description: Number of TRIM operations performed for the page-compression/NVM Compression workload for the 2K block-size.
* Scope:
* Data Type: `numeric`
* Introduced: [MariaDB 10.1.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/changelogs/changelogs-mariadb-101-series/mariadb-10120-changelog), [MariaDB 10.0.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.15) Fusion-io
* Removed: [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.4)

#### `Innodb_page_compression_trim_sect4096`

* Description: Number of TRIM operations performed for the page-compression/NVM Compression workload for the 4K block-size.
* Scope:
* Data Type: `numeric`
* Introduced: [MariaDB 10.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.0), [MariaDB 10.0.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.15) Fusion-io
* Removed: [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.4)

#### `Innodb_page_compression_trim_sect8192`

* Description: Number of TRIM operations performed for the page-compression/NVM Compression workload for the 8K block-size.
* Scope:
* Data Type: `numeric`
* Introduced:[MariaDB 10.1.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/changelogs/changelogs-mariadb-101-series/mariadb-10120-changelog), [MariaDB 10.0.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.15) Fusion-io
* Removed: [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.4)

#### `Innodb_page_compression_trim_sect16384`

* Description: Number of TRIM operations performed for the page-compression/NVM Compression workload for the 16K block-size.
* Scope:
* Data Type: `numeric`
* Introduced: [MariaDB 10.1.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/changelogs/changelogs-mariadb-101-series/mariadb-10120-changelog), [MariaDB 10.0.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.15) Fusion-io
* Removed: [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.4)

#### `Innodb_page_compression_trim_sect32768`

* Description: Number of TRIM operations performed for the page-compression/NVM Compression workload for the 32K block-size.
* Scope:
* Data Type: `numeric`
* Introduced: [MariaDB 10.1.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/changelogs/changelogs-mariadb-101-series/mariadb-10120-changelog), [MariaDB 10.0.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.15) Fusion-io
* Removed: [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.4)

#### `Innodb_page_size`

* Description: Page size used by InnoDB. Defaults to 16KB, can be compiled with a different value.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_pages_created`

* Description: Number of InnoDB pages created.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_pages_read`

* Description: Number of InnoDB pages read.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_pages0_read`

* Description: Counter for keeping track of reads of the first page of InnoDB data files, because the original implementation of data-at-rest-encryption for InnoDB introduced new code paths for reading the pages. Removed in [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104) as the extra reads of the first page were removed, and the encryption subsystem will be initialized whenever we first read the first page of each data file, in fil\_node\_open\_file().
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.4), [MariaDB 10.1.21](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.21)
* Removed: [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104)

#### `Innodb_pages_written`

* Description: Number of InnoDB pages written.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_purge_trx_id`

* Description: Purge transaction id as shown in the TRANSACTIONS section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102) and later, this status variable is not present.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)
* Removed: [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102)

#### `Innodb_purge_undo_no`

* Description: As shown in the TRANSACTIONS section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102) and later, this status variable is not present.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)
* Removed: [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102)

#### `Innodb_read_views_memory`

* Description: As shown in the BUFFER POOL AND MEMORY section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output. Shows the total of memory in bytes allocated for the InnoDB read view.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102) and later, this status variable is not present.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5.32](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/5.5.32)
* Removed: [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102)

#### `Innodb_row_lock_current_waits`

* Description: Number of pending row lock waits on InnoDB tables.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_row_lock_numbers`

* Description: Number of current row locks on InnoDB tables as shown in the TRANSACTIONS section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output. Renamed to [InnoDB\_current\_row\_locks](innodb-status-variables.md#innodb_current_row_locks) in XtraDB 5.5.10-20.1.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) / XtraDB 5.5.8-20
* Removed: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) / XtraDB 5.5.10-20.1

#### `Innodb_row_lock_time`

* Description: Total time in milliseconds spent getting InnoDB row locks.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_row_lock_time_avg`

* Description: Average time in milliseconds spent getting an InnoDB row lock.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_row_lock_time_max`

* Description: Maximum time in milliseconds spent getting an InnoDB row lock.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_row_lock_waits`

* Description: Number of times InnoDB had to wait before getting a row lock.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_rows_deleted`

* Description: Number of rows deleted from InnoDB tables that where not system tables. Almost equivalent to [Handler\_delete](server-status-variables.md#handler_delete) which does include system tables.
* Scope: Global
* Data Type: `numeric`
* Removed: [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/what-is-mariadb-1010)

#### `Innodb_rows_inserted`

* Description: Number of rows inserted into InnoDB tables that where not system tables. No direct equivalent in [Handler](server-status-variables.md#handler_commit) status variables.
* Scope: Global
* Data Type: `numeric`
* Removed: [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/what-is-mariadb-1010)

#### `Innodb_rows_read`

* Description: Number of rows read from InnoDB tables that where not system tables. Almost equivalent to the sum of [Handler\_read\*](server-status-variables.md#handler_read_first) status variables which do include system tables.
* Scope: Global
* Data Type: `numeric`
* Removed: [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/what-is-mariadb-1010)

#### `Innodb_rows_updated`

* Description: Number of rows updated in InnoDB tables that where not system tables. Almost equivalent to [Handler\_update](server-status-variables.md#handler_update) which does include system tables.
* Scope: Global
* Data Type: `numeric`
* Removed: [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/what-is-mariadb-1010)

#### `Innodb_s_lock_os_waits`

* Description: As shown in the SEMAPHORES section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102) and later, this status variable is not present.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)
* Removed: [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102)

#### `Innodb_s_lock_spin_rounds`

* Description: As shown in the SEMAPHORES section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102) and later, this status variable is not present.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)
* Removed: [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102)

#### `Innodb_s_lock_spin_waits`

* Description: As shown in the SEMAPHORES section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102) and later, this status variable is not present.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)
* Removed: [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102)

#### `Innodb_scrub_background_page_reorganizations`

* Description: See [Table and Tablespace Encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview.md).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.3)
* Removed: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.2)

#### `Innodb_scrub_background_page_split_failures_missing_index`

* Description: See [Table and Tablespace Encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview.md).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.3)
* Removed: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.2)

#### `Innodb_scrub_background_page_split_failures_out_of_filespace`

* Description: See [Table and Tablespace Encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview.md).
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.1.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.3)
* Removed: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.2)

#### `Innodb_scrub_background_page_split_failures_underflow`

* Description: See [Table and Tablespace Encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview.md).
* Scope: Global
* Data Type: `numeric`
* Removed: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.2)

#### `Innodb_scrub_background_page_split_failures_unknown`

* Description: See [Table and Tablespace Encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview.md).
* Scope: Global
* Data Type: `numeric`
* Removed: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.2)

#### `Innodb_scrub_background_page_splits`

* Description: See [Table and Tablespace Encryption](../../../security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview.md).
* Scope: Global
* Data Type: `numeric`
* Removed: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.2)

#### `Innodb_scrub_log`

* Description:
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.4)
* Removed: [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.2)

#### `Innodb_secondary_index_triggered_cluster_reads`

* Description: Used to track the effectiveness of the Prefix Index Queries Optimization ([MDEV-6929](https://jira.mariadb.org/browse/MDEV-6929)). Removed in [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/what-is-mariadb-1010) as the optimization is now always enabled.
* Scope: Global
* Data Type: `numeric`
* Removed: [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/what-is-mariadb-1010)

#### `Innodb_secondary_index_triggered_cluster_reads_avoided`

* Description: Used to track the effectiveness of the Prefix Index Queries Optimization ([MDEV-6929](https://jira.mariadb.org/browse/MDEV-6929)). Removed in [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/what-is-mariadb-1010) as the optimization is now always enabled.
* Scope: Global
* Data Type: `numeric`
* Removed: [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/what-is-mariadb-1010)

#### `Innodb_system_rows_deleted`

* Description: Number of rows deleted on system tables.
* Scope: Global
* Data Type: `numeric`
* Removed: [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/what-is-mariadb-1010)

#### `Innodb_system_rows_inserted`

* Description: Number of rows inserted on system tables.
* Scope: Global
* Data Type: `numeric`
* Removed: [MariaDB 10.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/what-is-mariadb-1010)

#### `Innodb_system_rows_read`

* Description: Number of rows read on system tables.
* Scope: Global
* Data Type: `numeric`
* Removed: [MariaDB 10.10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/10.10.0)

#### `Innodb_system_rows_updated`

* Description: Number of rows updated on system tables.
* Scope: Global
* Data Type: `numeric`
* Removed: [MariaDB 10.10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.10/10.10.0)

#### `Innodb_truncated_status_writes`

* Description: Number of times output from [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) has been truncated.
* Scope: Global
* Data Type: `numeric`

#### `Innodb_undo_truncations`

* Description: Number of undo tablespace truncation operations.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 10.3.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.10)

#### `Innodb_x_lock_os_waits`

* Description: As shown in the SEMAPHORES section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102) and later, this status variable is not present.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)
* Removed: [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102)

#### `Innodb_x_lock_spin_rounds`

* Description: As shown in the SEMAPHORES section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102) and later, this status variable is not present.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)
* Removed: [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102)

#### `Innodb_x_lock_spin_waits`

* Description: As shown in the SEMAPHORES section of the [SHOW ENGINE INNODB STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-engine-innodb-status.md) output.
  * In [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5) and [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1), this status variable is present in XtraDB.
  * In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102) and later, this status variable is not present.
* Scope: Global
* Data Type: `numeric`
* Introduced: [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.5/changes-improvements-in-mariadb-5-5)
* Removed: [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/what-is-mariadb-102)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
