---
description: >-
  Discover JSON_OVERLAPS in MariaDB. Available from version 10.9, this function
  compares two JSON documents, returning true if they share at least one common
  key-value pair, array element, or scalar val
---

# JSON\_OVERLAPS

{% hint style="info" %}
`JSON_OVERLAPS` is available from MariaDB 10.9.
{% endhint %}

## Syntax

```sql
JSON_OVERLAPS(json_doc1, json_doc2)
```

## Description

`JSON_OVERLAPS()` compares two json documents and returns true if they have at least one common\
key-value pair between two objects, array element common between two arrays, or array element common with scalar if one of the arguments is a scalar and other is an array. If two json documents are scalars, it returns true if they have same type and value.

If none of the above conditions are satisfied then it returns false.

## Examples

```sql
SELECT JSON_OVERLAPS('false', 'false');
+---------------------------------+
| JSON_OVERLAPS('false', 'false') |
+---------------------------------+
| 1                               |
+---------------------------------+

SELECT JSON_OVERLAPS('true', '["abc", 1, 2, true, false]');
+----------------------------------------------------+
| JSON_OVERLAPS('true','["abc", 1, 2, true, false]') |
+----------------------------------------------------+
| 1                                                  |
+----------------------------------------------------+

SELECT JSON_OVERLAPS('{"A": 1, "B": {"C":2}}', '{"A": 2, "B": {"C":2}}') AS is_overlap;
+---------------------+
| is_overlap          |
+---------------------+
| 1                   |
+---------------------+
```

Partial match is considered as no-match.

## Examples

```sql
SELECT JSON_OVERLAPS('[1, 2, true, false, null]', '[3, 4, [1]]') AS is_overlap;
+--------------------- +
| is_overlap           |
+----------------------+
| 0                    |
+----------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
