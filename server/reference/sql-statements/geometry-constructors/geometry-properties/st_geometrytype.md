---
description: >-
  Returns the name of the geometry type (e.g., 'POINT', 'LINESTRING', 'POLYGON')
  for the given geometry instance.
---

# ST\_GEOMETRYTYPE

## Syntax

```sql
ST_GeometryType(g)
GeometryType(g)
```

## Description

Returns as a string the name of the geometry type of which the geometry instance `g` is a member. The name corresponds to one of the instantiable Geometry subclasses.

`ST_GeometryType()` and `GeometryType()` are synonyms.

## Examples

```sql
SELECT GeometryType(GeomFromText('POINT(1 1)'));
+------------------------------------------+
| GeometryType(GeomFromText('POINT(1 1)')) |
+------------------------------------------+
| POINT                                    |
+------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
