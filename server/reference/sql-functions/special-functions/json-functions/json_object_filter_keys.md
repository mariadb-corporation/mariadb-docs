---
description: >-
  Discover JSON_OBJECT_FILTER_KEYS in MariaDB. Available from version 11.2, this
  function returns a new JSON object containing only the key-value pairs where
  the keys match those provided in a specified
---

# JSON\_OBJECT\_FILTER\_KEYS

{% hint style="info" %}
JSON\_OBJECT\_FILTER\_KEYS is available from MariaDB 11.2.
{% endhint %}

## Syntax

```sql
JSON_OBJECT_FILTER_KEYS(obj, array_keys)
```

## Description

`JSON_OBJECT_FILTER_KEYS` returns a JSON object with keys from the object that are also present in the array as string. It is used when one wants to get key-value pair such that the keys are common but the values may not be common.

## Example

```sql
SET @obj1= '{ "a": 1, "b": 2, "c": 3}';
SET @obj2= '{"b" : 10, "c": 20, "d": 30}';
SELECT JSON_OBJECT_FILTER_KEYS (@obj1, JSON_ARRAY_INTERSECT(JSON_KEYS(@obj1), JSON_KEYS(@obj2)));
+-------------------------------------------------------------------------------------------+
| JSON_OBJECT_FILTER_KEYS (@obj1, JSON_ARRAY_INTERSECT(JSON_KEYS(@obj1), JSON_KEYS(@obj2))) |
+-------------------------------------------------------------------------------------------+
| {"b": 2, "c": 3}                                                                          |
+-------------------------------------------------------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
