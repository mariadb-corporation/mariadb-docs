# FORMAT\_BYTES

**MariaDB starting with** [**11.8**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-8-series/what-is-mariadb-118)

Introduced in [MariaDB 11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-8-series/what-is-mariadb-118)

## Syntax

```
FORMAT_BYTES(double)
```

## Description

Given a byte count, returns a string consisting of a value and the units in a human-readable format. The units will be in bytes, KiB (kibibytes), MiB (mebibytes), GiB (gibibytes), TiB (tebibytes), PiB (pebibytes) or EiB (exbibytes).

The binary prefixes (kibi, mebi, gibi, tebi, pebi and exbi) were created in December 1998 by the International Electrotechnical Commission to avoid possible ambiguity, as the widely-used prefixes kilo, mega, giga, tera, peta and exa can be used to refer to both the power-of-10 decimal system multipliers and the power-of-two binary system multipliers.

This function is similar to the [Sys Schema format\_bytes](../../../sql-statements/administrative-sql-statements/system-tables/sys-schema/sys-schema-stored-functions/sys_schema_format_bytes.md) function, except that function does not display exbibytes.

## Examples

```
SELECT FORMAT_BYTES(1000)FORMAT_BYTES(1024);
+--------------------+--------------------+
| FORMAT_BYTES(1000) | FORMAT_BYTES(1024) |
+--------------------+--------------------+
| 1000 bytes         | 1.00 KiB           |
+--------------------+--------------------+

SELECT FORMAT_BYTES(1000000),FORMAT_BYTES(1048576);
+-----------------------+-----------------------+
| FORMAT_BYTES(1000000) | FORMAT_BYTES(1048576) |
+-----------------------+-----------------------+
| 976.56 KiB            | 1.00 MiB              |
+-----------------------+-----------------------+

SELECT FORMAT_BYTES(1000000000),FORMAT_BYTES(1073741874);
+--------------------------+--------------------------+
| FORMAT_BYTES(1000000000) | FORMAT_BYTES(1073741874) |
+--------------------------+--------------------------+
| 953.67 MiB               | 1.00 GiB                     |
+--------------------------+--------------------------+

SELECT FORMAT_BYTES(1000000000000),FORMAT_BYTES(1099511627776);
+-----------------------------+-----------------------------+
| FORMAT_BYTES(1000000000000) | FORMAT_BYTES(1099511627776) |
+-----------------------------+-----------------------------+
| 931.32 GiB                  | 1.00 TiB                    |
+-----------------------------+-----------------------------+

SELECT FORMAT_BYTES(1000000000000000),FORMAT_BYTES(1125899906842624);
+--------------------------------+--------------------------------+
| FORMAT_BYTES(1000000000000000) | FORMAT_BYTES(1125899906842624) |
+--------------------------------+--------------------------------+
| 909.49 TiB                     | 1.00 PiB                       |
+--------------------------------+--------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
