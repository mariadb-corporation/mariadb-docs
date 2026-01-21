---
description: >-
  The mysql.help_relation table links help keywords to help topics, defining the
  structure of the server-side help system.
---

# mysql.help\_relation Table

`mysql.help_relation` is one of the four tables used by the [HELP command](../../sql-statements/administrative-sql-statements/help-command.md). It is populated when the server is installed by the `fill_help_tables.sql` script. The other help tables are [help\_topic](mysql-help_topic-table.md), [help\_category](mysql-help_category-table.md) and [help\_keyword](mysql-help_keyword-table.md).

This table uses the [Aria](../../../server-usage/storage-engines/aria/) storage engine.

The `mysql.help_relation` table contains the following fields:

| Field             | Type             | Null | Key | Default | Description |
| ----------------- | ---------------- | ---- | --- | ------- | ----------- |
| help\_topic\_id   | int(10) unsigned | NO   | PRI | NULL    |             |
| help\_keyword\_id | int(10) unsigned | NO   | PRI | NULL    |             |

## Example

```
...
|           106 |             456 |
|           463 |             456 |
|           468 |             456 |
|           463 |             457 |
|           194 |             458 |
|           478 |             458 |
|           374 |             459 |
|           459 |             459 |
|            39 |             460 |
|            58 |             460 |
|           185 |             460 |
|           264 |             460 |
|           269 |             460 |
|           209 |             461 |
|           468 |             461 |
|           201 |             462 |
|           468 |             463 |
+---------------+-----------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
