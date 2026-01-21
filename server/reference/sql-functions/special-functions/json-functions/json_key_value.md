---
description: >-
  Explore JSON_KEY_VALUE in MariaDB. Available from version 11.2, this function
  extracts key/value pairs from a JSON object, enabling easier data
  transformation and usage with JSON_TABLE.
---

# JSON\_KEY\_VALUE

{% hint style="info" %}
JSON\_KEY\_VALUE is available from MariaDB 11.2.
{% endhint %}

## Syntax

```sql
JSON_KEY_VALUE(obj, json_path)
```

## Description

`JSON_KEY_VALUE` extracts key/value pairs from a JSON object. The JSON path parameter is used to only return key/value pairs for matching JSON objects.

## Example

```sql
SELECT JSON_KEY_VALUE('[[1, {"key1":"val1", "key2":"val2"}, 3], 2, 3]', '$[0][1]');
+-----------------------------------------------------------------------------+
| JSON_KEY_VALUE('[[1, {"key1":"val1", "key2":"val2"}, 3], 2, 3]', '$[0][1]') |
+-----------------------------------------------------------------------------+
| [{"key": "key1", "value": "val1"}, {"key": "key2", "value": "val2"}]        |
+-----------------------------------------------------------------------------+
```

`JSON_KEY_VALUE()` can be used as an argument to JSON\_TABLE(), which allows adding the key to a result set.

```sql
SELECT jt.* FROM JSON_TABLE(
JSON_KEY_VALUE('[[1, {"key1":"val1", "key2":"val2"}, 3], 2, 3]', '$[0][1]'),'$[*]'
COLUMNS (
k VARCHAR(20) PATH '$.key',
v VARCHAR(20) PATH '$.value',
id FOR ORDINALITY )) AS jt;
+------+------+------+
| k    | v    | id   |
+------+------+------+
| key1 | val1 |    1 |
| key2 | val2 |    2 |
+------+------+------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
