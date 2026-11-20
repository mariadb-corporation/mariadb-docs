---
description: >-
  Group related stored procedures and functions into a stored package, with
  package variables, private routines, and an initialization section. Covers
  privileges and name resolution.
---

# Stored Packages

A stored package groups related stored procedures and functions, and the variables they share, into one schema object. A package has two parts:

* The **specification**, created with [CREATE PACKAGE](../../reference/sql-statements/data-definition/create/create-package.md), declares the package's public routines.
* The **body**, created with [CREATE PACKAGE BODY](../../reference/sql-statements/data-definition/create/create-package-body.md), defines those routines. It can also declare package variables and private routines, and end with an initialization section.

{% hint style="info" %}
From MariaDB 11.4, stored packages can be used in any SQL mode. Before MariaDB 11.4, they're available only when [Oracle SQL\_MODE](../../editions-and-compatibility/comparisons-with-other-databases/sql_modeoracle.md) is set.

In Oracle mode, a package uses the PL/SQL dialect. In other modes, it uses the same SQL/PSM syntax as standalone [stored procedures](stored-procedures/) and [stored functions](stored-functions/). The examples on this page use the default mode.
{% endhint %}

## Why Use Packages

* **Grouping:** related routines are called with the package name as a prefix, such as `counter.next_value()`, so it's clear they belong together.
* **Private routines:** helper routines that callers shouldn't use stay inside the package.
* **Session state:** package variables keep their values between calls for the rest of the session, without user-defined variables.
* **One-time setup:** the initialization section runs once per session, before the package is first used.

## Packages and SQL Standard Modules

The SQL standard groups routines into modules, created with `CREATE MODULE`. MariaDB doesn't support modules; there is no `CREATE MODULE` statement. Stored packages follow the Oracle PL/SQL model instead, with a separate specification and body.

## Creating a Package

Create the specification first, then the body. Each routine declared in the specification must be defined in the body, or `CREATE PACKAGE BODY` fails with error 4095, and a body can't be created before its specification.

This package counts in steps. `next_value()` and `reset()` are public. `step()` is private, and `n` and `inits` are package variables.

