---
description: >-
  View and clear lingering table locks in MariaDB Enterprise ColumnStore using
  viewtablelock and cleartablelock, useful when a failed DDL or bulk load
  leaves a table locked.
---

# View/Clear Table Locks

MariaDB Enterprise ColumnStore acquires table locks for some operations, and it provides utilities to view and clear those locks.

MariaDB Enterprise ColumnStore acquires table locks for some operations, such as:

* DDL statements
* DML statements
* Bulk data loads

If an operation fails, the table lock does not always get released. If you try to access the table, you can see errors like the following:

```
ERROR 1815 (HY000): Internal error: CAL0009: Drop table failed due to IDB-2009: Unable to perform the drop table operation because cpimport with PID 16301 is currently holding the table lock for session -1.
```

To solve this problem, MariaDB Enterprise ColumnStore provides two utilities to view and clear the table locks:

* `cleartablelock`
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

## Clearing Table Locks

The `cleartablelock` utility clears table locks currently held by MariaDB Enterprise ColumnStore.

To clear a table lock, specify the lock ID shown by the `viewtablelock` utility:

```
cleartablelock 1
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
