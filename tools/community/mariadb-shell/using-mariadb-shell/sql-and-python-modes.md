---
description: >-
  Switch between SQL and Python mode, enter multi-line statements and stored
  program bodies, and run SQL from Python with session.run_sql and result
  objects.
---

# SQL and Python Modes

MariaDB Shell has two input modes. In SQL mode, everything you type goes to the server as SQL, much like the `mariadb` command-line client. In Python mode, you type Python code that runs in the shell's embedded Python interpreter, with global objects such as `session`, `util`, and `shell` ready to use. Shell commands such as `\use` or `\option` work in both.

The prompt shows the active mode:

```text
MariaDB localhost:3306 ssl  shop  SQL >
MariaDB localhost:3306 ssl  shop  Py >
```

## Choosing the Mode

The shell starts in SQL mode unless you choose otherwise. You can change the starting mode on the command line, or persist another default:

| Method | Effect |
| --- | --- |
| `--sql` | Starts in SQL mode. |
| `--py` or `--python` | Starts in Python mode. |
| `-f <file>` | Chooses the mode from the file extension: `.sql` for SQL, `.py` for Python. See [Batch Execution](batch-execution.md). |
| `defaultMode` option | Sets the starting mode when no command line option chooses one. For example, `\option --persist defaultMode py`. |

```sh
mariadb-shell --py mariadb://dba@localhost/shop
```

## Switching Modes

At the prompt, `\sql` switches to SQL mode and `\py` switches to Python mode. The global session stays open, so the connection, the default schema, and any open transaction carry over.

```text
MariaDB localhost:3306 ssl  shop  SQL > \py
Switching to Python mode...
MariaDB localhost:3306 ssl  shop  Py > \sql
Switching to SQL mode... Commands end with ;
MariaDB localhost:3306 ssl  shop  SQL >
```

