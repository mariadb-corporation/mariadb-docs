# ST\_PointFromText

## Syntax

```bnf
ST_PointFromText(wkt[,srid])
PointFromText(wkt[,srid])
```

## Description

Constructs a [POINT](../../../sql-statements/geometry-constructors/geometry-constructors/point.md) value using its [WKT](wkt-definition.md) representation and [SRID](../geometry-properties/st_srid.md).

`ST_PointFromText()` and `PointFromText()` are synonyms.

## Examples

```sql
CREATE TABLE gis_point  (g POINT);
SHOW FIELDS FROM gis_point;
INSERT INTO gis_point VALUES
    (PointFromText('POINT(10 10)')),
    (PointFromText('POINT(20 10)')),
    (PointFromText('POINT(20 20)')),
    (PointFromWKB(AsWKB(PointFromText('POINT(10 20)'))));
```

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
