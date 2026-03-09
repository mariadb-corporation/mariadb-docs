---
description: >-
  Complete guide to SELECT queries in MariaDB. Complete syntax reference for
  joins, subqueries, WHERE clauses, GROUP BY, and aggregate functions.
---

# SELECT INTO OUTFILE

## Syntax

```sql
SELECT ... INTO OUTFILE 'file_name'
        [CHARACTER SET charset_name]
        [export_options]

export_options:
    [{FIELDS | COLUMNS}
        [TERMINATED BY 'string']
        [[OPTIONALLY] ENCLOSED BY 'char']
        [ESCAPED BY 'char']
    ]
    [LINES
        [STARTING BY 'string']
        [TERMINATED BY 'string']
    ]
```

## Description

`SELECT INTO OUTFILE` writes the resulting rows to a file, and allows the use of column and row terminators to specify a particular output format. The default is to terminate fields with tabs () and lines with newlines ().

The file must not exist. It cannot be overwritten. A user needs the [FILE](../../account-management-sql-statements/grant.md#global-privileges) privilege to run this statement. Also, MariaDB needs permission to write files in the specified location. If the [secure\_file\_priv](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#secure_file_priv) system variable is set to a non-empty directory name, the file can only be written to that directory.

The [LOAD DATA INFILE](../inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) statement complements `SELECT INTO OUTFILE`.

### Character Sets

The `CHARACTER SET` clause specifies the [character set](../../../data-types/string-data-types/character-sets/) in which the results are to be written. Without the clause, no conversion takes place (the binary character set). In this case, if there are multiple character sets, the output will contain these too, and may not easily be able to be reloaded.

In cases where you have two servers using different character-sets, using `SELECT INTO OUTFILE` to transfer data from one to the other can have unexpected results. To ensure that MariaDB correctly interprets the escape sequences, use the `CHARACTER SET` clause on both the `SELECT INTO OUTFILE` statement and the subsequent [LOAD DATA INFILE](../inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) statement.

## Example

The following example produces a file in the CSV format:

```sql
SELECT customer_id, firstname, surname FROM customer
  INTO OUTFILE '/exportdata/customers.txt'
  FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
  LINES TERMINATED BY '\n';
```

The following ANSI syntax is also supported for simple `SELECT` without `UNION` :

```sql
SELECT customer_id, firstname, surname INTO OUTFILE '/exportdata/customers.txt'
  FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
  LINES TERMINATED BY '\n'
  FROM customers;
```

If you want to use the ANSI syntax with `UNION` or similar construct you have to use the syntax:

```sql
SELECT  * INTO OUTFILE "/tmp/skr3" 
FROM (SELECT * FROM t1 UNION SELECT * FROM t1);
```

## See Also

* [SELECT](select.md)
* [LOAD\_DATA()](../../../sql-functions/string-functions/load_file.md) function
* [LOAD DATA INFILE](../inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md)
* [SELECT INTO Variable](../../programmatic-compound-statements/selectinto.md)
* [SELECT INTO DUMPFILE](select-into-dumpfile.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
