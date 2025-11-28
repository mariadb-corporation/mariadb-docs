---
description: >-
  Prepare and run a dynamic SQL statement in one step. This command simplifies
  the process by combining the PREPARE and EXECUTE operations.
---

# EXECUTE IMMEDIATE

## Syntax

```sql
EXECUTE IMMEDIATE statement
    [USING param[, param] ...]

param:
    expression | IGNORE | DEFAULT
```

## Description

`EXECUTE IMMEDIATE` executes a dynamic SQL statement created on the fly, which can reduce performance overhead. For example:

```sql
EXECUTE IMMEDIATE 'SELECT 1'
```

which is shorthand for:

```sql
PREPARE stmt FROM "select 1";
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
```

EXECUTE IMMEDIATE supports complex expressions as prepare source and parameters:

```sql
EXECUTE IMMEDIATE CONCAT('SELECT COUNT(*) FROM ', 't1', ' WHERE a=?') USING 5+5;
```

Limitations: subselects and stored function calls are not supported as a prepare source.

The following examples return an error:

```sql
CREATE OR REPLACE FUNCTION f1() RETURNS VARCHAR(64) RETURN 'SELECT * FROM t1';
EXECUTE IMMEDIATE f1();
ERROR 1970 (42000): EXECUTE IMMEDIATE does not support subqueries or stored functions

EXECUTE IMMEDIATE (SELECT 'SELECT * FROM t1');
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that 
  corresponds to your MariaDB server version for the right syntax to use near 
  'SELECT 'SELECT * FROM t1')' at line 1

CREATE OR REPLACE FUNCTION f1() RETURNS INT RETURN 10;
EXECUTE IMMEDIATE 'SELECT * FROM t1 WHERE a=?' USING f1();
ERROR 1970 (42000): EXECUTE..USING does not support subqueries or stored functions

EXECUTE IMMEDIATE 'SELECT * FROM t1 WHERE a=?' USING (SELECT 10);
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that 
  corresponds to your MariaDB server version for the right syntax to use near 
  'SELECT 10)' at line 1
```

One can use a user or an SP variable as a workaround:

```sql
CREATE OR REPLACE FUNCTION f1() RETURNS VARCHAR(64) RETURN 'SELECT * FROM t1';
SET @stmt=f1();
EXECUTE IMMEDIATE @stmt;

SET @stmt=(SELECT 'SELECT 1');
EXECUTE IMMEDIATE @stmt;

CREATE OR REPLACE FUNCTION f1() RETURNS INT RETURN 10;
SET @param=f1();
EXECUTE IMMEDIATE 'SELECT * FROM t1 WHERE a=?' USING @param;

SET @param=(SELECT 10);
EXECUTE IMMEDIATE 'SELECT * FROM t1 WHERE a=?' USING @param;
```

`EXECUTE IMMEDIATE` supports user variables and SP variables as OUT parameters:

```sql
DELIMITER $$
CREATE OR REPLACE PROCEDURE p1(OUT a INT)
BEGIN
  SET a:= 10;
END;
$$
DELIMITER ;
SET @a=2;
EXECUTE IMMEDIATE 'CALL p1(?)' USING @a;
SELECT @a;
+------+
| @a   |
+------+
|   10 |
+------+
```

Similar to `PREPARE`, `EXECUTE IMMEDIATE` is allowed in stored procedures but is not allowed in stored functions.

This example uses `EXECUTE IMMEDIATE` inside a stored procedure:

```sql
DELIMITER $$
CREATE OR REPLACE PROCEDURE p1()
BEGIN
  EXECUTE IMMEDIATE 'SELECT 1';
END;
$$
DELIMITER ;
CALL p1;
+---+
| 1 |
+---+
| 1 |
+---+
```

This script returns an error:

```sql
DELIMITER $$
CREATE FUNCTION f1() RETURNS INT
BEGIN
  EXECUTE IMMEDIATE 'DO 1';
  RETURN 1;
END;
$$
ERROR 1336 (0A000): Dynamic SQL is not allowed in stored function or trigger
```

`EXECUTE IMMEDIATE` can use `DEFAULT` and `IGNORE` indicators as bind parameters:

```sql
CREATE OR REPLACE TABLE t1 (a INT DEFAULT 10);
EXECUTE IMMEDIATE 'INSERT INTO t1 VALUES (?)' USING DEFAULT;
SELECT * FROM t1;
+------+
| a    |
+------+
|   10 |
+------+
```

EXECUTE IMMEDIATE increments the [Com\_execute\_immediate](../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#com_execute_immediate) status variable, as well as the [Com\_stmt\_prepare](../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#com_stmt_prepare), [Com\_stmt\_execute](../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#com_stmt_execute) and [Com\_stmt\_close](../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#com_stmt_close) status variables.

Note, EXECUTE IMMEDIATE does not increment the [Com\_execute\_sql](../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#com_execute_sql) status variable. _Com\_execute\_sql_ is used only for [PREPARE](prepare-statement.md)..[EXECUTE](execute-statement.md).

This session screenshot demonstrates how EXECUTE IMMEDIATE affects status variables:

```sql
SELECT * FROM INFORMATION_SCHEMA.SESSION_STATUS WHERE VARIABLE_NAME RLIKE 
  ('COM_(EXECUTE|STMT_PREPARE|STMT_EXECUTE|STMT_CLOSE)');

+-----------------------+----------------+
| VARIABLE_NAME         | VARIABLE_VALUE |
+-----------------------+----------------+
| COM_EXECUTE_IMMEDIATE | 0              |
| COM_EXECUTE_SQL       | 0              |
| COM_STMT_CLOSE        | 0              |
| COM_STMT_EXECUTE      | 0              |
| COM_STMT_PREPARE      | 0              |
+-----------------------+----------------+

EXECUTE IMMEDIATE 'SELECT 1';
+---+
| 1 |
+---+
| 1 |
+---+

SELECT * FROM INFORMATION_SCHEMA.SESSION_STATUS WHERE VARIABLE_NAME RLIKE 
  ('COM_(EXECUTE|STMT_PREPARE|STMT_EXECUTE|STMT_CLOSE)');
+-----------------------+----------------+
| VARIABLE_NAME         | VARIABLE_VALUE |
+-----------------------+----------------+
| COM_EXECUTE_IMMEDIATE | 1              |
| COM_EXECUTE_SQL       | 0              |
| COM_STMT_CLOSE        | 1              |
| COM_STMT_EXECUTE      | 1              |
| COM_STMT_PREPARE      | 1              |
+-----------------------+----------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
