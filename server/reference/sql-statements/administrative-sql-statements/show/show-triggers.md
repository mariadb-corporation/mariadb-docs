---
description: >-
  List triggers defined on tables. View metadata such as the trigger event,
  timing, and the table it is associated with.
---

# SHOW TRIGGERS

## Syntax

```sql
SHOW TRIGGERS [FROM db_name]
    [LIKE 'pattern' | WHERE expr]
```

## Description

{% tabs %}
{% tab title="Current" %}
`SHOW TRIGGERS` lists the triggers currently defined for tables in a database (the default database unless a `FROM` clause is given). This statement requires the [TRIGGER](show-privileges.md) privilege.
{% endtab %}

{% tab title="< 5.1.22" %}
`SHOW TRIGGERS` lists the triggers currently defined for tables in a database (the default database unless a `FROM` clause is given). This statement requires the `SUPER` privilege.
{% endtab %}
{% endtabs %}

The `LIKE` clause, if present on its own, indicates which table names to match and causes the statement to display triggers for those tables. The `WHERE` and `LIKE` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](extended-show.md).

Similar information is stored in the [information\_schema.TRIGGERS](../../../system-tables/information-schema/information-schema-tables/information-schema-triggers-table.md) table.

If there are multiple triggers for the same action, then the triggers are shown in action order.

## Examples

For the trigger defined at [Trigger Overview](../../../../server-usage/triggers-events/triggers/trigger-overview.md):

```sql
SHOW triggers Like 'animals' \G
*************************** 1. row ***************************
             Trigger: the_mooses_are_loose
               Event: INSERT
               Table: animals
           Statement: BEGIN
 IF NEW.name = 'Moose' THEN
  UPDATE animal_count SET animal_count.animals = animal_count.animals+100;
 ELSE 
  UPDATE animal_count SET animal_count.animals = animal_count.animals+1;
 END IF;
END
              Timing: AFTER
             Created: 2016-09-29 13:53:34.35
            sql_mode: 
             Definer: root@localhost
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
```

Listing all triggers associated with a certain table:

```sql
SHOW TRIGGERS FROM test WHERE `Table` = 'user' \G
*************************** 1. row ***************************
             Trigger: user_ai
               Event: INSERT
               Table: user
           Statement: BEGIN END
              Timing: AFTER
             Created:  2016-09-29 13:53:34.35
            sql_mode: 
             Definer: root@%
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
```

```sql
SHOW triggers WHERE Event Like 'Insert' \G
*************************** 1. row ***************************
             Trigger: the_mooses_are_loose
               Event: INSERT
               Table: animals
           Statement: BEGIN
 IF NEW.name = 'Moose' THEN
  UPDATE animal_count SET animal_count.animals = animal_count.animals+100;
 ELSE 
  UPDATE animal_count SET animal_count.animals = animal_count.animals+1;
 END IF;
END
              Timing: AFTER
             Created: 2016-09-29 13:53:34.35
            sql_mode: 
             Definer: root@localhost
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
```

{% tabs %}
{% tab title="Current" %}
`character_set_client` is the session value of the [character\_set\_client](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#character_set_client) system variable when the trigger was created.

`collation_connection` is the session value of the [collation\_connection](../../../../../server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables.md#collation_connection) system variable when the trigger was created.

`Database Collation` is the collation of the database with which the trigger is associated.
{% endtab %}

{% tab title="< 5.1.21" %}
`character_set_client`, `collation_connection`, and`Database Collation` are not available.
{% endtab %}
{% endtabs %}

{% hint style="info" %}
Old triggers created before MySQL 5.7 and MariaDB 10.2.3 have NULL in the `Created` column.
{% endhint %}

## See also

* [Trigger Overview](../../../../server-usage/triggers-events/triggers/trigger-overview.md)
* [CREATE TRIGGER](../../../../server-usage/triggers-events/triggers/create-trigger.md)
* [DROP TRIGGER](../../data-definition/drop/drop-trigger.md)
* [information\_schema.TRIGGERS](../../../system-tables/information-schema/information-schema-tables/information-schema-triggers-table.md) table
* [SHOW CREATE TRIGGER](show-create-trigger.md)
* [Trigger Limitations](../../../../server-usage/triggers-events/triggers/trigger-limitations.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
