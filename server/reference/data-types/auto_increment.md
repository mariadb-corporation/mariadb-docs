# AUTO\_INCREMENT

## Description

The `AUTO_INCREMENT` attribute can be used to generate a unique identity for new rows. When you insert a new record to the table (or upon adding an [AUTO\_INCREMENT](auto_increment.md) attribute with the [ALTER TABLE](../sql-statements/data-definition/alter/alter-table.md) statement), and the auto\_increment field is [NULL](null-values.md) or DEFAULT (in the case of an INSERT), the value will automatically be incremented. This also applies to 0, unless the [NO\_AUTO\_VALUE\_ON\_ZERO SQL\_MODE](../../server-management/variables-and-modes/sql-mode.md#no_auto_value_on_zero) is enabled.

`AUTO_INCREMENT` columns start from 1 by default. The automatically generated value can never be lower than 0.

Each table can have only one `AUTO_INCREMENT` column. It must defined as a key (not necessarily the `PRIMARY KEY` or `UNIQUE` key). In some storage engines (including the default [InnoDB](../../server-usage/storage-engines/innodb/)), if the key consists of multiple columns, the `AUTO_INCREMENT` column must be the first column. Storage engines that permit the column to be placed elsewhere are [Aria](../../server-usage/storage-engines/aria/), [MyISAM](../../server-usage/storage-engines/myisam-storage-engine/), [MERGE](../../server-usage/storage-engines/merge.md), [Spider](../../server-usage/storage-engines/spider/), [TokuDB](../../server-usage/storage-engines/tokudb/), [BLACKHOLE](../../server-usage/storage-engines/blackhole.md), [FederatedX](../../server-usage/storage-engines/federatedx-storage-engine/) and [Federated](../../server-usage/storage-engines/legacy-storage-engines/federated-storage-engine.md).

```
CREATE TABLE animals (
     id MEDIUMINT NOT NULL AUTO_INCREMENT,
     name CHAR(30) NOT NULL,
     PRIMARY KEY (id)
 );

INSERT INTO animals (name) VALUES
    ('dog'),('cat'),('penguin'),
    ('fox'),('whale'),('ostrich');
```

```
SELECT * FROM animals;
+----+---------+
| id | name    |
+----+---------+
|  1 | dog     |
|  2 | cat     |
|  3 | penguin |
|  4 | fox     |
|  5 | whale   |
|  6 | ostrich |
+----+---------+
```

`SERIAL` is an alias for `BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE`.

```
CREATE TABLE t (id SERIAL, c CHAR(1)) ENGINE=InnoDB;

SHOW CREATE TABLE t \G
*************************** 1. row ***************************
       Table: t
Create Table: CREATE TABLE `t` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `c` char(1) DEFAULT NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

## Setting or Changing the Auto\_Increment Value

You can use an [ALTER TABLE](../sql-statements/data-definition/alter/alter-table.md) statement to assign a new value to the `auto_increment` table option, or set the [insert\_id](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#insert_id) server system variable to change the next `AUTO_INCREMENT` value inserted by the current session.

[LAST\_INSERT\_ID()](../sql-functions/secondary-functions/information-functions/last_insert_id.md) can be used to see the last `AUTO_INCREMENT` value inserted by the current session.

```
ALTER TABLE animals AUTO_INCREMENT=8;

INSERT INTO animals (name) VALUES ('aardvark');

SELECT * FROM animals;
+----+-----------+
| id | name      |
+----+-----------+
|  1 | dog       |
|  2 | cat       |
|  3 | penguin   |
|  4 | fox       |
|  5 | whale     |
|  6 | ostrich   |
|  8 | aardvark  |
+----+-----------+

SET insert_id=12;

INSERT INTO animals (name) VALUES ('gorilla');

SELECT * FROM animals;
+----+-----------+
| id | name      |
+----+-----------+
|  1 | dog       |
|  2 | cat       |
|  3 | penguin   |
|  4 | fox       |
|  5 | whale     |
|  6 | ostrich   |
|  8 | aardvark  |
| 12 | gorilla   |
+----+-----------+
```

## InnoDB

AUTO\_INCREMENT is persistent in InnoDB. Prior to [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1023-release-notes), InnoDB used an auto-increment counter that was stored in memory. When the server restarted, the counter was re-initialized to the highest value used in the table, which canceled the effects of any AUTO\_INCREMENT = N option in the table statements).

See also [AUTO\_INCREMENT Handling in InnoDB](../../server-usage/storage-engines/innodb/auto_increment-handling-in-innodb.md).

## Setting Explicit Values

It is possible to specify a value for an `AUTO_INCREMENT` column. If the key is primary or unique, the value must not already exist in the key.

If the new value is higher than the current maximum value, the `AUTO_INCREMENT` value is updated, so the next value will be higher. If the new value is lower than the current maximum value, the `AUTO_INCREMENT` value remains unchanged.

The following example demonstrates these behaviors:

```
CREATE TABLE t (id INTEGER UNSIGNED AUTO_INCREMENT PRIMARY KEY) ENGINE = InnoDB;

INSERT INTO t VALUES (NULL);
SELECT id FROM t;
+----+
| id |
+----+
|  1 |
+----+

INSERT INTO t VALUES (10); -- higher value
SELECT id FROM t;
+----+
| id |
+----+
|  1 |
| 10 |
+----+

INSERT INTO t VALUES (2); -- lower value
INSERT INTO t VALUES (NULL); -- auto value
SELECT id FROM t;
+----+
| id |
+----+
|  1 |
|  2 |
| 10 |
| 11 |
+----+
```

The [ARCHIVE](../../server-usage/storage-engines/archive.md) storage engine does not allow to insert a value that is lower than the current maximum.

## Missing Values

An AUTO\_INCREMENT column normally has missing values. This happens because if a row is deleted, or an AUTO\_INCREMENT value is explicitly updated, old values are never re-used. The REPLACE statement also deletes a row, and its value is wasted. With InnoDB, values can be reserved by a transaction; but if the transaction fails (for example, because of a ROLLBACK) the reserved value will be lost.

Thus AUTO\_INCREMENT values can be used to sort results in a chronological order, but not to create a numeric sequence.

## Replication

To make master-master or Galera safe to use `AUTO_INCREMENT` one should use the system variables [auto\_increment\_increment](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) and [auto\_increment\_offset](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md) to generate unique values for each server.

```
SET @@auto_increment_increment=3;

SHOW VARIABLES LIKE 'auto_inc%';
+--------------------------+-------+
| Variable_name            | Value |
+--------------------------+-------+
| auto_increment_increment | 3     |
| auto_increment_offset    | 1     |
+--------------------------+-------+

CREATE TABLE t (c INT NOT NULL AUTO_INCREMENT PRIMARY KEY);

INSERT INTO t VALUES (NULL), (NULL), (NULL);

SELECT * FROM t;
+---+
| c |
+---+
| 1 |
| 4 |
| 7 |
+---+

CREATE TABLE t2 (c INT NOT NULL AUTO_INCREMENT PRIMARY KEY);

SET @@auto_increment_offset=2;

SHOW VARIABLES LIKE 'auto_inc%';
+--------------------------+-------+
| Variable_name            | Value |
+--------------------------+-------+
| auto_increment_increment | 3     |
| auto_increment_offset    | 2     |
+--------------------------+-------+

INSERT INTO t2 VALUES (NULL), (NULL), (NULL);

SELECT * FROM t2;
+---+
| c |
+---+
| 2 |
| 5 |
| 8 |
+---+
```

If `auto_increment_offset` is larger than `auto_increment_increment`, the value of `auto_increment_offset` is ignored, and the offset reverts to the default of 1 instead:

```
SET @@auto_increment_offset=5;

SHOW VARIABLES LIKE 'auto_inc%';
+--------------------------+-------+
| Variable_name            | Value |
+--------------------------+-------+
| auto_increment_increment | 3     |
| auto_increment_offset    | 5     |
+--------------------------+-------+

CREATE TABLE t3 (c INT NOT NULL AUTO_INCREMENT PRIMARY KEY);

INSERT INTO t3 VALUES (NULL), (NULL), (NULL);

SELECT * FROM t3;
+---+
| c |
+---+
| 1 |
| 4 |
| 5 |
+---+

+--------------------------+-------+
| Variable_name            | Value |
+--------------------------+-------+
| auto_increment_increment | 3     |
| auto_increment_offset    | 3     |
+--------------------------+-------+

INSERT INTO t4 VALUES (NULL), (NULL), (NULL);

SELECT * FROM t4;
+---+
| c |
+---+
| 3 |
| 6 |
| 9 |
+---+
```

## Changing `auto_increment_increment` and `auto_incremenet_offset` when adding a new master to a multi-master setup

The purpose of [auto\_increment\_increment](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#auto_increment_increment) and [auto\_increment\_offset](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#auto_increment_offset) is to ensure that in a multi-master or multi-source setup, all masters generate unique values for `auto_increment` fields or for sequences with `INCREMENT=0`.&#x20;

If `auto_increment_increment` is larger than the current number of masters, then one can configure the new master with the not used `auto_increment_offset`. The easiest way to add a new master is to stop all MariaDB servers, update `auto_increment_increment` and `auto_increment_offset` in the configuration files, and restart.\


This has to be done if `auto_increment_increment` is 1. If one has more than one master (`auto_increment_increment` > 1), there is a way to add more masters with only having to restart one of the masters. The 'trick' is to configure one of the masters to not use all the values in its current sequence.&#x20;

The following example should illustrate how to do it. Assume you have two masters, A and B.

In this case you will have auto\_increment\_increment=2 for both masters and A would have `auto_increment_offset=1` and B would have `auto_increment_offset=2`. For A, all `auto_increment` and generated sequence values will be odd.

```
1
3
5
7
```

For B, all values will be even:

```
2
4
6
8
```

See the [Replication](auto_increment.md#replication) section above.

If we change `auto_increment_increment` from `2` to `4` in A, it will now generate values from this sequence:

```
1
5
9
13
```

As you can see, values `3`, `7`, `11` are not going to be used.We can get C to use values from this sequence by configuring `auto_increment_increment=4` and `auto_increment_offset=3`.

```
3
7
11
```

If we would like to add a 4'th master (D), we can do that by changing 'B' to use `auto_increment_increment=4` and then configure D to have `auto_increment_increment=4` and `auto_increment_offset=4`.&#x20;

{% hint style="info" %}
Note that when changing the `auto_increment_increment` or `auto_increment_offset` on a server, one has to either restart the server or ensure that all current connections are killed. This is needed to force all connections to use the new values.&#x20;

Also ensure that if you want to use the above trick, you always double the value of `auto_increment_increment`.  This is needed to ensure that the sequence used will not conflict with numbers generated by any other master.
{% endhint %}

## CHECK Constraints, DEFAULT Values and Virtual Columns

auto\_increment columns are not permitted in [CHECK constraints](../sql-statements/data-definition/constraint.md), [DEFAULT value expressions](../sql-statements/data-definition/create/create-table.md#default) and [virtual columns](../sql-statements/data-definition/create/generated-columns.md). They were permitted until [MariaDB 10.2.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-1026-release-notes), but did not work correctly. See [MDEV-11117](https://jira.mariadb.org/browse/MDEV-11117).

## Generating Auto\_Increment Values When Adding the Attribute

```
CREATE OR REPLACE TABLE t1 (a INT);
INSERT t1 VALUES (0),(0),(0);
ALTER TABLE t1 MODIFY a INT NOT NULL AUTO_INCREMENT PRIMARY KEY;
SELECT * FROM t1;
+---+
| a |
+---+
| 1 |
| 2 |
| 3 |
+---+
```

```
CREATE OR REPLACE TABLE t1 (a INT);
INSERT t1 VALUES (5),(0),(8),(0);
ALTER TABLE t1 MODIFY a INT NOT NULL AUTO_INCREMENT PRIMARY KEY;
SELECT * FROM t1;
+---+
| a |
+---+
| 5 |
| 6 |
| 8 |
| 9 |
+---+
```

If the [NO\_AUTO\_VALUE\_ON\_ZERO SQL\_MODE](../../server-management/variables-and-modes/sql-mode.md#no_auto_value_on_zero) is set, zero values will not be automatically incremented:

```
SET SQL_MODE='no_auto_value_on_zero';
CREATE OR REPLACE TABLE t1 (a INT);
INSERT t1 VALUES (3), (0);
ALTER TABLE t1 MODIFY a INT NOT NULL AUTO_INCREMENT PRIMARY KEY;
SELECT * FROM t1;
+---+
| a |
+---+
| 0 |
| 3 |
+---+
```

## See Also

* [Getting Started with Indexes](../../mariadb-quickstart-guides/mariadb-indexes-guide.md)
* [Sequences](../sql-structure/sequences/) - an alternative to auto\_increment available from [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103)
* [AUTO\_INCREMENT FAQ](auto_increment-faq.md)
* [LAST\_INSERT\_ID()](../sql-functions/secondary-functions/information-functions/last_insert_id.md)
* [AUTO\_INCREMENT handling in InnoDB](../../server-usage/storage-engines/innodb/auto_increment-handling-in-innodb.md)
* [BLACKHOLE and AUTO\_INCREMENT](../../server-usage/storage-engines/blackhole.md#blackhole-and-auto_increment)
* [UUID\_SHORT()](../sql-functions/secondary-functions/miscellaneous-functions/uuid_short.md) - Generate unique ids
* [Generating Identifiers – from AUTO\_INCREMENT to Sequence (percona.com)](https://www.percona.com/community-blog/2018/10/12/generating-identifiers-auto_increment-sequence/)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
