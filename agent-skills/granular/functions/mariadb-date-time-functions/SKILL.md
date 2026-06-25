---
name: mariadb-date-time-functions
description: "MariaDB date and time functions — current time (NOW, CURRENT_TIMESTAMP, SYSDATE, CURDATE, CURTIME, UTC_TIMESTAMP/UTC_DATE/UTC_TIME), arithmetic (DATE_ADD, DATE_SUB, ADDDATE, SUBDATE, INTERVAL units), differences (TIMESTAMPDIFF, TIMESTAMPADD, DATEDIFF, TIMEDIFF), extraction (EXTRACT, YEAR/MONTH/DAY/HOUR/MINUTE/SECOND/MICROSECOND, QUARTER, WEEK, DAYOFWEEK, WEEKDAY, LAST_DAY), parsing/formatting (STR_TO_DATE, DATE_FORMAT, GET_FORMAT), Unix time (UNIX_TIMESTAMP, FROM_UNIXTIME), time-zone conversion (CONVERT_TZ), construction (MAKEDATE, MAKETIME, SEC_TO_TIME), and Oracle-compat helpers (ADD_MONTHS, MONTHS_BETWEEN, TO_DATE). Use when computing, parsing, formatting, or converting dates, times, and timestamps in MariaDB."
---

# MariaDB Date and Time Functions

*Last updated: 2026-06-24*

Catalog of every built-in date/time function in MariaDB, with signature and a one-line semantic summary per entry. For a function not listed here, fall back to the canonical reference at <https://mariadb.com/docs/server/reference/sql-functions/date-time-functions>.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Functions with a `*(since X.Y)*` annotation are only available from that version onward; everything else is in every current LTS branch (10.6, 10.11, 11.4, 11.8).

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| `NOW()` and `SYSDATE()` are interchangeable | `NOW()` / `CURRENT_TIMESTAMP` are **constant for the whole statement** (statement-start time); `SYSDATE()` returns the **actual time when it executes** (two calls in one statement can differ), is non-deterministic, unsafe for statement-based replication, and prevents index use. Prefer `NOW()` |
| `NOW()` returns sub-second precision by default | Default fractional precision is **0** — sub-seconds are truncated. Use `NOW(6)` with a `DATETIME(6)`/`TIME(6)` column. Narrowing precision **truncates, not rounds** |
| `NOW()` / `CURDATE()` return UTC | They return the **session time zone** value (the `time_zone` variable, default `SYSTEM`). For UTC use `UTC_TIMESTAMP()` / `UTC_DATE()` / `UTC_TIME()` |
| `CONVERT_TZ(dt, 'UTC', 'Europe/Berlin')` works out of the box | Named zones require the time-zone tables to be **loaded** (`mariadb-tzinfo-to-sql`); with an unknown/unloaded zone `CONVERT_TZ` returns **`NULL`**. Numeric offsets like `'+00:00'` always work |
| `UNIX_TIMESTAMP()` / `FROM_UNIXTIME()` cap at 2038 | On 64-bit builds the max is `4294967295` = **`2106-02-07`** *(since 11.5)*; beyond it they return `NULL`. For dates past that, store a `DATETIME`, not a `TIMESTAMP`. `FROM_UNIXTIME()` applies the **session** time zone |
| `DAYOFWEEK()` and `WEEKDAY()` index the same way | They don't: `DAYOFWEEK()` is **1 = Sunday … 7 = Saturday**; `WEEKDAY()` is **0 = Monday … 6 = Sunday**. Mixing them shifts every weekday calculation |
| `WEEK(d)` gives an unambiguous week number | `WEEK()` depends on a **mode** argument (and `default_week_format` when omitted) for whether weeks start Sunday/Monday and whether week 1 must be full. Pass the mode explicitly |
| `DATE_ADD(d, 7)` adds 7 days | `DATE_ADD`/`DATE_SUB` need the `INTERVAL` form: `DATE_ADD(d, INTERVAL 7 DAY)` (or `d + INTERVAL 7 DAY`). Only `ADDDATE(d, 7)`/`SUBDATE(d, 7)` accept a bare-integer days argument |
| `TIMESTAMPDIFF(start, end, MONTH)` or guessing the order | Signature is `TIMESTAMPDIFF(unit, start, end)` returning **end − start** — the **unit comes first**. `TIMESTAMPADD(unit, n, datetime)` likewise takes the unit first and a plain number (no `INTERVAL`) |
| `STR_TO_DATE()` errors on input it can't parse | It returns **`NULL`** (with a warning) on a parse failure — guard for `NULL`. Its format specifiers (`%Y %m %d %H %i %s %f`) are shared with `DATE_FORMAT`; `%f` is microseconds |
| `ADD_MONTHS()` / `MONTHS_BETWEEN()` / `TRUNC()` only exist in Oracle mode | They're **always available**, in any `sql_mode`. Only **`TO_DATE()`** is Oracle-mode-specific (and new *(since 12.3)*). `ADD_MONTHS` clamps to the last day of a shorter target month |
| `DATE_FORMAT(d, '%Z')` / `'%z'` for a zone name/offset | The `%Z` (abbreviation) and `%z` (numeric offset) specifiers exist only *(since 11.3)* |

