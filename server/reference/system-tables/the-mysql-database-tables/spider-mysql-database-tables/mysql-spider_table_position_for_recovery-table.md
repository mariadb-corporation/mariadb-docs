---
description: >-
  This table records XA transaction positions for Spider tables, essential for
  recovering distributed transactions after a crash.
---

# mysql.spider\_table\_position\_for\_recovery Table

The `mysql.spider_table_position_for_recovery` table is installed by the [Spider storage engine](../../../../server-usage/storage-engines/spider/).

This table uses the [Aria](../../../../server-usage/storage-engines/aria/) storage engine.

It contains the following fields:

| Field            | Type      | Null | Key | Default | Description |
| ---------------- | --------- | ---- | --- | ------- | ----------- |
| db\_name         | char(64)  | NO   | PRI |         |             |
| table\_name      | char(199) | NO   | PRI |         |             |
| failed\_link\_id | int(11)   | NO   | PRI | 0       |             |
| source\_link\_id | int(11)   | NO   | PRI | 0       |             |
| file             | text      | YES  |     | NULL    |             |
| position         | text      | YES  |     | NULL    |             |
| gtid             | text      | YES  |     | NULL    |             |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
