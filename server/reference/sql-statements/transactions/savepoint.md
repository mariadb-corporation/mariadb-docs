---
description: >-
  Create a named marker within a transaction. Savepoints allow you to roll back
  part of a transaction without canceling the entire operation.
---

# SAVEPOINT

## Syntax

```sql
SAVEPOINT identifier
ROLLBACK [WORK] TO [SAVEPOINT] identifier
RELEASE SAVEPOINT identifier
```

## Description

InnoDB supports the SQL statements `SAVEPOINT`,`ROLLBACK TO SAVEPOINT`, `RELEASE SAVEPOINT`\
and the optional `WORK` keyword for`ROLLBACK`.

Each savepoint must have a legal [MariaDB identifier](../../sql-structure/sql-language-structure/identifier-names.md). A savepoint is a named sub-transaction.

Normally [ROLLBACK](rollback.md) undoes the changes performed by the whole transaction. When used with the `TO` clause, it undoes the changes performed after the specified savepoint, and erases all subsequent savepoints. However, all locks that have been acquired after the save point will survive. `RELEASE SAVEPOINT` does not rollback or commit any changes, but removes the specified savepoint.

When the execution of a trigger or a stored function begins, it is not possible to use statements which reference a savepoint which was defined from out of that stored program.

When a [COMMIT](commit.md) (including implicit commits) or a `ROLLBACK` statement (with no `TO` clause) is performed, they act on the whole transaction, and all savepoints are removed.

## Errors

If `COMMIT` or `ROLLBACK` is issued and no transaction was started, no error is reported.

If `SAVEPOINT` is issued and no transaction was started, no error is reported but no savepoint is created. When `ROLLBACK TO SAVEPOINT` or `RELEASE SAVEPOINT` is called for a savepoint that does not exist, an error like this is issued:

```sql
ERROR 1305 (42000): SAVEPOINT svp_name does not exist
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
