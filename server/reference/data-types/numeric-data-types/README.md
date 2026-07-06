---
description: >-
  Complete numeric types reference: INT/BIGINT ranges, DECIMAL(M,D)
  precision/scale, FLOAT/DOUBLE storage sizes, and numeric type selection
  guidelines.
---

# Numeric Data Types

{% columns %}
{% column %}
{% content-ref url="numeric-data-type-overview.md" %}
[numeric-data-type-overview.md](numeric-data-type-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
General introduction to numeric data types. This page summarizes the available integer, fixed-point, and floating-point types and their storage characteristics.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="bigint.md" %}
[bigint.md](bigint.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Large integer type. A BIGINT uses 8 bytes and can store values from -9223372036854775808 to 9223372036854775807 (signed) or 0 to 18446744073709551615 (unsigned).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="bit.md" %}
[bit.md](bit.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Bit-field data type. A BIT(M) column stores M bits per value, allowing storage of binary values from 1 to 64 bits in length.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="bool.md" %}
[bool.md](bool.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for TINYINT(1). This type is commonly used to represent boolean values, where 0 is considered false and non-zero values are true.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="boolean.md" %}
[boolean.md](boolean.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete BOOLEAN type reference: TINYINT(1) synonym, TRUE/FALSE aliases, CREATE TABLE/SHOW CREATE TABLE output, and IF()/IS operator evaluation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="dec-numeric-fixed.md" %}
[dec-numeric-fixed.md](dec-numeric-fixed.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonyms for DECIMAL. These keywords declare fixed-point numbers, which store exact numeric data with a defined precision and scale.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="numeric-data-types-dec.md" %}
[numeric-data-types-dec.md](numeric-data-types-dec.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for DECIMAL. This keyword creates a fixed-point column with exact precision, suitable for financial calculations.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="decimal.md" %}
[decimal.md](decimal.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete DECIMAL type reference: DECIMAL(M,D) syntax, precision limits (M≤65, D≤38), SIGNED/UNSIGNED/ZEROFILL options, and rounding behavior.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="double-precision.md" %}
[double-precision.md](double-precision.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for DOUBLE. This keyword declares a normal-size (8-byte) floating-point number with double precision.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="double.md" %}
[double.md](double.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Double precision floating-point number. A DOUBLE column uses 8 bytes to store large or precise approximate values.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="fixed.md" %}
[fixed.md](fixed.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for DECIMAL. This keyword is used to define columns that require exact numeric precision, such as currency.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="float.md" %}
[float.md](float.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Single precision floating-point number. A FLOAT column uses 4 bytes and stores approximate values with less precision than DOUBLE.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="float4.md" %}
[float4.md](float4.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for FLOAT. This keyword declares a single-precision floating-point column.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="float8.md" %}
[float8.md](float8.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for DOUBLE. This keyword declares a double-precision floating-point column.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="floating-point-accuracy.md" %}
[floating-point-accuracy.md](floating-point-accuracy.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explanation of floating-point precision issues. This page details why FLOAT and DOUBLE types are approximate and how rounding errors occur.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="int.md" %}
[int.md](int.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete INT type reference: INT(M) syntax, signed (-2147483648 to 2147483647) vs unsigned (0 to 4294967295) ranges, and ZEROFILL padding guidelines.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="int1.md" %}
[int1.md](int1.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for TINYINT. This type uses 1 byte of storage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="int2.md" %}
[int2.md](int2.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for SMALLINT. This type uses 2 bytes of storage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="int3.md" %}
[int3.md](int3.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for MEDIUMINT. This type uses 3 bytes of storage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="int4.md" %}
[int4.md](int4.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for INT. This type uses 4 bytes of storage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="int8.md" %}
[int8.md](int8.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for BIGINT. This type uses 8 bytes of storage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="integer.md" %}
[integer.md](integer.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for INT. This keyword declares a standard 4-byte integer column.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mediumint.md" %}
[mediumint.md](mediumint.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Medium-sized integer. A MEDIUMINT column uses 3 bytes and stores values from -8388608 to 8388607 (signed) or 0 to 16777215 (unsigned).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="middleint.md" %}
[middleint.md](middleint.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for MEDIUMINT. This keyword refers to the 3-byte integer type.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="number.md" %}
[number.md](number.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Oracle-compatible synonym for DECIMAL. This type is used for fixed-point arithmetic.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="numeric.md" %}
[numeric.md](numeric.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for DECIMAL. This type stores exact numeric data values.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="real.md" %}
[real.md](real.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for DOUBLE. In standard SQL mode, REAL is a double-precision floating-point number.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="smallint.md" %}
[smallint.md](smallint.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Small integer type. A SMALLINT column uses 2 bytes and stores values from -32768 to 32767 (signed) or 0 to 65535 (unsigned).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tinyint.md" %}
[tinyint.md](tinyint.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Very small integer type. A TINYINT column uses 1 byte and stores values from -128 to 127 (signed) or 0 to 255 (unsigned).
{% endcolumn %}
{% endcolumns %}
