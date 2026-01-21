---
description: >-
  Returns 1 if the LineString is closed (start and end points are the same), 0
  if not, and NULL if the argument is NULL.
---

# ST\_ISCLOSED

## Syntax

```sql
ST_IsClosed(g)
IsClosed(g)
```

## Description

Returns 1 if a given [LINESTRING's](../geometry-constructors/linestring.md) start and end points are the same, or 0 if they are not the same.

`ST_IsClosed()` and `IsClosed()` are synonyms.

## Examples

```sql
SET @ls = 'LineString(0 0, 0 4, 4 4, 0 0)';
SELECT ST_ISCLOSED(GEOMFROMTEXT(@ls));
+--------------------------------+
| ST_ISCLOSED(GEOMFROMTEXT(@ls)) |
+--------------------------------+
|                              1 |
+--------------------------------+

SET @ls = 'LineString(0 0, 0 4, 4 4, 0 1)';
SELECT ST_ISCLOSED(GEOMFROMTEXT(@ls));
+--------------------------------+
| ST_ISCLOSED(GEOMFROMTEXT(@ls)) |
+--------------------------------+
|                              0 |
+--------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
