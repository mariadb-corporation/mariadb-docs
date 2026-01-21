---
description: >-
  Retrieve a dynamic column value. This function extracts a specific column's
  value from a dynamic column blob, casting it to a specified type.
---

# COLUMN\_GET

## Syntax

```sql
COLUMN_GET(dyncol_blob, column_nr as type)
COLUMN_GET(dyncol_blob, column_name as type)
```

## Description

Gets the value of a [dynamic column](../../../sql-structure/nosql/dynamic-columns.md) by its name. If no column with the given name exists, `NULL` will be returned.

**`column_name as type`** requires that one specify the datatype of the dynamic column they are reading.

This may seem counter-intuitive: why would one need to specify which datatype they're retrieving? Can't the dynamic columns system figure the datatype from the data being stored?

The answer is: SQL is a statically-typed language. The SQL interpreter needs to know the datatypes of all expressions before the query is run (for example, when one is using prepared statements and runs `"select COLUMN_GET(...)"`, the prepared statement API requires the server to inform the client about the datatype of the column being read before the query is executed and the server can see what datatype the column actually has).

### Lengths

Suppose running a query like this:

```sql
SELECT COLUMN_GET(BLOB, 'colname' AS CHAR) ...
```

Without specifying a maximum length (i.e. using `as CHAR`, not `as CHAR(n)`), MariaDB will report the maximum length of the result set column to be 16,777,216. This may cause excessive memory usage in some client libraries, because they try to pre-allocate a buffer of maximum result set width. To avoid this problem, use CHAR(n) whenever you're using COLUMN\_GET in the select list.

See [Dynamic Columns:Datatypes](../../../sql-structure/nosql/dynamic-columns.md#datatypes) for more information about datatypes.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
