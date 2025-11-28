---
description: >-
  Synonym for ST_MultiLineStringFromText. Constructs a MultiLineString value
  from its WKT representation and an optional SRID.
---

# MLineFromText

## Syntax

```sql
MLineFromText(wkt[,srid])
MultiLineStringFromText(wkt[,srid])
```

## Description

Constructs a [MULTILINESTRING](../geometry-constructors/multilinestring.md) value using its [WKT](wkt-definition.md) representation and [SRID](../geometry-properties/st_srid.md).

`MLineFromText()` and `MultiLineStringFromText()` are synonyms.

## Examples

```sql
CREATE TABLE gis_multi_line (g MULTILINESTRING);
SHOW FIELDS FROM gis_multi_line;
INSERT INTO gis_multi_line VALUES
    (MultiLineStringFromText('MULTILINESTRING((10 48,10 21,10 0),(16 0,16 23,16 48))')),
    (MLineFromText('MULTILINESTRING((10 48,10 21,10 0))')),
    (MLineFromWKB(AsWKB(MultiLineString(
      LineString(Point(1, 2), Point(3, 5)), 
      LineString(Point(2, 5), Point(5, 8), Point(21, 7))))));
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
