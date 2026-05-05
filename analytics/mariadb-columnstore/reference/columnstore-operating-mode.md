---
description: >-
  MariaDB ColumnStore operating mode is set via infinidb_vtable_mode: 0 for
  row-by-row processing, 1 (default) for distributed only, or 2 for
  auto-switch by query compatibility.
---

# ColumnStore Operating Mode

ColumnStore has the ability to support full MariaDB query syntax through an operating mode. This operating mode may be set as a default for the instance or set at the session level. To set the operating mode at the session level, the following command is used. Once the session has ended, any subsequent session will return to the default for the instance.

```sql
SET infinidb_vtable_mode = n
```

where n is:

1. a generic, highly compatible row-by-row processing mode. Some `WHERE` clause components can be processed by ColumnStore, but joins are processed entirely by mysqld using a nested loop join mechanism.
2. (the default) query syntax is evaluated by ColumnStore for compatibility with distributed execution and incompatible queries are rejected. Queries executed in this mode take advantage of distributed execution and typically result in higher performance.
3. auto-switch mode: ColumnStore will attempt to process the query internally, if it cannot, it will automatically switch the query to run in row-by-row mode.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
