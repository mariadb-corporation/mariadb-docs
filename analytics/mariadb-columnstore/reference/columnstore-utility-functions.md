---
description: >-
  MariaDB ColumnStore utility functions report system status: mcsSystemReady()
  indicates whether queries are accepted, and mcsSystemReadOnly() reports
  read-only or suspended state.
---

# ColumnStore Utility Functions

MariaDB ColumnStore utility functions are a set of simple functions that return useful information about the system, such as whether it is ready for queries.

| Function            | Description                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| mcsSystemReady()    | Returns 1 if the system can accept queries, 0 if it's not ready yet.                                                                                                                                                                                                                                                                                                                 |
| mcsSystemReadOnly() | <p>Returns 1 if ColumnStore is in a write-suspended mode. That is, a user executed the <code>SuspendDatabaseWrites</code>. <br>It returns 2 if in a read-only state. ColumnStore puts itself into a read-only state if it detects a logic error that may have corrupted data. Generally, it means a <code>ROLLBACK</code> operation failed. Returns 0 if the system is writable.</p> |

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
