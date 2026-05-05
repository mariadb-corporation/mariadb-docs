---
description: >-
  Data ingestion options for MariaDB ColumnStore: cpimport for fast bulk
  loads, LOAD DATA INFILE, batch insert mode, INSERT INTO .. SELECT, DML, plus
  Bulk Write SDK and streaming adapters.

---

# Data Ingestion Methods & Tools

ColumnStore provides several mechanisms to ingest data:

* [cpimport](columnstore-bulk-data-loading.md) provides the fastest performance for inserting data and ability to route data to particular PrimProc nodes. Normally, this should be the default choice for loading data .
* [LOAD DATA INFILE](../../reference/data-manipulation-statements/columnstore-load-data-infile.md) provides another means of bulk inserting data.
  * By default, with autocommit on, it internally streams the data to an instance of the `cpimport` process. 
  * In transactional mode, DML inserts are performed, which is significantly slower and also consumes both binlog transaction files and ColumnStore VersionBuffer files.
* DML, i.e. `INSERT`, `UPDATE`, and `DELETE`, provide row-level changes. ColumnStore is optimized towards bulk modifications, so these operations are slower than they would be in, for instance, InnoDB.
  * Currently ColumnStore does not support operating as a replication replica target.
  * Bulk DML operations will in general perform better than multiple individual statements.
    * [INSERT INTO SELECT](columnstore-batch-insert-mode.md) with autocommit behaves similarly to `LOAD DATE INFILE` because, internally, it is mapped to `cpimport` for higher performance.
    * Bulk update operations based on a join with a small staging table can be relatively fast, especially if updating a single column.
* Using ColumnStore Bulk Write SDK or [ColumnStore Streaming Data Adapters](columnstore-streaming-data-adapters.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
