---
description: >-
  Complete MariaDB date and time functions guide. Complete reference for
  formatting, calculations, conversions, time zones, and operations for
  production use.
---

# Date & Time Functions

{% columns %}
{% column %}
{% content-ref url="date-and-time-units.md" %}
[date-and-time-units.md](date-and-time-units.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reference keywords for date arithmetic. These units, such as DAY, HOUR, and MINUTE, specify the interval type used in functions like DATE_ADD and EXTRACT.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="add_months.md" %}
[add_months.md](add_months.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Add a specific number of months to a date. This Oracle-compatible function simplifies date calculations involving monthly intervals.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="adddate.md" %}
[adddate.md](adddate.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Add a time interval to a date. This function performs date arithmetic, adding a specified value like days or hours to a starting date.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="addtime.md" %}
[addtime.md](addtime.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Add a time value to a date or time expression. This function sums two time arguments, returning a new time or datetime result.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="convert_tz.md" %}
[convert_tz.md](convert_tz.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Convert a datetime value between time zones. This function shifts a timestamp from a source time zone to a target time zone.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="curdate.md" %}
[curdate.md](curdate.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the current date. This function outputs today's date as a value in 'YYYY-MM-DD' or YYYYMMDD format, depending on the context.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="current_date.md" %}
[current_date.md](current_date.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for CURDATE(). Returns the current date as a value in 'YYYY-MM-DD' or YYYYMMDD format.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="current_time.md" %}
[current_time.md](current_time.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for CURTIME(). Returns the current time as a value in 'HH:MM:SS' or HHMMSS format.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="current_timestamp.md" %}
[current_timestamp.md](current_timestamp.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for NOW(). Returns the current date and time as a value in 'YYYY-MM-DD HH:MM:SS' or YYYYMMDDHHMMSS format.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="curtime.md" %}
[curtime.md](curtime.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the current time. This function outputs the current time of day as a value in 'HH:MM:SS' or HHMMSS format.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="date-function.md" %}
[date-function.md](date-function.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Extract the date part from a datetime expression. This function returns the year, month, and day portions, discarding the time component.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="date_add.md" %}
[date_add.md](date_add.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete DATE_ADD() reference: DATE_ADD(date, INTERVAL expr unit) syntax, negative interval support, unit keywords (DAY/MONTH/YEAR), and return types.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="date_format.md" %}
[date_format.md](date_format.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete DATE_FORMAT reference for MariaDB. Complete function guide with syntax, parameters, return values, and usage examples with comprehensive examples.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="date_sub.md" %}
[date_sub.md](date_sub.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Subtract a time interval from a date. This function calculates a past date by subtracting a specified unit, such as days, from a starting value.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="datediff.md" %}
[datediff.md](datediff.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete DATEDIFF() reference: DATEDIFF(expr1,expr2) syntax, date vs datetime expression handling, time component ignore, and positive/negative results.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="day.md" %}
[day.md](day.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for DAYOFMONTH(). Returns the day of the month (1-31) for a given date.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="dayname.md" %}
[dayname.md](dayname.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the name of the weekday. This function returns the full name of the day, such as 'Monday' or 'Sunday', for a given date.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="dayofmonth.md" %}
[dayofmonth.md](dayofmonth.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the day of the month. This function extracts the day portion of a date, returning a number from 1 to 31.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="dayofweek.md" %}
[dayofweek.md](dayofweek.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the weekday index. This function returns a number from 1 (Sunday) to 7 (Saturday) representing the day of the week.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="dayofyear.md" %}
[dayofyear.md](dayofyear.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the day of the year. This function returns a number from 1 to 366 indicating the day's position within the year.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="extract.md" %}
[extract.md](extract.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Extract a specific part of a date. This function retrieves components like YEAR, MONTH, DAY, or HOUR from a date or datetime expression.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="format_pico_time.md" %}
[format_pico_time.md](format_pico_time.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Format a time in picoseconds. This function converts a numeric picosecond value into a human-readable string with units like ps, ns, us, ms, s, m, h, or d.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="from_days.md" %}
[from_days.md](from_days.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Convert a day number to a date. This function returns a DATE value corresponding to the number of days since year 0.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="from_unixtime.md" %}
[from_unixtime.md](from_unixtime.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Convert a Unix timestamp to a datetime. This function formats a Unix timestamp as a date string or number in the current time zone.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="get_format.md" %}
[get_format.md](get_format.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return a format string. This function provides standard format strings for DATE_FORMAT and STR_TO_DATE based on regions like 'USA' or 'EUR'.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="hour.md" %}
[hour.md](hour.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Extract the hour. This function returns the hour portion of a time or datetime value as a number from 0 to 23.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="last_day.md" %}
[last_day.md](last_day.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the last day of the month. This function calculates the date of the final day for the month containing the given date.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="localtime.md" %}
[localtime.md](localtime.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for NOW(). Returns the current date and time in the session time zone.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="localtimestamp.md" %}
[localtimestamp.md](localtimestamp.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for NOW(). Returns the current date and time in the session time zone as a datetime value.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="makedate.md" %}
[makedate.md](makedate.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Create a date from a year and day of year. This function constructs a DATE value given a year and the day number within that year.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="maketime.md" %}
[maketime.md](maketime.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Create a time from hour, minute, and second. This function constructs a TIME value from three numeric arguments.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="microsecond.md" %}
[microsecond.md](microsecond.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Extract microseconds. This function returns the microsecond part of a time or datetime expression as a number from 0 to 999999.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="microseconds-in-mariadb.md" %}
[microseconds-in-mariadb.md](microseconds-in-mariadb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand microsecond precision. This concept page explains how MariaDB stores and handles fractional seconds in time data types.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="minute.md" %}
[minute.md](minute.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Extract the minute. This function returns the minute portion of a time or datetime value as a number from 0 to 59.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="month.md" %}
[month.md](month.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Extract the month. This function returns the month portion of a date as a number from 1 (January) to 12 (December).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="monthname.md" %}
[monthname.md](monthname.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the name of the month. This function returns the full name of the month, such as 'January' or 'December', for a given date.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="months_between.md" %}
[months_between.md](months_between.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate the difference between two months.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="now.md" %}
[now.md](now.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete NOW() function reference: NOW([precision]) and CURRENT_TIMESTAMP synonyms, TIMESTAMP vs DATETIME types, timezone/DST handling, and fractional seconds.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="period_add.md" %}
[period_add.md](period_add.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Add months to a period. This function adds a specified number of months to a period formatted as YYMM or YYYYMM.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="period_diff.md" %}
[period_diff.md](period_diff.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate the difference between periods. This function returns the number of months between two periods formatted as YYMM or YYYYMM.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="quarter.md" %}
[quarter.md](quarter.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the quarter of the year. This function returns a number from 1 to 4 indicating the quarter for a given date.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sec_to_time.md" %}
[sec_to_time.md](sec_to_time.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Convert seconds to time. This function returns a TIME value corresponding to the number of seconds elapsed from the start of the day.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="second.md" %}
[second.md](second.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Extract the second. This function returns the second portion of a time or datetime value as a number from 0 to 59.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="str_to_date.md" %}
[str_to_date.md](str_to_date.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete STR_TO_DATE() reference: parse strings to DATE/TIME/DATETIME, format specifiers (%Y %m %d %H %i %s), invalid input handling, and SQL_MODE errors.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="subdate.md" %}
[subdate.md](subdate.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Subtract a time interval from a date. This synonym for DATE_SUB calculates a past date by subtracting a specified unit from a starting value.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="subtime.md" %}
[subtime.md](subtime.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Subtract a time value. This function subtracts one time or datetime expression from another and returns the result.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sysdate.md" %}
[sysdate.md](sysdate.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the time of execution. Unlike NOW(), which returns the start time of the statement, SYSDATE() returns the time it executes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="time-function.md" %}
[time-function.md](time-function.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Extract the time portion. This function returns the time part of a time or datetime expression.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="time_format.md" %}
[time_format.md](time_format.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Format a time. This function formats a time value according to a format string, similar to DATE_FORMAT but for time values.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="time_to_sec.md" %}
[time_to_sec.md](time_to_sec.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
TIME_TO_SEC() converts a time value to the number of seconds, returning a DOUBLE that preserves microseconds.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="timediff.md" %}
[timediff.md](timediff.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Subtract two time values. This function calculates the difference between two time or datetime expressions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="timestamp-function.md" %}
[timestamp-function.md](timestamp-function.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Convert to datetime or add time. With one argument, it returns a datetime; with two, it adds a time expression to a date or datetime.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="timestampadd.md" %}
[timestampadd.md](timestampadd.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Add an interval to a timestamp. This function adds a specified integer number of units (like MONTH or SECOND) to a datetime expression.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="timestampdiff.md" %}
[timestampdiff.md](timestampdiff.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Calculate the difference between timestamps. This function returns the difference between two datetime expressions in the specified unit.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="to_date.md" %}
[to_date.md](to_date.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
TO_DATE() converts a string to a date using a specified format, with optional handling for conversion errors.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="to_days.md" %}
[to_days.md](to_days.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Convert a date to a day number. This function returns the number of days between year 0 and the given date.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="to_seconds.md" %}
[to_seconds.md](to_seconds.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Convert a date to seconds. This function returns the number of seconds from year 0 to the given date or datetime.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="trunc.md" %}
[trunc.md](trunc.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Truncate a date. In Oracle mode, this function truncates a date value to a specified unit of measure.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="unix_timestamp.md" %}
[unix_timestamp.md](unix_timestamp.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return a Unix timestamp. This function returns the number of seconds since the Unix Epoch ('1970-01-01 00:00:00' UTC).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="utc_date.md" %}
[utc_date.md](utc_date.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the current UTC date. This function returns the current Coordinated Universal Time date in 'YYYY-MM-DD' or YYYYMMDD format.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="utc_time.md" %}
[utc_time.md](utc_time.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the current UTC time. This function returns the current Coordinated Universal Time in 'HH:MM:SS' or HHMMSS format.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="utc_timestamp.md" %}
[utc_timestamp.md](utc_timestamp.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the current UTC timestamp. This function returns the current Coordinated Universal Time date and time.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="week.md" %}
[week.md](week.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the week number. This function returns the week number for a date, with an optional mode to define the start of the week.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="weekday.md" %}
[weekday.md](weekday.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the weekday index. This function returns the index of the day of the week (0=Monday, 6=Sunday).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="weekofyear.md" %}
[weekofyear.md](weekofyear.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the calendar week. This function returns the week number of the date (1-53), equivalent to WEEK(date, 3).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="year.md" %}
[year.md](year.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Extract the year. This function returns the year portion of a date as a number from 1000 to 9999.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="yearweek.md" %}
[yearweek.md](yearweek.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Return the year and week. This function returns the year and week number for a date, useful for grouping results by week.
{% endcolumn %}
{% endcolumns %}
