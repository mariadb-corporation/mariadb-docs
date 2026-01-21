---
description: >-
  This function inserts values into a JSON document at a specified path,
  returning the modified document, and supports evaluating multiple path-value
  pairs sequentially.
---

# JSON\_ARRAY\_INSERT

## Syntax

```sql
JSON_ARRAY_INSERT(json_doc, path, value[, path, value] ...)
```

## Description

Inserts a value into a JSON document, returning the modified document, or `NULL` if any of the arguments are `NULL`.

Evaluation is performed from left to right, with the resulting document from the previous pair becoming the new value against which the next pair is evaluated.

If the `json_doc` is not a valid JSON document, or if any of the paths are not valid, or contain a `*` or `**` wildcard, an error is returned.

## Examples

```sql
SET @json = '[1, 2, [3, 4]]';

SELECT JSON_ARRAY_INSERT(@json, '$[0]', 5);
+-------------------------------------+
| JSON_ARRAY_INSERT(@json, '$[0]', 5) |
+-------------------------------------+
| [5, 1, 2, [3, 4]]                   |
+-------------------------------------+

SELECT JSON_ARRAY_INSERT(@json, '$[1]', 6);
+-------------------------------------+
| JSON_ARRAY_INSERT(@json, '$[1]', 6) |
+-------------------------------------+
| [1, 6, 2, [3, 4]]                   |
+-------------------------------------+

SELECT JSON_ARRAY_INSERT(@json, '$[1]', 6, '$[2]', 7);
+------------------------------------------------+
| JSON_ARRAY_INSERT(@json, '$[1]', 6, '$[2]', 7) |
+------------------------------------------------+
| [1, 6, 7, 2, [3, 4]]                           |
+------------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
