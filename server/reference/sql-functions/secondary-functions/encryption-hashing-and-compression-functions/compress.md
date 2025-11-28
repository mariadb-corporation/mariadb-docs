---
description: >-
  Compress a string. This function compresses a string argument and returns the
  result as a binary string, useful for saving storage space.
---

# COMPRESS

## Syntax

```sql
COMPRESS(string_to_compress)
```

## Description

Compresses a string and returns the result as a binary string. This function requires MariaDB to have been compiled with a compression library such as zlib. Otherwise, the return value is always `NULL`. The\
compressed string can be uncompressed with [UNCOMPRESS()](uncompress.md).

The [have\_compress](../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#have_compress) server system variable indicates whether a compression library is present.

## Examples

```sql
SELECT LENGTH(COMPRESS(REPEAT('a',1000)));
+------------------------------------+
| LENGTH(COMPRESS(REPEAT('a',1000))) |
+------------------------------------+
|                                 21 |
+------------------------------------+

SELECT LENGTH(COMPRESS(''));
+----------------------+
| LENGTH(COMPRESS('')) |
+----------------------+
|                    0 |
+----------------------+

SELECT LENGTH(COMPRESS('a'));
+-----------------------+
| LENGTH(COMPRESS('a')) |
+-----------------------+
|                    13 |
+-----------------------+

SELECT LENGTH(COMPRESS(REPEAT('a',16)));
+----------------------------------+
| LENGTH(COMPRESS(REPEAT('a',16))) |
+----------------------------------+
|                               15 |
+----------------------------------+
```

## See Also

* [Automatic compression of columns](../../../../ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/storage-engine-independent-column-compression.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
