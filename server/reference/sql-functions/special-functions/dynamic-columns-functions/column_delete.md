---
description: >-
  Remove dynamic columns. This function deletes specified columns from a dynamic
  column blob and returns the updated blob.
---

# COLUMN\_DELETE

## Syntax

```sql
COLUMN_DELETE(dyncol_blob, column_nr, column_nr...)
COLUMN_DELETE(dyncol_blob, column_name, column_name...)
```

## Description

Deletes a [dynamic column](../../../sql-structure/nosql/dynamic-columns.md) with the specified name. Multiple names can be given. The return value is a dynamic column blob after the modification.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
