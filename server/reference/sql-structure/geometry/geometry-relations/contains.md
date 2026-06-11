# CONTAINS

## Syntax

```bnf
Contains(g1,g2)
```

## Description

Returns `1` or `0` to indicate whether a geometry `g1` completely contains geometry `g2`. CONTAINS() is based on the original MySQL implementation and uses object bounding rectangles, while [ST\_CONTAINS()](st-contains.md) uses object shapes.

This tests the opposite relationship to [Within()](within.md).

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
