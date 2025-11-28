---
description: >-
  Synonym for ST_LENGTH. Calculates the length of a LineString or
  MultiLineString in its associated spatial reference units.
---

# GLENGTH

## Syntax

```sql
GLength(ls)
```

## Description

Returns as a double-precision number the length of the [LineString](../geometry-constructors/linestring.md) value _`ls`_ in its associated spatial reference.

## Examples

```sql
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT GLength(GeomFromText(@ls));
+----------------------------+
| GLength(GeomFromText(@ls)) |
+----------------------------+
|           2.82842712474619 |
+----------------------------+
```

## See Also

* [ST\_LENGTH()](../geometry-relations/st_length.md) is the OpenGIS equivalent.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
