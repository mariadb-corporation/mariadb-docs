---
description: >-
  The Information Schema INNODB_LOCK_WAITS table maps blocked transactions to
  the transactions that are blocking them, aiding in deadlock analysis.
---

# Information Schema INNODB\_LOCK\_WAITS Table

The [Information Schema](../../) `INNODB_LOCK_WAITS` table contains information about blocked InnoDB transactions. The `PROCESS` [privilege](../../../../sql-statements/account-management-sql-statements/grant.md) is required to view the table.

It contains the following columns:

| Column              | Description                                                                                                                                           |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| REQUESTING\_TRX\_ID | Requesting transaction ID from the [INNODB\_TRX](information-schema-innodb_trx-table.md) table.                                                       |
| REQUESTED\_LOCK\_ID | Lock ID from the [INNODB.LOCKS](information-schema-innodb_locks-table.md) table for the waiting transaction.                                          |
| BLOCKING\_TRX\_ID   | Blocking transaction ID from the [INNODB\_TRX](information-schema-innodb_trx-table.md) table.                                                         |
| BLOCKING\_LOCK\_ID  | Lock ID from the [INNODB.LOCKS](information-schema-innodb_locks-table.md) table of a lock held by a transaction that is blocking another transaction. |

The table is often used in conjunction with the [INNODB\_LOCKS](information-schema-innodb_locks-table.md) and [INNODB\_TRX](information-schema-innodb_trx-table.md) tables to diagnose problematic locks and transactions.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
