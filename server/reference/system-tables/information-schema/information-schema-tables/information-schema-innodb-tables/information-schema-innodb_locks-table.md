---
description: >-
  The INNODB_LOCKS table provides information about locks that a transaction has
  requested but not yet obtained, or locks that are blocking another
  transaction.
---

# Information Schema INNODB\_LOCKS Table

The [Information Schema](../../) `INNODB_LOCKS` table stores information about locks that InnoDB transactions have requested but not yet acquired, or that are blocking another transaction.

It has the following columns:

| Column        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| LOCK\_ID      | Lock ID number - the format is not fixed, so do not rely upon the number for information.                                                                                                                                                                                                                                                                                                                                                                       |
| LOCK\_TRX\_ID | Lock's transaction ID. Matches the [INNODB\_TRX.TRX\_ID](information-schema-innodb_trx-table.md) column.                                                                                                                                                                                                                                                                                                                                                        |
| LOCK\_MODE    | [Lock mode](../../../../../server-usage/storage-engines/innodb/innodb-lock-modes.md). One of S (shared), X (exclusive), IS (intention shared), IX (intention exclusive row lock), S\_GAP (shared gap lock), X\_GAP (exclusive gap lock), IS\_GAP (intention shared gap lock), IX\_GAP (intention exclusive gap lock) or AUTO\_INC ([auto-increment table level lock](../../../../../server-usage/storage-engines/innodb/auto_increment-handling-in-innodb.md)). |
| LOCK\_TYPE    | Whether the lock is RECORD (row level) or TABLE level.                                                                                                                                                                                                                                                                                                                                                                                                          |
| LOCK\_TABLE   | Name of the locked table,or table containing locked rows.                                                                                                                                                                                                                                                                                                                                                                                                       |
| LOCK\_INDEX   | Index name if a RECORD LOCK\_TYPE, or NULL if not.                                                                                                                                                                                                                                                                                                                                                                                                              |
| LOCK\_SPACE   | Tablespace ID if a RECORD LOCK\_TYPE, or NULL if not.                                                                                                                                                                                                                                                                                                                                                                                                           |
| LOCK\_PAGE    | Locked record page number if a RECORD LOCK\_TYPE, or NULL if not.                                                                                                                                                                                                                                                                                                                                                                                               |
| LOCK\_REC     | Locked record heap number if a RECORD LOCK\_TYPE, or NULL if not.                                                                                                                                                                                                                                                                                                                                                                                               |
| LOCK\_DATA    | Locked record primary key as an SQL string if a RECORD LOCK\_TYPE, or NULL if not. If no primary key exists, the internal InnoDB row\_id number is instead used. To avoid unnecessary IO, also NULL if the locked record page is not in the [buffer pool](../../../../../server-usage/storage-engines/innodb/innodb-buffer-pool.md)                                                                                                                             |

The table is often used in conjunction with the [INNODB\_LOCK\_WAITS](information-schema-innodb_lock_waits-table.md) and [INNODB\_TRX](information-schema-innodb_trx-table.md) tables to diagnose problematic locks and transactions

## Example

```sql
-- session 1
START TRANSACTION;
UPDATE t SET id = 15 WHERE id = 10;

-- session 2
DELETE FROM t WHERE id = 10;

-- session 1
USE information_schema;
SELECT l.*, t.*
    FROM information_schema.INNODB_LOCKS l
    JOIN information_schema.INNODB_TRX t
        ON l.lock_trx_id = t.trx_id
    WHERE trx_state = 'LOCK WAIT' \G
*************************** 1. row ***************************
                   lock_id: 840:40:3:2
               lock_trx_id: 840
                 lock_mode: X
                 lock_type: RECORD
                lock_table: `test`.`t`
                lock_index: PRIMARY
                lock_space: 40
                 lock_page: 3
                  lock_rec: 2
                 lock_data: 10
                    trx_id: 840
                 trx_state: LOCK WAIT
               trx_started: 2019-12-23 18:43:46
     trx_requested_lock_id: 840:40:3:2
          trx_wait_started: 2019-12-23 18:43:46
                trx_weight: 2
       trx_mysql_thread_id: 46
                 trx_query: DELETE FROM t WHERE id = 10
       trx_operation_state: starting index read
         trx_tables_in_use: 1
         trx_tables_locked: 1
          trx_lock_structs: 2
     trx_lock_memory_bytes: 1136
           trx_rows_locked: 1
         trx_rows_modified: 0
   trx_concurrency_tickets: 0
       trx_isolation_level: REPEATABLE READ
         trx_unique_checks: 1
    trx_foreign_key_checks: 1
trx_last_foreign_key_error: NULL
          trx_is_read_only: 0
trx_autocommit_non_locking: 0
```

.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
