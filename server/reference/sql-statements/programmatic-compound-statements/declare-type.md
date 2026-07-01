---
description: >-
  Define data types for Oracle compatibility. This statement allows declaring
  PL/SQL-style record types and associative arrays, and REF CURSOR types within
  stored procedures.
---

# DECLARE TYPE

{% hint style="info" %}
This feature is available from MariaDB 12.1.
{% endhint %}

## Overview

The `DECLARE TYPE` declaration specifies user-defined data types that must be compatible with Oracle within stored procedures and anonymous blocks. It provides Oracle-compatible type declarations, such as record types, associative arrays, and `REF CURSOR` types, which allows for more flexible data handling and better compatibility with Oracle PL/SQL.

Associative arrays (`INDEX BY` tables) offer an in-memory key-value structure for quick data storage and effective lookups. REF CURSOR types allow for the creation of cursor variables that refer to query result sets and can be passed between program blocks.

The general syntax for defining associative array types is as follows:

```sql
DECLARE
   TYPE type_name TABLE OF rec_type_name INDEX BY idx_type_name
```

* `type_name` supports explicit and anchored data types (for instance, `t1.col1%TYPE`).
* `rec_type_name` supports scalar and record data types.
* The `INDEX BY` clause defines the key type using `idx_type_name`, which supports integer and string data types.

## Associative Arrays

In Oracle, associative arrays (called index-by tables) are sparse collections of elements indexed by keys, which can be integers or strings.

Here’s an example of how to declare an associative array in Oracle:

```sql
DECLARE
  TYPE array_t IS TABLE OF VARCHAR2(64) INDEX BY PLS_INTEGER;
  array array_t;
BEGIN
  array(1) := 'Hello';
  array(2) := 'World';
  DBMS_OUTPUT.PUT_LINE(array(1));
END;
```

### Methods

Associative arrays support the following methods:

* `FIRST` — a function that returns the first key
* `LAST` — a function that returns the last key
* `NEXT` — a function that returns the key after the given one
* `PRIOR` — a function that returns the key before the given one
* `COUNT` — a function that returns the number of elements
* `EXISTS` — a function that returns `TRUE` if the key exists
* `DELETE` — a procedure that removes a specific key, or clears the array

While the MariaDB implementation is largely aligned with Oracle’s implementation, there are a few differences:

* **Only literals as keys in the constructor**: When using constructors, keys must be literals — Oracle allows expressions.
* **Collation control**: Instead of `NLS_SORT` or `NLS_COMP`, MariaDB uses the SQL-standard `COLLATE` clause.
* **No nested associative arrays**: Arrays of arrays are not supported.

These differences are largely rooted in architectural constraints — MariaDB is aiming at staying as close to Oracle semantics as possible while maintaining performance and predictability.

### Examples

#### Associative Array of Scalar Elements

**Explicit type\_name**

```sql
DECLARE
  TYPE salary IS TABLE OF NUMBER INDEX BY VARCHAR2(20);
  salary_list salary;
  name VARCHAR2(20);
BEGIN
  salary_list('Rajnisj') := 62000;
  salary_list('James') := 78000;
  name:= salary_list.FIRST;
  WHILE name IS NOT NULL
  LOOP
    dbms_output.put_line(name || ' ' || TO_CHAR(salary_list(name)));
    name:= salary_list.NEXT(name);
  END LOOP;
END;
/
```

**Anchored type\_name**

```sql
CREATE TABLE t1 (a INT);
DECLARE
  TYPE salary IS TABLE OF t1.a%TYPE INDEX BY VARCHAR2(20);
  salary_list salary;
  name VARCHAR2(20);
BEGIN
  salary_list('Rajnisj') := 62000;
  salary_list('James') := 78000;
  name:= salary_list.FIRST;
  WHILE name IS NOT NULL
  LOOP
    dbms_output.put_line(name || ' ' || TO_CHAR(salary_list(name)));
    name:= salary_list.NEXT(name);
  END LOOP;
END;
/
```

