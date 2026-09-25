---
description: >-
  SQL transaction control in GridGain using BEGIN, COMMIT, and ROLLBACK
  statements.
---

# Transactions

{% hint style="warning" %}
Support for [SQL transactions](../../architecture/mvcc.md) is currently in the beta stage. For production use, consider key-value transactions.
{% endhint %}

## Description

GridGain supports the following functions that allow you to start, commit, or rollback a transaction:

```sql
BEGIN [TRANSACTION]

COMMIT [TRANSACTION]

ROLLBACK [TRANSACTION]
```

{% hint style="info" %}
DDL statements are not supported inside transactions.
{% endhint %}

A transaction is a sequence of SQL operations that starts with the `BEGIN` statement and ends with the `COMMIT` statement. Either all of the operations in a transaction succeed or they all fail.

The `ROLLBACK [TRANSACTION]` statement undoes all updates made since the last time a `COMMIT` or `ROLLBACK` command was issued.

## Example

Add a person and update the city population by 1 in a single transaction.

```sql
BEGIN;

INSERT INTO Person (id, name, city_id) VALUES (1, 'John Doe', 3);

UPDATE City SET population = population + 1 WHERE id = 3;

COMMIT;
```

Roll back the changes made by the previous commands.

```sql
BEGIN;

INSERT INTO Person (id, name, city_id) VALUES (1, 'John Doe', 3);

UPDATE City SET population = population + 1 WHERE id = 3;
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
