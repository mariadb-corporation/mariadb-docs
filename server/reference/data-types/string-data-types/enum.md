---
description: >-
  Complete ENUM type reference: ENUM('v1','v2') syntax, CHARACTER SET/COLLATE
  options, NULL/empty string defaults, and numeric index sorting guidelines.
---

# ENUM

## Syntax

```sql
ENUM('value1','value2',...) [CHARACTER SET charset_name] [COLLATE collation_name]
```

## Description

An enumeration. A string object that can have only one value, chosen from the list of values 'value1', 'value2', ..., `NULL` or the special '' error value. In theory, an `ENUM` column can have a maximum of 65,535 distinct values; in practice, the real maximum depends on many factors. `ENUM` values are represented internally as integers.

Trailing spaces are automatically stripped from `ENUM` values on table creation.

`ENUM` values require relatively little storage space compared to strings, either one or two bytes depending on the number of enumeration values.

### NULL and empty values

An `ENUM` can also contain `NULL` and empty values. If the `ENUM` column is declared to permit `NULL` values, `NULL` becomes a valid value, as well as the default value (see below). If [strict SQL Mode](../../../server-management/variables-and-modes/sql_mode.md) is not enabled, and an invalid value is inserted into an `ENUM`, a special empty string, with an index value of zero (see Numeric index, below), is inserted, with a warning. This may be confusing, because the empty string is also a possible value, and the only difference if that is this case its index is not 0. Inserting will fail with an error if strict mode is active.

If a `DEFAULT` clause is missing, the default value will be:

* `NULL` if the column is nullable;
* otherwise, the first value in the enumeration.

### Numeric index

`ENUM` values are indexed numerically in the order they are defined, and sorting will be performed in this numeric order. We suggest not using `ENUM` to store numerals, as there is little to no storage space benefit, and it is easy to confuse the enum integer with the enum numeral value by leaving out the quotes.

An `ENUM` defined as `ENUM('apple','orange','pear')` would have the following index values:

| Index | Value    |
| ----- | -------- |
| NULL  | NULL     |
| 0     | ''       |
| 1     | 'apple'  |
| 2     | 'orange' |
| 3     | 'pear'   |

## Examples

```sql
CREATE TABLE fruits (
  id INT NOT NULL auto_increment PRIMARY KEY,
  fruit ENUM('apple','orange','pear'),
  bushels INT);

DESCRIBE fruits;
+---------+-------------------------------+------+-----+---------+----------------+
| Field   | Type                          | Null | Key | Default | Extra          |
+---------+-------------------------------+------+-----+---------+----------------+
| id      | int(11)                       | NO   | PRI | NULL    | auto_increment |
| fruit   | enum('apple','orange','pear') | YES  |     | NULL    |                |
| bushels | int(11)                       | YES  |     | NULL    |                |
+---------+-------------------------------+------+-----+---------+----------------+

INSERT INTO fruits
    (fruit,bushels) VALUES
    ('pear',20),
    ('apple',100),
    ('orange',25);

INSERT INTO fruits
    (fruit,bushels) VALUES
    ('avocado',10);
ERROR 1265 (01000): Data truncated for column 'fruit' at row 1

SELECT * FROM fruits;
+----+--------+---------+
| id | fruit  | bushels |
+----+--------+---------+
|  1 | pear   |      20 |
|  2 | apple  |     100 |
|  3 | orange |      25 |
+----+--------+---------+
```

Selecting by numeric index:

```sql
SELECT * FROM fruits WHERE fruit=2;
+----+--------+---------+
| id | fruit  | bushels |
+----+--------+---------+
|  3 | orange |      25 |
+----+--------+---------+
```

Sorting is according to the index value:

```sql
CREATE TABLE enums (a ENUM('2','1'));

INSERT INTO enums VALUES ('1'),('2');

SELECT * FROM enums ORDER BY a ASC;
+------+
| a    |
+------+
| 2    |
| 1    |
+------+
```

It's easy to get confused between returning the enum integer with the stored value, so we don't suggest using `ENUM` to store numerals. The first example returns the 1st indexed field ('2' has an index value of 1, as it's defined first), while the second example returns the string value '1'.

```sql
SELECT * FROM enums WHERE a=1;
+------+
| a    |
+------+
| 2    |
+------+

SELECT * FROM enums WHERE a='1';
+------+
| a    |
+------+
| 1    |
+------+
```

Example of `ENUM`:

```sql
CREATE TABLE enum_example (
  description VARCHAR(20),
  example ENUM('Alpha', 'Beta', 'Gamma', 'RC', 'Stable')
);
```

```sql
INSERT INTO enum_example VALUES
  ('foo', 'Beta'),
  ('bar', 'RC'),
  ('baz', 'Alpha'),
  ('bob', 5);
```

```sql
SELECT * FROM enum_example;

+-------------+---------+
| description | example |
+-------------+---------+
| foo         | Beta    |
| bar         | RC      |
| baz         | Alpha   |
| bob         | Stable  |
+-------------+---------+
```

## See Also

* [Data Type Storage Requirements](../data-type-storage-requirements.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
