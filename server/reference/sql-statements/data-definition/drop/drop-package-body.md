# DROP PACKAGE BODY

## Syntax

```sql
DROP PACKAGE BODY [IF EXISTS]  [ db_name . ] package_name
```

## Description

The `DROP PACKAGE BODY` statement can be used when [Oracle SQL\_MODE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle) is set.

The `DROP PACKAGE BODY` statement drops the package body (that is, the implementation) which was created using the [CREATE PACKAGE BODY](../create/create-package-body.md) statement.

Note, `DROP PACKAGE BODY` drops only the package implementation, but does not drop the package specification. Use [DROP PACKAGE](drop-package.md) to drop the package entirely (i.e. both implementation and specification).

## See also

* [CREATE PACKAGE](../create/create-package.md)
* [SHOW CREATE PACKAGE](../../administrative-sql-statements/show/show-create-package.md)
* [DROP PACKAGE](drop-package.md)
* [CREATE PACKAGE BODY](../create/create-package-body.md)
* [SHOW CREATE PACKAGE BODY](../../administrative-sql-statements/show/show-create-package-body.md)
* [Oracle SQL\_MODE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
