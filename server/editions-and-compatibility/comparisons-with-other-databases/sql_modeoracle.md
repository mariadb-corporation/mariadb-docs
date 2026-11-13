---
description: >-
  Documentation for the ORACLE SQL mode, which provides extensive
  compatibility with Oracle Database PL/SQL syntax, data types, and sequences,
  facilitating migration.
---

# SQL\_MODE=ORACLE

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/Dn7q74OYovrrC5l3cYgb/" %}

MariaDB's `SQL_MODE = ORACLE` setting enables compatibility with Oracle Database SQL syntax and behavior in MariaDB. This feature is particularly useful for organizations looking to migrate applications from Oracle Database to MariaDB while preserving the behavior and syntax of Oracle SQL. By setting the [sql\_mode](../../server-management/variables-and-modes/sql_mode.md) to `ORACLE`, developers can ensure that their existing SQL scripts, application logic, and database interactions are compatible with MariaDB's behavior, easing the migration process. This page provides detailed information on supported Oracle SQL syntax, behavior differences between Oracle and MariaDB, and tips for adapting applications and scripts to work smoothly under this mode.

```sql
SET SQL_MODE='ORACLE';
```

All traditional MariaDB SQL/PSM syntax should work as before, as long as it does not conflict with Oracle's PL/SQL syntax. All MariaDB functions should be supported in both normal and Oracle modes.

`SET SQL_MODE=ORACLE` is the same as:

```sql
SET SQL_MODE='PIPES_AS_CONCAT,ANSI_QUOTES,IGNORE_SPACE,ORACLE,NO_KEY_OPTIONS,
NO_TABLE_OPTIONS,NO_FIELD_OPTIONS,NO_AUTO_CREATE_USER,SIMULTANEOUS_ASSIGNMENT';
```

## Supported Syntax in Oracle Mode

### Stored Procedures and Stored Functions

Oracle mode makes the following changes to [Stored Procedures](../../server-usage/stored-routines/stored-procedures/README.md) and [Stored Functions](../../server-usage/stored-routines/stored-functions/README.md):

