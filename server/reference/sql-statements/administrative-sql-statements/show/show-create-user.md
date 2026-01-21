---
description: >-
  View the CREATE USER statement. This statement returns the SQL required to
  recreate a user account with its authentication details.
---

# SHOW CREATE USER

## Syntax

```sql
SHOW CREATE USER [user-name]
```

## Description

Shows the [CREATE USER](../../account-management-sql-statements/create-user.md) statement that creates the given user. The statement requires the [SELECT](../../account-management-sql-statements/grant.md#table-privileges) privilege for the [mysql](../../../system-tables/the-mysql-database-tables/) database, except for the current user. The [CREATE USER](../../account-management-sql-statements/create-user.md) statement for the current user is shown where no user is specified.

`SHOW CREATE USER` quotes identifiers according to the value of the [sql\_quote\_show\_create](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_quote_show_create) system variable.

## Examples

```sql
CREATE USER foo4@test require cipher 'text' 
  issuer 'foo_issuer' subject 'foo_subject';

SHOW CREATE USER foo4@test\G
*************************** 1. row ***************************
CREATE USER 'foo4'@'test' 
  REQUIRE ISSUER 'foo_issuer' 
  SUBJECT 'foo_subject' 
  CIPHER 'text'
```

[User Password Expiry](../../../../security/user-account-management/user-password-expiry.md):

```sql
CREATE USER 'monty'@'localhost' PASSWORD EXPIRE INTERVAL 120 DAY;

SHOW CREATE USER 'monty'@'localhost';
+------------------------------------------------------------------+
| CREATE USER for monty@localhost                                  |
+------------------------------------------------------------------+
| CREATE USER 'monty'@'localhost' PASSWORD EXPIRE INTERVAL 120 DAY |
+------------------------------------------------------------------+
```

## See Also

* [CREATE USER](../../account-management-sql-statements/create-user.md)
* [ALTER USER](../../account-management-sql-statements/alter-user.md)
* [SHOW GRANTS](show-grants.md) shows the `GRANTS/PRIVILEGES` for a user.
* [SHOW PRIVILEGES](show-privileges.md) shows the privileges supported by MariaDB.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
