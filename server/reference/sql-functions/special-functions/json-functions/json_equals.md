---
description: >-
  Discover JSON_EQUALS in MariaDB. This function checks for equality between two
  JSON objects, returning 1 if they are equal, 0 if not, handling key order and
  data types intelligently.
---

# JSON\_EQUALS

{% hint style="info" %}
`JSON_EQUALS` is available from MariaDB 10.7.
{% endhint %}

## Syntax

```sql
JSON_EQUALS(json1, json2)
```

## Description

Checks if there is equality between two json objects. Returns `1` if it there is, `0` if not, or NULL if any of the arguments are null.

## Examples

```sql
SELECT JSON_EQUALS('{"a"   :[1, 2, 3],"b":[4]}', '{"b":[4],"a":[1, 2, 3.0]}');
+------------------------------------------------------------------------+
| JSON_EQUALS('{"a"   :[1, 2, 3],"b":[4]}', '{"b":[4],"a":[1, 2, 3.0]}') |
+------------------------------------------------------------------------+
|                                                                      1 |
+------------------------------------------------------------------------+

SELECT JSON_EQUALS('{"a":[1, 2, 3]}', '{"a":[1, 2, 3.01]}');
+------------------------------------------------------+
| JSON_EQUALS('{"a":[1, 2, 3]}', '{"a":[1, 2, 3.01]}') |
+------------------------------------------------------+
|                                                    0 |
+------------------------------------------------------+
```

## See Also

* [JSON\_NORMALIZE](json_normalize.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
