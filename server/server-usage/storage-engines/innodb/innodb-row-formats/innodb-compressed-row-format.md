---
description: >-
  Learn about the COMPRESSED row format, which compresses data and index pages
  using algorithms like zlib to minimize storage footprint at the cost of CPU.
---

# InnoDB COMPRESSED Row Format

An alternative (and usually superior) way to compress InnoDB tables is by using [InnoDB Page Compression](../innodb-page-compression.md). See [Comparison with the COMPRESSED Row Format](../innodb-page-compression.md#comparison-with-the-compressed-row-format).

The `COMPRESSED` row format is similar to the `COMPACT` row format, but tables using the `COMPRESSED` row format can store even more data on overflow pages than tables using the `COMPACT` row format. This results in more efficient data storage than tables using the `COMPACT` row format, especially for tables containing columns using the [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md), [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md), [BLOB](../../../../reference/data-types/string-data-types/blob.md) and [TEXT](../../../../reference/data-types/string-data-types/text.md) data types.

The `COMPRESSED` row format also supports compression of all data and index pages.

## Supported Block Sizes

The Compressed row format supports the following block sizes:

| Block Size | KEY\_BLOCK\_SIZE Value |
| ---------- | ---------------------- |
| 1 KB       | 1                      |
| 2 KB       | 2                      |
| 4 KB       | 4                      |
| 8 KB       | 8                      |
| 16 KB      | 16                     |

If the `KEY_BLOCK_SIZE` table option is not specified, the block size defaults to half of [innodb\_page\_size](../../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_page_size). With the default 16 KB page size, the block size defaults to 8 KB.

For compression to be effective, the chosen block size should be smaller than the servers value of the [innodb\_page\_size](../../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_page_size) system variable.

## Supported Index Prefix Limits

The limit for indexing column values depends on the [innodb\_page\_size](../../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_page_size) value:

| Page Size | Index Prefix Limit |
| --------- | ------------------ |
| 16k       | 3072 bytes         |
| 8k        | 1536 bytes         |
| 4k        | 768 bytes          |

## Using the `COMPRESSED` Row Format

The Compressed row format does not efficiently use the InnoDB buffer pool, so it is not the recommended way to achieve InnoDB table compression. For more information about how to compress InnoDB tables, see [Configure InnoDB Page Compression](../innodb-page-compression.md#configuring-the-innodb-page-compression-algorithm).

An InnoDB table that uses the `COMPRESSED` row format can be created by setting the [ROW\_FORMAT](../../../../reference/sql-statements/data-definition/create/create-table.md#row_format) table option to `COMPRESSED` and by setting the [KEY\_BLOCK\_SIZE](../../../../reference/sql-statements/data-definition/create/create-table.md#key_block_size) table option to one of the following values in a [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) or [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/) statement, where the units are in `KB`.

`16k` is the default value of the [innodb\_page\_size](../innodb-system-variables.md#innodb_page_size) system variable, so using `16` will usually result in minimal compression unless one of the following is true:

* The table has many columns that can be stored in overflow pages, such as columns that use the [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md), [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md), [BLOB](../../../../reference/data-types/string-data-types/blob.md) and [TEXT](../../../../reference/data-types/string-data-types/text.md) data types.
* The server is using a non-default [innodb\_page\_size](../innodb-system-variables.md#innodb_page_size) value that is greater than `16k`.

The value of the [innodb\_page\_size](../innodb-system-variables.md#innodb_page_size) system variable can be set to `32k` and `64k`. This is especially useful because the larger page size permits more columns using the [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md), [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md), [BLOB](../../../../reference/data-types/string-data-types/blob.md) and [TEXT](../../../../reference/data-types/string-data-types/text.md) data types. Regardless, even when the value of the [innodb\_page\_size](../innodb-system-variables.md#innodb_page_size) system variable is set to some value higher than `16k`, `16` is still the maximum value for the [KEY\_BLOCK\_SIZE](../../../../reference/sql-statements/data-definition/create/create-table.md#key_block_size) table option for InnoDB tables using the `COMPRESSED` row format.

The `COMPRESSED` row format cannot be set as the default row format with the [innodb\_default\_row\_format](../innodb-system-variables.md#innodb_default_row_format) system variable.

The `COMPRESSED` row format is only supported by the `Barracuda` [file format](../innodb-file-format.md). In earlier versions, the `COMPRESSED` row format is only supported if the [InnoDB file format](../innodb-file-format.md) is `Barracuda`. Therefore, the [innodb\_file\_format](../innodb-system-variables.md#innodb_file_format) system variable must be set to `Barracuda` to use these row formats in those versions.

In earlier versions, the `COMPRESSED` row format is also only supported if the table is in a [file per-table](../innodb-tablespaces/innodb-file-per-table-tablespaces.md) tablespace. Therefore, the [innodb\_file\_per\_table](../innodb-system-variables.md#innodb_file_per_table) system variable must be set to `ON` to use this row format in those versions.

It is also recommended to set the [innodb\_strict\_mode](../innodb-system-variables.md#innodb_strict_mode) system variable to `ON` when using this row format.

InnoDB automatically uses the `COMPRESSED` row format for a table if the [KEY\_BLOCK\_SIZE](../../../../reference/sql-statements/data-definition/create/create-table.md#key_block_size) table option is set to some value in a [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) or [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/) statement:

```sql
SET SESSION innodb_strict_mode=ON;

SET GLOBAL innodb_file_per_table=ON;

SET GLOBAL innodb_file_format='Barracuda';

CREATE TABLE tab (
   id INT,
   str VARCHAR(50)
) ENGINE=InnoDB KEY_BLOCK_SIZE=4;
```

If the [KEY\_BLOCK\_SIZE](../../../../reference/sql-statements/data-definition/create/create-table.md#key_block_size) table option is **not** set to some value, but the [ROW\_FORMAT](../../../../reference/sql-statements/data-definition/create/create-table.md#row_format) table option is set to `COMPRESSED` in a [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) or [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/) statement, then InnoDB uses a default value of `8` for the [KEY\_BLOCK\_SIZE](../../../../reference/sql-statements/data-definition/create/create-table.md#key_block_size) table option:

```sql
SET SESSION innodb_strict_mode=ON;

SET GLOBAL innodb_file_per_table=ON;

SET GLOBAL innodb_file_format='Barracuda';

CREATE TABLE tab (
   id INT,
   str VARCHAR(50)
) ENGINE=InnoDB ROW_FORMAT=COMPRESSED;
```

### Create an InnoDB Table with the Compressed Row Format using ROW\_FORMAT

The default block size for tables that use the Compressed row format is half of [innodb\_page\_size](../../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_page_size). With the default 16 KB page size, the block size defaults to 8 KB. A compressed table with the default block size can be created by setting the ROW\_FORMAT table option to COMPRESSED:

```sql
CREATE TABLE hq_sales.invoices (
   invoice_id BIGINT UNSIGNED AUTO_INCREMENT NOT NULL,
   branch_id INT NOT NULL,
   customer_id INT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
   PRIMARY KEY(invoice_id)
) ROW_FORMAT = Compressed;
```

#### Step-by-Step Procedure

1. Connect to the server using [MariaDB Client](../../../../clients-and-utilities/mariadb-client/):

```
$ mariadb --user=root
```

2. Confirm that the default storage engine is InnoDB by checking the [default\_storage\_engine](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine) system variable using the [SHOW SESSION VARIABLES](../../../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) statement:

```sql
SHOW SESSION VARIABLES
   LIKE 'default_storage_engine';
```

```
+------------------------+--------+
| Variable_name          | Value  |
+------------------------+--------+
| default_storage_engine | InnoDB |
+------------------------+--------+
```

3. Create the table using the [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) statement, and specify the Compressed row format using the `ROW_FORMAT` table option:

```sql
CREATE TABLE hq_sales.invoices (
   invoice_id BIGINT UNSIGNED AUTO_INCREMENT NOT NULL,
   branch_id INT NOT NULL,
   customer_id INT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
   PRIMARY KEY(invoice_id)
) ROW_FORMAT = Compressed;
```

4. Confirm that the table uses the Compressed row format with an 8 KB block size by querying the [information\_schema.INNODB\_SYS\_TABLES](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tables-table.md) table:

```sql
SELECT NAME, ROW_FORMAT, ZIP_PAGE_SIZE
FROM information_schema.INNODB_SYS_TABLES
WHERE NAME='hq_sales/invoices';
```

```
+-------------------+------------+---------------+
| NAME              | ROW_FORMAT | ZIP_PAGE_SIZE |
+-------------------+------------+---------------+
| hq_sales/invoices | Compressed |          8192 |
+-------------------+------------+---------------+
```

### Create an InnoDB Table with the Compressed Row Format using KEY\_BLOCK\_SIZE

The default block size for tables that use the Compressed row format is half of [innodb\_page\_size](../../../../ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables.md#innodb_page_size). With the default 16 KB page size, the block size defaults to 8 KB. A compressed table with a non-default block size can be created by setting the `KEY_BLOCK_SIZE` table option to the desired block size.

```sql
CREATE TABLE hq_sales.invoices (
   invoice_id BIGINT UNSIGNED AUTO_INCREMENT NOT NULL,
   branch_id INT NOT NULL,
   customer_id INT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
   PRIMARY KEY(invoice_id)
) KEY_BLOCK_SIZE = 4;
```

#### Step-by-Step Procedure

1. Connect to the server using [MariaDB Client](../../../../clients-and-utilities/mariadb-client/):

```
$ mariadb --user=root
```

2. Confirm that the default storage engine is InnoDB by checking the [default\_storage\_engine](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#default_storage_engine) system variable using the [SHOW SESSION VARIABLES](../../../../reference/sql-statements/administrative-sql-statements/show/show-variables.md) statement:

```
SHOW SESSION VARIABLES
   LIKE 'default_storage_engine';
```

```
+------------------------+--------+
| Variable_name          | Value  |
+------------------------+--------+
| default_storage_engine | InnoDB |
+------------------------+--------+
```

3. Create the table using the CREATE TABLE statement, and specify the block size using the `KEY_BLOCK_SIZE` table option, which implies the Compressed row format:

```sql
CREATE TABLE hq_sales.invoices (
   invoice_id BIGINT UNSIGNED AUTO_INCREMENT NOT NULL,
   branch_id INT NOT NULL,
   customer_id INT,
   invoice_date DATETIME(6),
   invoice_total DECIMAL(13, 2),
   payment_method ENUM('NONE', 'CASH', 'WIRE_TRANSFER', 'CREDIT_CARD', 'GIFT_CARD'),
   PRIMARY KEY(invoice_id)
) KEY_BLOCK_SIZE = 4;
```

4. Confirm that the table uses the Compressed row format with an 8 KB block size by querying the [information\_schema.INNODB\_SYS\_TABLES](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_sys_tables-table.md) table:

```sql
SELECT NAME, ROW_FORMAT, ZIP_PAGE_SIZE
FROM information_schema.INNODB_SYS_TABLES
WHERE NAME='hq_sales/invoices';
```

```
+-------------------+------------+---------------+
| NAME              | ROW_FORMAT | ZIP_PAGE_SIZE |
+-------------------+------------+---------------+
| hq_sales/invoices | Compressed |          4096 |
+-------------------+------------+---------------+
```

## Compression with the `COMPRESSED` Row Format

The `COMPRESSED` row format supports compression of all data and index pages.

To avoid compressing and uncompressing pages too many times, InnoDB tries to keep both compressed and uncompressed pages in the [buffer pool](../innodb-buffer-pool.md) when there is enough room. This results in a bigger cache. When there is not enough room, an adaptive LRU algorithm is used to decide whether compressed or uncompressed pages should be evicted from the buffer: for CPU-bound workloads, the compressed pages are evicted first; for I/O-bound workloads, the uncompressed pages are evicted first. Of course, when necessary, both the compressed and uncompressed version of the same data can be evicted from the buffer.

Each compressed page has an uncompressed _modification log_, stored within the page itself. InnoDB writes small changes into it. When the space in the modification log runs out, the page is uncompressed, changes are applied, and the page is recompressed again. This is done to avoid some unnecessary decompression and compression operations.

Sometimes a _compression failure_ might happen, because the data has grown too much to fit the page. When this happens, the page (and the index node) is split into two different pages. This process can be repeated recursively until the data fit the pages. This can be CPU-consuming on some busy servers which perform many write operations.

Before writing a compressed page into a data file, InnoDB writes it into the [redo log](../innodb-redo-log.md). This ensures that the [redo log](../innodb-redo-log.md) can always be used to recover tables after a crash, even if the compression library is updated and some incompatibilities are introduced. But this also means that the [redo log](../innodb-redo-log.md) will grow faster and might need more space, or the frequency of checkpoints might need to increase.

## Monitoring Performance of the `COMPRESSED` Row Format

The following `INFORMATION_SCHEMA` tables can be used to monitor the performances of InnoDB compressed tables:

* [INNODB\_CMP and INNODB\_CMP\_RESET](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_cmp-and-innodb_cmp_reset-tables.md)
* [INNODB\_CMP\_PER\_INDEX and INNODB\_CMP\_PER\_INDEX\_RESET](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb-tables-information-schema-innodb_cmp_per_index-an.md)
* [INNODB\_CMPMEM and INNODB\_CMPMEM\_RESET](../../../../reference/system-tables/information-schema/information-schema-tables/information-schema-innodb-tables/information-schema-innodb_cmpmem-and-innodb_cmpmem_reset-tables.md)

## Index Prefixes with the `COMPRESSED` Row Format

The `COMPRESSED` row format supports index prefixes up to 3072 bytes. In [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) and before, the [innodb\_large\_prefix](../innodb-system-variables.md#innodb_large_prefix) system variable is used to configure the maximum index prefix length. In these versions, if [innodb\_large\_prefix](../innodb-system-variables.md#innodb_large_prefix) is set to `ON`, then the maximum prefix length is 3072 bytes, and if it is set to `OFF`, then the maximum prefix length is 767 bytes.

## Overflow Pages with the `COMPRESSED` Row Format

All InnoDB row formats can store certain kinds of data in overflow pages. This allows for the maximum row size of an InnoDB table to be larger than the maximum amount of data that can be stored in the row's main data page. See [Maximum Row Size](innodb-compressed-row-format.md#maximum-row-size) for more information about the other factors that can contribute to the maximum row size for InnoDB tables.

In the `COMPRESSED` row format variable-length columns, such as columns using the [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md), [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md), [BLOB](../../../../reference/data-types/string-data-types/blob.md) and [TEXT](../../../../reference/data-types/string-data-types/text.md) data types, can be completely stored in overflow pages.

InnoDB only considers using overflow pages if the table's row size is greater than half of [innodb\_page\_size](../innodb-system-variables.md#innodb_page_size). If the row size is greater than this, then InnoDB chooses variable-length columns to be stored on overflow pages until the row size is less than half of [innodb\_page\_size](../innodb-system-variables.md#innodb_page_size).

For [BLOB](../../../../reference/data-types/string-data-types/blob.md) and [TEXT](../../../../reference/data-types/string-data-types/text.md) columns, only values longer than 40 bytes are considered for storage on overflow pages. For [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md) and [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md) columns, only values longer than 255 bytes are considered for storage on overflow pages. Bytes that are stored to track a value's length do not count towards these limits. These limits are only based on the length of the actual column's data.

These limits differ from the limits for the `COMPACT` row format, where the limit is 767 bytes for all types.

Fixed-length columns greater than 767 bytes are encoded as variable-length columns, so they can also be stored in overflow pages if the table's row size is greater than half of [innodb\_page\_size](../innodb-system-variables.md#innodb_page_size). Even though a column using the [CHAR](../../../../reference/data-types/string-data-types/char.md) data type can hold at most 255 characters, a [CHAR](../../../../reference/data-types/string-data-types/char.md) column can still exceed 767 bytes in some cases. For example, a `char(255)` column can exceed 767 bytes if the [character set](../../../../reference/data-types/string-data-types/character-sets/) is `utf8mb4`.

If a column is chosen to be stored on overflow pages, then the entire value of the column is stored on overflow pages, and only a 20-byte pointer to the column's first overflow page is stored on the main page. Each overflow page is the size of [innodb\_page\_size](../innodb-system-variables.md#innodb_page_size). If a column is too large to be stored on a single overflow page, then it is stored on multiple overflow pages. Each overflow page contains part of the data and a 20-byte pointer to the next overflow page, if a next page exists.

This behavior differs from the behavior of the `COMPACT` row format, which always stores the column prefix on the main page. This allows tables using the `COMPRESSED` row format to contain a high number of columns using the [VARBINARY](../../../../reference/data-types/string-data-types/varbinary.md), [VARCHAR](../../../../reference/data-types/string-data-types/varchar.md), [BLOB](../../../../reference/data-types/string-data-types/blob.md) and [TEXT](../../../../reference/data-types/string-data-types/text.md) data types.

## Read-Only

**MariaDB starting with** [**10.6**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106)

From [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1060-release-notes) until [MariaDB 10.6.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1065-release-notes), tables that are of the `COMPRESSED` row format are read-only by default. This was intended to be the first step towards removing write support and deprecating the feature.\
This plan has been scrapped, and from [MariaDB 10.6.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1066-release-notes), `COMPRESSED` tables are no longer read-only by default.\
From [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1060-release-notes) to [MariaDB 10.6.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1065-release-notes), set the [innodb\_read\_only\_compressed](../innodb-system-variables.md#innodb_read_only_compressed) variable to `OFF` to make the tables writable.

## See Also

* [InnoDB Page Compression](../innodb-page-compression.md)
* [Storage-Engine Independent Column Compression](../../../../ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/storage-engine-independent-column-compression.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
