---
description: >-
  This guide explores MariaDB functions for performing calculations and
  modifications on date and time values, like DATE_ADD and DATE_SUB.
---

# Changing Times in MariaDB

This guide explores MariaDB functions for performing calculations and modifications on date and time values. Learn to use functions like `DATE_ADD`, `DATE_SUB`, `TIME_TO_SEC`, and `SEC_TO_TIME` to accurately add or subtract intervals and manage date/time changes that cross midnight or month/year boundaries.

_(For foundational knowledge on date and time data types and basic retrieval, please refer to the "_[_Date and Time Handling Guide_](mariadb-datetime-guide.md)_".)_

### Calculating Time Across Midnight

When adding hours to a `TIME` value, calculations might exceed 24 hours. For example, if a task is entered at 23:00 and is promised 2 hours later, a simple addition can be problematic.

Consider an `INSERT` statement for a `tickets` table with `entered` and `promised` `TIME` columns:

```sql
-- Example: Calculating a promised time 2 hours (7200 seconds) from current time
INSERT INTO tickets (client_id, urgency, trouble, ticket_date, entered, promised)
VALUES ('some_client', 'ASAP', 'Issue details',
        CURDATE(), CURTIME(),
        SEC_TO_TIME(TIME_TO_SEC(CURTIME()) + 7200));
```

* `TIME_TO_SEC(time)` converts a time value to seconds.
* `SEC_TO_TIME(seconds)` converts seconds back to a time format (`HHH:MM:SS`).

If `CURTIME()` is `23:00:00` (82,800 seconds), `82800 + 7200 = 90000` seconds. `SEC_TO_TIME(90000)` would result in `25:00:00`. While MariaDB can store this, it doesn't represent a standard clock time for the next day.

Modulo Arithmetic for Time Rollover:

To handle time wrapping around the 24-hour clock (86,400 seconds in a day) for TIME columns, use the modulo operator (%):

```sql
-- Corrected calculation for 'promised' TIME, wraps around 24 hours
SEC_TO_TIME((TIME_TO_SEC(CURTIME()) + 7200) % 86400)
```

If current time is 23:00, `(82800 + 7200) % 86400` becomes `90000 % 86400`, which is `3600` seconds. `SEC_TO_TIME(3600)` correctly results in `01:00:00`.

### Tracking Date Changes with Time: Using `DATETIME`

The modulo arithmetic above gives the correct time of day but doesn't indicate if the promised time falls on the next calendar day. For calculations where the date might change, it's essential to use `DATETIME` (or `TIMESTAMP`) data types.

If your table initially used separate `DATE` and `TIME` columns (e.g., `ticket_date`, `entered_time`, `promised_time`), you would typically alter the table to use `DATETIME` columns (e.g., `entered_datetime`, `promised_datetime`) to store both date and time information accurately. This often involves:

1. Adding new `DATETIME` columns.
2. Populating them by combining the old date and time columns (e.g., using `CONCAT(ticket_date, ' ', entered_time)`).
3. Dropping the old separate date and time columns. _(Always back up your data before such structural changes.)_

With `DATETIME` columns, `NOW()` can be used to get the current date and time.

### Adding Durations with `DATE_ADD`

The `DATE_ADD(date, INTERVAL expr unit)` function is the most robust way to add a duration to a date, time, or datetime value. It correctly handles rollovers across days, months, and years.

* `date`: A `DATE`, `DATETIME`, or `TIME` value.
* `expr`: The value of the interval to add.
* `unit`: The unit of the interval (e.g., `HOUR`, `MINUTE`, `DAY`, `MONTH`, `YEAR`, etc.).

Adding Hours (handles date change):

If entered and promised are DATETIME columns:

```sql
INSERT INTO tickets (client_id, urgency, trouble, entered, promised)
VALUES ('some_client', 'ASAP', 'Issue details',
        NOW(),
        DATE_ADD(NOW(), INTERVAL 2 HOUR));
```

If `NOW()` is `2025-06-03 23:00:00`, `promised` will correctly be `2025-06-04 01:00:00`.

Adding Combined Hours and Minutes:

Use HOUR\_MINUTE as the unit. The expr is a string 'hours:minutes'.

```sql
-- Add 2 hours and 30 minutes
DATE_ADD(NOW(), INTERVAL '2:30' HOUR_MINUTE)
```

If `NOW()` is `2025-06-03 23:00:00`, this results in `2025-06-04 01:30:00`.

### Date Calculations Across Months and Years with `DATE_ADD`

`DATE_ADD` also correctly handles date changes across month and year boundaries, including leap years.

**Adding Days:**

```sql
-- Add 5 days
DATE_ADD(NOW(), INTERVAL 5 DAY)
```

If `NOW()` is `2025-02-27`, this would result in `2025-03-04` (assuming 2025 is not a leap year).

Adding Combined Days and Hours:

Use DAY\_HOUR as the unit. The expr is a string 'days hours'.

```sql
-- Add 2 days and 6 hours
DATE_ADD(NOW(), INTERVAL '2 6' DAY_HOUR)
```

Adding Combined Years and Months:

Use YEAR\_MONTH as the unit. The expr is a string 'years-months'.

```sql
-- Add 1 year and 2 months
DATE_ADD(NOW(), INTERVAL '1-2' YEAR_MONTH) -- Note: Original text used '1 2', '1-2' is common for YEAR_MONTH
```

If `NOW()` is `2025-09-15 23:00:00`, this results in `2026-11-15 23:00:00`. This type of interval typically does not affect the day or time components directly, only the year and month.

### Subtracting Durations

Using DATE\_ADD with a Negative Interval:

You can subtract durations by providing a negative value for expr.

```sql
-- Subtract 5 days
DATE_ADD(NOW(), INTERVAL -5 DAY)
```

Using DATE\_SUB(date, INTERVAL expr unit):

This function is specifically for subtracting durations.

```sql
-- Subtract 5 days
DATE_SUB(NOW(), INTERVAL 5 DAY)
```

Note: With `DATE_SUB`, `expr` is positive for subtraction. A negative `expr` would result in addition.

{% @marketo/form formId="4316" %}
