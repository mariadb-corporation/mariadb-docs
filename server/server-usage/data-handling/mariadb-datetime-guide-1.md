---
description: >-
  Master date and time handling in MariaDB with this guide on temporal data
  types, current time functions, and formatting dates for display.
---

# Doing Time with MariaDB

The recording of date and time in a MariaDB database is a very common requirement. For gathering temporal data, one needs to know which type of columns to use in a table. More importantly is knowing how to record chronological data and how to retrieve it in various formats. Although this is a seemingly basic topic, there are many built-in time functions that can be used for more accurate SQL statements and better formatting of data. In this article we will explore these various aspects of how to do time with MariaDB.

#### About Time

Since date and time are only numeric strings, they can be stored in a regular character column. However, by using temporal data type columns, you can make use of several built-in functions offered by MariaDB. Currently, there are five temporal data types available: `DATE`, `TIME`, `DATETIME`, `TIMESTAMP`, and `YEAR`. The `DATE` column type is for recording the date only and is basically in this format: `yyyy-mm-dd`. The `TIME` column type is for recording time in this format: `hhh:mm:ss`. To record a combination of date and time, there is the `DATETIME` column type: `yyyy-mm-dd hh:mm:ss`.

{% tabs %}
{% tab title="Current" %}
The `TIMESTAMP` column is similar to `DATETIME`, but it's a little limited in its range of allowable time. It starts at the Unix epoch time (1970-01-01) and ends on 2106-02-07. Finally, the `YEAR` data type is for recording only the year in a column: `yy` or `yyyy`. For the examples in this article, `DATE`, `TIME`, and `DATETIME` columns are used. The database that are referenced is for a fictitious psychiatry practice that keeps track of its patients and billable hours in MariaDB.
{% endtab %}

{% tab title="< 11.5" %}
The `TIMESTAMP` column is similar to `DATETIME`, but it's a little limited in its range of allowable time. It starts at the Unix epoch time (i.e., 1970-01-01) and ends on 2038-01-19. Finally, the `YEAR` data type is for recording only the year in a column: `yy` or `yyyy`. For the examples in this article, `DATE`, `TIME`, and `DATETIME` columns are used. The database that are referenced is for a fictitious psychiatry practice that keeps track of its patients and billable hours in MariaDB.
{% endtab %}
{% endtabs %}

#### Telling Time

To record the current date and time in a MariaDB table, there are a few built-in functions that may be used. First, to record the date there are the functions [CURRENT\_DATE](../../reference/sql-functions/date-time-functions/current_date.md) and [CURDATE( )](../../reference/sql-functions/date-time-functions/curdate.md) (depending on your style), which both produce the same results (e.g., 2017-08-01). Notice that [CURDATE( )](../../reference/sql-functions/date-time-functions/curdate.md) requires parentheses and the other does not. With many functions a column name or other variables are placed inside of the parentheses to get a result. With functions like [CURDATE( )](../../reference/sql-functions/date-time-functions/curdate.md), there is nothing that may go inside the parenthesis. Since these two functions retrieve the current date in the format of the `DATE` column type, they can be used to fill in a `DATE` column when inserting a row:

```sql
INSERT INTO billable_work
(doctor_id, patient_id, session_date)
VALUES('1021', '1256', CURRENT_DATE);
```

The column _session\_date_ is a `DATE` column. Notice that there are no quotes around the date function. If there were it would be taken as a literal value rather than a function. Incidentally, I've skipped discussing how the table was set up. If you're not familiar with how to set up a table, you may want to read the [MariaDB Basics](../../mariadb-quickstart-guides/basics-guide.md) article. To see what was just recorded by the [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) statement above, the following may be entered (results follow):

```sql
SELECT rec_id, doctor_id, 
patient_id, session_date
FROM billable_work
WHERE rec_id=LAST_INSERT_ID();

+--------+-----------+------------+--------------+
| rec_id | doctor_id | patient_id | session_date |
+--------+-----------+------------+--------------+
|   2462 | 1021      | 1256       | 2017-08-23   |
+--------+-----------+------------+--------------+
```

