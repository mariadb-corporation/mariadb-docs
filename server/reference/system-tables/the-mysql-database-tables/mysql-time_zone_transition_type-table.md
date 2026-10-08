---
description: >-
  The mysql.time_zone_transition_type table describes the properties of time
  zone transitions, such as the offset and abbreviation.
---

# mysql.time\_zone\_transition\_type Table

{% include "../../../.gitbook/includes/system-tables-warning.md" %}

The `mysql.time_zone_transition_type` table is one of the `mysql` system tables that can contain [time zone](../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) information. It is usually preferable for the system to handle the time zone, in which case the table will be empty (the default), but you can populate the `mysql` time zone tables using the [mariadb-tzinfo-to-sql](../../../clients-and-utilities/administrative-tools/mariadb-tzinfo-to-sql.md) utility. See [Time Zones](../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) for details.

This table uses the [Aria](../../../server-usage/storage-engines/aria/) storage engine.

The `mysql.time_zone_transition_type` table contains the following fields:

| Field                | Type                | Null | Key | Default | Description |
| -------------------- | ------------------- | ---- | --- | ------- | ----------- |
| Time\_zone\_id       | int(10) unsigned    | NO   | PRI | NULL    |             |
| Transition\_type\_id | int(10) unsigned    | NO   | PRI | NULL    |             |
| Offset               | int(11)             | NO   |     | 0       |             |
| Is\_DST              | tinyint(3) unsigned | NO   |     | 0       |             |
| Abbreviation         | char(8)             | NO   |     |         |             |

## Example

```sql
SELECT * FROM mysql.time_zone_transition_type;
+--------------+--------------------+--------+--------+--------------+
| Time_zone_id | Transition_type_id | Offset | Is_DST | Abbreviation |
+--------------+--------------------+--------+--------+--------------+
|            1 |                  0 |   -968 |      0 | LMT          |
|            1 |                  1 |      0 |      0 | GMT          |
|            2 |                  0 |    -52 |      0 | LMT          |
|            2 |                  1 |   1200 |      1 | GHST         |
|            2 |                  2 |      0 |      0 | GMT          |
|            3 |                  0 |   8836 |      0 | LMT          |
|            3 |                  1 |  10800 |      0 | EAT          |
|            3 |                  2 |   9000 |      0 | BEAT         |
|            3 |                  3 |   9900 |      0 | BEAUT        |
|            3 |                  4 |  10800 |      0 | EAT          |
...
+--------------+--------------------+--------+--------+--------------+
```

## See Also

* [mysql.time\_zone table](mysql-time_zone-table.md)
* [mysql.time\_zone\_leap\_second table](mysql-time_zone_leap_second-table.md)
* [mysql.time\_zone\_name table](mysql-time_zone_name-table.md)
* [mysql.time\_zone\_transition table](mysql-time_zone_transition-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
