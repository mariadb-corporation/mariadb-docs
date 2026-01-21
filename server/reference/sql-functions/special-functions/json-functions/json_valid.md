---
description: >-
  Check if a value is valid JSON. This function returns 1 if the argument is a
  valid JSON document, and 0 otherwise.
---

# JSON\_VALID

## Syntax

```sql
JSON_VALID(value)
```

## Description

Indicates whether the given value is a valid JSON document or not. Returns `1` if valid, `0` if not, and `NULL` if the argument is `NULL`.

{% tabs %}
{% tab title="Current" %}
The `JSON_VALID` function is automatically used as a [CHECK constraint](../../../sql-statements/data-definition/constraint.md#check-constraints) for the [JSON data type alias](../../../data-types/string-data-types/json.md) in order to ensure that a valid json document is inserted.
{% endtab %}

{% tab title="< 10.4.3" %}
The `JSON_VALID` function is **not** automatically used as a [CHECK constraint](../../../sql-statements/data-definition/constraint.md#check-constraints) for the [JSON data type alias](../../../data-types/string-data-types/json.md).
{% endtab %}
{% endtabs %}

## Examples

```sql
SELECT JSON_VALID('{"id": 1, "name": "Monty"}');
+------------------------------------------+
| JSON_VALID('{"id": 1, "name": "Monty"}') |
+------------------------------------------+
|                                        1 |
+------------------------------------------+

SELECT JSON_VALID('{"id": 1, "name": "Monty", "oddfield"}');
+------------------------------------------------------+
| JSON_VALID('{"id": 1, "name": "Monty", "oddfield"}') |
+------------------------------------------------------+
|                                                    0 |
+------------------------------------------------------+
```

## See Also

* [JSON video tutorial](https://www.youtube.com/watch?v=sLE7jPETp8g) covering JSON\_VALID.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
