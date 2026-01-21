---
description: >-
  Explains how to lock and unlock user accounts using `CREATE USER` and `ALTER
  USER` statements to prevent login access without deleting the account.
---

# Account Locking

## Syntax

```
 CREATE USER [...]
 [lock_option] [password_option] 
 
 ALTER USER [...]
 [lock_option] [password_option] 
```

{% tabs %}
{% tab title="Current" %}
The _lock\_option_ and _password\_option_ clauses can occur in either order.
{% endtab %}

{% tab title="<10.4.7, < 10.5.8" %}
Prior to [MariaDB 10.4.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1047-release-notes) and [MariaDB 10.5.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1058-release-notes), the _lock\_option_ must be placed before the _password\_option_.
{% endtab %}
{% endtabs %}

## Description

Account locking permits privileged administrators to lock/unlock user accounts. No new client connections will be permitted if an account is locked (existing connections are not affected).

### Locking Accounts

User accounts can be locked at creation, with the [CREATE USER](../../reference/sql-statements/account-management-sql-statements/create-user.md) statement, or modified after creation with the [ALTER USER](../../reference/sql-statements/account-management-sql-statements/alter-user.md) statement. For example:

```sql
CREATE USER 'lorin'@'localhost' ACCOUNT LOCK;
```

or

```sql
ALTER USER 'marijn'@'localhost' ACCOUNT LOCK;
```

The server will return an `ER_ACCOUNT_HAS_BEEN_LOCKED` error when locked users attempt to connect:

```sql
mariadb -ulorin
  ERROR 4151 (HY000): Access denied, this account is locked
```

### Unlocking Accounts

The [ALTER USER](../../reference/sql-statements/account-management-sql-statements/alter-user.md) statement is used to unlock a user:

```sql
ALTER USER 'lorin'@'localhost' ACCOUNT UNLOCK;
```

### Show Whether a Specific Account is Locked

The [SHOW CREATE USER](../../reference/sql-statements/administrative-sql-statements/show/show-create-user.md) statement will show whether the account is locked:

```sql
SHOW CREATE USER 'marijn'@'localhost';
+-----------------------------------------------+
| CREATE USER for marijn@localhost              |
+-----------------------------------------------+
| CREATE USER 'marijn'@'localhost' ACCOUNT LOCK |
+-----------------------------------------------+
```

as well as querying the [mysql.global\_priv table](../../reference/system-tables/the-mysql-database-tables/mysql-global_priv-table.md):

```sql
SELECT CONCAT(user, '@', host, ' => ', JSON_DETAILED(priv)) 
  FROM mysql.global_priv 
  WHERE user='marijn';
+--------------------------------------------------------------------------------------+
| CONCAT(user, '@', host, ' => ', JSON_DETAILED(priv))                                 |
+--------------------------------------------------------------------------------------+
| marijn@localhost => {
    "access": 0,
    "plugin": "mysql_native_password",
    "authentication_string": "",
    "account_locked": true,
    "password_last_changed": 1558017158
} |
+--------------------------------------------------------------------------------------+
```

### Find Locked Accounts

This query against the `mysql.global_priv` table will return all accounts which have `"account_locked": true` within the `Priv` json column:

```sql
SELECT CONCAT(user, '@', host) AS 'Locked Accounts' FROM mysql.global_priv WHERE Priv like '%account_locked":true%';
```

Example Output:

```
+------------------------+
| Locked Accounts        |
+------------------------+
| mariadb.sys@localhost  |
| bart.simpson@localhost |
+------------------------+
2 rows in set (0.000 sec)
```

## See Also

* [Account Locking and Password Expiry](https://www.youtube.com/watch?v=AWM_fWZ3XIw) video tutorial

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
