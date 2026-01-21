---
description: >-
  Learn about the JSON_COMPACT function in MariaDB. This function removes all
  unnecessary whitespace from a JSON document, minimizing its size for efficient
  storage and transmission.
---

# JSON\_COMPACT

## Syntax

```sql
JSON_COMPACT(json_doc)
```

## Description

Removes all unnecessary spaces so the json document is as short as possible.

## Example

```sql
SET @j = '{ "A": 1, "B": [2, 3]}';

SELECT JSON_COMPACT(@j), @j;
+-------------------+------------------------+
| JSON_COMPACT(@j)  | @j                     |
+-------------------+------------------------+
| {"A":1,"B":[2,3]} | { "A": 1, "B": [2, 3]} |
+-------------------+------------------------+
```

## See Also

* [JSON video tutorial](https://www.youtube.com/watch?v=sLE7jPETp8g) covering JSON\_COMPACT.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
