---
description: >-
  Display warnings from the last executed statement. View warning codes,
  messages, and levels for recent operations.
---

# SHOW WARNINGS

## Syntax

```sql
SHOW WARNINGS [LIMIT [offset,] row_count]
SHOW ERRORS [LIMIT row_count OFFSET offset]
SHOW COUNT(*) WARNINGS
```

## Description

`SHOW WARNINGS` shows the error, warning, and note messages that resulted from the last statement that generated messages in the current session. It shows nothing if the last statement used a table and generated no messages. (That is, a statement that uses a table but generates no messages clears the message list.) Statements that do not use tables and do not generate messages have no effect on the message list.

A note is different to a warning in that it only appears if the [sql\_notes](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_notes) variable is set to 1 (the default), and is not converted to an error if [strict mode](../../../../server-management/variables-and-modes/sql_mode.md) is enabled.

A related statement, [SHOW ERRORS](show-errors.md), shows only the errors.

The `SHOW COUNT(*) WARNINGS` statement displays the total number of errors, warnings, and notes. You can also retrieve this number from the [warning\_count](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#warning_count) variable:

```sql
SHOW COUNT(*) WARNINGS;
SELECT @@warning_count;
```

The value of [warning\_count](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#warning_count) might be greater than the number of messages displayed by `SHOW WARNINGS` if the [max\_error\_count](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_error_count) system variable is set so low that not all messages are stored.

The `LIMIT` clause has the same syntax as for the [SELECT statement](../../data-manipulation/selecting-data/select.md).

`SHOW WARNINGS` can be used after [EXPLAIN EXTENDED](../analyze-and-explain-statements/explain.md) to see how a query is internally rewritten by MariaDB.

If the [sql\_notes](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#sql_notes) server variable is set to 1, Notes are included in the output of `SHOW WARNINGS`; if it is set to 0, this statement will not show (or count) Notes.

The results of `SHOW WARNINGS` and `SHOW COUNT(*) WARNINGS` are directly sent to the client. If you need to access those information in a stored program, you can use the [GET DIAGNOSTICS](../../programmatic-compound-statements/programmatic-compound-statements-diagnostics/get-diagnostics.md) statement instead.

The [mariadb](../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) client also has a number of options related to warnings. The `\W` command will show warnings after every statement, while `\w` will disable this. Starting the client with the `--show-warnings` option will show warnings after every statement.

MariaDB implements a stored routine error stack trace. `SHOW WARNINGS` can also be used to show more information. See the example below.

## Examples

```sql
SELECT 1/0;
+------+
| 1/0  |
+------+
| NULL |
+------+

SHOW COUNT(*) WARNINGS;
+-------------------------+
| @@session.warning_count |
+-------------------------+
|                       1 |
+-------------------------+

SHOW WARNINGS;
+---------+------+---------------+
| Level   | Code | Message       |
+---------+------+---------------+
| Warning | 1365 | Division by 0 |
+---------+------+---------------+
```

### Stack Trace

Displaying a stack trace:

```sql
DELIMITER $$
CREATE OR REPLACE PROCEDURE p1()
  BEGIN
    DECLARE c CURSOR FOR SELECT * FROM not_existing;
    OPEN c;
    CLOSE c;
  END;
$$
CREATE OR REPLACE PROCEDURE p2()
  BEGIN
    CALL p1;
  END;
$$
DELIMITER ;
CALL p2;
ERROR 1146 (42S02): Table 'test.not_existing' doesn't exist

SHOW WARNINGS;
+-------+------+-----------------------------------------+
| Level | Code | Message                                 |
+-------+------+-----------------------------------------+
| Error | 1146 | Table 'test.not_existing' doesn't exist |
| Note  | 4091 | At line 6 in test.p1                    |
| Note  | 4091 | At line 4 in test.p2                    |
+-------+------+-----------------------------------------+
```

`SHOW WARNINGS` displays a stack trace, showing where the error actually happened:

* Line 4 in test.p1 is the OPEN command which actually raised the error.
* Line 3 in test.p2 is the CALL statement, calling p1 from p2.

## See Also

* [SHOW ERRORS](show-errors.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