## Related concept pages

These aren't functions, so they aren't in the catalog below, but they underpin it:

- **Date and time units** — the `INTERVAL quantity unit` reference: the unit keywords (`MICROSECOND`…`YEAR`) and composite units (`DAY_SECOND`, `YEAR_MONTH`, …) used by `DATE_ADD`/`DATE_SUB`/`EXTRACT`/`TIMESTAMPADD`/`+ INTERVAL`.
- **Microseconds** — the fractional-seconds model: default precision 0, `DATETIME(N)`/`TIME(N)` for N up to 6, the `%f` specifier, and truncate-not-round.

## Functions

Auto-generated from the canonical `server/reference/sql-functions/date-time-functions/` pages by `agent-skills/extractor/extract_function_category.py`; regenerate when the doc tree changes. Do not hand-edit between the markers.

<!-- BEGIN GENERATED -->
<!-- Extracted from server/reference/sql-functions/date-time-functions -->
<!-- 64 functions, 3 pages skipped on extraction failure -->

### ADDDATE
`ADDDATE(date,INTERVAL expr unit), ADDDATE(expr,days)`  
When invoked with the `INTERVAL` form of the second argument, `ADDDATE()` is a synonym for DATE_ADD().

### ADDTIME
`ADDTIME(expr1,expr2)`  
`ADDTIME()` adds _expr2_ to _expr1_ and returns the result.

### ADD_MONTHS
`ADD_MONTHS(date, months)`  
`ADD_MONTHS` adds an integer _months_ to a given _date_ (DATE, DATETIME or TIMESTAMP), returning the resulting date. *(since 10.6.1)*

### CONVERT_TZ
`CONVERT_TZ(dt,from_tz,to_tz)`  
`CONVERT_TZ()` converts a datetime value _dt_ from the time zone given by _from_tz_ to the time zone given by _to_tz_ and returns the resulting value.

### CURDATE
`CURDATE()`  
`CURDATE` returns the current date as a value in `YYYY-MM-DD` or `YYYYMMDD` format, depending on whether the function is used in a string or numeric context.

### CURRENT_DATE
`CURRENT_DATE, CURRENT_DATE()`  
`CURRENT_DATE` and `CURRENT_DATE()` are synonyms for CURDATE().

### CURRENT_TIME
`CURRENT_TIME`  
`CURRENT_TIME` and `CURRENT_TIME()` are synonyms for CURTIME().

### CURRENT_TIMESTAMP
`CURRENT_TIMESTAMP`  
`CURRENT_TIMESTAMP` and `CURRENT_TIMESTAMP()` are synonyms for NOW().

### CURTIME
`CURTIME([precision])`  
Returns the current time as a value in `HH:MM:SS` or `HHMMSS.uuuuuu` format, depending on whether the function is used in a string or numeric context.

### DATE
`DATE(expr)`  
Extracts the date part of the date or datetime expression _expr_.

### DATEDIFF
`DATEDIFF(expr1,expr2)`  
`DATEDIFF()` returns (_expr1_ – _expr2_) expressed as a value in days from one date to the other.

### DATE_ADD
`DATE_ADD(date,INTERVAL expr unit)`  
Performs date arithmetic.

### DATE_FORMAT
`DATE_FORMAT(date, format[, locale])`  
Formats the date value according to the format string.

