---
description: >-
  ROW is a data type used in stored programs to store a complete row of data
  from a cursor or table.
---

# ROW

## Syntax

```sql
ROW (<field name> <data type> [{, <field name> <data type>}... ])
```

## Description

`ROW` is a data type for [stored procedure](../../../server-usage/stored-routines/stored-procedures/) variables.

## Features

### ROW fields as normal variables

`ROW` fields (members) act as normal variables, and are able to appear in all query parts where a stored procedure variable is allowed:

* Assignment is using the `:=` operator and the [SET](../../sql-statements/administrative-sql-statements/set-commands/set.md) command:

```sql
a.x:= 10;
a.x:= b.x;
SET a.x= 10, a.y=20, a.z= b.z;
```

* Passing to functions and operators:

```sql
SELECT f1(rec.a), rec.a<10;
```

* Clauses (select list, WHERE, HAVING, LIMIT, etc...,):

```sql
SELECT var.a, t1.b FROM t1 WHERE t1.b=var.b LIMIT var.c;
```

* `INSERT` values:

```sql
INSERT INTO t1 VALUES (rec.a, rec.b, rec.c);
```

* `SELECT .. INTO` targets:

```sql
SELECT a,b INTO rec.a, rec.b FROM t1 WHERE t1.id=10;
```

* Dynamic SQL out parameters ([EXECUTE](../../sql-statements/prepared-statements/execute-statement.md) and [EXECUTE IMMEDIATE](../../sql-statements/prepared-statements/execute-immediate.md))

```sql
EXECUTE IMMEDIATE 'CALL proc_with_out_param(?)' USING rec.a;
```

### ROW type variables as FETCH targets

`ROW` type variables are allowed as [FETCH](../../sql-statements/programmatic-compound-statements/programmatic-compound-statements-cursors/fetch.md) targets:

```sql
FETCH cur INTO rec;
```

where `cur` is a `CURSOR` and `rec` is a `ROW` type stored procedure variable.

Note, currently an attempt to use `FETCH` for a `ROW` type variable returns this error:

```sql
ERROR 1328 (HY000): Incorrect number of FETCH variables
```

`FETCH` from a cursor `cur` into a `ROW` variable `rec` works as follows:

* The number of fields in `cur` must match the number of fields in `rec`. Otherwise, an error is reported.
* Assignment is done from left to right. The first cursor field is assigned to the first variable field, the second cursor field is assigned to the second variable field, etc.
* Field names in `rec` are not important and can differ from field names in `cur`.

