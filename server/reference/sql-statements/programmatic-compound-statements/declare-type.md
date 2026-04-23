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

One of the standout features of Oracle PL/SQL is the associative array — a versatile and efficient in-memory data structure that developers rely on for fast temporary lookups, streamlined batch processing, and dynamic report generation.

`DECLARE TYPE` adds support for Oracle-style `INDEX BY` tables (associative arrays) for stored routines and anonymous blocks, using this syntax:

```sql
DECLARE
   TYPE type_name TABLE OF rec_type_name INDEX BY idx_type_name
```

* `type_name` supports explicit and anchored data types (for instance, `t1.col1%TYPE`).
* The `INDEX BY` clause supports integer and string data types.
* `rec_type_name` supports scalar and record data types.

It supports the following associative array methods:

* `FIRST` — a function that returns the first key
* `LAST` — a function that returns the last key
* `NEXT` — a function that returns the key after the given one
* `PRIOR` — a function that returns the key before the given one
* `COUNT` — a function that returns the number of elements
* `EXISTS` — a function that returns `TRUE` if the key exists
* `DELETE` — a procedure that removes a specific key, or clears the array

## REF CURSOR Types

MariaDB supports Oracle-compatible `REF CURSOR` type declarations as a part of the `DECLARE TYPE` statement. A `REF CURSOR` is a cursor variable that can refer to a query result set and be passed across program blocks, such as stored procedures or functions.&#x20;

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

#### RETURN `record_variable%TYPE`&#x20;

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

#### RETURN `table_or_view%ROWTYPE`&#x20;

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

#### RETURN `cursor_variable%ROWTYPE`&#x20;

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

The following form is not supported.

```sql
TYPE cur1_t IS REF CURSOR RETURN cur0_t;
```

The `RETURN` clause must refer to a specific record type, not another `REF CURSOR` type.

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

While the MariaDB implementation is largely aligned with Oracle’s implementation, there are a few differences:

* **Only literals as keys in the constructor**: When using constructors, keys must be literals — Oracle allows expressions.
* **Collation control**: Instead of `NLS_SORT` or `NLS_COMP`, MariaDB uses the SQL-standard `COLLATE` clause.
* **No nested associative arrays**: Arrays of arrays are not supported.

These differences are largely rooted in architectural constraints — MariaDB is aiming at staying as close to Oracle semantics as possible while maintaining performance and predictability.

## Examples

### Associative Array of Scalar Elements

#### Explicit type\_name

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

#### Anchored type\_name

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

### Associative Array of Records

#### Using Explicit Data Types

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

#### Using Anchored Data Types

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

## See Also

* [DECLARE CURSOR](programmatic-compound-statements-cursors/declare-cursor.md)
* [DECLARE Variable](declare-variable.md)
* [Oracle Mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)
