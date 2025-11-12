# DROP PACKAGE

## Syntax

```sql
DROP PACKAGE [IF EXISTS]  [ db_name . ] package_name
```

## Description

The `DROP PACKAGE` statement can be used when [Oracle SQL\_MODE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle) is set.

The `DROP PACKAGE` statement drops a stored package entirely:

* Drops the package specification (earlier created using the [CREATE PACKAGE](../create/create-package.md) statement).
* Drops the package implementation, if the implementation was already created using the [CREATE PACKAGE BODY](../create/create-package-body.md) statement.

## See Also

* [SHOW CREATE PACKAGE](../../administrative-sql-statements/show/show-create-package.md)
* [CREATE PACKAGE](../create/create-package.md)
* [CREATE PACKAGE BODY](../create/create-package-body.md)
* [DROP PACKAGE BODY](drop-package-body.md)
* [Oracle SQL\_MODE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
