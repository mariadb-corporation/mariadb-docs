---
description: >-
  The mysql.spider_table_crd table stores cardinality statistics for Spider
  tables, which the optimizer uses to create efficient query plans.
---

# mysql.spider\_table\_crd Table

The `mysql.spider_table_crd` table is installed by the [Spider storage engine](../../../../server-usage/storage-engines/spider/).

This table uses the [Aria](../../../../server-usage/storage-engines/aria/) storage engine.

It contains the following fields:

| Field       | Type             | Null | Key | Default | Description |
| ----------- | ---------------- | ---- | --- | ------- | ----------- |
| db\_name    | char(64)         | NO   | PRI |         |             |
| table\_name | char(199)        | NO   | PRI |         |             |
| key\_seq    | int(10) unsigned | NO   | PRI | 0       |             |
| cardinality | bigint(20)       | NO   |     | 0       |             |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
