---
description: >-
  The Information Schema INNODB_BUFFER_PAGE_LRU table details pages in the
  buffer pool and their position in the LRU eviction list.
---

# Information Schema INNODB\_BUFFER\_PAGE\_LRU Table

The [Information Schema](../../) `INNODB_BUFFER_PAGE_LRU` table contains information about pages in the [buffer pool](../../../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md) and how they are ordered for eviction purposes.

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It has the following columns:

| Column               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| POOL\_ID             | Buffer Pool identifier. From [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/10.5.1) returns a value of 0, since multiple InnoDB buffer pool instances has been removed.                                                                                                                                                                                                                                                                               |
| LRU\_POSITION        | LRU (Least recently-used), for determining eviction order from the buffer pool.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| SPACE                | Tablespace identifier. Matches the SPACE value on the [INNODB\_SYS\_TABLES](information-schema-innodb_sys_tables-table.md) table.                                                                                                                                                                                                                                                                                                                                                                         |
| PAGE\_NUMBER         | Buffer pool page number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PAGE\_TYPE           | Page type; one of allocated (newly-allocated page), index (B-tree node), undo\_log (undo log page), inode (index node), ibuf\_free\_list (insert buffer free list), ibuf\_bitmap (insert buffer bitmap), system (system page), trx\_system (transaction system data), file\_space\_header (file space header), extent\_descriptor (extent descriptor page), blob (uncompressed blob page), compressed\_blob (first compressed blob page), compressed\_blob2 (subsequent compressed blob page) or unknown. |
| FLUSH\_TYPE          | Flush type. 0= FLUSH\_KEEP, 1 =FLUSH\_RELEASE, 2 = FLUSH\_IGNORE\_CHANGED, 3= FLUSH\_FORCE\_WRITE                                                                                                                                                                                                                                                                                                                                                                                                         |
| FIX\_COUNT           | Count of the threads using this block in the buffer pool. When it is zero, the block can be evicted from the buffer pool.                                                                                                                                                                                                                                                                                                                                                                                 |
| IS\_HASHED           | Whether or not a hash index has been built on this page.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| NEWEST\_MODIFICATION | Most recent modification's Log Sequence Number.                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| OLDEST\_MODIFICATION | Oldest modification's Log Sequence Number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ACCESS\_TIME         | Abstract number representing the time the page was first accessed.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| TABLE\_NAME          | Table that the page belongs to.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| INDEX\_NAME          | Index that the page belongs to, either a clustered index or a secondary index.                                                                                                                                                                                                                                                                                                                                                                                                                            |
| NUMBER\_RECORDS      | Number of records the page contains.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| DATA\_SIZE           | Size in bytes of all the records contained in the page.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| COMPRESSED\_SIZE     | Compressed size in bytes of the page, or NULL for pages that aren't compressed.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| PAGE\_STATE          | Page state; one of FILE\_PAGE (page from a file) or MEMORY (page from an in-memory object) for valid data, or one of NULL, READY\_FOR\_USE, NOT\_USED, REMOVE\_HASH.                                                                                                                                                                                                                                                                                                                                      |
| IO\_FIX              | Whether there is I/O pending for the page; one of IO\_NONE (no pending I/O), IO\_READ (read pending), IO\_WRITE (write pending).                                                                                                                                                                                                                                                                                                                                                                          |
| IS\_OLD              | Whether the page is old or not.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| FREE\_PAGE\_CLOCK    | Freed\_page\_clock counter, which tracks the number of blocks removed from the end of the LRU list, at the time the block was last placed at the head of the list.                                                                                                                                                                                                                                                                                                                                        |

The related [INFORMATION\_SCHEMA.INNODB\_BUFFER\_PAGE](information-schema-innodb_buffer_page-table.md) table contains the same information, but with a block id rather than LRU position.

## Example

```sql
DESC information_schema.innodb_buffer_page_lru;
+---------------------+---------------------+------+-----+---------+-------+
| Field               | Type                | Null | Key | Default | Extra |
+---------------------+---------------------+------+-----+---------+-------+
| POOL_ID             | bigint(21) unsigned | NO   |     | 0       |       |
| LRU_POSITION        | bigint(21) unsigned | NO   |     | 0       |       |
| SPACE               | bigint(21) unsigned | NO   |     | 0       |       |
| PAGE_NUMBER         | bigint(21) unsigned | NO   |     | 0       |       |
| PAGE_TYPE           | varchar(64)         | YES  |     | NULL    |       |
| FLUSH_TYPE          | bigint(21) unsigned | NO   |     | 0       |       |
| FIX_COUNT           | bigint(21) unsigned | NO   |     | 0       |       |
| IS_HASHED           | varchar(3)          | YES  |     | NULL    |       |
| NEWEST_MODIFICATION | bigint(21) unsigned | NO   |     | 0       |       |
| OLDEST_MODIFICATION | bigint(21) unsigned | NO   |     | 0       |       |
| ACCESS_TIME         | bigint(21) unsigned | NO   |     | 0       |       |
| TABLE_NAME          | varchar(1024)       | YES  |     | NULL    |       |
| INDEX_NAME          | varchar(1024)       | YES  |     | NULL    |       |
| NUMBER_RECORDS      | bigint(21) unsigned | NO   |     | 0       |       |
| DATA_SIZE           | bigint(21) unsigned | NO   |     | 0       |       |
| COMPRESSED_SIZE     | bigint(21) unsigned | NO   |     | 0       |       |
| COMPRESSED          | varchar(3)          | YES  |     | NULL    |       |
| IO_FIX              | varchar(64)         | YES  |     | NULL    |       |
| IS_OLD              | varchar(3)          | YES  |     | NULL    |       |
| FREE_PAGE_CLOCK     | bigint(21) unsigned | NO   |     | 0       |       |
+---------------------+---------------------+------+-----+---------+-------+
```

```sql
SELECT * FROM INFORMATION_SCHEMA.INNODB_BUFFER_PAGE_LRU\G
...
*************************** 6. row ***************************
            POOL_ID: 0
       LRU_POSITION: 5
              SPACE: 0
        PAGE_NUMBER: 11
          PAGE_TYPE: INDEX
         FLUSH_TYPE: 1
          FIX_COUNT: 0
          IS_HASHED: NO
NEWEST_MODIFICATION: 2046835
OLDEST_MODIFICATION: 0
        ACCESS_TIME: 2585566280
         TABLE_NAME: `SYS_INDEXES`
         INDEX_NAME: CLUST_IND
     NUMBER_RECORDS: 57
          DATA_SIZE: 4016
    COMPRESSED_SIZE: 0
         COMPRESSED: NO
             IO_FIX: IO_NONE
             IS_OLD: NO
    FREE_PAGE_CLOCK: 0
...
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
