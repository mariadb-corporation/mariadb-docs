---
description: >-
  Learn about the three storage formats supported by MyISAM: FIXED (static),
  DYNAMIC (variable length), and COMPRESSED (read-only).
---

# MyISAM Storage Formats

The [MyISAM](./) storage engine supports three different table storage formats.

These are FIXED, DYNAMIC and COMPRESSED. FIXED and DYNAMIC can be set with the ROW FORMAT option in the [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) statement, or are chosen automatically depending on the columns the table contains. COMPRESSED can only be set via the [myisampack](../../../clients-and-utilities/myisam-clients-and-utilities/myisampack.md) tool.

The [SHOW TABLE STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-table-status.md) statement can be used to see the storage format used by a table. Note that `COMPRESSED` tables are reported as `DYNAMIC` in that context.

## Fixed-length

Fixed-length (or static) tables contain records of a fixed-length. Each column is the same length for all records, regardless of the actual contents. It is the default format if a table has no [BLOB](../../../reference/data-types/string-data-types/blob.md), [TEXT](../../../reference/data-types/string-data-types/text.md), [VARCHAR](../../../reference/data-types/string-data-types/varchar.md) or [VARBINARY](../../../reference/data-types/string-data-types/varbinary.md) fields, and no ROW FORMAT is provided. You can also specify a fixed table with ROW\_FORMAT=FIXED in the table definition.

Tables containing BLOB or TEXT fields cannot be FIXED, as by design these are both dynamic fields. However, no error or warning are raised if you specify FIXED.

Fixed-length tables have a number of characteristics

* fast, since MariaDB will always know where a record begins
* easy to repair: [myisamchk](../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk.md) is always able to recover all rows, except for the last one if it is not entirely written
* easy to cache
* take up more space than dynamic or compressed tables, as the maximum amount of storage space are allocated to each record.
* reconstructing after a crash is uncomplicated due to the fixed positions
* no fragmentation or need to re-organize, unless records have been deleted and you want to free the space up.

## Dynamic

Dynamic tables contain records of a variable length. It is the default format if a table has any BLOB, TEXT, VARCHAR or VARBINARY fields, and no ROW FORMAT is provided. You can also specify a DYNAMIC table with ROW\_FORMAT=DYNAMIC in the table definition. If the table contains BLOB or TEXT columns, its format is always DYNAMIC, and the ROW FORMAT option is ignored.

Dynamic tables have a number of characteristics

* Each row contains a header indicating the length of the row.
* Rows tend to become fragmented easily. UPDATING a record to be longer will likely ensure it is stored in different places on the disk. Use [OPTIMIZE TABLE](../../../ha-and-performance/optimization-and-tuning/optimizing-tables/optimize-table.md) when the fragmentation is too high.
* All string columns with a length of four or more are dynamic.
* They require much less space than fixed-length tables.
* Restoring after a crash is more complicated than with FIXED tables. Some fragments may be lost.

If a DYNAMIC table has some frequently-accessed fixed-length columns, it could be a good idea to move them into a separate FIXED table to avoid fragmentation.

## Compressed

Compressed tables are a read-only format, created with the [myisampack](../../../clients-and-utilities/myisam-clients-and-utilities/myisampack.md) tool. This can be done while the server is running, but external lock must not be disabled. [myisamchk](../../../clients-and-utilities/myisam-clients-and-utilities/myisamchk.md) is used to uncompress them.

Compressed tables have a number of characteristics:

* while the data is read-only, DDL statements such as [DROP TABLE](../../../reference/sql-statements/data-definition/drop/drop-table.md) and [TRUNCATE TABLE](../../../reference/sql-statements/table-statements/truncate-table.md) will still function.
* take much less space than fixed or dynamic tables. Each data has usually a 40-70% compression ratio
* rows are compressed separately, reducing access overhead.
* row headers are from one to three bytes.
* rows can be compressed with different compression types, including
  * prefix space compression
  * suffix space compression
  * columns with small sets of values are converted to ENUM
  * numeric zeros are stored with only one bit
  * integer columns are reduced to the smallest int type that can hold the contents

## See Also

* [Why we still need MyISAM (for read-only tables)](https://jfg-mysql.blogspot.nl/2017/08/why-we-still-need-myisam.html) describes an important use case for MyISAM compressed tables.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
