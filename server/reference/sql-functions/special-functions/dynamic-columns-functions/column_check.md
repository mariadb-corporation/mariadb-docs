---
description: >-
  Verify dynamic column integrity. This function checks if a blob containing
  dynamic columns is valid and returns 1 if it is, 0 otherwise.
---

# COLUMN\_CHECK

## Syntax

```sql
COLUMN_CHECK(dyncol_blob);
```

## Description

Check if `dyncol_blob` is a valid packed dynamic columns blob. Return value of 1 means the blob is valid, return value of 0 means it is not.

**Rationale:**\
Normally, one works with valid dynamic column blobs. Functions like [COLUMN\_CREATE](column_create.md), [COLUMN\_ADD](column_add.md), [COLUMN\_DELETE](column_delete.md) always return valid dynamic column blobs. However, if a dynamic column blob is accidentally truncated, or transcoded from one character set to another, it will be corrupted. This function can be used to check if a value in a blob field is a valid dynamic column blob.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
