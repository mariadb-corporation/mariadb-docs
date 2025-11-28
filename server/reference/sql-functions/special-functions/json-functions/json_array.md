---
description: >-
  Create a JSON array. This function evaluates a list of values and returns a
  JSON array containing those values.
---

# JSON\_ARRAY

## Syntax

```sql
JSON_ARRAY([value[, value2] ...])
```

## Description

Returns a JSON array containing the listed values. The list can be empty.

## Example

```sql
SELECT Json_Array(56, 3.1416, 'My name is "Foo"', NULL);
+--------------------------------------------------+
| Json_Array(56, 3.1416, 'My name is "Foo"', NULL) |
+--------------------------------------------------+
| [56, 3.1416, "My name is \"Foo\"", null]         |
+--------------------------------------------------+
```

## See also

* [JSON\_MAKE\_ARRAY](../../../../server-usage/storage-engines/connect/connect-table-types/connect-json-table-type.md#json_make_array), the CONNECT storage engine function

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
