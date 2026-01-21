---
description: >-
  Extract a JSON object or array. This function extracts data from a JSON
  document at a given path, returning a JSON object or array.
---

# JSON\_QUERY

## Syntax

```sql
JSON_QUERY(json_doc, path)
```

## Description

Given a JSON document, returns an object or array specified by the path. Returns `NULL` if not given a valid JSON document, or if there is no match.

## Examples

```sql
SELECT json_query('{"key1":{"a":1, "b":[1,2]}}', '$.key1');
+-----------------------------------------------------+
| json_query('{"key1":{"a":1, "b":[1,2]}}', '$.key1') |
+-----------------------------------------------------+
| {"a":1, "b":[1,2]}                                  |
+-----------------------------------------------------+

SELECT json_query('{"key1":123, "key1": [1,2,3]}', '$.key1');
+-------------------------------------------------------+
| json_query('{"key1":123, "key1": [1,2,3]}', '$.key1') |
+-------------------------------------------------------+
| [1,2,3]                                               |
+-------------------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
