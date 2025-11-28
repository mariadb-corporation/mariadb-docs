---
description: >-
  The mysql.spider_table_sts table holds statistics such as row counts and data
  length for Spider tables, supporting the optimizer.
---

# mysql.spider\_table\_sts Table

The `mysql.spider_table_sts` table is installed by the [Spider storage engine](../../../../server-usage/storage-engines/spider/).

This table uses the [Aria](../../../../server-usage/storage-engines/aria/) storage engine.

It contains the following fields:

| Field                   | Type                | Null | Key | Default             | Description |
| ----------------------- | ------------------- | ---- | --- | ------------------- | ----------- |
| db\_name                | char(64)            | NO   | PRI |                     |             |
| table\_name             | char(199)           | NO   | PRI |                     |             |
| data\_file\_length      | bigint(20) unsigned | NO   |     | 0                   |             |
| max\_data\_file\_length | bigint(20) unsigned | NO   |     | 0                   |             |
| index\_file\_length     | bigint(20) unsigned | NO   |     | 0                   |             |
| records                 | bigint(20) unsigned | NO   |     | 0                   |             |
| mean\_rec\_length       | bigint(20) unsigned | NO   |     | 0                   |             |
| check\_time             | datetime            | NO   |     | 0000-00-00 00:00:00 |             |
| create\_time            | datetime            | NO   |     | 0000-00-00 00:00:00 |             |
| update\_time            | datetime            | NO   |     | 0000-00-00 00:00:00 |             |
| checksum                | bigint(20) unsigned | YES  |     | NULL                |             |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
