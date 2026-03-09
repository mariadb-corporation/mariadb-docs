---
description: The CONNECT storage engine.
---

# CONNECT DBF Table Type

## Overview

A table of type `DBF` is physically a dBASE III or IV formatted file (used by many products like dBASE, Xbase, FoxPro etc.). This format is similar to the [FIX](connect-dos-and-fix-table-types.md) type format with in addition a prefix giving the characteristics of the file, describing in particular all the fields (columns) of the table.

Because `DBF` files have a header that contains Meta data about the file, in particular the column description, it is possible to create a table based on an existing `DBF` file without giving the column description, for instance:

```sql
CREATE TABLE cust ENGINE=CONNECT table_type=DBF file_name='cust.dbf';
```

To see what CONNECT has done, you can use the `DESCRIBE` or `SHOW CREATE TABLE` statements, and eventually modify some options with the `ALTER TABLE` statement.

The case of deleted lines is handled in a specific way for DBF tables. Deleted lines are not removed from the file but are "soft deleted" meaning they are marked as deleted. In particular, the number of lines contained in the file header does not take care of soft deleted lines. This is why if you execute\
these two commands applied to a DBF table named _tabdbf_:

```sql
SELECT COUNT(*) FROM tabdbf;
SELECT COUNT(*) FROM tabdbf WHERE 1;
```

They can give a different result, the (fast) first one giving the number of physical lines in the file and the second one giving the number of line that are not (soft) deleted.

The commands `UPDATE`, `INSERT`, and `DELETE` can be used with DBF tables. The `DELETE` statement marks the deleted lines as suppressed but keeps them in the file. The `INSERT` statement, if it is used to populate a newly created table, constructs the file header before inserting new lines.

**Note:** For DBF tables, column name length is limited to 11 characters and field length to 256 bytes.

## Conversion of dBASE Data Types

CONNECT handles only types that are stored as characters.

| Symbol | DBF Type        | CONNECT Type                        | Description                                                                                         |
| ------ | --------------- | ----------------------------------- | --------------------------------------------------------------------------------------------------- |
| B      | Binary (string) | TYPE\_STRING                        | 10 digits representing a .DBT block number.                                                         |
| C      | Character       | TYPE\_STRING                        | All OEM code page characters - padded with blanks to the width of the field.                        |
| D      | Date            | TYPE\_DATE                          | 8 bytes - date stored as a string in the format YYYYMMDD.                                           |
| N      | Numeric         | TYPE\_INT TYPE\_BIGINT TYPE\_DOUBLE | Number stored as a string, right justified, and padded with blanks to the width of the field.       |
| L      | Logical         | TYPE\_STRING                        | 1 byte - initialized to 0x20 otherwise T or F.                                                      |
| M      | Memo (string)   | TYPE\_STRING                        | 10 digits representing a .DBT block number.                                                         |
| @      | Timestamp       | Not supported                       | 8 bytes - two longs, first for date, second for time. It is the number of days since 01/01/4713 BC. |
| I      | Long            | Not supported                       | 4 bytes. Leftmost bit used to indicate sign, 0 negative.                                            |
| +      | Autoincrement   | Not supported                       | Same as a Long                                                                                      |
| F      | Float           | TYPE\_DOUBLE                        | Number stored as a string, right justified, and padded with blanks to the width of the field.       |
| O      | Double          | Not supported                       | 8 bytes - no conversions, stored as a double.                                                       |
| G      | OLE             | TYPE\_STRING                        | 10 digits representing a .DBT block number.                                                         |

For the N numeric type, CONNECT converts it to `TYPE_DOUBLE` if the decimals value is not 0, to `TYPE_BIGINT` if the length value is greater than 10, else to TYPE\_INT.

For M, B, and G types, CONNECT just returns the DBT number.

## Reading soft deleted lines of a DBF table

It is possible to read these lines by changing the read mode of the table. This is specified by an option `READMODE` that can take the values:

|   |                                             |
| - | ------------------------------------------- |
| 0 | Standard mode. This is the default option.  |
| 1 | Read all lines including soft deleted ones. |
| 2 | Read only the soft deleted lines.           |

For example, to read all lines of the tabdbf table, you can do:

```
ALTER TABLE tabdbf option_list='Readmode=1';
```

To come back to normal mode, specify `READMODE=0`.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
