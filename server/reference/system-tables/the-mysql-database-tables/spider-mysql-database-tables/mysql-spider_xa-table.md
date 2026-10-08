---
description: >-
  The mysql.spider_xa table tracks the status of XA transactions involving
  Spider tables, ensuring atomicity across distributed nodes.
---

# mysql.spider\_xa Table

The `mysql.spider_xa` table is installed by the [Spider storage engine](../../../../server-usage/storage-engines/spider/).

This table uses the [Aria](../../../../server-usage/storage-engines/aria/) storage engine.

It contains the following fields:

| Field         | Type        | Null | Key | Default | Description |
| ------------- | ----------- | ---- | --- | ------- | ----------- |
| format\_id    | int(11)     | NO   | PRI | 0       |             |
| gtrid\_length | int(11)     | NO   | PRI | 0       |             |
| bqual\_length | int(11)     | NO   |     | 0       |             |
| data          | binary(128) | NO   | PRI |         |             |
| status        | char(8)     | NO   | MUL |         |             |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
