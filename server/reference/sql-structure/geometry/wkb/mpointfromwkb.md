# MPointFromWKB

## Syntax

```bnf
MPointFromWKB(wkb[,srid])
MultiPointFromWKB(wkb[,srid])
```

## Description

Constructs a [MULTIPOINT](../../../sql-statements/geometry-constructors/geometry-constructors/multipoint.md) value using its [WKB](well-known-binary-wkb-format.md) representation and [SRID](../geometry-properties/st_srid.md).

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

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
