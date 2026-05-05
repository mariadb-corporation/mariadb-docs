---
description: >-
  Reference for MariaDB ColumnStore system databases: calpontsys (table
  metadata), infinidb_querystats (query performance), and columnstore_info
  (usage-information stored procedures).
---

# ColumnStore System Databases

When using ColumnStore, MariaDB Server creates a series of system databases used for operational purposes.

| Database             | Description                                                                                                                                                                                                               |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| calpontsys           | Database maintains table metadata about ColumnStore tables.                                                                                                                                                               |
| infinidb\_querystats | Database maintains information about query performance. For more information, see [Query Analysis](../high-availability/analyzing-queries-in-columnstore.md).                                                             |
| columnstore\_info    | The database for stored procedures is used to retrieve information about ColumnStore usage. For more information, see the [ColumnStore Information Schema](../reference/columnstore-information-schema-tables.md) tables. |

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
