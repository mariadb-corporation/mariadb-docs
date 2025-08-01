# ColumnStore Delete

The `DELETE` statement is used to remove rows from tables.

1. [Syntax "Syntax"](columnstore-delete.md#syntax)

## Syntax

```sql
DELETE 
 [FROM] tbl_name 
    [WHERE where_condition]
    [ORDER BY ...]
    [LIMIT row_count]
```

No disk space is recovered after a `DELETE`. `TRUNCATE` and `DROP PARTITION` can be used to recover space, or `CREATE TABLE`, loading only the remaining rows, then using DROP TABLE on the original table and `RENAME TABLE`.

`LIMIT` will limit the number of rows deleted, which will perform the `DELETE` more quickly. The `DELETE` ... `LIMIT` statement can then be performed multiple times to achieve the same effect as `DELETE` with no `LIMIT`.

The following statement deletes customer records with a customer key identification between 1001 and 1999:

```sql
DELETE FROM customer 
  WHERE custkey > 1000 AND custkey <2000
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
