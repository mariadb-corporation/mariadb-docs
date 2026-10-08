---
description: >-
  The mysql.time_zone_leap_second table lists leap second corrections to be
  applied to specific time zones.
---

# mysql.time\_zone\_leap\_second Table

{% include "../../../.gitbook/includes/system-tables-warning.md" %}

The `mysql.time_zone_leap_second` table is one of the mysql system tables that can contain [time zone](../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) information. It is usually preferable for the system to handle the time zone, in which case the table will be empty (the default), but you can populate the mysql time zone tables using the [mariadb-tzinfo-to-sql](../../../clients-and-utilities/administrative-tools/mariadb-tzinfo-to-sql.md) utility. See [Time Zones](../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) for details.

This table uses the [Aria](../../../server-usage/storage-engines/aria/) storage engine.

The `mysql.time_zone_leap_second` table contains the following fields:

| Field            | Type       | Null | Key | Default | Description |
| ---------------- | ---------- | ---- | --- | ------- | ----------- |
| Transition\_time | bigint(20) | NO   | PRI | NULL    |             |
| Correction       | int(11)    | NO   |     | NULL    |             |

## See Also

* [mysql.time\_zone table](mysql-time_zone-table.md)
* [mysql.time\_zone\_name table](mysql-time_zone_name-table.md)
* [mysql.time\_zone\_transition table](mysql-time_zone_transition-table.md)
* [mysql.time\_zone\_transition\_type table](mysql-time_zone_transition_type-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
