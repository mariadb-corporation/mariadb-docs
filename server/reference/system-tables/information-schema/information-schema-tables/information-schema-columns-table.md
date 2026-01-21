---
description: >-
  The Information Schema COLUMNS table provides information about columns in
  each table on the server, including data types, defaults, and nullability.
---

# Information Schema COLUMNS Table

The [Information Schema](../) `COLUMNS` table provides information about columns in each table on the server.

It contains the following columns:

| Column                          | Description                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TABLE\_CATALOG                  | Always contains the string 'def'.                                                                                                                                                                                                                                                                                                                   |
| TABLE\_SCHEMA                   | Database name.                                                                                                                                                                                                                                                                                                                                      |
| TABLE\_NAME                     | Table name.                                                                                                                                                                                                                                                                                                                                         |
| COLUMN\_NAME                    | Column name.                                                                                                                                                                                                                                                                                                                                        |
| ORDINAL\_POSITION               | Column position in the table. Can be used for ordering.                                                                                                                                                                                                                                                                                             |
| COLUMN\_DEFAULT                 | Default value for the column. Literals are quoted to distinguish them from expressions. NULL means that the column has no default.                                                                                                                                                                                                                  |
| IS\_NULLABLE                    | Whether the column can contain NULLs.                                                                                                                                                                                                                                                                                                               |
| DATA\_TYPE                      | The column's [data type](../../../data-types/).                                                                                                                                                                                                                                                                                                     |
| CHARACTER\_MAXIMUM\_LENGTH      | Maximum length.                                                                                                                                                                                                                                                                                                                                     |
| CHARACTER\_OCTET\_LENGTH        | Same as the CHARACTER\_MAXIMUM\_LENGTH except for multi-byte [character sets](../../../data-types/string-data-types/character-sets/).                                                                                                                                                                                                               |
| NUMERIC\_PRECISION              | For numeric types, the precision (number of significant digits) for the column. NULL if not a numeric field.                                                                                                                                                                                                                                        |
| NUMERIC\_SCALE                  | For numeric types, the scale (significant digits to the right of the decimal point). NULL if not a numeric field.                                                                                                                                                                                                                                   |
| DATETIME\_PRECISION             | Fractional-seconds precision, or NULL if not a [time data type](../../../data-types/date-and-time-data-types/).                                                                                                                                                                                                                                     |
| CHARACTER\_SET\_NAME            | [Character set](../../../data-types/string-data-types/character-sets/) if a non-binary [string data type](../../../data-types/string-data-types/), otherwise NULL.                                                                                                                                                                                  |
| COLLATION\_NAME                 | [Collation](../../../data-types/string-data-types/character-sets/) if a non-binary [string data type](../../../data-types/string-data-types/), otherwise NULL.                                                                                                                                                                                      |
| COLUMN\_TYPE                    | Column definition, a MySQL and MariaDB extension.                                                                                                                                                                                                                                                                                                   |
| COLUMN\_KEY                     | Index type. PRI for primary key, UNI for unique index, MUL for multiple index. A MySQL and MariaDB extension.                                                                                                                                                                                                                                       |
| EXTRA                           | Additional information about a column, for example whether the column is an [invisible column](../../../sql-statements/data-definition/create/invisible-columns.md), or WITHOUT SYSTEM VERSIONING if the table is not a [system-versioned table](../../../sql-structure/temporal-tables/system-versioned-tables.md). A MySQL and MariaDB extension. |
| PRIVILEGES                      | Which privileges you have for the column. A MySQL and MariaDB extension.                                                                                                                                                                                                                                                                            |
| COLUMN\_COMMENT                 | Column comments.                                                                                                                                                                                                                                                                                                                                    |
| IS\_GENERATED                   | Indicates whether the column value is [generated (virtual, or computed)](../../../sql-statements/data-definition/create/generated-columns.md). Can be ALWAYS or NEVER.                                                                                                                                                                              |
| GENERATION\_EXPRESSION          | The expression used for computing the column value in a [generated (virtual, or computed)](../../../sql-statements/data-definition/create/generated-columns.md) column.                                                                                                                                                                             |
| IS\_SYSTEM\_TIME\_PERIOD\_START | From [MariaDB 11.4.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-1-release-notes).                                                                                                                                                                                                            |
| IS\_SYSTEM\_TIME\_PERIOD\_END   | From [MariaDB 11.4.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-1-release-notes).                                                                                                                                                                                                            |

It provides information similar to, but more complete, than [SHOW COLUMNS](../../../sql-statements/administrative-sql-statements/show/show-columns.md) and [mariadb-show](../../../../clients-and-utilities/administrative-tools/mariadb-show.md).

