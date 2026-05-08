---
description: >-
  mysql_stmt_affected_rows returns the number of rows affected by the last
  INSERT, UPDATE, DELETE, or REPLACE prepared statement, or -1 if the
  statement failed.
---

# mysql\_stmt\_affected\_rows

## Syntax

```c
my_ulonglong mysql_stmt_affected_rows(MYSQL_STMT * stmt);
```

* `stmt` - a statement handle, which was previously allocated by [mysql\_stmt\_init().](mysql_stmt_init.md)

## Description

Returns the number of affected rows by the last prepared statement associated with mysql, if the operation was an "upsert" ([INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert), [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update), [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) or [REPLACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/replace)) statement, or -1 if the last prepared statement failed.

{% hint style="info" %}
When using `UPDATE`, MariaDB will not update columns where the new value is the same as the old value. This creates the possibility that `mysql_stmt_affected_rows()` may not equal the number of rows matched, only the number of rows that were literally affected by the query.

The [REPLACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/replace) statement first deletes the record with the same primary key and then inserts the new record. This function returns the number of deleted records in addition to the number of inserted records.
{% endhint %}

## See Also

* [mysql\_stmt\_insert\_id()](mysql_stmt_insert_id.md)

{% @marketo/form formId="4316" %}
