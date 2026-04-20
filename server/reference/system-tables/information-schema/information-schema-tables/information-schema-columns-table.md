---
description: >-
  The Information Schema COLUMNS table provides information about columns in
  each table on the server, including data types, defaults, and nullability.
---

# Information Schema COLUMNS Table

The [Information Schema](../) `COLUMNS` table provides information about columns in each table on the server.

It contains the following columns:

<table data-header-hidden="false" data-header-sticky><thead><tr><th>Column</th><th>Description</th></tr></thead><tbody><tr><td>TABLE_CATALOG</td><td>Always contains the string <code>'def'</code>.</td></tr><tr><td>TABLE_SCHEMA</td><td>Database name.</td></tr><tr><td>TABLE_NAME</td><td>Table name.</td></tr><tr><td>COLUMN_NAME</td><td>Column name.</td></tr><tr><td>ORDINAL_POSITION</td><td>Column position in the table. Can be used for ordering.</td></tr><tr><td>COLUMN_DEFAULT</td><td>Default value for the column. Literals are quoted to distinguish them from expressions. <code>NULL</code> means that the column has no default.</td></tr><tr><td>IS_NULLABLE</td><td>Whether the column can contain <code>NULL</code> values.</td></tr><tr><td>DATA_TYPE</td><td>The column's <a href="../../../data-types/">data type</a>.</td></tr><tr><td>CHARACTER_MAXIMUM_LENGTH</td><td>Maximum length.</td></tr><tr><td>CHARACTER_OCTET_LENGTH</td><td>Same as the <code>CHARACTER_MAXIMUM_LENGTH</code> except for multi-byte <a href="../../../data-types/string-data-types/character-sets/">character sets</a>.</td></tr><tr><td>NUMERIC_PRECISION</td><td>For numeric types, the precision (number of significant digits) for the column. <code>NULL</code> if not a numeric field.</td></tr><tr><td>NUMERIC_SCALE</td><td>For numeric types, the scale (significant digits to the right of the decimal point). <code>NULL</code> if not a numeric field.</td></tr><tr><td>DATETIME_PRECISION</td><td>Fractional-seconds precision, or <code>NULL</code> if not a <a href="../../../data-types/date-and-time-data-types/">time data type</a>.</td></tr><tr><td>CHARACTER_SET_NAME</td><td><a href="../../../data-types/string-data-types/character-sets/">Character set</a> if a non-binary <a href="../../../data-types/string-data-types/">string data type</a>, otherwise <code>NULL</code>.</td></tr><tr><td>COLLATION_NAME</td><td><a href="../../../data-types/string-data-types/character-sets/">Collation</a> if a non-binary <a href="../../../data-types/string-data-types/">string data type</a>, otherwise <code>NULL</code>.</td></tr><tr><td>COLUMN_TYPE</td><td>Column definition, a MySQL and MariaDB extension.</td></tr><tr><td>COLUMN_KEY</td><td>Index type. <code>PRI</code> for primary key, <code>UNI</code> for unique index, <code>MUL</code> for multiple index. A MySQL and MariaDB extension.</td></tr><tr><td>CREATE_OPTIONS</td><td>Extra <a href="../../../sql-statements/data-definition/create/create-table.md">CREATE TABLE</a> options.This column is available from MariaDB 13.0.</td></tr><tr><td>EXTRA</td><td>Additional information about a column, for example whether the column is an <a href="../../../sql-statements/data-definition/create/invisible-columns.md">invisible column</a>, or <code>WITHOUT SYSTEM VERSIONING</code> if the table is not a <a href="../../../sql-structure/temporal-tables/system-versioned-tables.md">system-versioned table</a>. A MySQL and MariaDB extension.</td></tr><tr><td>PRIVILEGES</td><td>Which privileges you have for the column. A MySQL and MariaDB extension.</td></tr><tr><td>COLUMN_COMMENT</td><td>Column comments.</td></tr><tr><td>IS_GENERATED</td><td>Indicates whether the column value is <a href="../../../sql-statements/data-definition/create/generated-columns.md">generated (virtual, or computed)</a>. Can be <code>ALWAYS</code> or <code>NEVER</code>.</td></tr><tr><td>GENERATION_EXPRESSION</td><td>The expression used for computing the column value in a <a href="../../../sql-statements/data-definition/create/generated-columns.md">generated (virtual, or computed)</a> column.</td></tr><tr><td>IS_SYSTEM_TIME_PERIOD_START</td><td>From <a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.1">MariaDB 11.4.1</a>.</td></tr><tr><td>IS_SYSTEM_TIME_PERIOD_END</td><td>From <a href="https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/11.4.1">MariaDB 11.4.1</a>.</td></tr></tbody></table>

It provides information similar to, but more complete, than [SHOW COLUMNS](../../../sql-statements/administrative-sql-statements/show/show-columns.md) or output from [mariadb-show](../../../../clients-and-utilities/administrative-tools/mariadb-show.md).

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
