# Aria Storage Formats

The [Aria](./) storage engine supports three different table storage formats.

These are FIXED, DYNAMIC and PAGE, and they can be set with the ROW FORMAT option in the [CREATE TABLE](../../../reference/sql-statements/data-definition/create/create-table.md) statement. PAGE is the default format, while FIXED and DYNAMIC are essentially the same as the [MyISAM formats](../myisam-storage-engine/myisam-storage-formats.md).

The [SHOW TABLE STATUS](../../../reference/sql-statements/administrative-sql-statements/show/show-table-status.md) statement can be used to see the storage format used by a table.

## Fixed-length

Fixed-length (or static) tables contain records of a fixed-length. Each column is the same length for all records, regardless of the actual contents. It is the default format if a table has no BLOB, TEXT, VARCHAR or VARBINARY fields, and no ROW FORMAT is provided. You can also specify a fixed table with ROW\_FORMAT=FIXED in the table definition.

Tables containing BLOB or TEXT fields cannot be FIXED, as by design these are both dynamic fields.

Fixed-length tables have a number of characteristics

* fast, since MariaDB will always know where a record begins
* easy to cache
* take up more space than dynamic tables, as the maximum amount of storage space will be allocated to each record.
* reconstructing after a crash is uncomplicated due to the fixed positions
* no fragmentation or need to re-organize, unless records have been deleted and you want to free the space up.

## Dynamic

Dynamic tables contain records of a variable length. It is the default format if a table has any BLOB, TEXT, VARCHAR or VARBINARY fields, and no ROW FORMAT is provided. You can also specify a DYNAMIC table with ROW\_FORMAT=DYNAMIC in the table definition.

Dynamic tables have a number of characteristics

* Each row contains a header indicating the length of the row.
* Rows tend to become fragmented easily. UPDATING a record to be longer will likely ensure it is stored in different places on the disk.
* All string columns with a length of four or more are dynamic.
* They require much less space than fixed-length tables.
* Restoring after a crash is more complicated than with FIXED tables.

## Page

Page format is the default format for Aria tables, and is the only format that can be used if TRANSACTIONAL=1.

Page tables have a number of characteristics:

* It's cached by the page cache, which gives better random performance as it uses fewer system calls.
* Does not fragment as easily as the DYNAMIC format during UPDATES. The maximum number of fragments are very low.
* Updates more quickly than dynamic tables.
* Has a slight storage overhead, mainly notable on very small rows
* Slower to perform a full table scan
* Slower if there are multiple duplicated keys, as Aria will first write a row, then keys, and only then check for duplicates

## Transactional

See [Aria Storage Engine](aria-storage-engine.md) for the impact of the TRANSACTIONAL option on the row format.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
