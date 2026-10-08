---
description: >-
  This table logs failures when attempting to establish connections to remote
  Spider links, helping to diagnose network or configuration issues.
---

# mysql.spider\_link\_failed\_log Table

The `mysql.spider_link_failed_log` table is installed by the [Spider storage engine](../../../../server-usage/storage-engines/spider/).

This table uses the [Aria](../../../../server-usage/storage-engines/aria/) storage engine.

It contains the following fields:

| Field        | Type      | Null | Key | Default              | Description |
| ------------ | --------- | ---- | --- | -------------------- | ----------- |
| db\_name     | char(64)  | NO   |     |                      |             |
| table\_name  | char(199) | NO   |     |                      |             |
| link\_id     | char(64)  | NO   |     |                      |             |
| failed\_time | timestamp | NO   |     | current\_timestamp() |             |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
