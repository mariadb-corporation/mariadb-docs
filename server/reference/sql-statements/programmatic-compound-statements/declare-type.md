---
description: >-
  Define data types for Oracle compatibility. This statement allows declaring
  PL/SQL-style record types and associative arrays within stored procedures.
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
