---
description: >-
  This guide provides a walkthrough of the INSERT, UPDATE, and DELETE
  statements, demonstrating how to add, modify, and remove data in tables.
---

# Adding & Changing Data Guide

This guide explains how to add new data and modify existing data in MariaDB using `INSERT`, `REPLACE`, and `UPDATE` statements. Learn about various options for handling duplicates, managing statement priorities, inserting data from other tables, and performing conditional updates.

### Adding Data with `INSERT`

The `INSERT` statement is used to add new rows to a table.

Basic Syntax:

If providing values for all columns in their defined order:

```sql
INSERT table1 VALUES('value1','value2','value3');
```

The number of values must match the number of columns in `table1`.

Specifying Columns:

It's good practice to specify the columns you are inserting data into, which also allows you to insert columns in any order or omit columns that have default values or allow NULL.

```sql
INSERT INTO table1 (col3, col1) VALUES('value_for_col3', 'value_for_col1');
```

* The `INTO` keyword is optional but commonly used for readability.
* If a column is not listed and is an `AUTO_INCREMENT` key, its value will be generated. For other omitted columns, their `DEFAULT` value will be used, or `NULL` if allowed. You can explicitly insert a default value using the `DEFAULT` keyword in the `VALUES` list for a specific column.

Multiple Row Inserts:

Insert multiple rows in a single statement for efficiency:

```sql
INSERT INTO table2 (id_col, data_col1, data_col2) VALUES
  ('id1', 'text_a', 'text_b'),
  ('id2', 'text_c', 'text_d'),
  ('id3', 'text_e', 'text_f');
```

The `VALUES` keyword is used only once, with each row's values enclosed in parentheses and separated by commas.

Handling Duplicates with INSERT IGNORE:

If you attempt to insert a row that would cause a duplicate value in a PRIMARY KEY or UNIQUE index, an error normally occurs, and the row (and potentially subsequent rows in a multi-row insert) might not be inserted.

Using IGNORE tells MariaDB to discard the duplicate row(s) and continue inserting any other valid rows without generating an error.

```sql
INSERT IGNORE INTO table2 (unique_id_col, data_col) VALUES
  ('id1', 'some_data'),        -- Will be inserted if new
  ('id2', 'other_data'),       -- Will be inserted if new
  ('id1', 'duplicate_data');  -- Will be ignored if 'id1' already exists or was just inserted
```

### Managing `INSERT` Priority and Behavior

LOW\_PRIORITY:

An INSERT statement normally takes priority over SELECT statements, potentially locking the table and making other clients wait. LOW\_PRIORITY makes the INSERT wait until no other clients are reading from the table.

```sql
INSERT LOW_PRIORITY INTO table1 VALUES('value1','value2','value3');
```

* Once the `LOW_PRIORITY` insert begins, it will lock the table as usual. New read requests that arrive while it's waiting will be processed before it.

DELAYED:

(Note: INSERT DELAYED is a feature that was primarily associated with the MyISAM storage engine. It is deprecated in older MariaDB/MySQL versions and removed in modern MariaDB versions (e.g., from MariaDB 10.5). Check your MariaDB version for support and consider alternatives if using a recent version.)

`INSERT DELAYED` allowed the server to queue the insert request and return control to the client immediately. Data was written when the table was not in use. Multiple `DELAYED` inserts were batched.

```sql
-- Syntax for historical reference; may not be supported
INSERT DELAYED INTO table1 VALUES('value1','value2','value3');
```

Flaws included no confirmation of successful insertion and potential data loss if the server crashed before data was written from memory.

### Inserting Data from Another Table (`INSERT...SELECT`)

You can insert rows into a table based on data retrieved from another table (or tables) using `INSERT ... SELECT`.

```sql
INSERT INTO softball_team (last_name, first_name, telephone)
  SELECT name_last, name_first, tel_home
  FROM company_database.employees
  WHERE is_on_softball_team = 'Y';
```

* The columns in the `INSERT INTO softball_team (...)` list must correspond in number and general data type compatibility to the columns in the `SELECT` list.
* `INSERT...SELECT` statements generally cannot operate on the exact same table as both the target and the source directly without mechanisms like temporary tables or certain subquery structures.

### Replacing Data with `REPLACE`

