# Error 1044: Access denied for user

| Error Code | SQLSTATE | Error                       | Description                                       |
| ---------- | -------- | --------------------------- | ------------------------------------------------- |
| 1044       | 42000    | ER\_DBACCESS\_DENIED\_ERROR | Access denied for user '%s'@'%s' to database '%s' |

## Possible Causes and Solutions

The user is trying to access a database/schema they do not have access to. See [Troubleshooting Connection Issues](../../../mariadb-quickstart-guides/mariadb-connection-troubleshooting-guide.md) for more, as well as [GRANT](../../sql-statements/account-management-sql-statements/grant.md) for details on setting permissions.

## See Also

* [When access\_denied\_errors status variable is incremented](../../../security/user-account-management/incrementing-of-the-access_denied_errors-status-variable.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
