---
description: >-
  Return the current date and time. This function returns the current timestamp
  as a value in 'YYYY-MM-DD HH:MM:SS' or YYYYMMDDHHMMSS format.
---

# NOW

## Syntax

```sql
NOW([precision])
CURRENT_TIMESTAMP
CURRENT_TIMESTAMP([precision])
LOCALTIME, LOCALTIME([precision])
LOCALTIMESTAMP
LOCALTIMESTAMP([precision])
```

## Description

Returns the current date and time as a value in `YYYY-MM-DD HH:MM:SS` or `YYYYMMDDHHMMSS.uuuuuu` format, depending on whether the function is used in a string or numeric context. The value is expressed in the current [time zone](../../data-types/string-data-types/character-sets/internationalization-and-localization/time-zones.md).

**MariaDB starting with** [**11.7**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-11-7-rolling-releases/what-is-mariadb-117)

{% tabs %}
{% tab title="Current" %}
These functions return SQL standard compliant types:

* `NOW()` and `CURRENT_TIMESTAMP()` return a `TIMESTAMP` value (analogous to the standard type `TIMESTAMP WITH LOCAL TIME ZONE`) which corresponds to the current point in time and is unambiguous around DST changes.
* `LOCALTIMESTAMP` returns a `DATETIME` value (analogous to the standard type `TIMESTAMP WITHOUT TIME ZONE`). Storing its result in a `TIMESTAMP` column can result in a data loss around DST changes.
{% endtab %}

{% tab title="< 11.7" %}
These functions do **not** return SQL standard compliant types:

* `NOW()`
* `CURRENT_TIMESTAMP()`
* `LOCALTIMESTAMP`
{% endtab %}
{% endtabs %}

The optional _precision_ determines the microsecond precision. See [Microseconds in MariaDB](microseconds-in-mariadb.md).

`NOW()` (or its synonyms) can be used as the default value for [TIMESTAMP](../../data-types/date-and-time-data-types/timestamp.md) columns as well as.

When displayed in the [INFORMATION\_SCHEMA.COLUMNS](../../system-tables/information-schema/information-schema-tables/information-schema-columns-table.md) table, a default [CURRENT TIMESTAMP](current_timestamp.md) is displayed as `current_timestamp()` .

Changing the [timestamp system variable](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#timestamp) with a [SET](../../sql-statements/administrative-sql-statements/set-commands/set.md) `timestamp` statement affects the value returned by `NOW()`, but not by [SYSDATE()](sysdate.md).

## Examples

```sql
SELECT NOW();
+---------------------+
| NOW()               |
+---------------------+
| 2010-03-27 13:13:25 |
+---------------------+

SELECT NOW() + 0;
+-----------------------+
| NOW() + 0             |
+-----------------------+
| 20100327131329.000000 |
+-----------------------+
```

With precision:

```sql
SELECT CURRENT_TIMESTAMP(2);
+------------------------+
| CURRENT_TIMESTAMP(2)   |
+------------------------+
| 2018-07-10 09:47:26.24 |
+------------------------+
```

Used as a default TIMESTAMP:

```sql
CREATE TABLE t (createdTS TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP);
```

```sql
SELECT * FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA='test'
  AND COLUMN_NAME LIKE '%ts%'\G
*************************** 1. row ***************************
           TABLE_CATALOG: def
            TABLE_SCHEMA: test
              TABLE_NAME: t
             COLUMN_NAME: ts
        ORDINAL_POSITION: 1
          COLUMN_DEFAULT: current_timestamp()
...
```

## See Also

* [Microseconds in MariaDB](microseconds-in-mariadb.md)
* [timestamp server system variable](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#timestamp)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
