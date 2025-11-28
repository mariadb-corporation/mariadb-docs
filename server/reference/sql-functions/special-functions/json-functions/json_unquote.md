---
description: >-
  Unquote a JSON value. This function removes the quotes from a JSON string and
  unescapes special characters.
---

# JSON\_UNQUOTE

## Syntax

```sql
JSON_UNQUOTE(val)
```

## Description

Unquotes a JSON value, returning a string, or `NULL` if the argument is null.

An error will occur if the given value begins and ends with double quotes and is an invalid JSON string literal.

If the given value is not a JSON string, value is passed through unmodified.

Certain character sequences have special meanings within a string. Usually, a backslash is ignored, but the escape sequences in the table below are recognised by MariaDB, unless the [SQL Mode](../../../../server-management/variables-and-modes/sql_mode.md) is set to `NO_BACKSLASH_ESCAPES` .

| Escape sequence | Character                          |
| --------------- | ---------------------------------- |
| "               | Double quote (")                   |
| \b              | Backslash                          |
| \f              | Formfeed                           |
| \n              | Newline (linefeed)                 |
| \r              | Carriage return                    |
| \t              | Tab                                |
| \\              | Backslash ()                       |
| \uXXXX          | UTF-8 bytes for Unicode value XXXX |

## Examples

```sql
SELECT JSON_UNQUOTE('"Monty"');
+-------------------------+
| JSON_UNQUOTE('"Monty"') |
+-------------------------+
| Monty                   |
+-------------------------+
```

With the default [SQL Mode](../../../../server-management/variables-and-modes/sql_mode.md):

```sql
SELECT JSON_UNQUOTE('Si\bng\ting');
+-----------------------------+
| JSON_UNQUOTE('Si\bng\ting') |
+-----------------------------+
| Sng	ing                   |
+-----------------------------+
```

Setting `NO_BACKSLASH_ESCAPES`:

```sql
SET @@sql_mode = 'NO_BACKSLASH_ESCAPES';

SELECT JSON_UNQUOTE('Si\bng\ting');
+-----------------------------+
| JSON_UNQUOTE('Si\bng\ting') |
+-----------------------------+
| Si\bng\ting                 |
+-----------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
