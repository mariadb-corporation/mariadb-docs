---
description: >-
  Create a dynamic column blob. This function generates a binary string
  containing specified column names and values for storage in a BLOB.
---

# COLUMN\_CREATE

## Syntax

```sql
COLUMN_CREATE(column_nr, value [as type], [column_nr, value [as type]]...)
COLUMN_CREATE(column_name, value [as type], [column_name, value [as type]]...)
```

## Description

Returns a [dynamic columns](../../../sql-structure/nosql/dynamic-columns.md) blob that stores the specified columns with values.

The return value is suitable for

* storing in a table;
* further modification with other dynamic columns functions.

The **`as type`** part allows one to specify the value type. In most cases, this is redundant because MariaDB will be able to deduce the type of the value. Explicit type specification may be needed when the type of the value is not apparent. For example, a literal `'2012-12-01'` has a CHAR type by default, one will need to specify `'2012-12-01' AS DATE` to have it stored as a date. See [Dynamic Columns:Datatypes](../../../sql-structure/nosql/dynamic-columns.md#datatypes) for further details.

## Examples

```sql
INSERT INTO tbl SET dyncol_blob=COLUMN_CREATE("column_name", "value");
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
