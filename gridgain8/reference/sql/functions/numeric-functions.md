---
description: >-
  Reference of the SQL numeric functions supported by GridGain — trigonometric,
  logarithmic, bitwise, rounding, random, encryption, and compression functions.
---

# Numeric Functions

## ABS

### Description

Returns the absolute value of an expression.

```sql
ABS (expression)
```

### Parameters

`expression` - may be a column name, a result of another function, or a math operation

### Example

Calculate an absolute value:

```sql
SELECT transfer_id, ABS (price) from Transfers;
```

## ACOS

### Description

Calculates the arc cosine, returns a `double`.

```sql
ACOS (expression)
```

### Parameters

`expression` - may be a column name, a result of another function, or a math operation

### Example

Calculate the arc cos value:

```sql
SELECT acos(angle) FROM Triangles;
```

## ASIN

### Description

Calculates the arc sine, returns a `double`.

```sql
ASIN (expression)
```

### Parameters

`expression` - may be a column name, a result of another function, or a math operation

### Example

Calculate an arc sine:

```sql
SELECT asin(angle) FROM Triangles;
```

## ATAN

### Description

Calculates the arc tangent, returns a `double`.

```sql
ATAN (expression)
```

### Parameters

`expression` - may be a column name, a result of another function, or a math operation

### Example

Calculate an arc tangent:

```sql
SELECT atan(angle) FROM Triangles;
```

## COS

### Description

Calculates the trigonometric cosine, returns a `double`.

```sql
COS (expression)
```

### Parameters

`expression` - may be a column name, a result of another function, or a math operation

### Example

Calculate a cosine:

```sql
SELECT COS(angle) FROM Triangles;
```

## COSH

### Description

Calculates the hyperbolic cosine, returns a `double`.

```sql
COSH (expression)
```

### Parameters

`expression` - may be a column name, a result of another function, or a math operation

### Example

Calculate n hyperbolic cosine:

```sql
SELECT HCOS(angle) FROM Triangles;
```

## COT

### Description

Calculates the trigonometric cotangent (1/TAN(ANGLE)), returns a `double`.

```sql
COT (expression)
```

### Parameters

`expression` - may be a column name, a result of another function, or a math operation

### Example

Calculate trigonometric cotangent:

```sql
SELECT COT(angle) FROM Triangles;
```

## SIN

### Description

Calculates the trigonometric sine, returns a `double`.

```sql
SIN (expression)
```

### Parameters

`expression` - may be a column name, a result of another function, or a math operation

### Example

Calculate a trigonometric sine:

```sql
SELECT SIN(angle) FROM Triangles;
```

## SINH

### Description

Calculates the hyperbolic sine, returns a `double`.

```sql
SINH (expression)
```

### Parameters

`expression` - may be a column name, a result of another function, or a math operation

### Example

Calculate a hyperbolic sine:

```sql
SELECT SINH(angle) FROM Triangles;
```

## TAN

### Description

Calculates the trigonometric tangent, returns a `double`.

```sql
TAN (expression)
```

### Parameters

`expression` - may be a column name, a result of another function, or a math operation

### Example

Calculate a trigonometric tangent:

```sql
SELECT TAN(angle) FROM Triangles;
```

## TANH

### Description

Calculates the hyperbolic tangent, returns a `double`.

```sql
TANH (expression)
```

### Parameters

`expression` - may be a column name, a result of another function, or a math operation

### Example

Calculate a hyperbolic tangent:

```sql
SELECT TANH(angle) FROM Triangles;
```

## ATAN2

### Description

Calculates the angle when converting the rectangular coordinates to the polar coordinates, returns a `double`.

```sql
ATAN2 (y, x)
```

### Parameters

`x` and `y` - the arguments

### Example

Calculate a 2-argument arctangent:

```sql
SELECT ATAN2(X, Y) FROM Triangles;
```

## BITAND

### Description

The bitwise AND operation, returns a `long`.

```sql
BITAND (y, x)
```

### Parameters

`x` and `y` - the arguments.

### Example

Return the bitwise AND:

```sql
SELECT BITAND(X, Y) FROM Triangles;
```

## BITGET

### Description

Returns `true` if and only if the first parameter has a bit set in the position specified by the second parameter. The second parameter is zero-indexed; the least significant bit has position 0.

```sql
BITGET (y, x)
```

### Parameters

`x` and `y` - the arguments

### Example

Verify that the third bit is 1:

```sql
SELECT BITGET(X, 3) from Triangles;
```

## BITOR

### Description

