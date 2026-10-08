---
description: >-
  The Information Schema PERIODS table provides information about
  Application-Time Periods, detailing the start and end columns for system
  versioning.
---

# Information Schema PERIODS Table

{% hint style="info" %}
This table is available as of MariaDB 11.4.
{% endhint %}

The [Information Schema](../) `PERIODS` table provides information about [Application-Time Periods](../../../sql-structure/temporal-tables/application-time-periods.md).

It contains the following columns:

| Column              | Description                                |
| ------------------- | ------------------------------------------ |
| TABLE\_CATALOG      | Always contains the string 'def'.          |
| TABLE\_SCHEMA       | Database name.                             |
| TABLE\_NAME         | Table name.                                |
| PERIOD              | Period name.                               |
| START\_COLUMN\_NAME | Name of the column that starts the period. |
| END\_COLUMN\_NAME   | Name of the column that ends the period.   |

## Example

```sql
CREATE OR REPLACE TABLE t1(
 name VARCHAR(50), 
 date_1 DATE, 
 date_2 DATE, 
 PERIOD FOR date_period(date_1, date_2)
);

SELECT * FROM INFORMATION_SCHEMA.PERIODS;
+---------------+--------------+------------+-------------+-------------------+-----------------+
| TABLE_CATALOG | TABLE_SCHEMA | TABLE_NAME | PERIOD      | START_COLUMN_NAME | END_COLUMN_NAME |
+---------------+--------------+------------+-------------+-------------------+-----------------+
| def           | test         | t1         | date_period | date_1            | date_2          |
+---------------+--------------+------------+-------------+-------------------+-----------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
