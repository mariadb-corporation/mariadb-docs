---
description: >-
  The XTRADB_INTERNAL_HASH_TABLES table provides memory usage statistics for
  internal hash tables used by the XtraDB/InnoDB storage engine.
---

# Information Schema XTRADB\_INTERNAL\_HASH\_TABLES Table

The [Information Schema](../../) `XTRADB_INTERNAL_HASH_TABLES` table contains InnoDB/XtraDB hash table memory usage information.

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It has the following columns:

| Column                      | Description     |
| --------------------------- | --------------- |
| INTERNAL\_HASH\_TABLE\_NAME | Hash table name |
| TOTAL\_MEMORY               | Total memory    |
| CONSTANT\_MEMORY            | Constant memory |
| VARIABLE\_MEMORY            | Variable memory |

## Example

```
SELECT * FROM information_schema.XTRADB_INTERNAL_HASH_TABLES;
+--------------------------------+--------------+-----------------+-----------------+
| INTERNAL_HASH_TABLE_NAME       | TOTAL_MEMORY | CONSTANT_MEMORY | VARIABLE_MEMORY |
+--------------------------------+--------------+-----------------+-----------------+
| Adaptive hash index            |      2217568 |         2213368 |            4200 |
| Page hash (buffer pool 0 only) |       139112 |          139112 |               0 |
| Dictionary Cache               |       613423 |          554768 |           58655 |
| File system                    |       816368 |          812272 |            4096 |
| Lock System                    |       332872 |          332872 |               0 |
| Recovery System                |            0 |               0 |               0 |
+--------------------------------+--------------+-----------------+-----------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
