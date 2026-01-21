---
description: >-
  Explore JSON_EXISTS in MariaDB. This function checks whether a specified JSON
  document contains an element at a given path, returning 1 for existence and 0
  otherwise.
---

# JSON\_EXISTS

## Syntax

```sql
JSON_EXISTS(json_doc, json_path)
```

## Description

Determines whether `json_doc` has an element pointed to by path `json_path`. Returns `1` if the element exists, `0` if not, or `NULL` if any of the inputs were `NULL`.

## Examples

```sql
SELECT JSON_EXISTS('{"key1":"xxxx", "key2":[1, 2, 3]}', "$.key2");
+------------------------------------------------------------+
| JSON_EXISTS('{"key1":"xxxx", "key2":[1, 2, 3]}', "$.key2") |
+------------------------------------------------------------+
|                                                          1 |
+------------------------------------------------------------+

SELECT JSON_EXISTS('{"key1":"xxxx", "key2":[1, 2, 3]}', "$.key3");
+------------------------------------------------------------+
| JSON_EXISTS('{"key1":"xxxx", "key2":[1, 2, 3]}', "$.key3") |
+------------------------------------------------------------+
|                                                          0 |
+------------------------------------------------------------+

SELECT JSON_EXISTS('{"key1":"xxxx", "key2":[1, 2, 3]}', "$.key2[1]");
+---------------------------------------------------------------+
| JSON_EXISTS('{"key1":"xxxx", "key2":[1, 2, 3]}', "$.key2[1]") |
+---------------------------------------------------------------+
|                                                             1 |
+---------------------------------------------------------------+

SELECT JSON_EXISTS('{"key1":"xxxx", "key2":[1, 2, 3]}', "$.key2[10]");
+----------------------------------------------------------------+
| JSON_EXISTS('{"key1":"xxxx", "key2":[1, 2, 3]}', "$.key2[10]") |
+----------------------------------------------------------------+
|                                                              0 |
+----------------------------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