The bitwise OR operation, returns a `long`.

```sql
BITOR (y, x)
```

### Parameters

`x` and `y` - the arguments

### Example

Perform the bitwise OR operation:

```sql
SELECT BITGET(X, Y) from Triangles;
```

## BITXOR

### Description

The bitwise XOR operation, returns a `long`.

```sql
BITXOR (y, x)
```

### Parameters

`x` and `y` - the arguments

### Example

Perform the bitwise XOR operation:

```sql
SELECT BITXOR(X, Y) FROM Triangles;
```

## MOD

### Description

The modulo operation, returns a `long`.

```sql
MOD (y, x)
```

### Parameters

`x` and `y` - the arguments

### Example

Calculate MOD between two fields:

```sql
SELECT BITXOR(X, Y) FROM Triangles;
```

## CEILING

### Description

Returns the smallest integer value that is greater than, or equal to, the argument. The returned value is of the same type as the argument, with the scale set to `0` the precision adjusted (if applicable).

```sql
CEIL (expression)
CEILING (expression)
```

### Parameters

`expression` - any valid numeric expression

### Example

Calculate a ceiling price for items:

```sql
SELECT item_id, CEILING(price) FROM Items;
```

## DEGREES

### Description

Converts an angle measured in radians to an approximately equivalent angle measured in degrees, returns a `double`.

```sql
DEGREES (expression)
```

### Parameters

`expression` - any valid numeric expression

### Example

Convert radians to degrees:

```sql
SELECT DEGREES(X) FROM Triangles;
```

## EXP

### Description

Calculates E raised to the power of x, returns a `double`.

```sql
EXP (expression)
```

### Parameters

`expression` - any valid numeric expression

### Example

Calculate exp(X):

```sql
SELECT EXP(X) FROM Triangles;
```

## FLOOR

### Description

Returns the largest integer value that is less than, or equal to, the argument. The returned value is of the same type as the argument, with the scale set to `0` the precision adjusted (if applicable).

```sql
FLOOR (expression)
```

### Parameters

`expression` - any valid numeric expression

### Example

Calculate a floor price:

```sql
SELECT FLOOR(X) FROM Items;
```

## LOG

### Description

Calculates the natural logarithm (base e) of a `double` value, returns a `double`.

```sql
LOG (expression)
LN (expression)
```

### Parameters

`expression` - any valid numeric expression

### Example

Calculate a natural logarithm:

```sql
SELECT LOG(X) from Items;
```

## LOG10

### Description

Calculates the base 10 logarithm of a `double` value, returns a `double`.

```sql
LOG10 (expression)
```

### Parameters

`expression` - any valid numeric expression

### Example

Calculate a base 10 algorithm:

```sql
SELECT LOG(X) FROM Items;
```

## RADIANS

### Description

Converts an angle measured in degrees to an approximately equivalent angle measured in radians, returns a `double`.

```sql
RADIANS (expression)
```

### Parameters

`expression` - any valid numeric expression

### Example

Calculate RADIANS:

```sql
SELECT RADIANS(X) FROM Items;
```

## SQRT

### Description

Calculates the correctly rounded positive square root of a double value, returns a `double`.

```sql
SQRT (expression)
```

### Parameters

`expression` - any valid numeric expression

### Example

Calculate a square root:

```sql
SELECT SQRT(X) FROM Items;
```

## PI

### Description

Returns Pi as a static final `double` constant.

```sql
PI (expression)
```

### Example

Calculate Pi:

```sql
SELECT PI(X) FROM Items;
```

## POWER

### Description

Calculates a number raised to the power of some other number, returns a `double`.

```sql
POWER (X, Y)
```

### Parameters

- `x` - the base
- `y` - the power

### Example

Calculate n in the power of 2:

```sql
SELECT pow(n, 2) FROM Rows;
```

## RAND

### Description

When called without a parameter, returns a pseudo random number. When called with a parameter, seeds the session's random number generator. Returns a `double` between 0 (including) and 1 (excluding).

```sql
{RAND | RANDOM} ([expression])
```

### Parameters

`expression` - any valid numeric expression

### Example

Return a random number for every play:

```sql
SELECT random() FROM Play;
```

## RANDOM_UUID

### Description

Returns a new UUID with 122 pseudo random bits.

```sql
{RANDOM_UUID | UUID} ()
```

### Example

Return a random number for every Player:

```sql
SELECT UUID(),name FROM Player;
```

## ROUND

### Description

Rounds to the specified number of digits, or to the nearest long (if the number of digits if not specified). Returns a `numeric` (the same type as the input).

