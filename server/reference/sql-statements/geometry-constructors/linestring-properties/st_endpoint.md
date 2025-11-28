---
description: >-
  Returns the end Point of a LineString. This function retrieves the final
  coordinate in the linear geometry sequence.
---

# ST\_ENDPOINT

## Syntax

```sql
ST_EndPoint(ls)
EndPoint(ls)
```

## Description

Returns the [Point](../geometry-constructors/point.md) that is the endpoint of the [LineString](../geometry-constructors/linestring.md) value `ls`.

`ST_EndPoint()` and `EndPoint()` are synonyms.

## Examples

```sql
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT AsText(EndPoint(GeomFromText(@ls)));
+-------------------------------------+
| AsText(EndPoint(GeomFromText(@ls))) |
+-------------------------------------+
| POINT(3 3)                          |
+-------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
