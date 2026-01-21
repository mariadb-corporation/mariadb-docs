---
description: >-
  The Information Schema INNODB_BUFFER_POOL_PAGES table provides a record for
  each page in the buffer pool, specific to the XtraDB engine.
---

# Information Schema INNODB\_BUFFER\_POOL\_PAGES Table

The [Information Schema](../../) `INNODB_BUFFER_POOL_PAGES` table is a Percona enhancement, and is only available for XtraDB, not InnoDB (see [XtraDB and InnoDB](../../../../../server-usage/storage-engines/innodb/)). It contains a record for each page in the [buffer pool](../../../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md).

It has the following columns:

| Column        | Description                                                                                                                                        |
| ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| PAGE\_TYPE    | Type of page; one of index, undo\_log, inode, ibuf\_free\_list, allocated, bitmap, sys, trx\_sys, fsp\_hdr, xdes, blob, zblob, zblob2 and unknown. |
| SPACE\_ID     | Tablespace ID.                                                                                                                                     |
| PAGE\_NO      | Page offset within tablespace.                                                                                                                     |
| LRU\_POSITION | Page position in the LRU (least-recently-used) list.                                                                                               |
| FIX\_COUNT    | Page reference count, incremented each time the page is accessed. 0 if the page is not currently being accessed.                                   |
| FLUSH\_TYPE   | Flush type of the most recent flush.0 (LRU), 2 (flush\_list)                                                                                       |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
