---
description: >-
  Return a single value. A scalar subquery produces a one-row, one-column result
  that can be used anywhere a constant or expression is valid.
---

# Scalar Subqueries

A scalar subquery is a [subquery](./) that returns a single value. This is the simplest form of a subquery, and can be used in most places a literal or single column value is valid.

The data type, length and [character set and collation](../../../../../data-types/string-data-types/character-sets/) are all taken from the result returned by the subquery. The result of a subquery can always be NULL, that is, no result returned. Even if the original value is defined as NOT NULL, this is disregarded.

A subquery cannot be used where only a literal is expected, for example [LOAD DATA INFILE](../../../inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) expects a literal string containing the file name, and LIMIT requires a literal integer.

## Examples

```sql
CREATE TABLE sq1 (num TINYINT);

CREATE TABLE sq2 (num TINYINT);

INSERT INTO sq1 VALUES (1);

INSERT INTO sq2 VALUES (10* (SELECT num FROM sq1));

SELECT * FROM sq2;
+------+
| num  |
+------+
|   10 |
+------+
```

Inserting a second row means the subquery is no longer a scalar, and this particular query is not valid:

```sql
INSERT INTO sq1 VALUES (2);

INSERT INTO sq2 VALUES (10* (SELECT num FROM sq1));
ERROR 1242 (21000): Subquery returns more than 1 row
```

No rows in the subquery, so the scalar is NULL:

```sql
INSERT INTO sq2 VALUES (10* (SELECT num FROM sq3 WHERE num='3'));

SELECT * FROM sq2;
+------+
| num  |
+------+
|   10 |
| NULL |
+------+
```

A more traditional scalar subquery, as part of a `WHERE` clause:

```sql
SELECT * FROM sq1 WHERE num = (SELECT MAX(num)/10 FROM sq2); 
+------+
| num  |
+------+
|    1 |
+------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
