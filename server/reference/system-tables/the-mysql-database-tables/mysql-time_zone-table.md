---
description: >-
  The mysql.time_zone table assigns a unique ID to each time zone supported by
  the server, linking to other time zone system tables.
---

# mysql.time\_zone Table

The `mysql.time_zone` table is one of the mysql system tables that can contain [time zone](../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) information. It is usually preferable for the system to handle the time zone, in which case the table will be empty (the default), but you can populate the mysql time zone tables using the [mariadb-tzinfo-to-sql](../../../clients-and-utilities/administrative-tools/mariadb-tzinfo-to-sql.md) utility. See [Time Zones](../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) for details.

This table uses the [Aria](../../../server-usage/storage-engines/aria/) storage engine.

The `mysql.time_zone` table contains the following fields:

| Field              | Type             | Null | Key | Default | Description                           |
| ------------------ | ---------------- | ---- | --- | ------- | ------------------------------------- |
| Time\_zone\_id     | int(10) unsigned | NO   | PRI | NULL    | ID field, auto\_increments.           |
| Use\_leap\_seconds | enum('Y','N')    | NO   |     | N       | Whether or not leap seconds are used. |

## Example

```sql
SELECT * FROM mysql.time_zone;
+--------------+------------------+
| Time_zone_id | Use_leap_seconds |
+--------------+------------------+
|            1 | N                |
|            2 | N                |
|            3 | N                |
|            4 | N                |
|            5 | N                |
|            6 | N                |
|            7 | N                |
|            8 | N                |
|            9 | N                |
|           10 | N                |
...
+--------------+------------------+
```

## See Also

* [mysql.time\_zone\_leap\_second table](mysql-time_zone_leap_second-table.md)
* [mysql.time\_zone\_name table](mysql-time_zone_name-table.md)
* [mysql.time\_zone\_transition table](mysql-time_zone_transition-table.md)
* [mysql.time\_zone\_transition\_type table](mysql-time_zone_transition_type-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
