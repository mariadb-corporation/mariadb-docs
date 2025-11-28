---
description: >-
  Understand MariaDB Server memory allocation. This section explains how memory
  is managed, key configuration parameters, and strategies for optimizing memory
  usage for enhanced performance.
---

# MariaDB Memory Allocation

### Allocating RAM for MariaDB - The Short Answer

If only using [MyISAM](../server-usage/storage-engines/myisam-storage-engine/), set [key\_buffer\_size](../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size) to 20% of **available** RAM. (Plus [innodb\_buffer\_pool\_size](../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size) = 0)

If only using InnoDB, set [innodb\_buffer\_pool\_size](../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size) to 70% of **available** RAM. (Plus [key\_buffer\_size](../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size) = 10M, small, but not zero.)

Rule of thumb for tuning:

* Start with released copy of my.cnf / my.ini.
* Change [key\_buffer\_size](../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size) and [innodb\_buffer\_pool\_size](../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size) according to engine usage and RAM.
* Slow queries can usually be 'fixed' via indexes, schema changes, or SELECT changes, not by tuning.
* Don't get carried away with the [query cache](optimization-and-tuning/buffers-caches-and-threads/query-cache.md) until you understand what it can and cannot do.
* Don't change anything else unless you run into trouble (eg, max connections).
* Be sure the changes are under the \[mysqld] section, not some other section.

The 20%/70% assumes you have at least 4GB of RAM. If you have less total available RAM, then those percentages are too high and can lead to OOM events or swapping.

Now for the gory details.

### How to troubleshoot out-of-memory issues

If the MariaDB server is crashing because of 'out-of-memory' then it is probably wrongly configured.

There are two kinds of buffers in MariaDB:

