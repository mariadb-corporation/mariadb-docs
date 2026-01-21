---
description: >-
  This table defines the remote servers used for link monitoring in the Spider
  storage engine, ensuring high availability and failover handling.
---

# mysql.spider\_link\_mon\_servers Table

The `mysql.spider_link_mon_servers` table is installed by the [Spider storage engine](../../../../server-usage/storage-engines/spider/).

This table uses the [Aria](../../../../server-usage/storage-engines/aria/) storage engine.

It contains the following fields:

| Field                     | Type             | Null | Key | Default | Description |
| ------------------------- | ---------------- | ---- | --- | ------- | ----------- |
| db\_name                  | char(64)         | NO   | PRI |         |             |
| table\_name               | char(199)        | NO   | PRI |         |             |
| link\_id                  | char(64)         | NO   | PRI |         |             |
| sid                       | int(10) unsigned | NO   | PRI | 0       |             |
| server                    | char(64)         | YES  |     | NULL    |             |
| scheme                    | char(64)         | YES  |     | NULL    |             |
| host                      | char(64)         | YES  |     | NULL    |             |
| port                      | char(5)          | YES  |     | NULL    |             |
| socket                    | text             | YES  |     | NULL    |             |
| username                  | char(64)         | YES  |     | NULL    |             |
| password                  | char(64)         | YES  |     | NULL    |             |
| ssl\_ca                   | text             | YES  |     | NULL    |             |
| ssl\_capath               | text             | YES  |     | NULL    |             |
| ssl\_cert                 | text             | YES  |     | NULL    |             |
| ssl\_cipher               | char(64)         | YES  |     | NULL    |             |
| ssl\_key                  | text             | YES  |     | NULL    |             |
| ssl\_verify\_server\_cert | tinyint(4)       | NO   |     | 0       |             |
| default\_file             | text             | YES  |     | NULL    |             |
| default\_group            | char(64)         | YES  |     | NULL    |             |
| dsn                       | char(64)         | YES  |     | NULL    |             |
| filedsn                   | text             | YES  |     | NULL    |             |
| driver                    | char(64)         | YES  |     | NULL    |             |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
