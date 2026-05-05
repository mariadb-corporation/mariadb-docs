---
description: >-
  The ColumnStore Execution Plan (CSEP) is the internal query-plan
  representation in MariaDB Enterprise ColumnStore, generated from SELECT_LEX
  and viewable through calSetTrace.
---

# Execution Plan (CSEP)

## Overview

The ColumnStore storage engine uses a ColumnStore Execution Plan (CSEP) to represent a query plan internally.

When the select handler receives the `SELECT_LEX` object, it transforms it into a CSEP as part of the query planning and optimization process. For additional information, see "[MariaDB Enterprise ColumnStore Query Evaluation](../../../architecture/mariadb-enterprise-columnstore-query-evaluation.md)."

## Viewing the CSEP

The CSEP for a given query can be viewed by performing the following:

1. Calling the `calSetTrace(1)` function:

```sql
SELECT calSetTrace(1);
```

2. Executing the query:

```sql
SELECT column1, column2
FROM columnstore_tab
WHERE column1 > '2020-04-01'
AND column1 < '2020-11-01';
```

3. Calling the `calGetTrace()` function:

```sql
SELECT calGetTrace();
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
