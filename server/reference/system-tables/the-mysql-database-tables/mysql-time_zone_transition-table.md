---
description: >-
  The mysql.time_zone_transition table defines the exact times at which daylight
  saving time or other time zone transitions occur.
---

# mysql.time\_zone\_transition Table

{% include "../../../.gitbook/includes/system-tables-warning.md" %}

The `mysql.time_zone_transition` table is one of the `mysql` system tables that can contain [time zone](../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) information. It is usually preferable for the system to handle the time zone, in which case the table will be empty (the default), but you can populate the `mysql` time zone tables using the [mariadb-tzinfo-to-sql](../../../clients-and-utilities/administrative-tools/mariadb-tzinfo-to-sql.md) utility. See [Time Zones](../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) for details.

This table uses the [Aria](../../../server-usage/storage-engines/aria/) storage engine.

The `mysql.time_zone_transition` table contains the following fields:

| Field                | Type             | Null | Key | Default | Description |
| -------------------- | ---------------- | ---- | --- | ------- | ----------- |
| Time\_zone\_id       | int(10) unsigned | NO   | PRI | NULL    |             |
| Transition\_time     | bigint(20)       | NO   | PRI | NULL    |             |
| Transition\_type\_id | int(10) unsigned | NO   |     | NULL    |             |

## Example

```sql
SELECT * FROM mysql.time_zone_transition;
+--------------+-----------------+--------------------+
| Time_zone_id | Transition_time | Transition_type_id |
+--------------+-----------------+--------------------+
|            1 |     -1830383032 |                  1 |
|            2 |     -1640995148 |                  2 |
|            2 |     -1556841600 |                  1 |
|            2 |     -1546388400 |                  2 |
|            2 |     -1525305600 |                  1 |
|            2 |     -1514852400 |                  2 |
|            2 |     -1493769600 |                  1 |
|            2 |     -1483316400 |                  2 |
|            2 |     -1462233600 |                  1 |
|            2 |     -1451780400 |                  2 |
...
+--------------+-----------------+--------------------+
```

## See Also

* [mysql.time\_zone table](mysql-time_zone-table.md)
* [mysql.time\_zone\_leap\_second table](mysql-time_zone_leap_second-table.md)
* [mysql.time\_zone\_name table](mysql-time_zone_name-table.md)
* [mysql.time\_zone\_transition\_type table](mysql-time_zone_transition_type-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
