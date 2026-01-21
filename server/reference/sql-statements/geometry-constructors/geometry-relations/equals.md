---
description: >-
  Synonym for ST_EQUALS. Checks if two geometries are spatially equal, meaning
  they contain exactly the same point set.
---

# EQUALS

## Syntax

```sql
MBREQUALS(g1,g2)
```

## Description

Returns `1` or `0` to indicate whether _`g1`_ is spatially equal to _`g2`_.

EQUALS() is based on the original MySQL implementation and uses object bounding rectangles, while [ST\_EQUALS()](equals.md) uses object shapes.

`MBREQUALS` is a synonym for `Equals`.

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
