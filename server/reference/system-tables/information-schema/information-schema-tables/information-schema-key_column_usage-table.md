---
description: >-
  The Information Schema KEY_COLUMN_USAGE table details which columns in a table
  are constrained by keys, such as primary or foreign keys.
---

# Information Schema KEY\_COLUMN\_USAGE Table

The [Information Schema](../) `KEY_COLUMN_USAGE` table shows which key columns have constraints.

It contains the following columns:

| Column                           | Description                                                                                                                                                 |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CONSTRAINT\_CATALOG              | Always def.                                                                                                                                                 |
| CONSTRAINT\_SCHEMA               | Database name of the constraint.                                                                                                                            |
| CONSTRAINT\_NAME                 | Name of the constraint (PRIMARY for the primary key).                                                                                                       |
| TABLE\_CATALOG                   | Always #def.                                                                                                                                                |
| TABLE\_SCHEMA                    | Database name of the column constraint.                                                                                                                     |
| TABLE\_NAME                      | Table name of the column constraint.                                                                                                                        |
| COLUMN\_NAME                     | Column name of the constraint.                                                                                                                              |
| ORDINAL\_POSITION                | Position of the column within the constraint.                                                                                                               |
| POSITION\_IN\_UNIQUE\_CONSTRAINT | For [foreign keys](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys.md), the position in the unique constraint. |
| REFERENCED\_TABLE\_SCHEMA        | For foreign keys, the referenced database name.                                                                                                             |
| REFERENCED\_TABLE\_NAME          | For foreign keys, the referenced table name.                                                                                                                |
| REFERENCED\_COLUMN\_NAME         | For foreign keys, the referenced column name.                                                                                                               |

## Example

```sql
SELECT * FROM information_schema.KEY_COLUMN_USAGE LIMIT 1 \G
********************** 1. row **********************
           CONSTRAINT_CATALOG: def
            CONSTRAINT_SCHEMA: my_website
              CONSTRAINT_NAME: PRIMARY
                TABLE_CATALOG: def
                 TABLE_SCHEMA: users
                  COLUMN_NAME: user_id
             ORDINAL_POSITION: 1
POSITION_IN_UNIQUE_CONSTRAINT: NULL
      REFERENCED_TABLE_SCHEMA: NULL
        REFERENCED_TABLE_NAME: NULL
       REFERENCED_COLUMN_NAME: NULL
```

## See Also

* [Finding Tables Without Primary Keys](../../../../mariadb-quickstart-guides/mariadb-indexes-guide.md#finding-tables-without-primary-keys)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
