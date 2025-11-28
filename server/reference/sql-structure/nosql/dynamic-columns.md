# Dynamic Columns

## Overview

Dynamic columns allow one to store different sets of columns for each row in a table. It works by storing a set of columns in a blob and having a small set of functions to manipulate it.

Dynamic columns should be used when it is not possible to use regular columns.

A typical use case is when one needs to store items that may have many different attributes (like size, color, weight, etc), and the set of possible attributes is very large and/or unknown in advance. In that case, attributes can be put into dynamic columns.

## Dynamic Columns Basics

The table should have a blob column which will be used as storage for dynamic columns:

```sql
main
CREATE TABLE assets (
  item_name VARCHAR(32) PRIMARY KEY, -- A common attribute for all items
  dynamic_cols  BLOB  -- Dynamic columns will be stored here
);
```

Once created, you can access dynamic columns via dynamic column functions.

Insert a row with two dynamic columns: color=blue, size=XL:

```sql
INSERT INTO assets VALUES 
  ('MariaDB T-shirt', COLUMN_CREATE('color', 'blue', 'size', 'XL'));
```

Insert another row with dynamic columns: color=black, price=500:

```sql
INSERT INTO assets VALUES
  ('Thinkpad Laptop', COLUMN_CREATE('color', 'black', 'price', 500));
```

Select the dynamic column 'color' for all items:

```sql
SELECT item_name, COLUMN_GET(dynamic_cols, 'color' as char) 
  AS color FROM assets;
+-----------------+-------+
| item_name       | color |
+-----------------+-------+
| MariaDB T-shirt | blue  |
| Thinkpad Laptop | black |
+-----------------+-------+
```

It is possible to add and remove dynamic columns from a row:

```sql
-- Remove a column:
UPDATE assets SET dynamic_cols=COLUMN_DELETE(dynamic_cols, "price") 
WHERE COLUMN_GET(dynamic_cols, 'color' AS CHAR)='black'; 

-- Add a column:
UPDATE assets SET dynamic_cols=COLUMN_ADD(dynamic_cols, 'warranty', '3 years')
WHERE item_name='Thinkpad Laptop';
```

You can also list all columns, or get them together with their values in JSON format:

```sql
SELECT item_name, column_list(dynamic_cols) FROM assets;
+-----------------+---------------------------+
| item_name       | column_list(dynamic_cols) |
+-----------------+---------------------------+
| MariaDB T-shirt | `size`,`color`            |
| Thinkpad Laptop | `color`,`warranty`        |
+-----------------+---------------------------+

SELECT item_name, COLUMN_JSON(dynamic_cols) FROM assets;
+-----------------+----------------------------------------+
| item_name       | COLUMN_JSON(dynamic_cols)              |
+-----------------+----------------------------------------+
| MariaDB T-shirt | {"size":"XL","color":"blue"}           |
| Thinkpad Laptop | {"color":"black","warranty":"3 years"} |
+-----------------+----------------------------------------+
```

## Dynamic Columns Reference

This is a complete reference of dynamic columns in MariaDB.

{% hint style="success" %}
**Column can be referred to by name (column\_name in the following code blocks). This is the preferred method.**\
If you need support for old (< 10.0) MariaDB versions, you have to refer to columns by number. In that case, replace _column\_name_ with _column\_nr_. This method is not recommended.
{% endhint %}

### Dynamic Columns Functions

#### COLUMN\_CREATE

```sql
COLUMN_CREATE(column_name, value [as type], [column_name, value 
  [as type]]...);
```

Returns a dynamic columns blob that stores the specified columns with values. The return value is suitable for

* storing in a table,
* further modification with other dynamic columns functions.

