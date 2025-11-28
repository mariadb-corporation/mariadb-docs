---
description: >-
  Rename existing database accounts. This guide explains how to change a user's
  name while preserving their current privileges and properties.
---

# RENAME USER

## Syntax

```bnf
RENAME USER old_user TO new_user
    [, old_user TO new_user] ...
```

## Description

The RENAME USER statement renames existing MariaDB accounts. To use it, you must have the global [CREATE USER](grant.md#global-privileges) privilege or the [UPDATE](grant.md#table-privileges) privilege for the `mysql` database. Each account is named using the same format as for the [CREATE USER](create-user.md) statement; for example, `'jeffrey'@'localhost'`.\
If you specify only the user name part of the account name, a host name part of `'%'` is used.

If any of the old user accounts do not exist or any of the new user accounts already exist, `ERROR 1396 (HY000)` results. If an error occurs, `RENAME USER`will still rename the accounts that do not result in an error.

For modifying an existing account, see [ALTER USER](alter-user.md).

## Examples

```sql
CREATE USER 'donald', 'mickey';
RENAME USER 'donald' TO 'duck'@'localhost', 'mickey' TO 'mouse'@'localhost';
```

Renaming the host component of a user:

```sql
RENAME USER 'foo'@'1.2.3.4' TO 'foo'@'10.20.30.40';
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
