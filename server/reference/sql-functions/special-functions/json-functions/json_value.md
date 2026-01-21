---
description: >-
  Extract a scalar value from a JSON document. This function extracts a value
  from a JSON document at a given path and returns it as a scalar.
---

# JSON\_VALUE

## Syntax

```sql
JSON_VALUE(json_doc, path)
```

## Description

Given a JSON document, returns the scalar specified by the path. Returns NULL if not given a valid JSON document, or if there is no match.

## Examples

```sql
SELECT json_value('{"key1":123}', '$.key1');
+--------------------------------------+
| json_value('{"key1":123}', '$.key1') |
+--------------------------------------+
| 123                                  |
+--------------------------------------+

SELECT json_value('{"key1": [1,2,3], "key1":123}', '$.key1');
+-------------------------------------------------------+
| json_value('{"key1": [1,2,3], "key1":123}', '$.key1') |
+-------------------------------------------------------+
| 123                                                   |
+-------------------------------------------------------+
```

In the `SET` statement below, two escape characters are needed, as a single escape character would be applied by the SQL parser in the `SET` statement, and the escaped character would not form part of the saved value.

```sql
SET @json = '{"key1":"60\\" Table", "key2":"1"}';

SELECT JSON_VALUE(@json,'$.key1') AS Name , json_value(@json,'$.key2') as ID;
+-----------+------+
| Name      | ID   |
+-----------+------+
| 60" Table | 1    |
+-----------+------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
