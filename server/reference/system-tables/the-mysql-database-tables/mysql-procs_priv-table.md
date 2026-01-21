---
description: >-
  The mysql.procs_priv table records privileges granted to users specifically
  for executing or altering stored procedures and functions.
---

# mysql.procs\_priv Table

{% include "../../../.gitbook/includes/system-tables-warning.md" %}

The `mysql.procs_priv` table contains information about [stored procedure](../../../server-usage/stored-routines/stored-procedures/) and [stored function](../../../server-usage/stored-routines/stored-functions/) privileges. See [CREATE PROCEDURE](../../../server-usage/stored-routines/stored-procedures/create-procedure.md) and [CREATE FUNCTION](../../sql-statements/data-definition/create/create-function.md) on creating these.

The [INFORMATION\_SCHEMA.ROUTINES](../information-schema/information-schema-tables/information-schema-routines-table.md) table derives its contents from `mysql.procs_priv`.

This table uses the [Aria](../../../server-usage/storage-engines/aria/) storage engine.

The `mysql.procs_priv` table contains the following fields:

| Field         | Type                                                    | Null | Key | Default            | Description                                                                                                                                                                                                                                                                                                                                        |
| ------------- | ------------------------------------------------------- | ---- | --- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Host          | char(60)                                                | NO   | PRI |                    | Host (together with Db, User, Routine\_name and Routine\_type makes up the unique identifier for this record).                                                                                                                                                                                                                                     |
| Db            | char(64)                                                | NO   | PRI |                    | Database (together with Host, User, Routine\_name and Routine\_type makes up the unique identifier for this record).                                                                                                                                                                                                                               |
| User          | char(80)                                                | NO   | PRI |                    | User (together with Host, Db, Routine\_name and Routine\_type makes up the unique identifier for this record).                                                                                                                                                                                                                                     |
| Routine\_name | char(64)                                                | NO   | PRI |                    | Routine\_name (together with Host, Db User and Routine\_type makes up the unique identifier for this record).                                                                                                                                                                                                                                      |
| Routine\_type | enum('FUNCTION','PROCEDURE', 'PACKAGE', 'PACKAGE BODY') | NO   | PRI | NULL               | Whether the routine is a [stored procedure](../../../server-usage/stored-routines/stored-procedures/), [stored function](../../../server-usage/stored-routines/stored-functions/), [package](../../sql-statements/data-definition/create/create-package.md) or [package body](../../sql-statements/data-definition/create/create-package-body.md). |
| Grantor       | char(141)                                               | NO   | MUL |                    |                                                                                                                                                                                                                                                                                                                                                    |
| Proc\_priv    | set('Execute','Alter Routine','Grant')                  | NO   |     |                    | The routine privilege. See [Function Privileges](../../sql-statements/account-management-sql-statements/grant.md#function-privileges) and [Procedure Privileges](../../sql-statements/account-management-sql-statements/grant.md#procedure-privileges) for details.                                                                                |
| Timestamp     | timestamp                                               | NO   |     | CURRENT\_TIMESTAMP |                                                                                                                                                                                                                                                                                                                                                    |

The [Acl\_function\_grants](../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#acl_function_grants) status variable indicates how many rows the `mysql.columns_priv` table contains with the `FUNCTION` routine type.

The [Acl\_procedure\_grants](../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#acl_procedure_grants) status variable indicates how many rows the `mysql.columns_priv` table contains with the `PROCEDURE` routine type.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
