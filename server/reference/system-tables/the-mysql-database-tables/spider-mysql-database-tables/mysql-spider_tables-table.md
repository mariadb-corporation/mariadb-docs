---
description: >-
  This table stores specific parameters and metadata for Spider tables, defining
  how they map to remote backend tables.
---

# mysql.spider\_tables Table

The `mysql.spider_tables` table is installed by the [Spider storage engine](../../../../server-usage/storage-engines/spider/).

This table uses the [Aria](../../../../server-usage/storage-engines/aria/) storage engine.

It contains the following fields:

| Field                                | Type       | Null | Key | Default | Description |
| ------------------------------------ | ---------- | ---- | --- | ------- | ----------- |
| db\_name                             | char(64)   | NO   | PRI |         |             |
| table\_name                          | char(199)  | NO   | PRI |         |             |
| link\_id                             | int(11)    | NO   | PRI | 0       |             |
| priority                             | bigint(20) | NO   | MUL | 0       |             |
| server                               | char(64)   | YES  |     | NULL    |             |
| scheme                               | char(64)   | YES  |     | NULL    |             |
| host                                 | char(64)   | YES  |     | NULL    |             |
| port                                 | char(5)    | YES  |     | NULL    |             |
| socket                               | text       | YES  |     | NULL    |             |
| username                             | char(64)   | YES  |     | NULL    |             |
| password                             | char(64)   | YES  |     | NULL    |             |
| ssl\_ca                              | text       | YES  |     | NULL    |             |
| ssl\_capath                          | text       | YES  |     | NULL    |             |
| ssl\_cert                            | text       | YES  |     | NULL    |             |
| ssl\_cipher                          | char(64)   | YES  |     | NULL    |             |
| ssl\_key                             | text       | YES  |     | NULL    |             |
| ssl\_verify\_server\_cert            | tinyint(4) | NO   |     | 0       |             |
| monitoring\_binlog\_pos\_at\_failing | tinyint(4) | NO   |     | 0       |             |
| default\_file                        | text       | YES  |     | NULL    |             |
| default\_group                       | char(64)   | YES  |     | NULL    |             |
| dsn                                  | char(64)   | YES  |     | NULL    |             |
| filedsn                              | text       | YES  |     | NULL    |             |
| driver                               | char(64)   | YES  |     | NULL    |             |
| tgt\_db\_name                        | char(64)   | YES  |     | NULL    |             |
| tgt\_table\_name                     | char(64)   | YES  |     | NULL    |             |
| link\_status                         | tinyint(4) | NO   |     | 1       |             |
| block\_status                        | tinyint(4) | NO   |     | 0       |             |
| static\_link\_id                     | char(64)   | YES  |     | NULL    |             |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
