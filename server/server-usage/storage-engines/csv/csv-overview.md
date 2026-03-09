---
description: >-
  The CSV Storage Engine stores data in comma-separated values format text
  files, making it easy to exchange data with other applications.
---

# CSV Overview

The CSV Storage Engine can read and append to files stored in CSV (comma-separated-values) format.

## The CSV storage engine and logging to tables

The CSV storage engine is the default storage engine when using [logging of SQL queries](../../../server-management/server-monitoring-logs/writing-logs-into-tables.md) to tables.

```bash
mysqld --log-output=table
```

## CSV Storage Engine files

When you create a table using the CSV storage engine, three files are created:

* `<table_name>.frm`
* `<table_name>.CSV`
* `<table_name>.CSM`

The `.frm` file is the table format file.

The `.CSV` file is a plain text file. Data you enter into the table is stored as plain text in comma-separated-values format.

The `.CSM` file stores metadata about the table such as the state and the number of rows in the table.

## Limitations

* CSV tables do not support indexing.
* CSV tables cannot be partitioned.
* Columns in CSV tables must be declared as NOT NULL.
* No [transactions](../../../reference/sql-statements/transactions/).
* The original CSV-format does not enable IETF-compatible parsing of embedded quote and comma characters. From [MariaDB 10.1.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.8), it is possible to do so by setting the [IETF\_QUOTES](../../../reference/sql-statements/data-definition/create/create-table.md#ietf_quotes) option when creating a table.

## Examples

Forgetting to add NOT NULL:

```sql
CREATE TABLE csv_test (x INT, y DATE, z CHAR(10)) ENGINE=CSV;
ERROR 1178 (42000): The storage engine for the table doesn't support nullable columns
```

Creating, inserting and selecting:

```sql
CREATE TABLE csv_test (
  x INT NOT NULL, y DATE NOT NULL, z CHAR(10) NOT NULL
  ) ENGINE=CSV;
```

```sql
INSERT INTO csv_test VALUES
    (1,CURDATE(),'one'),
    (2,CURDATE(),'two'),
    (3,CURDATE(),'three');
```

```sql
SELECT * FROM csv_test;
+---+------------+-------+
| x | y          | z     |
+---+------------+-------+
| 1 | 2011-11-16 | one   |
| 2 | 2011-11-16 | two   |
| 3 | 2011-11-16 | three |
+---+------------+-------+
```

Viewing in a text editor:

```bash
$ cat csv_test.CSV
1,"2011-11-16","one"
2,"2011-11-16","two"
3,"2011-11-16","three"
```

## See Also

* [Checking and Repairing CSV Tables](checking-and-repairing-csv-tables.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
