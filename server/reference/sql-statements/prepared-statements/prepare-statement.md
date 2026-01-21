---
description: >-
  Parse and optimize a SQL statement for later use. This command assigns a name
  to the statement, enabling efficient execution with parameters.
---

# PREPARE Statement

## Syntax

```sql
PREPARE stmt_name FROM preparable_stmt
```

## Description

The `PREPARE` statement prepares a statement and assigns it a name,`stmt_name`, by which to refer to the statement later. Statement names are not case sensitive. `preparable_stmt` is either a string literal or a [user variable](../../sql-structure/sql-language-structure/user-defined-variables.md) (not a [local variable](../programmatic-compound-statements/declare-variable.md), an SQL expression or a subquery) that contains the text of the statement. The text must represent a single SQL statement, not multiple statements. Within the statement, "?" characters can be used as parameter markers to indicate where data values are to be bound to the query later when you execute it. The "?" characters should not be enclosed within quotes, even if you intend to bind them to string values. Parameter markers can be used only where expressions should appear, not for SQL keywords, identifiers, and so forth.

The scope of a prepared statement is the session within which it is created. Other sessions cannot see it.

If a prepared statement with the given name already exists, it is deallocated implicitly before the new statement is prepared. This means that if the new statement contains an error and cannot be prepared, an error is returned and no statement with the given name exists.

Prepared statements can be `PREPARE` and [EXECUTE](execute-statement.md) in a stored procedure, but not in a stored function or trigger. Also, even if the statement is prepared with `PREPARE` in a procedure, it will not be deallocated when the procedure execution ends.

A prepared statement can access [user-defined variables](../../sql-structure/sql-language-structure/user-defined-variables.md), but not [local variables](../programmatic-compound-statements/declare-variable.md) or procedure's parameters.

If the prepared statement contains a syntax error, PREPARE will fail. As a side effect, stored procedures can use it to check if a statement is valid. For example:

```sql
CREATE PROCEDURE `test_stmt`(IN sql_text TEXT)
BEGIN
        DECLARE EXIT HANDLER FOR SQLEXCEPTION
        BEGIN
                SELECT CONCAT(sql_text, ' is not valid');
        END;
        SET @SQL := sql_text;
        PREPARE stmt FROM @SQL;
        DEALLOCATE PREPARE stmt;
END;
```

The [FOUND\_ROWS()](../../sql-functions/secondary-functions/information-functions/found_rows.md) and [ROW\_COUNT()](../../sql-functions/secondary-functions/information-functions/row_count.md) functions, if called immediatly after EXECUTE, return the number of rows read or affected by the prepared statements; however, if they are called after DEALLOCATE PREPARE, they provide information about this statement. If the prepared statement produces errors or warnings, [GET DIAGNOSTICS](../programmatic-compound-statements/programmatic-compound-statements-diagnostics/get-diagnostics.md) return information about them. DEALLOCATE PREPARE shouldn't clear the [diagnostics area](../programmatic-compound-statements/programmatic-compound-statements-diagnostics/diagnostics-area.md), unless it produces an error.

A prepared statement is executed with [EXECUTE](execute-statement.md) and released with [DEALLOCATE PREPARE](deallocate-drop-prepare.md).

The [max\_prepared\_stmt\_count](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_prepared_stmt_count) server system variable determines the number of allowed prepared statements that can be prepared on the server. If it is set to 0, prepared statements are not allowed. If the limit is reached, an error similar to the following will be produced:

```sql
ERROR 1461 (42000): Can't create more than max_prepared_stmt_count statements 
  (current value: 0)
```

### Oracle Mode

In [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle), `PREPARE stmt FROM 'SELECT :1, :2'` is used, instead of `?`.

## Permitted Statements

{% hint style="info" %}
The following is valid only from MariaDB [**10.6.2**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1062-release-notes)**.**
{% endhint %}

All statements can be prepared, except [PREPARE](prepare-statement.md), [EXECUTE](execute-statement.md), and [DEALLOCATE / DROP PREPARE](deallocate-drop-prepare.md).

Prior to this, not all statements can be prepared. Only the following SQL commands are permitted:

