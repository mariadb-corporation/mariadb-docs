---
description: >-
  A result set consists of a sequence of packets including column counts, column
  definitions, and row data, terminated by an EOF or OK packet.
---

# Result Set Packets

MariaDB Server sends the following packets as part of a result set.

A result set consists of different packets:

* [Result set metadata](result-set-packets.md#ResultSet-metadata).
  * 1 [column count packet](result-set-packets.md#column-count-packet).
* If not (`MARIADB_CLIENT_CACHE_METADATA` capability set) `OR` (send metadata == 1):
  * For each column (for instance, `column_count` times):
    * [Column Definition packet](result-set-packets.md#column-definition-packet).
* If not (`CLIENT_DEPRECATE_EOF` capability set) [EOF\_Packet](eof_packet.md).
* n [result set row](resultset-row.md).
* If error:
  * [ERR\_Packet](err_packet.md).
* Else:
  * If `CLIENT_DEPRECATE_EOF` capability:
    * [OK\_Packet](ok_packet.md) with a `0xFE` header.
  * Else [EOF\_Packet](eof_packet.md).

{% hint style="warning" %}
It would be unsafe to assume that any packet with a 0xFE header is an [OK packet (OK\_Packet)](ok_packet.md) or an [EOF packet (EOF\_Packet)](eof_packet.md), because [result-set row packets (ResultsetRow)](resultset-row.md) can also begin with 0xFE when using the text protocol with a field length greater than 0xFFFFFF.\
To safely confirm that a packet with a 0xFE header is an [OK packet (OK\_Packet)](ok_packet.md) or an [EOF packet (EOF\_Packet)](eof_packet.md), you must also check that the packet length is less than 0xFFFFFF.
{% endhint %}

## Column Count Packet

The column count packet describes the number of columns in the result set. It uses the following format:

* [int](../protocol-data-types.md#length-encoded-integers) column count.
* If (`MARIADB_CLIENT_CACHE_METADATA` capability set):
  * int<1> metadata follows (0 / 1).

The metadata indicator byte is only present if both the client and the server declare the `MARIADB_CLIENT_CACHE_METADATA` capability.

If the metadata byte is set to `1`, the normal metadata follows the column definitions. If the metadata byte is set to `0`, the Column Count Packet is immediately followed by the second [EOF packet (EOF\_Packet)](eof_packet.md) or the result set rows if the `CLIENT_DEPRECATE_EOF` capability is set.

## Column Definition Packet

A column definition packet describes a column in the result set. It uses the following format:

* [string](../protocol-data-types.md#length-encoded-strings) catalog (always 'def').
* [string](../protocol-data-types.md#length-encoded-strings) schema.
* [string](../protocol-data-types.md#length-encoded-strings) table alias.
* [string](../protocol-data-types.md#length-encoded-strings) table.
* [string](../protocol-data-types.md#length-encoded-strings) column alias.
* [string](../protocol-data-types.md#length-encoded-strings) column.
* If extended type supported (see `MARIADB_CLIENT_EXTENDED_METADATA` ):
  * [string](../protocol-data-types.md#length-encoded-strings) [extended metadata](result-set-packets.md#extended-metadata).
* [int](../protocol-data-types.md#length-encoded-integers) length of fixed fields (=0xC).
* [int<2>](../protocol-data-types.md#fixed-length-integers) character set number.
* [int<4>](../protocol-data-types.md#fixed-length-integers) max. column size.
* [int<1>](../protocol-data-types.md#fixed-length-integers) [Field types](result-set-packets.md#field-types).
* [int<2>](../protocol-data-types.md#fixed-length-integers) [Field detail flag](result-set-packets.md#field-details-flag).
* [int<1>](../protocol-data-types.md#fixed-length-integers) decimals.
* [int<2>](../protocol-data-types.md#fixed-length-integers) - unused -

## Field types

The column type field in the column definition packet describes the base type of the column. It also indicates how the values are encoded for `COM_STMT_EXECUTE` parameters and binary result set rows.

| Value | Protocol Column Type      | Encoding                                                                                                                          |
| ----- | ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| 0     | MYSQL\_TYPE\_DECIMAL      | [byte encoding](../protocol-data-types.md#length-encoded-bytes)                                                                   |
| 1     | MYSQL\_TYPE\_TINY         | [TINYINT Binary encoding](resultset-row.md#tinyint-binary-encoding)                                                               |
| 2     | MYSQL\_TYPE\_SHORT        | [SMALLINT Binary encoding](resultset-row.md#smallint-binary-encoding)                                                             |
| 3     | MYSQL\_TYPE\_LONG         | [INTEGER Binary encoding](resultset-row.md#integer-binary-encoding)                                                               |
| 4     | MYSQL\_TYPE\_FLOAT        | [FLOAT Binary encoding](resultset-row.md#float-binary-encoding)                                                                   |
| 5     | MYSQL\_TYPE\_DOUBLE       | [DOUBLE Binary encoding](resultset-row.md#double-binary-encoding)                                                                 |
| 6     | MYSQL\_TYPE\_NULL         | Not used, nullness is indicated by the NULL-bitmap in the result                                                                  |
| 7     | MYSQL\_TYPE\_TIMESTAMP    | [TIMESTAMP Binary encoding](resultset-row.md#timestamp-binary-encoding)                                                           |
| 8     | MYSQL\_TYPE\_LONGLONG     | [BIGINT Binary encoding](resultset-row.md#bigint-binary-encoding)                                                                 |
| 9     | MYSQL\_TYPE\_INT24        | [INTEGER Binary encoding](resultset-row.md#integer-binary-encoding)                                                               |
| 10    | MYSQL\_TYPE\_DATE         | [TIMESTAMP Binary encoding](resultset-row.md#timestamp-binary-encoding)                                                           |
| 11    | MYSQL\_TYPE\_TIME         | [TIME Binary encoding](resultset-row.md#time-binary-encoding)                                                                     |
| 12    | MYSQL\_TYPE\_DATETIME     | [TIMESTAMP Binary encoding](resultset-row.md#timestamp-binary-encoding)                                                           |
| 13    | MYSQL\_TYPE\_YEAR         | [SMALLINT Binary encoding](resultset-row.md#smallint-binary-encoding)                                                             |
| 14    | MYSQL\_TYPE\_NEWDATE      | [byte encoding](../protocol-data-types.md#length-encoded-bytes)                                                                   |
| 15    | MYSQL\_TYPE\_VARCHAR      | [byte encoding](../protocol-data-types.md#length-encoded-bytes)                                                                   |
| 16    | MYSQL\_TYPE\_BIT          | [byte encoding](../protocol-data-types.md#length-encoded-bytes)                                                                   |
| 17    | MYSQL\_TYPE\_TIMESTAMP2   | Used only in the replication protocol                                                                                             |
| 18    | MYSQL\_TYPE\_DATETIME2    | Used only in the replication protocol                                                                                             |
| 19    | MYSQL\_TYPE\_TIME2        | Used only in the replication protocol                                                                                             |
| 245   | MYSQL\_TYPE\_JSON         | [byte encoding](../protocol-data-types.md#length-encoded-bytes) (only used with MySQL, MariaDB uses MYSQL\_TYPE\_STRING for JSON) |
| 246   | MYSQL\_TYPE\_NEWDECIMAL   | [byte encoding](../protocol-data-types.md#length-encoded-bytes)                                                                   |
| 247   | MYSQL\_TYPE\_ENUM         | [byte encoding](../protocol-data-types.md#length-encoded-bytes)                                                                   |
| 248   | MYSQL\_TYPE\_SET          | [byte encoding](../protocol-data-types.md#length-encoded-bytes)                                                                   |
| 249   | MYSQL\_TYPE\_TINY\_BLOB   | [byte encoding](../protocol-data-types.md#length-encoded-bytes)                                                                   |
| 250   | MYSQL\_TYPE\_MEDIUM\_BLOB | [byte encoding](../protocol-data-types.md#length-encoded-bytes)                                                                   |
| 251   | MYSQL\_TYPE\_LONG\_BLOB   | [byte encoding](../protocol-data-types.md#length-encoded-bytes)                                                                   |
| 252   | MYSQL\_TYPE\_BLOB         | [byte encoding](../protocol-data-types.md#length-encoded-bytes)                                                                   |
| 253   | MYSQL\_TYPE\_VAR\_STRING  | [byte encoding](../protocol-data-types.md#length-encoded-bytes)                                                                   |
| 254   | MYSQL\_TYPE\_STRING       | [byte encoding](../protocol-data-types.md#length-encoded-bytes)                                                                   |
| 255   | MYSQL\_TYPE\_GEOMETRY     | [byte encoding](../protocol-data-types.md#length-encoded-bytes)                                                                   |

## Field Details Flag

The column details flag describes certain column attributes and whether certain column options are set.

It is a bitmask with the following flags:

| Flag Value | Flag Name                | Flag Description                          |
| ---------- | ------------------------ | ----------------------------------------- |
| 1          | NOT\_NULL                | field cannot be null                      |
| 2          | PRIMARY\_KEY             | field is a primary key                    |
| 4          | UNIQUE\_KEY              | field is unique                           |
| 8          | MULTIPLE\_KEY            | field is in a multiple key                |
| 16         | BLOB                     | is this field a Blob                      |
| 32         | UNSIGNED                 | is this field unsigned                    |
| 64         | ZEROFILL\_FLAG           | is this field a zerofill                  |
| 128        | BINARY\_COLLATION        | whether this field has a binary collation |
| 256        | ENUM                     | Field is an enumeration                   |
| 512        | AUTO\_INCREMENT          | field auto-increment                      |
| 1024       | TIMESTAMP                | field is a timestamp value                |
| 2048       | SET                      | field is a SET                            |
| 4096       | NO\_DEFAULT\_VALUE\_FLAG | field doesn't have default value          |
| 8192       | ON\_UPDATE\_NOW\_FLAG    | field is set to NOW on UPDATE             |
| 32768      | NUM\_FLAG                | field is num                              |

{% hint style="info" %}
The `BLOB` flag cannot be used to determine if a column has binary data, because [BINARY](../../data-types/string-data-types/binary.md) and [VARBINARY](../../data-types/string-data-types/varbinary.md) columns are treated as strings, instead of blobs.

The `BINARY_COLLATION` flag can be used to determine if a string column has binary data.
{% endhint %}

## Extended Metadata

This extended column type information can be used to find out more specific details about the column type:

* For a [POINT](../../sql-statements/geometry-constructors/geometry-constructors/point.md) column, the column type field is `MYSQL_TYPE_GEOMETRY`, but the extended type indicates 'point'.
* For a [JSON](../../data-types/string-data-types/json.md) column, the column type field is `MYSQL_TYPE_STRING`, but the extended type indicates 'json'.
* While string has data:
  * [int<1>](../protocol-data-types.md#fixed-length-integers) data type: 0x00:type, 0x01: format.
  * [string](../protocol-data-types.md#length-encoded-strings) value.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
