---
description: >-
  Statement digests aggregate statistics for similar queries by removing
  specific data values, allowing you to identify performance patterns across
  statement types.
---

# Performance Schema Digests

The Performance Schema digest is a normalized form of a statement, with the specific data values removed. It allows statistics to be gathered for similar kinds of statements.

For example:

```sql
SELECT * FROM customer WHERE age < 20
SELECT * FROM customer WHERE age < 30
```

With the data values removed, both of these statements normalize to:

```sql
SELECT * FROM customer WHERE age < ?
```

which is the digest text. The digest text is used to compute a digest. For example:

```sql
DIGEST_TEXT: SELECT * FROM `performance_schema` . `users`
DIGEST: 0f70cec4015f2a346df4ac0e9475d9f1
```

By contrast, the following two statements would not have the same digest as, while the data values are the same, they call upon different tables.

```sql
SELECT * FROM customer1 WHERE age < 20
SELECT * FROM customer2 WHERE age < 20
```

The digest text is limited to 1024 bytes. Queries exceeding this limit are truncated with '...', meaning that long queries that would otherwise have different digests may share the same digest.

Digest information is used in a number of performance scheme tables. These include

* [events\_statements\_current](performance-schema-tables/performance-schema-events_statements_current-table.md)
* [events\_statements\_history](performance-schema-tables/performance-schema-events_statements_history-table.md)
* [events\_statements\_history\_long](performance-schema-tables/performance-schema-events_statements_history_long-table.md)
* [events\_statements\_summary\_by\_digest](performance-schema-tables/performance-schema-events_statements_summary_by_digest-table.md) (a summary table by schema and digest)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