* [ALTER TABLE](../data-definition/alter/alter-table/)
* [ANALYZE TABLE](../table-statements/analyze-table.md)
* [BINLOG](../administrative-sql-statements/binlog.md)
* [CACHE INDEX](../administrative-sql-statements/cache-index.md)
* [CALL](../stored-routine-statements/call.md)
* [CHANGE MASTER](../administrative-sql-statements/replication-statements/change-master-to.md)
* [CHECKSUM {TABLE | TABLES}](../table-statements/checksum-table.md)
* [COMMIT](../transactions/commit.md)
* {[CREATE](../data-definition/create/create-database.md) | [DROP](../data-definition/drop/drop-database.md)} DATABASE
* {[CREATE](../data-definition/create/create-index.md) | [DROP](../data-definition/drop/drop-index.md)} INDEX
* {[CREATE](../data-definition/create/create-table.md) | [RENAME](../data-definition/rename-table.md) | [DROP](../data-definition/drop/drop-table.md)} TABLE
* {[CREATE](../account-management-sql-statements/create-user.md) | [RENAME](../account-management-sql-statements/rename-user.md) | [DROP](../account-management-sql-statements/drop-user.md)} USER
* {[CREATE](../../../server-usage/views/create-view.md) | [DROP](../../../server-usage/views/drop-view.md)} VIEW
* [DELETE](../data-manipulation/changing-deleting-data/delete.md)
* [DESCRIBE](../administrative-sql-statements/describe.md)
* [DO](../stored-routine-statements/do.md)
* [EXPLAIN](../administrative-sql-statements/analyze-and-explain-statements/explain.md)
* [FLUSH](../administrative-sql-statements/flush-commands/flush.md) {TABLE | TABLES | TABLES WITH READ LOCK | HOSTS | PRIVILEGES | LOGS | STATUS |\
  MASTER | SLAVE | DES\_KEY\_FILE | USER\_RESOURCES | [QUERY CACHE](../administrative-sql-statements/flush-commands/flush-query-cache.md) | TABLE\_STATISTICS |\
  INDEX\_STATISTICS | USER\_STATISTICS | CLIENT\_STATISTICS}
* [GRANT](../account-management-sql-statements/grant.md)
* [INSERT](../data-manipulation/inserting-loading-data/insert.md)
* INSTALL {[PLUGIN](../administrative-sql-statements/plugin-sql-statements/install-plugin.md) | [SONAME](../administrative-sql-statements/plugin-sql-statements/install-soname.md)}
* [HANDLER READ](../../sql-structure/nosql/handler/handler-commands.md)
* [KILL](../administrative-sql-statements/kill.md)
* [LOAD INDEX INTO CACHE](../data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-index.md)
* [OPTIMIZE TABLE](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md)
* [REPAIR TABLE](../table-statements/repair-table.md)
* [REPLACE](../data-manipulation/changing-deleting-data/replace.md)
* [RESET](../administrative-sql-statements/reset.md) {[MASTER](../administrative-sql-statements/replication-statements/reset-master.md) | [SLAVE](../administrative-sql-statements/replication-statements/reset-replica.md) | [QUERY CACHE](../administrative-sql-statements/reset.md)}
* [REVOKE](../account-management-sql-statements/revoke.md)
* [ROLLBACK](../transactions/rollback.md)
* [SELECT](../data-manipulation/selecting-data/select.md)
* [SET](../administrative-sql-statements/set-commands/set.md)
* [SET GLOBAL SQL\_SLAVE\_SKIP\_COUNTER](../administrative-sql-statements/replication-statements/set-global-sql_slave_skip_counter.md)
* [SET ROLE](../account-management-sql-statements/set-role.md)
* [SET SQL\_LOG\_BIN](../administrative-sql-statements/set-commands/set-sql_log_bin.md)
* [SET TRANSACTION ISOLATION LEVEL](../transactions/set-transaction.md)
* [SHOW EXPLAIN](../administrative-sql-statements/show/show-explain.md)
* SHOW {[DATABASES](../administrative-sql-statements/show/show-databases.md) | [TABLES](../administrative-sql-statements/show/show-tables.md) | [OPEN TABLES](../administrative-sql-statements/show/show-open-tables.md) | [TABLE STATUS](../administrative-sql-statements/show/show-table-status.md) | [COLUMNS](../administrative-sql-statements/show/show-columns.md) | [INDEX](../administrative-sql-statements/show/show-index.md) | [TRIGGERS](../administrative-sql-statements/show/show-triggers.md) |[EVENTS](../administrative-sql-statements/show/show-events.md) | [GRANTS](../administrative-sql-statements/show/show-grants.md) | [CHARACTER SET](../administrative-sql-statements/show/show-character-set.md) | [COLLATION](../administrative-sql-statements/show/show-collation.md) | [ENGINES](../administrative-sql-statements/show/show-events.md) | \[PLUGINS [SONAME](../administrative-sql-statements/show/show-plugins.md)] | [PRIVILEGES](../administrative-sql-statements/show/show-privileges.md) |[PROCESSLIST](../administrative-sql-statements/show/show-processlist.md) | [PROFILE](../administrative-sql-statements/show/show-profile.md) | [PROFILES](../administrative-sql-statements/show/show-profiles.md) | [VARIABLES](../administrative-sql-statements/show/show-variables.md) | [STATUS](../administrative-sql-statements/show/show-status.md) | [WARNINGS](../administrative-sql-statements/show/show-warnings.md) | [ERRORS](../administrative-sql-statements/show/show-errors.md) |[TABLE\_STATISTICS](../administrative-sql-statements/show/show-table-statistics.md) | [INDEX\_STATISTICS](../administrative-sql-statements/show/show-index-statistics.md) | [USER\_STATISTICS](../administrative-sql-statements/show/show-user-statistics.md) | [CLIENT\_STATISTICS](../administrative-sql-statements/show/show-client-statistics.md) | [AUTHORS](../administrative-sql-statements/show/show-authors.md) |[CONTRIBUTORS](../administrative-sql-statements/show/show-contributors.md)}
* SHOW CREATE {[DATABASE](../administrative-sql-statements/show/show-create-database.md) | [TABLE](../administrative-sql-statements/show/show-create-table.md) | [VIEW](../administrative-sql-statements/show/show-create-view.md) | [PROCEDURE](../administrative-sql-statements/show/show-create-procedure.md) | [FUNCTION](../administrative-sql-statements/show/show-create-function.md) | [TRIGGER](../administrative-sql-statements/show/show-create-trigger.md) | [EVENT](../administrative-sql-statements/show/show-create-event.md)}
* SHOW {[FUNCTION](../administrative-sql-statements/show/show-function-code.md) | [PROCEDURE](../administrative-sql-statements/show/show-procedure-code.md)} CODE
* [SHOW BINLOG EVENTS](../administrative-sql-statements/show/show-binlog-events.md)
* [SHOW SLAVE HOSTS](../administrative-sql-statements/show/show-replica-hosts.md)
* SHOW {MASTER | BINARY} LOGS
* SHOW {MASTER | SLAVE | TABLES | INNODB | FUNCTION | PROCEDURE} STATUS
* SLAVE {[START](../administrative-sql-statements/replication-statements/start-replica.md) | [STOP](../administrative-sql-statements/replication-statements/stop-replica.md)}
* [TRUNCATE TABLE](../table-statements/truncate-table.md)
* [SHUTDOWN](../administrative-sql-statements/shutdown.md)
* UNINSTALL {PLUGIN | SONAME}
* [UPDATE](../data-manipulation/changing-deleting-data/update.md)