Notice in the billable\_work table that the primary key column (i.e., `rec_id`) is an automatically generated and incremental number column (i.e., `AUTO_INCREMENT`). As long as another record is not created or the user does not exit from the mariadb client or otherwise end the session, the [LAST\_INSERT\_ID( )](../../reference/sql-functions/secondary-functions/information-functions/last_insert_id.md) function will retrieve the value of the `rec_id` for the last record entered by the user.

To record the time of an appointment for a patient in a time data type column, [CURRENT\_TIME](../../reference/sql-functions/date-time-functions/current_time.md) or [CURTIME( )](../../reference/sql-functions/date-time-functions/curtime.md) are used in the same way to insert the time. The following is entered to update the row created above to mark the starting time of the appointment—another [SELECT](../../reference/sql-statements/data-manipulation/selecting-data/select.md) statement follows with the results:

```sql
UPDATE billable_work
SET session_time=CURTIME()
WHERE rec_id='2462';

SELECT patient_id, session_date, session_time
FROM billable_work
WHERE rec_id='2462';

+------------+--------------+--------------+
| patient_id | session_date | session_time |
+------------+--------------+--------------+
| 1256       | 2017-08-23   | 10:30:23     |
+------------+--------------+--------------+
```

The column session\_time is a time column. To record the date and time together in the same column, [CURRENT\_TIMESTAMP](../../reference/sql-functions/date-time-functions/current_timestamp.md) or [SYSDATE( )](../../reference/sql-functions/date-time-functions/sysdate.md) or [NOW( )](../../reference/sql-functions/date-time-functions/now.md) can be used. All three functions produce the same time format: `yyyy-mm-dd hh:mm:ss`. Therefore, the column's data type would have to be `DATETIME` to use them.

#### How to get a Date

Although MariaDB records the date in a fairly agreeable format, you may want to present the date when it's retrieved in a different format. Or, you may want to extract part of the date, such as only the day of the month. There are many functions for reformatting and selectively retrieving date and time information. To start off with, let's select a column with a data type of `DATE` and look at the functions available for retrieving each component. To extract the year, there's the [YEAR( )](../../reference/sql-functions/date-time-functions/year.md) function. For extracting just the month, the [MONTH( )](../../reference/sql-functions/date-time-functions/month.md) function could be called upon. And to grab the day of the month, [DAYOFMONTH( )](../../reference/sql-functions/date-time-functions/dayofmonth.md) will work. Using the record entered above, here's what an SQL statement and its results would look like in which the session date is broken up into separate parts, but in a different order:

```sql
SELECT MONTH(session_date) AS Month,
DAYOFMONTH(session_date) AS Day,
YEAR(session_date) AS Year
FROM billable_work
WHERE rec_id='2462';

+-------+------+------+
| Month | Day  | Year |
+-------+------+------+
|     8 |   23 | 2017 |
+-------+------+------+
```

For those who aren't familiar with the keyword `AS`, it's used to label a column's output and may be referenced within an SQL statement. Splitting up the elements of a date can be useful in analyzing a particular element. If the bookkeeper of the fictitious psychiatry office needed to determine if the day of the week of each session was on a Saturday because the billing rate would be higher (time and a half), the [DAYOFWEEK( )](../../reference/sql-functions/date-time-functions/dayofweek.md) function could be used. To spice up the examples, let's wrap the date function up in an [IF( )](../../reference/sql-functions/control-flow-functions/if-function.md) function that tests for the day of the week and sets the billing rate accordingly.

