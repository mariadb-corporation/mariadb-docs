---
description: >-
  Reference of the SQL date and time functions supported by GridGain — current
  date/time, DATEADD, DATEDIFF, EXTRACT, formatting, and component extraction.
---

# Date and Time Functions

## CURRENT_DATE

### Description

Returns the current date. When called multiple times within a transaction, returns the same value.

```sql
{CURRENT_DATE [()] | CURDATE() | SYSDATE | TODAY}
```

### Example

Return the current date:

```sql
CURRENT_DATE()
```

## CURRENT_TIME

### Description

Returns the current time.

```sql
{CURRENT_TIME [ () ] | CURTIME()}
```

### Example

Return the current time:

```sql
CURRENT_TIME()
```

## CURRENT_TIMESTAMP

### Description

Returns the current timestamp. When called multiple times within a transaction, returns the same value.

```sql
{CURRENT_TIMESTAMP [([int])] | NOW([int])}
```

### Parameters

`int` - (optional) the precision parameter for nanoseconds - the number of digits after the decimal point (for example, 9 is nanoseconds)

### Example

Return the current timestamp:

```sql
CURRENT_TIMESTAMP()
```

## DATEADD | TIMESTAMPADD

### Description

Adds units to the timestamp or date (if the value is positive). Subtracts units from the timestamp or date (if the value is negative). The DATEADD function returns a `timestamp`. The TIMESTAMPADD function returns a `long`.

```sql
{DATEADD | TIMESTAMPADD} (unitString, addIntLong, timestamp)
```

### Parameters

