---
description: >-
  Synonym for ST_DISJOINT. Checks if two geometries are disjoint, meaning they
  have no points in common.
---

# DISJOINT

## Syntax

```sql
Disjoint(g1,g2)
```

## Description

Returns `1` or `0` to indicate whether `g1` is spatially disjoint from (does not intersect) `g2`.

`DISJOINT()` tests the opposite relationship to [INTERSECTS()](intersects.md).

`DISJOINT()` is based on the original MySQL implementation and uses object bounding rectangles, while [ST\_DISJOINT()](st_disjoint.md) uses object shapes.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