* Global ones that are only allocated once during the lifetime of the server:
  * Storage engine buffers ( [innodb\_buffer\_pool\_size](../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size), [key\_buffer\_size](../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size), [aria\_pagecache\_buffer\_size](../server-usage/storage-engines/aria/aria-system-variables.md#aria_pagecache_buffer_size), etc)
  * Query cache [query\_cache\_size](optimization-and-tuning/system-variables/server-system-variables.md#query_cache_size).
* Global caches onces that grow and shrink dynamically on demand up to max limit:
  * [max\_user\_connections](optimization-and-tuning/system-variables/server-system-variables.md#max_user_connections)
  * [table\_open\_cache](optimization-and-tuning/system-variables/server-system-variables.md#table_open_cache)
  * [table\_definition\_cache](optimization-and-tuning/system-variables/server-system-variables.md#table_definition_cache)
  * [thread\_cache\_size](optimization-and-tuning/system-variables/server-system-variables.md#thread_cache_size)
* Local buffers that are allocated on demand whenever needed
  * Internal ones used during engine index creation\
    ([myisam\_sort\_buffer\_size](../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#myisam_sort_buffer_size), [aria\_sort\_buffer\_size).](../server-usage/storage-engines/aria/aria-system-variables.md#aria_sort_buffer_size)
  * Internal buffers for storing blobs.
    * Some storage engine will keep a temporary cache to store the largest blob seen so far when scanning a table. This will be freed at end of query. Note that temporary blob storage is not included in the memory information in [information\_schema.processlist](../reference/system-tables/information-schema/information-schema-tables/information-schema-processlist-table.md) but only in the total memory used (`show global status like "memory_used"`).
  * Buffers and caches used during query execution:

| Variable                                                                                                          | Description                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [join\_buffer\_size](optimization-and-tuning/system-variables/server-system-variables.md#join_buffer_size)        | Used when no keys can be used to find a row in next table                                                                                               |
| [mrr\_buffer\_size](optimization-and-tuning/system-variables/server-system-variables.md#mrr_buffer_size)          | Size of buffer to use when using multi-range read with range access                                                                                     |
| [net\_buffer\_length](optimization-and-tuning/system-variables/server-system-variables.md#net_buffer_length)      | Max size of network packet                                                                                                                              |
| [read\_buffer\_size](optimization-and-tuning/system-variables/server-system-variables.md#read_buffer_size)        | Used by some storage engines when doing bulk insert                                                                                                     |
| [sort\_buffer\_size](optimization-and-tuning/system-variables/server-system-variables.md#sort_buffer_size)        | When doing ORDER BY or GROUP BY                                                                                                                         |
| [max\_heap\_table\_size](optimization-and-tuning/system-variables/server-system-variables.md#max_heap_table_size) | Used to store temporary tables in memory. See [Optimizing memory tables](optimization-and-tuning/optimizing-data-structure/optimizing-memory-tables.md) |

If any variables in the last group is very large and you have a lot of simultaneous users that are executing queries that are using these buffers then you can run into trouble.

In a default MariaDB installation the default of most of the above variables are quite small to ensure that one does not run out of memory.

You can check which variables that have been changed in your setup by executing the following sql statement. If you are running into out-of-memory issues, it is very likely that the problematic variable is\
in this list!

```sql
SELECT information_schema.system_variables.variable_name,
information_schema.system_variables.default_value,
global_variables.variable_value FROM
information_schema.system_variables,information_schema.global_variables WHERE
system_variables.variable_name=global_variables.variable_name AND
system_variables.default_value <> global_variables.variable_value AND
system_variables.default_value <> 0
```

### What is the Key Buffer?

[MyISAM](../server-usage/storage-engines/myisam-storage-engine/) does two different things for caching.

* Index blocks (1KB each, BTree structured, from .MYI file) live in the "key buffer".
* Data block caching (from .MYD file) is left to the OS, so be sure to leave a bunch of free space for this.\
  Caveat: Some flavors of OS always claim to be using over 90%, even when there is really lots of free space.

```sql
SHOW GLOBAL STATUS LIKE 'Key%';
```

then calculate [Key\_read\_requests](optimization-and-tuning/system-variables/server-status-variables.md#key_read_requests) / [Key\_reads](optimization-and-tuning/system-variables/server-status-variables.md#key_reads). If it is high (say, over 10), then the key buffer is big enough, otherwise you should adjust the [key\_buffer\_size](../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size) value.

### What is the Buffer Pool?

InnoDB does all its caching in the [buffer pool](../server-usage/storage-engines/innodb/innodb-buffer-pool.md), whose size is controlled by [innodb\_buffer\_pool\_size](../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size). By default, it contains 16KB data and index blocks from the open tables (see [innodb\_page\_size](../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_page_size)), plus some maintenance overhead.

From [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5), multiple buffer pools are permitted; this can help because there is one mutex per pool, thereby relieving some of the mutex bottleneck.

[More on InnoDB tuning](https://www.mysqlperformanceblog.com/2007/11/01/innodb-performance-optimization-basics/)

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

There are two variables that dictates how memory is allocated by MariaDB while parsing and executing a query.[query\_prealloc\_size](optimization-and-tuning/system-variables/server-system-variables.md#query_prealloc_size) defines the standard buffer for memory used for query execution and [query\_alloc\_block\_size](optimization-and-tuning/system-variables/server-system-variables.md#query_alloc_block_size) that is size of memory blocks if `query_prealloc_size` was not big enough. Getting these variables right will reduce memory fragmentation in the server.

### Mutex Bottleneck

MySQL was designed in the days of single-CPU machines and designed to be easily ported to many different architectures. Unfortunately, that lead to some sloppiness in how to interlock actions. There are a small number (too small) of "mutexes" to gain access to several critical processes. Of note:

* MyISAM's key\_buffer
* The Query Cache
* InnoDB's buffer\_pool\
  With multi-core boxes, the mutex problem is causing performance problems. In general, past 4-8 cores, MySQL gets slower, not faster. MySQL 5.5 and Percona's XtraDB made that somewhat better in InnoDB; the practical limit for cores is more like 32, and performance tends plateaus after that rather than declining. 5.6 claims to scale up to about 48 cores.

### 32-bit OS and MariaDB

First, the OS (and the hardware?) may conspire to not let you use all 4GB, if that is what you have. If you have more than 4GB of RAM, the excess beyond 4GB is _totally_ inaccessable and unusable on a 32-bit OS.

Secondly, the OS probably has a limit on how much RAM it will allow any process to use.

Example: FreeBSD's maxdsiz, which defaults to 512MB.

Example:

```bash
$ ulimit -a
...
max memory size (kbytes, -m) 524288
```

So, once you have determined how much RAM is available to mysqld, then apply the 20%/70%, but round down some.

If you get an error like `[ERROR] /usr/libexec/mysqld: Out of memory (Needed xxx bytes)`, it probably means that MySQL exceeded what the OS is willing to give it. Decrease the cache settings.

### 64-bit OS with 32-bit MariaDB

The OS is not limited by 4GB, but MariaDB is. If you have at least 4GB of RAM, then maybe these would be good:

* [key\_buffer\_size](../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size) = 20% of _all_ of RAM, but not more than 3G
* [innodb\_buffer\_pool\_size](../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size) = 3G

You should probably upgrade MariaDB to 64-bit.

### 64-bit OS and MariaDB

MyISAM only: [key\_buffer\_size](../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size): Use about 20% of RAM. Set (in my.cnf / my.ini) [innodb\_buffer\_pool\_size](../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size) = 0.

InnoDB only: [innodb\_buffer\_pool\_size](../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size) = 70% of RAM. If you have lots of RAM and are using 5.5 (or later), then consider having multiple pools. Recommend 1-16 [innodb\_buffer\_pool\_instances](../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_instances), such that each one is no smaller than 1GB. (Sorry, no metric on how much this will help; probably not a lot.)

Meanwhile, set [key\_buffer\_size](../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size) = 20M (tiny, but non-zero)

If you have a mixture of engines, lower both numbers.

max\_connections, thread\_stack\
Each "thread" takes some amount of RAM. This used to be about 200KB; 100 threads would be 20MB, not a significant size. If you have [max\_connections](optimization-and-tuning/system-variables/server-system-variables.md#max_connections) = 1000, then you are talking about 200MB, maybe more. Having that many connections probably implies other issues that should be addressed.

In 5.6 (or [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)), optional thread pooling interacts with [max\_connections](optimization-and-tuning/system-variables/server-system-variables.md#max_connections). This is a more advanced topic.

Thread stack overrun rarely happens. If it does, do something like thread\_stack=256K. [More on max\_connections, wait\_timeout, connection pooling, etc](https://www.mysqlperformanceblog.com/2013/11/28/mysql-error-too-many-connections/)

### table\_open\_cache

(In older versions this was called table\_cache)

The OS has some limit on the number of open files it will let a process have. Each table needs 1 to 3 open files. Each PARTITION is effectively a table. Most operations on a partitioned table open _all_ partitions.

In \*nix, ulimit tells you what the file limit is. The maximum value is in the tens of thousands, but sometimes it is set to only 1024. This limits you to about 300 tables. More discussion on ulimit

(This paragraph is in disputed.) On the other side, the table cache is (was) inefficiently implemented -- lookups were done with a linear scan. Hence, setting table\_cache in the thousands could actually slow down mysql. (Benchmarks have shown this.)

You can see how well your system is performing via [SHOW GLOBAL STATUS](../reference/sql-statements/administrative-sql-statements/show/show-status.md); and computing the opens/second via [Opened\_files](optimization-and-tuning/system-variables/server-status-variables.md#opened_files) / [Uptime](optimization-and-tuning/system-variables/server-status-variables.md#uptime) If this is more than, say, 5, [table\_open\_cache](optimization-and-tuning/system-variables/server-system-variables.md#table_open_cache) should be increased. If it is less than, say, 1, you might get improvement by decreasing [table\_open\_cache](optimization-and-tuning/system-variables/server-system-variables.md#table_open_cache).

From [MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/changes-improvements-in-mariadb-10-1), [table\_open\_cache](optimization-and-tuning/system-variables/server-system-variables.md#table_open_cache) defaults to 2000.

### Query Cache

Short answer: [query\_cache\_type](optimization-and-tuning/system-variables/server-system-variables.md#query_cache_type) = OFF and [query\_cache\_size](optimization-and-tuning/system-variables/server-system-variables.md#query_cache_size) = 0

The [Query Cache](optimization-and-tuning/buffers-caches-and-threads/query-cache.md) (QC) is effectively a hash mapping SELECT statements to resultsets.

Long answer... There are many aspects of the "Query cache"; many are negative.

* Novice Alert! The QC is totally unrelated to the key\_buffer and buffer\_pool.
* When it is useful, the QC is blazingly fast. It would not be hard to create a benchmark that runs 1000x faster.
* There is a single mutex controlling the QC.
* The QC, unless it is OFF & 0, is consulted for _every_ SELECT.
* Yes, the mutex is hit even if [query\_cache\_type](optimization-and-tuning/system-variables/server-system-variables.md#query_cache_type) = DEMAND (2).
* Any change to a query (even adding a space) leads (potentially) to a different entry in the QC.
* If my.cnf says type=ON and you later turn it OFF, it is not fully OFF. Ref: [bug.php?id=60696](https://bugs.mysql.com/bug.php?id=60696)

"Pruning" is costly and frequent:

* When _any_ write happens on a table, _all_ entries in the QC for _that_ table are removed.
* It happens even on a read-only Slave.
* Purges are performed with a linear algorithm, so a large QC (even 200MB) can be noticeably slow.

To see how well your QC is performing, SHOW GLOBAL STATUS LIKE 'Qc%'; then compute the read hit rate: [Qcache\_hits](optimization-and-tuning/system-variables/server-status-variables.md#qcache_hits) / [Qcache\_inserts](optimization-and-tuning/system-variables/server-status-variables.md#qcache_inserts) If it is over, say, 5, the QC might be worth keeping.

If you decide the QC is right for you, then I recommend

* [query\_cache\_size](optimization-and-tuning/system-variables/server-system-variables.md#query_cache_size) = no more than 50M
* [query\_cache\_type](optimization-and-tuning/system-variables/server-system-variables.md#query_cache_type) = DEMAND
* [SQL\_CACHE or SQL\_NO\_CACHE](optimization-and-tuning/buffers-caches-and-threads/query-cache.md#sql_no_cache-and-sql_cache) in all SELECTs, based on which queries are likely to benefit from caching.
* [Why to turn off the QC](https://dba.stackexchange.com/a/136814/1876)
* [Discussion about size](https://haydenjames.io/mysql-query-cache-size-performance/)

### thread\_cache\_size

It is not necessary to tune [thread\_cache\_size](optimization-and-tuning/system-variables/server-system-variables.md#thread_cache_size) from [MariaD](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) Previously, it was minor tunable variable. Zero will slow down thread (connection) creation. A small (say, 10), non-zero number is good. The setting has essentially no impact on RAM usage.

It is the number of extra processes to hang onto. It does not restrict the number of threads; [max\_connections](optimization-and-tuning/system-variables/server-system-variables.md#max_connections) does.

### Binary Logs

If you have turned on [binary logging](../server-management/server-monitoring-logs/binary-log/) (via [log\_bin](standard-replication/replication-and-binary-log-system-variables.md#log_bin)) for replication and/or point-in-time recovery, the system will create binary logs forever. That is, they can slowly fill up the disk. Suggest setting [expire\_logs\_days](standard-replication/replication-and-binary-log-system-variables.md#expire_logs_days) = 14 to keep only 14 days' worth of logs.

### Swappiness

RHEL, in its infinite wisdom, decided to let you control how aggressively the OS will pre-emptively swap RAM. This is good in general, but lousy for MariaDB.

MariaDB would love for RAM allocations to be reasonably stable -- the caches are (mostly) pre-allocated; the threads, etc, are (mostly) of limited scope. ANY swapping is likely to severely hurt performance of MariaDB.

With a high value for swappiness, you lose some RAM because the OS is trying to keep a lot of space free for future allocations (that MySQL is not likely to need).

With swappiness = 0, the OS will probably crash rather than swap. I would rather have MariaDB limping than die. The latest recommendation is swappiness = 1. (2015)

[More confirmation](https://www.mysqlperformanceblog.com/2014/04/28/oom-relation-vm-swappiness0-new-kernel/)

Somewhere in between (say, 5?) might be a good value for a MariaDB-only server.

### NUMA

OK, it's time to complicate the architecture of how a CPU talks to RAM. NUMA (Non-Uniform Memory Access) enters the picture. Each CPU (or maybe socket with several cores) has a part of the RAM hanging off each. This leads to memory access being faster for local RAM, but slower (tens of cycles slower) for RAM hanging off other CPUs.

Then the OS enters the picture. In at least one case (RHEL?), two things seem to be done:

* OS allocations are pinned to the 'first' CPU's RAM.]
* Other allocations go by default to the first CPU until it is full.

Now for the problem.

* The OS and MariaDB have allocated all the 'first' RAM.
* MariaDB has allocated some of the second RAM.
* The OS needs to allocate something.\
  Ouch -- it is out of room in the one CPU where it is willing to allocate its stuff, so it swaps out some of MariaDB. Bad.

dmesg | grep -i numa

Probable solution: Configure the BIOS to "interleave" the RAM allocations. This should prevent the premature swapping, at the cost of off-CPU RAM accesses half the time. Well, you have the costly accesses anyway, since you really want to use all of RAM. Older MySQL versions: numactl --interleave=all. Or: [innodb\_numa\_interleave](../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_numa_interleave)=1

Another possible solution: Turn numa off (if the OS has a way of doing that)

Overall performance loss/gain: A few percent.

### Huge Pages

[MariaDB 10.6.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/10.6.17) (and other releases after 19 Jan 2024) have transparent huge pages automatically disabled. See [MDEV-33279](https://jira.mariadb.org/browse/MDEV-33279) "Disable transparent huge pages after page buffers has been allocated" for more information.

This is another hardware performance gimmick.

For a CPU to access RAM, especially mapping a 64-bit address to somewhere in, say, 128GB or 'real' RAM, the TLB is used. (TLB = Translation Lookup Buffer.) Think of the TLB as a hardware associative memory lookup table; given a 64-bit virtual address, what is the real address.

Because it is an associative memory of finite size, sometimes there will be "misses" that require reaching into real RAM to resolve the lookup. This is costly, so should be avoided.

Normally, RAM is 'paged' in 4KB pieces; the TLB actually maps the top (64-12) bits into a specific page. Then the bottom 12 bits of the virtual address are carried over intact.

For example, 128GB of RAM broken 4KB pages means 32M page-table entries. This is a lot, and probably far exceeds the capacity of the TLB. So, enter the "Huge page" trick.

With the help of both the hardware and the OS, it is possible to have some of RAM in huge pages, of say 4MB (instead of 4KB). This leads to far fewer TLB entries, but it means the unit of paging is 4MB for such parts of RAM. Hence, huge pages tend to be non-pagable.

Now RAM is broken into pagable and non pagable parts; what parts can reasonably be non pagable? In MariaDB, the [Innodb Buffer Pool](../server-usage/storage-engines/innodb/innodb-buffer-pool.md) is a perfect candidate. So, by correctly configuring these, InnoDB can run a little faster:

* Huge pages enabled
* Tell the OS to allocate the right amount (namely to match the buffer\_pool)
* Tell MariaDB to use huge pages
* [innodb memory usage vs swap](https://forums.mysql.com/read.php?22,384707,385002)

That thread has more details on what to look for and what to set.

Overall performance gain: A few percent. Yawn. Too much hassle for too little benefit.

Jumbo Pages? Turn off.

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

To see the setting a global VARIABLE do something like

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

### Web Server

A web server like Apache runs multiple threads. If each thread opens a connection to MariaDB, you could run out of connections. Make sure MaxClients (or equivalent) is set to some civilized number (under 50).

### Tools

* MySQLTuner
* TUNING-PRIMER

There are several tools that advise on memory. One misleading entry they come up with

Maximum possible memory usage: 31.3G (266% of installed RAM)

Don't let it scare you -- the formulas used are excessively conservative. They assume all of [max\_connections](optimization-and-tuning/system-variables/server-system-variables.md#max_connections) are in use and active and doing something memory intensive.

Total fragmented tables: 23 This implies that OPTIMIZE TABLE _might_ help. I suggest it for tables with either a high percentage of "free space" (see SHOW TABLE STATUS) or where you know you do a lot of DELETEs and/or UPDATEs. Still, don't bother to OPTIMIZE too often. Once a month might suffice.

### MySQL 5.7

5.7 stores a lot more information in RAM, leading to the footprint being perhaps half a GB more than 5.6. See [Memory increase in 5.7](https://blogs.oracle.com/svetasmirnova/entry/memory_summary_tables_in_performance).

### Postlog

Created 2010; Refreshed Oct, 2012, Jan, 2014

The tips in this document apply to MySQL, MariaDB, and Percona.

### See Also

* [Configuring MariaDB for Optimal Performance](../server-management/install-and-upgrade-mariadb/configuring-mariadb/mariadb-performance-advanced-configurations/configuring-mariadb-for-optimal-performance.md)
* More in-depth: Tocker's tuning for 5.6
* Irfan's InnoDB performance optimization basics (redux)
* 10 MySQL settings to tune after installation
* Magento
* Peter Zaitsev's take on such (5/2016)

Rick James graciously allowed us to use this article in the documentation.

[Rick James' site](https://mysql.rjweb.org/) has other useful tips, how-tos, optimizations, and debugging tips.

Original source: [random](https://mysql.rjweb.org/doc.php/random)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
