---
description: >-
  Discover JSON_LOOSE in MariaDB. This function adds spaces to a JSON document
  to improve its readability, providing a format that is easier for humans to
  scan than compact JSON.
---

# JSON\_LOOSE

## Syntax

```sql
JSON_LOOSE(json_doc)
```

## Description

Adds spaces to a JSON document to make it look more readable.

## Example

```sql
SET @j = '{ "A":1,"B":[2,3]}';

SELECT JSON_LOOSE(@j), @j;
+-----------------------+--------------------+
| JSON_LOOSE(@j)        | @j                 |
+-----------------------+--------------------+
| {"A": 1, "B": [2, 3]} | { "A":1,"B":[2,3]} |
+-----------------------+--------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
