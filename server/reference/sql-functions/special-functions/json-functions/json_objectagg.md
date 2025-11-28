---
description: >-
  Aggregate key-value pairs into a JSON object. This function aggregates two
  columns or expressions into a single JSON object.
---

# JSON\_OBJECTAGG

{% hint style="info" %}
`JSON_OBJECTAGG` is available from MariaDB 10.5.
{% endhint %}

## Syntax

```sql
JSON_OBJECTAGG(key, value)
```

## Description

`JSON_OBJECTAGG` returns a JSON object containing key-value pairs. It takes two expressions that evaluate to a single value, or two column names, as arguments, the first used as a key, and the second as a value.

The maximum returned length in bytes is determined by the [group\_concat\_max\_len](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#group_concat_max_len) server system variable.

Returns `NULL` in the case of an error, or if the result contains no rows.

`JSON_OBJECTAGG` cannot currently be used as a [window function](../window-functions/).

## Examples

```sql
SELECT * FROM t1;
+------+-------+
| a    | b     |
+------+-------+
|    1 | Hello |
|    1 | World |
|    2 | This  |
+------+-------+

SELECT JSON_OBJECTAGG(a, b) FROM t1;
+----------------------------------------+
| JSON_OBJECTAGG(a, b)                   |
+----------------------------------------+
| {"1":"Hello", "1":"World", "2":"This"} |
+----------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
