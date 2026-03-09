# ColumnStore Information Schema Tables

MariaDB ColumnStore has four information schema tables that expose information about the table and column storage. The tables were added in version 1.0.5 and were heavily modified for 1.0.6.

## COLUMNSTORE\_TABLES

The first table is the `INFORMATION_SCHEMA.COLUMNSTORE_TABLES`. It contains information about the tables inside ColumnStore. The table layout is as follows:

| Column         | Description                                                         |
| -------------- | ------------------------------------------------------------------- |
| TABLE\_SCHEMA  | The database schema for the table                                   |
| TABLE\_NAME    | The table name                                                      |
| OBJECT\_ID     | The ColumnStore object ID for the table                             |
| CREATION\_DATE | The date the table was created                                      |
| COLUMN\_COUNT  | The number of columns in the table                                  |
| AUTOINCREMENT  | The start autoincrement value for the table set during CREATE TABLE |

> Tables created with ColumnStore 1.0.4 or lower will have the year field of the creation data set incorrectly by 1900 years.

## COLUMNSTORE\_COLUMNS

The `INFORMATION_SCHEMA.COLUMNSTORE_COLUMNS` table contains information about every single column inside ColumnStore. The table layout is as follows:

| Column                 |                                                                                 |
| ---------------------- | ------------------------------------------------------------------------------- |
| TABLE\_SCHEMA          | The database schema for the table                                               |
| TABLE\_NAME            | The table name for the column                                                   |
| COLUMN\_NAME           | The column name                                                                 |
| OBJECT\_ID             | The object ID for the column                                                    |
| DICTIONARY\_OBJECT\_ID | The dictionary object ID for the column (NULL if there is no dictionary object) |
| LIST\_OBJECT\_ID       | Placeholder for future information                                              |
| TREE\_OBJECT\_ID       | Placeholder for future information                                              |
| DATA\_TYPE             | The data type for the column                                                    |
| COLUMN\_LENGTH         | The data length for the column                                                  |
| COLUMN\_POSITION       | The position of the column in the table, starting at 0                          |
| COLUMN\_DEFAULT        | The default value for the column                                                |
| IS\_NULLABLE           | Whether or not the column can be set to NULL                                    |
| NUMERIC\_PRECISION     | The numeric precision for the column                                            |
| NUMERIC\_SCALE         | The numeric scale for the column                                                |
| IS\_AUTOINCREMENT      | Set to 1 if the column is an autoincrement column                               |
| COMPRESSION\_TYPE      | The type of compression (either "None" or "Snappy")                             |

## COLUMNSTORE\_EXTENTS

This table displays the extent map in a user-consumable form. An extent is a collection of details about a section of data related to a columnstore column. A majority of columns in ColumnStore will have multiple extents, and the columns table above can be joined to this one to filter results by table or column. The table layout is as follows:

| Column                | Description                                                                                             |
| --------------------- | ------------------------------------------------------------------------------------------------------- |
| OBJECT\_ID            | The object ID for the extent                                                                            |
| OBJECT\_TYPE          | Whether this is a "Column" or "Dictionary" extent                                                       |
| LOGICAL\_BLOCK\_START | ColumnStore's internal start LBID for this extent                                                       |
| LOGICAL\_BLOCK\_END   | ColumnStore's internal end LBID for this extent                                                         |
| MIN\_VALUE            | This minimum value stored in this extent                                                                |
| MAX\_VALUE            | The maximum value stored in this extent                                                                 |
| WIDTH                 | The data width for the extent                                                                           |
| DBROOT                | The DBRoot number for the extent                                                                        |
| PARTITION\_ID         | The partition ID for the extent                                                                         |
| SEGMENT\_ID           | The segment ID for the extent                                                                           |
| BLOCK\_OFFSET         | The block offset for the data file, each data file can contain multiple extents for a column            |
| MAX\_BLOCKS           | The maximum number of blocks for the extent                                                             |
| HIGH\_WATER\_MARK     | The last block committed to the extent (starting at 0)                                                  |
| STATE                 | The state of the extent (see below)                                                                     |
| STATUS                | The availability status for the column, which is either "Available", "Unavailable", or "Out of service" |
| DATA\_SIZE            | The uncompressed data size for the extent is calculated as (HWM + 1) \* BLOCK\_SIZE                     |

**Notes:**

1. The state is "Valid" for a normal state, "Invalid" if a cpimport has completed but the table has not yet been accessed (min/max values will be invalid), or "Updating" if there is a DML statement writing to the column.
2. In ColumnStore, the block size is 8192 bytes.
3. By default, ColumnStore will write and create an extent file of 256\_1024\_WIDTH bytes for the first partition; if this is too small, then for uncompressed data, it will create a file of the maximum size for the extent (`MAX_BLOCKS * BLOCK_SIZE`). Snappy always compresses and adds a header block.
4. Object IDs of less than 3000 are for internal tables and will not appear in any of the information schema tables.
5. HWM is set to zero for the lower segments when there are multiple segments in an extent file; these can be observed when `BLOCK_OFFSET > 0`.
6. When HWM is 0, the `DATA_SIZE` will show 0 instead of 8192 to avoid confusion when there are multiple segments in an extent file.

## COLUMNSTORE\_FILES

The `columnstore_files` table provides information about each file associated with extensions. Each extension can reuse a file at different block offsets, so this is not a 1:1 relationship to the `columnstore_extent`s table.

| Column                 | Description                                                                                                                                |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| OBJECT\_ID             | The object ID for the extent                                                                                                               |
| SEGMENT\_ID            | The segment ID for the extent                                                                                                              |
| PARTITION\_ID          | The partition ID for the extent                                                                                                            |
| FILENAME               | The full path and filename for the extent file, multiple extents for the same column can point to this file with different `BLOCK_OFFSETs` |
| FILE\_SIZE             | The disk file size for the extent                                                                                                          |
| COMPRESSED\_DATA\_SIZE | The amount of the compressed file used, `NULL` if this is an uncompressed file                                                             |

## Stored Procedures

The `total_usage()` procedure gives a total disk usage summary for all the columns in ColumnStore except the columns used for internal maintenance. It is executed using the following query:

```sql
> call columnstore_info.total_usage();
```

### table\_usage Procedure

The `table_usage()` procedure gives the total data disk usage, dictionary disk usage, and overall disk usage per table. It can be called in several ways; the first gives a total for each table:

```sql
> call columnstore_info.table_usage(NULL, NULL);
```

Or for a specific table, `my_table` in `my_schema` in this example:

```sql
> call columnstore_info.table_usage('my_schema', 'my_table');
```

You can also request all tables for a specified schema:

```sql
> call columnstore_info.table_usage('my_schema', NULL);
```

{% hint style="info" %}
**Note:** The quotes around the table name are required; an error will occur without them.
{% endhint %}

### compression\_ratio Procedure

The `compression_ratio()` procedure calculates the average compression ratio across all the compressed extents in ColumnStore. It is called using

```sql
> call columnstore_info.compression_ratio();
```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
