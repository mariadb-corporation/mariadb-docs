---
description: >-
  Acquire a named user-level lock. This function attempts to obtain a lock with
  a specified name and timeout, returning 1 on success or 0 on timeout.
---

# GET\_LOCK

## Syntax

```sql
GET_LOCK(str,timeout)
```

## Description

Tries to obtain a lock with a name given by the string `str`, using a timeout of `timeout` seconds. Returns `1` if the lock was obtained successfully, `0` if the attempt timed out (for example, because another client has previously locked the name), or `NULL` if an error occurred (such as running out of memory or the thread was killed with [mariadb-admin kill](../../../../clients-and-utilities/administrative-tools/mariadb-admin.md#mariadb-admin-commands)).

A lock is released with [RELEASE\_LOCK()](release_lock.md), when the connection terminates (either normally or abnormally). A connection can hold multiple locks at the same time, so a lock that is no longer needed needs to be explicitly released.

The [IS\_FREE\_LOCK](is_free_lock.md) function returns whether a specified lock is free or not, and the [IS\_USED\_LOCK](is_used_lock.md) whether the function is in use or not.

Locks obtained with `GET_LOCK()` do not interact with transactions. That is, committing a transaction does not release any such locks obtained during the transaction.

It is also possible to recursively set the same lock. If a lock with the same name is set `n` times, it needs to be released `n` times as well.

`str` is case insensitive for `GET_LOCK()` and related functions. If `str` is an empty string or `NULL`, `GET_LOCK()` returns `NULL` and does nothing. `timeout` supports microseconds.

If the [metadata\_lock\_info](../../../plugins/other-plugins/metadata-lock-info-plugin.md) plugin is installed, locks acquired with this function are visible in the [Information Schema](../../../system-tables/information-schema/) [METADATA\_LOCK\_INFO](../../../system-tables/information-schema/information-schema-tables/information-schema-metadata_lock_info-table.md) table.

This function can be used to implement application locks or to simulate record locks. Names are locked on a server-wide basis. If a name has been locked by one client, `GET_LOCK()` blocks any request by another client for a lock with the same name. This allows clients that agree on a given lock name to use the name to perform cooperative advisory locking. But be aware that it also allows a client that is not among the set of cooperating clients to lock a name, either inadvertently or deliberately, and thus prevent any of the cooperating clients from locking that name. One way to reduce the likelihood of this is to use lock names that are database-specific or application-specific. For example, use lock names of the form `db_name.str` or `app_name.str`.

Statements using the `GET_LOCK` function are [not safe for statement-based replication](../../../../ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication.md).

The patch to permit multiple locks was [contributed by Konstantin "Kostja" Osipov](https://kostja-osipov.livejournal.com/46410.html) ([MDEV-3917](https://jira.mariadb.org/browse/MDEV-3917)).

## Examples

```sql
SELECT GET_LOCK('lock1',10);
+----------------------+
| GET_LOCK('lock1',10) |
+----------------------+
|                    1 |
+----------------------+

SELECT IS_FREE_LOCK('lock1'), IS_USED_LOCK('lock1');
+-----------------------+-----------------------+
| IS_FREE_LOCK('lock1') | IS_USED_LOCK('lock1') |
+-----------------------+-----------------------+
|                     0 |                    46 |
+-----------------------+-----------------------+

SELECT IS_FREE_LOCK('lock2'), IS_USED_LOCK('lock2');
+-----------------------+-----------------------+
| IS_FREE_LOCK('lock2') | IS_USED_LOCK('lock2') |
+-----------------------+-----------------------+
|                     1 |                  NULL |
+-----------------------+-----------------------+
```

Multiple locks can be held:

```sql
SELECT GET_LOCK('lock2',10);
+----------------------+
| GET_LOCK('lock2',10) |
+----------------------+
|                    1 |
+----------------------+

SELECT IS_FREE_LOCK('lock1'), IS_FREE_LOCK('lock2');
+-----------------------+-----------------------+
| IS_FREE_LOCK('lock1') | IS_FREE_LOCK('lock2') |
+-----------------------+-----------------------+
|                     0 |                     0 |
+-----------------------+-----------------------+

SELECT RELEASE_LOCK('lock1'), RELEASE_LOCK('lock2');
+-----------------------+-----------------------+
| RELEASE_LOCK('lock1') | RELEASE_LOCK('lock2') |
+-----------------------+-----------------------+
|                     1 |                     1 |
+-----------------------+-----------------------+
```

It is possible to hold the same lock recursively. This example is viewed using the [metadata\_lock\_info](../../../plugins/other-plugins/metadata-lock-info-plugin.md) plugin:

```sql
SELECT GET_LOCK('lock3',10);
+----------------------+
| GET_LOCK('lock3',10) |
+----------------------+
|                    1 |
+----------------------+

SELECT GET_LOCK('lock3',10);
+----------------------+
| GET_LOCK('lock3',10) |
+----------------------+
|                    1 |
+----------------------+

SELECT * FROM INFORMATION_SCHEMA.METADATA_LOCK_INFO;
+-----------+---------------------+---------------+-----------+--------------+------------+
| THREAD_ID | LOCK_MODE           | LOCK_DURATION | LOCK_TYPE | TABLE_SCHEMA | TABLE_NAME |
+-----------+---------------------+---------------+-----------+--------------+------------+
|        46 | MDL_SHARED_NO_WRITE | NULL          | User lock | lock3        |            |
+-----------+---------------------+---------------+-----------+--------------+------------+

SELECT RELEASE_LOCK('lock3');
+-----------------------+
| RELEASE_LOCK('lock3') |
+-----------------------+
|                     1 |
+-----------------------+

SELECT * FROM INFORMATION_SCHEMA.METADATA_LOCK_INFO;
+-----------+---------------------+---------------+-----------+--------------+------------+
| THREAD_ID | LOCK_MODE           | LOCK_DURATION | LOCK_TYPE | TABLE_SCHEMA | TABLE_NAME |
+-----------+---------------------+---------------+-----------+--------------+------------+
|        46 | MDL_SHARED_NO_WRITE | NULL          | User lock | lock3        |            |
+-----------+---------------------+---------------+-----------+--------------+------------+

SELECT RELEASE_LOCK('lock3');
+-----------------------+
| RELEASE_LOCK('lock3') |
+-----------------------+
|                     1 |
+-----------------------+

SELECT * FROM INFORMATION_SCHEMA.METADATA_LOCK_INFO;
Empty set (0.000 sec)
```

Timeout example: Connection 1:

```sql
SELECT GET_LOCK('lock4',10);
+----------------------+
| GET_LOCK('lock4',10) |
+----------------------+
|                    1 |
+----------------------+
```

Connection 2:

```sql
SELECT GET_LOCK('lock4',10);
```

After 10 seconds...

```sql
+----------------------+
| GET_LOCK('lock4',10) |
+----------------------+
|                    0 |
+----------------------+
```

Deadlocks are automatically detected and resolved. Connection 1:

```sql
SELECT GET_LOCK('lock5',10); 
+----------------------+
| GET_LOCK('lock5',10) |
+----------------------+
|                    1 |
+----------------------+
```

Connection 2:

```sql
SELECT GET_LOCK('lock6',10);
+----------------------+
| GET_LOCK('lock6',10) |
+----------------------+
|                    1 |
+----------------------+
```

Connection 1:

```sql
SELECT GET_LOCK('lock6',10); 
+----------------------+
| GET_LOCK('lock6',10) |
+----------------------+
|                    0 |
+----------------------+
```

Connection 2:

```sql
SELECT GET_LOCK('lock5',10);
ERROR 1213 (40001): Deadlock found when trying to get lock; try restarting transaction
```

## See Also

* [RELEASE\_LOCK](release_lock.md)
* [IS\_FREE\_LOCK](is_free_lock.md)
* [IS\_USED\_LOCK](is_used_lock.md)
* [RELEASE\_ALL\_LOCKS](release_all_locks.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
