---
description: >-
  The INNODB_BUFFER_POOL_PAGES_INDEX table provides information about index
  pages in the buffer pool, specific to the XtraDB engine.
---

# Information Schema INNODB\_BUFFER\_POOL\_PAGES\_INDEX Table

The [Information Schema](../../) `INNODB_BUFFER_POOL_PAGES` table is a Percona enhancement, and is only available for XtraDB, not InnoDB (see [XtraDB and InnoDB](../../../../../server-usage/storage-engines/innodb/)). It contains information about [buffer pool](../../../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md) index pages.

It has the following columns:

| Column        | Description                                                                                                      |
| ------------- | ---------------------------------------------------------------------------------------------------------------- |
| INDEX\_ID     | Index name                                                                                                       |
| SPACE\_ID     | Tablespace ID                                                                                                    |
| PAGE\_NO      | Page offset within tablespace.                                                                                   |
| N\_RECS       | Number of user records on the page.                                                                              |
| DATA\_SIZE    | Total data size in bytes of records in the page.                                                                 |
| HASHED        | 1 if the block is in the adaptive hash index, 0 if not.                                                          |
| ACCESS\_TIME  | Page's last access time.                                                                                         |
| MODIFIED      | 1 if the page has been modified since being loaded, 0 if not.                                                    |
| DIRTY         | 1 if the page has been modified since it was last flushed, 0 if not                                              |
| OLD           | 1 if the page in the in the old blocks of the LRU (least-recently-used) list, 0 if not.                          |
| LRU\_POSITION | Position in the LRU (least-recently-used) list.                                                                  |
| FIX\_COUNT    | Page reference count, incremented each time the page is accessed. 0 if the page is not currently being accessed. |
| FLUSH\_TYPE   | Flush type of the most recent flush.0 (LRU), 2 (flush\_list)                                                     |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
