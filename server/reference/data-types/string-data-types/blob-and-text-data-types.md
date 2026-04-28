---
description: >-
  Overview of large object types. This page compares BLOB (binary) and TEXT
  (character) types, explaining their storage and usage differences.
---

# BLOB and TEXT Data Types

## Description

A `BLOB` is a binary large object that can hold a variable amount of data. The four `BLOB` types are

* [TINYBLOB](tinyblob.md),
* [BLOB](blob.md),
* [MEDIUMBLOB](mediumblob.md), and
* [LONGBLOB](longblob.md).

These differ only in the maximum length of the values they can hold.

The `TEXT` types are

* [TINYTEXT](tinytext.md),
* [TEXT](text.md),
* [MEDIUMTEXT](mediumtext.md), and
* [LONGTEXT](longtext.md).
* [JSON](json.md) (alias for LONGTEXT)

These correspond to the four `BLOB` types and have the same maximum lengths and [storage requirements](../data-type-storage-requirements.md).

`BLOB` and `TEXT` columns can have a `DEFAULT` value.

{% hint style="info" %}
It is possible to set a unique index on columns that use the `BLOB` or `TEXT` data types.
{% endhint %}

## Handling Large Data via APIs

When working with very large `BLOB` or `TEXT` values, the data may exceed the limit set by the [max\_allowed\_packet](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_allowed_packet) system variable. To avoid this—and to reduce memory consumption on the client—most MariaDB connectors allow you to "stream" data in chunks.

* Connector/C: Use [mysql\_stmt\_send\_long\_data()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_send_long_data) to send parameter data in pieces before calling [mysql\_stmt\_execute()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_execute). This bypasses `max_allowed_packet`  limits and reduces the peak memory footprint (RSS) of the application.
* Connector/J: Use `PreparedStatement.setBinaryStream()` (for `BLOB`) or `PreparedStatement.setCharacterStream()` (for `TEXT`).
* Protocol: These APIs utilize the [COM\_STMT\_SEND\_LONG\_DATA](../../clientserver-protocol/3-binary-protocol-prepared-statements/com_stmt_send_long_data.md) command, which appends data to a parameter on the server side.

### **Technical Rules for C/C++**

* 0-Based Indexing: Parameter numbering starts at `0`.
* The  `is_null` Flag: This must be `0`; if set to nonzero, the server may discard the streamed data.
* Resetting: Use  [mysql\_stmt\_reset()](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/api-prepared-statement-functions/mysql_stmt_reset) to clear all accumulated long data on the server if you need to abort or retry.
* Chunk Size: A practical performance "sweet spot" is between `64` KB and `1` MB per chunk.

## See Also

* [Store a column as compressed](../../sql-statements/data-definition/create/create-table.md#compressed)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
