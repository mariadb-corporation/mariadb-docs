---
description: >-
  This event provides a mapping between a table ID and its table definition,
  preceding row events to interpret the row data correctly.
---

# TABLE\_MAP\_EVENT

Used for row-based binary logging beginning (binlog\_format=`ROW` or `MIXED`).

This event precedes each row operation event and maps a table definition to a number, where the table definition consists of database and table names.

#### Header

* Event Type is `19` (`0x13`).

## Fields

### Fixed Data Part

* [uint<6>](../protocol-data-types.md#fixed-length-integers) The table ID.
* [uint<2>](../protocol-data-types.md#fixed-length-integers) Reserved for future use.

### Variable Data Part

* [uint<1>](../protocol-data-types.md#fixed-length-integers) Database name length.
* [string](../protocol-data-types.md#null-terminated-strings) The database name (null-terminated).
* [uint<1>](../protocol-data-types.md#fixed-length-integers) Table name length.
* [string](../protocol-data-types.md#null-terminated-strings) The table name (null-terminated).
* [int](../protocol-data-types.md#length-encoded-integers) The number of columns in the table.
* [byte](../protocol-data-types.md#fixed-length-bytes) An array of 'n' column types, one byte per column.
* [int](../protocol-data-types.md#length-encoded-integers) The length of the metadata block.
* [byte](../protocol-data-types.md#fixed-length-bytes) The metadata block;
* [byte](../protocol-data-types.md#fixed-length-bytes) Bit-field indicating whether each column can be `NULL`, one bit per column.
* If (more\_data\_available):
  * [byte](../protocol-data-types.md#variable-length-bytes) Optional metadata block.

#### Metadata Block

The metadata block contains type specific metadata information for each column.

| Type                                           | Length | Description                                                                                                                      |
| ---------------------------------------------- | ------ | -------------------------------------------------------------------------------------------------------------------------------- |
| MYSQL\_TYPE\_BLOB                              | 1      | Number of bytes for length: e.g. 4 bytes means length is stored in a 4 byte integer).                                            |
| MYSQL\_TYPE\_DATETIME2                         | 1      | Length of microseconds.                                                                                                          |
| MYSQL\_TYPE\_DECIMAL                           | 2      | Not in use anymore.                                                                                                              |
| MYSQL\_TYPE\_DOUBLE ,MYSQL\_TYPE\_FLOAT        | 1      | length (4 or 8 bytes).                                                                                                           |
| MYSQL\_TYPE\_STRING                            | 2      | The first byte contains type (`MYSQL_TYPE_STRING`, `MYSQL_TYPE_ENUM`, or `MYSQL_TYPE_SET`). The second byte contains the length. |
| MYSQL\_TYPE\_NEWDECIMAL                        | 2      | Precision, Scale.                                                                                                                |
| MYSQL\_TYPE\_TIME2                             | 1      | Length in microseconds.                                                                                                          |
| MYSQL\_TYPE\_TIMESTAMP2                        | 1      | Length in microseconds.                                                                                                          |
| MYSQL\_TYPE\_VARCHAR, MYSQL\_TYPE\_VAR\_STRING | 2      | Defined varchar length. If the value is > 255, the length is stored in 2 bytes, otherwise in 1 byte.                             |

#### Optional Metadata Block

Optional metadata are available if the global server variable `BINLOG_ROW_METADATA` is set to `MIN` or `FULL`.

The metadata block consists of one or more of the following blocks:

* [byte<1>](../protocol-data-types.md#fixed-length-bytes) Optional metadata type.
* [int](../protocol-data-types.md#length-encoded-integers) Length.
* [byte](../protocol-data-types.md#fixed-length-bytes) Data.

**Optional metadata types:**

| Name                             | Value | Mode | Description                                                                                                                                                                                                        |
| -------------------------------- | ----- | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| SIGNEDNESS                       | 1     | MIN  | Data contains a bitmap indicating which integer columns are signed.                                                                                                                                                |
| DEFAULT\_CHARSET                 | 2     | MIN  | Character set of string columns, used if most columns have the same result. Columns with other character sets will follow as pair (column\_index, collation number).                                               |
| COLUMN\_CHARSET                  | 3     | MIN  | Character set of columns, used if columns have different character sets. Returned as a sequence of collation numbers.                                                                                              |
| COLUMN\_NAME                     | 4     | FULL | List of Column names, the first byte specifies the length of the column name.                                                                                                                                      |
| SET\_STR\_VALUE                  | 5     | FULL | List of set values: First byte is the number of different values, followed by length/value pairs.                                                                                                                  |
| ENUM\_STR\_VALUE                 | 6     | FULL | Same as SET\_STR\_VALUE. Since ENUM values might have up to 0xFFFF members, the number of values is a length encoded integer.                                                                                      |
| GEOMETRY\_TYPE                   | 7     | FULL | A sequence of bytes repesenting the type of `GEOMETRY` columns: 0 = `GEOMETRY`, 1 = `POINT`, 2 = `LINESTRING`, 3 = `POLYGON`, 4=`MULTIPOINT`, 5 = `MULTILINESTRING`, 6 = `MULTIPOLYGON`, 7 = `GEOMETRYCOLLECTION`. |
| SIMPLE\_PRIMARY\_KEY             | 8     | FULL | A sequence of length encoded column indexes.                                                                                                                                                                       |
| PRIMARY\_KEY\_WITH\_PREFIX       | 9     | FULL | A sequence of length encoded column indexes and prefix lengths.                                                                                                                                                    |
| ENUM\_AND\_SET\_DEFAULT\_CHARSET | 10    | FULL | The default character set number used for `ENUM` and `SET` columns.                                                                                                                                                |
| ENUM\_AND\_SET\_COLUMN\_CHARSET  | 11    | FULL | Character set of `ENUM` and `SET` columns, used if these columns have different character sets. Returned as a sequence of collation numbers.                                                                       |

## Example From mysqlbinlog

```
# at 847
#171206 13:43:00 server id 10124  end_log_pos 892 CRC32 0xbe3c6b05 	Table_map: `test`.`t4` mapped to number 33
# at 892
```

## Complete Event

```
d4 e5 27 5a 13 8c 27 00  00 2d 00 00 00 7c 03 00  ..'Z..'..-...|..
00 00 00 21 00 00 00 00  00 01 00 04 74 65 73 74  ...!........test
00 02 74 34 00 01 03 01  01 05 6b 3c be           ..t4......k<.
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
