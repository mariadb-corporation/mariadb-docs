---
description: >-
  Double precision floating-point number. A DOUBLE column uses 8 bytes to store
  large or precise approximate values.
---

# DOUBLE

## Syntax

```sql
DOUBLE[(M,D)] [SIGNED | UNSIGNED | ZEROFILL]
DOUBLE PRECISION[(M,D)] [SIGNED | UNSIGNED | ZEROFILL]
REAL[(M,D)] [SIGNED | UNSIGNED | ZEROFILL]
```

## Description

A normal-size (double-precision) floating-point number (see [FLOAT](float.md) for a single-precision floating-point number). Allowable values are:

* `-1.7976931348623157E+308` to `-2.2250738585072014E-308`
* `0`
* `2.2250738585072014E-308` to `1.7976931348623157E+308`

These are the theoretical limits, based on the IEEE standard. The actual range might be slightly smaller depending on your hardware or operating system.

`M` is the total number of digits and `D` is the number of digits following the decimal point. If `M` and `D` are omitted, values are stored to the limits allowed by the hardware. A double-precision floating-point number is accurate to approximately 15 decimal places.

`UNSIGNED`, if specified, disallows negative values.

`ZEROFILL`, if specified, pads the number with zeros, up to the total number of digits specified by `M`.

`REAL` and `DOUBLE PRECISION` are synonyms, unless the `REAL_AS_FLOAT` [SQL mode](../../../server-management/variables-and-modes/sql_mode.md) is enabled, in which case `REAL` is a synonym for [FLOAT](float.md) rather than `DOUBLE`.

See [Floating Point Accuracy](floating-point-accuracy.md) for issues when using floating-point numbers.

For more details on the attributes, see [Numeric Data Type Overview](numeric-data-type-overview.md).

## Examples

```sql
CREATE TABLE t1 (d DOUBLE(5,0) zerofill);

INSERT INTO t1 VALUES (1),(2),(3),(4);

SELECT * FROM t1;
+-------+
| d     |
+-------+
| 00001 |
| 00002 |
| 00003 |
| 00004 |
+-------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