#### Associative Array of Records

**Using Explicit Data Types**

```sql
DECLARE
  TYPE person_t IS RECORD
  (
    first_name VARCHAR(64),
    last_name VARCHAR(64)
  );
  person person_t;
  TYPE table_of_peson_t IS TABLE OF person_t INDEX BY VARCHAR(20);
  person_by_nickname table_of_peson_t;
  nick VARCHAR(20);
BEGIN
  person_by_nickname('Monty') := person_t('Michael', 'Widenius');
  person_by_nickname('Serg') := person_t('Sergei ', 'Golubchik');
  nick:= person_by_nickname.FIRST;
  WHILE nick IS NOT NULL
  LOOP
    person:= person_by_nickname(nick);
    dbms_output.put_line(nick || ' ' || person.first_name || ' '|| person.last_name);
    nick:= person_by_nickname.NEXT(nick);
  END LOOP;
  /
```

**Using Anchored Data Types**

```sql
DROP TABLE persons;
CREATE TABLE persons (nickname VARCHAR(64), first_name VARCHAR(64), last_name VARCHAR(64));
INSERT INTO persons VALUES ('Serg','Sergei ', 'Golubchik');
INSERT INTO persons VALUES ('Monty','Michael', 'Widenius');
DECLARE
  TYPE table_of_person_t IS TABLE OF persons%ROWTYPE INDEX BY persons.nickname%TYPE;
  person_by_nickname table_of_person_t;
  nickname persons.nickname%TYPE;
  person persons%ROWTYPE;
BEGIN
  FOR rec IN (SELECT * FROM persons)
  LOOP
    person_by_nickname(rec.nickname):= rec;
  END LOOP;
 
  nickname:= person_by_nickname.FIRST;
  WHILE nickname IS NOT NULL
  LOOP
    person:= person_by_nickname(nickname);
    dbms_output.put_line(person.nickname || ' ' || person.first_name || ' '|| person.last_name);
    nickname:= person_by_nickname.NEXT(nickname);
  END LOOP;
END;
/
```

## RECORD Types

In `sql_mode=ORACLE`, the `TYPE ... IS RECORD` statement allows you to define a user-defined data structure consisting of one or more fields.

Previously, TYPE-defined `RECORD` types could only be used in local program blocks and not in routine parameters or function `RETURN` clauses.

### **Syntax**

```sql
TYPE record_type_name IS RECORD (
    field_name data_type [NOT NULL] [DEFAULT expr],
    ...
);
```

* `record_type_name` is the name of the new record type.
* Each `field_name` is a named attribute of the record.
* Each `field_type` is a valid MariaDB data type or anchored type (`%TYPE`, `%ROWTYPE`).

### RECORD Types in Routine Parameters and Function RETURN

Starting with MariaDB 13.0.1, custom types defined with `DECLARE TYPE` (including `RECORD` and `REF CURSOR`) can be used as:

* Parameters of stored procedures and functions
* `RETURN` types of stored functions

Earlier, the use of a `RECORD` type in these contexts was prohibited by the MariaDB grammar and resulted in:

```
ERROR 4161 (HY000): Unknown data type
```

This change improves compatibility with Oracle PL/SQL, especially for private helper routines inside packages and for `REF CURSOR` usage.

### Using RECORDs in Routine Parameters

Starting with MariaDB 13.0.1, stored procedures within the same package can use a `RECORD` type declared inside the package body as a parameter.

```sql
SET sql_mode=ORACLE;
DELIMITER $$
CREATE OR REPLACE PACKAGE pkg1 AS
  PROCEDURE p1();
END;
CREATE OR REPLACE PACKAGE BODY pkg1 AS
  TYPE rec0_t IS RECORD (a INT, b VARCHAR(2), c INT);
  PROCEDURE private_p1(p0 rec0_t) AS
  BEGIN
    NULL;
  END;
  PROCEDURE p1 AS
  BEGIN
    CALL private_p1(a0);
  END;
END;
$$
DELIMITER ;
```

