---
description: >-
  Plan MariaDB memory usage by sizing global caches, per-connection buffers, and
  engine-specific settings to avoid swapping and out-of-memory conditions.
---

# MariaDB Memory Allocation

### Quick Recommendations

{% hint style="info" %}
Size MariaDB against **available RAM**, not total installed RAM.

On a dedicated host, available RAM means total RAM minus operating system needs and other running services. In containers or VMs, use the effective memory limit and leave headroom for the OS, filesystem cache, and temporary per-connection allocations.
{% endhint %}

Start with these defaults:

* Mostly InnoDB: set [innodb\_buffer\_pool\_size](../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size) to about 60% to 70% of available RAM. Keep [key\_buffer\_size](../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size) small, such as `16M` to `64M`, unless you use MyISAM indexes.
* Mostly [MyISAM](../server-usage/storage-engines/myisam-storage-engine/): set [key\_buffer\_size](../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size) to about 20% of available RAM. Set [innodb\_buffer\_pool\_size](../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size) to `0` only if you do not use InnoDB at all.
* Mixed engines: prioritize InnoDB first. Then size [key\_buffer\_size](../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size) to actual MyISAM index usage.
* Hosts with less than 4 GB of RAM: use lower percentages and leave extra headroom.

Use these as starting points:

* Start from the packaged `my.cnf` or `my.ini`.
* Change only the major cache settings first.
* Fix slow queries with indexes, schema changes, or query changes before tuning smaller buffers.
* Keep the settings in the `[mysqld]` section.
* Restart the server after file-based changes.

Memory problems usually come from one of two causes:

* global caches are too large
* per-connection buffers are too large for the current concurrency

### How MariaDB Uses Memory

MariaDB uses three broad kinds of memory:

