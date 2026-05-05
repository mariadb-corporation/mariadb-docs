---
description: >-
  DELETE for MariaDB ColumnStore removes rows but does not reclaim disk space;
  use TRUNCATE, DROP PARTITION, or a CREATE/RENAME-based rebuild to recover
  space after deletes.
---

# ColumnStore DELETE

The `DELETE` statement is used to remove rows from tables.

## Syntax

```sql
DELETE 
 [FROM] tbl_name 
    [WHERE where_condition]
    [ORDER BY ...]
    [LIMIT row_count]
```

No disk space is recovered after a `DELETE`. `TRUNCATE` and `DROP PARTITION` can be used to recover space, or `CREATE TABLE`, loading only the remaining rows, then using DROP TABLE on the original table and `RENAME TABLE`.

`LIMIT` will limit the number of rows deleted, which will perform the `DELETE` more quickly. The `DELETE ... LIMIT` statement can then be performed multiple times to achieve the same effect as `DELETE` with no `LIMIT`.

The following statement deletes customer records with a customer key identification between 1001 and 1999:

```sql
DELETE FROM customer 
  WHERE custkey > 1000 AND custkey <2000
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