### Using RECORDs as a Function Return Type

A `RECORD` type declared inside a package body can also be used as the return type for a stored function inside the same package.

```sql
SET sql_mode=ORACLE;
DELIMITER $$
CREATE OR REPLACE PACKAGE pkg1 AS
  PROCEDURE p1();
END;
CREATE OR REPLACE PACKAGE BODY pkg1 AS
  TYPE rec0_t IS RECORD (a INT, b VARCHAR(2), c INT);
  FUNCTION private_f1() RETURN rec0_t AS
  BEGIN
    RETURN NULL;
  END;
  PROCEDURE p1() AS
  BEGIN
    DO private_f1();
  END;
END;
$$
DELIMITER ;
```

### Requirement

This feature is available in Oracle SQL mode. The SQL mode is stored when the package is created, so `SET sql_mode=ORACLE` must be executed before creating the package.

## REF CURSOR Types

MariaDB supports Oracle-compatible `REF CURSOR` type declarations as a part of the `DECLARE TYPE` statement. A `REF CURSOR` is a cursor variable that can refer to a query result set and be passed across program blocks, such as stored procedures or functions.

`REF CURSOR` types must be specified with a `TYPE` declaration before any variables of that type can be declared. It can be defined as weak or strong based on whether a return type is specified.

### Syntax

```sql
ref_cursor_type_definition:
   TYPE type_name IS REF CURSOR [ RETURN return_type ];
```

* If `RETURN` is deleted, the cursor type is weak.
* If `RETURN` is specified, the cursor type is strong and limited to a single row structure.

### Weak REF CURSOR

A weak `REF CURSOR` type is defined without a `RETURN` clause. It can be used with any query result.

```sql
TYPE weak_cursor IS REF CURSOR; -- weak type: no RETURN clause 
```

### Strong REF CURSOR

A strong `REF CURSOR` type is defined by a `RETURN` clause that defines the row structure the cursor must return.

```sql
TYPE storong_cursor IS REF CURSOR RETURN employees%ROWTYPE;  -- strong type
```

### Supported RETURN Types

MariaDB supports the following `RETURN` clause formats:

#### RETURN `record_type`

The return type can be a user-defined record type. Columns that correspond to the field names and types of the record must be returned by the query run against the cursor.

```sql
DROP TABLE t1;
CREATE TABLE t1 (a INT,b VARCHAR(10));
INSERT INTO t1 VALUES (10,'b10');
DECLARE
  TYPE rec_t IS RECORD (a INT, b VARCHAR(19));
  TYPE cur_rec_t IS REF CURSOR RETURN rec_t;
  c0 cur_rec_t;
  r0 rec_t;
BEGIN
  OPEN c0 FOR SELECT * FROM t1;
  LOOP
    FETCH c0 INTO r0;
    EXIT WHEN c0%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE(r0.a || ' ' || r0.b);
  END LOOP;
END;
```

#### RETURN `record_type%ROWTYPE`

The declared `RECORD` type can include anchored field types, such as `t1.b%TYPE`. This enables the record and therefore the cursor to automatically modify in the event that the underlying table column type changes.

```sql
DROP TABLE t1;
CREATE TABLE t1 (a INT,b VARCHAR(10));
INSERT INTO t1 VALUES (10,'b10');
DECLARE
  TYPE rec_t IS RECORD (a t1.a%TYPE, b t1.b%TYPE);
  TYPE cur_rec_t IS REF CURSOR RETURN rec_t;
  r0 rec_t;
  c0 cur_rec_t;
BEGIN
  OPEN c0 FOR SELECT * FROM t1;
  LOOP
    FETCH c0 INTO r0;
    EXIT WHEN c0%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE(r0.a || ' ' || r0.b);
  END LOOP;
END;
```