Each mode keeps its own command history. See [Editing and History](editing-and-history.md#command-history).

### Running One SQL Statement from Python Mode

`\sql` followed by a statement runs that statement and stays in Python mode. The result is printed as in SQL mode. Use it for a quick look at the data while you work on a Python script:

```text
MariaDB localhost:3306 ssl  shop  Py > \sql SELECT COUNT(*) FROM product
+----------+
| COUNT(*) |
+----------+
|        3 |
+----------+
1 row in set (0.0001 sec)
```

No terminator is needed after the statement.

## SQL Mode

### Statement Terminators

A statement runs when the shell reads a terminator. Until then, the shell collects lines, and the prompt changes to `->` to show that a statement is pending:

```text
MariaDB localhost:3306 ssl  shop  SQL > SELECT name, price
                                     -> FROM product
                                     -> WHERE price > 20;
```

| Terminator | Effect |
| --- | --- |
| `;` | Runs the statement and prints the result in the current result format. You can change it with `DELIMITER`. |
| `\g` | Runs the statement like `;`. |
| `\G` | Runs the statement and prints the result vertically, one `column: value` line per column, regardless of the current result format. |
| `\Gj`, `\GJ`, `\GT`, `\Gt` | Runs the statement and prints the result as a JSON array, as JSON with result metadata, as tab-separated values with a header, or as tab-separated values without a header. See [Output Formats](output-formats.md#format-for-one-statement). |

```text
MariaDB localhost:3306 ssl  shop  SQL > SELECT * FROM product WHERE id = 1\G
*************************** 1. row ***************************
      id: 1
    name: Desk lamp
   price: 24.90
in_stock: 1
1 row in set (0.0001 sec)
```

You can put several statements on one line. Each runs in turn and prints its own result:

```text
MariaDB localhost:3306 ssl  shop  SQL > SELECT COUNT(*) FROM product; SELECT COUNT(*) FROM customer;
```

To abandon a pending statement, press **Ctrl+C**.

### Stored Programs and DELIMITER

The body of a stored procedure, function, trigger, or event contains semicolons that must not end the outer statement. Change the terminator with `DELIMITER`, write the statement, and change it back:

```text
MariaDB localhost:3306 ssl  shop  SQL > DELIMITER //
MariaDB localhost:3306 ssl  shop  SQL > CREATE PROCEDURE cheap_products()
                                     -> BEGIN
                                     ->   SELECT name FROM product WHERE price < 10;
                                     -> END//
Query OK, 0 rows affected (0.0125 sec)
MariaDB localhost:3306 ssl  shop  SQL > DELIMITER ;
MariaDB localhost:3306 ssl  shop  SQL > CALL cheap_products();
+----------+
| name     |
+----------+
| Notebook |
+----------+
1 row in set (0.0003 sec)

Query OK, 0 rows affected (0.0003 sec)
```

`DELIMITER` must start a new statement: type it at the main prompt, not in the middle of a pending statement. The current delimiter is shown by `\status`. SQL files that you run with `-f` or `\source` can use `DELIMITER` in the same way.

### Multi-Line Input

The `\` command, alone on a line, starts a block. In a block, the shell collects every line you type, including complete statements, without running anything. An empty line ends the block, and the shell then runs the statements in it:

```text
MariaDB localhost:3306 ssl  shop  SQL > \
                                      > UPDATE product SET price = price * 1.05 WHERE in_stock;
                                      > SELECT name, price FROM product;
                                      >
```

Use a block when you paste several statements and want to look at them before any of them runs. Each statement in the block still needs a terminator: a statement without one stays pending after the empty line, as at the normal prompt.

### Warnings

By default, the shell prints the warnings that a statement raises right after its result. `\nowarnings` (`\w`) turns this off and `\warnings` (`\W`) turns it back on. To start without warnings, use `--show-warnings=false`, or persist `showWarnings` as `false`. See [Shell Commands](shell-commands.md#warnings).

## Python Mode

In Python mode, the shell runs Python 3 code. Compound statements such as `for`, `if`, and `def` continue on the next lines, and an empty line ends them:

```text
MariaDB localhost:3306 ssl  shop  Py > for row in session.run_sql("SELECT id FROM product").fetch_all():
                                    ->     print(row.id)
                                    ->
1
2
3
```

The global session is available as `session`. To open additional sessions from Python, use `mysql.get_session()` or `shell.open_session()`. See [Sessions](../getting-started/sessions.md) and [Global Objects](../getting-started/global-objects.md).

### Running SQL from Python

`session.run_sql(query[, args])` sends one statement to the server and returns a `ClassicResult` object. Use `?` placeholders for values and pass them as a list in `args`. The shell quotes and escapes them, so values never become part of the SQL text:

```python
res = session.run_sql(
    "SELECT id, name, price FROM product WHERE price > ? ORDER BY price",
    [10])
```

At the interactive prompt, a result object that you evaluate on its own is printed as a table, as in SQL mode. In a script, you read the rows yourself.

### Reading Rows

| Method | Returns |
| --- | --- |
| `fetch_one()` | The next row as a `Row` object, or `None` when no rows are left. |
| `fetch_all()` | A list of all remaining rows. |
| `fetch_one_object()` | The next row as a dictionary that maps column names to values, or `None`. |
| `has_data()` | `True` if the statement produced a result set, also when it has no rows. |
| `next_result()` | Moves to the next result set when a statement, such as a `CALL`, returns several. Returns `False` when there are no more. |

A `Row` gives access to its fields in three ways: as an attribute (`row.name`), by position (`row[1]`), and by name with `row.get_field("name")`. Use `get_field()` for column names that aren't valid Python identifiers, such as `COUNT(*)` or `order-date`. `len(row)` and `row.length` return the number of fields.

```python
res = session.run_sql("SELECT id, name, price FROM product WHERE price > ?", [10])
row = res.fetch_one()
print(row.name, row[2], row.get_field("price"))
# Desk lamp 24.90 24.90

remaining = res.fetch_all()
print(len(remaining))
# 1

obj = session.run_sql("SELECT name FROM product WHERE id = 1").fetch_one_object()
print(obj)
# {"name": "Desk lamp"}
```

{% hint style="info" %}
`DECIMAL` values arrive in Python as strings, so no precision is lost. Convert them with `decimal.Decimal(row.price)` before you calculate with them. Integer columns arrive as `int`, and `NULL` as `None`.
{% endhint %}

### Result Information

| Property | Description |
| --- | --- |
| `affected_items_count` | Rows inserted, updated, or deleted by the statement. |
| `auto_increment_value` | The `AUTO_INCREMENT` value generated by the last `INSERT`. |
| `warnings_count` | Number of warnings the statement raised. |
| `warnings` | The warnings, as a list of `[level, code, message]` entries. Also available as `get_warnings()`. |
| `info` | The server's information string, such as `Rows matched: 3  Changed: 0  Warnings: 0`. |
| `execution_time` | The execution time as a string, such as `0.0002 sec`. |
| `column_count` | Number of columns in the result set. |
| `column_names` | List of column names. |
| `columns` | List of `Column` objects with column metadata. See [Column Metadata](#column-metadata). |
| `statement_id` | The ID of the statement that produced the result. |

Every property also has a getter method, for example `get_affected_items_count()`.

```python
r = session.run_sql("INSERT INTO product (name, price) VALUES (?, ?)", ["Stapler", 7.25])
print(r.affected_items_count, r.auto_increment_value, r.warnings_count)
# 1 4 0

r = session.run_sql("SELECT CAST('abc' AS INT)")
r.fetch_all()
print(r.warnings_count, r.get_warnings())
# 1 [["Warning", 1292, "Truncated incorrect INTEGER value: 'abc'"]]
```

### Column Metadata

Each entry in `columns` is a `Column` object with these properties:

| Property | Description |
| --- | --- |
| `column_name`, `column_label` | The original column name and the name or alias in the result. |
| `table_name`, `table_label` | The original table name and its alias. |
| `schema_name` | The schema of the table. |
| `type` | The column type, such as `Type.INT`, `Type.STRING`, or `Type.DECIMAL`. |
| `length` | The column length. |
| `fractional_digits` | The number of decimal places. |
| `number_signed` | Whether a numeric column is signed. |
| `zero_fill` | Whether the column has the `ZEROFILL` attribute. |
| `collation_name`, `character_set_name` | The collation and character set of a string column. |
| `flags` | Other column flags, such as `NOT_NULL` or `PRI_KEY`. |

```python
res = session.run_sql("SELECT id, name, price FROM product")
for col in res.columns:
    print(col.column_name, col.type, col.length, col.fractional_digits)
# id <Type.INT> 11 0
# name <Type.STRING> 160 0
# price <Type.DECIMAL> 10 2
```

For the full list of members, type `\? ClassicResult`, `\? Row`, or `\? Column` at the prompt.

### Transactions

`session.start_transaction()`, `session.commit()`, and `session.rollback()` control transactions from Python. You can also send `START TRANSACTION`, `COMMIT`, and `ROLLBACK` with `run_sql()`. Autocommit follows the server setting, as in SQL mode.

```python
session.start_transaction()
try:
    session.run_sql("UPDATE product SET price = price * 0.9 WHERE in_stock = 0")
    session.run_sql("INSERT INTO price_log (note) VALUES (?)", ["clearance"])
    session.commit()
except Exception:
    session.rollback()
    raise
```

To print a result in one of the shell's output formats from Python, use `shell.dump_rows()`. See [Output Formats](output-formats.md#formatting-results-in-python).
