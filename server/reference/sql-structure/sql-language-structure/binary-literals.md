---
description: >-
  Binary literal syntax in MariaDB: b'value', B'value', and 0bvalue.
---

# Binary Literals

Binary literals can be written in one of the following formats: `b'value'`, `B'value'` or `0bvalue`, where `value` is a string composed by `0` and `1` digits.

Binary literals are interpreted as binary strings, and are convenient to represent [VARBINARY](../../data-types/string-data-types/varbinary.md), [BINARY](../../data-types/string-data-types/binary.md) or [BIT](../../data-types/numeric-data-types/bit.md) values.

To convert a binary literal into an integer, just add `0`.

## Examples

Printing the value as a binary string:

```sql
SELECT 0b1000001;
+-----------+
| 0b1000001 |
+-----------+
| A         |
+-----------+
```

Converting the same value into a number:

```sql
SELECT 0b1000001+0;
+-------------+
| 0b1000001+0 |
+-------------+
|          65 |
+-------------+
```

## See Also

* [BIN()](../../sql-functions/string-functions/bin.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
