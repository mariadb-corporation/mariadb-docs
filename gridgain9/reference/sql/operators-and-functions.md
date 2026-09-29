---
description: >-
  SQL functions reference for GridGain 9, covering aggregate, date/time, JSON,
  numeric, string, and other functions built on Apache Calcite.
---

# SQL Functions Reference

This reference documents the SQL functions available in GridGain 9. These functions are built on Apache Calcite's SQL implementation and provide comprehensive support for data manipulation, analysis, and transformation operations.

For more information on functions supported by Apache Calcite, see the [Calcite documentation](https://calcite.apache.org/docs/reference.html#operators-and-functions).

## Aggregate Functions

### ANY_VALUE

Returns an arbitrary non-null value from the input values that matches the provided filter, if any. The specific value returned is not deterministic.  If input is empty, or no rows match the filter, `NULL` is returned.

```sql
ANY_VALUE( expression ) [ FILTER ( WHERE filter_condition ) ]
```

**Arguments**

- expression - Expression to evaluate. Accepts any data type.
- filter_condition - Optional. Boolean expression used to filter rows before aggregation.

**Return Type**

Same type as input (nullable)

### AVG

Returns the average (arithmetic mean) of all input values.

```sql
AVG( [ ALL | DISTINCT ] expression ) [ FILTER ( WHERE filter_condition ) ]
```

**Arguments**

- ALL - Default. Applies the aggregate function to all values.
- DISTINCT - Calculates the average of unique values only, excluding duplicates from the calculation.
- expression - Numeric expression to average. Supported data types: `TINYINT`, `SMALLINT`, `INTEGER`, `BIGINT`, `DECIMAL`, `REAL`, `FLOAT`, `DOUBLE`.
- filter_condition - Optional. Boolean expression used to filter rows before aggregation.

**Return Type**

The return type depends on the input type:

| Input type | Result type | Result precision | Result scale | Notes |
| --- | --- | --- | --- | --- |
| `DECIMAL` | `DECIMAL` | input_precision + (scale - input_scale) | MAX(16, input_scale) | Minimum scale of 16 is enforced |
| `BIGINT`, `INTEGER`, `SMALLINT`, `TINYINT` | `DECIMAL` | input_precision + 16 | 16 | Integer types converted to DECIMAL |
| `DOUBLE`, `REAL`, `FLOAT` | `DOUBLE` | N/A | N/A | All approximate types return `DOUBLE` |

### COUNT

Returns the number of rows or non-null values.

```sql
COUNT( * ) [ FILTER ( WHERE filter_condition ) ]
COUNT( [ ALL | DISTINCT ] expression ) [ FILTER ( WHERE filter_condition ) ]
```

**Arguments**

- * (asterisk) - Counts all rows including those with null values in any column.
- ALL - Default. Counts all non-null values in the expression.
- DISTINCT - Counts only unique non-null values, excluding duplicates.
- expression - Expression to evaluate. Accepts any data type.
- filter_condition - Optional. Boolean expression used to filter rows before aggregation.

**Return Type**

`BIGINT` (not null)

### EVERY

Returns `TRUE` if for every input row `boolean_expression` evaluates to `TRUE`, `FALSE` otherwise.

```sql
EVERY( boolean_expression ) [ FILTER ( WHERE filter_condition ) ]
```

**Arguments**

- boolean_expression - Boolean expression to evaluate. Accepts `BOOLEAN` type values.
- filter_condition - Optional. Boolean expression used to filter rows before aggregation.

**Return Type**

`BOOLEAN` (nullable)

### GROUPING

Returns a bit vector indicating which grouping expressions are part of the current grouping set. Used with `GROUP BY ROLLUP`, `CUBE`, or `GROUPING SETS`.

```sql
GROUPING( expression [, expression, ...] )
```

**Arguments**

- expression - One or more grouping column expressions from the `GROUP BY` clause.

**Return Type**

`BIGINT` (not null) - Bit vector where 1 indicates the expression is aggregated

### MAX

Returns the maximum value from all input values.

```sql
MAX( [ ALL | DISTINCT ] expression ) [ FILTER ( WHERE filter_condition ) ]
```

**Arguments**

- ALL - Default. Considers all values in the expression.
- DISTINCT - Has no effect for `MAX` (maximum of distinct values equals maximum of all values).
- expression - Expression to evaluate. Accepts any comparable data type (numeric, string, date/time).
- filter_condition - Optional. Boolean expression used to filter rows before aggregation.

**Return Type**

Same type as input (nullable)

### MIN

Returns the minimum value from all input values.

```sql
MIN( [ ALL | DISTINCT ] expression ) [ FILTER ( WHERE filter_condition ) ]
```

**Arguments**

- ALL - Default. Considers all values in the expression.
- DISTINCT - Has no effect for MIN (minimum of distinct values equals minimum of all values).
- expression - Expression to evaluate. Accepts any comparable data type (numeric, string, date/time).
- filter_condition - Optional. Boolean expression used to filter rows before aggregation.

**Return Type**

Same type as input (nullable)

### SOME

Returns `TRUE` if any input row `boolean_expression` evaluates to `TRUE`, `FALSE` if all evaluate to `FALSE`.

```sql
SOME( boolean_expression ) [ FILTER ( WHERE filter_condition ) ]
```

**Arguments**

- boolean_expression - Boolean expression to evaluate. Accepts `BOOLEAN` type values.
- filter_condition - Optional. Boolean expression used to filter rows before aggregation.

**Return Type**

`BOOLEAN` (nullable)

### SUM

Returns the sum of all input values.

```sql
SUM( [ ALL | DISTINCT ] numeric_expression ) [ FILTER ( WHERE filter_condition ) ]
```

**Arguments**

- ALL - Sums all values in the expression. This is the default behavior.
- DISTINCT - Sums only unique values, excluding duplicates from the calculation.
- numeric_expression - Numeric expression to sum. Accepts `TINYINT`, `SMALLINT`, `INTEGER`, `BIGINT`, `DECIMAL`, `REAL`, `FLOAT`, `DOUBLE` data types.
- filter_condition - Optional. Boolean expression used to filter rows before aggregation.

**Return Type**

| Input type | Result type | Notes |
| --- | --- | --- |
| `INTEGER`, `SMALLINT`, `TINYINT` | `BIGINT` | Integer types promoted to BIGINT |
| `BIGINT` | `DECIMAL(19, 0)` | BIGINT promoted to `DECIMAL` to avoid overflow |
| `DECIMAL` | `DECIMAL` | Precision may increase to accommodate sum |
| `REAL`, `FLOAT`, `DOUBLE` | `DOUBLE` | All approximate types return `DOUBLE` |

Result is nullable.

## Date/Time Functions

### CEIL

Rounds a numeric value up, or a datetime value up to the specified time unit.

```sql
CEIL( numeric_expression )
CEIL( datetime TO timeUnit )
```

**Arguments**

- numeric_expression - Numeric value to round up. Accepts numeric data types.
- datetime - Date, time, or timestamp expression to round. Accepts `DATE`, `TIME`, `TIMESTAMP` types.
- timeUnit - Time unit to round up to: `YEAR`, `QUARTER`, `MONTH`, `WEEK`, `DAY`, `HOUR`, `MINUTE`, `SECOND`, `MILLISECOND`, `MICROSECOND`.

**Return Type**

Same type as input (nullable)

### CURRENT_DATE

Returns the current date in the session's time zone.

```sql
CURRENT_DATE
```

**Arguments**

None

**Return Type**

`DATE` (not null)

### CURRENT_TIMESTAMP

Returns the current timestamp in the session's local time zone.

```sql
CURRENT_TIMESTAMP
CURRENT_TIMESTAMP( precision )
```

**Arguments**

- precision - Optional. Number of fractional seconds digits (0-9). Default value is 6.

**Return Type**

`TIMESTAMP WITH LOCAL TIME ZONE`

### DATE

Converts a string or timestamp to a date.

```sql
DATE( string )
DATE( timestamp )
DATE(year, month, day) // all ints
DATE(timestamp)
DATE(timestampLtz [, timeZone])
```

**Arguments**

- string - String in date format (e.g., 'YYYY-MM-DD'). Accepts `VARCHAR` or `CHAR` data types.
- timestamp - Timestamp expression to extract date from. Accepts `TIMESTAMP` data type.
- year - Integer value representing the year component (e.g., 2024). Accepts `INTEGER` data type.
- month - Integer value representing the month component (1-12). Accepts `INTEGER` data type.
- day - Integer value representing the day component (1-31). Accepts `INTEGER` data type.
- timestampLtz - Timestamp with local time zone to construct a date from. Accepts `TIMESTAMP WITH LOCAL TIME ZONE` data type.
- timeZone - Optional. A string specifying the time zone for conversion. Accepts `VARCHAR` data type. Used when converting from timestamp with local time zone.

**Return Type**

`DATE` (nullable)

### DATE_FROM_UNIX_DATE

Converts days since 1970-01-01 (Unix epoch) to a date.

```sql
DATE_FROM_UNIX_DATE( days )
```

**Arguments**

- days - Number of days since Unix epoch (1970-01-01). Accepts `INTEGER` type.

**Return Type**

`DATE` (nullable)

### DAYNAME

Returns the name of the weekday (e.g., 'Monday', 'Tuesday') for a given date.

```sql
DAYNAME( date )
```

**Arguments**

- date - Date or timestamp expression to get weekday name from. Accepts `DATE` or `TIMESTAMP` types.

**Return Type**

`VARCHAR` (nullable)

### DAYOFMONTH

Returns the day of the month (1-31) from a date.

```sql
DAYOFMONTH( date )
```

**Arguments**

- date - Date or timestamp expression to extract day from. Accepts `DATE` or `TIMESTAMP` types.

**Return Type**

`BIGINT` (nullable)

### DAYOFWEEK

Returns the day of the week (1-7, where 1=Sunday) from a date.

```sql
DAYOFWEEK( date )
```

**Arguments**

- date - Date or timestamp expression to extract day of week from. Accepts `DATE` or `TIMESTAMP` types.

**Return Type**

`BIGINT` (nullable)

### DAYOFYEAR

Returns the day of the year (1-366) from a date.

```sql
DAYOFYEAR( date )
```

**Arguments**

- date - Date or timestamp expression to extract day of year from. Accepts `DATE` or `TIMESTAMP` types.

**Return Type**

`BIGINT` (nullable)

### EXTRACT

Extracts a specified time unit from a datetime value.

```sql
EXTRACT( timeUnit FROM datetime )
```

**Arguments**

- timeUnit - Type of time unit to extract: `YEAR`, `QUARTER`, `MONTH`, `WEEK`, `DAY`, `DAYOFWEEK`, `DAYOFYEAR`, `HOUR`, `MINUTE`, `SECOND`.
- datetime - Date, time, or timestamp expression to extract from. Accepts `DATE`, `TIME`, or `TIMESTAMP` types.

**Return Type**

`BIGINT` (nullable)

### FLOOR

Rounds a numeric value down, or a datetime value down to the specified time unit.

```sql
FLOOR( numeric_expression )
FLOOR( datetime TO timeUnit )
```

**Arguments**

- numeric_expression - Numeric value to round down. Accepts numeric data types.
- datetime - Date, time, or timestamp expression to round. Accepts `DATE`, `TIME`, `TIMESTAMP` types.
- timeUnit - Time unit to round down to: `YEAR`, `QUARTER`, `MONTH`, `WEEK`, `DAY`, `HOUR`, `MINUTE`, `SECOND`, `MILLISECOND`, `MICROSECOND`.

**Return Type**

Same type as input (nullable)

### HOUR

Returns the hour (0-23) from a time or timestamp.

```sql
HOUR( time )
```

**Arguments**

- time - Time or timestamp expression to extract hour from. Accepts `TIME` or `TIMESTAMP` types.

**Return Type**

`BIGINT` (nullable)

### LAST_DAY

Returns the last day of the month for a given date.

```sql
LAST_DAY( date )
```

**Arguments**

- date - Date or timestamp expression to get last day of month. Accepts `DATE` or `TIMESTAMP` types.

**Return Type**

`DATE` (nullable)

### LOCALTIME

Returns the current time in the session's local time zone.

```sql
LOCALTIME
LOCALTIME( precision )
```

**Arguments**

- precision - Optional. Number of fractional seconds digits (0-9). Default value is 0.

**Return Type**

`TIME` (not null)

### LOCALTIMESTAMP

Returns the current timestamp in the session's local time zone.

```sql
LOCALTIMESTAMP
LOCALTIMESTAMP( precision )
```

**Arguments**

- precision - Optional. Number of fractional seconds digits (0-9). Default value is 0.

**Return Type**

`TIMESTAMP` (not null)

### MINUTE

Returns the minute (0-59) from a time or timestamp.

```sql
MINUTE( time )
```

**Arguments**

- time - Time or timestamp expression to extract minute from. Accepts `TIME` or `TIMESTAMP` types.

**Return Type**

`BIGINT` (nullable)

### MONTH

Returns the month (1-12) from a date.

```sql
MONTH( date )
```

**Arguments**

- date - Date or timestamp expression to extract month from. Accepts `DATE` or `TIMESTAMP` types.

**Return Type**

`BIGINT` (nullable)

### MONTHNAME

Returns the name of the month (e.g., 'January', 'February') for a given date.

```sql
MONTHNAME( date )
```

**Arguments**

- date - Date or timestamp expression to get month name from. Accepts `DATE` or `TIMESTAMP` types.

**Return Type**

`VARCHAR` (nullable)

### QUARTER

Returns the quarter (1-4) from a date.

```sql
QUARTER( date )
```

**Arguments**

- date - Date or timestamp expression to extract quarter from. Accepts `DATE` or `TIMESTAMP` types.

**Return Type**

`BIGINT` (nullable)

### SECOND

Returns the second (0-59) from a time or timestamp.

```sql
SECOND( time )
```

**Arguments**

- time - Time or timestamp expression to extract second from. Accepts `TIME` or `TIMESTAMP` types.

**Return Type**

`BIGINT` (nullable)

### TIMESTAMPADD

Adds a specified number of time units to a datetime value.

```sql
TIMESTAMPADD( timeUnit, count, datetime )
```

**Arguments**

- timeUnit - Time unit to add: `YEAR`, `QUARTER`, `MONTH`, `WEEK`, `DAY`, `HOUR`, `MINUTE`, `SECOND`, `MILLISECOND`, `MICROSECOND`.
- count - Number of time units to add to datetime. Accepts `INTEGER` type (can be negative).
- datetime - Timestamp expression to add time units to. Accepts `TIMESTAMP` data type.

**Return Type**

`TIMESTAMP` (nullable)

### TIMESTAMPDIFF

Returns the difference between two datetime values in the specified time unit.

```sql
TIMESTAMPDIFF( timeUnit, datetime1, datetime2 )
```

**Arguments**

- timeUnit - Time unit for difference: `YEAR`, `QUARTER`, `MONTH`, `WEEK`, `DAY`, `HOUR`, `MINUTE`, `SECOND`, `MILLISECOND`, `MICROSECOND`.
- datetime1 - First timestamp to compare. Accepts `TIMESTAMP` data type.
- datetime2 - Second timestamp to compare. Accepts `TIMESTAMP` data type.

**Return Type**

`INTEGER` (nullable) - Returns `datetime2 - datetime1` value

### TIMESTAMP_MICROS

Converts microseconds since 1970-01-01 00:00:00 UTC (Unix epoch) to a timestamp.

```sql
TIMESTAMP_MICROS( microseconds )
```

**Arguments**

- microseconds - Number of microseconds since Unix epoch (1970-01-01 00:00:00 UTC). Accepts `BIGINT` type.

**Return Type**

`TIMESTAMP` (nullable)

### TIMESTAMP_MILLIS

Converts milliseconds since 1970-01-01 00:00:00 UTC (Unix epoch) to a timestamp.

```sql
TIMESTAMP_MILLIS( milliseconds )
```

**Arguments**

- milliseconds - Number of milliseconds since Unix epoch (1970-01-01 00:00:00 UTC). Accepts `BIGINT` type.

**Return Type**

`TIMESTAMP` (nullable)

### TIMESTAMP_SECONDS

Converts seconds since 1970-01-01 00:00:00 UTC (Unix epoch) to a timestamp.

```sql
TIMESTAMP_SECONDS( seconds )
```

**Arguments**

- seconds - Number of seconds since Unix epoch (1970-01-01 00:00:00 UTC). Accepts `BIGINT` type.

**Return Type**

`TIMESTAMP` (nullable)

### UNIX_DATE

Converts a date to days since 1970-01-01 (Unix epoch).

```sql
UNIX_DATE( date )
```

**Arguments**

- date - Date expression to convert to Unix epoch days. Accepts `DATE` type.

**Return Type**

`INTEGER` (nullable)

### UNIX_MICROS

Converts a timestamp to microseconds since 1970-01-01 00:00:00 UTC (Unix epoch).

```sql
UNIX_MICROS( timestamp )
```

**Arguments**

- timestamp - Timestamp expression to convert to microseconds. Accepts `TIMESTAMP` data type.

**Return Type**

`BIGINT` (nullable)

### UNIX_MILLIS

Converts a timestamp to milliseconds since 1970-01-01 00:00:00 UTC (Unix epoch).

```sql
UNIX_MILLIS( timestamp )
```

**Arguments**

- timestamp - Timestamp expression to convert to milliseconds. Accepts `TIMESTAMP` data type.

**Return Type**

`BIGINT` (nullable)

### UNIX_SECONDS

Converts a timestamp to seconds since 1970-01-01 00:00:00 UTC (Unix epoch).

```sql
UNIX_SECONDS( timestamp )
```

**Arguments**

- timestamp - Timestamp expression to convert to seconds. Accepts `TIMESTAMP` data type.

**Return Type**

`BIGINT` (nullable)

### WEEK

Returns the week of the year (1-53) from a date.

```sql
WEEK( date )
```

**Arguments**

- date - Date or timestamp expression to extract week from. Accepts `DATE` or `TIMESTAMP` types.

**Return Type**

`BIGINT` (nullable)

### YEAR

Returns the year from a date.

```sql
YEAR( date )
```

**Arguments**

- date - Date or timestamp expression to extract year from. Accepts `DATE` or `TIMESTAMP` types.

**Return Type**

`BIGINT` (nullable)

## JSON Functions

### IS_JSON_ARRAY

Tests whether a string is a valid JSON array.

```sql
expression IS JSON ARRAY
```

**Arguments**

- expression - String expression to test for JSON array format. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`BOOLEAN` (not null)

### IS_JSON_OBJECT

Tests whether a string is a valid JSON object.

```sql
expression IS JSON OBJECT
```

**Arguments**

- expression - String expression to test for JSON object format. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`BOOLEAN` (not null)

### IS_JSON_SCALAR

Tests whether a string is a valid JSON scalar (string, number, boolean, or null).

```sql
expression IS JSON SCALAR
```

**Arguments**

- expression - String expression to test for JSON scalar format. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`BOOLEAN` (not null)

### IS_JSON_VALUE

Tests whether a string is a valid JSON scalar value.

```sql
expression IS JSON VALUE
```

**Arguments**

- expression - String expression to test for JSON scalar value. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`BOOLEAN` (not null)

### IS_NOT_JSON_ARRAY

Tests whether a string is not a valid JSON array.

```sql
expression IS NOT JSON ARRAY
```

**Arguments**

- expression - String expression to test for non-JSON array format. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`BOOLEAN` (not null)

### IS_NOT_JSON_OBJECT

Tests whether a string is not a valid JSON object.

```sql
expression IS NOT JSON OBJECT
```

**Arguments**

- expression - String expression to test for non-JSON object format. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`BOOLEAN` (not null)

### IS_NOT_JSON_SCALAR

Tests whether a string is not a valid JSON scalar.

```sql
expression IS NOT JSON SCALAR
```

**Arguments**

- expression - String expression to test for non-JSON scalar format. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`BOOLEAN` (not null)

### IS_NOT_JSON_VALUE

Tests whether a string is not a valid JSON scalar value.

```sql
expression IS NOT JSON VALUE
```

**Arguments**

- expression - String expression to test for non-JSON scalar value. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`BOOLEAN` (not null)

### JSON_ARRAY

Constructs a JSON array from values.

```sql
JSON_ARRAY( [ value1 [, value2 ]... ]
  [ NULL ON NULL | ABSENT ON NULL ] )
```

**Arguments**

- value - One or more values to include in the array. Accepts any data type.
- NULL ON NULL - Default. Include null values in the resulting JSON array.
- ABSENT ON NULL - Omit null values from the resulting JSON array.

**Return Type**

`VARCHAR` containing JSON array

### JSON_DEPTH

Returns the maximum depth of a JSON document.

```sql
JSON_DEPTH( json_doc )
```

**Arguments**

- json_doc - JSON document string to measure depth. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`INTEGER` (nullable)

### JSON_EXISTS

Tests whether a JSON path returns any items.

```sql
JSON_EXISTS( json_doc, path
  [ { ERROR | TRUE | FALSE | UNKNOWN } ON ERROR ] )
```

**Arguments**

- json_doc - JSON document string to search. Accepts `VARCHAR` or `CHAR` data types.
- path - JSON path expression specifying the location to check.
- ON ERROR - Optional. Behavior when error occurs: ERROR (raise error, default), TRUE, FALSE, or UNKNOWN.

**Return Type**

`BOOLEAN` (nullable)

### JSON_KEYS

Returns the keys from a JSON object as a JSON array.

```sql
JSON_KEYS( json_doc )
JSON_KEYS( json_doc, path )
```

**Arguments**

- json_doc - JSON object string to extract keys from. Accepts `VARCHAR` or `CHAR` data types.
- path - Optional. JSON path specifying object location. Default values is the root.

**Return Type**

`VARCHAR` (nullable) containing JSON array

### JSON_LENGTH

Returns the length (number of elements) of a JSON document.

```sql
JSON_LENGTH( json_doc )
JSON_LENGTH( json_doc, path )
```

**Arguments**

- json_doc - JSON document string to measure. Accepts `VARCHAR` or `CHAR` data types.
- path - Optional. JSON path specifying location to measure. Default values is the root.

**Return Type**

`INTEGER` (nullable)

### JSON_OBJECT

Constructs a JSON object from key-value pairs.

```sql
JSON_OBJECT( [ KEY key1 VALUE value1 [, KEY key2 VALUE value2 ]... ]
  [ NULL ON NULL | ABSENT ON NULL ] )
```

**Arguments**

- key - String expression used as keys in the JSON object. Accepts `VARCHAR` or `CHAR` data types.
- value - Values to associate with keys. Accepts any data type.
- NULL ON NULL - Default. Include null values in the resulting JSON object.
- ABSENT ON NULL - Omit key-value pairs where value is null.

**Return Type**

`VARCHAR` containing JSON object

### JSON_PRETTY

Returns a pretty-printed (formatted) version of a JSON document.

```sql
JSON_PRETTY( json_doc )
```

**Arguments**

- json_doc - JSON document string to format with indentation. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`VARCHAR` (nullable)

### JSON_QUERY

Extracts a JSON object or array from a JSON document.

```sql
JSON_QUERY( json_doc, path
  [ { WITHOUT [ ARRAY ] | WITH [ CONDITIONAL | UNCONDITIONAL ] [ ARRAY ] } WRAPPER ]
  [ { ERROR | NULL | EMPTY ARRAY | EMPTY OBJECT } ON EMPTY ]
  [ { ERROR | NULL | EMPTY ARRAY | EMPTY OBJECT } ON ERROR ] )
```

**Arguments**

- json_doc - JSON document string to query. Accepts `VARCHAR` or `CHAR` data types.
- path - JSON path expression specifying location to extract.
- WRAPPER - Optional. Controls array wrapping: `WITHOUT`, `WITH CONDITIONAL`, or `WITH UNCONDITIONAL` .
- ON EMPTY - Optional. Behavior when path returns empty: `ERROR`, `NULL`, `EMPTY ARRAY`, `EMPTY OBJECT`.
- ON ERROR - Optional. Behavior on error: `ERROR`, `NULL`, `EMPTY ARRAY`, `EMPTY OBJECT`.

**Return Type**

`VARCHAR` (nullable) containing JSON

### JSON_REMOVE

Removes elements from a JSON document at specified paths.

```sql
JSON_REMOVE( json_doc, path [, path, ...] )
```

**Arguments**

- json_doc - JSON document string to modify. Accepts `VARCHAR` or `CHAR` data types.
- path - One or more JSON paths specifying elements to remove from the document.

**Return Type**

`VARCHAR` (nullable) containing modified JSON

### JSON_STORAGE_SIZE

Returns the approximate storage size in bytes of a JSON document.

```sql
JSON_STORAGE_SIZE( json_doc )
```

**Arguments**

- json_doc - JSON document string to measure storage size. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`INTEGER` (nullable)

### JSON_TYPE

Returns the type of a JSON value as a string.

```sql
JSON_TYPE( json_value )
```

**Arguments**

- json_value - JSON expression to check type. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`VARCHAR` (nullable) - Returns `OBJECT`, `ARRAY`, `STRING`, `NUMBER`, `BOOLEAN`, or `NULL` for invalid JSON

### JSON_VALUE

Extracts a scalar value from a JSON document.

```sql
JSON_VALUE( json_doc, path [ RETURNING data_type ]
  [ { ERROR | NULL | DEFAULT default_value } ON EMPTY ]
  [ { ERROR | NULL | DEFAULT default_value } ON ERROR ] )
```

**Arguments**

- json_doc - JSON document string to extract value from. Accepts `VARCHAR` or `CHAR` data types.
- path - JSON path expression specifying scalar value location.
- data_type - Optional. Target return data type (e.g., `INTEGER`, `VARCHAR`). Default value is `VARCHAR`.
- ON EMPTY - Optional. Behavior when path returns empty: `ERROR`, `NULL`, or `DEFAULT` with value.
- ON ERROR - Optional. Behavior on error: `ERROR`, `NULL`, or `DEFAULT` with value.

**Return Type**

`VARCHAR` (nullable) or specified data type

## Numeric Functions

### ABS

Returns the absolute value of a numeric value.

```sql
ABS( numeric )
```

**Arguments**

- numeric - Numeric expression to get absolute value. Accepts `TINYINT`, `SMALLINT`, `INTEGER`, `BIGINT`, `DECIMAL`, `REAL`, `FLOAT`, `DOUBLE`.

**Return Type**

Same type as input (nullable)

### ACOS

Returns the arc cosine of a numeric value. The value must be between -1 and 1.

```sql
ACOS( numeric )
```

**Arguments**

- numeric - Numeric expression for arc cosine calculation. Must be between -1 and 1. Accepts numeric data types.

**Return Type**

`DOUBLE` (nullable) - Result in radians

### ASIN

Returns the arc sine of a numeric value. The value must be between -1 and 1.

```sql
ASIN( numeric )
```

**Arguments**

- numeric - Numeric expression for arc sine calculation. Must be between -1 and 1. Accepts numeric data types.

**Return Type**

`DOUBLE` (nullable) - Result in radians

### ATAN

Returns the arc tangent of a numeric value.

```sql
ATAN( numeric )
```

**Arguments**

- numeric - Numeric expression for arc tangent calculation. Accepts numeric data types.

**Return Type**

`DOUBLE` (nullable) - Result in radians

### ATAN2

Returns the arc tangent of y/x, using the signs of both arguments to determine the quadrant.

```sql
ATAN2( y, x )
```

**Arguments**

- y - Y-coordinate value for arc tangent calculation. Accepts numeric data types.
- x - X-coordinate value for arc tangent calculation. Accepts numeric data types.

**Return Type**

`DOUBLE` (nullable) - Result in radians

### CBRT

Returns the cube root of a numeric value.

```sql
CBRT( numeric )
```

**Arguments**

- numeric - Numeric expression to calculate cube root. Accepts numeric data types.

**Return Type**

`DOUBLE` (nullable)

### COS

Returns the cosine of a numeric value (in radians).

```sql
COS( numeric )
```

**Arguments**

- numeric - Angle in radians for cosine calculation. Accepts numeric data types.

**Return Type**

`DOUBLE` (nullable)

### COSH

Returns the hyperbolic cosine of a numeric value.

```sql
COSH( numeric )
```

**Arguments**

- numeric - Numeric expression for hyperbolic cosine calculation. Accepts numeric data types.

**Return Type**

`DOUBLE` (nullable)

### COT

Returns the cotangent of a numeric value (in radians).

```sql
COT( numeric )
```

**Arguments**

- numeric - Angle in radians for cotangent calculation. Accepts numeric data types.

**Return Type**

`DOUBLE` (nullable)

### DEGREES

Converts radians to degrees.

```sql
DEGREES( radians )
```

**Arguments**

- radians - Angle value in radians to convert to degrees. Accepts numeric data types.

**Return Type**

`DOUBLE` (nullable)

### EXP

Returns e raised to the power of the numeric value.

```sql
EXP( numeric )
```

**Arguments**

- numeric - Exponent value for `e^x` calculation. Accepts numeric data types.

**Return Type**

`DOUBLE` (nullable)

### LN

Returns the natural logarithm (base e) of a numeric value.

```sql
LN( numeric )
```

**Arguments**

- numeric - Positive numeric expression for natural logarithm. Must be more than 0. Accepts numeric data types.

**Return Type**

`DOUBLE` (nullable)

### LOG10

Returns the base 10 logarithm of a numeric value.

```sql
LOG10( numeric )
```

**Arguments**

- numeric - Positive numeric expression for base 10 logarithm. Must be more than 0. Accepts numeric data types.

**Return Type**

`DOUBLE` (nullable)

### MOD

Returns the remainder of dividend divided by divisor.

```sql
MOD( dividend, divisor )
```

**Arguments**

- dividend - Numeric expression to be divided (numerator). Accepts numeric data types.
- divisor - Numeric expression to divide by (denominator). Must not be zero. Accepts numeric data types.

**Return Type**

Same type as inputs (nullable)

### PI

Returns the mathematical constant π (pi).

```sql
PI()
```

**Arguments**

None

**Return Type**

`DOUBLE` (not null) - Approximately 3.141592653589793

### POWER

Returns base raised to the power of exponent.

```sql
POWER( base, exponent )
```

**Arguments**

- base - Base value for power calculation. Accepts numeric data types.
- exponent - Exponent value to raise base to. Accepts numeric data types.

**Return Type**

`DOUBLE` (nullable)

### RADIANS

Converts degrees to radians.

```sql
RADIANS( degrees )
```

**Arguments**

- degrees - Angle value in degrees to convert to radians. Accepts numeric data types.

**Return Type**

`DOUBLE` (nullable)

### RAND

Returns a random `DOUBLE` value between 0.0 (inclusive) and 1.0 (exclusive).

```sql
RAND()
RAND( seed )
```

**Arguments**

- seed - Optional. Seed value for reproducible random number generation. Accepts `INTEGER` type.

**Return Type**

`DOUBLE` (not null)

### RAND_INTEGER

Returns a random INTEGER value between 0 (inclusive) and bound (exclusive).

```sql
RAND_INTEGER( bound )
RAND_INTEGER( seed, bound )
```

**Arguments**

- seed - Optional. Seed value for reproducible random number generation. Accepts `INTEGER` type.
- bound - Upper bound for random integer (exclusive). Result will be less than bound. Accepts `INTEGER` type.

**Return Type**

`INTEGER` (not null)

### ROUND

Rounds a numeric value to a specified number of decimal places.

```sql
ROUND( numeric )
ROUND( numeric, scale )
```

**Arguments**

- numeric - Numeric expression to round. Accepts `TINYINT`, `SMALLINT`, `INTEGER`, `BIGINT`, `DECIMAL`, `REAL`, `FLOAT`, `DOUBLE`.
- scale - Optional. Number of decimal places to round to. Accepts `INTEGER`. Default value is 0.

**Return Type**

For single argument (no scale specified):

- Same type as input with scale set to 0
- Preserves precision and nullability

For two arguments (scale specified):

- Same type as input
- Preserves precision, uses specified scale, and nullability

### SIGN

Returns the sign of a numeric value: -1 for negative, 0 for zero, 1 for positive.

```sql
SIGN( numeric )
```

**Arguments**

- numeric - Numeric expression to get sign. Accepts numeric data types.

**Return Type**

Same type as input (nullable)

### SIN

Returns the sine of a numeric value (in radians).

```sql
SIN( numeric )
```

**Arguments**

- numeric - Angle in radians for sine calculation. Accepts numeric data types.

**Return Type**

`DOUBLE` (nullable)

### SINH

Returns the hyperbolic sine of a numeric value.

```sql
SINH( numeric )
```

**Arguments**

- numeric - Numeric expression for hyperbolic sine calculation. Accepts numeric data types.

**Return Type**

`DOUBLE` (nullable)

### SQRT

Returns the square root of a numeric value.

```sql
SQRT( numeric )
```

**Arguments**

- numeric - Non-negative numeric expression for square root. Must be more than or equal to 0. Accepts numeric data types.

**Return Type**

`DOUBLE` (nullable)

### TAN

Returns the tangent of a numeric value (in radians).

```sql
TAN( numeric )
```

**Arguments**

- numeric - Angle in radians for tangent calculation. Accepts numeric data types.

**Return Type**

`DOUBLE` (nullable)

### TANH

Returns the hyperbolic tangent of a numeric value.

```sql
TANH( numeric )
```

**Arguments**

- numeric - Numeric expression for hyperbolic tangent calculation. Accepts numeric data types.

**Return Type**

`DOUBLE` (nullable)

### TRUNCATE

Truncates a numeric value to a specified number of decimal places.

```sql
TRUNCATE( numeric )
TRUNCATE( numeric, scale )
```

**Arguments**

- numeric - Numeric expression to truncate. Accepts `TINYINT`, `SMALLINT`, `INTEGER`, `BIGINT`, `DECIMAL`, `REAL`, `FLOAT`, `DOUBLE`.
- scale - Optional. Number of decimal places to truncate to. Accepts `INTEGER`. Default value is 0.

**Return Type**

For single argument (no scale specified):

- Same type as input with scale set to 0
- Preserves precision and nullability

For two arguments (scale specified):

- Same type as input
- Preserves precision, uses specified scale, and nullability

## Other Functions

### CASE

Returns a value based on conditional logic.

```sql
CASE
  WHEN condition1 THEN result1
  [ WHEN condition2 THEN result2 ]
  ...
  [ ELSE default_result ]
END

CASE expression
  WHEN value1 THEN result1
  [ WHEN value2 THEN result2 ]
  ...
  [ ELSE default_result ]
END
```

**Arguments**

- condition - Boolean expressions that are evaluated in order until one returns `TRUE`.
- expression - Expression to compare against values in the simple `CASE` form.
- value - Values to compare with expression in the simple `CASE` form.
- result - Result values returned when condition/value matches. Must be compatible types.
- default_result - Optional. Default value returned when no conditions match.

**Return Type**

Least restrictive type of all result expressions (nullable if no `ELSE` clause)

### CAST

Converts an expression from one data type to another.

```sql
CAST( expression AS target_type [FORMAT format_string] )
```

**Arguments**

- expression - Expression to convert. Accepts any data type.
- target_type - Target data type for conversion (e.g., `INTEGER`, `VARCHAR`, `DECIMAL`, `DATE`, `TIMESTAMP`).
- format_string - Optional. Format pattern for datetime conversions. Accepts `VARCHAR` data type with datetime format patterns according to SQL 2016 format (for example, 'YYYY-MM-DD', 'HH24:MI:SS', 'HH24;MI').

**Return Type**

The specified target type

### COALESCE

Returns the first non-null value from the list of arguments.

```sql
COALESCE( value1, value2 [, value3, ...] )
```

**Arguments**

- value1, value2, ... - Two or more expressions of compatible types to evaluate from left to right.

**Return Type**

Least restrictive type of all arguments (nullable)

### DECODE

Compares expression to each search value. Returns the corresponding result for the first match, or default if no match.

```sql
DECODE( expression, search1, result1 [, search2, result2 ]... [, default ] )
```

**Arguments**

- expression - Expression to compare against search values. Accepts any comparable type.
- search - One or more values to compare against expression.
- result - Result values returned when expression matches corresponding search value.
- default - Optional. Default value returned when no search values match.

**Return Type**

Least restrictive type of all result values (nullable if odd number of arguments)

### GREATEST

Returns the largest value from a list of values.

```sql
GREATEST( value1, value2 [, value3, ...] )
```

**Arguments**

- value1, value2, ... - Two or more expressions of comparable types (numeric, string, date/time).

**Return Type**

Least restrictive type of all arguments (nullable)

### INFIX_CAST

Cast operator. Converts an expression to a different type.

```sql
expression :: type
```

**Arguments**

- expression - Expression to convert. Accepts any data type.
- type - Target data type for conversion (e.g., `INTEGER`, `VARCHAR`, `DECIMAL`, `DATE`, `TIMESTAMP`).

**Return Type**

The specified target type

### LEAST

Returns the smallest value from a list of values.

```sql
LEAST( value1, value2 [, value3, ...] )
```

**Arguments**

- value1, value2, ... - Two or more expressions of comparable types (numeric, string, date/time).

**Return Type**

Least restrictive type of all arguments (nullable)

### NULLIF

Returns null if value1 equals value2, otherwise returns value1.

```sql
NULLIF( value1, value2 )
```

**Arguments**

- value1 - First expression to compare. Accepts any comparable type.
- value2 - Second expression to compare with value1. Must be comparable to value1.

**Return Type**

Same type as value1 (nullable)

### NVL

Returns value if not null, otherwise returns default_value.

```sql
NVL( value, default_value )
```

**Arguments**

- value - Expression to evaluate. Accepts any data type.
- default_value - Value returned if value is null. Must be compatible with value's type.

**Return Type**

Least restrictive type of both arguments (nullable)

### RAND_UUID

Generates a random UUID (Universally Unique Identifier).

```sql
RAND_UUID()
```

**Arguments**

None

**Return Type**

`UUID`

{% hint style="info" %}
This function is non-deterministic and dynamic.
{% endhint %}

### SYSTEM_RANGE

Generates a table of integer values from start to end with an optional step.

```sql
SYSTEM_RANGE( start, end )
SYSTEM_RANGE( start, end, step )
```

**Arguments**

- start - Starting value for range (inclusive). Accepts `BIGINT` type.
- end - Ending value for range (inclusive). Accepts `BIGINT` type.
- step - Optional. Increment value for each step. Accepts `BIGINT` type. Default value is 1.

**Return Type**

Table function returning a table with single `BIGINT` column

### TYPEOF

Returns the SQL type name of an expression as a string.

```sql
TYPEOF( expression )
```

**Arguments**

- expression - Expression to check type. Accepts any data type.

**Return Type**

`VARCHAR(2000)`

## Regular Expression Functions

### REGEXP_REPLACE

Replaces occurrences of a regular expression pattern with flags.

```sql
REGEXP_REPLACE( string, pattern )
REGEXP_REPLACE( string, pattern, replacement )
REGEXP_REPLACE( string, pattern, replacement, position )
REGEXP_REPLACE( string, pattern, replacement, position, occurrence )
REGEXP_REPLACE( string, pattern, replacement, position, occurrence, flags )
```

**Arguments**

- string - Original string to search. Accepts `VARCHAR` or `CHAR` data types.
- pattern - Regular expression pattern to match. Accepts `VARCHAR` type.
- replacement - Optional. String to replace matches with. Accepts `VARCHAR` type. Empty string by default.
- position - Optional. Starting position for search (1-based). Accepts `INTEGER` type. Default value is 1.
- occurrence - Optional. Which occurrence to replace (0 for all). Accepts `INTEGER` type. Default value is 0.
- flags - Optional. Regex flags (e.g., 'i' for case-insensitive). Accepts `VARCHAR` type. Empty by default.

**Return Type**

`VARCHAR` (nullable)

### POSIX_REGEX

Matches a string against a regular expression pattern using the [POSIX syntax](https://pubs.opengroup.org/onlinepubs/9699919799/basedefs/V1_chap09.html).

The following operators are supported:

- Case-sensitive comparison:

  ```
  <string> ~ <pattern>
  ```
- Case-insensitive comparison:

  ```
  <string> ~* <pattern>
  ```
- Negative case-sensitive comparison:

  ```
  <string> !~ <pattern>
  ```
- Negative case-insensitive comparison:

  ```
  <string> !~* <pattern>
  ```

**Arguments**

- string - String to match against. Accepts `VARCHAR` or `CHAR` data types.
- pattern - Regular expression pattern to match. Accepts `VARCHAR` type.

**Return Type**

`BOOLEAN` (nullable)

## Security Functions

### CURRENT_USER

Returns the username of the current database session.

```sql
CURRENT_USER
```

**Arguments**

None

**Return Type**

`VARCHAR` (not null)

## Sequence Functions

### CURRVAL

Returns the current value of a sequence without advancing it.

```sql
CURRVAL( sequence_name )
```

**Arguments**

- sequence_name - Name of the sequence to query. Accepts `VARCHAR` type with sequence identifier.

**Return Type**

`BIGINT` (not null)

### NEXTVAL

Advances the sequence to its next value and returns the new value.

```sql
NEXTVAL( sequence_name )
```

**Arguments**

- sequence_name - Name of the sequence to advance. Accepts `VARCHAR` type with sequence identifier.

**Return Type**

`BIGINT` (not null)

### SETVAL

Sets the current value of a sequence to the specified value.

```sql
SETVAL( sequence_name, value )
```

**Arguments**

- sequence_name - Name of the sequence to modify. Accepts `VARCHAR` type with sequence identifier.
- value - New value to set for the sequence. Accepts `BIGINT` type.

**Return Type**

`BIGINT` (not null) - Returns the value that was set

## String Functions

### ASCII

Returns the ASCII code of the first character in a string.

```sql
ASCII( string )
```

**Arguments**

- string - Character string expression to get ASCII code from. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`INTEGER` (nullable)

### CHAR_LENGTH

Returns the number of characters in a string.

```sql
CHAR_LENGTH( string )
```

**Arguments**

- string - Character string expression to measure. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`INTEGER` (nullable)

### CHARACTER_LENGTH

Returns the number of characters in a string. Identical to `CHAR_LENGTH`.

```sql
CHARACTER_LENGTH( string )
```

**Arguments**

- string - Character string expression to measure. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`INTEGER` (nullable)

### CHR

Returns the character with the specified ASCII/Unicode code.

```sql
CHR( code )
```

**Arguments**

- code - Integer code value to convert to character. Accepts `INTEGER` type for ASCII/Unicode.

**Return Type**

`CHAR(1)` (nullable)

### COMPRESS

Compresses a string using gzip compression.

```sql
COMPRESS( string )
```

**Arguments**

- string - String expression to compress using gzip. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`VARBINARY` (nullable)

### CONCAT

Concatenates two or more strings. This is the operator form of (string1 || string2) expression.

```sql
CONCAT( string1, string2 [, string3, ...] )
```

**Arguments**

- string1, string2, ... - Two or more character string expressions to concatenate. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`VARCHAR` (nullable)

### DIFFERENCE

Returns the difference between the Soundex codes of two strings (0-4, where 4 indicates most similar).

```sql
DIFFERENCE( string1, string2 )
```

**Arguments**

- string1 - First string to compare using Soundex algorithm. Accepts `VARCHAR` or `CHAR` data types.
- string2 - Second string to compare using Soundex algorithm. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`INTEGER` (nullable)

### FROM_BASE64

Decodes a Base64-encoded string to binary data.

```sql
FROM_BASE64( string )
```

**Arguments**

- string - Base64-encoded string to decode. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`VARBINARY` (nullable)

### INITCAP

Converts the first letter of each word to uppercase and the rest to lowercase.

```sql
INITCAP( string )
```

**Arguments**

- string - Character string expression to capitalize. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`VARCHAR` (nullable) - Same length as input

### LEFT

Returns the leftmost `length` characters from a string.

```sql
LEFT( string, length )
```

**Arguments**

- string - Character string expression to extract from. Accepts `VARCHAR`, `VARBINARY` or `CHAR` data types.
- length - Number of characters to return from left. Accepts `INTEGER` type.

**Return Type**

`VARCHAR` (nullable)

### LENGTH

Returns the number of characters in a string or the number of bytes in a binary value.

```sql
LENGTH( string | binary )
```

**Arguments**

- string - Character string expression to measure. Accepts `VARCHAR` or `CHAR` data types.
- binary - Binary expression to measure bytes. Accepts `VARBINARY` or `BINARY` types.

**Return Type**

`INTEGER` (nullable)

### LOWER

Converts all characters in a string to lowercase.

```sql
LOWER( string )
```

**Arguments**

- string - Character string expression to convert. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`VARCHAR` (nullable) - Same length as input

### LTRIM

Removes leading whitespace from a string.

```sql
LTRIM( string )
```

**Arguments**

- string - Character string expression to trim. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`VARCHAR` (nullable)

### MD5

Computes the MD5 hash of a string or binary value.

```sql
MD5( string | binary )
```

**Arguments**

- string - String expression to hash. Accepts `VARCHAR` or `CHAR` data types.
- binary - Binary expression to hash. Accepts `VARBINARY` or `BINARY` types.

**Return Type**

`VARCHAR(32)` (nullable) - Hexadecimal string representation

### OCTET_LENGTH

Returns the number of bytes in a string or binary value.

```sql
OCTET_LENGTH( string | binary )
```

**Arguments**

- string - Character string expression to measure bytes. Accepts `VARCHAR` or `CHAR` data types.
- binary - Binary expression to measure bytes. Accepts `VARBINARY` or `BINARY` types.

**Return Type**

`INTEGER` (nullable)

### OVERLAY

Replaces part of a string with another string.

```sql
OVERLAY( string PLACING replacement FROM position )
OVERLAY( string PLACING replacement FROM position FOR length )
```

**Arguments**

- string - Original string to modify. Accepts `VARCHAR` or `CHAR` data types.
- replacement - Replacement string to insert. Accepts `VARCHAR` or `CHAR` data types.
- position - Starting position for replacement (1-based). Accepts `INTEGER` type.
- length - Optional. Number of characters to replace. Default value is the length of the replacement argument.

**Return Type**

`VARCHAR` (nullable)

### POSITION

Returns the position of a substring within a string.

```sql
POSITION( substring IN string [FROM start_position])
```

**Arguments**

- substring - Substring to search for. Accepts `VARCHAR` or `CHAR` data types.
- string - String to search within. Accepts `VARCHAR` or `CHAR` data types.
- start_position - Optional. Starting position (1-based, inclusive) from which to begin the search. Accepts `INTEGER` data type.

**Return Type**

`INTEGER` (nullable) - Position (1-based), or 0 if not found

### REPEAT

Repeats a string a specified number of times.

```sql
REPEAT( string, count )
```

**Arguments**

- string - Character string expression to repeat. Accepts `VARCHAR` or `CHAR` data types.
- count - Number of times to repeat string. Accepts `INTEGER` type.

**Return Type**

`VARCHAR` (nullable)

### REPLACE

Replaces all occurrences of a search string with a replacement string.

```sql
REPLACE( string, search, replacement )
```

**Arguments**

- string - Original string to modify. Accepts `VARCHAR` or `CHAR` data types.
- search - Substring to find and replace. Accepts `VARCHAR` or `CHAR` data types.
- replacement - Substring to replace with. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`VARCHAR` (nullable)

### REVERSE

Reverses a string.

```sql
REVERSE( string )
```

**Arguments**

- string - Character string expression to reverse. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`VARCHAR` (nullable)

### RIGHT

Returns the rightmost length characters from a string.

```sql
RIGHT( string, length )
```

**Arguments**

- string - Character string expression to extract from. Accepts `VARCHAR`, `VARBINARY` or `CHAR` data types.
- length - Number of characters to return from right. Accepts `INTEGER` type.

**Return Type**

`VARCHAR` (nullable)

### RTRIM

Removes trailing whitespace from a string.

```sql
RTRIM( string )
```

**Arguments**

- string - Character string expression to trim. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`VARCHAR` (nullable)

### SHA1

Computes the SHA-1 hash of a string or binary value.

```sql
SHA1( string | binary )
```

**Arguments**

- string - String expression to hash. Accepts `VARCHAR` or `CHAR` data types.
- binary - Binary expression to hash. Accepts `VARBINARY` or `BINARY` types.

**Return Type**

`VARCHAR(40)` (nullable) - Hexadecimal string representation

### SOUNDEX

Returns the Soundex code of a string (phonetic algorithm).

```sql
SOUNDEX( string )
```

**Arguments**

- string - Character string expression to encode. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`VARCHAR(4)` (nullable)

### SPACE

Returns a string consisting of count spaces.

```sql
SPACE( count )
```

**Arguments**

- count - Number of spaces to generate. Accepts `INTEGER` type.

**Return Type**

`VARCHAR` (nullable)

### STRCMP

Compares two strings lexicographically. Returns 0 if equal, negative if `string1 < string2`, positive if `string1 > string2`.

```sql
STRCMP( string1, string2 )
```

**Arguments**

- string1 - First string to compare. Accepts `VARCHAR` or `CHAR` data types.
- string2 - Second string to compare. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`INTEGER` (nullable)

### SUBSTR

Returns a substring of a string starting at a position. This function is identical to `SUBSTRING`.

```sql
SUBSTR( string, position )
SUBSTR( string, position, length )
```

**Arguments**

- string - Character string expression to extract from. Accepts `VARCHAR`, `VARBINARY` or `CHAR` data types.
- position - Starting position for extraction (1-based). Accepts `INTEGER` type.
- length - Optional. Number of characters to extract. Default values is the end of string.

**Return Type**

`VARCHAR` (nullable) - Same type as input string with varying length

### SUBSTRING

Returns a substring of a string starting at a position.

```sql
SUBSTRING( string FROM position )
SUBSTRING( string FROM position FOR length )
```

**Arguments**

- string - Character string expression to extract from. Accepts `VARCHAR`, `VARBINARY` or `CHAR` data types.
- position - Starting position for extraction (1-based). Accepts `INTEGER` type.
- length - Optional. Number of characters to extract. Default values is the end of string.

**Return Type**

`VARCHAR` (nullable) - Varying length

### TO_BASE64

Encodes binary data or a string to Base64 encoding.

```sql
TO_BASE64( binary | string )
```

**Arguments**

- binary - Binary expression to encode. Accepts `VARBINARY` or `BINARY` types.
- string - String expression to encode using UTF-8. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`VARCHAR` (nullable)

### TRANSLATE

Replaces characters in a string. Each character in from_string is replaced with the corresponding character in to_string.

```sql
TRANSLATE( string, from_string, to_string )
```

**Arguments**

- string - Original string to modify. Accepts `VARCHAR` or `CHAR` data types.
- from_string - Characters to find and replace. Accepts `VARCHAR` or `CHAR` data types.
- to_string - Replacement characters (by position). Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`VARCHAR` (nullable)

### TRIM

Removes leading and/or trailing characters from a string.

```sql
TRIM( [ [ LEADING | TRAILING | BOTH ] [ trim_character ] FROM ] string )
```

**Arguments**

- LEADING - Remove characters from start of string only.
- TRAILING - Remove characters from end of string only.
- BOTH - Remove characters from both ends of string (default behavior).
- trim_character - Optional. Character to remove. Default values is space.
- string - Character string expression to trim. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`VARCHAR` (nullable)

### UPPER

Converts all characters in a string to uppercase.

```sql
UPPER( string )
```

**Arguments**

- string - Character string expression to convert. Accepts `VARCHAR` or `CHAR` data types.

**Return Type**

`VARCHAR` (nullable) - Same length as input

## XML Functions

### EXISTS_NODE

Tests whether an XPath expression returns any nodes in an XML document.

```sql
EXISTS_NODE( xml_string, xpath )
EXISTS_NODE( xml_string, xpath, namespace )
```

**Arguments**

- xml_string - XML document string to search. Accepts `VARCHAR` or `CHAR` data types.
- xpath - XPath expression specifying node location to check.
- namespace - Optional. Namespace prefix mappings for XPath. Accepts VARCHAR values.

**Return Type**

`INTEGER` (nullable) - Returns 1 if nodes exist, 0 otherwise

### EXTRACT_VALUE

Extracts a value from an XML string using XPath.

```sql
EXTRACT_VALUE( xml_string, xpath )
```

**Arguments**

- xml_string - XML document string to extract from. Accepts `VARCHAR` or `CHAR` data types.
- xpath - XPath expression specifying value location to extract.

**Return Type**

`VARCHAR` (nullable)

### EXTRACT_XML

Extracts XML from an XML string using XPath with namespace support.

```sql
EXTRACT_XML( xml_string, xpath, namespace )
```

**Arguments**

- xml_string - XML document string to extract from. Accepts `VARCHAR` or `CHAR` data types.
- xpath - XPath expression specifying XML fragment location.
- namespace - Namespace prefix mappings for XPath. Accepts `VARCHAR` type.

**Return Type**

`VARCHAR` (nullable)

### XML_TRANSFORM

Transforms an XML string using XSLT.

```sql
XML_TRANSFORM( xml_string, xslt_string )
```

**Arguments**

- xml_string - XML document string to transform. Accepts `VARCHAR` or `CHAR` data types.
- xslt_string - XSLT stylesheet string defining transformation. Accepts `VARCHAR` type.

**Return Type**

`VARCHAR` (nullable)
