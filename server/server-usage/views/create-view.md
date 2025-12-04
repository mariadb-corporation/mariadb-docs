---
description: >-
  Create a virtual table based on a query. This statement defines a view that
  presents data from underlying tables as a single, queryable object.
---

# CREATE VIEW

## Syntax

```sql
CREATE
    [OR REPLACE]
    [ALGORITHM = {UNDEFINED | MERGE | TEMPTABLE}]
    [DEFINER = { user | CURRENT_USER | role | CURRENT_ROLE }]
    [SQL SECURITY { DEFINER | INVOKER }]
    VIEW [IF NOT EXISTS] view_name [(column_list)]
    AS select_statement
    [WITH [CASCADED | LOCAL] CHECK OPTION]
```

## Description

The CREATE VIEW statement creates a new [view](./), or replaces an existing\
one if the OR REPLACE clause is given. If the view does not exist, CREATE OR\
REPLACE VIEW is the same as CREATE VIEW. If the view does exist, CREATE OR\
REPLACE VIEW is the same as [ALTER VIEW](alter-view.md).

The select\_statement is a [SELECT](../../reference/sql-statements/data-manipulation/selecting-data/select.md) statement that provides the definition of\
the view. (When you select from the view, you select in effect using the SELECT\
statement.) select\_statement can select from base tables or other views.

The view definition is "frozen" at creation time, so changes to the underlying\
tables afterwards do not affect the view definition. For example, if a view is\
defined as SELECT \* on a table, new columns added to the table later do not\
become part of the view. A [SHOW CREATE VIEW](../../reference/sql-statements/administrative-sql-statements/show/show-create-view.md) shows that\
such queries are rewritten and column names are included in the view\
definition.

The view definition must be a query that does not return errors at view\
creation times. However, the base tables used by the views might be altered\
later and the query may not be valid anymore. In this case, querying the view\
will result in an error. [CHECK TABLE](../../reference/sql-statements/table-statements/check-table.md) helps in finding this kind\
of problems.

The [ALGORITHM clause](view-algorithms.md) affects how MariaDB processes the\
view. The DEFINER and SQL SECURITY clauses specify the security context to be\
used when checking access privileges at view invocation time. The WITH CHECK\
OPTION clause can be given to constrain inserts or updates to rows in tables\
referenced by the view. These clauses are described later in this section.

The CREATE VIEW statement requires the CREATE VIEW privilege for the\
view, and some privilege for each column selected by the SELECT\
statement. For columns used elsewhere in the SELECT statement you must\
have the SELECT privilege. If the OR REPLACE clause is present, you\
must also have the DROP privilege for the view.

A view belongs to a database. By default, a new view is created in the\
default database. To create the view explicitly in a given database,\
specify the name as db\_name.view\_name when you create it.

```sql
CREATE VIEW test.v AS SELECT * FROM t;
```

Base tables and views share the same namespace within a database, so a\
database cannot contain a base table and a view that have the same\
name.

Views must have unique column names with no duplicates, just like base\
tables. By default, the names of the columns retrieved by the SELECT\
statement are used for the view column names. To define explicit names\
for the view columns, the optional column\_list clause can be given as\
a list of comma-separated identifiers. The number of names in\
column\_list must be the same as the number of columns retrieved by the\
SELECT statement.

Columns retrieved by the SELECT statement can be simple references to\
table columns. They can also be expressions that use functions,\
constant values, operators, and so forth.

Unqualified table or view names in the SELECT statement are\
interpreted with respect to the default database. A view can refer to\
tables or views in other databases by qualifying the table or view\
name with the proper database name.

A view can be created from many kinds of SELECT statements. It can\
refer to base tables or other views. It can use joins, UNION, and\
subqueries. The SELECT need not even refer to any tables. The\
following example defines a view that selects two columns from another\
table, as well as an expression calculated from those columns:

```sql
CREATE TABLE t (qty INT, price INT);

INSERT INTO t VALUES(3, 50);

CREATE VIEW v AS SELECT qty, price, qty*price AS value FROM t;

SELECT * FROM v;
+------+-------+-------+
| qty  | price | value |
+------+-------+-------+
|    3 |    50 |   150 |
+------+-------+-------+
```

A view definition is subject to the following restrictions:

* The SELECT statement cannot contain a subquery in the FROM clause.
* The SELECT statement cannot refer to system or user variables.
* Within a stored program, the definition cannot refer to program parameters or local variables.
* The SELECT statement cannot refer to prepared statement parameters.
* Any table or view referred to in the definition must exist. However, after a view has been created, it is possible to drop a table or view that the definition refers to. In this case, use of the view results in an error. To check a view definition for problems of this kind, use the CHECK TABLE statement.
* The definition cannot refer to a TEMPORARY table, and you cannot create a TEMPORARY view.
* Any tables named in the view definition must exist at definition time.
* You cannot associate a trigger with a view.
* For valid identifiers to use as view names, see [Identifier Names](../../reference/sql-structure/sql-language-structure/identifier-names.md).

