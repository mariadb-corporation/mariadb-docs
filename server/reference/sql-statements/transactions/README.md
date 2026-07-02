---
description: >-
  Learn about transactions in MariaDB Server. This section covers SQL statements
  for managing atomic operations (START TRANSACTION, COMMIT, ROLLBACK), ensuring
  data integrity and consistency.
---

# Transactions

{% columns %}
{% column %}
{% content-ref url="commit.md" %}
[commit.md](commit.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Commit the current transaction. This statement permanently saves all changes made during the current transaction to the database.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="lock-tables.md" %}
[lock-tables.md](lock-tables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete LOCK TABLES reference: READ/WRITE/WRITE CONCURRENT lock syntax, table aliases, WAIT n|NOWAIT timeouts, UNLOCK TABLES, and innodb_table_locks behavior.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="metadata-locking.md" %}
[metadata-locking.md](metadata-locking.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand how MariaDB manages concurrency. Metadata locks protect the structure of database objects from being modified while they are in use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="transactions-read-committed.md" %}
[transactions-read-committed.md](transactions-read-committed.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Set the transaction isolation level to READ COMMITTED. In this mode, each query within a transaction sees only data committed before the query began.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="transactions-read-uncommitted.md" %}
[transactions-read-uncommitted.md](transactions-read-uncommitted.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Set the transaction isolation level to READ UNCOMMITTED. This lowest isolation level allows dirty reads, where a transaction can see uncommitted changes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="transactions-repeatable-read.md" %}
[transactions-repeatable-read.md](transactions-repeatable-read.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Set the transaction isolation level to REPEATABLE READ. This default InnoDB level ensures consistent results for repeated reads within the same transaction.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="rollback.md" %}
[rollback.md](rollback.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Undo changes in the current transaction. This statement reverts the database to its state before the transaction started or to a specific savepoint.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="savepoint.md" %}
[savepoint.md](savepoint.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Create a named marker within a transaction. Savepoints allow you to roll back part of a transaction without canceling the entire operation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="transactions-serializable.md" %}
[transactions-serializable.md](transactions-serializable.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Set the transaction isolation level to SERIALIZABLE. This highest level ensures total isolation by converting plain SELECTs to locking reads.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sql-statements-that-cause-an-implicit-commit.md" %}
[sql-statements-that-cause-an-implicit-commit.md](sql-statements-that-cause-an-implicit-commit.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Identify statements that force a commit. Certain commands, like DDL statements, implicitly commit the current transaction before executing.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="start-transaction.md" %}
[start-transaction.md](start-transaction.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete START TRANSACTION reference: BEGIN/COMMIT/ROLLBACK syntax, WITH CONSISTENT SNAPSHOT option, READ ONLY/WRITE modes, AND [NO] CHAIN/RELEASE modifiers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="transaction-timeouts.md" %}
[transaction-timeouts.md](transaction-timeouts.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand how timeouts affect transactions. This section explains system variables that control wait times for locks and transaction duration.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="transactions-unlock-tables.md" %}
[transactions-unlock-tables.md](transactions-unlock-tables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Release explicit table locks. This statement releases all locks acquired by the current session with LOCK TABLES.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="wait-and-nowait.md" %}
[wait-and-nowait.md](wait-and-nowait.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Control lock wait behavior. These clauses allow statements to wait for a specific timeout or fail immediately if a lock cannot be acquired.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="xa-transactions.md" %}
[xa-transactions.md](xa-transactions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Manage distributed transactions. This section covers XA statements for coordinating two-phase commits across multiple resources.
{% endcolumn %}
{% endcolumns %}