### DATE_SUB
`DATE_SUB(date,INTERVAL expr unit)`  
Performs date arithmetic.

### DAY
`DAY(date)`  
`DAY()` is a synonym for DAYOFMONTH().

### DAYNAME
`DAYNAME(date)`  
Returns the name of the weekday for date.

### DAYOFMONTH
`DAYOFMONTH(date)`  
Returns the day of the month for date, in the range `1` to `31`, or `0` for dates such as `'0000-00-00'` or `'2008-00-00'` which have a zero day part.

### DAYOFWEEK
`DAYOFWEEK(date)`  
Returns the day of the week index for the date (1 = Sunday, 2 = Monday, ..., 7 = Saturday).

### DAYOFYEAR
`DAYOFYEAR(date)`  
Returns the day of the year for date, in the range 1 to 366.

### EXTRACT
`EXTRACT(unit FROM date)`  
The EXTRACT() function extracts the required unit from the date.

### FORMAT_PICO_TIME
`FORMAT_PICO_TIME(time_val)`  
Given a time in picoseconds, returns a human-readable time value and unit indicator.

### FROM_DAYS
`FROM_DAYS(N)`  
Given a day number N, returns a DATE value.

### FROM_UNIXTIME
`FROM_UNIXTIME(unix_timestamp)`  
Converts the number of seconds from the epoch (1970-01-01 00:00:00 UTC) to a`TIMESTAMP` value, the opposite of what UNIX_TIMESTAMP() is doing.

### GET_FORMAT
`GET_FORMAT({DATE|DATETIME|TIME}, {'EUR'|'USA'|'JIS'|'ISO'|'INTERNAL'})`  
Returns a format string.

### HOUR
`HOUR(time)`  
Returns the hour for time.

### LAST_DAY
`LAST_DAY(date)`  
Takes a date or datetime value and returns the corresponding value for the last day of the month.

### LOCALTIME
`LOCALTIME`  
`LOCALTIME` and `LOCALTIME()` are synonyms for NOW().

### LOCALTIMESTAMP
`LOCALTIMESTAMP`  
`LOCALTIMESTAMP` and `LOCALTIMESTAMP()` are synonyms for NOW().

### MAKEDATE
`MAKEDATE(year,dayofyear)`  
Returns a date, given `year` and `day-of-year values`.

### MAKETIME
`MAKETIME(hour,minute,second)`  
Returns a time value calculated from the `hour`, `minute`, and `second` arguments.

### MICROSECOND
`MICROSECOND(expr)`  
Returns the microseconds from the time or datetime expression _expr_ as a number in the range from 0 to 999999.

### MINUTE
`MINUTE(time)`  
Returns the minute for _time_, in the range 0 to 59.

### MONTH
`MONTH(date)`  
Returns the month for `date` in the range 1 to 12 for January to December, or 0 for dates such as `0000-00-00` or `2008-00-00` that have a zero month part.

### MONTHNAME
`MONTHNAME(date)`  
Returns the full name of the month for date.

### NOW
`NOW([precision])`  
Returns the current date and time as a value in `YYYY-MM-DD HH:MM:SS` or `YYYYMMDDHHMMSS.uuuuuu` format, depending on whether the function is used in a string or numeric context.

### PERIOD_ADD
`PERIOD_ADD(P,N)`  
Adds `N` months to period `P`.

### PERIOD_DIFF
`PERIOD_DIFF(P1,P2)`  
Returns the number of months between periods P1 and P2.

### QUARTER
`QUARTER(date)`  
Returns the quarter of the year for `date`, in the range 1 to 4.

### SECOND
`SECOND(time)`  
Returns the second for a given `time` (which can include microseconds), in the range 0 to 59, or `NULL` if not given a valid time value.

### SEC_TO_TIME
`SEC_TO_TIME(seconds)`  
Returns the seconds argument, converted to hours, minutes, and seconds, as a TIME value.

### STR_TO_DATE
`STR_TO_DATE(str,format)`  
This is the inverse of the DATE_FORMAT() function.

### SUBDATE
`SUBDATE(date,INTERVAL expr unit), SUBDATE(expr,days)`  
When invoked with the `INTERVAL` form of the second argument, `SUBDATE()` is a synonym for DATE_SUB().