ORDER BY is allowed in a view definition, but it is ignored if you\
select from a view using a statement that has its own ORDER BY.

For other options or clauses in the definition, they are added to the\
options or clauses of the statement that references the view, but the\
effect is undefined. For example, if a view definition includes a\
LIMIT clause, and you select from the view using a statement that has\
its own LIMIT clause, it is undefined which limit applies. This same\
principle applies to options such as ALL, DISTINCT, or\
SQL\_SMALL\_RESULT that follow the SELECT keyword, and to clauses such\
as INTO, FOR UPDATE, and LOCK IN SHARE MODE.

The PROCEDURE clause cannot be used in a view definition, and it cannot be used if a view is referenced in the FROM clause.

If you create a view and then change the query processing environment\
by changing system variables, that may affect the results that you get\
from the view:

```sql
CREATE VIEW v (mycol) AS SELECT 'abc';

SET sql_mode = '';

SELECT "mycol" FROM v;
+-------+
| mycol |
+-------+
| mycol | 
+-------+

SET sql_mode = 'ANSI_QUOTES';

SELECT "mycol" FROM v;
+-------+
| mycol |
+-------+
| abc   | 
+-------+
```

The DEFINER and SQL SECURITY clauses determine which MariaDB account to\
use when checking access privileges for the view when a statement is\
executed that references the view. They were added in MySQL 5.1.2.\
The legal SQL SECURITY characteristic values are DEFINER and INVOKER.\
These indicate that the required privileges must be held by the user\
who defined or invoked the view, respectively. The default SQL\
SECURITY value is DEFINER.

If a user value is given for the DEFINER clause, it should be a MariaDB\
account in 'user\_name'@'host\_name' format (the same format used in the\
GRANT statement). The user\_name and host\_name values both are\
required. The definer can also be given as CURRENT\_USER or\
CURRENT\_USER(). The default DEFINER value is the user who executes the\
CREATE VIEW statement. This is the same as specifying DEFINER =\
CURRENT\_USER explicitly.

If you specify the DEFINER clause, these rules determine the legal\
DEFINER user values:

