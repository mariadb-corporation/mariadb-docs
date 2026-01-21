---
description: >-
  Learn about the JSON_INSERT function in MariaDB. This function inserts new
  data into a JSON document without replacing existing values, returning the
  updated document or NULL.
---

# JSON\_INSERT

## Syntax

```sql
JSON_INSERT(json_doc, path, val[, path, val] ...)
```

## Description

Inserts data into a JSON document, returning the resulting document or `NULL` if either of the _json\_doc_ or _path_ arguments are null.

An error occurs if the JSON document is invalid, or if any of the paths are invalid or contain a `*` or `**` wildcard.

JSON\_INSERT can only insert data, while [JSON\_REPLACE](json_replace.md) can only update. [JSON\_SET](json_set.md) can update or insert data.

## Examples

```sql
SET @json = '{ "A": 0, "B": [1, 2]}';

SELECT JSON_INSERT(@json, '$.C', '[3, 4]');
+--------------------------------------+
| JSON_INSERT(@json, '$.C', '[3, 4]')  |
+--------------------------------------+
| { "A": 0, "B": [1, 2], "C":"[3, 4]"} |
+--------------------------------------+
```

## See Also

* [JSON video tutorial](https://www.youtube.com/watch?v=sLE7jPETp8g) covering JSON\_INSERT.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
