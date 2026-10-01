---
description: >-
  Describes the SPIDER_WRAPPER_PROTOCOLS table, which lists the available
  foreign data wrappers (like mysql) that Spider can use to connect to remote
  servers.
---

# Information Schema SPIDER\_WRAPPER\_PROTOCOLS Table

The [Information Schema](../../../reference/system-tables/information-schema/) `SPIDER_WRAPPER_PROTOCOLS` table is installed along with the [Spider](./) storage engine.

It contains the following columns:

| Column               | Type        | Description |
| -------------------- | ----------- | ----------- |
| WRAPPER\_NAME        | varchar(64) |             |
| WRAPPER\_VERSION     | varchar(20) |             |
| WRAPPER\_DESCRIPTION | longtext    |             |
| WRAPPER\_MATURITY    | varchar(12) |             |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
