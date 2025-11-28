---
description: >-
  Reference for storage space usage. This page lists the disk space consumed by
  each data type, helping with capacity planning and schema optimization.
---

# Data Type Storage Requirements

The following tables indicate the approximate data storage requirements for each data type.

## Numeric Data Types

| Data Type                                    | Storage Requirement                   |
| -------------------------------------------- | ------------------------------------- |
| [TINYINT](numeric-data-types/tinyint.md)     | 1 byte                                |
| [SMALLINT](numeric-data-types/smallint.md)   | 2 bytes                               |
| [MEDIUMINT](numeric-data-types/mediumint.md) | 3 bytes                               |
| [INT](numeric-data-types/int.md)             | 4 bytes                               |
| [BIGINT](numeric-data-types/bigint.md)       | 8 bytes                               |
| [FLOAT](numeric-data-types/float.md)(p)      | 4 bytes if p <= 24, otherwise 8 bytes |
| [DOUBLE](numeric-data-types/double.md)       | 8 bytes                               |
| [DECIMAL](numeric-data-types/decimal.md)     | See table below                       |
| [BIT](numeric-data-types/bit.md)(M)          | (M+7)/8 bytes                         |

Note that `MEDIUMINT` columns will require 4 bytes in memory (for example, in InnoDB buffer pool).

### Decimal

[Decimals](numeric-data-types/decimal.md) are stored using a binary format, with the integer and the fraction stored separately. Each nine-digit multiple requires 4 bytes, followed by a number of bytes for whatever remains, as follows:

| Remaining digits | Storage Requirement |
| ---------------- | ------------------- |
| 0                | 0 bytes             |
| 1                | 1 byte              |
| 2                | 1 byte              |
| 3                | 2 bytes             |
| 4                | 2 bytes             |
| 5                | 3 bytes             |
| 6                | 3 bytes             |
| 7                | 4 bytes             |
| 8                | 4 bytes             |

## String Data Types

In the descriptions below, `M` is the declared column length (in characters or in bytes), while `len` is the actual length in bytes of the value.

| Data Type                                                                                    | Storage Requirement                                                                                        |
| -------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| [ENUM](string-data-types/enum.md)                                                            | 1 byte for up to 255 enum values, 2 bytes for 256 to 65,535 enum values                                    |
| [CHAR(M)](string-data-types/char.md)                                                         | M × w bytes, where w is the number of bytes required for the maximum-length character in the character set |
| [BINARY(M)](string-data-types/binary.md)                                                     | M bytes                                                                                                    |
| [VARCHAR(M)](string-data-types/varchar.md), [VARBINARY(M)](string-data-types/varbinary.md)   | len + 1 bytes if column is 0 – 255 bytes, len + 2 bytes if column may require more than 255 bytes          |
| [TINYBLOB](string-data-types/tinyblob.md), [TINYTEXT](string-data-types/tinytext.md)         | len + 1 bytes                                                                                              |
| [BLOB](string-data-types/blob.md), [TEXT](string-data-types/text.md)                         | len + 2 bytes                                                                                              |
| [MEDIUMBLOB](string-data-types/mediumblob.md), [MEDIUMTEXT](string-data-types/mediumtext.md) | len + 3 bytes                                                                                              |
| [LONGBLOB](string-data-types/longblob.md), [LONGTEXT](string-data-types/longtext.md)         | len + 4 bytes                                                                                              |
| [SET](string-data-types/set-data-type.md)                                                    | Given M members of the set, (M+7)/8 bytes, rounded up to 1, 2, 3, 4, or 8 bytes                            |
| [INET6](string-data-types/inet6.md)                                                          | 16 bytes                                                                                                   |
| [UUID](string-data-types/uuid-data-type.md)                                                  | 16 bytes                                                                                                   |

In some [character sets](string-data-types/character-sets/), not all characters use the same number of bytes. utf8 encodes characters with one to three bytes per character, while `utf8mb4` requires one to four bytes per character.

When using field the `COMPRESSED` attribute, 1 byte is reserved for metadata. For example, `VARCHAR(255)` will use +2 bytes instead of +1.

### Examples

Assuming a single-byte character-set:

| Value | CHAR(2) | Storage Required | VARCHAR(2) | Storage Required |
| ----- | ------- | ---------------- | ---------- | ---------------- |
| ''    | ' '     | 2 bytes          | ''         | 1 byte           |
| '1'   | '1 '    | 2 bytes          | '1'        | 2 bytes          |
| '12'  | '12'    | 2 bytes          | '12'       | 3 bytes          |

## Date and Time Data Types

| Data Type                                          | Storage Requirement |
| -------------------------------------------------- | ------------------- |
| [DATE](date-and-time-data-types/date.md)           | 3 bytes             |
| [TIME](date-and-time-data-types/time.md)           | 3 bytes             |
| [DATETIME](date-and-time-data-types/datetime.md)   | 8 bytes             |
| [TIMESTAMP](date-and-time-data-types/timestamp.md) | 4 bytes             |
| [YEAR](date-and-time-data-types/year-data-type.md) | 1 byte              |

### Microseconds

MariaDB defaults to the MySQL format (by means of the [mysql56\_temporal\_format](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#mysql56_temporal_format) variable). Microseconds have the following additional storage requirements:

| Precision | Storage Requirement |
| --------- | ------------------- |
| 0         | 0 bytes             |
| 1,2       | 1 byte              |
| 3,4       | 2 bytes             |
| 5,6       | 3 bytes             |

## NULL Values

For the InnoDB [COMPACT](../../server-usage/storage-engines/innodb/innodb-row-formats/innodb-compact-row-format.md), [DYNAMIC](../../server-usage/storage-engines/innodb/innodb-row-formats/innodb-dynamic-row-format.md) and [COMPRESSED](../../server-usage/storage-engines/innodb/innodb-row-formats/innodb-compressed-row-format.md) row formats, a number of bytes will be allocated in the record header for the nullable fields. If there are between 1 and 8 nullable fields, 1 such byte will be allocated. In the record payload area, no space will be reserved for values that are `NULL`.

For the [InnoDB REDUNDANT row format](../../server-usage/storage-engines/innodb/innodb-row-formats/innodb-redundant-row-format.md), the overhead is 1 bit in the record header (as a part of the 1-byte or 2-byte "end of field" pointer). In that format, a `NULL` fixed-length field will consume the same amount of space as any `NOT NULL` value in the record payload area. The motivation is that it is possible to update in place between `NOT NULL` and `NULL` values.

In other formats, `NULL` values usually require 1 bit in the data file, 1 byte in the index file.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
