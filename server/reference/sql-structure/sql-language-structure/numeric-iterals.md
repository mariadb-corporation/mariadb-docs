---
description: >-
  Numeric literal syntax for integers and decimals, including signs and
  exponents.
---


# Numeric Literals

Numeric literals are written as a sequence of digits from `0` to `9`. Initial zeros are ignored. A sign can always precede the digits, but it is optional for positive numbers. In decimal numbers, the integer part and the decimal part are divided with a dot (`.`).


If the integer part is zero, it can be omitted, but the literal must begin with a dot.


The notation with exponent can be used. The exponent is preceded by an `E` or `e` character. The exponent can be preceded by a sign and must be an integer. A number `N` with an exponent part `X`, is calculated as `N * POW(10, X)`.


In some cases, adding zeroes at the end of a decimal number can increment the precision of the expression where the number is used. For example, [PI()](../../sql-functions/numeric-functions/pi.md) by default returns a number with 6 decimal digits. But the `PI()+0.0000000000` expression (with 10 zeroes) returns a number with 10 decimal digits.


[Hexadecimal literals](hexadecimal-literals.md) are interpreted as numbers when used in numeric contexts.


## Examples


```
10
+10
-10
```

All these literals are equivalent:


```
0.1
.1
+0.1
+.1
```

With exponents:


```
0.2E3 -- 0.2 * POW(10, 3) = 200
.2e3
.2e+2
1.1e-10 -- 0.00000000011
-1.1e10 -- -11000000000
```


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
