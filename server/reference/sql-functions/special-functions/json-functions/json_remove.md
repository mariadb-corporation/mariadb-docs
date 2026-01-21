---
description: >-
  Remove data from a JSON document. This function removes data from a JSON
  document at a specified path and returns the result.
---

# JSON\_REMOVE

## Syntax

```sql
JSON_REMOVE(json_doc, path[, path] ...)
```

## Description

Removes data from a JSON document returning the result, or `NULL` if any of the arguments are null. If the element does not exist in the document, no changes are made.

The function returns `NULL` and throws a warning if the JSON document is invalid, the path is invalid, contains a range, or contains a `*` or `**` wildcard.

Path arguments are evaluated from left to right, with the result from the earlier evaluation being used as the value for the next.

## Examples

```sql
SELECT JSON_REMOVE('{"A": 1, "B": 2, "C": {"D": 3}}', '$.C');
+-------------------------------------------------------+
| JSON_REMOVE('{"A": 1, "B": 2, "C": {"D": 3}}', '$.C') |
+-------------------------------------------------------+
| {"A": 1, "B": 2}                                      |
+-------------------------------------------------------+

SELECT JSON_REMOVE('["A", "B", ["C", "D"], "E"]', '$[1]');
+----------------------------------------------------+
| JSON_REMOVE('["A", "B", ["C", "D"], "E"]', '$[1]') |
+----------------------------------------------------+
| ["A", ["C", "D"], "E"]                             |
+----------------------------------------------------+
```

## See Also

* [JSON video tutorial](https://www.youtube.com/watch?v=sLE7jPETp8g) covering JSON\_REMOVE.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
