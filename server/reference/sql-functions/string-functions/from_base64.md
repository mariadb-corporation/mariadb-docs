---
description: >-
  Decode a base-64 encoded string. This function takes a base-64 string and
  returns the decoded binary result.
---

# FROM\_BASE64

## Syntax

```sql
FROM_BASE64(str)
```

## Description

Decodes the given base-64 encode string, returning the result as a binary string. Returns `NULL` if the given string is `NULL` or if it's invalid.

It is the reverse of the [TO\_BASE64](to_base64.md) function.

There are numerous methods to base-64 encode a string. MariaDB uses the following:

* It encodes alphabet value 64 as '`+`'.
* It encodes alphabet value 63 as '`/`'.
* It codes output in groups of four printable characters. Each three byte of data encoded uses four characters. If the final group is incomplete, it pads the difference with the '`=`' character.
* It divides long output, adding a new line very 76 characters.
* In decoding, it recognizes and ignores newlines, carriage returns, tabs and space whitespace characters.

```sql
SELECT TO_BASE64('Maria') AS 'Input';
+-----------+
| Input     |
+-----------+
| TWFyaWE=  |
+-----------+

SELECT FROM_BASE64('TWFyaWE=') AS 'Output';
+--------+
| Output |
+--------+
| Maria  |
+--------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
