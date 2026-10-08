---
description: >-
  These tables provide status information on compression operations for
  XtraDB/InnoDB tables, grouped by individual indexes.
---

# Information Schema INNODB\_CMP\_PER\_INDEX and INNODB\_CMP\_PER\_INDEX\_RESET Tables

The `INNODB_CMP_PER_INDEX` and `INNODB_CMP_PER_INDEX_RESET` tables contain status information on compression operations related to [compressed XtraDB/InnoDB tables](../../../../../server-usage/storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview.md), grouped by individual indexes. These tables are only populated if the [innodb\_cmp\_per\_index\_enabled](../../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_cmp_per_index_enabled) system variable is set to `ON`.

The [PROCESS](../../../../sql-statements/account-management-sql-statements/grant.md#global-privileges) privilege is required to query this table.

These tables contains the following columns:

| Column Name       | Description                                                                                                                                                                                                                                                   |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DATABASE\_NAME    | Database containing the index.                                                                                                                                                                                                                                |
| TABLE\_NAME       | Table containing the index.                                                                                                                                                                                                                                   |
| INDEX\_NAME       | Other values are totals which refer to this index's compression.                                                                                                                                                                                              |
| COMPRESS\_OPS     | How many times a page of INDEX\_NAME has been compressed. This happens when a new page is created because the compression log runs out of space. This value includes both successful operations and compression failures.                                     |
| COMPRESS\_OPS\_OK | How many times a page of INDEX\_NAME has been successfully compressed. This value should be as close as possible to COMPRESS\_OPS. If it is notably lower, either avoid compressing some tables, or increase the KEY\_BLOCK\_SIZE for some compressed tables. |
| COMPRESS\_TIME    | Time (in seconds) spent to compress pages of the size PAGE\_SIZE. This value includes time spent in compression failures.                                                                                                                                     |
| UNCOMPRESS\_OPS   | How many times a page of INDEX\_NAME has been uncompressed. This happens when an uncompressed version of a page is created in the buffer pool, or when a compression failure occurs.                                                                          |
| UNCOMPRESS\_TIME  | Time (in seconds) spent to uncompress pages of INDEX\_NAME.                                                                                                                                                                                                   |

These tables can be used to measure the effectiveness of XtraDB/InnoDB compression, per table or per index. The values in these tables show which tables perform better with index compression, and which tables cause too many _compression failures_ or perform too many compression/uncompression operations. When compression performs badly for a table, this might mean that you should change its `KEY_BLOCK_SIZE`, or that the table should not be compressed.

`INNODB_CMP_PER_INDEX` and `INNODB_CMP_PER_INDEX_RESET` have the same columns and always contain the same values, but when `INNODB_CMP_PER_INDEX_RESET` is queried, both the tables are cleared. `INNODB_CMP_PER_INDEX_RESET` can be used, for example, if a script periodically logs the performances of compression in the last period of time. `INNODB_CMP_PER_INDEX` can be used to see the cumulated statistics.

## See Also

Other tables that can be used to monitor XtraDB/InnoDB compressed tables:

* [INNODB\_CMP and INNODB\_CMP\_RESET](information-schema-innodb_cmp-and-innodb_cmp_reset-tables.md)
* [INNODB\_CMPMEM and INNODB\_CMPMEM\_RESET](information-schema-innodb_cmpmem-and-innodb_cmpmem_reset-tables.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