## Examples

```sql
SELECT * FROM information_schema.COLUMNS\G
...
*************************** 9. row ***************************
           TABLE_CATALOG: def
            TABLE_SCHEMA: test
              TABLE_NAME: t2
             COLUMN_NAME: j
        ORDINAL_POSITION: 1
          COLUMN_DEFAULT: NULL
             IS_NULLABLE: YES
               DATA_TYPE: longtext
CHARACTER_MAXIMUM_LENGTH: 4294967295
  CHARACTER_OCTET_LENGTH: 4294967295
       NUMERIC_PRECISION: NULL
           NUMERIC_SCALE: NULL
      DATETIME_PRECISION: NULL
      CHARACTER_SET_NAME: utf8mb4
          COLLATION_NAME: utf8mb4_bin
             COLUMN_TYPE: longtext
              COLUMN_KEY: 
                   EXTRA: 
              PRIVILEGES: select,insert,update,references
          COLUMN_COMMENT: 
            IS_GENERATED: NEVER
   GENERATION_EXPRESSION: NULL
...
```

```sql
CREATE TABLE t (
  s1 VARCHAR(20) DEFAULT 'ABC',
  s2 VARCHAR(20) DEFAULT (concat('A','B')),
  s3 VARCHAR(20) DEFAULT ("concat('A','B')"),
  s4 VARCHAR(20),
  s5 VARCHAR(20) DEFAULT NULL,
  s6 VARCHAR(20) NOT NULL,
  s7 VARCHAR(20) DEFAULT 'NULL' NULL,
  s8 VARCHAR(20) DEFAULT 'NULL' NOT NULL
);

SELECT 
  table_name, 
  column_name, 
  ordinal_position, 
  column_default,
  column_default IS NULL
FROM information_schema.COLUMNS
WHERE table_schema=DATABASE()
AND TABLE_NAME='t';
+------------+-------------+------------------+-----------------------+------------------------+
| table_name | column_name | ordinal_position | column_default        | column_default IS NULL |
+------------+-------------+------------------+-----------------------+------------------------+
| t          | s1          |                1 | 'ABC'                 |                      0 |
| t          | s2          |                2 | concat('A','B')       |                      0 |
| t          | s3          |                3 | 'concat(''A'',''B'')' |                      0 |
| t          | s4          |                4 | NULL                  |                      0 |
| t          | s5          |                5 | NULL                  |                      0 |
| t          | s6          |                6 | NULL                  |                      1 |
| t          | s7          |                7 | 'NULL'                |                      0 |
| t          | s8          |                8 | 'NULL'                |                      0 |
+------------+-------------+------------------+-----------------------+------------------------+
```

In the results above, the two single quotes in `concat(''A'',''B'')` indicate an escaped single quote - see [string-literals](../../../sql-structure/sql-language-structure/string-literals.md). Note that while [mariadb client](../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) appears to show the same default value for columns `s5` and `s6`, the first is a 4-character string "NULL", while the second is the SQL `NULL` value.

{% hint style="info" %}
The following statement is available from MariaDB 11.3.
{% endhint %}

```sql
CREATE TABLE t(
     x INT,
     start_timestamp TIMESTAMP(6) GENERATED ALWAYS AS ROW START,
     end_timestamp TIMESTAMP(6) GENERATED ALWAYS AS ROW END,
     PERIOD FOR SYSTEM_TIME(start_timestamp, end_timestamp)
) WITH SYSTEM VERSIONING;

SELECT TABLE_NAME, COLUMN_NAME, ORDINAL_POSITION, 
  IS_SYSTEM_TIME_PERIOD_START, IS_SYSTEM_TIME_PERIOD_END 
  FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='t'\G
*************************** 1. row ***************************
                 TABLE_NAME: t
                COLUMN_NAME: x
           ORDINAL_POSITION: 1
IS_SYSTEM_TIME_PERIOD_START: NO
  IS_SYSTEM_TIME_PERIOD_END: NO
*************************** 2. row ***************************
                 TABLE_NAME: t
                COLUMN_NAME: start_timestamp
           ORDINAL_POSITION: 2
IS_SYSTEM_TIME_PERIOD_START: YES
  IS_SYSTEM_TIME_PERIOD_END: NO
*************************** 3. row ***************************
                 TABLE_NAME: t
                COLUMN_NAME: end_timestamp
           ORDINAL_POSITION: 3
IS_SYSTEM_TIME_PERIOD_START: NO
  IS_SYSTEM_TIME_PERIOD_END: YES
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
