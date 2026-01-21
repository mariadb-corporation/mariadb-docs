---
description: >-
  Understand how to work with date and time values in MariaDB, including data
  types like DATETIME and TIMESTAMP, and useful temporal functions.
---

# Doing Time Guide

This guide covers effective ways to work with date and time information in MariaDB. Learn about temporal data types, essential functions for recording current date/time, extracting specific parts, and formatting your date/time values for display or analysis.

### Temporal Data Types

While dates and times can be stored as character strings, using specific temporal data types allows you to leverage MariaDB's built-in functions for manipulation and formatting.

* **`DATE`**: For dates only. Format: `YYYY-MM-DD`.
* **`TIME`**: For time only. Format: `HHH:MM:SS` (hours can range beyond 24).
* **`DATETIME`**: For combined date and time. Format: `YYYY-MM-DD HH:MM:SS`.
* **`TIMESTAMP`**: Similar to `DATETIME`, but with a more limited range and automatic update capabilities (not covered here). Range typically from `1970-01-01 00:00:01` UTC to `2038-01-19 03:14:07` UTC. From MariaDB 11.5 (64-bit), this range extends to `2106-02-07`.
* **`YEAR`**: For years only. Format: `YY` or `YYYY`.

### Recording Current Date and Time

MariaDB provides several functions to get the current date and time.

**Current Date:**\
Use `CURRENT_DATE` (no parentheses) or `CURDATE()` (with parentheses).

```sql
INSERT INTO billable_work (doctor_id, patient_id, session_date)
VALUES ('1021', '1256', CURRENT_DATE);
```

To see the ID of the last inserted row (if the primary key is `AUTO_INCREMENT`):

```sql
SELECT rec_id, doctor_id, patient_id, session_date
FROM billable_work
WHERE rec_id = LAST_INSERT_ID();
```

```
+--------+-----------+------------+--------------+
| rec_id | doctor_id | patient_id | session_date |
+--------+-----------+------------+--------------+
|   2462 | 1021      | 1256       | 2025-05-28   | -- Example date
+--------+-----------+------------+--------------+
```

**Current Time:**\
Use `CURRENT_TIME` or `CURTIME()`.

```sql
UPDATE billable_work
SET session_time = CURTIME()
WHERE rec_id = '2462';

SELECT patient_id, session_date, session_time
FROM billable_work
WHERE rec_id = '2462';
```

```
+------------+--------------+--------------+
| patient_id | session_date | session_time |
+------------+--------------+--------------+
| 1256       | 2025-05-28   | 13:03:22     | -- Example time
+------------+--------------+--------------+
```

**Current Date and Time (Timestamp):**\
Use `CURRENT_TIMESTAMP`, `NOW()`, or `SYSDATE()`. These functions return the current date and time in `YYYY-MM-DD HH:MM:SS` format, suitable for `DATETIME` or `TIMESTAMP` columns.

### Extracting Date and Time Parts

**Extracting from `DATE` types:**

* `YEAR(date_column)`: Extracts the year.
* `MONTH(date_column)`: Extracts the month number (1-12).
* `DAYOFMONTH(date_column)`: Extracts the day of the month (1-31). Also `DAY()`.

```sql
SELECT
    MONTH(session_date) AS Month,
    DAYOFMONTH(session_date) AS Day,
    YEAR(session_date) AS Year
FROM billable_work
WHERE rec_id = '2462';
```

```
+-------+------+------+
| Month | Day  | Year |
+-------+------+------+
|     5 |   28 | 2025 | -- Example output
+-------+------+------+
```

_(The `AS` keyword is used to provide an alias for the output column name.)_

**Day of the Week:**

* `DAYOFWEEK(date_column)`: Returns the weekday index (1=Sunday, 2=Monday, ..., 7=Saturday).
* `WEEKDAY(date_column)`: Returns the weekday index (0=Monday, 1=Tuesday, ..., 6=Sunday).

Example using `IF()` to determine a billing rate based on the day of the week (Saturday = day 7 for `DAYOFWEEK`):

```sql
SELECT
    patient_id AS 'Patient ID',
    session_date AS 'Date of Session',
    IF(DAYOFWEEK(session_date) = 7, 1.5, 1.0) AS 'Billing Rate'
FROM billable_work
WHERE rec_id = '2462';
```

The `IF(condition, value_if_true, value_if_false)` function allows conditional logic.

**Other Date Part Functions:**

* `DAYOFYEAR(date_column)`: Returns the day of the year (1-366).
* `QUARTER(date_column)`: Returns the quarter of the year (1-4).

Example: Selecting sessions in a specific quarter (e.g., Q2):

```sql
SELECT patient_id, session_date
FROM billable_work
WHERE QUARTER(session_date) = 2;
```

User variables can be used for dynamic queries:

```sql
SET @target_quarter := 2;
SELECT patient_id, COUNT(*) AS num_sessions
FROM billable_work
WHERE QUARTER(session_date) = @target_quarter AND doctor_id = '1021'
GROUP BY patient_id;
```

**Extracting from `TIME` types:**

* `HOUR(time_column)`: Extracts the hour.
* `MINUTE(time_column)`: Extracts the minute.
* `SECOND(time_column)`: Extracts the second.

```sql
SELECT
    HOUR(session_time) AS Hour,
    MINUTE(session_time) AS Minute,
    SECOND(session_time) AS Second
FROM billable_work
WHERE rec_id = '2462';
```

```
+------+--------+--------+
| Hour | Minute | Second |
+------+--------+--------+
|   13 |     03 |     22 | -- Example output
+------+--------+--------+
```

