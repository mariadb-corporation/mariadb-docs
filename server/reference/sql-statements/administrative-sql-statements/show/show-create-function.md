---
description: >-
  Retrieve the CREATE FUNCTION statement. This statement shows the exact SQL
  used to define a stored function, including its body and characteristics.
---

# SHOW CREATE FUNCTION

## Syntax

```sql
SHOW CREATE FUNCTION func_name
```

## Description

This statement is similar to [SHOW CREATE PROCEDURE](show-create-procedure.md) but for [stored functions](../../../../server-usage/stored-routines/stored-functions/).

{% tabs %}
{% tab title="Current" %}
`SHOW CREATE FUNCTION` quotes identifiers, according to the value of the [sql\_quote\_show\_create](https://kb-archive.mariadb.net/kb/en/server-system-variables/#sql_quote_show_create) system variable.
{% endtab %}

{% tab title="< 10.6.5 / 10.5.13 / 10.4.22" %}
`SHOW CREATE FUNCTION` quotes identifiers, according to the value of the [sql\_quote\_show\_create](https://kb-archive.mariadb.net/kb/en/server-system-variables/#sql_quote_show_create) system variable. However, the output of this statement is unreliably affected by the [sql\_quote\_show\_create](https://kb-archive.mariadb.net/kb/en/server-system-variables/#sql_quote_show_create) system variable.
{% endtab %}
{% endtabs %}

## Example

```sql
SHOW CREATE FUNCTION VatCents\G
*************************** 1. row ***************************
            Function: VatCents
            sql_mode: 
     Create Function: CREATE DEFINER=`root`@`localhost` FUNCTION `VatCents`(price DECIMAL(10,2)) RETURNS int(11)
    DETERMINISTIC
BEGIN
 DECLARE x INT;
 SET x = price * 114;
 RETURN x;
END
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
```

## See Also

* [Stored Functions](../../../../server-usage/stored-routines/stored-functions/)
* [CREATE FUNCTION](../../data-definition/create/create-function.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