| Oracle syntax                                                  | Description                                                                                                                                                                                                                                                                                    |
| -------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CREATE PROCEDURE p1 (param OUT INT)`                          | ANSI uses `(OUT param INT)`                                                                                                                                                                                                                                                                    |
| `CREATE PROCEDURE p1 (a IN OUT INT)`                           | ANSI uses `(INOUT param INT)`                                                                                                                                                                                                                                                                  |
| `AS` before function body                                      | `CREATE FUNCTION f1 RETURN NUMBER AS BEGIN...`                                                                                                                                                                                                                                                 |
| `IS` before function body                                      | `CREATE FUNCTION f1 RETURN NUMBER IS BEGIN...`                                                                                                                                                                                                                                                 |
| If function has no parameters then parentheses must be omitted | Example: `CREATE PROCEDURE p1 AS BEGIN NULL; END;`                                                                                                                                                                                                                                             |
| `CREATE PROCEDURE p1 AS BEGIN END p1;`                         | Optional routine name after `END` keyword. [MDEV-12089](https://jira.mariadb.org/browse/MDEV-12089)                                                                                                                                                                                            |
| `CREATE FUNCTION f1(a VARCHAR)`                                | [VARCHAR](../../reference/data-types/string-data-types/varchar.md) can be used without length for routine parameters and RETURN clause. The length is inherited from the argument at call time. [MDEV-10596](https://jira.mariadb.org/browse/MDEV-10596) |
| `CREATE AGGREGATE FUNCTION f1( )`                              | Creates an [aggregate function](../../server-usage/stored-routines/stored-functions/stored-aggregate-functions.md), which performs the function against a set of rows and returns one aggregate result.                                                  |
| No `CALL` needed in Stored Procedures                          | In Oracle mode one can call other stored procedures with name only. [MDEV-12107](https://jira.mariadb.org/browse/MDEV-12107)                                                                                                                                                                   |
| `RETURN`. Can also be used in stored procedures                | ANSI uses `RETURNS`. MariaDB mode only supports `RETURNS` in stored functions                                                                                                                                                                                                                  |

### Cursors

Oracle mode makes the following changes to [Cursors](../../reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-cursors/README.md):

| Oracle syntax                                                                          | Description                                                                                                                                                                                                                                                                         |
| -------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `CREATE PROCEDURE p1 AS CURSOR cur IS (SELECT a, b FROM t1); BEGIN FOR rec IN cur ...` | Explicit cursor with [FOR loop](../../reference/sql-statements/programmatic-compound-statements/for.md). [MDEV-10581](https://jira.mariadb.org/browse/MDEV-10581)                                                                             |
| `CREATE PROCEDURE p1 AS rec IN (SELECT a, b FROM t1)`                                  | Implicit cursor with [FOR loop](../../reference/sql-statements/programmatic-compound-statements/for.md). [MDEV-12098](https://jira.mariadb.org/browse/MDEV-12098)                                                                             |
| `CURSOR c(prm_a VARCHAR2, prm_b VARCHAR2) ... OPEN c(1,2)`                             | Cursor with parameters. [MDEV-10597](https://jira.mariadb.org/browse/MDEV-10597)                                                                                                                                                                                                    |
| `CURSOR c(prm_a VARCHAR2, prm_b VARCHAR2) ... FOR rec in c(1,2)`                       | Cursor with parameters and [FOR loop](../../reference/sql-statements/programmatic-compound-statements/for.md). [MDEV-12314](https://jira.mariadb.org/browse/MDEV-12314)                                                                       |
| `s %ISOPEN, %ROWCOUNT, %FOUND, %NOTFOUND`                                              | Explicit cursor attributes. [MDEV-10582](https://jira.mariadb.org/browse/MDEV-10582)                                                                                                                                                                                                |
| `TYPE type_name IS REF CURSOR [ RETURN return_type ]`                                  | Declares as `REF CURSOR` (cursor variable). Supports weak and strong types. See [DECLARE TYPE](../../reference/sql-statements/programmatic-compound-statements/declare-type.md) and [MDEV-10152](https://jira.mariadb.org/browse/MDEV-10152). |

### LOOP

Oracle mode makes the following changes to [LOOP](../../reference/sql-statements/programmatic-compound-statements/loop.md):

| Oracle syntax                                                                 | Description                                                                                                                                                                                |
| ----------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `FOR i IN 1..10 LOOP ... END LOOP`                                            | Numeric [FOR loop](../../reference/sql-statements/programmatic-compound-statements/for.md). [MDEV-10580](https://jira.mariadb.org/browse/MDEV-10580) |
| `GOTO`                                                                        | [GOTO statement](../../reference/sql-statements/programmatic-compound-statements/goto.md). [MDEV-10697](https://jira.mariadb.org/browse/MDEV-10697)  |
| `<<label>>` used with GOTO                                                    | ANSI uses `label:`. [MDEV-10697](https://jira.mariadb.org/browse/MDEV-10697)                                                                                                               |
| To leave loop block: `EXIT [ label ] [ WHEN bool_expr ]`                      | ANSI syntax is `IF bool_expr THEN LEAVE label`                                                                                                                                             |
| `[<<label>>] WHILE boolean_expression LOOP statement... END LOOP [ label ] ;` | Oracle style `WHILE` loop                                                                                                                                                                  |
| `CONTINUE [ label ] [ WHEN boolean_expression]`                               | `CONTINUE` is only valid inside a loop                                                                                                                                                     |

### Variables

| Oracle syntax                                                                                                                     | Description                                                                                                                                                                                                         |
| --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `var:= 10;` Can also be used with MariaDB system variables                                                                        | MariaDB uses `SET var= 10;`                                                                                                                                                                                         |
| `var INT := 10`                                                                                                                   | Default variable value                                                                                                                                                                                              |
| `var1 table_name.column_name%TYPE`                                                                                                | Take data type from a table column. [MDEV-10577](https://jira.mariadb.org/browse/MDEV-10577)                                                                                                                        |
| `var2 var1%TYPE`                                                                                                                  | Take data type from another variable                                                                                                                                                                                |
| `rec1 table_name%ROWTYPE`                                                                                                         | Take ROW structure from a table. [MDEV-12133](https://jira.mariadb.org/browse/MDEV-12133)                                                                                                                           |
| `rec2 rec1%ROWTYPE`                                                                                                               | Take ROW structure from ROW variable                                                                                                                                                                                |
| `CURSOR c1 IS SELECT a,b FROM t1; rec1 c1%ROWTYPE;`                                                                               | Take ROW structure from a cursor. [MDEV-12011](https://jira.mariadb.org/browse/MDEV-12011)                                                                                                                          |
| Variables can be declared after cursor declarations                                                                               | In MariaDB mode, variables must be declared before cursors. [MDEV-10598](https://jira.mariadb.org/browse/MDEV-10598)                                                                                                |
| Triggers uses `:NEW` and `:OLD`                                                                                                   | ANSI uses NEW and OLD. [MDEV-10579](https://jira.mariadb.org/browse/MDEV-10579)                                                                                                                                     |
| `SQLCODE`                                                                                                                         | Returns the number code of the most recent exception. Can only be used in Stored Procedures. [MDEV-10578](https://jira.mariadb.org/browse/MDEV-10578)                                                               |
| `SQLERRM`                                                                                                                         | Returns the error message associated to it's error number argument or `SQLCODE` if no argument is given. Can only be used in Stored Procedures. [MDEV-10578](https://jira.mariadb.org/browse/MDEV-10578)           |
| `SQL%ROWCOUNT`                                                                                                                    | Almost same as [ROW\_COUNT()](../../reference/sql-functions/secondary-functions/information-functions/row_count.md). [MDEV-10583](https://jira.mariadb.org/browse/MDEV-10583) |
| [ROWNUM](../../reference/sql-functions/secondary-functions/information-functions/rownum.md) | Returns number of accepted rows. From [MariaDB 10.6](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/what-is-mariadb-106).                                                                                                                            |
| Associative arrays                                                                                                                | See [blog post](https://mariadb.org/bringing-oracles-associative-arrays-to-mariadb/). From [MariaDB 12.1](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/12.1/changes-and-improvements-in-mariadb-12.1).                                     |

### Exceptions

| Oracle syntax                                                         | Description                                                                                                     |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `BEGIN ... EXCEPTION WHEN OTHERS THEN BEGIN .. END; END;`             | Exception handlers are declared at the end of a block                                                           |
| `TOO_MANY_ROWS, NO_DATA_FOUND, DUP_VAL_ON_INDEX`                      | Predefined exceptions. [MDEV-10839](https://jira.mariadb.org/browse/MDEV-10839)                                 |
| `RAISE TOO_MANY_ROWS ; .... EXCEPTION WHEN TOO_MANY_ROWS THEN ...`    | Exception can be used with RAISE and EXCEPTION...WHEN. [MDEV-10840](https://jira.mariadb.org/browse/MDEV-10840) |
| `CREATE OR REPLACE FUNCTION f1 (a INT) RETURN INT AS e1 EXCEPTION...` | User defined exceptions. [MDEV-10587](https://jira.mariadb.org/browse/MDEV-10587)                               |

### BEGIN Blocks

| Oracle syntax                                                   | Description                                                                                                                                                                                                                         |
| --------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BEGIN` to start a block                                        | MariaDB uses [BEGIN NOT ATOMIC](../../reference/sql-statements/programmatic-compound-statements/begin-end.md) for anyonymous blocks. [MDEV-10655](https://jira.mariadb.org/browse/MDEV-10655) |
| `DECLARE` is used before `BEGIN`                                | `DECLARE a INT; b VARCHAR(10); BEGIN v:= 10; END;`                                                                                                                                                                                  |
| `WHEN DUP_VAL_ON_INDEX THEN NULL ; NULL; WHEN OTHERS THEN NULL` | Do not require `BEGIN..END` in multi-statement exception handlers in `THEN` clause. [MDEV-12088](https://jira.mariadb.org/browse/MDEV-12088)                                                                                        |

### Simple Syntax Compatibility

<table><thead><tr><th>Oracle syntax</th><th width="72.407470703125">Version</th><th>Description</th></tr></thead><tbody><tr><td><code>ELSIF</code></td><td>10.3</td><td>ANSI uses <a href="../../reference/sql-statements/programmatic-compound-statements/if.md">ELSEIF</a></td></tr><tr><td><code>SELECT UNIQUE</code></td><td>10.3</td><td>Same as <a href="../../reference/sql-statements/data-manipulation/selecting-data/select.md#distinct">SELECT DISTINCT</a>. <a href="https://jira.mariadb.org/browse/MDEV-12086">MDEV-12086</a></td></tr><tr><td><code>TRUNCATE TABLE t1 [DROP STORAGE] or [REUSE STORAGE]</code></td><td>10.3</td><td><code>DROP STORAGE</code> and <code>REUSE STORAGE</code> are allowed as optional keywords for <a href="../../reference/sql-statements/table-statements/truncate-table.md">TRUNCATE TABLE</a>. <a href="https://jira.mariadb.org/browse/MDEV-10588">MDEV-10588</a></td></tr><tr><td><a href="../../reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/subqueries/subqueries-in-a-from-clause-derived-tables.md">Subqueries in a FROM clause</a> without an alias</td><td>10.6</td><td><code>SELECT * FROM (SELECT 1 FROM DUAL), (SELECT 2 FROM DUAL)</code></td></tr><tr><td><a href="../../reference/sql-statements/data-manipulation/selecting-data/set-operations/union.md">UNION</a>, <a href="../../reference/sql-statements/data-manipulation/selecting-data/set-operations/except.md">EXCEPT</a> and <a href="../../reference/sql-statements/data-manipulation/selecting-data/set-operations/intersect.md">INTERSECT</a> all have the same precedence.</td><td>10.3</td><td><a href="../../reference/sql-statements/data-manipulation/selecting-data/set-operations/intersect.md">INTERSECT</a> has higher precedence than <a href="../../reference/sql-statements/data-manipulation/selecting-data/set-operations/union.md">UNION</a> and <a href="../../reference/sql-statements/data-manipulation/selecting-data/set-operations/except.md">EXCEPT</a> in non-Oracle modes.</td></tr><tr><td><code>MINUS</code></td><td>10.6</td><td>MINUS is a synonym for <a href="../../reference/sql-statements/data-manipulation/selecting-data/set-operations/except.md">EXCEPT</a>.</td></tr></tbody></table>

### Functions

<table><thead><tr><th width="286.5926513671875">Oracle syntax</th><th width="84.25927734375">Version</th><th>Description</th></tr></thead><tbody><tr><td><a href="../../reference/sql-functions/date-time-functions/add_months.md">ADD_MONTHS()</a></td><td>10.6.1</td><td>Added as a wrapper for <a href="../../reference/sql-functions/date-time-functions/date_add.md">DATE_ADD()</a> to enhance Oracle compatibility. All modes.</td></tr><tr><td><a href="../../reference/sql-functions/string-functions/cast.md">CAST(expr as VARCHAR(N))</a></td><td>10.3</td><td>Cast expression to a VARCHAR(N). <a href="https://jira.mariadb.org/browse/MDEV-11275">MDEV-11275</a></td></tr><tr><td><a href="../../reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/decode.md">DECODE</a></td><td>10.3</td><td>In Oracle mode, compares and matches search expressions</td></tr><tr><td><code>LENGTH()</code> is same as <a href="../../reference/sql-functions/string-functions/char_length.md">CHAR_LENGTH()</a></td><td>10.3</td><td>MariaDB translates <a href="../../reference/sql-functions/string-functions/length.md">LENGTH()</a> to <a href="../../reference/sql-functions/string-functions/octet_length.md">OCTET_LENGTH()</a>. In all modes one can use LENGTHB() as a synonym to OCTET_LENGTH()</td></tr><tr><td><a href="../../reference/sql-functions/string-functions/chr.md">CHR(num)</a></td><td>10.3</td><td>Returns a <code>VARCHAR(1)</code> with character set and collation according to <code>@@character_set_database</code> and <code>@@collation_database</code></td></tr><tr><td><code>substr('abc',0 ,3) same as substr('abc', 1 ,3)</code></td><td>10.3</td><td>Position <code>0</code> for <a href="../../reference/sql-functions/string-functions/substring.md">substr()</a> is same as position <code>1</code></td></tr><tr><td><a href="../../reference/sql-functions/secondary-functions/miscellaneous-functions/sys_guid.md">SYS_GUID</a></td><td>10.6.1</td><td>Generates a globally unique identifier. Similar to <a href="../../reference/sql-functions/secondary-functions/miscellaneous-functions/uuid.md">UUID</a> but without the <code>-</code>. All modes.</td></tr><tr><td><a href="../../reference/sql-functions/string-functions/to_char.md">TO_CHAR</a></td><td>10.6.1</td><td>Added to enhance Oracle compatibility. All modes.</td></tr><tr><td><a href="../../reference/sql-functions/numeric-functions/to_number.md">TO_NUMBER</a></td><td>12.2.1</td><td>Added to enhance Oracle compatibility. All modes.</td></tr><tr><td><a href="../../reference/sql-functions/string-functions/trim.md">TRIM</a>, <a href="../../reference/sql-functions/string-functions/ltrim.md">LTRIM</a>, <a href="../../reference/sql-functions/string-functions/rtrim.md">RTRIM</a>, <a href="../../reference/sql-functions/string-functions/lpad.md">LPAD</a> and <a href="../../reference/sql-functions/string-functions/rpad.md">RPAD</a></td><td>10.3</td><td>Returns <code>NULL</code> instead of an empty string if returning an empty result. These functions can also be accessed outside of <code>ORACLE</code> mode by suffixing <code>_ORACLE</code> onto the end of the function name, such as <code>TRIM_ORACLE</code>.</td></tr></tbody></table>

### Prepared Statements

Oracle mode makes the following changes to [Prepared Statements](../../reference/sql-statements/prepared-statements/README.md):

| Oracle syntax                                                             | Description                                                                    |
| ------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| `PREPARE stmt FROM 'SELECT :1, :2'`                                       | ANSI uses `?`. [MDEV-10801](https://jira.mariadb.org/browse/MDEV-10801)        |
| `EXECUTE IMMEDIATE 'INSERT INTO t1 SELECT (:x,:y) FROM DUAL' USING 10,20` | Dynamic placeholders. [MDEV-10801](https://jira.mariadb.org/browse/MDEV-10801) |

### Synonyms for Basic SQL Types

| Oracle type                | MariaDB synonym                                                                                                           |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `VARCHAR2`                 | [VARCHAR](../../reference/data-types/string-data-types/varchar.md)                  |
| `NUMBER(M [,D])`           | [DECIMAL(M\[,D\])](../../reference/data-types/numeric-data-types/decimal.md)        |
| `NUMBER`                   | [DOUBLE](../../reference/data-types/numeric-data-types/double.md)                   |
| `DATE` (with time portion) | MariaDB [DATETIME](../../reference/data-types/date-and-time-data-types/datetime.md) |
| `RAW`                      | [VARBINARY](../../reference/data-types/string-data-types/varbinary.md)              |
| `CLOB`                     | [LONGTEXT](../../reference/data-types/string-data-types/longtext.md)                |
| `BLOB`                     | [LONGBLOB](../../reference/data-types/string-data-types/longblob.md)                |

This was implemented as part of [MDEV-10343](https://jira.mariadb.org/browse/MDEV-10343).

If one does a [SHOW CREATE TABLE](../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) in `ORACLE` mode on a table that has a native MariaDB `DATE` column, it will be displayed as [mariadb\_schema.date](../../reference/sql-structure/sql-language-structure/schema-qualifiers.md) to not conflict with the Oracle `DATE` type.

### Packages

The following syntax has been supported since [MariaDB 10.3.5](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.5):

* [CREATE PACKAGE](../../reference/sql-statements/data-definition/create/create-package.md)
* [CREATE PACKAGE BODY](../../reference/sql-statements/data-definition/create/create-package-body.md)
* [DROP PACKAGE](../../reference/sql-statements/data-definition/drop/drop-package.md)
* [DROP PACKAGE BODY](../../reference/sql-statements/data-definition/drop/drop-package-body.md)
* [SHOW CREATE PACKAGE](../../reference/sql-statements/administrative-sql-statements/show/show-create-package.md)
* [SHOW CREATE PACKAGE BODY](../../reference/sql-statements/administrative-sql-statements/show/show-create-package-body.md)

### NULL Handling

Oracle mode makes the following changes to [NULL handling](../../reference/data-types/null-values.md):

#### NULL As a Statement

`NULL` can be used as a statement:

```sql
IF a=10 THEN NULL; ELSE NULL; END IF
```

#### Translating Empty String Literals to NULL

In Oracle, empty string ('') and NULL are the same thing,

By using `sql_mode=EMPTY_STRING_IS_NULL` you can get a similar
experience in MariaDB:

```sql
SET sql_mode=EMPTY_STRING_IS_NULL;
SELECT '' IS NULL; -- returns TRUE
INSERT INTO t1 VALUES (''); -- inserts NULL
```

#### Concat Operator Ignores NULL

[CONCAT()](../../reference/sql-functions/string-functions/concat.md) and [||](../../reference/sql-structure/operators/logical-operators/or.md) ignore NULL in Oracle mode. Can also be accessed outside of ORACLE mode by using CONCAT\_OPERATOR\_ORACLE. [MDEV-11880](https://jira.mariadb.org/browse/MDEV-11880) and [MDEV-12143](https://jira.mariadb.org/browse/MDEV-12143).

### Reserved Words

There are a number of [extra reserved words](../../reference/sql-structure/sql-language-structure/reserved-words.md#oracle-mode) in Oracle mode.

### SHOW CREATE TABLE

The [SHOW CREATE TABLE](../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) statement will not display MariaDB-specific table options, such as AUTO\_INCREMENT or CHARSET, when Oracle mode is set.

## See Also

* [mariadb\_schema](../../reference/sql-structure/sql-language-structure/schema-qualifiers.md)
* [Using SEQUENCEs](../../reference/sql-structure/sequences/README.md)
* [SQL\_MODE](../../server-management/variables-and-modes/sql_mode.md) EMPTY\_STRING\_IS\_NULL
* [SQL\_MODE=MSSQL](sql_modemssql.md)
* [Migration from Oracle to MariaDB with no application change - Pickup Li - FOSDEM 2021](https://www.youtube.com/watch?v=kQXpjCSt1So) (video)
* [A user story: migrating from Oracle to MariaDB - Lixun Peng - MariaDB Server Fest 2020](https://www.youtube.com/watch?v=5pqEZ91zHsA) (video)
* [Curious case of the disappearing commercial databases (13 minute offset) - Monty Widenius - MariaDB Server Fest 2021](https://www.youtube.com/watch?v=0nysJV3pozg) (video)
* [Sqlines - Oracle to MariaDB migration tool](https://sqlines.com/oracle-to-mariadb)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formid="4316" formId="4316" %}
