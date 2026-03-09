---
description: >-
  Compute CRC32C checksum. This function calculates a cyclic redundancy check
  value using the Castagnoli polynomial.
---

# CRC32C

{% hint style="info" %}
`CRC32C` is available from MariaDB [10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.8/what-is-mariadb-108).
{% endhint %}

`CRC32C` is used to compute a cyclic redundancy check (CRC) value using the Castagnoli polynomial.

## Syntax

```sql
CRC32C([par,]expr)
```

## Description

MariaDB has always included a native unary function [CRC32()](crc32.md) that computes the CRC-32 of a string using the ISO 3309 polynomial that used by zlib and many others.

InnoDB and MyRocks use a different polynomial, which was implemented in SSE4.2 instructions that were introduced in the Intel Nehalem microarchitecture. This is commonly called CRC-32C (Castagnoli).

The CRC32C function uses the Castagnoli polynomial.

This allows `SELECT…INTO DUMPFILE` to be used for the creation of files with valid checksums, such as a logically empty InnoDB redo log file`ib_logfile0` corresponding to a particular log sequence number.

The optional parameter allows the checksum to be computed in pieces:\
CRC32C('MariaDB')=CRC32C(CRC32C('Maria'),'DB').

## Examples

```sql
SELECT CRC32C('MariaDB');
+-------------------+
| CRC32C('MariaDB') |
+-------------------+
|         809606978 |
+-------------------+

SELECT CRC32C(CRC32C('Maria'),'DB');
+------------------------------+
| CRC32C(CRC32C('Maria'),'DB') |
+------------------------------+
|                    809606978 |
+------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
