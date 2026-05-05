---
description: >-
  LOAD DATA INFILE for MariaDB ColumnStore loads rows from a text file into a
  table at high speed; auto-translated to a cpimport bulk load when batch
  insert mode is on.
---

# ColumnStore LOAD DATA INFILE

## Overview

The `LOAD DATA INFILE` statement reads rows from a text file into a table at a very high speed. The file name must be given as a literal string.

```sql
LOAD DATA [LOCAL] INFILE 'file_name' 
  INTO TABLE tbl_name
  [CHARACTER SET charset_name]
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

* ColumnStore ignores the `ON DUPLICATE KEY` clause.
* Non-transactional `LOAD DATA INFILE` is directed to ColumnStores cpimport tool by default, which significantly increases performance.
* Transactional `LOAD DATA INFILE` statements (that is, with `AUTOCOMMIT` off or after a `START TRANSACTION`) are processed through normal DML processes.
* Use cpimport for importing `UTF-8` data that contains multi-byte values

The following example loads data into a simple 5- column table: A file named `/simpletable.tbl`_`has` the following data in it._

```sql
1|100|1000|10000|Test Number 1|
2|200|2000|20000|Test Number 2|
3|300|3000|30000|Test Number 3|
```

The data can then be loaded into the simpletable table with the following syntax:

```sql
LOAD DATA INFILE 'simpletable.tbl' INTO TABLE simpletable FIELDS TERMINATED BY '|'
```

If the default mode is set to use cpimport internally, any output error files will be written to `/var/log/mariadb/columnstore/cpimport/` directory. It can be consulted for troubleshooting any errors reported.

## See Also

[LOAD DATA INFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
