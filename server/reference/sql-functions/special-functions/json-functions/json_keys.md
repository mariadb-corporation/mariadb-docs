---
description: >-
  Return keys from a JSON object. This function returns the keys from the
  top-level value of a JSON object as a JSON array.
---

# JSON\_KEYS

## Syntax

```sql
JSON_KEYS(json_doc[, path])
```

## Description

Returns the keys as a JSON array from the top-level value of a JSON object or, if the optional path argument is provided, the top-level keys from the path.

Excludes keys from nested sub-objects in the top level value. The resulting array will be empty if the selected object is empty.

Returns `NULL` if any of the arguments are null, a given path does not locate an object, or if the json\_doc argument is not an object.

An error will occur if JSON document is invalid, the path is invalid or if the path contains a `*` or `**` wildcard.

## Examples

```sql
SELECT JSON_KEYS('{"A": 1, "B": {"C": 2}}');
+--------------------------------------+
| JSON_KEYS('{"A": 1, "B": {"C": 2}}') |
+--------------------------------------+
| ["A", "B"]                           |
+--------------------------------------+

SELECT JSON_KEYS('{"A": 1, "B": 2, "C": {"D": 3}}', '$.C');
+-----------------------------------------------------+
| JSON_KEYS('{"A": 1, "B": 2, "C": {"D": 3}}', '$.C') |
+-----------------------------------------------------+
| ["D"]                                               |
+-----------------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
