---
description: >-
  Return the name of the month. This function returns the full name of the
  month, such as 'January' or 'December', for a given date.
---

# MONTHNAME

## Syntax

```sql
MONTHNAME(date)
```

## Description

Returns the full name of the month for date. The language used for the name is controlled by the value of the [lc\_time\_names](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#lc_time_names) system variable. See [server locale](../../data-types/string-data-types/character-sets/internationalization-and-localization/server-locale.md) for more on the supported locales.

## Examples

```sql
SELECT MONTHNAME('2019-02-03');
+-------------------------+
| MONTHNAME('2019-02-03') |
+-------------------------+
| February                |
+-------------------------+
```

Changing the locale:

```sql
SET lc_time_names = 'fr_CA';

SELECT MONTHNAME('2019-05-21');
+-------------------------+
| MONTHNAME('2019-05-21') |
+-------------------------+
| mai                     |
+-------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
