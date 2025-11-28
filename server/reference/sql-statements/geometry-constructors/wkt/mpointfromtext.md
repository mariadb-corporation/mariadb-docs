---
description: >-
  Synonym for ST_MultiPointFromText. Constructs a MultiPoint value from its WKT
  representation and an optional SRID.
---

# MPointFromText

## Syntax

```sql
MPointFromText(wkt[,srid])
MultiPointFromText(wkt[,srid])
```

## Description

Constructs a [MULTIPOINT](../geometry-constructors/multipoint.md) value using its [WKT](wkt-definition.md) representation and [SRID](../geometry-properties/st_srid.md).

`MPointFromText()` and `MultiPointFromText()` are synonyms.

## Examples

```sql
CREATE TABLE gis_multi_point (g MULTIPOINT);
SHOW FIELDS FROM gis_multi_point;
INSERT INTO gis_multi_point VALUES
    (MultiPointFromText('MULTIPOINT(0 0,10 10,10 20,20 20)')),
    (MPointFromText('MULTIPOINT(1 1,11 11,11 21,21 21)')),
    (MPointFromWKB(AsWKB(MultiPoint(Point(3, 6), Point(4, 10)))));
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