Both `CREATE` statements contain semicolons, which end each declaration and each statement inside the routines. The [mariadb](../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md#delimiters) command-line client normally sends a statement to the server as soon as it reads a semicolon, which would cut `CREATE PACKAGE` off after its first declaration. So the example first sets the client's delimiter to `$$`, ends each `CREATE` statement with `$$`, and then sets the delimiter back with `DELIMITER ;`. `DELIMITER` is a command of the client, not an SQL statement: an application that creates a package through a connector sends each `CREATE` statement as it is, without it.

```sql
DELIMITER $$

CREATE PACKAGE counter
  FUNCTION next_value() RETURNS INT;
  PROCEDURE reset();
END;
$$

CREATE PACKAGE BODY counter
  -- package variables
  DECLARE n INT DEFAULT 0;
  DECLARE inits INT DEFAULT 0;

  -- a private routine: not declared in the specification
  FUNCTION step() RETURNS INT
  BEGIN
    RETURN 1;
  END;

  -- public routines
  FUNCTION next_value() RETURNS INT
  BEGIN
    SET n = n + step();
    RETURN n * 100 + inits;
  END;

  PROCEDURE reset()
  BEGIN
    SET n = 0;
  END;

  -- initialization section
  SET inits = inits + 1;
END;
$$

DELIMITER ;
```

```sql
SELECT counter.next_value(), counter.next_value();
+----------------------+----------------------+
| counter.next_value() | counter.next_value() |
+----------------------+----------------------+
|                  101 |                  201 |
+----------------------+----------------------+

CALL counter.reset();

SELECT counter.next_value();
+----------------------+
| counter.next_value() |
+----------------------+
|                  101 |
+----------------------+
```

The last two digits are `inits`: the initialization section ran once, however many routines the session calls.

### Package Variables

Package variables are declared with `DECLARE` at the start of the body, before the routines. Every routine in the package can read and change them, but they can't be referenced from outside the package.

Each session has its own copy of the package variables. They keep their values between calls for the rest of the session, and a new session starts again from their `DEFAULT` values.

### Public and Private Routines

A routine declared in the specification is public. A routine defined only in the body is private: it's for use by the other routines in the package and by the initialization section, and isn't part of the package's interface.

Outside the package, a public routine must be called with the package name, such as `counter.next_value()`. Inside the body, routines of the same package can call each other without it, as `next_value()` calls `step()` above.
### Initialization Section

Statements after the last routine in the body, before `END`, form the initialization section. It runs once per session, before the session's first use of the package, and is typically used to set package variables.

## Calling Package Routines

There are two ways to name a public package routine:

* `package_name.routine()`, such as `counter.next_value()`, works when the package's database is the current database.
* `db_name.package_name.routine()`, such as `db1.counter.next_value()`, works from any database, and with no current database.

The two-part form is the same as the form for calling a stored routine in another schema: `tax.rate()` can also mean the function `rate()` in the schema `tax`. When a two-part name could mean either, MariaDB checks for a package first. It calls the package routine only if both of these are true:

* The current database has a package with that name.
* That package has a public routine with that name.

Otherwise, MariaDB calls the routine in the schema with that name.

For example, the database `sales` has a package `tax` with one public function, `rate()`. The server also has a schema called `tax`, with the stored functions `rate()` and `region()`. This is what each call runs:

| Call | Current database is `sales` | Current database is any other, or none |
| ---- | --------------------------- | -------------------------------------- |
| `tax.rate()` | The package function | The function `rate()` in the schema `tax` |
| `tax.region()` | The function `region()` in the schema `tax`, because the package has no `region()` | The function `region()` in the schema `tax` |
| `sales.tax.rate()` | The package function | The package function |

To call a package routine without depending on the current database, use the three-part name.

A package can also have the same name as a standalone stored function or procedure in the same database. A standalone routine isn't called with a package-style name, so the two don't conflict.

## Privileges

Packages use the stored routine privileges, granted on a package specification or a package body:

* Creating a package or package body requires the `CREATE ROUTINE` privilege.
* Calling a package's routines requires the `EXECUTE` privilege on its package body.

```sql
GRANT EXECUTE ON PACKAGE BODY db1.counter TO alice@localhost;
```

For how these privileges are granted automatically, and what happens to them when a package is replaced or dropped, see [Stored Routine Privileges](stored-functions/stored-routine-privileges.md).

## Viewing Packages

* [SHOW CREATE PACKAGE](../../reference/sql-statements/administrative-sql-statements/show/show-create-package.md) and [SHOW CREATE PACKAGE BODY](../../reference/sql-statements/administrative-sql-statements/show/show-create-package-body.md) show the statements that created the specification and the body.
* [SHOW PACKAGE STATUS](../../reference/sql-statements/administrative-sql-statements/show/show-package-status.md) and [SHOW PACKAGE BODY STATUS](../../reference/sql-statements/administrative-sql-statements/show/show-package-body-status.md) list packages and their characteristics.
* The [information\_schema.ROUTINES](../../reference/system-tables/information-schema/information-schema-tables/information-schema-routines-table.md) table has one row of type `PACKAGE` and one of type `PACKAGE BODY` for each package. The routines inside a package aren't listed separately.
* `SHOW PACKAGE BODY CODE` shows the internal representation of the body, like [SHOW PROCEDURE CODE](../../reference/sql-statements/administrative-sql-statements/show/show-procedure-code.md). It's available only in debug builds of the server. There's no `SHOW PACKAGE CODE`, because a specification has no code.

## How Packages Are Stored

A package is stored as two rows in the [mysql.proc](../../reference/system-tables/the-mysql-database-tables/mysql-proc-table.md) table, of type `PACKAGE` and `PACKAGE BODY`. The body row holds the whole implementation: the variables, every routine, and the initialization section. Privileges on packages are kept in the [mysql.procs\_priv](../../reference/system-tables/the-mysql-database-tables/mysql-procs_priv-table.md) table, with a `Routine_type` of `PACKAGE` or `PACKAGE BODY`.

## Dropping Packages

[DROP PACKAGE](../../reference/sql-statements/data-definition/drop/drop-package.md) drops the specification and the body. [DROP PACKAGE BODY](../../reference/sql-statements/data-definition/drop/drop-package-body.md) drops only the body.

## See Also

* [CREATE PACKAGE](../../reference/sql-statements/data-definition/create/create-package.md)
* [CREATE PACKAGE BODY](../../reference/sql-statements/data-definition/create/create-package-body.md)
* [Stored Procedure Overview](stored-procedures/stored-procedure-overview.md)
* [Stored Function Overview](stored-functions/stored-function-overview.md)
* [Stored Routine Privileges](stored-functions/stored-routine-privileges.md)
* [Oracle SQL\_MODE](../../editions-and-compatibility/comparisons-with-other-databases/sql_modeoracle.md)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
