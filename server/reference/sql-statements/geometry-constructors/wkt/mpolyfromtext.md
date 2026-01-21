---
description: >-
  Synonym for ST_MultiPolygonFromText. Constructs a MultiPolygon value from its
  WKT representation and an optional SRID.
---

# MPolyFromText

## Syntax

```sql
MPolyFromText(wkt[,srid])
MultiPolygonFromText(wkt[,srid])
```

## Description

Constructs a [MULTIPOLYGON](../geometry-constructors/multipolygon.md) value using its [WKT](wkt-definition.md) representation and [SRID](../geometry-properties/st_srid.md).

`MPolyFromText()` and `MultiPolygonFromText()` are synonyms.

## Examples

```sql
CREATE TABLE gis_multi_polygon  (g MULTIPOLYGON);
SHOW FIELDS FROM gis_multi_polygon;
INSERT INTO gis_multi_polygon VALUES
    (MultiPolygonFromText('MULTIPOLYGON(
       ((28 26,28 0,84 0,84 42,28 26),(52 18,66 23,73 9,48 6,52 18)),
       ((59 18,67 18,67 13,59 13,59 18)))')),
    (MPolyFromText('MULTIPOLYGON(
       ((28 26,28 0,84 0,84 42,28 26),(52 18,66 23,73 9,48 6,52 18)),
       ((59 18,67 18,67 13,59 13,59 18)))')),
    (MPolyFromWKB(AsWKB(MultiPolygon(Polygon(
       LineString(Point(0, 3), Point(3, 3), Point(3, 0), Point(0, 3)))))));
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
