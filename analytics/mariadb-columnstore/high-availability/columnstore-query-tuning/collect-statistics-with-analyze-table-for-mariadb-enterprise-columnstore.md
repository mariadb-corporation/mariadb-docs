---
description: >-
  Optimizer statistics collected with ANALYZE TABLE in MariaDB Enterprise
  ColumnStore 6 enable circular inner joins and help ExeMgr choose better join
  orders for analytical queries.
---

# Collecting Statistics with ANALYZE TABLE

## Overview

In MariaDB Enterprise ColumnStore 6, the [ExeMgr process](../../architecture/mariadb-enterprise-columnstore-query-evaluation.md#exemgr-processfacility) uses optimizer statistics in its query planning process.

ColumnStore uses the optimizer statistics to add support for queries that contain circular inner joins.

In Enterprise ColumnStore 5 and before, ColumnStore would raise the following error when a query containing a circular inner join was executed:

```sql
ERROR 1815 (HY000): Internal error: IDB-1003: Circular joins are not supported.
```

The optimizer statistics store each column's NDV (Number of Distinct Values), which can help the ExeMgr process choose the optimal join order for queries with circular joins. When Enterprise ColumnStore executes a query with a circular join, the query's execution can take longer if ColumnStore chooses a sub-optimal join order. When you collect optimizer statistics for your ColumnStore tables, the ExeMgr process is less likely to choose a sub-optimal join order.

Enterprise ColumnStore's optimizer statistics can be collected for ColumnStore tables by executing [ANALYZE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/analyze-table):

```sql
[[analyze-table|ANALYZE TABLE]] columnstore_tab;
```

Enterprise ColumnStore's optimizer statistics are not updated automatically. To update the optimizer statistics for a ColumnStore table, [ANALYZE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/analyze-table) must be re-executed.

Enterprise ColumnStore does not implement an interface to show optimizer statistics.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
