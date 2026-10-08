---
description: >-
  The mysql.spider_xa_member table lists the member nodes participating in a
  distributed XA transaction managed by the Spider engine.
---

# mysql.spider\_xa\_member Table

The `mysql.spider_xa_member` table is installed by the [Spider storage engine](../../../../server-usage/storage-engines/spider/).

This table uses the [Aria](../../../../server-usage/storage-engines/aria/) storage engine.

It contains the following fields:

| Field                     | Type        | Null | Key | Default | Description |
| ------------------------- | ----------- | ---- | --- | ------- | ----------- |
| format\_id                | int(11)     | NO   |     | 0       |             |
| gtrid\_length             | int(11)     | NO   |     | 0       |             |
| bqual\_length             | int(11)     | NO   |     | 0       |             |
| data                      | binary(128) | NO   | MUL |         |             |
| scheme                    | char(64)    | NO   |     |         |             |
| host                      | char(64)    | NO   |     |         |             |
| port                      | char(5)     | NO   |     |         |             |
| socket                    | text        | NO   |     | NULL    |             |
| username                  | char(64)    | NO   |     |         |             |
| password                  | char(64)    | NO   |     |         |             |
| ssl\_ca                   | text        | YES  |     | NULL    |             |
| ssl\_capath               | text        | YES  |     | NULL    |             |
| ssl\_cert                 | text        | YES  |     | NULL    |             |
| ssl\_cipher               | char(64)    | YES  |     | NULL    |             |
| ssl\_key                  | text        | YES  |     | NULL    |             |
| ssl\_verify\_server\_cert | tinyint(4)  | NO   |     | 0       |             |
| default\_file             | text        | YES  |     | NULL    |             |
| default\_group            | char(64)    | YES  |     | NULL    |             |
| dsn                       | char(64)    | YES  |     | NULL    |             |
| filedsn                   | text        | YES  |     | NULL    |             |
| driver                    | char(64)    | YES  |     | NULL    |             |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
