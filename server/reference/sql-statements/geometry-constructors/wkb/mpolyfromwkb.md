---
description: >-
  Synonym for ST_MultiPolygonFromWKB. Constructs a MultiPolygon value from its
  WKB representation and an optional SRID.
---

# MPolyFromWKB

## Syntax

```sql
MPolyFromWKB(wkb[,srid])
MultiPolygonFromWKB(wkb[,srid])
```

## Description

Constructs a [MULTIPOLYGON](../geometry-constructors/multipolygon.md) value using its [WKB](well-known-binary-wkb-format.md) representation and [SRID](../geometry-properties/st_srid.md).

`MPolyFromWKB()` and `MultiPolygonFromWKB()` are synonyms.

## Examples

```sql
SET @g = ST_AsBinary(MPointFromText('MULTIPOLYGON(((28 26,28 0,84 0,84 42,28 26),(52 18,66 23,73 9,48 6,52 18)),((59 18,67 18,67 13,59 13,59 18)))'));

SELECT ST_AsText(MPolyFromWKB(@g))\G
*************************** 1. row ***************************
ST_AsText(MPolyFromWKB(@g)): MULTIPOLYGON(((28 26,28 0,84 0,84 42,28 26),(52 18,66 23,73 9,48 6,52 18)),((59 18,67 18,67 13,59 13,59 18)))
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