**Using `EXTRACT()` for `DATETIME` or `TIMESTAMP` types:**\
The `EXTRACT(unit FROM datetime_column)` function extracts a specified `unit` from a date/time value.\
Common units: `YEAR`, `MONTH`, `DAY`, `HOUR`, `MINUTE`, `SECOND`.\
Combined units: `YEAR_MONTH`, `DAY_HOUR`, `HOUR_MINUTE`, etc.

```sql
SELECT
    patient_name AS Patient,
    EXTRACT(HOUR FROM appointment) AS Hour,
    EXTRACT(MINUTE FROM appointment) AS Minute
FROM billable_work
JOIN patients ON billable_work.patient_id = patients.patient_id
WHERE doctor_id = '1021'
  AND EXTRACT(MONTH FROM appointment) = 5
  AND EXTRACT(DAY FROM appointment) = 28;
```

_(For details on joining tables, refer to relevant SQL documentation or a guide like "Essential Queries Guide".)_

Using a combined unit:

```sql
SELECT
    patient_name AS Patient,
    EXTRACT(HOUR_MINUTE FROM appointment) AS AppointmentHM
FROM billable_work
JOIN patients ON billable_work.patient_id = patients.patient_id
WHERE doctor_id = '1021';
```

Output for `HOUR_MINUTE` might be like `1303` (for 13:03).

### Formatting Dates and Times for Display

**Wordier Date Formats:**

* `MONTHNAME(date_column)`: Returns the full name of the month (e.g., 'May').
* `DAYNAME(date_column)`: Returns the full name of the day (e.g., 'Wednesday').

Example using `CONCAT()` to combine parts:

```sql
SELECT
    patient_name AS Patient,
    CONCAT(
        DAYNAME(appointment), ' - ',
        MONTHNAME(appointment), ' ',
        DAYOFMONTH(appointment), ', ',
        YEAR(appointment)
    ) AS Appointment
FROM billable_work
JOIN patients ON billable_work.patient_id = patients.patient_id
WHERE doctor_id = '1021' AND DATE(appointment) = '2025-05-28'
LIMIT 1;
```

```
+-------------------+------------------------------+
| Patient           | Appointment                  |
+-------------------+------------------------------+
| Michael Zabalaoui | Wednesday - May 28, 2025     | -- Example
+-------------------+------------------------------+
```

**Using `DATE_FORMAT(datetime_column, format_string)`:**\
This function provides extensive formatting options.\
Syntax: `DATE_FORMAT(date_value, 'format_options_and_literals')`.

```sql
SELECT
    patient_name AS Patient,
    DATE_FORMAT(appointment, '%W - %M %e, %Y') AS Appointment
FROM billable_work
JOIN patients ON billable_work.patient_id = patients.patient_id
WHERE doctor_id = '1021' AND DATE_FORMAT(appointment, '%c') = 5 -- Filter by month 5 (May)
LIMIT 1;
```

Common format specifiers:

* `%W`: Full weekday name
* `%M`: Full month name
* `%e`: Day of the month, numeric (1-31)
* `%d`: Day of the month, 2 digits (01-31)
* `%Y`: Year, 4 digits
* `%y`: Year, 2 digits
* `%c`: Month, numeric (1-12)
* `%r`: Time in 12-hour format (hh:mm:ss AM/PM)
* `%T`: Time in 24-hour format (hh:mm:ss)
* `%H`: Hour (00-23)
* `%h` or `%I`: Hour (01-12)
* `%i`: Minutes (00-59)
* `%s` or `%S`: Seconds (00-59)
* `%p`: AM or PM

Example with time:

```sql
SELECT
    DATE_FORMAT(appointment, '%W - %M %e, %Y at %r') AS Appointment
FROM billable_work
LIMIT 1;
```

```
+-------------------------------------------------+
| Appointment                                     |
+-------------------------------------------------+
| Wednesday - May 28, 2025 at 01:03:22 PM         | -- Example
+-------------------------------------------------+
```

For a complete list of options, see the official [DATE\_FORMAT() documentation](../reference/sql-functions/date-time-functions/date_format.md).

**Using `TIME_FORMAT(time_column, format_string)`:**\
Similar to `DATE_FORMAT()`, but uses only time-related format options.

```sql
SELECT
    patient_name AS Patient,
    TIME_FORMAT(appointment, '%l:%i %p') AS AppointmentTime
FROM billable_work
JOIN patients ON billable_work.patient_id = patients.patient_id
WHERE doctor_id = '1021'
  AND DATE(appointment) = CURDATE();
```

```
+-------------------+-----------------+
| Patient           | AppointmentTime |
+-------------------+-----------------+
| Michael Zabalaoui |     1:03 PM     | -- Example
+-------------------+-----------------+
```

Here, `%l` is hour (1-12) and `%p` adds AM/PM.

### Tips for Effective Date/Time Handling

* **Use Appropriate Data Types:** Choose temporal data types (`DATE`, `TIME`, `DATETIME`, `TIMESTAMP`, `YEAR`) over string types for date/time data to leverage built-in functions and ensure data integrity.
* **Leverage Built-in Functions:** MariaDB offers a rich set of functions for date/time manipulation. Use them within your SQL queries to avoid complex logic in your application code.
* **Test Queries:** When dealing with complex date/time logic or formatting, test your SQL statements directly in a MariaDB client (like the `mariadb` command-line tool) to verify results before embedding them in applications.
* **Be Aware of Time Zones:** `TIMESTAMP` values are stored in UTC and converted to/from the session's time zone, while `DATETIME` values are stored "as is" without time zone conversion. Understand how your server and session time zones are configured if working with data across different regions. (Time zone handling is a more advanced topic not fully covered here).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
