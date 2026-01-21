---
description: >-
  Synonym for ST_WITHIN. Checks if the first geometry is completely enclosed by
  the second geometry.
---

# WITHIN

## Syntax

```sql
Within(g1,g2)
```

## Description

Returns `1` or `0` to indicate whether `g1` is spatially within `g2`. This tests the opposite relationship as [Contains()](contains.md).

`WITHIN()` is based on the original MySQL implementation, and uses object bounding rectangles, while [ST\_WITHIN()](st-within.md) uses object shapes.

## Examples

```sql
SET @g1 = GEOMFROMTEXT('POINT(174 149)');
SET @g2 = GEOMFROMTEXT('POINT(176 151)');
SET @g3 = GEOMFROMTEXT('POLYGON((175 150, 20 40, 50 60, 125 100, 175 150))');

SELECT within(@g1,@g3);
+-----------------+
| within(@g1,@g3) |
+-----------------+
|               1 |
+-----------------+

SELECT within(@g2,@g3);
+-----------------+
| within(@g2,@g3) |
+-----------------+
|               0 |
+-----------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