```sql
SELECT patient_id AS 'Patient ID',
session_date AS 'Date of Session',
IF(DAYOFWEEK(session_date)=6, 1.5, 1.0)
  AS 'Billing Rate' 
FROM billable_work
WHERE rec_id='2462';

+-------------+-----------------+--------------+
| Patient ID  | Date of Session | Billing Rate |
+-------------+-----------------+--------------+
|        1256 |    2017-08-23   |          1.5 |
+-------------+-----------------+--------------+
```

Since we've slipped in the [IF( )](../../reference/sql-functions/control-flow-functions/if-function.md) function, we should explain it's format. The test condition is listed first within the parentheses. In this case, the test is checking if the session date is the sixth day of the week. Then, what MariaDB should display is given if the test passes, followed by the result if it fails.

Similar to the [DAYOFWEEK( )](../../reference/sql-functions/date-time-functions/dayofweek.md) function, there's also [WEEKDAY( )](../../reference/sql-functions/date-time-functions/weekday.md). The only difference is that for [DAYOFWEEK( )](../../reference/sql-functions/date-time-functions/dayofweek.md) the first day of the week is Sunday—with [WEEKDAY( )](../../reference/sql-functions/date-time-functions/weekday.md) the first day is Monday. Both functions represent the first day with 0 and the last with `6`. Having _Saturday_ and _Sunday_ symbolized by `5` and `6` can be handy in constructing an IF statement that has a test component like "`WEEKDAY(session_date) > 4`" to determine if a date is a weekend day. This is cleaner than testing for values of `0` and `6`.

There is a function for determining the day of the year: [DAYOFYEAR( )](../../reference/sql-functions/date-time-functions/dayofyear.md). It's not used often, but it is available if you ever need it. Occasionally, though, knowing the quarter of a year for a date can be useful for financial accounting. Rather than set up a formula in a script to determine the quarter, the [QUARTER( )](../../reference/sql-functions/date-time-functions/quarter.md) function can do this easily. For instance, suppose an accountant wants a list of a doctor's sessions for each patient for the previous quarter. These three SQL statements could be entered in sequence to achieve the results that follow:

```sql
SET @LASTQTR:=IF((QUARTER(CURDATE())-1)=0, 
4, QUARTER(CURDATE())-1);

SET @YR:=IF(@LASTQTR=4, 
YEAR(NOW())-1, YEAR(NOW()));

SELECT patient_id AS 'Patient ID', 
COUNT(session_time) 
  AS 'Number of Sessions'
FROM billable_work
WHERE QUARTER(session_date) = @LASTQTR
  AND YEAR(session_date) = @YR
  AND doctor_id='1021'
GROUP BY patient_id
ORDER BY patient_id LIMIT 5;

+------------+--------------------+
| Patient ID | Number of Sessions |
+------------+--------------------+
| 1104       |                 10 |
| 1142       |                  7 |
| 1203       |                 18 |
| 1244       |                  6 |
| 1256       |                 12 |
+------------+--------------------+
```

