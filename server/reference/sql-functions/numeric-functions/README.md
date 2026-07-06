---
description: >-
  Learn about numeric functions in MariaDB Server. This section details SQL
  functions for performing mathematical calculations, rounding, and manipulating
  numeric values in your queries.
---

# Numeric Functions

{% columns %}
{% column %}
{% content-ref url="abs.md" %}
[abs.md](abs.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate absolute value. This function returns the non-negative value of a number, removing any negative sign.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="acos.md" %}
[acos.md](acos.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate arc cosine. This function returns the angle in radians whose cosine is the given number.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="asin.md" %}
[asin.md](asin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate arc cosine. This function returns the angle in radians whose cosine is the given number.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="atan.md" %}
[atan.md](atan.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate arc tangent. This function returns the angle in radians whose tangent is the given number.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="atan2.md" %}
[atan2.md](atan2.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate arc tangent of two variables. This function returns the angle in radians between the positive x-axis and the point (X, Y).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ceil.md" %}
[ceil.md](ceil.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for CEILING(). Rounds a number up to the nearest integer.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ceiling.md" %}
[ceiling.md](ceiling.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Round up to the nearest integer. This function returns the smallest integer value that is greater than or equal to the argument.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="conv.md" %}
[conv.md](conv.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Convert numbers between bases. This function transforms a number from one numeric base system to another.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="cos.md" %}
[cos.md](cos.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate cosine. This function returns the cosine of an angle given in radians.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="cot.md" %}
[cot.md](cot.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate cotangent. This function returns the cotangent of an angle given in radians.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="crc32.md" %}
[crc32.md](crc32.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Compute cyclic redundancy check. This function returns a 32-bit unsigned integer representing the CRC32 checksum of a string.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="crc32c.md" %}
[crc32c.md](crc32c.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Compute CRC32C checksum. This function calculates a cyclic redundancy check value using the Castagnoli polynomial.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="degrees.md" %}
[degrees.md](degrees.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Convert radians to degrees. This function transforms an angle measured in radians to its equivalent in degrees.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="div.md" %}
[div.md](div.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Perform integer division. This operator divides one number by another and returns the integer result, discarding any remainder.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="exp.md" %}
[exp.md](exp.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate exponential value. This function returns the value of e (the base of natural logarithms) raised to the power of the argument.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="floor.md" %}
[floor.md](floor.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Round down to the nearest integer. This function returns the largest integer value that is less than or equal to the argument.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="ln.md" %}
[ln.md](ln.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate natural logarithm. This function returns the logarithm of a number to the base e.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="log.md" %}
[log.md](log.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate logarithm. This function returns the natural logarithm of a number, or the logarithm to a specified base if two arguments are provided.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="log10.md" %}
[log10.md](log10.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate base-10 logarithm. This function returns the logarithm of a number to the base 10.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="log2.md" %}
[log2.md](log2.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate base-2 logarithm. This function returns the logarithm of a number to the base 2.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mod.md" %}
[mod.md](mod.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate modulo. This function returns the remainder of a number divided by another number.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="oct.md" %}
[oct.md](oct.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Convert to octal. This function returns the octal string representation of a numeric argument.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="pi.md" %}
[pi.md](pi.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the value of pi. This function returns the mathematical constant π (approximately 3.141593).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="pow.md" %}
[pow.md](pow.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for POWER(). Returns the value of a number raised to the power of another number.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="power.md" %}
[power.md](power.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate power. This function returns the value of a number raised to the specified exponent.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="radians.md" %}
[radians.md](radians.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Convert degrees to radians. This function transforms an angle measured in degrees to its equivalent in radians.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="rand.md" %}
[rand.md](rand.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Generate a random number. This function returns a random floating-point value between 0 and 1.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="round.md" %}
[round.md](round.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Round a number. This function rounds a number to a specified number of decimal places.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sign.md" %}
[sign.md](sign.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the sign of a number. This function returns -1, 0, or 1 depending on whether the argument is negative, zero, or positive.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sin.md" %}
[sin.md](sin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate sine. This function returns the sine of an angle given in radians.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sqrt.md" %}
[sqrt.md](sqrt.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate square root. This function returns the non-negative square root of a number.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="tan.md" %}
[tan.md](tan.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate tangent. This function returns the tangent of an angle given in radians.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="to_number.md" %}
[to_number.md](to_number.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Convert a string to a number. This Oracle-compatible function parses a string using a specified format and returns a numeric value.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="truncate.md" %}
[truncate.md](truncate.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Truncate a number. This function truncates a number to a specified number of decimal places.
{% endcolumn %}
{% endcolumns %}