The `as type` part allows one to specify the value type. In most cases, this is redundant because MariaDB will be able to deduce the type of the value. Explicit type specification may be needed when the type of the value is not apparent. For example, a literal `'2012-12-01'` has a `CHAR` type by default, one will need to specify `'2012-12-01' AS DATE` to have it stored as a date. See the [Datatypes](dynamic-columns.md#Datatypes) section for further details. Note also [MDEV-597](https://jira.mariadb.org/browse/MDEV-597).

Typical usage:

```sql
INSERT INTO tbl SET dyncol_blob=COLUMN_CREATE("column_name", "value");
```

#### COLUMN\_ADD

```sql
COLUMN_ADD(dyncol_blob, column_name, value [as type], 
  [column_name, value [as type]]...);
```

Adds or updates dynamic columns.

* `dyncol_blob` must be either a valid dynamic columns blob (for example, `COLUMN_CREATE` returns such blob), or an empty string.
* `column_name` specifies the name of the column to be added. If `dyncol_blob` already has a column with this name, it will be overwritten.
* `value` specifies the new value for the column. Passing a NULL value will cause the column to be deleted.
* `as type` is optional. See the [datatypes](dynamic-columns.md#datatypes) section for a discussion about types.

The return value is a dynamic column blob after the modifications.

Typical usage:

```sql
UPDATE t1 SET dyncol_blob=COLUMN_ADD(dyncol_blob, "column_name", "value") 
  WHERE id=1;
```

Note: `COLUMN_ADD()` is a regular function (just like [CONCAT()](../../sql-functions/string-functions/concat.md)), hence, in order to update the value in the table you have to use the `UPDATE ... SET dynamic_col=COLUMN_ADD(dynamic_col, ....)` pattern.

#### COLUMN\_GET

```sql
COLUMN_GET(dyncol_blob, column_name as type);
```

Retrieves the value of a dynamic column by its name. If no column with the given name exists, `NULL` is returned.

`column_name as type` requires that one specify the datatype of the dynamic column they are reading.

This may seem counter-intuitive: Why would you need to specify which datatype they're retrieving? Can't the dynamic columns system figure the datatype from the data being stored?

The answer is: SQL is a statically typed language. The SQL interpreter needs to know the datatypes of all expressions before the query is run (for example, when one is using prepared statements and runs`"select COLUMN_GET(...)"`, the prepared statement API requires the server to inform the client about the datatype of the column being read before the query is executed and the server can see what datatype the column actually has).

See the [Datatypes](dynamic-columns.md#datatypes) section for more information about datatypes.

#### COLUMN\_DELETE

```sql
COLUMN_DELETE(dyncol_blob, column_name, column_name...);
```

Deletes a dynamic column with the specified name. Multiple names can be given.

The return value is a dynamic column blob after the modification.

#### COLUMN\_EXISTS

```sql
COLUMN_EXISTS(dyncol_blob, column_name);
```

Checks if a column with name `column_name` exists in `dyncol_blob`. If yes, return `1`, otherwise return `0`.

#### COLUMN\_LIST

```sql
COLUMN_LIST(dyncol_blob);
```

Returns a comma-separated list of column names. The names are quoted with backticks.

```sql
SELECT column_list(column_create('col1','val1','col2','val2'));
+---------------------------------------------------------+
| column_list(column_create('col1','val1','col2','val2')) |
+---------------------------------------------------------+
| `col1`,`col2`                                           |
+---------------------------------------------------------+
```

#### COLUMN\_CHECK

```sql
COLUMN_CHECK(dyncol_blob);
```

Checks if `dyncol_blob` is a valid packed dynamic columns blob. A return value of `1` means the blob is valid, a return value of `0` means it is not.

**Rationale:**\
Normally, you work with valid dynamic column blobs. Functions like`COLUMN_CREATE`, `COLUMN_ADD`, `COLUMN_DELETE` always return valid dynamic column blobs. However, if a dynamic column blob is accidentally truncated, or transcoded from one character set to another, it is corrupted. This function can be used to check if a value in a blob field is a valid dynamic column blob.

{% hint style="warning" %}
It is possible that a truncation cuts a Dynamic Column "clearly" so that `COLUMN_CHECK` does not notice the corruption, but, in any case of truncation, a warning is issued during value storing.
{% endhint %}

#### COLUMN\_JSON

```sql
COLUMN_JSON(dyncol_blob);
```

Returns a JSON representation of data in `dyncol_blob` :

```sql
SELECT item_name, COLUMN_JSON(dynamic_cols) FROM assets;
+-----------------+----------------------------------------+
| item_name       | COLUMN_JSON(dynamic_cols)              |
+-----------------+----------------------------------------+
| MariaDB T-shirt | {"size":"XL","color":"blue"}           |
| Thinkpad Laptop | {"color":"black","warranty":"3 years"} |
+-----------------+----------------------------------------+
```

Limitation: `COLUMN_JSON` decodes nested dynamic columns at a nesting level of not more than 10 levels deep. Dynamic columns that are nested deeper than 10 levels are shown as a `BINARY` string, without encoding.

### Nesting Dynamic Columns

It is possible to use nested dynamic columns by putting one dynamic column blob inside another. The `COLUMN_JSON` function will display nested columns.

```sql
SET @tmp= column_create('parent_column', 
  column_create('child_column', 12345));
Query OK, 0 rows affected (0.00 sec)

SELECT column_json(@tmp);
+------------------------------------------+
| column_json(@tmp)                        |
+------------------------------------------+
| {"parent_column":{"child_column":12345}} |
+------------------------------------------+

SELECT column_get(column_get(@tmp, 'parent_column' AS char), 
  'child_column' AS int);
+------------------------------------------------------------------------------+
| column_get(column_get(@tmp, 'parent_column' as char), 'child_column' as int) |
+------------------------------------------------------------------------------+
|                                                                        12345 |
+------------------------------------------------------------------------------+
```

If you are trying to get a nested dynamic column as a string, use `AS BINARY` as the last argument of `COLUMN_GET` . Otherwise, problems with character set conversion and illegal symbols are possible:

```sql
SELECT column_json( column_get(
  column_create('test1', 
    column_create('key1','value1','key2','value2','key3','value3')),
  'test1' AS BINARY));
```

### Datatypes

In SQL, one needs to define the type of each column in a table. Dynamic columns do not provide any way to declare a type in advance ("whenever there is a column 'weight', it should be integer" is not possible). However, each particular dynamic column value is stored together with its datatype.

The set of possible datatypes is mostly the same as that used by the [CAST](../../sql-functions/string-functions/cast.md) and [CONVERT](../../sql-functions/string-functions/convert.md) functions. However, note that there are currently some differences - see [MDEV-597](https://jira.mariadb.org/browse/MDEV-597).

| Type                | Dynamic column internal type | Description                                                                                                                 |
| ------------------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| BINARY\[(N)]        | DYN\_COL\_STRING             | (variable length string with binary charset)                                                                                |
| CHAR\[(N)]          | DYN\_COL\_STRING             | (variable length string with charset)                                                                                       |
| DATE                | DYN\_COL\_DATE               | (date - 3 bytes)                                                                                                            |
| DATETIME\[(D)]      | DYN\_COL\_DATETIME           | (date and time (with [microseconds](../../sql-functions/date-time-functions/microseconds-in-mariadb.md)) - 9 bytes)         |
| DECIMAL\[(M\[,D])]  | DYN\_COL\_DECIMAL            | (variable length binary decimal representation with MariaDB limitation)                                                     |
| DOUBLE\[(M,D)]      | DYN\_COL\_DOUBLE             | (64 bit double-precision floating point)                                                                                    |
| INTEGER             | DYN\_COL\_INT                | (variable length, up to 64-bit signed integer)                                                                              |
| SIGNED \[INTEGER]   | DYN\_COL\_INT                | (variable length, up to 64-bit signed integer)                                                                              |
| TIME\[(D)]          | DYN\_COL\_TIME               | (time (with [microseconds](../../sql-functions/date-time-functions/microseconds-in-mariadb.md), may be negative) - 6 bytes) |
| UNSIGNED \[INTEGER] | DYN\_COL\_UINT               | (variable length, up to 64bit unsigned integer)                                                                             |

#### A Note About Lengths

If you're running queries without specifying a maximum length (i.e. using #as CHAR#, not `as CHAR(n)`), MariaDB reports the maximum length of the result set column to be`53,6870,911` (bytes or characters?). This may cause excessive memory usage in some client libraries, because they try to pre-allocate a buffer of maximum result set width. If you suspect you're hitting this problem, use `CHAR(n)`\
whenever you're using `COLUMN_GET` in the select list.

```sql
SELECT COLUMN_GET(blob, 'colname' as CHAR) ...
```

### Client-side API

It is also possible to create or parse dynamic columns blobs on the client side. `libmysql` client library now includes an API for writing/reading dynamic column blobs. See [dynamic-columns-api](dynamic-column-api.md) for details.

### Limitations

| Description                                   | Limit                                                                                                                                           |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Max number of columns                         | 65535                                                                                                                                           |
| Maximum total length of packed dynamic column | [max\_allowed\_packet](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_allowed_packet) (1G) |

## See Also

* [Dynamic Columns](broken-reference/)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
