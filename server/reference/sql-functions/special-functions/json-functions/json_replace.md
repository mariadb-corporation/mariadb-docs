---
description: >-
  Replace values in a JSON document. This function replaces existing values in a
  JSON document and returns the result.
---

# JSON\_REPLACE

## Syntax

```sql
JSON_REPLACE(json_doc, path, val[, path, val] ...)
```

## Description

Replaces existing values in a JSON document, returning the result, or `NULL` if any of the arguments are `NULL`.

An error will occur if the JSON document is invalid, the path is invalid or if the path contains a `*` or `**` wildcard.

Paths and values are evaluated from left to right, with the result from the earlier evaluation being used as the value for the next.

JSON\_REPLACE can only update data, while [JSON\_INSERT](json_insert.md) can only insert. [JSON\_SET](json_set.md) can update or insert data.

## Examples

```sql
SELECT JSON_REPLACE('{ "A": 1, "B": [2, 3]}', '$.B[1]', 4);
+-----------------------------------------------------+
| JSON_REPLACE('{ "A": 1, "B": [2, 3]}', '$.B[1]', 4) |
+-----------------------------------------------------+
| { "A": 1, "B": [2, 4]}                              |
+-----------------------------------------------------+
```

## See Also

* [JSON video tutorial](https://www.youtube.com/watch?v=sLE7jPETp8g) covering JSON\_REPLACE.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
