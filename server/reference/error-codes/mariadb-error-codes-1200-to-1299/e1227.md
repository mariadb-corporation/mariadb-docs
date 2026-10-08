# Error 1227: Access denied; you need (at least one of) the privilege(s) for this operation

| Error Code | SQLSTATE | Error                               | Description                                                                      |
| ---------- | -------- | ----------------------------------- | -------------------------------------------------------------------------------- |
| 1227       | 42000    | ER\_SPECIFIC\_ACCESS\_DENIED\_ERROR | Access denied; you need (at least one of) the %s privilege(s) for this operation |

## Possible Causes and Solutions

The user is trying to access a database/schema/object they do not have access to. The error shows which [GRANT](../../sql-statements/account-management-sql-statements/grant.md) is needed to access the resource.

## See Also

* [When access\_denied\_errors status variable is incremented](../../../security/user-account-management/incrementing-of-the-access_denied_errors-status-variable.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
