---
description: >-
  Synonym for ST_OVERLAPS. Checks if two geometries overlap, sharing some but
  not all points, and having the same dimension.
---

# OVERLAPS

## Syntax

```sql
OVERLAPS(g1,g2)
```

## Description

Returns `1` or `0` to indicate whether `g1` spatially overlaps `g2`.\
The term spatially overlaps is used if two geometries of equal dimensions intersect and their intersection results in a geometry of the same dimension but not equal to either of the given geometries.

`OVERLAPS()` is based on the original MySQL implementation and uses object bounding rectangles, while [ST\_OVERLAPS()](st-overlaps.md) uses object shapes.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
