---
description: >-
  View and clear lingering table locks in MariaDB ColumnStore using
  viewtablelock and cleartablelock, useful when a failed DDL or bulk load leaves
  a table locked.
---

# View and Clear Table Locks

MariaDB ColumnStore acquires table locks for some operations, and it provides utilities to view and clear those locks.

MariaDB ColumnStore acquires table locks for some operations, such as:

* DDL statements
* DML statements
* Bulk data loads

If an operation fails, the table lock does not always get released. If you try to access the table, you can see errors like the following:

```
ERROR 1815 (HY000): Internal error: CAL0009: Drop table failed due to IDB-2009: Unable to perform the drop table operation because cpimport with PID 16301 is currently holding the table lock for session -1.
```

To solve this problem, MariaDB Enterprise ColumnStore provides two utilities to view and clear the table locks:

* `cleartablelock`
* `viewallxml`
* `viewtablelock`

## Viewing Table Locks

The `viewtablelock` utility shows table locks currently held by MariaDB Enterprise ColumnStore:

To view all table locks:

```bash
viewtablelock
 There is 1 table lock

  Table                     LockID  Process   PID    Session   Txn  CreationTime               State    DBRoots
  hq_sales.invoices         1       cpimport  16301  BulkLoad  n/a  Wed April 7 14:20:42 2021  LOADING  1
```

To view table locks for a specific table, specify the database and table:

```bash
viewtablelock hq_sales invoices
 There is 1 table lock

  Table                     LockID  Process   PID    Session   Txn  CreationTime               State    DBRoots
  hq_sales.invoices         1       cpimport  16301  BulkLoad  n/a  Wed April 7 14:20:42 2021  LOADING  1
```

## Identifying Failed Transactions

Sometimes, a problem with a rollback transaction can result in the DBRM setting the system to read-only and failing to release the table lock. To identify if there is a stuck or failed rollback of a transaction, you can utilize the `viewallxml` command. This utility helps read the active transaction XML files and pinpoints orphaned or hanging transactions that might be preventing standard lock clearance.

## Clearing Table Locks

The `cleartablelock` utility clears table locks currently held by MariaDB Enterprise ColumnStore.

To clear a table lock, specify the lock ID shown by the `viewtablelock` utility:

```
cleartablelock 1
```

### Forced Releases for Lingering Locks

In certain situations, using the standard `cleartablelock <id>` command does not unlock a table lock. You may encounter an error indicating the lock is not found or still in use:

```
Rollback error: Unable to grab lock; Lock not found or still in use.
Table lock 54303 for table edf_colstore.pl_cs_tracking_summary_t is not cleared.
```

If a table lock remains stuck, you can utilize the `-l` flag to forcefully release it.

* Note: This is an undocumented and experimental flag.
* To force clear the lock, execute: `cleartablelock -l <id>`.

```bash
root@vm-uks-edf-maria:/var/log/mariadb/columnstore# cleartablelock -l 54303
Clearing table lock 54303 for table edf_colstore.pl_cs_tracking_summary_t

Table lock 54303 for table edf_colstore.pl_cs_tracking_summary_t is cleared.
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
