---
description: >-
  Format a number. This function formats a number to a format like
  '#,###,###.##', rounded to a specified number of decimal places.
---

# FORMAT

## Syntax

```
FORMAT(num, decimal_position[, locale])
```

## Description

Formats the given number for display as a string, adding separators to appropriate position and rounding the results to the given decimal position. For instance, it would format `15233.345` to `15,233.35`.

If the given decimal position is `0`, it rounds to return no decimal point or fractional part. You can optionally specify a [locale](../../data-types/string-data-types/character-sets/internationalization-and-localization/server-locale.md) value to format numbers to the pattern appropriate for the given region.

## Examples

```sql
SELECT FORMAT(1234567890.09876543210, 4) AS 'Format';
+--------------------+
| Format             |
+--------------------+
| 1,234,567,890.0988 |
+--------------------+

SELECT FORMAT(1234567.89, 4) AS 'Format';
+----------------+
| Format         |
+----------------+
| 1,234,567.8900 |
+----------------+

SELECT FORMAT(1234567.89, 0) AS 'Format';
+-----------+
| Format    |
+-----------+
| 1,234,568 |
+-----------+

-- Format number to German number formatting
SELECT FORMAT(123456789,2,'de_DE') AS 'Format';
+----------------+
| Format         |
+----------------+
| 123.456.789,00 |
+----------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
