---
description: >-
  DROP TABLE for MariaDB ColumnStore deletes a table from the database; the
  ColumnStore-specific RESTRICT clause limits the drop to the front end for
  sync purposes.
---

# ColumnStore DROP TABLE

The [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table) statement deletes a table from ColumnStore.

## Syntax

```sql
DROP  TABLE [IF EXISTS] 
    tbl_name 
    [RESTRICT ]
```

The `RESTRICT` clause limits the table to being dropped in the front end only. This could be useful when the table has been dropped on one user module and needs to be synced to others.

The following statement drops the _orders_ table on the front end only:

```sql
DROP TABLE orders RESTRICT;
```

## See also

* [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
