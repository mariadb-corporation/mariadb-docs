---
description: >-
  Return a format string. This function provides standard format strings for
  DATE_FORMAT and STR_TO_DATE based on regions like 'USA' or 'EUR'.
---

# GET\_FORMAT

## Syntax

```sql
GET_FORMAT({DATE|DATETIME|TIME}, {'EUR'|'USA'|'JIS'|'ISO'|'INTERNAL'})
```

## Description

Returns a format string. This function is useful in combination with the [DATE\_FORMAT()](date_format.md) and the [STR\_TO\_DATE()](str_to_date.md) functions.

Possible result formats are:

| Function Call                    | Result Format       |
| -------------------------------- | ------------------- |
| GET\_FORMAT(DATE,'EUR')          | '%d.%m.%Y'          |
| GET\_FORMAT(DATE,'USA')          | '%m.%d.%Y'          |
| GET\_FORMAT(DATE,'JIS')          | '%Y-%m-%d'          |
| GET\_FORMAT(DATE,'ISO')          | '%Y-%m-%d'          |
| GET\_FORMAT(DATE,'INTERNAL')     | '%Y%m%d'            |
| GET\_FORMAT(DATETIME,'EUR')      | '%Y-%m-%d %H.%i.%s' |
| GET\_FORMAT(DATETIME,'USA')      | '%Y-%m-%d %H.%i.%s' |
| GET\_FORMAT(DATETIME,'JIS')      | '%Y-%m-%d %H:%i:%s' |
| GET\_FORMAT(DATETIME,'ISO')      | '%Y-%m-%d %H:%i:%s' |
| GET\_FORMAT(DATETIME,'INTERNAL') | '%Y%m%d%H%i%s'      |
| GET\_FORMAT(TIME,'EUR')          | '%H.%i.%s'          |
| GET\_FORMAT(TIME,'USA')          | '%h:%i:%s %p'       |
| GET\_FORMAT(TIME,'JIS')          | '%H:%i:%s'          |
| GET\_FORMAT(TIME,'ISO')          | '%H:%i:%s'          |
| GET\_FORMAT(TIME,'INTERNAL')     | '%H%i%s'            |

## Examples

Obtaining the string matching to the standard European date format:

```sql
SELECT GET_FORMAT(DATE, 'EUR');
+-------------------------+
| GET_FORMAT(DATE, 'EUR') |
+-------------------------+
| %d.%m.%Y                |
+-------------------------+
```

Using the same string to format a date:

```sql
SELECT DATE_FORMAT('2003-10-03',GET_FORMAT(DATE,'EUR'));
+--------------------------------------------------+
| DATE_FORMAT('2003-10-03',GET_FORMAT(DATE,'EUR')) |
+--------------------------------------------------+
| 03.10.2003                                       |
+--------------------------------------------------+

SELECT STR_TO_DATE('10.31.2003',GET_FORMAT(DATE,'USA'));
+--------------------------------------------------+
| STR_TO_DATE('10.31.2003',GET_FORMAT(DATE,'USA')) |
+--------------------------------------------------+
| 2003-10-31                                       |
+--------------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
