---
description: >-
  The Information Schema LOCALES table lists all compiled-in locales available
  to the server, providing their IDs, names, and descriptions.
---

# Information Schema LOCALES Table

## Description

The [Information Schema](../) `LOCALES` table contains a list of all compiled-in locales. It is only available if the [LOCALES plugin](../../../data-types/string-data-types/character-sets/internationalization-and-localization/locales-plugin.md) has been installed.

It contains the following columns:

| Column                   | Description                                               |
| ------------------------ | --------------------------------------------------------- |
| ID                       | Row ID.                                                   |
| NAME                     | Locale name, for example en\_GB.                          |
| DESCRIPTION              | Locale description, for example English - United Kingdom. |
| MAX\_MONTH\_NAME\_LENGTH | Numeric length of the longest month in the locale         |
| MAX\_DAY\_NAME\_LENGTH   | Numeric length of the longest day name in the locale.     |
| DECIMAL\_POINT           | Decimal point character (some locales use a comma).       |
| THOUSAND\_SEP            | Thousand's character separator,                           |
| ERROR\_MESSAGE\_LANGUAGE | Error message language.                                   |

The table is not a standard Information Schema table, and is a MariaDB extension.

The [SHOW LOCALES](../../../sql-statements/administrative-sql-statements/show/show-locales.md) statement returns a subset of the information.

## Example

```sql
SELECT * FROM information_schema.LOCALES;
+-----+-------+-------------------------------------+-----------------------+---------------------+---------------+--------------+------------------------+
| ID  | NAME  | DESCRIPTION                         | MAX_MONTH_NAME_LENGTH | MAX_DAY_NAME_LENGTH | DECIMAL_POINT | THOUSAND_SEP | ERROR_MESSAGE_LANGUAGE |
+-----+-------+-------------------------------------+-----------------------+---------------------+---------------+--------------+------------------------+
|   0 | en_US | English - United States             |                     9 |                   9 | .             | ,            | english                |
|   1 | en_GB | English - United Kingdom            |                     9 |                   9 | .             | ,            | english                |
|   2 | ja_JP | Japanese - Japan                    |                     3 |                   3 | .             | ,            | japanese               |
|   3 | sv_SE | Swedish - Sweden                    |                     9 |                   7 | ,             |              | swedish                |
|   4 | de_DE | German - Germany                    |                     9 |                  10 | ,             | .            | german                 |
|   5 | fr_FR | French - France                     |                     9 |                   8 | ,             |              | french                 |
|   6 | ar_AE | Arabic - United Arab Emirates       |                     6 |                   8 | .             | ,            | english                |
|   7 | ar_BH | Arabic - Bahrain                    |                     6 |                   8 | .             | ,            | english                |
|   8 | ar_JO | Arabic - Jordan                     |                    12 |                   8 | .             | ,            | english                |
...
| 106 | no_NO | Norwegian - Norway                  |                     9 |                   7 | ,             | .            | norwegian              |
| 107 | sv_FI | Swedish - Finland                   |                     9 |                   7 | ,             |              | swedish                |
| 108 | zh_HK | Chinese - Hong Kong SAR             |                     3 |                   3 | .             | ,            | english                |
| 109 | el_GR | Greek - Greece                      |                    11 |                   9 | ,             | .            | greek                  |
+-----+-------+-------------------------------------+-----------------------+---------------------+---------------+--------------+------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