* **Fixed global allocations**
  * engine caches such as [innodb\_buffer\_pool\_size](../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size), [key\_buffer\_size](../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size), and [aria\_pagecache\_buffer\_size](../server-usage/storage-engines/aria/aria-system-variables.md#aria_pagecache_buffer_size)
  * optional caches such as [query\_cache\_size](optimization-and-tuning/system-variables/server-system-variables.md#query_cache_size)
* **Dynamic global structures**
  * metadata and connection-related structures such as [table\_open\_cache](optimization-and-tuning/system-variables/server-system-variables.md#table_open_cache), [table\_definition\_cache](optimization-and-tuning/system-variables/server-system-variables.md#table_definition_cache), and [thread\_cache\_size](optimization-and-tuning/system-variables/server-system-variables.md#thread_cache_size)
  * limits such as [max\_connections](optimization-and-tuning/system-variables/server-system-variables.md#max_connections) do not allocate memory by themselves, but they raise the possible peak memory footprint
* **Per-connection and per-query allocations**
  * execution buffers such as [join\_buffer\_size](optimization-and-tuning/system-variables/server-system-variables.md#join_buffer_size), [mrr\_buffer\_size](optimization-and-tuning/system-variables/server-system-variables.md#mrr_buffer_size), [read\_buffer\_size](optimization-and-tuning/system-variables/server-system-variables.md#read_buffer_size), and [sort\_buffer\_size](optimization-and-tuning/system-variables/server-system-variables.md#sort_buffer_size)
  * temporary in-memory tables controlled by [max\_heap\_table\_size](optimization-and-tuning/system-variables/server-system-variables.md#max_heap_table_size) and [tmp\_memory\_table\_size](optimization-and-tuning/system-variables/server-system-variables.md#tmp_memory_table_size)
  * temporary blob storage and engine-specific work areas

{% hint style="warning" %}
On containers, cgroups, or managed environments, use the memory limit seen by MariaDB. Do not size caches against the physical RAM of the host.
{% endhint %}

{% stepper %}
{% step %}
### Confirm memory pressure

Check whether the host is swapping or being killed by the OOM killer.

On the MariaDB side, inspect overall memory use:

```sql
SHOW GLOBAL STATUS LIKE 'memory_used';
```

If the server is swapping, reduce major caches before tuning anything else.
{% endstep %}

{% step %}
### Review non-default variables

List variables that differ from the compiled defaults:

```sql
SELECT information_schema.system_variables.variable_name,
       information_schema.system_variables.default_value,
       information_schema.global_variables.variable_value
FROM information_schema.system_variables
JOIN information_schema.global_variables
  ON information_schema.system_variables.variable_name =
     information_schema.global_variables.variable_name
WHERE information_schema.system_variables.default_value <>
      information_schema.global_variables.variable_value
  AND information_schema.system_variables.default_value <> 0;
```

If the server is running out of memory, the cause is often in this list.
{% endstep %}

{% step %}
### Reduce the biggest consumers first

Start with the variables that move total memory the most:

* [innodb\_buffer\_pool\_size](../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size)
* [key\_buffer\_size](../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size)
* [aria\_pagecache\_buffer\_size](../server-usage/storage-engines/aria/aria-system-variables.md#aria_pagecache_buffer_size)
* [query\_cache\_size](optimization-and-tuning/system-variables/server-system-variables.md#query_cache_size)

Then review per-connection buffers, especially if concurrency is high:

* [join\_buffer\_size](optimization-and-tuning/system-variables/server-system-variables.md#join_buffer_size)
* [mrr\_buffer\_size](optimization-and-tuning/system-variables/server-system-variables.md#mrr_buffer_size)
* [sort\_buffer\_size](optimization-and-tuning/system-variables/server-system-variables.md#sort_buffer_size)
* [read\_buffer\_size](optimization-and-tuning/system-variables/server-system-variables.md#read_buffer_size)
* [max\_heap\_table\_size](optimization-and-tuning/system-variables/server-system-variables.md#max_heap_table_size)

Large per-connection buffers are safe only when few sessions use them at the same time.
{% endstep %}

{% step %}
### Re-test under real concurrency

After each change, recheck swapping, memory use, and query latency.

Avoid tuning many memory variables at once. Change the largest settings first, then re-measure.
{% endstep %}
{% endstepper %}

### What Is the Key Buffer?

[MyISAM](../server-usage/storage-engines/myisam-storage-engine/) does two different things for caching.

* Index blocks (1KB each, BTree structured, from .MYI file) live in the "key buffer".
* Data block caching (from .MYD file) is left to the OS, so be sure to leave a bunch of free space for this.\
  Caveat: Some flavors of OS always claim to be using over 90%, even when there is really lots of free space.

```sql
SHOW GLOBAL STATUS LIKE 'Key%';
```

then calculate [Key\_read\_requests](optimization-and-tuning/system-variables/server-status-variables.md#key_read_requests) / [Key\_reads](optimization-and-tuning/system-variables/server-status-variables.md#key_reads). If it is high (say, over 10), then the key buffer is big enough, otherwise you should adjust the [key\_buffer\_size](../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size) value.

### What Is the Buffer Pool?

InnoDB does all its caching in the [buffer pool](../server-usage/storage-engines/innodb/innodb-buffer-pool.md), whose size is controlled by [innodb\_buffer\_pool\_size](../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size). By default, it contains 16KB data and index blocks from the open tables (see [innodb\_page\_size](../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_page_size)), plus some maintenance overhead.

In current MariaDB releases, focus first on total buffer pool size. Older releases allowed multiple buffer pool instances, but [innodb\_buffer\_pool\_instances](../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_instances) is deprecated and ignored from [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.1).

### Another Algorithm

This will set the main cache settings to the minimum; it could be important to systems with lots of other processes and/or RAM is 2GB or smaller.

Do [SHOW TABLE STATUS](../reference/sql-statements/administrative-sql-statements/show/show-table-status.md) for all the tables in all the databases.

Add up Index\_length for all the MyISAM tables. Set [key\_buffer\_size](../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size) no larger than that size.

Add up Data\_length + Index\_length for all the InnoDB tables. Set [innodb\_buffer\_pool\_size](../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size) to no more than 110% of that total.

If that leads to swapping, cut both settings back. Suggest cutting them down proportionately.

Run this to see the values for your system. (If you have a lot of tables, it can take minute(s).)

```sql
SELECT  ENGINE,
        ROUND(SUM(data_length) /1024/1024, 1) AS "Data MB",
        ROUND(SUM(index_length)/1024/1024, 1) AS "Index MB",
        ROUND(SUM(data_length + index_length)/1024/1024, 1) AS "Total MB",
        COUNT(*) "Num Tables"
    FROM  INFORMATION_SCHEMA.TABLES
    WHERE  table_schema NOT IN (
             "information_schema", 
             "PERFORMANCE_SCHEMA", 
             "SYS_SCHEMA", 
             "ndbinfo")
    GROUP BY  ENGINE;
```

### Query Memory Allocation

There are two variables that dictate how memory is allocated while MariaDB parses and executes a query. [query\_prealloc\_size](optimization-and-tuning/system-variables/server-system-variables.md#query_prealloc_size) defines the standard buffer for query execution, and [query\_alloc\_block\_size](optimization-and-tuning/system-variables/server-system-variables.md#query_alloc_block_size) defines the size of extra memory blocks if `query_prealloc_size` is not large enough. Getting these variables right can reduce memory fragmentation in the server.

### Legacy and Specialized Scenarios

The sections below cover older platforms, specialized hardware, and edge cases. Use them only if they match your environment.

### Mutex Bottleneck

This is mostly a historical concern.

Older MySQL and MariaDB releases could hit mutex contention around a few shared structures:

* MyISAM's `key_buffer`
* The Query Cache
* InnoDB's `buffer_pool`

On current MariaDB releases, this is much less important than:

* sizing the buffer pool correctly
* avoiding unnecessary query cache usage
* fixing slow queries and bad indexes
* sizing connection concurrency realistically

### Legacy Platform Notes

These notes only apply to older or unusual deployments.

#### 32-Bit Operating Systems

On a 32-bit OS, MariaDB cannot effectively use large amounts of RAM.

* RAM above 4 GB is not usable by a 32-bit process.
* The operating system may impose a much lower per-process limit.
* Large cache settings can fail with out-of-memory errors even when the host still has free RAM.

Example: FreeBSD's `maxdsiz`, which defaults to 512MB.

```bash
$ ulimit -a
...
max memory size (kbytes, -m) 524288
```

If you must run MariaDB on a 32-bit platform, keep cache settings conservative.

If you get an error like `[ERROR] /usr/libexec/mysqld: Out of memory (Needed xxx bytes)`, it probably means that MySQL exceeded what the OS is willing to give it. Decrease the cache settings.

#### 64-Bit OS with 32-Bit MariaDB

The OS can use more than 4 GB, but the MariaDB process still cannot.

If you are in this configuration, upgrade MariaDB to 64-bit if possible.

Until then, keep cache sizes below the effective 32-bit process limit.

#### 64-Bit OS and MariaDB

This is the standard deployment target today.

Use the recommendations at the top of this page. They are more accurate than the old platform-specific rules of thumb.

max\_connections, thread\_stack\
Each "thread" takes some amount of RAM. This used to be about 200KB; 100 threads would be 20MB, not a significant size. If you have [max\_connections](optimization-and-tuning/system-variables/server-system-variables.md#max_connections) = 1000, then you are talking about 200MB, maybe more. Having that many connections probably implies other issues that should be addressed.

Thread pooling can change how concurrency behaves, but it does not remove the need to budget memory for peak active sessions.

Thread stack overruns are rare. If they occur, adjust `thread_stack` carefully and test.

### table\_open\_cache

The OS has some limit on the number of open files it will let a process have. Each table needs 1 to 3 open files. Each partition is effectively a table. Most operations on a partitioned table open _all_ partitions.

In Unix, ulimit tells you what the file limit is. The maximum value is in the tens of thousands, but sometimes it is set to only 1024. This limits you to about 300 tables. More discussion on ulimit

You can see how well your system is performing via [SHOW GLOBAL STATUS](../reference/sql-statements/administrative-sql-statements/show/show-status.md); and computing the opens/second via [Opened\_files](optimization-and-tuning/system-variables/server-status-variables.md#opened_files) / [Uptime](optimization-and-tuning/system-variables/server-status-variables.md#uptime) If this is more than, say, 5, [table\_open\_cache](optimization-and-tuning/system-variables/server-system-variables.md#table_open_cache) should be increased. If it is less than, say, 1, you might get improvement by decreasing [table\_open\_cache](optimization-and-tuning/system-variables/server-system-variables.md#table_open_cache).

[table\_open\_cache](optimization-and-tuning/system-variables/server-system-variables.md#table_open_cache) defaults to 2000.

### Query Cache

Short answer: set [query\_cache\_type](optimization-and-tuning/system-variables/server-system-variables.md#query_cache_type) to `OFF` and [query\_cache\_size](optimization-and-tuning/system-variables/server-system-variables.md#query_cache_size) to `0` unless measurements show a clear benefit.

The [query cache](optimization-and-tuning/buffers-caches-and-threads/query-cache.md) can be very fast for repeated identical `SELECT` statements, but it has significant trade-offs:

* every eligible `SELECT` must consult it
* a write to a table invalidates cached results for that table
* contention around the shared cache can hurt concurrency

If you decide to use it:

* keep [query\_cache\_size](optimization-and-tuning/system-variables/server-system-variables.md#query_cache_size) small, usually no more than `50M`
* prefer [query\_cache\_type](optimization-and-tuning/system-variables/server-system-variables.md#query_cache_type) = `DEMAND`
* use `SQL_CACHE` only on queries that benefit from reuse

To see whether it helps:

```sql
SHOW GLOBAL STATUS LIKE 'Qc%';
```

A rough read hit rate is:

* `Qcache_hits / Qcache_inserts`

If that ratio stays low, disable the query cache.

### thread\_cache\_size

In current MariaDB releases, [thread\_cache\_size](optimization-and-tuning/system-variables/server-system-variables.md#thread_cache_size) rarely needs manual tuning. Keep it small but non-zero unless you have evidence that connection creation is a bottleneck.

This setting controls how many disconnected threads are kept ready for reuse. It does not limit concurrent connections; [max\_connections](optimization-and-tuning/system-variables/server-system-variables.md#max_connections) does.

A very high value usually wastes memory without helping throughput.

### Binary Logs

If you enable [binary logging](../server-management/server-monitoring-logs/binary-log/) for replication or point-in-time recovery, logs will accumulate until they are purged.

Set a retention policy explicitly. On current MariaDB releases, prefer [binlog\_expire\_logs\_seconds](standard-replication/replication-and-binary-log-system-variables.md#binlog_expire_logs_seconds). Older setups may still use [expire\_logs\_days](standard-replication/replication-and-binary-log-system-variables.md#expire_logs_days).

Choose a retention period that matches your recovery and replication requirements.

### Swapping

Swapping usually hurts MariaDB badly.

For dedicated MariaDB hosts on Linux, a low `vm.swappiness` value often works best because it reduces the chance that large caches are pushed to disk under pressure.

In practice:

* avoid heavy swapping
* leave enough free RAM for the OS
* use a low `vm.swappiness` value if your platform and workload support it

Do not use this as a substitute for proper memory sizing.

### NUMA

NUMA can cause uneven memory allocation on multi-socket systems.

If you see swapping or memory imbalance on a NUMA host, check the platform configuration before changing MariaDB settings. In some environments, interleaving memory allocation can avoid one NUMA node filling early while others stay underused.

Possible mitigations include:

* BIOS or firmware memory interleaving
* OS-level NUMA configuration
* [innodb\_numa\_interleave](../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_numa_interleave) where supported

Only tune NUMA after you confirm it is part of the problem.

### Huge Pages

Huge pages can reduce page table overhead for large memory allocations.

For InnoDB-heavy systems with large buffer pools, explicit huge pages can help. Transparent huge pages are often less predictable and can hurt latency, so review your OS defaults and current MariaDB release behavior before changing anything.

If you use huge pages:

* size them to match the intended buffer pool usage
* validate startup and allocation behavior
* measure latency and throughput after enabling them

Do not enable huge pages blindly on small or memory-constrained systems.

### ENGINE=MEMORY

The [Memory Storage Engine](../server-usage/storage-engines/memory-storage-engine.md) is a little-used alternative to [MyISAM](../server-usage/storage-engines/myisam-storage-engine/) and [InnoDB](../server-usage/storage-engines/innodb/). The data is not persistent, so it has limited uses. The size of a MEMORY table is limited to [max\_heap\_table\_size](optimization-and-tuning/system-variables/server-system-variables.md#max_heap_table_size), which defaults to 16MB. I mention it in case you have changed the value to something huge; this would be stealing from other possible uses of RAM.

### How to Set Variables

In the text file my.cnf (my.ini on Windows), add or modify a line to say something like

[innodb\_buffer\_pool\_size](../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size) = 5G

That is, VARIABLE name, "=", and a value. Some abbreviations are allowed, such as M for million (1048576), G for billion.

For the server to see it, the settings must be in the "\[mysqld]" section of the file.

The settings in my.cnf or my.ini will not take effect until you restart the server.

Most settings can be changed on the live system by connecting as user root (or other user with SUPER privilege) and doing something like

```sql
SET @@global.key_buffer_size = 77000000;
```

Note: No M or G suffix is allowed here.

To see the setting a global variable, do something like this:

```sql
SHOW GLOBAL VARIABLES LIKE "key_buffer_size";
+-----------------+----------+
| Variable_name   | Value    |
+-----------------+----------+
| key_buffer_size | 76996608 |
+-----------------+----------+
```

Note that this particular setting was rounded down to some multiple that MariaDB liked.

You may want to do both (SET and modify my.cnf) in order to make the change immediately and have it so that the next restart (for whatever reason) will again get the value.

### Application Connection Pools

Application servers and web servers can create far more database connections than MariaDB can use efficiently.

* Size the application pool explicitly.
* Keep [max\_connections](optimization-and-tuning/system-variables/server-system-variables.md#max_connections) high enough for real traffic, but not so high that worst-case per-connection buffers can exhaust RAM.
* Prefer connection pooling over one-connection-per-request patterns.

### Tools

* MySQLTuner
* TUNING-PRIMER

These tools can help identify obvious configuration problems, but they often assume worst-case memory use.

One common warning looks like this:

Maximum possible memory usage: 31.3G (266% of installed RAM)

Treat that as an upper bound, not a prediction. It usually assumes all [max\_connections](optimization-and-tuning/system-variables/server-system-variables.md#max_connections) are active and all are using large per-query buffers at the same time.

Total fragmented tables: 23 This implies that OPTIMIZE TABLE _might_ help. I suggest it for tables with either a high percentage of "free space" (see SHOW TABLE STATUS) or where you know you run a lot of DELETE and/or UPDATE statements. Still, don't bother to OPTIMIZE too often. Once a month might suffice.

### See Also

* [Configuring MariaDB for Optimal Performance](../server-management/install-and-upgrade-mariadb/configuring-mariadb/mariadb-performance-advanced-configurations/configuring-mariadb-for-optimal-performance.md)
* [InnoDB Buffer Pool](../server-usage/storage-engines/innodb/innodb-buffer-pool.md)
* [Server System Variables](optimization-and-tuning/system-variables/server-system-variables.md)
* [What to Do if MariaDB Doesn't Start](../server-management/starting-and-stopping-mariadb/what-to-do-if-mariadb-doesnt-start.md)

### Attribution

Rick James wrote the original version of this page. [Rick James' site](https://mysql.rjweb.org/), original source: [random](https://mysql.rjweb.org/doc.php/random).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
