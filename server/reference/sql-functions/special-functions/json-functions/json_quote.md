---
description: >-
  Quote a string as a JSON value. This function wraps a string with double
  quotes and escapes special characters to create a valid JSON string literal.
---

# JSON\_QUOTE

## Syntax

```sql
JSON_QUOTE(json_value)
```

## Description

Quotes a string as a JSON value, usually for producing valid JSON string literals for inclusion in JSON documents. Wraps the string with double quote characters and escapes interior quotes and other special characters, returning a utf8mb4 string.

Returns `NULL` if the argument is `NULL`.

## Examples

```sql
SELECT JSON_QUOTE('A'), JSON_QUOTE("B"), JSON_QUOTE('"C"');
+-----------------+-----------------+-------------------+
| JSON_QUOTE('A') | JSON_QUOTE("B") | JSON_QUOTE('"C"') |
+-----------------+-----------------+-------------------+
| "A"             | "B"             | "\"C\""           |
+-----------------+-----------------+-------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
