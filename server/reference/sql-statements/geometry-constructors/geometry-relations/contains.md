---
description: >-
  Synonym for ST_CONTAINS. Checks if the first geometry completely contains the
  second geometry, with no points of the second geometry outside the first.
---

# CONTAINS

## Syntax

```sql
Contains(g1,g2)
```

## Description

Returns `1` or `0` to indicate whether a geometry `g1` completely contains geometry `g2`. CONTAINS() is based on the original MySQL implementation and uses object bounding rectangles, while [ST\_CONTAINS()](st-contains.md) uses object shapes.

This tests the opposite relationship to [Within()](within.md).

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}