* If you do not have the [SUPER](../../reference/sql-statements/account-management-sql-statements/grant.md#super) privilege, or, from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1052-release-notes), the [SET USER](../../reference/sql-statements/account-management-sql-statements/grant.md#set-user) privilege, the only legal user value is your own account, either specified literally or by using CURRENT\_USER. You cannot set the definer to some other account.
* If you have the [SUPER](../../reference/sql-statements/account-management-sql-statements/grant.md#super) privilege, or, from [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1052-release-notes), the [SET USER](../../reference/sql-statements/account-management-sql-statements/grant.md#set-user) privilege, you can specify any syntactically legal account name. If the account does not actually exist, a warning is generated.
* If the SQL SECURITY value is DEFINER but the definer account does not exist when the view is referenced, an error occurs.

Within a view definition, CURRENT\_USER returns the view's DEFINER\
value by default. For views\
defined with the SQL SECURITY INVOKER characteristic, CURRENT\_USER\
returns the account for the view's invoker. For information about user\
auditing within views, see [account-activity-auditing.html](https://dev.mysql.com/doc/refman/5.1/en/account-activity-auditing.html).

Within a stored routine that is defined with the SQL SECURITY DEFINER\
characteristic, CURRENT\_USER returns the routine's DEFINER value. This\
also affects a view defined within such a program, if the view\
definition contains a DEFINER value of CURRENT\_USER.

View privileges are checked like this:

* At view definition time, the view creator must have the privileges needed to use the top-level objects accessed by the view. For example, if the view definition refers to table columns, the creator must have privileges for the columns, as described previously. If the definition refers to a stored function, only the privileges needed to invoke the function can be checked. The privileges required when the function runs can be checked only as it executes: For different invocations of the function, different execution paths within the function might be taken.
* When a view is referenced, privileges for objects accessed by the view are checked against the privileges held by the view creator or invoker, depending on whether the SQL SECURITY characteristic is DEFINER or INVOKER, respectively.
* If reference to a view causes execution of a stored function, privilege checking for statements executed within the function depend on whether the function is defined with a SQL SECURITY characteristic of DEFINER or INVOKER. If the security characteristic is DEFINER, the function runs with the privileges of its creator. If the characteristic is INVOKER, the function runs with the privileges determined by the view's SQL SECURITY characteristic.

Example: A view might depend on a stored function, and that function\
might invoke other stored routines. For example, the following view\
invokes a stored function f():

```sql
CREATE VIEW v AS SELECT * FROM t WHERE t.id = f(t.name);

Suppose that f() contains a statement such AS this:

IF name IS NULL THEN
  CALL p1();
ELSE
  CALL p2();
END IF;
```

The privileges required for executing statements within f() need to be\
checked when f() executes. This might mean that privileges are needed\
for p1() or p2(), depending on the execution path within f(). Those\
privileges must be checked at runtime, and the user who must possess\
the privileges is determined by the SQL SECURITY values of the view v\
and the function f().

The DEFINER and SQL SECURITY clauses for views are extensions to\
standard SQL. In standard SQL, views are handled using the rules for\
SQL SECURITY INVOKER.

If you invoke a view that was created before MySQL 5.1.2, it is\
treated as though it was created with a SQL SECURITY DEFINER clause\
and with a DEFINER value that is the same as your account. However,\
because the actual definer is unknown, MySQL issues a warning. To make\
the warning go away, it is sufficient to re-create the view so that\
the view definition includes a DEFINER clause.

The optional ALGORITHM clause is an extension to standard SQL. It\
affects how MariaDB processes the view. ALGORITHM takes three values:\
MERGE, TEMPTABLE, or UNDEFINED. The default algorithm is UNDEFINED if\
no ALGORITHM clause is present. See [View Algorithms](view-algorithms.md) for more information.

Some views are updatable. That is, you can use them in statements such\
as UPDATE, DELETE, or INSERT to update the contents of the underlying\
table. For a view to be updatable, there must be a one-to-one\
relationship between the rows in the view and the rows in the\
underlying table. There are also certain other constructs that make a\
view non-updatable. See [Inserting and Updating with Views](inserting-and-updating-with-views.md).

### WITH CHECK OPTION

The WITH CHECK OPTION clause can be given for an updatable view to\
prevent inserts or updates to rows except those for which the WHERE\
clause in the select\_statement is true.

In a WITH CHECK OPTION clause for an updatable view, the LOCAL and\
CASCADED keywords determine the scope of check testing when the view\
is defined in terms of another view. The LOCAL keyword restricts the\
CHECK OPTION only to the view being defined. CASCADED causes the\
checks for underlying views to be evaluated as well. When neither\
keyword is given, the default is CASCADED.

For more information about updatable views and the WITH CHECK OPTION\
clause, see [Inserting and Updating with Views](inserting-and-updating-with-views.md).

### IF NOT EXISTS

When the IF NOT EXISTS clause is used, MariaDB will return a warning instead of an error if the specified view already exists. Cannot be used together with the `OR REPLACE` clause.

### Atomic DDL

**MariaDB starting with** [**10.6.1**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1061-release-notes)

[MariaDB 10.6.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1061-release-notes) supports [Atomic DDL](../../reference/sql-statements/data-definition/atomic-ddl.md) and `CREATE VIEW` is atomic.

## Examples

```sql
CREATE TABLE t (a INT, b INT) ENGINE = InnoDB;

INSERT INTO t VALUES (1,1), (2,2), (3,3);

CREATE VIEW v AS SELECT a, a*2 AS a2 FROM t;

SELECT * FROM v;
+------+------+
| a    | a2   |
+------+------+
|    1 |    2 |
|    2 |    4 |
|    3 |    6 |
+------+------+
```

OR REPLACE and IF NOT EXISTS:

```sql
CREATE VIEW v AS SELECT a, a*2 AS a2 FROM t;
ERROR 1050 (42S01): Table 'v' already exists

CREATE OR REPLACE VIEW v AS SELECT a, a*2 AS a2 FROM t;
Query OK, 0 rows affected (0.04 sec)

CREATE VIEW IF NOT EXISTS v AS SELECT a, a*2 AS a2 FROM t;
Query OK, 0 rows affected, 1 warning (0.01 sec)

SHOW WARNINGS;
+-------+------+--------------------------+
| Level | Code | Message                  |
+-------+------+--------------------------+
| Note  | 1050 | Table 'v' already exists |
+-------+------+--------------------------+
```

## See Also

* [Identifier Names](../../reference/sql-structure/sql-language-structure/identifier-names.md)
* [ALTER VIEW](alter-view.md)
* [DROP VIEW](drop-view.md)
* [SHOW CREATE VIEWS](../../reference/sql-statements/administrative-sql-statements/show/show-create-view.md)
* [INFORMATION SCHEMA VIEWS Table](information-schema-views-table.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
