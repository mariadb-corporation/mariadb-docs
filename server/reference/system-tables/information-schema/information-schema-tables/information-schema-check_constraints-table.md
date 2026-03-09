---
description: >-
  The Information Schema CHECK_CONSTRAINTS table stores metadata about the
  constraints defined for tables in all databases, including the check clause.
---

# Information Schema CHECK\_CONSTRAINTS Table

The [Information Schema](../) `CHECK_CONSTRAINTS` table stores metadata about the [constraints](../../../sql-statements/data-definition/constraint.md) defined for tables in all databases.

It contains the following columns:

| Column              | Description                                                                                                                                                      |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CONSTRAINT\_CATALOG | Always contains the string 'def'.                                                                                                                                |
| CONSTRAINT\_SCHEMA  | Database name.                                                                                                                                                   |
| CONSTRAINT\_NAME    | Constraint name.                                                                                                                                                 |
| TABLE\_NAME         | Table name.                                                                                                                                                      |
| LEVEL               | Type of the constraint ('Column' or 'Table'). From [MariaDB 10.5.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.10). |
| CHECK\_CLAUSE       | Constraint clause.                                                                                                                                               |

## Example

A table with a numeric table check constraint and with a default check constraint name:

```sql
CREATE TABLE t ( a INT, CHECK (a>10));
```

To see check constraint call `check_constraints` table from [information schema](../).

```sql
SELECT * FROM INFORMATION_SCHEMA.CHECK_CONSTRAINTS\G
```

```sql
*************************** 1. row ***************************
CONSTRAINT_CATALOG: def
 CONSTRAINT_SCHEMA: test
   CONSTRAINT_NAME: CONSTRAINT_1
        TABLE_NAME: t
      CHECK_CLAUSE: `a` > 10
```

A new table check constraint called `a_upper`:

```sql
ALTER TABLE t ADD CONSTRAINT a_upper CHECK (a<100);
```

```sql
SELECT * FROM INFORMATION_SCHEMA.CHECK_CONSTRAINTS\G
```

```sql
*************************** 1. row ***************************
CONSTRAINT_CATALOG: def
 CONSTRAINT_SCHEMA: test
   CONSTRAINT_NAME: CONSTRAINT_1
        TABLE_NAME: t
      CHECK_CLAUSE: `a` > 10
*************************** 2. row ***************************
CONSTRAINT_CATALOG: def
 CONSTRAINT_SCHEMA: test
   CONSTRAINT_NAME: a_upper
        TABLE_NAME: t
      CHECK_CLAUSE: `a` < 100
```

A new table `tt` with a field check constraint called `b` , as well as a table check constraint called `b_upper`:

```sql
CREATE TABLE tt(b INT CHECK(b>0),CONSTRAINT b_upper CHECK(b<50));

SELECT * FROM INFORMATION_SCHEMA.CHECK_CONSTRAINTS;
+--------------------+-------------------+-----------------+------------+--------------+
| CONSTRAINT_CATALOG | CONSTRAINT_SCHEMA | CONSTRAINT_NAME | TABLE_NAME | CHECK_CLAUSE |
+--------------------+-------------------+-----------------+------------+--------------+
| def                | test              | b               | tt         | `b` > 0      |
| def                | test              | b_upper         | tt         | `b` < 50     |
| def                | test              | CONSTRAINT_1    | t          | `a` > 10     |
| def                | test              | a_upper         | t          | `a` < 100    |
+--------------------+-------------------+-----------------+------------+--------------+
```

_Note:_ The name of the field constraint is the same as the field name.

After dropping the default table constraint called `CONSTRAINT_1`:

```sql
ALTER TABLE t DROP CONSTRAINT CONSTRAINT_1;

SELECT * FROM INFORMATION_SCHEMA.CHECK_CONSTRAINTS;
+--------------------+-------------------+-----------------+------------+--------------+
| CONSTRAINT_CATALOG | CONSTRAINT_SCHEMA | CONSTRAINT_NAME | TABLE_NAME | CHECK_CLAUSE |
+--------------------+-------------------+-----------------+------------+--------------+
| def                | test              | b               | tt         | `b` > 0      |
| def                | test              | b_upper         | tt         | `b` < 50     |
| def                | test              | a_upper         | t          | `a` < 100    |
+--------------------+-------------------+-----------------+------------+--------------+
```

Trying to insert invalid arguments into table `t` and `tt` generates an error.

```sql
INSERT INTO t VALUES (10),(20),(100);
ERROR 4025 (23000): CONSTRAINT `a_upper` failed for `test`.`t`

INSERT INTO tt VALUES (10),(-10),(100);
ERROR 4025 (23000): CONSTRAINT `b` failed for `test`.`tt`

INSERT INTO tt VALUES (10),(20),(100);
ERROR 4025 (23000): CONSTRAINT `b_upper` failed for `test`.`tt`
```

{% hint style="info" %}
The following statement can be performed from MariaDB 10.5.10.
{% endhint %}

```sql
CREATE TABLE majra(CHECK(x>0), x INT, y INT CHECK(y < 0), z INT,
                              CONSTRAINT z CHECK(z>0), CONSTRAINT xyz CHECK(x<10 AND y<10 AND z<10));
Query OK, 0 rows affected (0.036 sec)

SHOW CREATE TABLE majra;
+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Table | Create Table                                                                                                                                                                                                                                                                                                   |
+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| majra | CREATE TABLE `majra` (
  `x` int(11) DEFAULT NULL,
  `y` int(11) DEFAULT NULL CHECK (`y` < 0),
  `z` int(11) DEFAULT NULL,
  CONSTRAINT `CONSTRAINT_1` CHECK (`x` > 0),
  CONSTRAINT `z` CHECK (`z` > 0),
  CONSTRAINT `xyz` CHECK (`x` < 10 AND `y` < 10 AND `z` < 10)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 |
+-------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.000 sec)


SELECT * FROM information_schema.check_constraints WHERE table_name='majra';
+--------------------+-------------------+------------+-----------------+--------+------------------------------------+
| CONSTRAINT_CATALOG | CONSTRAINT_SCHEMA | TABLE_NAME | CONSTRAINT_NAME | LEVEL  | CHECK_CLAUSE                       |
+--------------------+-------------------+------------+-----------------+--------+------------------------------------+
| def                | test              | majra      | y               | Column | `y` < 0                            |
| def                | test              | majra      | CONSTRAINT_1    | Table  | `x` > 0                            |
| def                | test              | majra      | z               | Table  | `z` > 0                            |
| def                | test              | majra      | xyz             | Table  | `x` < 10 and `y` < 10 and `z` < 10 |
+--------------------+-------------------+------------+-----------------+--------+------------------------------------+
4 rows in set (0.001 sec)
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
