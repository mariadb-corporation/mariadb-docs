---
description: >-
  Retrieve the CREATE TRIGGER statement. This statement displays the SQL syntax
  defining a specific trigger and its timing events.
---

# SHOW CREATE TRIGGER

## Syntax

```sql
SHOW CREATE TRIGGER trigger_name
```

## Description

This statement shows a [CREATE TRIGGER](../../../../../server-usage/programming-customizing-mariadb/triggers-events/triggers/create-trigger.md) statement that creates the given trigger, as well as the [SQL\_MODE](../../../../server-management/variables-and-modes/sql_mode.md) that was used when the trigger has been created and the character set used by the connection.

The [TRIGGER](../../account-management-sql-commands/grant.md#table-privileges) privilege is required on the table the trigger is defined for to execute this statement.

{% tabs %}
{% tab title="Current" %}
`SHOW CREATE TRIGGER` quotes identifiers, according to the value of the [sql\_quote\_show\_create](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) system variable.
{% endtab %}

{% tab title="< 10.6.5 / 10.5.13 / 10.4.22" %}
`SHOW CREATE TRIGGER` quotes identifiers, according to the value of the [sql\_quote\_show\_create](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) system variable. However, the output of this statement is unreliably affected by the [sql\_quote\_show\_create](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) system variable.
{% endtab %}
{% endtabs %}

## Examples

```sql
SHOW CREATE TRIGGER example\G
*************************** 1. row ***************************
               Trigger: example
              sql_mode: ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,STRICT_ALL_TABLES
,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_
ENGINE_SUBSTITUTION
SQL Original Statement: CREATE DEFINER=`root`@`localhost` TRIGGER example BEFORE
 INSERT ON t FOR EACH ROW
BEGIN
        SET NEW.c = NEW.c * 2;
END
  character_set_client: cp850
  collation_connection: cp850_general_ci
  Database Collation: utf8_general_ci
  Created: 2016-09-29 13:53:34.35
```

{% tabs %}
{% tab title="Current" %}
The `Created` column serves to better view multiple trigger events.
{% endtab %}

{% tab title="< 10.2.3" %}
The `Created` column is unavailable.
{% endtab %}
{% endtabs %}

## See Also

* [Trigger Overview](../../../../server-usage/triggers-events/triggers/trigger-overview.md)
* [CREATE TRIGGER](../../../../server-usage/triggers-events/triggers/create-trigger.md)
* [DROP TRIGGER](../../data-definition/drop/drop-trigger.md)
* [information\_schema.TRIGGERS Table](../../../system-tables/information-schema/information-schema-tables/information-schema-triggers-table.md)
* [SHOW TRIGGERS](show-triggers.md)
* [Trigger Limitations](../../../../server-usage/triggers-events/triggers/trigger-limitations.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
