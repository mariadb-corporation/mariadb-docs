---
description: >-
  Access the unique row identifier. This pseudo column often aliases the primary
  key, allowing direct row access even if the primary key column name is
  unknown.
---

# \_rowid

## Syntax

```sql
_rowid
```

## Description

The `_rowid` pseudo column is mapped to the primary key in the related table. This can be used as a replacement of the `rowid` pseudo column in other databases. Another usage is to simplify sql queries as one doesn't have to know the name of the primary key.

## Examples

```sql
CREATE TABLE t1 (a INT PRIMARY KEY, b VARCHAR(80));
INSERT INTO t1 VALUES (1,"one"),(2,"two");
SELECT * FROM t1 WHERE _rowid=1;
```

```
+---+------+
| a | b    |
+---+------+
| 1 | one  |
+---+------+
```

```sql
UPDATE t1 SET b="three" WHERE _rowid=2;
SELECT * FROM t1 WHERE _rowid>=1 AND _rowid<=10;
```

```
+---+-------+
| a | b     |
+---+-------+
| 1 | one   |
| 2 | three |
+---+-------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
