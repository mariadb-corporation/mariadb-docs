---
description: >-
  Constructs a MultiPoint value from a list of WKB Point arguments. It creates a
  geometry collection consisting of multiple individual points.
---

# MULTIPOINT

## Syntax

```sql
MultiPoint(pt1,pt2,...)
```

## Description

Constructs a [WKB](../wkb/) MultiPoint value using WKB [Point](point.md) arguments. If any argument is not a WKB Point, the return value is `NULL`.

## Examples

```sql
SET @g = ST_GEOMFROMTEXT('MultiPoint( 1 1, 2 2, 5 3, 7 2, 9 3, 8 4, 6 6, 6 9, 4 9, 1 5 )');

CREATE TABLE gis_multi_point (g MULTIPOINT);
INSERT INTO gis_multi_point VALUES
    (MultiPointFromText('MULTIPOINT(0 0,10 10,10 20,20 20)')),
    (MPointFromText('MULTIPOINT(1 1,11 11,11 21,21 21)')),
    (MPointFromWKB(AsWKB(MultiPoint(Point(3, 6), Point(4, 10)))));
```

MultiPoint\_Example:

```sql
CREATE TABLE multipoint_example (
  m MULTIPOINT
);
```

```sql
INSERT INTO multipoint_example VALUES
  (ST_MultiPointFromText('MULTIPOINT(0 0, 1 0, 1 1, 0 1)')),
  (ST_MPointFromText('MULTIPOINT(1 1, 2 2, 3 3, 4 4)')),
  (MultiPoint(Point(0, 0), Point(1, 1)));
```

```sql
INSERT INTO multipoint_example VALUES
  (MultiPointFromText('MULTIPOINT(0 0, 1 0, 1 1, 0 1)')),
  (MPointFromText('MULTIPOINT(1 1, 2 2, 3 3, 4 4)')),
  (MultiPoint(Point(0, 0), Point(1, 1)));
```

```sql
SELECT ST_AsWKT(m) FROM multipoint_example;
```

```sql
+-----------------------------+
| ST_AsWKT(m)                 |
+-----------------------------+
| MULTIPOINT(0 0,1 0,1 1,0 1) |
| MULTIPOINT(1 1,2 2,3 3,4 4) |
| MULTIPOINT(0 0,1 1)         |
+-----------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
