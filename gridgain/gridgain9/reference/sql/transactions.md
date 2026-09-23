---
description: >-
  SQL transaction control in GridGain 9 using START TRANSACTION and COMMIT,
  including read-only and read-write modes.
---

# Transactions

A transaction is a sequence of SQL operations that starts with the `START TRANSACTION` statement and ends with the `COMMIT` statement. Either the effect of all operations will be published, or no results will be published at all.

{% hint style="warning" %}
Transaction control statements are only allowed within a [script](../../gridgain9-usage/sql/sql-api.md#using-scripts).
{% endhint %}

In GridGain 9, you start the transaction by using the `START TRANSACTION` statement:

```bnf
START TRANSACTION [ READ ONLY | READ WRITE ]
```

<!-- Diagram(
Terminal('START TRANSACTION'),
ZeroOrMore(
Terminal('READ ONLY'),
Terminal('READ WRITE'))) -->

{% hint style="info" %}
DDL statements are not supported inside transactions.
{% endhint %}

Parameters:

- `READ WRITE` - both read and write operations are allowed in the transaction. Used by default.
- `READ ONLY` - only read operations are allowed in the transaction.

You close and commit the transaction by using the `COMMIT` statement:

```bnf
COMMIT
```

<!-- Diagram(
Terminal('COMMIT')) -->

## Example

The example below inserts 3 lines into the table in a single transaction, ensuring they will all be committed together:

```sql
START TRANSACTION READ WRITE;

INSERT INTO Person (id, name, surname) VALUES (1, 'John', 'Smith');
INSERT INTO Person (id, name, surname) VALUES (2, 'Jane', 'Smith');
INSERT INTO Person (id, name, surname) VALUES (3, 'Adam', 'Mason');

COMMIT;
```
