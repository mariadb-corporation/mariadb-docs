---
description: >-
  Check for a JSON path. This function returns 1 if a specified path exists
  within a JSON document, or 0 if it does not.
---

# JSON\_CONTAINS\_PATH

## Syntax

```sql
JSON_CONTAINS_PATH(json_doc, return_arg, path[, path] ...)
```

## Description

Indicates whether the given JSON document contains data at the specified path or paths. Returns `1` if it does, `0` if not and `NULL` if any of the arguments are null.

The _return\_arg_ can be `one` or `all`:

* `one` - Returns `1` if at least one path exists within the JSON document.
* `all` - Returns `1` only if all paths exist within the JSON document.

## Examples

```sql
SET @json = '{"A": 1, "B": [2], "C": [3, 4]}';

SELECT JSON_CONTAINS_PATH(@json, 'one', '$.A', '$.D');
+------------------------------------------------+
| JSON_CONTAINS_PATH(@json, 'one', '$.A', '$.D') |
+------------------------------------------------+
|                                              1 |
+------------------------------------------------+
1 row in set (0.00 sec)

SELECT JSON_CONTAINS_PATH(@json, 'all', '$.A', '$.D');
+------------------------------------------------+
| JSON_CONTAINS_PATH(@json, 'all', '$.A', '$.D') |
+------------------------------------------------+
|                                              0 |
+------------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
