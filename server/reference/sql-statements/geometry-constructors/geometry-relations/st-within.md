---
description: >-
  Checks if geometry A is within geometry B. Returns 1 if A is completely inside
  B, 0 otherwise. This is the inverse of ST_CONTAINS.
---

# ST\_WITHIN

## Syntax

```sql
ST_WITHIN(g1,g2)
```

## Description

Returns `1` or `0` to indicate whether geometry _`g1`_ is spatially within geometry _`g2`_.

This tests the opposite relationship as [ST\_CONTAINS()](st-contains.md).

`ST_WITHIN()` uses object shapes, while [WITHIN()](within.md), based on the original MySQL implementation, uses object bounding rectangles.

## Examples

```sql
SET @g1 = ST_GEOMFROMTEXT('POINT(174 149)');

SET @g2 = ST_GEOMFROMTEXT('POLYGON((175 150, 20 40, 50 60, 125 100, 175 150))');

SELECT ST_WITHIN(@g1,@g2);
+--------------------+
| ST_WITHIN(@g1,@g2) |
+--------------------+
|                  1 |
+--------------------+

SET @g1 = ST_GEOMFROMTEXT('POINT(176 151)');

SELECT ST_WITHIN(@g1,@g2);
+--------------------+
| ST_WITHIN(@g1,@g2) |
+--------------------+
|                  0 |
+--------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
