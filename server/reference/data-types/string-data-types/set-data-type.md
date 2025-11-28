---
description: >-
  String object with zero or more values from a predefined list. A SET column
  can store multiple values selected from a list of permitted strings.
---

# SET Data Type

## Syntax

```sql
SET('value1','value2',...) [CHARACTER SET charset_name] [COLLATE collation_name]
```

## Description

A set. A string object that can have zero or more values, each of which must be chosen from the list of values 'value1', 'value2', ... A `SET` column can have a maximum of 64 members. `SET` values are\
represented internally as integers.

`SET` values cannot contain commas.

If a `SET` contains duplicate values, an error will be returned if [strict mode](../../../server-management/variables-and-modes/sql_mode.md#strict-mode) is enabled, or a warning if strict mode is not enabled.

## EXAMPLES

```sql
CREATE TABLE set_example (
  description VARCHAR(20),
  example SET('Foo', 'Bar', 'Baz', 'Bob')
);
```

```sql
INSERT INTO set_example VALUES
  ('1 val', 'Foo'),
  ('2 vals', 'Baz,Foo'),
  ('4 vals', 'Bob,Foo,Bar,Foo,Baz,Bob');
```

```sql
SELECT * FROM set_example;

+-------------+-----------------+
| description | example         |
+-------------+-----------------+
| 1 val       | Foo             |
| 2 vals      | Foo,Baz         |
| 4 vals      | Foo,Bar,Baz,Bob |
+-------------+-----------------+
```

## See Also

* [Character Sets and Collations](character-sets/supported-character-sets-and-collations.md)
* [Data Type Storage Requirements](../data-type-storage-requirements.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
