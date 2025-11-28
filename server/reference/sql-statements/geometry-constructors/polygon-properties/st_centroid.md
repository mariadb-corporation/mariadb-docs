---
description: >-
  Returns the centroid of a Polygon or MultiPolygon. The result is a Point
  geometry representing the mathematical center of mass.
---

# ST\_CENTROID

## Syntax

```sql
ST_Centroid(mpoly)
Centroid(mpoly)
```

## Description

Returns a point reflecting the mathematical centroid (geometric center) for the [MultiPolygon](../geometry-constructors/multipolygon.md) _mpoly_. The resulting point will not necessarily be on the MultiPolygon.

`ST_Centroid()` and `Centroid()` are synonyms.

## Examples

```sql
SET @poly = ST_GeomFromText('POLYGON((0 0,20 0,20 20,0 20,0 0))');
SELECT ST_AsText(ST_Centroid(@poly)) AS center;
+--------------+
| center       |
+--------------+
| POINT(10 10) |
+--------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
