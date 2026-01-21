---
description: Synonym for TINYINT. This type uses 1 byte of storage.
---

# INT1

`INT1` is a synonym for [TINYINT](tinyint.md).

```sql
CREATE TABLE t1 (x INT1);

DESC t1;
+-------+------------+------+-----+---------+-------+
| Field | Type       | Null | Key | Default | Extra |
+-------+------------+------+-----+---------+-------+
| x     | tinyint(4) | YES  |     | NULL    |       |
+-------+------------+------+-----+---------+-------+
```

## EXAMPLES

```sql
CREATE TABLE int1_example (
  example INT1
);
```

```sql
SHOW CREATE TABLE int1_example\G
```

```sql
*************************** 1. row ***************************
       Table: int1_example
Create Table: CREATE TABLE `int1_example` (
  `example` tinyint(4) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
