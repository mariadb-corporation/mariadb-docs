# DISJOINT

## Syntax

```bnf
Disjoint(g1,g2)
```

## Description

Returns `1` or `0` to indicate whether `g1` is spatially disjoint from\
(does not intersect) `g2`.

DISJOINT() tests the opposite relationship to [INTERSECTS()](intersects.md).

DISJOINT() is based on the original MySQL implementation and uses object bounding rectangles, while [ST\_DISJOINT()](st_disjoint.md) uses object shapes.

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
