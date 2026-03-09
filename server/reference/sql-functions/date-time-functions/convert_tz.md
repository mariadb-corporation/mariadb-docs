---
description: >-
  Convert a datetime value between time zones. This function shifts a timestamp
  from a source time zone to a target time zone.
---

# CONVERT\_TZ

## Syntax

```sql
CONVERT_TZ(dt,from_tz,to_tz)
```

## Description

`CONVERT_TZ()` converts a datetime value _dt_ from the [time zone](../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) given by _from\_tz_ to the time zone given by _to\_tz_ and returns the resulting value.

In order to use named time zones, such as GMT, MET or Africa/Johannesburg, the `time_zone` tables must be loaded (see [mysql\_tzinfo\_to\_sql](../../../clients-and-utilities/legacy-clients-and-utilities/mysql_tzinfo_to_sql.md)).

No conversion takes place if the value falls outside of the supported `TIMESTAMP` range when converted from _from\_tz_ to UTC.

{% tabs %}
{% tab title="Currrent" %}
The supported range is `1970-01-01 00:00:00` to `2106-02-07 06:28:15` UTC.
{% endtab %}

{% tab title="< 11.5" %}
The supported range is `1970-01-01 00:00:01` to `2038-01-19 05:14:07` UTC.
{% endtab %}
{% endtabs %}

This function returns `NULL` if the arguments are invalid (or named time zones have not been loaded).

See [time zones](../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md) for more information.

## Examples

```sql
SELECT CONVERT_TZ('2016-01-01 12:00:00','+00:00','+10:00');
+-----------------------------------------------------+
| CONVERT_TZ('2016-01-01 12:00:00','+00:00','+10:00') |
+-----------------------------------------------------+
| 2016-01-01 22:00:00                                 |
+-----------------------------------------------------+
```

Using named time zones (with the time zone tables loaded):

```sql
SELECT CONVERT_TZ('2016-01-01 12:00:00','GMT','Africa/Johannesburg');
+---------------------------------------------------------------+
| CONVERT_TZ('2016-01-01 12:00:00','GMT','Africa/Johannesburg') |
+---------------------------------------------------------------+
| 2016-01-01 14:00:00                                           |
+---------------------------------------------------------------+
```

The value is out of the `TIMESTAMP` range, so no conversion takes place:

```sql
SELECT CONVERT_TZ('1969-12-31 22:00:00','+00:00','+10:00');
+-----------------------------------------------------+
| CONVERT_TZ('1969-12-31 22:00:00','+00:00','+10:00') |
+-----------------------------------------------------+
| 1969-12-31 22:00:00                                 |
+-----------------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
