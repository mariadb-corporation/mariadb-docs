---
description: >-
  Reference of the SQL system functions supported by GridGain — CASEWHEN, CAST,
  COALESCE, CONVERT, DECODE, GREATEST, IFNULL, LEAST, NULLIF, NVL2, and TABLE.
---

# System Functions

## CASEWHEN

### Description

Returns 'aValue' if the Boolean expression is true, 'bValue' otherwise.

{% hint style="info" %}
GridGain supports a more powerful [CASE WHEN expression](https://www.h2database.com/html/grammar.html#case_expression).
{% endhint %}

```sql
CASEWHEN (boolean , aValue , bValue)
```

### Parameters

- `boolean` - the value to evaluate
- `aValue` - the value to return if Boolean is `true`
- `bValue` - value to return if Boolean is `false`

### Example

Evaluate the ID and return the corresponding value:

```sql
CASEWHEN(ID=1, 'A', 'B')
```

## CAST

### Description

Converts a value to another data type using one the following conversion rules:

- When converting a number to a Boolean, `0 is considered `false` and any other value is considered `true`
- When converting a Boolean to a number, `false` is `0` and `true` is `1`
- When converting a number to a number of another type, the value is checked for overflow
- When converting a number to a binary type, the number of bytes matches the precision
- When converting a string to a binary type, it is hex-encoded
- A hex string can be converted to the binary type and then to a number; if a direct conversion is not possible, the value is first converted to a string

```sql
CAST (value AS dataType)
```

### Parameters

- `value` - the value to convert
- `dataType` - the data type to convert the value to

### Examples

```sql
CAST(NAME AS INT);
CAST(65535 AS BINARY);
CAST(CAST('FFFF' AS BINARY) AS INT);
```

## COALESCE | NVL

### Description

Returns the first value that is not `NULL`.

```sql
{COALESCE | NVL } (aValue, bValue [,...])
```

### Parameters

`aValue`, `bValue` - values to process

### Example

Return the first non-null value out of A, B, and C:

```sql
COALESCE(A, B, C)
```

## CONVERT

### Description

Converts a value to another data type.

```sql
CONVERT (value , dataType)
```

### Parameters

- `value` - the value to convert
- `dataType` - the data type to convert the value to

### Example

Convert NAME to an integer:

```sql
CONVERT(NAME, INT)
```

## DECODE

### Description

Returns the first matching value. `NULL` matches `NULL`. If no match is found, `NULL` or the last parameter is returned (if the parameter count is even).

```sql
DECODE(value, whenValue, thenValue [,...])
```

### Parameters

- `value` - the value to match against
- `whenValue`, `thenValue`, etc. - values to check

### Example

Return the first value that matches `random number greater than 0.5`:

```sql
DECODE(RAND()>0.5, 0, 'Red', 1, 'Black')
```

## GREATEST

### Description

Returns the greatest value that is not `NULL`, or `NULL` if all values are `NULL`.

```sql
GREATEST(aValue, bValue [,...])
```

### Parameters

`aValue`, `bValue` - values to process

### Example

Return the greatest values out of 1, 2, and 3:

```sql
GREATEST(1, 2, 3)
```

## IFNULL

### Description

Returns 'a' if the value is not `NULL`, 'b' otherwise.

```sql
IFNULL(aValue, bValue)
```

### Parameters

`aValue`, `bValue` - values to process

### Example

Check NULL and space ('') for being `NULL`:

```sql
IFNULL(NULL, '')
```

## LEAST

### Description

Returns the smallest value that is not NULL, or NULL if all values are NULL.

```sql
LEAST(aValue, bValue [,...])
```

### Parameters

### Example

```sql
LEAST(1, 2, 3)
```

## NULLIF

### Description

Returns NULL if 'a' equals 'b', otherwise returns 'a'.

```sql
NULLIF(aValue, bValue)
```

### Parameters

`aValue`, `bValue` - values to process

### Example

Check if A=B:

```sql
NULLIF(A, B)
```

## NVL2

### Description

If the test value is `NULL`, returns 'bValue'. Otherwise, returns 'aValue'. The data type of the returned value is the same as that of 'aValue'.

```sql
NVL2(testValue, aValue, bValue)
```

### Parameters

- `testValue` - the value to test for `NULL`
- `aValue` - the value to return if testVale is not `NULL`
- `bValue` - the value to return if testVale is `NULL`

### Example

Test if X is `NULL`:

```sql
NVL2(X, 'not null', 'null')
```

## TABLE | TABLE_DISTINCT

### Description

Returns the result set that matches the criteria. TABLE_DISTINCT removes duplicate rows.

```sql
TABLE | TABLE_DISTINCT	(name dataType = expression)
```

### Parameters

- `name` - the table name
- `dataType` - the data type to return
- `expression` - the expression that defines the dataType

### Example

Return everything from the table:

```sql
SELECT * FROM TABLE(ID INT=(1, 2), NAME VARCHAR=('Hello', 'World'))
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
