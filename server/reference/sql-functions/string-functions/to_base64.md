---
description: >-
  Encode a string to base-64. This function converts a string argument to its
  base-64 encoded form.
---

# TO\_BASE64

## Syntax

```sql
TO_BASE64(str)
```

## Description

Converts the string argument `str` to its base-64 encoded form, returning the result as a character string in the connection character set and collation.

The argument `str` will be converted to string first if it is not a string. A `NULL` argument will return a `NULL` result.

The reverse function, [FROM\_BASE64()](from_base64.md), decodes an encoded base-64 string.

There are a numerous different methods to base-64 encode a string. The following are used by MariaDB and MySQL:

* Alphabet value 64 is encoded as '+'.
* Alphabet value 63 is encoded as '/'.
* Encoding output is made up of groups of four printable characters, with each three bytes of data encoded using four characters. If the final group is not complete, it is padded with '=' characters to make up a length of four.
* To divide long output, a newline is added after every 76 characters.
* Decoding will recognize and ignore newlines, carriage returns, tabs, and spaces.

## Examples

```sql
SELECT TO_BASE64('Maria');
+--------------------+
| TO_BASE64('Maria') |
+--------------------+
| TWFyaWE=           |
+--------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
