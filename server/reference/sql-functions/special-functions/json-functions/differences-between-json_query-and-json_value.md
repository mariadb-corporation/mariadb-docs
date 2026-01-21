---
description: >-
  Learn the difference between JSON_QUERY and JSON_VALUE in MariaDB. JSON_QUERY
  returns objects or arrays, while JSON_VALUE extracts scalar values.
---

# Differences between JSON\_QUERY and JSON\_VALUE

The primary difference between the two functions is that _JSON\_QUERY_ returns an object or an array, while _JSON\_VALUE_ returns a scalar.

Take the following JSON document as an example:

```sql
SET @json='{ "x": [0,1], "y": "[0,1]", "z": "Monty" }';
```

Note that data member "x" is an array, and data members "y" and "z" are strings. The following examples demonstrate the differences between the two functions.

```sql
SELECT JSON_QUERY(@json,'$'), JSON_VALUE(@json,'$');
+--------------------------------------------+-----------------------+
| JSON_QUERY(@json,'$')                      | JSON_VALUE(@json,'$') |
+--------------------------------------------+-----------------------+
| { "x": [0,1], "y": "[0,1]", "z": "Monty" } | NULL                  |
+--------------------------------------------+-----------------------+

SELECT JSON_QUERY(@json,'$.x'), JSON_VALUE(@json,'$.x');
+-------------------------+-------------------------+
| JSON_QUERY(@json,'$.x') | JSON_VALUE(@json,'$.x') |
+-------------------------+-------------------------+
| [0,1]                   | NULL                    |
+-------------------------+-------------------------+

SELECT JSON_QUERY(@json,'$.y'), JSON_VALUE(@json,'$.y');
+-------------------------+-------------------------+
| JSON_QUERY(@json,'$.y') | JSON_VALUE(@json,'$.y') |
+-------------------------+-------------------------+
| NULL                    | [0,1]                   |
+-------------------------+-------------------------+

SELECT JSON_QUERY(@json,'$.z'), JSON_VALUE(@json,'$.z');
+-------------------------+-------------------------+
| JSON_QUERY(@json,'$.z') | JSON_VALUE(@json,'$.z') |
+-------------------------+-------------------------+
| NULL                    | Monty                   |
+-------------------------+-------------------------+

SELECT JSON_QUERY(@json,'$.x[0]'), JSON_VALUE(@json,'$.x[0]');
+----------------------------+----------------------------+
| JSON_QUERY(@json,'$.x[0]') | JSON_VALUE(@json,'$.x[0]') |
+----------------------------+----------------------------+
| NULL                       | 0                          |
+----------------------------+----------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