See [FETCH Examples](row.md#fetch-examples) (below) for examples of using this with`sql_mode=ORACLE` and `sql_mode=DEFAULT`.

### ROW type variables as `SELECT...INTO` targets

`ROW` type variables are allowed as `SELECT..INTO` targets with some differences depending on which `sql_mode` is in use.

* When using `sql_mode=ORACLE`, `table%ROWTYPE` and `cursor%ROWTYPE` variables can be used as `SELECT...INTO` targets.
* Using multiple `ROW` variables in the `SELECT..INTO` list will report an error.
* Using `ROW` variables with a different column count than in the `SELECT..INTO` list will report an error.

See [SELECT...INTO Examples](row.md#selectinto-examples) (below) for examples of using this with `sql_mode=ORACLE` and `sql_mode=DEFAULT`.

## Features not implemented

The following features are planned, but not implemented yet:

* Returning a `ROW` type expression from a stored function (see [MDEV-12252](https://jira.mariadb.org/browse/MDEV-12252)). This will need some grammar change to support field names after parentheses:

```sql
SELECT f1().x FROM DUAL;
```

* Returning a `ROW` type expression from a built-in hybrid type function, such as `CASE`, `IF`, etc.
* `ROW` of `ROW` values

## Examples

### Declaring a ROW in a stored procedure

```sql
DELIMITER $$
CREATE PROCEDURE p1()
BEGIN
  DECLARE r ROW (c1 INT, c2 VARCHAR(10));
  SET r.c1= 10;
  SET r.c2= 'test';
  INSERT INTO t1 VALUES (r.c1, r.c2);
END;
$$
DELIMITER ;
CALL p1();
```

### FETCH Examples

A complete `FETCH` example for `sql_mode=ORACLE`:

```sql
DROP TABLE IF EXISTS t1;
CREATE TABLE t1 (a INT, b VARCHAR(32));
INSERT INTO t1 VALUES (10,'b10');
INSERT INTO t1 VALUES (20,'b20');
INSERT INTO t1 VALUES (30,'b30');

SET sql_mode=oracle;
DROP PROCEDURE IF EXISTS p1;
DELIMITER $$
CREATE PROCEDURE p1 AS
  rec ROW(a INT, b VARCHAR(32));
  CURSOR c IS SELECT a,b FROM t1;
BEGIN
  OPEN c;
  LOOP
    FETCH c INTO rec;
    EXIT WHEN c%NOTFOUND;
    SELECT ('rec=(' || rec.a ||','|| rec.b||')');
  END LOOP;
  CLOSE c;
END;
$$
DELIMITER ;
CALL p1();
```

A complete `FETCH` example for `sql_mode=DEFAULT`:

```sql
DROP TABLE IF EXISTS t1;
CREATE TABLE t1 (a INT, b VARCHAR(32));
INSERT INTO t1 VALUES (10,'b10');
INSERT INTO t1 VALUES (20,'b20');
INSERT INTO t1 VALUES (30,'b30');

SET sql_mode=DEFAULT;
DROP PROCEDURE IF EXISTS p1;
DELIMITER $$
CREATE PROCEDURE p1()
BEGIN
  DECLARE done INT DEFAULT FALSE;
  DECLARE rec ROW(a INT, b VARCHAR(32));
  DECLARE c CURSOR FOR SELECT a,b FROM t1;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;
  OPEN c;
read_loop:
  LOOP
    FETCH c INTO rec;
    IF done THEN
      LEAVE read_loop;
    END IF;
    SELECT CONCAT('rec=(',rec.a,',',rec.b,')');
  END LOOP;
  CLOSE c;
END;
$$
DELIMITER ;
CALL p1();
```

### SELECT...INTO Examples

A `SELECT...INTO` example for `sql_mode=DEFAULT`:

```sql
SET sql_mode=DEFAULT;
DROP TABLE IF EXISTS t1;
DROP PROCEDURE IF EXISTS p1;
CREATE TABLE t1 (a INT, b VARCHAR(32));
INSERT INTO t1 VALUES (10,'b10');
DELIMITER $$
CREATE PROCEDURE p1()
BEGIN
  DECLARE rec1 ROW(a INT, b VARCHAR(32));
  SELECT * FROM t1 INTO rec1;
  SELECT rec1.a, rec1.b;
END;
$$
DELIMITER ;
CALL p1();
```

The above example returns:

```sql
+--------+--------+
| rec1.a | rec1.b |
+--------+--------+
|     10 | b10    |
+--------+--------+
```

A `SELECT...INTO` example for `sql_mode=ORACLE`:

```sql
SET sql_mode=ORACLE;
DROP TABLE IF EXISTS t1;
DROP PROCEDURE IF EXISTS p1;
CREATE TABLE t1 (a INT, b VARCHAR(32));
INSERT INTO t1 VALUES (10,'b10');
DELIMITER $$
CREATE PROCEDURE p1 AS
  rec1 ROW(a INT, b VARCHAR(32));
BEGIN
  SELECT * FROM t1 INTO rec1;
  SELECT rec1.a, rec1.b;
END;
$$
DELIMITER ;
CALL p1();
```

The above example returns:

```sql
+--------+--------+
| rec1.a | rec1.b |
+--------+--------+
|     10 | b10    |
+--------+--------+
```

An example for `sql_mode=ORACLE` using `table%ROWTYPE` variables as `SELECT..INTO` targets:

```sql
SET sql_mode=ORACLE;
DROP TABLE IF EXISTS t1;
DROP PROCEDURE IF EXISTS p1;
CREATE TABLE t1 (a INT, b VARCHAR(32));
INSERT INTO t1 VALUES (10,'b10');
DELIMITER $$
CREATE PROCEDURE p1 AS
  rec1 t1%ROWTYPE;
BEGIN
  SELECT * FROM t1 INTO rec1;
  SELECT rec1.a, rec1.b;
END;
$$
DELIMITER ;
CALL p1();
```

The above example returns:

```sql
+--------+--------+
| rec1.a | rec1.b |
+--------+--------+
|     10 | b10    |
+--------+--------+
```

An example for `sql_mode=ORACLE` using `cursor%ROWTYPE` variables as `SELECT..INTO` targets:

```sql
SET sql_mode=ORACLE;
DROP TABLE IF EXISTS t1;
DROP PROCEDURE IF EXISTS p1;
CREATE TABLE t1 (a INT, b VARCHAR(32));
INSERT INTO t1 VALUES (10,'b10');
DELIMITER $$
CREATE PROCEDURE p1 AS
  CURSOR cur1 IS SELECT * FROM t1;
  rec1 cur1%ROWTYPE;
BEGIN
  SELECT * FROM t1 INTO rec1;
  SELECT rec1.a, rec1.b;
END;
$$
DELIMITER ;
CALL p1();
```

The above example returns:

```sql
+--------+--------+
| rec1.a | rec1.b |
+--------+--------+
|     10 | b10    |
+--------+--------+
```

Row Table example:

```sql
CREATE TABLE row_table(
  descr VARCHAR(20),
  val INT
);
```

```sql
INSERT INTO row_table VALUES ('Life', 42);
```

```sql
DELIMITER $$
CREATE PROCEDURE row_proc()
BEGIN
  DECLARE rec1 ROW(descr VARCHAR(20), val INT);
  SELECT * INTO rec1 FROM row_table;
  SELECT rec1.descr, rec1.val;
END;
$$
DELIMITER ;
```

```sql
CALL row_proc();

+------------+----------+
| rec1.descr | rec1.val |
+------------+----------+
| Life       |       42 |
+------------+----------+
```

## See Also

* [STORED PROCEDURES](../../../server-usage/stored-routines/stored-procedures/)
* [DECLARE Variable](../../sql-statements/programmatic-compound-statements/declare-variable.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
