---
description: >-
  Convert numbers between bases. This function transforms a number from one
  numeric base system to another.
---

# CONV

## Syntax

```sql
CONV(N,from_base,to_base)
```

## Description

Converts numbers between different number bases. Returns a string representation of the number _`N`_, converted from base _`from_base`_ to base _`to_base`_.

Returns `NULL` if any argument is `NULL`, or if the second or third argument are not in the allowed range.

{% tabs %}
{% tab title="Current" %}
The argument _`N`_ is interpreted as an integer, but may be specified as an integer or a string. The minimum base is 2 and the maximum base is 62. If _`to_base`_ is a negative number, _`N`_ is regarded as a signed number. Otherwise, _`N`_ is treated as unsigned. `CONV()` works with 64-bit precision.
{% endtab %}

{% tab title="< 11.4" %}
The argument _`N`_ is interpreted as an integer, but may be specified as an integer or a string. The minimum base is 2 and the maximum base is 36. If _`to_base`_ is a negative number, _`N`_ is regarded as a signed number. Otherwise, _`N`_ is treated as unsigned. `CONV()` works with 64-bit precision.
{% endtab %}
{% endtabs %}

Some shortcuts for this function are also available: [BIN()](../string-functions/bin.md), [OCT()](oct.md), [HEX()](../string-functions/hex.md), [UNHEX()](../string-functions/unhex.md). Also, MariaDB allows [binary](../../sql-structure/sql-language-structure/binary-literals.md) literal values and [hexadecimal](../../sql-structure/sql-language-structure/hexadecimal-literals.md) literal values.

## Examples

```sql
SELECT CONV('a',16,2);
+----------------+
| CONV('a',16,2) |
+----------------+
| 1010           |
+----------------+

SELECT CONV('6E',18,8);
+-----------------+
| CONV('6E',18,8) |
+-----------------+
| 172             |
+-----------------+

SELECT CONV(-17,10,-18);
+------------------+
| CONV(-17,10,-18) |
+------------------+
| -H               |
+------------------+

SELECT CONV(12+'10'+'10'+0xa,10,10);
+------------------------------+
| CONV(12+'10'+'10'+0xa,10,10) |
+------------------------------+
| 42                           |
+------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