Synonyms are not listed here, but can be used. For example, `DESC` can be used instead of `DESCRIBE`.

[Compound statements](../programmatic-compound-statements/using-compound-statements-outside-of-stored-programs.md) can be prepared too.

Note that if a statement can be run in a stored routine, it will work even if it is called by a prepared statement. For example, [SIGNAL](../programmatic-compound-statements/signal.md) can't be directly prepared. However, it is allowed in [stored routines](../../../server-usage/stored-routines/). If the x() procedure contains `SIGNAL`, you can still prepare and execute the '`CALL` x();' prepared statement.

`PREPARE` supports most kinds of expressions as well, for example:

```sql
PREPARE stmt FROM CONCAT('SELECT * FROM ', table_name);
```

When PREPARE is used with a statement which is not supported, the following error is produced:

```sql
ERROR 1295 (HY000): This command is not supported in the prepared statement protocol yet
```

## Example

```sql
CREATE TABLE t1 (a INT,b CHAR(10));
INSERT INTO t1 VALUES (1,"one"),(2, "two"),(3,"three");
PREPARE test FROM "select * from t1 where a=?";
SET @param=2;
EXECUTE test USING @param;
+------+------+
| a    | b    |
+------+------+
|    2 | two  |
+------+------+
SET @param=3;
EXECUTE test USING @param;
+------+-------+
| a    | b     |
+------+-------+
|    3 | three |
+------+-------+
DEALLOCATE PREPARE test;
```

Since identifiers are not permitted as prepared statements parameters, sometimes it is necessary to dynamically compose an SQL statement. This technique is called _dynamic SQL_). The following example shows how to use dynamic SQL:

```sql
CREATE PROCEDURE test.stmt_test(IN tab_name VARCHAR(64))
BEGIN
	SET @sql = CONCAT('SELECT COUNT(*) FROM ', tab_name);
	PREPARE stmt FROM @sql;
	EXECUTE stmt;
	DEALLOCATE PREPARE stmt;
END;

CALL test.stmt_test('mysql.user');
+----------+
| COUNT(*) |
+----------+
|        4 |
+----------+
```

Use of variables in prepared statements:

```sql
PREPARE stmt FROM 'SELECT @x;';

SET @x = 1;

EXECUTE stmt;
+------+
| @x   |
+------+
|    1 |
+------+

SET @x = 0;

EXECUTE stmt;
+------+
| @x   |
+------+
|    0 |
+------+

DEALLOCATE PREPARE stmt;
```

## See Also

* [EXECUTE Statement](execute-statement.md)
* [DEALLOCATE / DROP Prepared Statement](deallocate-drop-prepare.md)
* [EXECUTE IMMEDIATE](execute-immediate.md)
* [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
