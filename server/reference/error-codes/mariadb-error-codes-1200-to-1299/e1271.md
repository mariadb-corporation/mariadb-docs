# Error 1271: Illegal mix of collations for operation

| Error Code | SQLSTATE | Error                            | Description                                  |
| ---------- | -------- | -------------------------------- | -------------------------------------------- |
| 1271       | HY000    | ER\_CANT\_AGGREGATE\_NCOLLATIONS | Illegal mix of collations for operation '%s' |

## Possible Causes and Solutions

This error occurs when attempting to combine (e.g., using UNION) two tables where the same column has different collation types. To resolve this, one of the column's collations must be adjusted to match the other.

## Diagnosing Collation Types

To identify the collation type of a column, you can use the following query:

```
SELECT COLUMN_NAME, COLLATION_NAME
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'your_database_name'
AND TABLE_NAME = 'your_table_name';
```

For a comprehensive comparison, you might want to join `table1` and `table2` based on the `COLUMN_NAME` to visually inspect the collation differences.

## Resolving Collation Conflicts

Assuming one column is using `utf8mb3_general_ci` and the other `utf8mb3_unicode_ci`, you can standardize the collation for a particular operation as follows:

```
FROM table;
SELECT COLUMN COLLATE utf8mb3_unicode_ci
```

This command temporarily adjusts the collation for `column` during the SELECT operation to `utf8mb3_unicode_ci`, ensuring consistent collation for the operation.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
