# LEAST

## Syntax

```bnf
LEAST(value1,value2,...)
```

## Description

With two or more arguments, returns the smallest (minimum-valued) argument. The arguments are compared using the following rules:

* If the return value is used in an `INTEGER` context or all arguments are integer-valued, they are compared as integers.
* If the return value is used in a `REAL` context or all arguments are real-valued, they are compared as reals.
* If any argument is a case-sensitive string, the arguments are compared as case-sensitive strings.
* In all other cases, the arguments are compared as case-insensitive strings.

`LEAST()` returns `NULL` if any argument is `NULL`.

## Examples

```sql
SELECT LEAST(2,0);
+------------+
| LEAST(2,0) |
+------------+
|          0 |
+------------+
```

```sql
SELECT LEAST(34.0,3.0,5.0,767.0);
+---------------------------+
| LEAST(34.0,3.0,5.0,767.0) |
+---------------------------+
|                       3.0 |
+---------------------------+
```

```sql
SELECT LEAST('B','A','C');
+--------------------+
| LEAST('B','A','C') |
+--------------------+
| A                  |
+--------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
