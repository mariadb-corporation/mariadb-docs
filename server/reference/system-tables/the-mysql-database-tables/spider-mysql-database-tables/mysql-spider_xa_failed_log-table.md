---
description: >-
  This table logs details of failed XA transactions in the Spider storage
  engine, providing a record for troubleshooting distributed transaction errors.
---

# mysql.spider\_xa\_failed\_log Table

The `mysql.spider_xa_failed_log` table is installed by the [Spider storage engine](../../../../server-usage/storage-engines/spider/).

This table uses the [Aria](../../../../server-usage/storage-engines/aria/) storage engine.

It contains the following fields:

| Field                     | Type        | Null | Key | Default              | Description |
| ------------------------- | ----------- | ---- | --- | -------------------- | ----------- |
| format\_id                | int(11)     | NO   |     | 0                    |             |
| gtrid\_length             | int(11)     | NO   |     | 0                    |             |
| bqual\_length             | int(11)     | NO   |     | 0                    |             |
| data                      | binary(128) | NO   | MUL |                      |             |
| scheme                    | char(64)    | NO   |     |                      |             |
| host                      | char(64)    | NO   |     |                      |             |
| port                      | char(5)     | NO   |     |                      |             |
| socket                    | text        | NO   |     | NULL                 |             |
| username                  | char(64)    | NO   |     |                      |             |
| password                  | char(64)    | NO   |     |                      |             |
| ssl\_ca                   | text        | YES  |     | NULL                 |             |
| ssl\_capath               | text        | YES  |     | NULL                 |             |
| ssl\_cert                 | text        | YES  |     | NULL                 |             |
| ssl\_cipher               | char(64)    | YES  |     | NULL                 |             |
| ssl\_key                  | text        | YES  |     | NULL                 |             |
| ssl\_verify\_server\_cert | tinyint(4)  | NO   |     | 0                    |             |
| default\_file             | text        | YES  |     | NULL                 |             |
| default\_group            | char(64)    | YES  |     | NULL                 |             |
| dsn                       | char(64)    | YES  |     | NULL                 |             |
| filedsn                   | text        | YES  |     | NULL                 |             |
| driver                    | char(64)    | YES  |     | NULL                 |             |
| thread\_id                | int(11)     | YES  |     | NULL                 |             |
| status                    | char(8)     | NO   |     |                      |             |
| failed\_time              | timestamp   | NO   |     | current\_timestamp() |             |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
