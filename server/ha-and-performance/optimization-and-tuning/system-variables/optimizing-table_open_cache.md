# Optimizing table\_open\_cache

[_table\_open\_cache_](server-system-variables.md#table_open_cache) can be a useful variable to adjust to improve performance.

Each concurrent session accessing the same table does so independently. This improves performance, although it comes at a cost of extra memory usage.

_table\_open\_cache_ indicates the maximum number of tables the server can keep open in any one table cache instance. Ideally, you'd like this set so as to re-open a table as infrequently as possible.

However, note that this is not a hard limit. When the server needs to open a table, it evicts the least recently used closed table from the cache, and adds the new table. If all tables are used, the server adds the new table and does not evict any table. As soon as a table is not used anymore, it will be evicted from the list even if no table needs to be open, until the number of open tables will be equal to _table\_open\_cache_

_table\_open\_cache_ has defaulted to 2000 since [MariaDB 10.1.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.7). Before that, the default was 400.

You can view the current setting in the my.cnf file, or by running:

```sql
SELECT @@table_open_cache;
+--------------------+
| @@table_open_cache |
+--------------------+
|                400 |
+--------------------+
```

To evaluate whether you could do with a higher table\_open\_cache, look at the number of opened tables, in conjunction with the server uptime ([Opened\_tables](server-status-variables.md#opened_tables) and [Uptime](server-status-variables.md#uptime) status variables):

```sql
SHOW global status LIKE 'opened_tables';
+---------------+--------+
| Variable_name | Value  |
+---------------+--------+
| Opened_tables | 354858 |
+---------------+--------+
```

If the number of opened tables is increasing rapidly, you should look at increasing the table\_open\_cache value. Try to find a value that sees a slow, or possibly even no, increase in the number of opened tables.

Make sure that your operating system can cope with the number of open file descriptors required by the table\_open\_cache setting. If table\_open\_cache is set too high, MariaDB may start to refuse connections as the operating system runs out of file descriptors. Also note that the MyISAM (and Aria?) storage engines need two file descriptors per open table.

It's possible that the open\_table\_cache can even be reduced.

If your number of open\_tables has not yet reached the table\_open\_cache\_size, and the server has been up a while, you can look at decreasing the value.

```sql
SHOW global status LIKE 'open_tables';
+---------------+-------+
| Variable_name | Value |
+---------------+-------+
| Open_tables   | 354   |
+---------------+-------+
```

The open table cache can be emptied with [FLUSH TABLES](../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) or with the `flush-tables` or `refresh` [mariadb-admin](../../../clients-and-utilities/administrative-tools/mariadb-admin.md) commands.

## Automatic Creation of New Table Open Cache Instances

MariaDB Server can create multiple instances of the table open cache. It initially creates just a single instance. However, whenever it detects contention on the existing instances, it will automatically create a new instance. When the number of instances has been increased due to contention, it does not decrease again.

When MariaDB Server creates a new instance, it prints a message like the following to the [error log](../../../server-management/server-monitoring-logs/error-log.md):

```
[Note] Detected table cache mutex contention at instance 1: 25% waits. Additional 
  table cache instance activated. Number of instances after activation: 2.
```

The maximum number of instances is defined by the [table\_open\_cache\_instances](server-system-variables.md#table_open_cache_instances) system variable. The default value of the [table\_open\_cache\_instances](server-system-variables.md#table_open_cache_instances) system variable is `8`, which is expected to handle up to 100 CPU cores. If your system is larger than this, then you may benefit from increasing the value of this system variable.

Depending on the ratio of actual available file handles, and [table\_open\_cache](server-system-variables.md#table_open_cache) size, the max. instance count may be auto adjusted to a lower value on server startup.

The implementation and behavior of this feature is different than the same feature in MySQL 5.6.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
