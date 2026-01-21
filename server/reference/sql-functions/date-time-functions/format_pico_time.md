---
description: >-
  Format a time in picoseconds. This function converts a numeric picosecond
  value into a human-readable string with units like ps, ns, us, ms, s, m, h, or
  d.
---

# FORMAT\_PICO\_TIME

{% hint style="info" %}
FORMAT\_PICO\_TIME is available from [MariaDB 11.0.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-2-release-notes).
{% endhint %}

## Syntax

```sql
FORMAT_PICO_TIME(time_val)
```

## Description

Given a time in picoseconds, returns a human-readable time value and unit indicator. Resulting unit is dependent on the length of the argument, and can be:

* ps - picoseconds
* ns - nanoseconds
* us - microseconds
* ms - milliseconds
* s - seconds
* min - minutes
* h - hours
* d - days

With the exception of results under one nanosecond, which are not rounded and are represented as whole numbers, the result is rounded to 2 decimal places, with a minimum of 3 significant digits.

Returns NULL if the argument is NULL.

This function is very similar to the [Sys Schema](../../system-tables/sys-schema/) [FORMAT\_TIME](../../system-tables/sys-schema/sys-schema-stored-functions/format_time.md) function, but with the following differences:

* Represents minutes as `min` rather than `m`.
* Does not represent weeks.

## Examples

```sql
SELECT
    FORMAT_PICO_TIME(43) AS ps,
    FORMAT_PICO_TIME(4321) AS ns, 
    FORMAT_PICO_TIME(43211234) AS us,
    FORMAT_PICO_TIME(432112344321) AS ms,
    FORMAT_PICO_TIME(43211234432123) AS s,
    FORMAT_PICO_TIME(432112344321234) AS m,
    FORMAT_PICO_TIME(4321123443212345) AS h,
    FORMAT_PICO_TIME(432112344321234545) AS d;
+--------+---------+----------+-----------+---------+----------+--------+--------+
| ps     | ns      | us       | ms        | s       | m        | h      | d      |
+--------+---------+----------+-----------+---------+----------+--------+--------+
|  43 ps | 4.32 ns | 43.21 us | 432.11 ms | 43.21 s | 7.20 min | 1.20 h | 5.00 d |
+--------+---------+----------+-----------+---------+----------+--------+--------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
