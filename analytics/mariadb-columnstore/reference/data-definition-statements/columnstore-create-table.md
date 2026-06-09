---
description: >-
  CREATE TABLE syntax for MariaDB ColumnStore: defines tables with
  ENGINE=columnstore, optional compression COMMENT, and standard
  column-definition syntax for most MariaDB data types.
---

# ColumnStore CREATE TABLE

A database consists of tables that store user data. You can create multiple columns with the `CREATE TABLE` statement. The data type follows the column name when adding columns.

## Syntax

```bnf
CREATE TABLE [IF NOT EXISTS] tbl_name
    (create_definition,...)  
ENGINE=columnstore  [ DEFAULT CHARSET=character-set] 
[COMMENT '[compression=0|1][;]
CREATE TABLE [IF NOT EXISTS] tbl_name
   { LIKE old_table_name | (LIKE old_table_name) }
create_definition:
    { col_name column_definition } 
column_definition:
    data_type
      [NOT NULL | NULL]
      [DEFAULT default_value]
      [COMMENT '[compression=0|1]
      [COMMENT='schema sync only']
      [COMMENT 'autoincrement column_name'];
```

images here

## Notes

* ColumnStore tables should not be created in the mysql, `information_schema`, `calpontsys`, or test databases.
* ColumnStore stores all object names in lowercase.
* `CREATE TABLE AS SELECT` is not supported and will instead create the table in the default storage engine.
* Compression level (`0` for no compression, `1` for compression) is set at the system level. If a session default exists, it will override the system default. In turn, it can be overridden by the table-level compression comment and, finally, a compression comment at the column level.
* A table is created in the front end only by using a ‘schema sync only’ comment.
* The column `DEFAULT` value can be a maximum of 64 characters.
* For maximum compatibility with external tools, MariaDB ColumnStore will accept the following table attributes; however, these are not implemented within MariaDB ColumnStore:
  * `MIN_ROWS`
  * `MAX_ROWS`
  * `AUTO_INCREMENT`

All of these are ignored by ColumnStore. The following statement creates a table called "orders" with two columns: `orderkey` with datatype `INTEGER`, and `customer` with datatype `VARCHAR`:

```sql
CREATE TABLE orders (
  orderkey INTEGER, 
  customer VARCHAR(45)
) ENGINE=ColumnStore
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
