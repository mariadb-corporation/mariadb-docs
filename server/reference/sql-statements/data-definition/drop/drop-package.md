---
description: >-
  Remove a stored package completely. This command deletes both the package
  specification (interface) and its body (implementation) from the database.
---

# DROP PACKAGE

## Syntax

```bnf
DROP PACKAGE [IF EXISTS]  [ db_name . ] package_name
```

## Description

From MariaDB 11.4, the `DROP PACKAGE` statement can be used in any mode. Before MariaDB 11.4, it can be used only when [Oracle SQL\_MODE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle) is set.

The `DROP PACKAGE` statement drops a stored package entirely:

* Drops the package specification (earlier created using the [CREATE PACKAGE](../create/create-package.md) statement).
* Drops the package implementation, if the implementation was already created using the [CREATE PACKAGE BODY](../create/create-package-body.md) statement.

If [automatic\_sp\_privileges](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#automatic_sp_privileges) is set (the default), privileges on the package and its body are revoked from all accounts. `CREATE OR REPLACE PACKAGE` keeps them. See [Stored Routine Privileges](../../../../server-usage/stored-routines/stored-functions/stored-routine-privileges.md#dropping-stored-routines).

## See Also

* [SHOW CREATE PACKAGE](../../administrative-sql-statements/show/show-create-package.md)
* [CREATE PACKAGE](../create/create-package.md)
* [CREATE PACKAGE BODY](../create/create-package-body.md)
* [DROP PACKAGE BODY](drop-package-body.md)
* [Oracle SQL\_MODE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
