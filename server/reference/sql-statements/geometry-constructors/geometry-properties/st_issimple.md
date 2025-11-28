---
description: >-
  Checks if the geometry is simple (no self-intersections or anomalous points).
  Returns 1 if simple, 0 otherwise.
---

# ST\_IsSimple

## Syntax

```sql
ST_IsSimple(g)
IsSimple(g)
```

## Description

Returns true if the given Geometry has no anomalous geometric points, false if it does, or NULL if given a NULL value.

ST\_IsSimple() and IsSimple() are synonyms.

## Examples

A POINT is always simple.

```sql
SET @g = 'Point(1 2)';

SELECT ST_ISSIMPLE(GEOMFROMTEXT(@g));
+-------------------------------+
| ST_ISSIMPLE(GEOMFROMTEXT(@g)) |
+-------------------------------+
|                             1 |
+-------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
