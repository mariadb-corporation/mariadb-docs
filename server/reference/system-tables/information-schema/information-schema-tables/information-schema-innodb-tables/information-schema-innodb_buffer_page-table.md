---
description: >-
  The Information Schema INNODB_BUFFER_PAGE table contains detailed information
  about each page currently in the InnoDB buffer pool.
---

# Information Schema INNODB\_BUFFER\_PAGE Table

The [Information Schema](../../) `INNODB_BUFFER_PAGE` table contains information about pages in the [buffer pool](../../../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md).

Querying this table can have a noticeable performance impact on a production server.

The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It has the following columns:

| Column               | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| POOL\_ID             | Buffer Pool identifier. From [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1051-release-notes) returns a value of 0, since multiple InnoDB buffer pool instances has been removed.                                                                                                                                                                                                                                            |
| BLOCK\_ID            | Buffer Pool Block identifier.                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| SPACE                | Tablespace identifier. Matches the SPACE value in the [INNODB\_SYS\_TABLES](information-schema-innodb_sys_tables-table.md) table.                                                                                                                                                                                                                                                                                                                                                                         |
| PAGE\_NUMBER         | Buffer pool page number.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| PAGE\_TYPE           | Page type; one of allocated (newly-allocated page), index (B-tree node), undo\_log (undo log page), inode (index node), ibuf\_free\_list (insert buffer free list), ibuf\_bitmap (insert buffer bitmap), system (system page), trx\_system (transaction system data), file\_space\_header (file space header), extent\_descriptor (extent descriptor page), blob (uncompressed blob page), compressed\_blob (first compressed blob page), compressed\_blob2 (subsequent compressed blob page) or unknown. |
| FLUSH\_TYPE          | Flush type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
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
| FREE\_PAGE\_CLOCK    | Freed\_page\_clock counter, which tracks the number of blocks removed from the end of the least recently used (LRU) list, at the time the block was last placed at the head of the list.                                                                                                                                                                                                                                                                                                                  |

The related [INFORMATION\_SCHEMA.INNODB\_BUFFER\_PAGE\_LRU](information-schema-innodb_buffer_page_lru-table.md) table contains the same information, but with an LRU (least recently used) position rather than block id.

## Examples

```sql
DESC information_schema.innodb_buffer_page;
+---------------------+---------------------+------+-----+---------+-------+
| Field               | Type                | Null | Key | Default | Extra |
+---------------------+---------------------+------+-----+---------+-------+
| POOL_ID             | bigint(21) unsigned | NO   |     | 0       |       |
| BLOCK_ID            | bigint(21) unsigned | NO   |     | 0       |       |
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
| PAGE_STATE          | varchar(64)         | YES  |     | NULL    |       |
| IO_FIX              | varchar(64)         | YES  |     | NULL    |       |
| IS_OLD              | varchar(3)          | YES  |     | NULL    |       |
| FREE_PAGE_CLOCK     | bigint(21) unsigned | NO   |     | 0       |       |
+---------------------+---------------------+------+-----+---------+-------+
```

```sql
SELECT * FROM INFORMATION_SCHEMA.INNODB_BUFFER_PAGE\G
...
*************************** 6. row ***************************
            POOL_ID: 0
           BLOCK_ID: 5
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
         PAGE_STATE: FILE_PAGE
             IO_FIX: IO_NONE
             IS_OLD: NO
    FREE_PAGE_CLOCK: 0
...
```

## See Also

* [InnoDB Buffer Pool](../../../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