The `REPLACE` statement works like `INSERT`, but if a new row has the same value as an existing row for a `PRIMARY KEY` or a `UNIQUE` index, the existing row is deleted before the new row is inserted. If no such conflict exists, it acts like a normal `INSERT`.

```sql
REPLACE LOW_PRIORITY INTO table2 (id_col, data_col1, data_col2) VALUES
  ('id1', 'new_text_a', 'new_text_b'), -- If 'id1' exists, old row is deleted, this is inserted
  ('id2', 'new_text_c', 'new_text_d'), -- If 'id2' doesn't exist, this is inserted
  ('id3', 'new_text_e', 'new_text_f');
```

* Flags like `LOW_PRIORITY` work similarly to `INSERT`.
* `REPLACE` also supports the `REPLACE ... SELECT` syntax.
* Because `REPLACE` performs a delete then an insert, any columns in the table not specified in the `REPLACE` statement will receive their default values for the newly inserted row, not values from the old row.

### Modifying Data with `UPDATE`

Use the `UPDATE` statement to change data in existing rows.

**Basic Syntax:**

```sql
UPDATE table3
SET col1 = 'new_value_a', col2 = 'new_value_b'
WHERE id_column < 100;
```

* The `SET` clause specifies which columns to modify and their new values.
* The `WHERE` clause is crucial; it determines which rows are updated. **Without a `WHERE` clause, all rows in the table will be updated.**
* `LOW_PRIORITY` and `IGNORE` (to ignore errors like unique key violations during update, allowing other valid row updates to proceed) can also be used with `UPDATE`.

Using Current Column Values in an Update:

You can use a column's current value in the calculation for its new value.

```sql
UPDATE table5
SET event_date = DATE_ADD(event_date, INTERVAL 1 DAY)
WHERE DAYOFWEEK(event_date) = 1; -- Example: Add 1 day if event_date is a Sunday
```

ORDER BY and LIMIT with UPDATE:

You can control the order in which rows are updated and limit the number of rows affected (for single-table updates).

```sql
UPDATE LOW_PRIORITY table3
SET col1 = 'updated_text_a', col2 = 'updated_text_b'
WHERE status_column = 'pending'
ORDER BY creation_date DESC
LIMIT 10;
```

This updates the 10 most recently created 'pending' rows.

Multi-Table UPDATE:

You can update rows in one table based on values from another table by joining them.

```sql
UPDATE products p
JOIN stock_levels s ON p.product_id = s.product_id
SET p.stock_count = s.current_stock
WHERE s.warehouse_id = 'WHA';
```

* Here, `products.stock_count` is updated using values from `stock_levels`.
* `ORDER BY` and `LIMIT` are generally not allowed with multi-table `UPDATE` statements in this direct join form.

### Conditional Inserts or Updates (`INSERT ... ON DUPLICATE KEY UPDATE`)

This powerful feature allows you to `INSERT` a new row, but if a duplicate key (Primary or Unique) conflict occurs, it performs an `UPDATE` on the existing row instead.

```sql
INSERT INTO table1 (id, col1, col2, status_column)
VALUES ('1012', 'some_text', 'other_text', 'new')
ON DUPLICATE KEY UPDATE status_column = 'old', col2 = VALUES(col2);
```

* If `id` '1012' does not exist, the row is inserted with `status_column = 'new'`.
* If `id` '1012' already exists, the existing row is updated: `status_column` is set to 'old', and `col2` is updated with the value that _would have been inserted_ for `col2` (using `VALUES(col2)`).
* The `IGNORE` keyword can be used with `INSERT ... ON DUPLICATE KEY UPDATE` to ignore errors that might occur during the `UPDATE` part if the update itself causes a problem (though this is less common). If `IGNORE` is used with `INSERT` and `ON DUPLICATE KEY UPDATE` is also present, `IGNORE` only applies to the `INSERT` part, not the `UPDATE` part.

### Further Data Modification Methods

Beyond these SQL statements, MariaDB offers bulk methods for adding data, such as:

* [`LOAD DATA INFILE`](../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md): For importing data from text files.
* [`mariadb-import` utility](../clients-and-utilities/backup-restore-and-import-clients/mariadb-import.md): A command-line tool that uses `LOAD DATA INFILE`. These are covered in "[Bulk Data Importing Guide](mariadb-importing-data-guide.md)").

CC BY-SA / Gnu FDL
