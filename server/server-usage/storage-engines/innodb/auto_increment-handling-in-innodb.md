---
description: >-
  This page explains how InnoDB manages AUTO_INCREMENT columns, including
  initialization behavior, gap handling, and potential restart effects.
---

# AUTO\_INCREMENT Handling in InnoDB

## AUTO\_INCREMENT Lock Modes

The [innodb\_autoinc\_lock\_mode](innodb-system-variables.md#innodb_autoinc_lock_mode) system variable determines the lock mode when generating [AUTO\_INCREMENT](../../../reference/data-types/auto_increment.md) values for [InnoDB](./) tables. These modes allow [InnoDB](./) to make significant performance optimizations in certain circumstances.

The [innodb\_autoinc\_lock\_mode](innodb-system-variables.md#innodb_autoinc_lock_mode) system variable may be removed in a future release. See [MDEV-19577](https://jira.mariadb.org/browse/MDEV-19577) for more information.

### Traditional Lock Mode

When [innodb\_autoinc\_lock\_mode](innodb-system-variables.md#innodb_autoinc_lock_mode) is set to `0`, [InnoDB](./) uses the traditional lock mode.

In this mode, [InnoDB](./) holds a table-level lock for all [INSERT](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statements until the statement completes.

### Consecutive Lock Mode

When [innodb\_autoinc\_lock\_mode](innodb-system-variables.md#innodb_autoinc_lock_mode) is set to `1`, [InnoDB](./) uses the consecutive lock mode.

In this mode, [InnoDB](./) holds a table-level lock for all bulk [INSERT](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statements (such as [LOAD DATA](../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) or [INSERT ... SELECT](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-select.md)) until the end of the statement. For simple [INSERT](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statements, no table-level lock is held. Instead, a lightweight mutex is used which scales significantly better. This is the default setting.

### Interleaved Lock Mode

When [innodb\_autoinc\_lock\_mode](innodb-system-variables.md#innodb_autoinc_lock_mode) is set to `2`, [InnoDB](./) uses the interleaved lock mode.

In this mode, [InnoDB](./) does not hold any table-level locks at all. This is the fastest and most scalable mode, but is not safe for [statement-based](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based) replication.

## Setting AUTO\_INCREMENT Values

The [AUTO\_INCREMENT](../../../reference/data-types/auto_increment.md) value for an [InnoDB](./) table can be set for a table by executing the [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/) statement and specifying the [AUTO\_INCREMENT](../../../reference/sql-statements/data-definition/create/create-table.md#auto_increment) table option:

```
ALTER TABLE tab AUTO_INCREMENT=100;
```

However, in [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.3) and before, [InnoDB](./) stores the table's [AUTO\_INCREMENT](../../../reference/data-types/auto_increment.md) counter in memory. In these versions, when the server restarts, the counter is re-initialized to the highest value found in the table. This means that the above operation can be undone if the server is restarted before any rows are written to the table.

In [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.2/10.2.4) and later, the [AUTO\_INCREMENT](../../../reference/data-types/auto_increment.md) counter is persistent, so this restriction is no longer present. Persistent, however, does not mean transactional. Gaps may still occur in some cases, such as if a [INSERT IGNORE](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-ignore.md) statement fails, or if a user executes [ROLLBACK](../../../reference/sql-statements/transactions/rollback.md) or [ROLLBACK TO SAVEPOINT](../../../reference/sql-statements/transactions/savepoint.md).

For example:

```sql
CREATE TABLE t1 (pk INT AUTO_INCREMENT PRIMARY KEY, i INT, UNIQUE (i)) ENGINE=InnoDB;

INSERT INTO t1 (i) VALUES (1),(2),(3);
INSERT IGNORE INTO t1 (pk, i) VALUES (100,1);
Query OK, 0 rows affected, 1 warning (0.099 sec)

SELECT * FROM t1;
+----+------+
| pk | i    |
+----+------+
|  1 |    1 |
|  2 |    2 |
|  3 |    3 |
+----+------+

SHOW CREATE TABLE t1\G
*************************** 1. row ***************************
       Table: t1
Create Table: CREATE TABLE `t1` (
  `pk` int(11) NOT NULL AUTO_INCREMENT,
  `i` int(11) DEFAULT NULL,
  PRIMARY KEY (`pk`),
  UNIQUE KEY `i` (`i`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1
```

If the server is restarted at this point, then the [AUTO\_INCREMENT](../../../reference/data-types/auto_increment.md) counter will revert to `101`, which is the persistent value set as part of the failed [INSERT IGNORE](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert-ignore.md).

```sql
# Restart server
SHOW CREATE TABLE t1\G
*************************** 1. row ***************************
       Table: t1
Create Table: CREATE TABLE `t1` (
  `pk` int(11) NOT NULL AUTO_INCREMENT,
  `i` int(11) DEFAULT NULL,
  PRIMARY KEY (`pk`),
  UNIQUE KEY `i` (`i`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=latin1
```

## See Also

* [AUTO\_INCREMENT](../../../reference/data-types/auto_increment.md)
* [AUTO\_INCREMENT FAQ](../../../reference/data-types/auto_increment-faq.md)
* [LAST\_INSERT\_ID](../../../reference/sql-functions/secondary-functions/information-functions/last_insert_id.md)
* [Sequences](../../../reference/sql-structure/sequences/) - an alternative to auto\_increment available from [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
