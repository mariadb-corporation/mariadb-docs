---
description: >-
  Create a JSON object. This function evaluates a list of key-value pairs and
  returns a JSON object containing those pairs.
---

# JSON\_OBJECT

## Syntax

```sql
JSON_OBJECT([key, value[, key, value] ...])
```

## Description

Returns a JSON object containing the given key/value pairs. The key/value list can be empty.

An error will occur if there are an odd number of arguments, or any key name is `NULL`.

## Example

```sql
SELECT JSON_OBJECT("id", 1, "name", "Monty");
+---------------------------------------+
| JSON_OBJECT("id", 1, "name", "Monty") |
+---------------------------------------+
| {"id": 1, "name": "Monty"}            |
+---------------------------------------+
```

## See also

* [JSON\_MAKE\_OBJECT](../../../../server-usage/storage-engines/connect/connect-table-types/connect-json-table-type.md#json_make_object), the CONNECT storage engine function

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
