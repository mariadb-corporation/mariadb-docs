---
description: >-
  Insert or update data in a JSON document. This function inserts or updates
  data in a JSON document at a specified path and returns the result.
---

# JSON\_SET

## Syntax

```sql
JSON_SET(json_doc, path, val[, path, val] ...)
```

## Description

Updates or inserts data into a JSON document, returning the result, or `NULL` if any of the arguments are `NULL` or the optional path fails to find an object.

An error will occur if the JSON document is invalid, the path is invalid or if the path contains a `*` or a wildcard\*\*.\*\*

`JSON_SET` can update or insert data, while [JSON\_REPLACE](json_replace.md) can only update, and [JSON\_INSERT](json_insert.md) only insert.

## Examples

```sql
SELECT JSON_SET(Priv, '$.locked', 'true') FROM mysql.global_priv
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
