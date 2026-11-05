---
description: >-
  Delete the body of a stored package. This command removes the implementation
  logic while preserving the package specification and interface.
---

# DROP PACKAGE BODY

## Syntax

```bnf
DROP PACKAGE BODY [IF EXISTS]  [ db_name . ] package_name
```

## Description

From MariaDB 11.4, the `DROP PACKAGE BODY` statement can be used in any mode. Before MariaDB 11.4, it can be used only when [Oracle SQL\_MODE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle) is set.

The `DROP PACKAGE BODY` statement drops the package body (that is, the implementation) which was created using the [CREATE PACKAGE BODY](../create/create-package-body.md) statement.

Note, `DROP PACKAGE BODY` drops only the package implementation, but does not drop the package specification. Use [DROP PACKAGE](drop-package.md) to drop the package entirely (i.e. both implementation and specification).

If [automatic\_sp\_privileges](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#automatic_sp_privileges) is set (the default), privileges on the package body are revoked from all accounts. `CREATE OR REPLACE PACKAGE BODY` keeps them. See [Stored Routine Privileges](../../../../server-usage/stored-routines/stored-functions/stored-routine-privileges.md#dropping-stored-routines).

## See also

* [CREATE PACKAGE](../create/create-package.md)
* [SHOW CREATE PACKAGE](../../administrative-sql-statements/show/show-create-package.md)
* [DROP PACKAGE](drop-package.md)
* [CREATE PACKAGE BODY](../create/create-package-body.md)
* [SHOW CREATE PACKAGE BODY](../../administrative-sql-statements/show/show-create-package-body.md)
* [Oracle SQL\_MODE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
