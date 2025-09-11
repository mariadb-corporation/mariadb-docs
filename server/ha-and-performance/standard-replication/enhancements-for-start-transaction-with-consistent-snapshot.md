---
description: >-
  Explore enhancements for START TRANSACTION WITH CONSISTENT SNAPSHOT. This
  section details how these improvements aid in achieving consistent backups and
  replication in highly active environments.
---

# START TRANSACTION ... WITH CONSISTENT SNAPSHOT

The `START TRANSACTION WITH CONSISTENT SNAPSHOT` statement begins a new transaction and, for the InnoDB storage engine, immediately establishes a consistent read view of the database.

This differs from a standard `START TRANSACTION` or `BEGIN` statement, which creates its read view _lazily_ only when the first read operation is performed. Using `WITH CONSISTENT SNAPSHOT` is essential for transactions where the snapshot's timing must be precisely aligned with the start of the transaction itself, not a later read query.

## Syntax

`START TRANSACTION` and its alias `BEGIN` can be modified with one or more characteristics.

```sql
START TRANSACTION [transaction_characteristic [, transaction_characteristic] ...]

transaction_characteristic:
    WITH CONSISTENT SNAPSHOT
  | READ WRITE | READ ONLY
  | [NOT] CHAIN
```

For example:

`BEGIN WITH CONSISTENT SNAPSHOT;`\
`START TRANSACTION READ ONLY, WITH CONSISTENT SNAPSH`OT;

## **The InnoDB Read View**

MariaDB's InnoDB storage engine uses a mechanism called MVCC (Multi-Version Concurrency Control) to handle concurrent data access. A core component of MVCC is the read view.

A read view can be thought of as an instantaneous snapshot of the database. When a transaction uses a read view, it sees only the data that was committed at the moment the "snapshot" was taken. It ignores any changes made by transactions that had not yet committed, as well as any changes from transactions that started after the read view was created.

The key difference addressed by this command is the timing of this snapshot:

<table><thead><tr><th width="203.71484375">Transaction Type</th><th width="200.11328125">Creation of Read View</th><th>Time of Read View Creation</th></tr></thead><tbody><tr><td><code>START TRANSACTION</code></td><td>Created lazily</td><td>At the first read operation (e.g., a <code>SELECT</code>)</td></tr><tr><td><code>START TRANSACTION WITH CONSISTENT SNAPSHOT</code></td><td>Created immediately</td><td>At the moment the statement is executed, before other actions</td></tr></tbody></table>

## **Behavior with Transaction Isolation Levels**

The behavior of `WITH CONSISTENT SNAPSHOT` is dependent on the transaction isolation level.

<table><thead><tr><th width="144.5390625">Isolation Level</th><th width="241.09375">Default Read View Behavior</th><th>Effect of WITH CONSISTENT SNAPSHOT</th></tr></thead><tbody><tr><td>REPEATABLE READ</td><td>A single, stable read view is created and used for the entire transaction.</td><td>Guarantees the read view is established immediately at the start of the transaction.</td></tr><tr><td>SERIALIZABLE</td><td>Same as REPEATABLE READ</td><td>Provides a predictable snapshot for all subsequent reads. This is its most common use case.</td></tr><tr><td>READ COMMITTED</td><td>A new read view is created for each individual <code>SELECT</code> statement.</td><td>Affects the first read statement only, ensuring its snapshot is taken at the transaction's start time.</td></tr><tr><td>READ UNCOMMITTED</td><td>Does not use read views. Reads include uncommitted data ("dirty reads").</td><td>Not permitted and has no effect.</td></tr></tbody></table>

### With Default Read View Behavior

#### Checking an Account Balance with a Transaction Delay

In this situation, there is a delay in the application logic after initiating a transaction to check an account balance.

#### Setup

```sql
CREATE TABLE accounts (
    id INT PRIMARY KEY,
    balance DECIMAL(10, 2)
) ENGINE=InnoDB;

INSERT INTO accounts VALUES (1, 1000.00);
```

#### Scenario: Two sessions are running concurrently.

<table><thead><tr><th width="111.34375">Timeline</th><th>Session 1 (Application checking balance)</th><th>Session 2 (An external deposit)</th></tr></thead><tbody><tr><td>T1</td><td><code>START TRANSACTION;</code></td><td></td></tr><tr><td>T2</td><td><code>-- Application logic causes a 2-second delay</code>  <code>DO SLEEP(2);</code></td><td><code>START TRANSACTION;</code></td></tr><tr><td>T3</td><td></td><td><code>UPDATE accounts SET balance = 1500.00 WHERE id = 1;</code></td></tr><tr><td>T4</td><td></td><td><code>COMMIT;</code></td></tr><tr><td>T5</td><td><code>SELECT balance FROM accounts WHERE id = 1;</code></td><td></td></tr><tr><td>T6</td><td><code>COMMIT;</code></td><td></td></tr></tbody></table>

In the scenario above, the read view for Session 1 is created at T5. Since Session 2's `COMMIT` happened at T4, the `SELECT` in Session 1 will see the new balance: `$1500.00`. This might not be the desired behavior if the goal was to see the balance as it was at T1.

### With CONSISTENT SNAPSHOT

<table><thead><tr><th width="104.4765625">Timeline</th><th>Session 1 (Application checking balance)</th><th>Session 2 (An external deposit)</th></tr></thead><tbody><tr><td>T1</td><td><code>START TRANSACTION WITH CONSISTENT SNAPSHOT;</code></td><td></td></tr><tr><td>T2</td><td><code>-- Application logic causes a 2-second delay</code> <code>DO SLEEP(2);</code></td><td><code>START TRANSACTION;</code></td></tr><tr><td>T3</td><td></td><td><code>UPDATE accounts SET balance = 1500.00 WHERE id = 1;</code></td></tr><tr><td>T4</td><td></td><td><code>COMMIT;</code></td></tr><tr><td>T5</td><td><code>SELECT balance FROM accounts WHERE id = 1;</code></td><td></td></tr><tr><td>T6</td><td><code>COMMIT;</code></td><td></td></tr></tbody></table>

In this second scenario, the read view for Session 1 is created immediately at T1. Even though Session 2 commits a change at T4, the `SELECT` at T5 uses the original snapshot. It will see the old balance: `$1000.00`, reflecting the state of the database when the transaction began.

## **Related System Variables**

### `innodb_snapshot_isolation`

This system variable influences the behavior of locking reads (e.g., `SELECT ... FOR UPDATE`). When [innodb\_snapshot\_isolation](../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_snapshot_isolation) is enabled (ON), locking reads will reference the transaction's read view. If a transaction tries to lock a row modified by another transaction not visible in the current read view, MariaDB returns an `ER_CHECKREAD` error instead of waiting for a lock. This enforces stricter snapshot consistency, even for locking operations.
