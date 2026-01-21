---
description: >-
  Compute cyclic redundancy check. This function returns a 32-bit unsigned
  integer representing the CRC32 checksum of a string.
---

# CRC32

## Syntax

{% tabs %}
{% tab title="Current" %}
```sql
CRC32([par,]expr)
```
{% endtab %}

{% tab title="< 10.8" %}
```sql
CRC32(expr)
```
{% endtab %}
{% endtabs %}

## Description

Computes a cyclic redundancy check (CRC) value and returns a 32-bit unsigned value. The result is `NULL` if the argument is `NULL`. The argument is expected to be a string and (if possible) is treated as one if it is not.

{% tabs %}
{% tab title="Current" %}
Uses the alternate Castagnoli polynomia.

Often, CRC is computed in pieces. To facilitate this, there's an optional parameter: CRC32('MariaDB')=CRC32(CRC32('Maria'),'DB').
{% endtab %}

{% tab title="< 10.8" %}
Uses the ISO 3309 polynomial that used by zlib and many others.
{% endtab %}
{% endtabs %}

## Examples

{% tabs %}
{% tab title="Current" %}
```sql
SELECT CRC32(CRC32('Maria'),'DB');
+----------------------------+
| CRC32(CRC32('Maria'),'DB') |
+----------------------------+
|                 4227209140 |
+----------------------------+
```
{% endtab %}

{% tab title="< 10.8" %}
```sql
SELECT CRC32('MariaDB');
+------------------+
| CRC32('MariaDB') |
+------------------+
|       4227209140 |
+------------------+

SELECT CRC32('mariadb');
+------------------+
| CRC32('mariadb') |
+------------------+
|       2594253378 |
+------------------+
```
{% endtab %}
{% endtabs %}

## See Also

* [CRC32C()](crc32c.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
