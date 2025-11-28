---
description: >-
  Returns a geometry representing the difference between two geometries. The
  result contains points from the first geometry that are not in the second.
---

# ST\_EQUALS

## Syntax

```sql
ST_EQUALS(g1,g2)
```

## Description

Returns `1` or `0` to indicate whether geometry _`g1`_ is spatially equal to geometry _`g2`_.

`ST_EQUALS()` uses object shapes, while [EQUALS()](equals.md), based on the original MySQL implementation, uses object bounding rectangles.

## Examples

```sql
SET @g1 = ST_GEOMFROMTEXT('LINESTRING(174 149, 176 151)');

SET @g2 = ST_GEOMFROMTEXT('LINESTRING(176 151, 174 149)');

SELECT ST_EQUALS(@g1,@g2);
+--------------------+
| ST_EQUALS(@g1,@g2) |
+--------------------+
|                  1 |
+--------------------+
```

```sql
SET @g1 = ST_GEOMFROMTEXT('POINT(0 2)');

SET @g1 = ST_GEOMFROMTEXT('POINT(2 0)');

SELECT ST_EQUALS(@g1,@g2);
+--------------------+
| ST_EQUALS(@g1,@g2) |
+--------------------+
|                  0 |
+--------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