### SUBTIME
`SUBTIME(expr1,expr2)`  
`SUBTIME()` returns `expr1` - `expr2` expressed as a value in the same format as `expr1`.

### SYSDATE
`SYSDATE([precision])`  
Returns the current date and time as a value in `YYYY-MM-DD HH:MM:SS` or `YYYYMMDDHHMMSS.uuuuuu` format, depending on whether the function is used in a string or numeric context.

### TIME
`TIME(expr)`  
Extracts the time part of the time or datetime expression `expr` and returns it as a string.

### TIMEDIFF
`TIMEDIFF(expr1,expr2)`  
TIMEDIFF() returns `expr1` - `expr2` expressed as a time value.

### TIMESTAMP
`TIMESTAMP(expr), TIMESTAMP(expr1,expr2)`  
With a single argument, this function returns the date or datetime expression `expr` as a datetime value.

### TIMESTAMPADD
`TIMESTAMPADD(unit,interval,datetime_expr)`  
Adds the integer expression interval to the date or datetime expression datetime_expr.

### TIMESTAMPDIFF
`TIMESTAMPDIFF(unit,datetime_expr1,datetime_expr2)`  
Returns `datetime_expr2` - `datetime_expr1`, where `datetime_expr1` and`datetime_expr2` are date or datetime expressions.

### TIME_FORMAT
`TIME_FORMAT(time,format)`  
This is used like the DATE_FORMAT() function, but the format string may contain format specifiers only for hours, minutes, and seconds.

### TIME_TO_SEC
`TIME_TO_SEC(time)`  
Returns the time argument, converted to seconds.

### TO_DATE
`TO_DATE(string_expression [DEFAULT string_expression ON CONVERSION ERROR],`  
`TO_DATE` was added for Oracle support. *(since 12.3)*

### TO_DAYS
`TO_DAYS(date)`  
Given a date `date`, returns the number of days since the start of the current calendar (`0000-00-00`).

### TO_SECONDS
`TO_SECONDS(expr)`  
Returns the number of seconds from year 0 till `expr`, or NULL if `expr` is not a valid date or datetime.

### TRUNC
`TRUNC(date[,fmt])`  
Returns a DATETIME truncated according to `fmt`.

### UNIX_TIMESTAMP
`UNIX_TIMESTAMP()`  
If called with no argument, returns a Unix timestamp (seconds since `1970-01-01 00:00:00` UTC) as an unsigned integer.

### UTC_DATE
`UTC_DATE, UTC_DATE()`  
Returns the current UTC date as a value in `YYYY-MM-DD` or `YYYYMMDD` format, depending on whether the function is used in a string or numeric context.

### UTC_TIME
`UTC_TIME`  
Returns the current UTC time as a value in `HH:MM:SS` or `HHMMSS.uuuuuu` format, depending on whether the function is used in a string or numeric context.

### UTC_TIMESTAMP
`UTC_TIMESTAMP`  
Returns the current UTC date and time as a value in `YYYY-MM-DD HH:MM:SS` or `YYYYMMDDHHMMSS.uuuuuu` format, depending on whether the function is used in a string or numeric context.

### WEEK
`WEEK(date[,mode])`  
This function returns the week number for `date`.

### WEEKDAY
`WEEKDAY(date)`  
Returns the weekday index for `date` (`0` = Monday, `1` = Tuesday, ...

### WEEKOFYEAR
`WEEKOFYEAR(date)`  
Returns the calendar week of the date as a number in the range from 1 sqto 53.

### YEAR
`YEAR(date)`  
Returns the year for the given date, in the range 1000 to 9999, or 0 for the "zero" date.

### YEARWEEK
`YEARWEEK(date), YEARWEEK(date,mode)`  
Returns year and week for a date.
<!-- END GENERATED -->

## See Also

- **`mariadb-create-table`** — `DEFAULT CURRENT_TIMESTAMP` / `ON UPDATE CURRENT_TIMESTAMP` auto-timestamp columns, and choosing `DATETIME(6)` vs `TIMESTAMP` (the 2106 range cutoff)
- **`mariadb-features`** (topical) — `sql_mode=ORACLE` (for `TO_DATE`) and temporal/system-versioning context
- Canonical reference on `mariadb.com/docs`: <https://mariadb.com/docs/server/reference/sql-functions/date-time-functions>
