---
description: >-
  Constructs a Point value using its coordinates. This basic constructor creates
  a point geometry from given X and Y (and optionally Z/M) values.
---

# POINT

## Syntax

```sql
Point(x,y)
```

## Description

Constructs a [WKB](../wkb/) Point using the given coordinates.

## Examples

```sql
SET @g = ST_GEOMFROMTEXT('Point(1 1)');

CREATE TABLE gis_point  (g POINT);
INSERT INTO gis_point VALUES
    (PointFromText('POINT(10 10)')),
    (PointFromText('POINT(20 10)')),
    (PointFromText('POINT(20 20)')),
    (PointFromWKB(AsWKB(PointFromText('POINT(10 20)'))));
```

Point\_Example:

```sql
CREATE TABLE point_example (
  p POINT
);
```

```sql
INSERT INTO point_example VALUES
  (ST_PointFromText('POINT(1 1)')),
  (ST_PointFromText('POINT(2 2)')),
  (Point(3, 3)),
  (Point(4, 4));
```

```sql
SELECT ST_AsWKT(p) FROM point_example;
```

```sql
+-------------+
| ST_AsWKT(p) |
+-------------+
| POINT(1 1)  |
| POINT(2 2)  |
| POINT(3 3)  |
| POINT(4 4)  |
+-------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
