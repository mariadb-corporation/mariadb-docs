---
description: >-
  The mysql.time_zone_name table maps human-readable time zone names (e.g.,
  "Europe/Berlin") to their internal time zone IDs.
---

# mysql.time\_zone\_name Table

{% include "../../../.gitbook/includes/system-tables-warning.md" %}

The `mysql.time_zone_name` table is one of the mysql system tables that can contain [time zone](../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) information. It is usually preferable for the system to handle the time zone, in which case the table will be empty (the default), but you can populate the mysql time zone tables using the [mariadb-tzinfo-to-sql](../../../clients-and-utilities/administrative-tools/mariadb-tzinfo-to-sql.md) utility. See [Time Zones](../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) for details.

This table uses the [Aria](../../../server-usage/storage-engines/aria/) storage engine.

The `mysql.time_zone_name` table contains the following fields:

| Field          | Type             | Null | Key | Default | Description                 |
| -------------- | ---------------- | ---- | --- | ------- | --------------------------- |
| Name           | char(64)         | NO   | PRI | NULL    | Name of the time zone.      |
| Time\_zone\_id | int(10) unsigned | NO   | PRI | NULL    | ID field, auto\_increments. |

## Example

```sql
SELECT * FROM mysql.time_zone_name;
+--------------------+--------------+
| Name               | Time_zone_id |
+--------------------+--------------+
| Africa/Abidjan     |            1 |
| Africa/Accra       |            2 |
| Africa/Addis_Ababa |            3 |
| Africa/Algiers     |            4 |
| Africa/Asmara      |            5 |
| Africa/Asmera      |            6 |
| Africa/Bamako      |            7 |
| Africa/Bangui      |            8 |
| Africa/Banjul      |            9 |
| Africa/Bissau      |           10 |
...
+--------------------+--------------+
```

## See Also

* [mysql.time\_zone table](mysql-time_zone-table.md)
* [mysql.time\_zone\_leap\_second table](mysql-time_zone_leap_second-table.md)
* [mysql.time\_zone\_transition table](mysql-time_zone_transition-table.md)
* [mysql.time\_zone\_transition\_type table](mysql-time_zone_transition_type-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
