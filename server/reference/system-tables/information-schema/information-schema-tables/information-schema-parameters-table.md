---
description: >-
  The Information Schema PARAMETERS table stores information about parameters
  for stored procedures and functions, including data types and modes.
---

# Information Schema PARAMETERS Table

The [Information Schema](../) `PARAMETERS` table stores information about [stored procedures](../../../../server-usage/stored-routines/stored-procedures/) and [stored functions](../../../../server-usage/stored-routines/stored-functions/) parameters.

It contains the following columns:

| Column                     | Description                                                                                                                                                        |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| SPECIFIC\_CATALOG          | Always def.                                                                                                                                                        |
| SPECIFIC\_SCHEMA           | Database name containing the stored routine parameter.                                                                                                             |
| SPECIFIC\_NAME             | Stored routine name.                                                                                                                                               |
| ORDINAL\_POSITION          | Ordinal position of the parameter, starting at 1. 0 for a function RETURNS clause.                                                                                 |
| PARAMETER\_DEFAULT         | Displays default values for stored routine parameters.                                                                                                             |
| PARAMETER\_MODE            | One of IN, OUT, INOUT or NULL for RETURNS.                                                                                                                         |
| PARAMETER\_NAME            | Name of the parameter, or NULL for RETURNS.                                                                                                                        |
| DATA\_TYPE                 | The column's [data type](../../../data-types/).                                                                                                                    |
| CHARACTER\_MAXIMUM\_LENGTH | Maximum length.                                                                                                                                                    |
| CHARACTER\_OCTET\_LENGTH   | Same as the CHARACTER\_MAXIMUM\_LENGTH except for multi-byte [character sets](../../../data-types/string-data-types/character-sets/).                              |
| NUMERIC\_PRECISION         | For numeric types, the precision (number of significant digits) for the column. NULL if not a numeric field.                                                       |
| NUMERIC\_SCALE             | For numeric types, the scale (significant digits to the right of the decimal point). NULL if not a numeric field.                                                  |
| DATETIME\_PRECISION        | Fractional-seconds precision, or NULL if not a [time data type](../../../data-types/date-and-time-data-types/).                                                    |
| CHARACTER\_SET\_NAME       | [Character set](../../../data-types/string-data-types/character-sets/) if a non-binary [string data type](../../../data-types/string-data-types/), otherwise NULL. |
| COLLATION\_NAME            | [Collation](../../../data-types/string-data-types/character-sets/) if a non-binary [string data type](../../../data-types/string-data-types/), otherwise NULL.     |
| DTD\_IDENTIFIER            | Description of the data type.                                                                                                                                      |
| ROUTINE\_TYPE              | PROCEDURE or FUNCTION.                                                                                                                                             |
| PARAMETER\_DEFAULT         | Default parameter value. From [MariaDB 12.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/12.2/mariadb-12.2-changes-and-improvements).          |

Information from this table is similar to that found in the `param_list` column in the [mysql.proc](../../the-mysql-database-tables/mysql-proc-table.md) table, and the output of the [SHOW CREATE PROCEDURE](../../../sql-statements/administrative-sql-statements/show/show-create-procedure.md) and [SHOW CREATE FUNCTION](../../../sql-statements/administrative-sql-statements/show/show-create-function.md) statements.

To obtain information about the routine itself, you can query the [Information Schema ROUTINES table](information-schema-routines-table.md).

## Example

```sql
SELECT * FROM information_schema.PARAMETERS
LIMIT 1 \G
********************** 1. row **********************
        SPECIFIC_CATALOG: def
         SPECIFIC_SCHEMA: accounts
           SPECIFIC_NAME: user_counts
        ORDINAL_POSITION: 1
          PARAMETER_MODE: IN
          PARAMETER_NAME: user_order
               DATA_TYPE: varchar
CHARACTER_MAXIMUM_LENGTH: 255
  CHARACTER_OCTET_LENGTH: 765
       NUMERIC_PRECISION: NULL
           NUMERIC_SCALE: NULL
      DATETIME_PRECISION: NULL
      CHARACTER_SET_NAME: utf8
          COLLATION_NAME: utf8_general_ci
          DTD_IDENTIFIER: varchar(255)
            ROUTINE_TYPE: PROCEDURE
       PARAMETER_DEFAULT: NULL
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
