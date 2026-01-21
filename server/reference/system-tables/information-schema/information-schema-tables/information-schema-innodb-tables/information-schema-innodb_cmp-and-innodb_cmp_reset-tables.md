---
description: >-
  These tables contain status information on compression operations for
  compressed XtraDB/InnoDB tables, detailing compress and uncompress ops.
---

# Information Schema INNODB\_CMP and INNODB\_CMP\_RESET Tables

The `INNODB_CMP` and `INNODB_CMP_RESET` tables contain status information on compression operations related to [compressed XtraDB/InnoDB tables](../../../../../server-usage/storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview.md).

The [PROCESS](../../../../sql-statements/account-management-sql-statements/grant.md#process) privilege is required to query this table.

These tables contain the following columns:

| Column Name       | Description                                                                                                                                                                                                                                                           |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PAGE\_SIZE        | Compressed page size, in bytes. This value is unique in the table; other values are totals which refer to pages of this size.                                                                                                                                         |
| COMPRESS\_OPS     | How many times a page of the size PAGE\_SIZE has been compressed. This happens when a new page is created because the compression log runs out of space. This value includes both successful operations and compression failures.                                     |
| COMPRESS\_OPS\_OK | How many times a page of the size PAGE\_SIZE has been successfully compressed. This value should be as close as possible to COMPRESS\_OPS. If it is notably lower, either avoid compressing some tables, or increase the KEY\_BLOCK\_SIZE for some compressed tables. |
| COMPRESS\_TIME    | Time (in seconds) spent to compress pages of the size PAGE\_SIZE. This value includes time spent in compression failures.                                                                                                                                             |
| UNCOMPRESS\_OPS   | How many times a page of the size PAGE\_SIZE has been uncompressed. This happens when an uncompressed version of a page is created in the buffer pool, or when a compression failure occurs.                                                                          |
| UNCOMPRESS\_TIME  | Time (in seconds) spent to uncompress pages of the size PAGE\_SIZE.                                                                                                                                                                                                   |

These tables can be used to measure the effectiveness of XtraDB/InnoDB table compression. When you have to decide a value for `KEY_BLOCK_SIZE`, you can create more than one version of the table (one for each candidate value) and run a realistic workload on them. Then, these tables can be used to see how the operations performed with different page sizes.

`INNODB_CMP` and `INNODB_CMP_RESET` have the same columns and always contain the same values, but when `INNODB_CMP_RESET` is queried, both the tables are cleared. `INNODB_CMP_RESET` can be used, for example, if a script periodically logs the performances of compression in the last period of time. `INNODB_CMP` can be used to see the cumulated statistics.

## Examples

```sql
SELECT * FROM information_schema.INNODB_CMP\G
**************************** 1. row *****************************
      page_size: 1024
   compress_ops: 0
compress_ops_ok: 0
  compress_time: 0
 uncompress_ops: 0
uncompress_time: 0
...
```

## See Also

Other tables that can be used to monitor XtraDB/InnoDB compressed tables:

* [INNODB\_CMP\_PER\_INDEX and INNODB\_CMP\_PER\_INDEX\_RESET](information-schema-innodb-tables-information-schema-innodb_cmp_per_index-an.md)
* [INNODB\_CMPMEM and INNODB\_CMPMEM\_RESET](information-schema-innodb_cmpmem-and-innodb_cmpmem_reset-tables.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
