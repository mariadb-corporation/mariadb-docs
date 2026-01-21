---
description: >-
  Returns the Minimum Bounding Rectangle (MBR) for the geometry value. The
  result is returned as a Polygon defined by the corner points.
---

# ST\_ENVELOPE

## Syntax

```sql
ST_ENVELOPE(g)
ENVELOPE(g)
```

## Description

Returns the Minimum Bounding Rectangle (MBR) for the geometry value `g`. The result is returned as a Polygon value.

The polygon is defined by the corner points of the bounding box:

```
POLYGON((MINX MINY, MAXX MINY, MAXX MAXY, MINX MAXY, MINX MINY))
```

`ST_ENVELOPE()` and `ENVELOPE()` are synonyms.

## Examples

```sql
SELECT AsText(ST_ENVELOPE(GeomFromText('LineString(1 1,4 4)')));
+----------------------------------------------------------+
| AsText(ST_ENVELOPE(GeomFromText('LineString(1 1,4 4)'))) |
+----------------------------------------------------------+
| POLYGON((1 1,4 1,4 4,1 4,1 1))                           |
+----------------------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
