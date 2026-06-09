# INTERSECTS

## Syntax

```bnf
INTERSECTS(g1,g2)
```

## Description

Returns `1` or `0` to indicate whether geometry _`g1`_ spatially intersects geometry _`g2`_.

INTERSECTS() is based on the original MySQL implementation and uses object bounding rectangles, while [ST\_INTERSECTS()](st-intersects.md) uses object shapes.

INTERSECTS() tests the opposite relationship to [DISJOINT()](disjoint.md).

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
