# Error 1142: command denied to user for table

| Error Code | SQLSTATE | Error                          | Description                                        |
| ---------- | -------- | ------------------------------ | -------------------------------------------------- |
| 1142       | 42000    | ER\_TABLEACCESS\_DENIED\_ERROR | %s command denied to user '%s'@'%s' for table '%s' |

## Possible Causes and Solutions

The user is trying to access a table or a column from a table they do not have access to. See [GRANT](../../sql-statements/account-management-sql-statements/grant.md) for details on setting permissions.

## See Also

* [When access\_denied\_errors status variable is incremented](../../../security/user-account-management/incrementing-of-the-access_denied_errors-status-variable.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
