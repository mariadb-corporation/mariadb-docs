---
description: >-
  Checks whether a geometry is simple, with no self-intersections or repeated
  points. Returns 1 if it is simple, 0 if not, and NULL for a NULL argument.
---

# ST\_IsSimple

## Syntax

```bnf
ST_IsSimple(g)
IsSimple(g)
```

## Description

Returns 1 if the geometry `g` is simple, 0 if it is not, and `NULL` if `g` is `NULL`.

A geometry is simple if it has no anomalous geometric points, such as self-intersections or self-tangency:

* A `POINT` is always simple.
* A `LINESTRING` is simple if it does not cross or touch itself. A closed `LINESTRING`, whose first and last points are the same, is simple if it does not touch itself anywhere else.
* A `MULTIPOINT` is simple if no two of its points are the same.

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

A LINESTRING that crosses itself is not simple:

```sql
SET @g = 'LineString(0 0,1 1,0 1,1 0)';

SELECT ST_ISSIMPLE(ST_GEOMFROMTEXT(@g));
+----------------------------------+
| ST_ISSIMPLE(ST_GEOMFROMTEXT(@g)) |
+----------------------------------+
|                                0 |
+----------------------------------+
```

A closed LINESTRING that does not cross itself is simple:

```sql
SET @g = 'LineString(0 0,1 0,1 1,0 0)';

SELECT ST_ISSIMPLE(ST_GEOMFROMTEXT(@g));
+----------------------------------+
| ST_ISSIMPLE(ST_GEOMFROMTEXT(@g)) |
+----------------------------------+
|                                1 |
+----------------------------------+
```

A MULTIPOINT with a repeated point is not simple:

```sql
SET @g = 'MultiPoint(0 0,0 0)';

SELECT ST_ISSIMPLE(ST_GEOMFROMTEXT(@g));
+----------------------------------+
| ST_ISSIMPLE(ST_GEOMFROMTEXT(@g)) |
+----------------------------------+
|                                0 |
+----------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
