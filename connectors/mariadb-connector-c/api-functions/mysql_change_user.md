---
description: >-
  mysql_change_user changes the authenticated user and default database on
  an existing connection, resetting session state including transactions,
  temporary tables, and locks.
---

# mysql\_change\_user

## Syntax

```c
my_bool mysql_change_user(MYSQL * mysql,
                          const char * user,
                          const char * passwd,
                          const char * db);
```

* `mysql` - a mysql handle, which was previously allocated by [mysql\_init()](mysql_init.md) or [mysql\_real\_connect()](mysql_real_connect.md).
* `user` - the user name for server authentication
* `passwd` - the password for server authentication
* `db` - the default database. If desired, the NULL value may be passed resulting in only changing the user and not selecting a database. To select a database in this case use the [mysql\_select\_db()](mysql_select_db.md) function.

## Description

Changes the user and default database of the current connection.

In order to successfully change users a valid username and password parameters must be provided and that user must have sufficient permissions to access the desired database. If for any reason authorization fails, the current user authentication will remain.

Returns zero on success, nonzero if an error occured.

{% hint style="info" %}
mysql\_change\_user will always cause the current database connection to behave as if was a completely new database connection, regardless of if the operation was completed successfully. This reset includes performing a rollback on any active transactions, closing all temporary tables, and unlocking all locked tables.
{% endhint %}


{% @marketo/form formId="4316" %}
