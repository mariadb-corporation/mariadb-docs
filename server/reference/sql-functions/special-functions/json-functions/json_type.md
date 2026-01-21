---
description: >-
  Return the type of a JSON value. This function returns a string indicating the
  type of a JSON value (e.g., OBJECT, ARRAY, INTEGER).
---

# JSON\_TYPE

## Syntax

```sql
JSON_TYPE(json_val)
```

## Description

Returns the type of a JSON value (as a string), or `NULL` if the argument is null.

An error will occur if the argument is an invalid JSON value.

The following is a complete list of the possible return types:

| Return type | Value                                                                                         | Example                   |
| ----------- | --------------------------------------------------------------------------------------------- | ------------------------- |
| ARRAY       | JSON array                                                                                    | \[1, 2, {"key": "value"}] |
| OBJECT      | JSON object                                                                                   | {"key":"value"}           |
| BOOLEAN     | JSON true/false literals                                                                      | true, false               |
| DOUBLE      | A number with at least one floating point decimal.                                            | 1.2                       |
| INTEGER     | A number without a floating point decimal.                                                    | 1                         |
| NULL        | JSON null literal (this is returned as a string, not to be confused with the SQL NULL value!) | null                      |
| STRING      | JSON String                                                                                   | "a sample string"         |

## Examples

```sql
SELECT JSON_TYPE('{"A": 1, "B": 2, "C": 3}');
+---------------------------------------+
| JSON_TYPE('{"A": 1, "B": 2, "C": 3}') |
+---------------------------------------+
| OBJECT                                |
+---------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