```sql
ROUND ( expression [, precision] )
```

### Parameters

- `expression` - any valid numeric expression
- `precision` - the number of digits after the decimal point to round to

### Example

Convert every Player's age to an integer:

```sql
SELECT name, ROUND(age) FROM Player;
```

## ROUNDMAGIC

### Description

Rounds numbers. Has a special handling algorithm for numbers around 0. Only numbers smaller than or equal to `+/-1000000000000` are supported. The value is converted to a `string` internally, and then the last 4 characters are checked. '000x' becomes '0000' and '999x' becomes '999999', which is rounded automatically. This function returns a `double`.

{% hint style="info" %}
This function can be slow.
{% endhint %}

```sql
ROUNDMAGIC (expression)
```

### Parameters

`expression` - any valid numeric expression

### Example

Round every Player's age:

```sql
SELECT name, ROUNDMAGIC(AGE/3*3) FROM Player;
```

## SECURE_RAND

### Description

Generates a number of cryptographically secure random numbers, returns `bytes`.

```sql
SECURE_RAND (int)
```

### Parameters

`int` - the number of digits

### Example

Get a truly random number:

```sql
SELECT name, SECURE_RAND(10) FROM Player;
```

## SIGN

### Description

Returns `-1` if the value is smaller than zero, `0` if zero, `1` otherwise.

```sql
SIGN (expression)
```

### Parameters

`expression` - any valid numeric expression

### Example

Get a sign for every value:

```sql
SELECT name, SIGN(VALUE) FROM Player;
```

## ENCRYPT

### Description

Encrypts data using a key. The supported algorithm is AES. The block size is 16 bytes. Returns `bytes`.

```sql
ENCRYPT (algorithmString , keyBytes , dataBytes)
```

### Parameters

- `algorithmString` - the AES algorithm
- `keyBytes` - the key
- `dataBytes` - data block size

### Example

Encrypt players names:

```sql
SELECT ENCRYPT('AES', '00', STRINGTOUTF8(Name)) FROM Player;
```

## DECRYPT

### Description

Decrypts data using a key. The supported algorithm is AES. The block size is 16 bytes. Returns `bytes`.

```sql
DECRYPT (algorithmString , keyBytes , dataBytes)
```

### Parameters

- `algorithmString` - the AES algorithm
- `keyBytes` - the key
- `dataBytes` - data block size

### Example

Decrypt Players' names:

```sql
SELECT DECRYPT('AES', '00', '3fabb4de8f1ee2e97d7793bab2db1116'))) FROM Player;
```

## TRUNCATE

### Description

Truncates to a number of digits (to the next value closer to 0). Returns a `double`. When used with a timestamp, truncates the timestamp to the date (day) value. When used with a date, truncates the date to the date (day) value less the time part. When used with a timestamp as `string`, truncates the  timestamp to a date (day) value.

```sql
{TRUNC | TRUNCATE} ({{numeric, digitsInt} | timestamp | date | timestampString})
```

### Parameters

- `digitsInt` - the number for digits to truncate to
- `timestamp` - the timestamp to truncate
- `date` - the date to truncate to
- `timestampString` - the timestamp expressed as a string

### Example

Truncate teg value to 2 digits:

```sql
TRUNCATE(VALUE, 2);
```

## COMPRESS

### Description

Compresses the data using the specified compression algorithm. The supported algorithms are: LZF (faster but lower compression; default) and DEFLATE (higher degree of compression). Compression does not always reduce size. Very small objects and objects with little redundancy may get larger. This function returns `bytes`.

```sql
COMPRESS(dataBytes [, algorithmString])
```

### Parameters

- `dataBytes` - the data to compress
- `algorithmString` - the algorithm to use for compression

### Example

Compress STRINGTOUTF8 using the LZF (default) algorithm:

```sql
COMPRESS(STRINGTOUTF8('Test'))
```

## EXPAND

### Description

Expands data that was previously compressed using the the COMPRESS function, returns `bytes`.

```sql
EXPAND(dataBytes)
```

### Parameters

`dataBytes` - the data to expand

### Example

Converts the string to UTF8 format, compress it, expand it, and converts it back to Unicode:

```sql
UTF8TOSTRING(EXPAND(COMPRESS(STRINGTOUTF8('LZF'))))
```

## ZERO

### Description

Returns the value of `0`. Can be used even if numeric literals are disabled.

```sql
ZERO()
```

### Example

Return 0:

```sql
ZERO()
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
