---
description: >-
  This page explains the privileges required to create, alter, execute, and drop
  stored routines, including the automatic grants for creators.
---

# Stored Routine Privileges

It's important to give careful thought to the privileges associated with [stored functions](./) and [stored procedures](../stored-procedures/). The following is an explanation of how they work.

## Creating Stored Routines

* To create a stored routine, the [CREATE ROUTINE](../../../reference/sql-statements/account-management-sql-statements/grant.md#database-privileges) privilege is needed. The [SUPER](../../../reference/sql-statements/account-management-sql-statements/grant.md#super) privilege is required if a `DEFINER` is declared that's not the creator's account (see [DEFINER clause](stored-routine-privileges.md#definer-clause) below). The `SUPER` privilege is also required if statement-based binary logging is used. See [Binary Logging of Stored Routines](../binary-logging-of-stored-routines.md) for more details.

## Altering Stored Routines

* To make changes to, or drop, a stored routine, the [ALTER ROUTINE](../../../reference/sql-statements/account-management-sql-statements/grant.md#function-privileges) privilege is needed. When a routine is created, its creator is granted `ALTER ROUTINE` and `EXECUTE` on it, unless the [automatic\_sp\_privileges](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#automatic_sp_privileges) variable is set to `0` (it defaults to `1`). These are ordinary grants, stored in [mysql.procs\_priv](../../../reference/system-tables/the-mysql-database-tables/mysql-procs_priv-table.md), and are shown by [SHOW GRANTS](../../../reference/sql-statements/administrative-sql-statements/show/show-grants.md).
* The `SUPER` privilege is also required if statement-based binary logging is used. See [Binary Logging of Stored Routines](../binary-logging-of-stored-routines.md) for more details.

## Running Stored Routines

* To run a stored routine, the [EXECUTE](../../../reference/sql-statements/account-management-sql-statements/grant.md#function-privileges) privilege is needed. The creator is granted it when the routine is created, unless the [automatic\_sp\_privileges](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#automatic_sp_privileges) variable is set to `0`.
* The [SQL SECURITY clause](stored-routine-privileges.md#sql-security-clause) (by default `DEFINER`) specifies what privileges are used when a routine is called. If `SQL SECURITY` is `INVOKER`, the function body are evaluated using the privileges of the user calling the function. If `SQL SECURITY` is `DEFINER`, the function body is always evaluated using the privileges of the definer account. `DEFINER` is the default. Thus, by default, users who can access the database associated with the stored routine can also run the routine, and potentially perform operations they wouldn't normally have permissions for.
* The creator of a routine is the account that ran the [CREATE FUNCTION](../../../reference/sql-statements/data-definition/create/create-function.md) or [CREATE PROCEDURE](../stored-procedures/create-procedure.md) statement, regardless of whether a `DEFINER` is provided. The definer is by default the creator unless otherwise specified.
* The server automatically changes the privileges in the [mysql.procs\_priv](../../../reference/system-tables/the-mysql-database-tables/mysql-procs_priv-table.md) table as required, but will not look out for manual changes.

### DEFINER Clause

If left out, the `DEFINER` is treated as the account that created the stored routine or view. If the account creating the routine has the `SUPER` privilege, another account can be specified as the `DEFINER`.

### SQL SECURITY Clause

This clause specifies the context the stored routine or view will run as. It can take two values - `DEFINER` or `INVOKER`. `DEFINER` is the account specified as the `DEFINER` when the stored routine or view was created (see the section above). `INVOKER` is the account invoking the routine or view.

As an example, let's assume a routine, created by a superuser who's specified as the `DEFINER`, deletes all records from a table. If `SQL SECURITY=DEFINER`, anyone running the routine, regardless of whether they have delete privileges, are able to delete the records. If `SQL SECURITY = INVOKER`, the routine will only delete the records if the account invoking the routine has permission to do so.

`INVOKER` is usually less risky, as a user cannot perform any operations they're normally unable to. However, it's not uncommon for accounts to have relatively limited permissions, but be specifically granted access to routines, which are then invoked in the `DEFINER` context.

## Dropping Stored Routines

When [automatic\_sp\_privileges](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#automatic_sp_privileges) is `1` (the default), dropping a stored routine with [DROP PROCEDURE](../stored-procedures/drop-procedure.md), [DROP FUNCTION](drop-function.md), [DROP PACKAGE](../../../reference/sql-statements/data-definition/drop/drop-package.md), or [DROP PACKAGE BODY](../../../reference/sql-statements/data-definition/drop/drop-package-body.md) revokes every privilege that is specific to that routine, from all accounts and roles, not just the creator. When `automatic_sp_privileges` is `0`, these privileges are left in place.

`CREATE OR REPLACE` keeps them. If you replace a routine with [CREATE OR REPLACE PROCEDURE](../stored-procedures/create-procedure.md), [CREATE OR REPLACE FUNCTION](../../../reference/sql-statements/data-definition/create/create-function.md), [CREATE OR REPLACE PACKAGE](../../../reference/sql-statements/data-definition/create/create-package.md), or [CREATE OR REPLACE PACKAGE BODY](../../../reference/sql-statements/data-definition/create/create-package-body.md), the existing privileges on it stay in effect. So `CREATE OR REPLACE` is not the same as `DROP` followed by `CREATE`:

```sql
CREATE PROCEDURE p1() SELECT 1;
CREATE PROCEDURE p2() SELECT 1;
GRANT EXECUTE ON PROCEDURE p1 TO alice@localhost;
GRANT EXECUTE ON PROCEDURE p2 TO alice@localhost;

CREATE OR REPLACE PROCEDURE p1() SELECT 2;  -- alice keeps EXECUTE on p1
DROP PROCEDURE p2;                          -- alice loses EXECUTE on p2
CREATE PROCEDURE p2() SELECT 2;             -- and does not get it back
```

{% hint style="info" %}
This applies only to stored routines. For tables, views, sequences, and databases, `DROP` does not remove privileges on the object, so replacing it with `CREATE OR REPLACE` or with `DROP` and `CREATE` leaves the same privileges in place. For users and roles, both `CREATE OR REPLACE` and `DROP` followed by `CREATE` remove all of the account's privileges.
{% endhint %}

## See Also

* [Changing the DEFINER of MySQL stored routines etc.](https://mariadb.com/blog/changing-definer-mysql-stored-routines-etc) - maria.com post on what to do after you've dropped a user, and now want to change the DEFINER on all database objects that currently have it set to this dropped user.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
