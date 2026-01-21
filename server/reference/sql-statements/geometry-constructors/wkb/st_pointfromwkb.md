---
description: Constructs a Point value using its WKB representation and an optional SRID.
---

# ST\_PointFromWKB

## Syntax

```sql
ST_PointFromWKB(wkb[,srid])
PointFromWKB(wkb[,srid])
```

## Description

Constructs a [POINT](../geometry-constructors/point.md) value using its [WKB](well-known-binary-wkb-format.md) representation and [SRID](../geometry-properties/st_srid.md).

`ST_PointFromWKB()` and `PointFromWKB()` are synonyms.

## Examples

```sql
SET @g = ST_AsBinary(ST_PointFromText('POINT(0 4)'));

SELECT ST_AsText(ST_PointFromWKB(@g)) AS p;
+------------+
| p          |
+------------+
| POINT(0 4) |
+------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
