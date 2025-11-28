---
description: >-
  Check for a dynamic column. This function returns 1 if a specified column
  exists within a dynamic column blob, and 0 otherwise.
---

# COLUMN\_EXISTS

## Syntax

```sql
COLUMN_EXISTS(dyncol_blob, column_nr)
COLUMN_EXISTS(dyncol_blob, column_name)
```

## Description

Checks if a column with name `column_name` exists in `dyncol_blob`. If yes, return `1`, otherwise return `0`. See [dynamic columns](../../../sql-structure/nosql/dynamic-columns.md) for more information.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
