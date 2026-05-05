---
description: >-
  Batch insert mode uses cpimport for non-transactional LOAD DATA INFILE and
  INSERT INTO .. SELECT statements in MariaDB ColumnStore, controlled via
  infinidb_use_import_for_batchinsert.
hidden: true
---

# ColumnStore Batch Insert Mode

### Introduction

MariaDB ColumnStore has the ability to utilize the cpimport fast data import tool for non-transactional [LOAD DATA INFILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile) and [INSERT INTO SELECT FROM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) SQL statements. Using this method results in a significant increase in performance in loading data through these two SQL statements. This optimization is independent of the storage engine used for the tables in the select statement.

### Enable/disable using cpimport for batch insert

The `infinidb_use_import_for_batchinsert` variable is used to control if cpimport is used for these statements. This variable may be set as a default for the instance, set at the session level, or at the statement level by toggling this variable on and off.

To enable/disable the use of the use cpimport for batch insert at the session level, the following command is used. Once the session has ended, any subsequent session will return to the default for the instance.

```sql
set infinidb_use_import_for_batchinsert = n
where n is:
* 0 (disabled)
* 1 (enabled)
```

### Changing default delimiter for INSERT SELECT

* The `infinidb_import_for_batchinsert_delimiter` variable is used internally by MariaDB ColumnStore on a non-transactional `INSERT INTO SELECT FROM` statement as the default delimiter passed to the cpimport tool. With a default value ascii 7, there should be no need to change this value unless your data contains ASCII 7 values.

To change this variable value at the at the session level, the following command is used. Once the session has ended, any subsequent session will return to the default for the instance.

```sql
set infinidb_import_for_batchinsert_delimiter = ascii_value
where ascii_value is an ascii value representation of the delimiter desired.
```

Note that this setting may cause issues with multi-byte character set data. It is recommended to utilize `UTF8` files directly with cpimport.

### Version buffer file management

If the following error is received, most likely with a transaction `LOAD DATA INFILE or INSERT INTO SELECT` then it is recommended to break up the load into multiple smaller chunks, increase the `VersionBufferFileSize` setting, or consider a non-transactional `LOAD DATA INFILE` or to use cpimport.

```sql
ERROR 1815 (HY000) at line 1 in file: 'ldi.sql': Internal error: CAL0006: IDB-2008: The version buffer overflowed. Increase VersionBufferFileSize or limit the rows to be processed.
```

The `VersionBufferFileSize` setting is updated in the `ColumnStore.xml,` typically located under `/usr/local/mariadb/columnstore/etc`. This dictates the size of the version buffer file on disk, which provides DML transactional consistency. The default value is '1GB' which reserves up to a 1 Gigabyte file size. Modify this on the PM1 node and restart the system if you require a larger value.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
