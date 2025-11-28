---
description: >-
  Constructs a geometry value of any type using its WKT representation and an
  optional SRID.
---

# ST\_GeomFromText

## Syntax

```sql
ST_GeomFromText(wkt[,srid])
ST_GeometryFromText(wkt[,srid])
GeomFromText(wkt[,srid])
GeometryFromText(wkt[,srid])

ST_MultiLineStringFromText(wkt[,srid])
ST_MLineFromText(wkt[,srid])
ST_MPointFromText(wkt[,srid])
ST_MultiPointFromText(wkt[,srid])
```

## Description

Constructs a geometry value of any type using its [WKT](wkt-definition.md) representation and [SRID](../geometry-properties/st_srid.md).

`GeomFromText()`, `GeometryFromText()`, `ST_GeomFromText()`, `ST_GeometryFromText()`, `ST_MultiLineStringFromText`, `ST_MLineFromText`, `ST_MultiPolyFromText` and `ST_MPolygonFromText` are all synonyms.

## Example

```sql
SET @g = ST_GEOMFROMTEXT('POLYGON((1 1,1 5,4 9,6 9,9 3,7 2,1 1))');
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