#### RETURN `record_variable%TYPE`

The cursor's return type is determined from a defined variable using the `%TYPE` attribute. At the time of declaration, the cursor inherits the type of the variable's row structure.

```sql
CREATE OR REPLACE PROCEDURE p1 IS
  TYPE rec0_t IS RECORD (a INT, b VARCHAR(10));
  v0 rec0_t;
  TYPE cur0_t IS REF CURSOR RETURN v0%TYPE;
  c0 cur0_t;
BEGIN
  OPEN c0 FOR SELECT 1,2 FROM DUAL;
  FETCH c0 INTO v0;
  DBMS_OUTPUT.PUT_LINE(v0.a || v0.b);
  CLOSE c0;
END;
```

#### RETURN `cursor%ROWTYPE`

The row structure of an existing static cursor declared in the same block serves as the anchor for the cursor's return type. The column types and names from that cursor's `SELECT` statement are inherited by the `REF CURSOR`.

```sql
CREATE OR REPLACE PROCEDURE p1 IS
  CURSOR cs IS SELECT 1 AS a,2 AS b FROM DUAL;
  TYPE curs_t IS REF CURSOR RETURN cs%ROWTYPE;
  c0 curs_t;
  v0 cs%ROWTYPE;
BEGIN
  OPEN c0 FOR SELECT 1,2 FROM DUAL;
  FETCH c0 INTO v0;
  DBMS_OUTPUT.PUT_LINE(v0.a || v0.b);
  CLOSE c0;
END;
```

#### RETURN `table_or_view%ROWTYPE`

Using `%ROWTYPE`, the return type of the cursor is directly linked to a table or view row structure. This cursor variable can only be used with queries that return all columns from the referenced table or view in the same sequence.

```sql
DROP TABLE t1;
CREATE TABLE t1 (a INT,b VARCHAR(10));
INSERT INTO t1 VALUES (10,'b10');
DECLARE
  TYPE cur_rec_t IS REF CURSOR RETURN t1%ROWTYPE;
  c0 cur_rec_t;
  r0 t1%ROWTYPE;
BEGIN
  OPEN c0 FOR SELECT * FROM t1;
  LOOP
    FETCH c0 INTO r0;
    EXIT WHEN c0%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE(r0.a || ' ' || r0.b);
  END LOOP;
END;
```

#### RETURN `cursor_variable%ROWTYPE`

The cursor's return type is derived from another `REF CURSOR` variable using `%ROWTYPE`. This allows for the connection of cursor type declarations, so that a second cursor inherits its structure from a previously specified cursor variable.

```sql
DROP TABLE t1;
CREATE TABLE t1 (a INT,b VARCHAR(10));
INSERT INTO t1 VALUES (10,'b10');
DECLARE
  TYPE cur1_t IS REF CURSOR RETURN t1%ROWTYPE;
  c1 cur1_t;
  TYPE cur0_t IS REF CURSOR RETURN c1%ROWTYPE;
  c0 cur0_t;
  r0 c0%ROWTYPE;
BEGIN
  OPEN c0 FOR SELECT * FROM t1;
  LOOP
    FETCH c0 INTO r0;
    EXIT WHEN c0%NOTFOUND;
    DBMS_OUTPUT.PUT_LINE(r0.a || ' ' || r0.b);
  END LOOP;
END;
```

### Limitations

The following form is not supported:

```sql
TYPE cur1_t IS REF CURSOR RETURN cur0_t;
```

The `RETURN` clause must refer to a specific record type, not another `REF CURSOR` type.

## See Also

* [DECLARE CURSOR](programmatic-compound-statements-cursors/declare-cursor.md)
* [DECLARE Variable](declare-variable.md)
* [Oracle Mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)
* [CREATE FUNCTION](../data-definition/create/create-function.md)
* [CREATE PROCEDURE](../../../server-usage/stored-routines/stored-procedures/create-procedure.md)
