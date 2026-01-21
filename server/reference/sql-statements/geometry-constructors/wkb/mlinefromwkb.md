---
description: >-
  Synonym for ST_MultiLineStringFromWKB. Constructs a MultiLineString value from
  its WKB representation and an optional SRID.
---

# MLineFromWKB

## Syntax

```sql
MLineFromWKB(wkb[,srid])
MultiLineStringFromWKB(wkb[,srid])
```

## Description

Constructs a [MULTILINESTRING](../geometry-constructors/multilinestring.md) value using its [WKB](well-known-binary-wkb-format.md) representation and [SRID](../geometry-properties/st_srid.md).

`MLineFromWKB()` and `MultiLineStringFromWKB()` are synonyms.

## Examples

```sql
SET @g = ST_AsBinary(MLineFromText('MULTILINESTRING((10 48,10 21,10 0),(16 0,16 23,16 48))'));

SELECT ST_AsText(MLineFromWKB(@g));
+--------------------------------------------------------+
| ST_AsText(MLineFromWKB(@g))                            |
+--------------------------------------------------------+
| MULTILINESTRING((10 48,10 21,10 0),(16 0,16 23,16 48)) |
+--------------------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
