# TOUCHES

## Syntax

```bnf
Touches(g1,g2)
```

## Description

Returns `1` or `0` to indicate whether `g1` spatially touches `g2`. Two\
geometries spatially touch if the interiors of the geometries do not intersect,\
but the boundary of one of the geometries intersects either the boundary or the\
interior of the other.

TOUCHES() is based on the original MySQL implementation and uses object bounding rectangles, while [ST\_TOUCHES()](st-touches.md) uses object shapes.

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