- `unitString` - the unit to add or subtract (see the [EXTRACT](#extract) function for supported units)
- `addIntLong` - the number of units to add or subtract; may be `long` when manipulating milliseconds, `int` otherwise
- `timestamp` - the timestamp to add units to

### Example

Add 1 month to Jan 31 2021:

```sql
DATEADD('MONTH', 1, DATE '2001-01-31')
```

## DATEDIFF

### Description

Returns the number of specified units that differentiate between two timestamps as a `long`.

```sql
{DATEDIFF | TIMESTAMPDIFF} (unitString, aTimestamp, bTimestamp)
```

### Parameters

- `unitString` - the unit to consider (see the [EXTRACT](#extract) function for supported units)
- `aTimestamp` - the first timestamp to compare
- `bTimestamp` - the second timestamp to compare

### Example

Return the number of years that differentiate T1.CREATED from T2.CREATED:

```sql
DATEDIFF('YEAR', T1.CREATED, T2.CREATED)
```

## DAYNAME

### Description

Returns the name of the day of the week (in English).

```sql
DAYNAME(date)
```

### Parameters

`date` - the date to process

### Example

Return the day of the week for CREATED:

```sql
DAYNAME(CREATED)
```

## DAY_OF_MONTH

### Description

Returns the day of the month (1-31).

```sql
DAY_OF_MONTH(date)
```

### Parameters

`date` - the date to process

### Example

Return the day of the month for CREATED:

```sql
DAY_OF_MONTH(CREATED)
```

## DAY_OF_WEEK

### Description

Returns the day of the week (1-7, 1=Sunday).

```sql
DAY_OF_WEEK(date)
```

### Parameters

`date` - the date to process

### Example

Return the number of the day of the week for CREATED:

```sql
DAY_OF_WEEK(CREATED)
```

## DAY_OF_YEAR

### Description

Returns the day of the year (1-366).

```sql
DAY_OF_YEAR(date)
```

### Parameters

`date` - the date to process

### Example

Return the number of the day of the year for CREATED:

```sql
DAY_OF_YEAR(CREATED)
```

## EXTRACT

### Description

Returns a specific value from a timestamp as an `int`.

```sql
EXTRACT ({EPOCH | YEAR | YY | QUARTER | MONTH | MM | WEEK | ISO_WEEK
| DAY | DD | DAY_OF_YEAR | DOY | DAY_OF_WEEK | DOW | ISO_DAY_OF_WEEK
| HOUR | HH | MINUTE | MI | SECOND | SS | MILLISECOND | MS
| MICROSECOND | MCS | NANOSECOND | NS}
FROM timestamp)
```

### Parameters

`timestamp` - the timestamp to process

### Example

Extract the value of the 'seconds' part from CURRENT_TIMESTAMP:

```sql
EXTRACT(SECOND FROM CURRENT_TIMESTAMP)
```

## FORMATDATETIME

### Description

Formats a date, time, or timestamp as a `string`. The main format characters are: `y` year, `M` month, `d` day, `H` hour, `m` minute, and `s` second. For more details, see the [java.text.SimpleDateFormat method](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/text/SimpleDateFormat.html).

```sql
FORMATDATETIME (timestamp, formatString [,localeString [,timeZoneString]])
```

### Parameters

- `timestamp` - the timestamp to process
- `formatString` - the format to apply
- `localeString` - the name of the locale
- `timeZoneString` - the time zone

### Example

Format 2001-02-03 04:05:06 in English for GMT using the 'EEE, d MMM yyyy HH:mm:ss z' format:

```sql
FORMATDATETIME(TIMESTAMP '2001-02-03 04:05:06', 'EEE, d MMM yyyy HH:mm:ss z', 'en', 'GMT')
```

## HOUR

### Description

Returns the hour (0-23) from a timestamp.

```sql
HOUR(timestamp)
```

### Parameters

`timestamp` - the timestamp to process

### Example

Return the number of hours for CREATED:

```sql
HOUR(CREATED)
```

## MINUTE

### Description

Returns the minutes (0-59) from a timestamp.

```sql
MINUTE(timestamp)
```

### Parameters

`timestamp` - the timestamp to process

### Example

Return the number of minutes from CREATED:

```sql
MINUTE(CREATED)
```

## MONTH

### Description

Returns the month (1-12) from a timestamp.

```sql
MONTH(timestamp)
```

### Parameters

`timestamp` - the timestamp to process

### Example

Return the months from CREATED:

```sql
MONTH(CREATED)
```

## MONTHNAME

### Description

Returns the name of the month (in English).

```sql
MONTHNAME(date)
```

### Parameters

`date` - the date to process

### Example

Return the name of the month from CREATED:

```sql
MONTHNAME(CREATED)
```

## PARSEDATETIME

### Description

Parses a string and converts it to `timestamp`. The main characters in the string format are: `y` year, `M` month, `d` day, `H` hour, `m` minute, and `s` second. For more details, see the [java.text.SimpleDateFormat method](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/text/SimpleDateFormat.html).

```sql
PARSEDATETIME(string, formatString [, localeString [, timeZoneString]])
```

### Parameters

- `string` - the string top parse
- `formatString` - the string format
- `localeString` - the name of the locale
- `timeZoneString` - the time zone

### Example

Convert to `timestamp` the 'Sat, 3 Feb 2001 03:05:06 GMT':

```sql
PARSEDATETIME('Sat, 3 Feb 2001 03:05:06 GMT', 'EEE, d MMM yyyy HH:mm:ss z', 'en', 'GMT')
```

## QUARTER

### Description

Returns the quarter (1-4) from a timestamp.

```sql
QUARTER(timestamp)
```

### Parameters

`timestamp` - the timestamp to process

### Example

Return the quarter for CREATED:

```sql
QUARTER(CREATED)
```

## SECOND

### Description

Returns the second (0-59) from a timestamp.

```sql
SECOND(timestamp)
```

### Parameters

`timestamp` - the timestamp to process

### Example

Return the number of seconds for CREATED:

```sql
SECOND(CREATED)
```

## WEEK

### Description

Returns the week (1-53) from a timestamp using the current system locale.

```sql
WEEK(timestamp)
```

### Parameters

`timestamp` - the timestamp to process

### Example

Return the number of the week from CREATED:

```sql
WEEK(CREATED)
```

## YEAR

### Description

Returns the year from a timestamp.

```sql
YEAR(timestamp)
```

### Parameters

`timestamp` - the timestamp to process

### Example

Return the year from CREATED:

```sql
YEAR(CREATED)
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
