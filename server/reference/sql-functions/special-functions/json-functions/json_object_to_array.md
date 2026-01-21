---
description: >-
  Explore JSON_OBJECT_TO_ARRAY in MariaDB. Available from version 11.2, this
  function converts JSON objects into arrays of key-value pairs, facilitating
  operations like finding common values when used w
---

# JSON\_OBJECT\_TO\_ARRAY

{% hint style="info" %}
JSON\_OBJECT\_TO\_ARRAY is available from MariaDB 11.2.
{% endhint %}

## Syntax

```sql
JSON_OBJECT_TO_ARRAY(Obj)
```

## Description

It is used to convert all JSON objects found in a JSON document to JSON arrays where each item in the outer array represents a single key-value pair from the object. It is used when we want not just common keys, but also common values. It can be used in conjunction with `JSON_ARRAY_INTERSECT()`.

## Examples

```sql
SET @obj1= '{ "a": [1, 2, 3], "b": { "key1":"val1", "key2": {"key3":"val3"} }}';

SELECT JSON_OBJECT_TO_ARRAY(@obj1);
+-----------------------------------------------------------------------+
| JSON_OBJECT_TO_ARRAY(@obj1)                                           |
+-----------------------------------------------------------------------+
| [["a", [1, 2, 3]], ["b", {"key1": "val1", "key2": {"key3": "val3"}}]] |
+-----------------------------------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
