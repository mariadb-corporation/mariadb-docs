---
description: >-
  While technically a storage engine, PERFORMANCE_SCHEMA provides a way to
  inspect internal server execution details at a low level.
---

# PERFORMANCE\_SCHEMA

If you run [SHOW ENGINES](../../reference/sql-statements/administrative-sql-statements/show/show-engines.md), you'll see the following storage engine listed.

```sql
SHOW ENGINES\G
...
      Engine: PERFORMANCE_SCHEMA
     Support: YES
     Comment: Performance Schema
Transactions: NO
          XA: NO
  Savepoints: NO
...
```

The PERFORMANCE\_SCHEMA is not a regular storage engine for storing data, it's a mechanism for implementing the [Performance Schema](../../reference/system-tables/performance-schema/) feature.

The [SHOW ENGINE PERFORMANCE\_SCHEMA STATUS](../../reference/sql-statements/administrative-sql-statements/show/show-engine.md#show-engine-performance_schema-status) statement is also available, which shows how much memory is used by the tables and internal buffers.

See [Performance Schema](../../reference/system-tables/performance-schema/) for more details.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
