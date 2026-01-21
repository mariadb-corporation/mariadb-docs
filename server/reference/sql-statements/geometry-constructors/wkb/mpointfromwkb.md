---
description: >-
  Synonym for ST_MultiPointFromWKB. Constructs a MultiPoint value from its WKB
  representation and an optional SRID.
---

# MPointFromWKB

## Syntax

```sql
MPointFromWKB(wkb[,srid])
MultiPointFromWKB(wkb[,srid])
```

## Description

Constructs a [MULTIPOINT](../geometry-constructors/multipoint.md) value using its [WKB](well-known-binary-wkb-format.md) representation and [SRID](../geometry-properties/st_srid.md).

`MPointFromWKB()` and `MultiPointFromWKB()` are synonyms.

## Examples

```sql
SET @g = ST_AsBinary(MPointFromText('MultiPoint( 1 1, 2 2, 5 3, 7 2, 9 3, 8 4, 6 6, 6 9, 4 9, 1 5 )'));

SELECT ST_AsText(MPointFromWKB(@g));
+-----------------------------------------------------+
| ST_AsText(MPointFromWKB(@g))                        |
+-----------------------------------------------------+
| MULTIPOINT(1 1,2 2,5 3,7 2,9 3,8 4,6 6,6 9,4 9,1 5) |
+-----------------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
