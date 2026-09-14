# Error 1045: Access denied for user (using password)

| Error Code | SQLSTATE | Error                     | Description                                           |
| ---------- | -------- | ------------------------- | ----------------------------------------------------- |
| 1045       | 28000    | ER\_ACCESS\_DENIED\_ERROR | Access denied for user '%s'@'%s' (using password: %s) |

## Possible Causes and Solutions

The user/password combination does not exist or the user does not have privileges to the given database. See [Troubleshooting Connection Issues](../../../mariadb-quickstart-guides/mariadb-connection-troubleshooting-guide.md) for more, as well as [GRANT](../../sql-statements/account-management-sql-statements/grant.md) for details on setting permissions.

## See Also

* [When access\_denied\_errors status variable is incremented](../../../security/user-account-management/incrementing-of-the-access_denied_errors-status-variable.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
