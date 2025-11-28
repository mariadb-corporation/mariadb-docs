---
description: >-
  These tables provide status statistics on compressed pages within the buffer
  pool, useful for analyzing compression efficiency.
---

# Information Schema INNODB\_CMPMEM and INNODB\_CMPMEM\_RESET Tables

The `INNODB_CMPMEM` and `INNODB_CMPMEM_RESET` tables contain status information on compressed pages in the [buffer pool](../../../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md) (see InnoDB [COMPRESSED](../../../../../server-usage/storage-engines/innodb/innodb-row-formats/innodb-row-formats-overview.md) format).

The [PROCESS](../../../../sql-statements/account-management-sql-statements/grant.md#process) privilege is required to query this table.

These tables contain the following columns:

| Column Name            | Description                                                                                                                                                                                                                                                    |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| PAGE\_SIZE             | Compressed page size, in bytes. This value is unique in the table; other values are totals which refer to pages of this size.                                                                                                                                  |
| BUFFER\_POOL\_INSTANCE | Buffer Pool identifier. From [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1051-release-notes) returns a value of 0, since multiple InnoDB buffer pool instances has been removed. |
| PAGES\_USED            | Number of pages of the size PAGE\_SIZE which are currently in the buffer pool.                                                                                                                                                                                 |
| PAGES\_FREE            | Number of pages of the size PAGE\_SIZE which are currently free, and thus are available for allocation. This value represents the buffer pool's fragmentation. A totally unfragmented buffer pool has at most 1 free page.                                     |
| RELOCATION\_OPS        | How many times a page of the size PAGE\_SIZE has been relocated. This happens when data exceeds a page (because a row must be copied into a new page) and when two pages are merged (because their data shrunk and can now be contained in one page).          |
| RELOCATION\_TIME       | Time (in seconds) spent in relocation operations for pages of the size PAGE\_SIZE. This column is reset when the INNODB\_CMPMEM\_RESET table is queried.                                                                                                       |

These tables can be used to measure the effectiveness of InnoDB table compression. When you have to decide a value for `KEY_BLOCK_SIZE`, you can create more than one version of the table (one for each candidate value) and run a realistic workload on them. Then, these tables can be used to see how the operations performed with different page sizes.

`INNODB_CMPMEM` and `INNODB_CMPMEM_RESET` have the same columns and always contain the same values, but when `INNODB_CMPMEM_RESET` is queried, the `RELOCATION_TIME` column from both the tables are cleared. `INNODB_CMPMEM_RESET` can be used, for example, if a script periodically logs the performances of compression in the last period of time. `INNODB_CMPMEM` can be used to see the cumulated statistics.

## Example

```sql
SELECT * FROM information_schema.INNODB_CMPMEM\G
********************** 1. row **********************
            page_size: 1024
 buffer_pool_instance: 0
           pages_used: 0
           pages_free: 0
      reloacation_ops: 0
      relocation_time: 0
```

## See Also

Other tables that can be used to monitor InnoDB compressed tables:

* [INNODB\_CMP and INNODB\_CMP\_RESET](information-schema-innodb_cmp-and-innodb_cmp_reset-tables.md)
* [INNODB\_CMP\_PER\_INDEX and INNODB\_CMP\_PER\_INDEX\_RESET](information-schema-innodb-tables-information-schema-innodb_cmp_per_index-an.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
