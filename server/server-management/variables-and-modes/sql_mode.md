# SQL\_MODE

MariaDB supports several different modes which allow you to tune it to suit your needs.

The most important ways for doing this are using `SQL_MODE` (controlled by the [sql\_mode](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_mode) system variable) and [OLD\_MODE](old_mode.md) (the [old\_mode](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#old_mode) system variable). `SQL_MODE` is used for getting MariaDB to emulate behavior from other SQL servers, while [OLD\_MODE](old_mode.md) is used for emulating behavior from older MariaDB or MySQL versions.

`SQL_MODE`is a string with different options separated by commas ('`,`') without spaces. The options are case insensitive.

You can check the local and global value of it with:

```sql
SELECT @@SQL_MODE, @@GLOBAL.SQL_MODE;
```

## Setting SQL\_MODE

### Defaults

| From version                                                                                                                                                     | Default sql\_mode setting                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes)      | STRICT\_TRANS\_TABLES, ERROR\_FOR\_DIVISION\_BY\_ZERO , NO\_AUTO\_CREATE\_USER, NO\_ENGINE\_SUBSTITUTION |
| [MariaDB 10.1.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-7-release-notes)    | NO\_ENGINE\_SUBSTITUTION, NO\_AUTO\_CREATE\_USER                                                         |
| <= [MariaDB 10.1.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-6-release-notes) | No value                                                                                                 |

You can set the `SQL_MODE` either from the [command line](../starting-and-stopping-mariadb/mariadbd-options.md) (the `--sql-mode` option) or by setting the [sql\_mode](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_mode) system variable.

```sql
SET sql_mode = 'modes';
SET GLOBAL sql_mode = 'modes';
```

The session value only affects the current client, and can be changed by the client when required. To set the global value, the SUPER privilege is required, and the change affects any clients that connect from that point on.

## SQL\_MODE Values

The different `SQL_MODE` values are:

#### ALLOW\_INVALID\_DATES

Allow any day between 1-31 in the day part. This is convenient when you want to read in all (including wrong data) into the database and then manipulate it there.

Note, that MariaDB assumes that table content matches the current setting of this mode. If you enable it, insert some invalid dates into the table and then disable it for a session, the result will be not well defined — some queries might return invalid dates, while other will not.

#### ANSI

Changes the SQL syntax to be closer to ANSI SQL.

Sets: [REAL\_AS\_FLOAT](sql_mode.md#real_as_float), [PIPES\_AS\_CONCAT](sql_mode.md#pipes_as_concat), [ANSI\_QUOTES](sql_mode.md#ansi_quotes), [IGNORE\_SPACE](sql_mode.md#ignore_space).

It also adds a restriction: an error will be returned if a subquery uses an [aggregating function](../../reference/sql-functions/aggregate-functions/) with a reference to a column from an outer query in a way that cannot be resolved.

If set, [SHOW CREATE TABLE](../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) output will not display MariaDB-specific table attributes.

#### ANSI\_QUOTES

Changes `"` to be treated as \`\`\`, the identifier quote character. This may break old MariaDB applications which assume that `"` is used as a string quote character.

#### DB2

Same as: [PIPES\_AS\_CONCAT](sql_mode.md#pipes_as_concat), [ANSI\_QUOTES](sql_mode.md#ansi_quotes) , [IGNORE\_SPACE](sql_mode.md#ignore_space), [DB2](sql_mode.md#db2), [NO\_KEY\_OPTIONS](sql_mode.md#no_key_options), [NO\_TABLE\_OPTIONS](sql_mode.md#no_table_options), [NO\_FIELD\_OPTIONS](sql_mode.md#no_field_options)

If set, [SHOW CREATE TABLE](../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) output will not display MariaDB-specific table attributes.

#### EMPTY\_STRING\_IS\_NULL

Oracle-compatibility option that translates Item\_string created in the parser to Item\_null, and translates binding an empty string as prepared statement parameters to binding NULL. For example, `SELECT '' IS NULL` returns TRUE, `INSERT INTO t1 VALUES ('')` inserts NULL. Since [MariaDB 10.3.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1033-release-notes)

#### ERROR\_FOR\_DIVISION\_BY\_ZERO

If not set, division by zero returns NULL. If set returns an error if one tries to update a column with 1/0 and returns a warning as well. Also see [MDEV-8319](https://jira.mariadb.org/browse/MDEV-8319). Default since [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes).

#### HIGH\_NOT\_PRECEDENCE

Compatibility option for MySQL 5.0.1 and before; This changes `NOT a BETWEEN b AND c` to be parsed as `(NOT a) BETWEEN b AND c`

#### IGNORE\_BAD\_TABLE\_OPTIONS

If this is set generate a warning (not an error) for wrong table option in CREATE TABLE. Also, since 10.0.13, do not comment out these wrong table options in [SHOW CREATE TABLE](../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md).

#### IGNORE\_SPACE

Allow one to have spaces (including tab characters and new line characters) between function name and '('. The drawback is that this causes built in functions to become [reserved words](../../reference/sql-structure/sql-language-structure/reserved-words.md).

#### MAXDB

Same as: [PIPES\_AS\_CONCAT](sql_mode.md#pipes_as_concat), [ANSI\_QUOTES](sql_mode.md#ansi_quotes), [IGNORE\_SPACE](sql_mode.md#ignore_space), [MAXDB](sql_mode.md#maxdb), [NO\_KEY\_OPTIONS](sql_mode.md#no_key_options), [NO\_TABLE\_OPTIONS](sql_mode.md#no_table_options), [NO\_FIELD\_OPTIONS](sql_mode.md#no_field_options), [NO\_AUTO\_CREATE\_USER](sql_mode.md#no_auto_create_user).

Also has the effect of silently converting [TIMESTAMP](../../reference/data-types/date-and-time-data-types/timestamp.md) fields into [DATETIME](../../reference/data-types/date-and-time-data-types/datetime.md) fields when created or modified.

If set, [SHOW CREATE TABLE](../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) output will not display MariaDB-specific table attributes.

#### MSSQL

Additionally implies the following: [PIPES\_AS\_CONCAT](sql_mode.md#pipes_as_concat), [ANSI\_QUOTES](sql_mode.md#ansi_quotes), [IGNORE\_SPACE](sql_mode.md#ignore_space), [NO\_KEY\_OPTIONS](sql_mode.md#no_key_options), [NO\_TABLE\_OPTIONS](sql_mode.md#no_table_options), [NO\_FIELD\_OPTIONS](sql_mode.md#no_field_options).

Additionally from [MariaDB 10.4.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1045-release-notes), implements a limited subset of Microsoft SQL Server's language. See [SQL\_MODE=MSSQL](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modemssql) for more.

If set, [SHOW CREATE TABLE](../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) output will not display MariaDB-specific table attributes.

#### MYSQL323

Same as: [NO\_FIELD\_OPTIONS](sql_mode.md#no_field_options), [HIGH\_NOT\_PRECEDENCE](sql_mode.md#high_not_precedence).

#### MYSQL40

Same as: [NO\_FIELD\_OPTIONS](sql_mode.md#no_field_options), [HIGH\_NOT\_PRECEDENCE](sql_mode.md#high_not_precedence).

#### NO\_AUTO\_CREATE\_USER

Don't automatically create users with `GRANT` unless authentication information is specified. If none is provided, will produce a 1133 error: "Can't find any matching row in the user table". Default since [MariaDB 10.1.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-7-release-notes).

#### NO\_AUTO\_VALUE\_ON\_ZERO

If set, don't generate an [AUTO\_INCREMENT](../../reference/data-types/auto_increment.md) on [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) of zero in an `AUTO_INCREMENT` column, or when adding an [AUTO\_INCREMENT](../../reference/data-types/auto_increment.md) attribute with the [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table/) statement. Normally both `zero` and `NULL` generate new `AUTO_INCREMENT` values.

#### NO\_BACKSLASH\_ESCAPES

Disables using the backslash character `\` as an escape character within strings, making it equivalent to an ordinary character.

#### NO\_DIR\_IN\_CREATE

Ignore all INDEX DIRECTORY and DATA DIRECTORY directives when creating a table. Can be useful on [replica](../../server-usage/storage-engines/myrocks/myrocks-and-replication.md) servers.

#### NO\_ENGINE\_SUBSTITUTION

If not set, if the available storage engine specified by a CREATE TABLE or ALTER TABLE is not available, a warning is given and the default storage engine is used instead. If set, generate a 1286 error when creating a table if the specified [storage engine](../../server-usage/storage-engines/) is not available. See also [enforce\_storage\_engine](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#enforce_storage_engine). Default since [MariaDB 10.1.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-7-release-notes).

#### NO\_FIELD\_OPTIONS

Remove MariaDB-specific column options from the output of [SHOW CREATE TABLE](../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md). This is also used by the portability mode of [mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md).

#### NO\_KEY\_OPTIONS

Remove MariaDB-specific index options from the output of [SHOW CREATE TABLE](../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md). This is also used by the portability mode of [mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md).

#### NO\_TABLE\_OPTIONS

Remove MariaDB-specific table options from the output of [SHOW CREATE TABLE](../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md). This is also used by the portability mode of [mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md).

#### NO\_UNSIGNED\_SUBTRACTION

When enabled, subtraction results are signed even if the operands are unsigned.

#### NO\_ZERO\_DATE

Don't allow '0000-00-00' as a valid date in strict mode (produce a 1525 error). Zero dates can be inserted with [IGNORE](../../reference/sql-statements/data-manipulation/inserting-loading-data/ignore.md). If not in strict mode, a warning is generated.

#### NO\_ZERO\_IN\_DATE

Don't allow dates where the year is not zero but the month or day parts of the date _are_ zero (produce a 1525 error). For example, with this set, '0000-00-00' is allowed, but '1970-00-10' or '1929-01-00' are not. If the ignore option is used, MariaDB will insert '0000-00-00' for those types of dates. If not in strict mode, a warning is generated instead.

#### ONLY\_FULL\_GROUP\_BY

For [SELECT ... GROUP BY](../../reference/sql-statements/data-manipulation/selecting-data/select.md#group-by) queries, disallow [SELECTing](../../reference/sql-statements/data-manipulation/selecting-data/select.md) columns which are not referred to in the GROUP BY clause, unless they are passed to an aggregate function like [COUNT()](../../reference/sql-functions/aggregate-functions/count.md) or [MAX()](../../reference/sql-functions/aggregate-functions/max.md). Produce a 1055 error.

#### ORACLE

In all versions of MariaDB up to [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102), this sets `sql_mode` that is equivalent to: [PIPES\_AS\_CONCAT](sql_mode.md#pipes_as_concat), [ANSI\_QUOTES](sql_mode.md#ansi_quotes), [IGNORE\_SPACE](sql_mode.md#ignore_space), [NO\_KEY\_OPTIONS](sql_mode.md#no_key_options), [NO\_TABLE\_OPTIONS](sql_mode.md#no_table_options), [NO\_FIELD\_OPTIONS](sql_mode.md#no_field_options), [NO\_AUTO\_CREATE\_USER](sql_mode.md#no_auto_create_user)

From [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/what-is-mariadb-103), this mode also sets [SIMULTANEOUS\_ASSIGNMENT](sql_mode.md#simultaneous_assignment) and configures the server to understand a large subset of Oracle's PL/SQL language instead of MariaDB's traditional syntax for stored routines. See [SQL\_MODE=ORACLE From MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle).

If set, [SHOW CREATE TABLE](../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) output will not display MariaDB-specific table attributes.

#### PAD\_CHAR\_TO\_FULL\_LENGTH

Trailing spaces in [CHAR](../../reference/data-types/string-data-types/char.md) columns are by default trimmed upon retrieval. With PAD\_CHAR\_TO\_FULL\_LENGTH enabled, no trimming occurs. Does not apply to [VARCHARs](../../reference/data-types/string-data-types/varchar.md).

#### PIPES\_AS\_CONCAT

Allows using the pipe character (ASCII 124) as string concatenation operator. This means that `"A" || "B"` can be used in place of `CONCAT("A", "B")`.

#### POSTGRESQL

Same as: [PIPES\_AS\_CONCAT](sql_mode.md#pipes_as_concat), [ANSI\_QUOTES](sql_mode.md#ansi_quotes), [IGNORE\_SPACE](sql_mode.md#ignore_space), [POSTGRESQL](sql_mode.md#postgresql), [NO\_KEY\_OPTIONS](sql_mode.md#no_key_options), [NO\_TABLE\_OPTIONS](sql_mode.md#no_table_options), [NO\_FIELD\_OPTIONS](sql_mode.md#no_field_options).

If set, [SHOW CREATE TABLE](../../reference/sql-statements/administrative-sql-statements/show/show-create-table.md) output will not display MariaDB-specific table attributes.

#### REAL\_AS\_FLOAT

`REAL` is a synonym for [FLOAT](../../reference/data-types/numeric-data-types/float.md) rather than [DOUBLE](../../reference/data-types/numeric-data-types/double.md).

#### SIMULTANEOUS\_ASSIGNMENT

Setting this makes the SET part of the [UPDATE](../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) statement evaluate all assignments simultaneously, not left-to-right. From [MariaDB 10.3.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-1035-release-notes).

#### STRICT\_ALL\_TABLES

Strict mode. Statements with invalid or missing data are aborted and rolled back. For a non-transactional storage engine with a statement affecting multiple rows, this may mean a partial insert or update if the error is found in a row beyond the first.

#### STRICT\_TRANS\_TABLES

Strict mode. Statements with invalid or missing data are aborted and rolled back, except that for non-transactional storage engines and statements affecting multiple rows where the invalid or missing data is not the first row, MariaDB will convert the invalid value to the closest valid value, or, if a value is missing, insert the column default value. Default since [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes).

#### TIME\_ROUND\_FRACTIONAL

With this mode unset, MariaDB truncates fractional seconds when changing precision to smaller. When set, MariaDB will round when converting to TIME, DATETIME and TIMESTAMP, and truncate when converting to DATE. Since [MariaDB 10.4.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-1041-release-notes)

#### TRADITIONAL

Makes MariaDB work like a traditional SQL server. Same as: [STRICT\_TRANS\_TABLES](sql_mode.md#strict_trans_tables), [STRICT\_ALL\_TABLES](sql_mode.md#strict_all_tables), [NO\_ZERO\_IN\_DATE](sql_mode.md#no_zero_in_date), [NO\_ZERO\_DATE](sql_mode.md#no_zero_date), [ERROR\_FOR\_DIVISION\_BY\_ZERO](sql_mode.md#error_for_division_by_zero), [NO\_ENGINE\_SUBSTITUTION](sql_mode.md#no_engine_substitution), [NO\_AUTO\_CREATE\_USER](sql_mode.md#no_auto_create_user).

## Strict Mode

A mode where at least one of `STRICT_TRANS_TABLES` or `STRICT_ALL_TABLES` is enabled is called _strict mode_.

With strict mode set (default from [MariaDB 10.2.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1024-release-notes)), statements that modify tables (either transactional for `STRICT_TRANS_TABLES` or all for `STRICT_ALL_TABLES`) will fail, and an error will be returned instead. The IGNORE keyword can be used when strict mode is set to convert the error to a warning.

With strict mode not set (default in version <= [MariaDB 10.2.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/mariadb-1023-release-notes)), MariaDB will automatically adjust invalid values, for example, truncating strings that are too long, or adjusting numeric values that are out of range, and produce a warning.

Statements that don't modify data will return a warning when adjusted regardless of mode.

## SQL\_MODE and Stored Programs

[Stored programs and views](../../server-usage/stored-routines/) always use the SQL\_MODE that was active when they were created. This means that users can safely change session or global SQL\_MODE; the stored programs they use will still work as usual.

It is possible to change session SQL\_MODE within a stored program. In this case, the new SQL\_MODE will be in effect only in the body of the current stored program. If it calls some stored procedures, they will not be affected by the change.

Some Information Schema tables (such as [ROUTINES](../../reference/system-tables/information-schema/information-schema-tables/information-schema-routines-table.md)) and SHOW CREATE statements such as [SHOW CREATE PROCEDURE](../../reference/sql-statements/administrative-sql-statements/show/show-create-procedure.md) show the SQL\_MODE used by the stored programs.

## Examples

This example shows how to get a readable list of enabled SQL\_MODE flags:

```sql
SELECT REPLACE(@@SQL_MODE, ',', '\n');
+-------------------------------------------------------------------------+
| REPLACE(@@SQL_MODE, ',', '\n')                                          |
+-------------------------------------------------------------------------+
| STRICT_TRANS_TABLES
NO_ZERO_IN_DATE
NO_ZERO_DATE
NO_ENGINE_SUBSTITUTION |
+-------------------------------------------------------------------------+
```

Adding a new flag:

```sql
SET @@SQL_MODE = CONCAT(@@SQL_MODE, ',NO_ENGINE_SUBSTITUTION');
```

If the specified flag is already ON, the above example has no effect but does not produce an error.

How to unset a flag:

```sql
SET @@SQL_MODE = REPLACE(@@SQL_MODE, 'NO_ENGINE_SUBSTITUTION', '');
```

How to check if a flag is set:

```sql
SELECT @@SQL_MODE LIKE '%NO_ZERO_DATE%';
+----------------------------------+
| @@SQL_MODE LIKE '%NO_ZERO_DATE%' |
+----------------------------------+
|                                1 |
+----------------------------------+
```

Without and with strict mode:

```sql
CREATE TABLE strict (s CHAR(5), n TINYINT);

INSERT INTO strict VALUES ('MariaDB', '128');
Query OK, 1 row affected, 2 warnings (0.14 sec)

SHOW WARNINGS;
+---------+------+--------------------------------------------+
| Level   | Code | Message                                    |
+---------+------+--------------------------------------------+
| Warning | 1265 | Data truncated for column 's' at row 1     |
| Warning | 1264 | Out of range value for column 'n' at row 1 |
+---------+------+--------------------------------------------+
2 rows in set (0.00 sec)

SELECT * FROM strict;
+-------+------+
| s     | n    |
+-------+------+
| Maria |  127 |
+-------+------+

SET sql_mode='STRICT_TRANS_TABLES';

INSERT INTO strict VALUES ('MariaDB', '128');
ERROR 1406 (22001): Data too long for column 's' at row 1
```

Overriding strict mode with the IGNORE keyword:

```sql
INSERT IGNORE INTO strict VALUES ('MariaDB', '128');
Query OK, 1 row affected, 2 warnings (0.15 sec)
```

## See Also

* [SQL\_MODE=MSSQL](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modemssql)
* [SQL\_MODE=ORACLE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
