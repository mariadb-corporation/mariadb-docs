---
description: >-
  InnoDB employs Row-Level Locking with Shared (S) and Exclusive (X) locks,
  along with Intention locks, to manage concurrent transaction access.
---

# InnoDB Lock Modes

Locks are acquired by a transaction to prevent concurrent transactions from modifying, or even reading, some rows or ranges of rows. This is done to make sure that concurrent write operations never collide.

[InnoDB](./) supports a number of lock modes.

## Shared and Exclusive Locks

The two standard row-level locks are _share locks_(S) and _exclusive locks_(X).

A shared lock is obtained to read a row, and allows other transactions to read the locked row, but not to write to the locked row. Other transactions may also acquire their own shared locks.

An exclusive lock is obtained to write to a row, and stops other transactions from locking the same row. It's specific behavior depends on the [isolation level](../../../reference/sql-statements/transactions/set-transaction.md); the default (REPEATABLE READ), allows other transactions to read from the exclusively locked row.

## Intention Locks

InnoDB also permits table locking, and to allow locking at both table and row level to co-exist gracefully, a series of locks called _intention locks_ exist.

An _intention shared lock_(IS) indicates that a transaction intends to set a shared lock.

An _intention exclusive lock_(IX) indicates that a transaction intends to set an exclusive lock.

Whether a lock is granted or not can be summarised as follows:

* An X lock is not granted if any other lock (X, S, IX, IS) is held.
* An S lock is not granted if an X or IX lock is held. It is granted if an S or IS lock is held.
* An IX lock is not granted if in X or S lock is held. It is granted if an IX or IS lock is held.
* An IS lock is not granted if an X lock is held. It is granted if an S, IX or IS lock is held.

## AUTO\_INCREMENT Locks

Locks are also required for auto-increments - see [AUTO\_INCREMENT handling in InnoDB](auto_increment-handling-in-innodb.md).

## Gap Locks

With the default [isolation level](../../../reference/sql-statements/transactions/set-transaction.md), `REPEATABLE READ`, and, until [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104), the default setting of the [innodb\_locks\_unsafe\_for\_binlog](innodb-system-variables.md#innodb_locks_unsafe_for_binlog) variable, a method called gap locking is used. When InnoDB sets a shared or exclusive lock on a record, it's actually on the index record. Records will have an internal InnoDB index even if they don't have a unique index defined. At the same time, a lock is held on the gap before the index record, so that another transaction cannot insert a new index record in the gap between the record and the preceding record.

The gap can be a single index value, multiple index values, or not exist at all depending on the contents of the index.

If a statement uses all the columns of a unique index to search for unique row, gap locking is not used.

Similar to the shared and exclusive intention locks described above, there can be a number of types of gap locks. These include the shared gap lock, exclusive gap lock, intention shared gap lock and intention exclusive gap lock.

Gap locks are disabled if the [innodb\_locks\_unsafe\_for\_binlog](innodb-system-variables.md#innodb_locks_unsafe_for_binlog) system variable is set (until [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/what-is-mariadb-104)), or the [isolation level](../../../reference/sql-statements/transactions/set-transaction.md) is set to `READ COMMITTED`.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
