---
description: >-
  Checks if geometry A contains geometry B. Returns 1 if B is completely inside
  A, 0 otherwise.
---

# ST\_CONTAINS

## Syntax

```sql
ST_CONTAINS(g1,g2)
```

## Description

Returns `1` or `0` to indicate whether a geometry `g1` completely contains geometry `g2`.

ST\_CONTAINS() uses object shapes, while [CONTAINS()](contains.md), based on the original MySQL implementation, uses object bounding rectangles.

ST\_CONTAINS tests the opposite relationship to [ST\_WITHIN()](st-within.md).

## Examples

```sql
SET @g1 = ST_GEOMFROMTEXT('POLYGON((175 150, 20 40, 50 60, 125 100, 175 150))');

SET @g2 = ST_GEOMFROMTEXT('POINT(174 149)');

SELECT ST_CONTAINS(@g1,@g2);
+----------------------+
| ST_CONTAINS(@g1,@g2) |
+----------------------+
|                    1 |
+----------------------+

SET @g2 = ST_GEOMFROMTEXT('POINT(175 151)');

SELECT ST_CONTAINS(@g1,@g2);
+----------------------+
| ST_CONTAINS(@g1,@g2) |
+----------------------+
|                    0 |
+----------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
