---
description: >-
  Explore JSON_ARRAY_APPEND in MariaDB. This function appends values to the end
  of specified arrays within a JSON document, returning the modified result.
---

# JSON\_ARRAY\_APPEND

## Syntax

```sql
JSON_ARRAY_APPEND(json_doc, path, value[, path, value] ...)
```

## Description

Appends values to the end of the specified arrays within a JSON document, returning the result, or `NULL` if any of the arguments are `NULL`.

Evaluation is performed from left to right, with the resulting document from the previous pair becoming the new value against which the next pair is evaluated.

If the `json_doc` is not a valid JSON document, or if any of the paths are not valid, or contain a `*` or `**` wildcard, an error is returned.

## Examples

```sql
SET @json = '[1, 2, [3, 4]]';

SELECT JSON_ARRAY_APPEND(@json, '$[0]', 5)
+-------------------------------------+
| JSON_ARRAY_APPEND(@json, '$[0]', 5) |
+-------------------------------------+
| [[1, 5], 2, [3, 4]]                 |
+-------------------------------------+

SELECT JSON_ARRAY_APPEND(@json, '$[1]', 6);
+-------------------------------------+
| JSON_ARRAY_APPEND(@json, '$[1]', 6) |
+-------------------------------------+
| [1, [2, 6], [3, 4]]                 |
+-------------------------------------+

SELECT JSON_ARRAY_APPEND(@json, '$[1]', 6, '$[2]', 7);
+------------------------------------------------+
| JSON_ARRAY_APPEND(@json, '$[1]', 6, '$[2]', 7) |
+------------------------------------------------+
| [1, [2, 6], [3, 4, 7]]                         |
+------------------------------------------------+

SELECT JSON_ARRAY_APPEND(@json, '$', 5);
+----------------------------------+
| JSON_ARRAY_APPEND(@json, '$', 5) |
+----------------------------------+
| [1, 2, [3, 4], 5]                |
+----------------------------------+

SET @json = '{"A": 1, "B": [2], "C": [3, 4]}';

SELECT JSON_ARRAY_APPEND(@json, '$.B', 5);
+------------------------------------+
| JSON_ARRAY_APPEND(@json, '$.B', 5) |
+------------------------------------+
| {"A": 1, "B": [2, 5], "C": [3, 4]} |
+------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
