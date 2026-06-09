---
description: >-
  ALTER TABLE for MariaDB ColumnStore modifies existing tables: add, drop, or
  rename columns and rename tables, with ColumnStore-specific syntax notes for
  the columnar engine.
---

# ColumnStore ALTER TABLE

The `ALTER TABLE` statement modifies existing tables. It includes adding, deleting, and renaming columns as well as renaming tables.

## Syntax

```bnf
ALTER TABLE tbl_name
    alter_specification [, alter_specification] ...

alter_specification:
    table_option ...
  | ADD [COLUMN] col_name column_definition
  | ADD [COLUMN] (col_name column_definition,...)
  | ALTER [COLUMN] col_name {SET DEFAULT literal | DROP DEFAULT}
  | CHANGE [COLUMN] old_col_name new_col_name column_definition
  | DROP [COLUMN] col_name
  | RENAME [TO] new_tbl_name
 

column_definition:
    data_type
      [NOT NULL | NULL]
      [DEFAULT default_value]
      [COMMENT '[compression=0|1];']

table_options:
    table_option [[,] table_option] ...  (see CREATE TABLE OPTIONS)
```

images here

### ADD

The ADD clause allows you to add columns to a table. You must specify the data type after the column name. The following statement adds a priority column with an integer datatype to the orders table:

```sql
ALTER TABLE orders ADD COLUMN priority INTEGER;
```

* Compression level (0 for no compression, 1 for compression) is set at the system level. If a session default exists, it will override the system default. In turn, it can be overridden by the table-level compression comment and finally, a compression comment at the column level.

### Online ALTER TABLE ADD Columntable Level

The ColumnStore engine fully supports online DDL (one session can be adding columns to a table while another session is querying that table).\
MariaDB ColumnStore has provided its own syntax to do so for adding columns to a table, one at a time only. Do not attempt to use it for any other purpose. Follow the example below as closely as possible.

We have also provided the following workaround. This workaround is intended for adding columns to a table, one at a time only. Do not attempt to use it for any other purpose. Follow the example below as closely as possible.

**Scenario**: Add an `INT` column named `col7` to the existing table `foo`:

```sql
SELECT calonlinealter('alter table foo add column col7 int;');
ALTER TABLE foo ADD COLUMN col7 INT COMMENT 'schema sync only';
```

The `SELECT` statement may take several tens of seconds to run, depending on how many rows are currently in the table. Regardless, other sessions can select against the table during this time (but they won’t be able to see the new column yet). The `ALTER TABLE` statement will take less than 1 second (depending on how busy MariaDB is), and during this brief time interval, other table reads will be held off.

### CHANGE

The `CHANGE` clause allows you to rename a column in a table.

Notes to `CHANGE COLUMN`:

* You cannot currently use `CHANGE COLUMN` to change the definition of that column.
* You can only change a single column at a time. The following example renames the `order_qty` field to quantity in the orders table:

```sql
ALTER TABLE orders CHANGE COLUMN order_qty quantity
INTEGER;
```

### DROP

The DROP clause allows you to drop columns. All associated data is removed when the column is dropped. You can `DROP COLUMN` (column\_name).\
The following example alters the orders table to drop the priority column:

```sql
ALTER TABLE orders DROP COLUMN priority;
```

### RENAME

The `RENAME` clause allows to rename a table. The following example renames the `orders` table:

```sql
ALTER TABLE orders RENAME TO customer_orders;
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