This example is the most complicated so far. But it's not too difficult to understand if we pull it apart. The first SQL statement sets up a user variable containing the previous quarter (i.e., 1, 2, 3, or 4). This variable are needed in the other two statements. The [IF( )](../../reference/sql-functions/control-flow-functions/if-function.md) clause in the first statement checks if the quarter of the current date minus one is zero. It will equal zero when it's run during the first quarter of a year. During a first quarter, of course, the previous quarter is the fourth quarter of the previous year. So, if the equation equals zero, then the variable `@LASTQTR` is set to `4`. Otherwise, `@LASTQTR` is set to the value of the current quarter minus one. The second statement is necessary to ensure that the records for the correct year are selected. So, if `@LASTQTR` equals four, then `@YR` needs to equal last year. If not, `@YR` is set to the current year. With the user variables set to the correct quarter and year, the [SELECT](../../reference/sql-statements/data-manipulation/selecting-data/select.md) statement can be entered. The [COUNT( )](../../reference/sql-functions/aggregate-functions/count.md) function counts the number of appointments that match the `WHERE` clause for each patient based on the [GROUP BY](../../reference/sql-statements/data-manipulation/selecting-data/select.md#group-by) clause. The `WHERE` clause looks for sessions with a quarter that equals `@LASTQTR` and a year that equals `@YR`, as well as the doctor's identification number. In summary, what we end up with is a set of SQL statements that retrieve the desired information regardless of which quarter or year it's entered.

#### What is the Time?

The last section covered how to retrieve pieces of a date column. Now let's look at how to do the same with a time column. To extract just the hour of a time saved in MariaDB, the [HOUR( )](../../reference/sql-functions/date-time-functions/hour.md) function could be used. For the minute and second, there's [MINUTE( )](../../reference/sql-functions/date-time-functions/minute.md) and [SECOND( )](../../reference/sql-functions/date-time-functions/second.md). Let's put them all together in one straightforward [SELECT](../../reference/sql-statements/data-manipulation/selecting-data/select.md) statement:

```sql
SELECT HOUR(session_time) AS Hour, 
MINUTE(session_time) AS Minute, 
SECOND(session_time) AS Second
FROM billable_work
WHERE rec_id='2462';

+------+--------+--------+
| Hour | Minute | Second |
+------+--------+--------+
|   10 |     30 |     00 |
+------+--------+--------+
```

#### Date & Time Combined

All of the examples given so far have involved separate columns for date and time. The [EXTRACT( )](../../reference/sql-functions/date-time-functions/extract.md) function, however, will allow a particular component to be extracted from a combined column type (i.e., `DATETIME` or `TIMESTAMP`). The format is `EXTRACT(date_type FROM date_column)` where _date\_type_ is the component to retrieve and _date\_column_ is the name of the column from which to extract data. To extract the year, the _date\_type_ would be `YEAR`; for month, `MONTH` is used; and for day, there's `DAY`. To extract time elements, `HOUR` is used for hour, `MINUTE` for minute, and `SECOND` for second. Although that's all pretty simple, let's look at an example. Suppose the table billable\_work has a column called `appointment` (a `datetime` column) that contains the date and time for which the appointment was scheduled (as opposed to the time it actually started in `session_time`). To get the hour and minute for a particular date, the following SQL statement will suffice:

```sql
SELECT patient_name AS Patient, 
EXTRACT(HOUR FROM appointment) AS Hour, 
EXTRACT(MINUTE FROM appointment) AS Minute
FROM billable_work, patients
WHERE doctor_id='1021' 
  AND EXTRACT(MONTH FROM appointment)='8' 
  AND EXTRACT(DAY FROM appointment)='30'
  AND billable_work.patient_id =
    patients.patient_id;
```

This statement calls upon another table (`patients`) which holds patient information such as their names. It requires a connecting point between the tables (i.e., the `patient_id` from each table). If you're confused on how to form relationships between tables in a [SELECT](../../reference/sql-statements/data-manipulation/selecting-data/select.md) statement, you may want to go back and read the [Getting Data from MariaDB](../../mariadb-quickstart-guides/mariadb-selecting-data-guide.md) article. The SQL statement above would be used to retrieve the appointments for one doctor for one day, giving results like this:

```sql
+-------------------+------+--------+
| Patient           | Hour | Minute |
+-------------------+------+--------+
| Michael Zabalaoui |   10 |     00 |
| Jerry Neumeyer    |   11 |     00 |
| Richard Stringer  |   13 |     30 |
| Janice Sogard     |   14 |     30 |
+-------------------+------+--------+
```

In this example, the time elements are separated and they don't include the date. With the [EXTRACT( )](../../reference/sql-functions/date-time-functions/extract.md) function, however, you can also return combined date and time elements. There is `DAY_HOUR` for the day and hour; there's `DAY_MINUTE` for the day, hour, and minute; `DAY_SECOND` for day, hour, minute, and second; and `YEAR_MONTH` for year and month. There are also some time only combinations: `HOUR_MINUTE` for hour and minute; `HOUR_SECOND` for hour, minute, and second; and `MINUTE_SECOND` for minute and second. However, there's not a `MONTH_DAY` to allow the combining of the two extracts in the `WHERE` clause of the last [SELECT](../../reference/sql-statements/data-manipulation/selecting-data/select.md) statement above. Nevertheless, we'll modify the example above and use the `HOUR_MINUTE` date\_type to retrieve the hour and minute in one resulting column. It would only require the second and third lines to be deleted and replaced with this:

```sql
...
EXTRACT(HOUR_MINUTE FROM appointment) 
  AS Appointment 
...

+-------------------+-------------+
| Patient           | Appointment |
+-------------------+-------------+
| Michael Zabalaoui |        1000 |
| Jerry Neumeyer    |        1100 |
| Richard Stringer  |        1330 |
| Janice Sogard     |        1430 |
+-------------------+-------------+
```

The problem with this output, though, is that the times aren't very pleasing looking. For more natural date and time displays, there are a few simple date formatting functions available and there are the [DATE\_FORMAT( )](../../reference/sql-functions/date-time-functions/date_format.md) and [TIME\_FORMAT( )](../../reference/sql-functions/date-time-functions/time_format.md) functions.

#### Fine Time Pieces

The simple functions that we mentioned are used for reformatting the output of days and months. To get the date of patient sessions for August, but in a more wordier format, [MONTHNAME( )](../../reference/sql-functions/date-time-functions/monthname.md) and [DAYNAME( )](../../reference/sql-functions/date-time-functions/dayname.md) could be used:

```sql
SELECT patient_name AS Patient, 
CONCAT(DAYNAME(appointment), ' - ', 
  MONTHNAME(appointment), ' ', 
  DAYOFMONTH(appointment), ', ', 
  YEAR(appointment)) AS Appointment
FROM billable_work, patients
WHERE doctor_id='1021'
  AND billable_work.patient_id =
    patients.patient_id
  AND appointment>'2017-08-01' 
  AND appointment<'2017-08-31' 
LIMIT 1;

+-------------------+-----------------------------+
| Patient           | Appointment                 |
+-------------------+-----------------------------+
| Michael Zabalaoui | Wednesday - August 30, 2017 |
+-------------------+-----------------------------+
```

In this statement the [CONCAT( )](../../reference/sql-functions/string-functions/concat.md) splices together the results of several date functions along with spaces and other characters. The [EXTRACT( )](../../reference/sql-functions/date-time-functions/extract.md) function was eliminated from the `WHERE` clause and instead a simple numeric test for sessions in August was given. Although [EXTRACT( )](../../reference/sql-functions/date-time-functions/extract.md) is fairly straightforward, this all can be accomplished with less typing by using the [DATE\_FORMAT( )](../../reference/sql-functions/date-time-functions/date_format.md) function.

The [DATE\_FORMAT( )](../../reference/sql-functions/date-time-functions/date_format.md) function has over thirty options for formatting the date to your liking. Plus, you can combine the options and add your own separators and other text. The syntax is `DATE_FORMAT(date_column, 'options & characters')`. As an example, let's reproduce the last SQL statement by using the [DATE\_FORMAT( )](../../reference/sql-functions/date-time-functions/date_format.md) function for formatting the date of the appointment and for scanning for appointments in July only:

```sql
SELECT patient_name AS Patient, 
DATE_FORMAT(appointment, '%W - %M %e, %Y') 
  AS Appointment
FROM billable_work, patients
WHERE doctor_id='1021'
  AND billable_work.patient_id = 
    patients.patient_id
  AND DATE_FORMAT(appointment, '%c') = 8
LIMIT 1;
```

This produces the exact same output as above, but with a more succinct statement. The option `%W` gives the name of the day of the week. The option `%M` provides the month's name. The option `%e` displays the day of the month (`%d` would work, but it left-pads single-digit dates with zeros). Finally, `%Y` is for the four character year. All other elements within the quotes (i.e., the spaces, the dash, and the comma) are literal characters for a nicer display.

With [DATE\_FORMAT( )](../../reference/sql-functions/date-time-functions/date_format.md), time elements of a field also can be formatted. For instance, suppose we also wanted the hour and minute of the appointment. We would only need to change the second line of the SQL statement above (to save space, patient\_name was eliminated):

```sql
SELECT 
DATE_FORMAT(appointment, '%W - %M %e, %Y at %r') 
  AS Appointment
...

+--------------------------------------------+
| Appointment                                |
+--------------------------------------------+
| Wednesday - August 30, 2017 at 02:11:19 AM |
+--------------------------------------------+
```

The word at was added along with the formatting option `%r` which gives the time with AM or PM at the end.

Although it may be a little confusing at first, once you've learned some of the common formatting options, [DATE\_FORMAT( )](../../reference/sql-functions/date-time-functions/date_format.md) is much easier to use than [EXTRACT( )](../../reference/sql-functions/date-time-functions/extract.md). There are many more options to [DATE\_FORMAT( )](../../reference/sql-functions/date-time-functions/date_format.md) that we haven't mentioned. For a complete list of the options available, see the [DATE\_FORMAT( ) documentation page](../../reference/sql-functions/date-time-functions/date_format.md).

#### Clean up Time

In addition to [DATE\_FORMAT( )](../../reference/sql-functions/date-time-functions/date_format.md), MariaDB has a comparable built-in function for formating only time: [TIME\_FORMAT( )](../../reference/sql-functions/date-time-functions/time_format.md). The syntax is the same and uses the same options as [DATE\_FORMAT( )](../../reference/sql-functions/date-time-functions/date_format.md), except only the time related formatting options apply. As an example, here's an SQL statement that a doctor might use at the beginning of each day to get a list of her appointments for the day:

```sql
SELECT patient_name AS Patient, 
TIME_FORMAT(appointment, '%l:%i %p') 
  AS Appointment
FROM billable_work, patients
WHERE doctor_id='1021'
  AND billable_work.patient_id = 
    patients.patient_id
  AND DATE_FORMAT(appointment, '%Y-%m-%d') =
    CURDATE();

+-------------------+-------------+
| Patient           | Appointment |
+-------------------+-------------+
| Michael Zabalaoui |    10:00 AM |
| Jerry Neumeyer    |    11:00 AM |
| Richard Stringer  |    01:30 PM |
| Janice Sogard     |    02:30 PM |
+-------------------+-------------+
```

The option `%l` provides the hours 01 through 12. The `%p` at the end indicates (with the AM or PM) whether the time is before or after noon. The `%i` option gives the minute. The colon and the space are for additional display appeal. Of course, all of this can be done exactly the same way with the [DATE\_FORMAT( )](../../reference/sql-functions/date-time-functions/date_format.md) function. As for the [DATE\_FORMAT( )](../../reference/sql-functions/date-time-functions/date_format.md) component in the WHERE clause here, the date is formatted exactly as it are with [CURDATE( )](../../reference/sql-functions/date-time-functions/curdate.md) (i.e., 2017-08-30) so that they may be compared properly.

#### Time to End

Many developers use PHP, Perl, or some other scripting language with MariaDB. Sometimes developers will solve retrieval problems with longer scripts rather than learn precisely how to extract temporal data with MariaDB. As you can see in several of the examples here (particularly the one using the [QUARTER( )](../../reference/sql-functions/date-time-functions/quarter.md) function), you can accomplish a great deal within MariaDB. When faced with a potentially complicated SQL statement, try creating it in the mariadb client first. Once you get what you need (under various conditions) and in the format desired, then copy the statement into your script. This practice can greatly help you improve your MariaDB statements and scripting code.

CC BY-SA / Gnu FDL
