---
description: >-
  Convert to string. This function converts a value (often date/time) to a
  string, potentially using a format mask.
---

# TO\_CHAR

{% hint style="info" %}
`TO_CHAR` is available from [MariaDB 10.6.](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106)
{% endhint %}

## Syntax

```sql
TO_CHAR(expr[, fmt])
```

## Description

{% tabs %}
{% tab title="Current" %}
The `TO_CHAR` function converts an _expr_ of type [date](../../data-types/date-and-time-data-types/date.md), [datetime](../../data-types/date-and-time-data-types/datetime.md), [time](../../data-types/date-and-time-data-types/time.md) or [timestamp](../../data-types/date-and-time-data-types/timestamp.md) to a string. The optional _fmt_ argument supports `YYY/YYY/YY/RRRR/RR/MM/MON/MONTH/MI/DD/DY/HH/HH12/HH24/SS` and special characters. The default value is `YYYY-MM-DD HH24:MI:SS`. From [MariaDB 12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.0-rolling-releases/what-is-mariadb-120), `TO_CHAR` also accepts `FM` in the format string, which disables padding of all components following it.

FM can be specified multiple times, with each time disabling the previous state:

* an odd number of FMs disables padding
* an even number of FMs enables padding
{% endtab %}

{% tab title="< MariaDB 12.0" %}
The `TO_CHAR` function converts an _expr_ of type [date](../../data-types/date-and-time-data-types/date.md), [datetime](../../data-types/date-and-time-data-types/datetime.md), [time](../../data-types/date-and-time-data-types/time.md) or [timestamp](../../data-types/date-and-time-data-types/timestamp.md) to a string. The optional _fmt_ argument supports `YYY/YYY/YY/RRRR/RR/MM/MON/MONTH/MI/DD/DY/HH/HH12/HH24/SS` and special characters. The default value is `YYYY-MM-DD HH24:MI:SS`.
{% endtab %}
{% endtabs %}

In Oracle, `TO_CHAR` can also be used to convert numbers to strings, but this is not supported in MariaDB and will give an error.

## Examples

{% tabs %}
{% tab title="Current" %}
```sql
SELECT TO_CHAR('1980-01-11 04:50:39', 'YYYY-MM-DD');
+----------------------------------------------+
| TO_CHAR('1980-01-11 04:50:39', 'YYYY-MM-DD') |
+----------------------------------------------+
| 1980-01-11                                   |
+----------------------------------------------+

SELECT TO_CHAR('1980-01-11 04:50:39', 'HH24-MI-SS');
+----------------------------------------------+
| TO_CHAR('1980-01-11 04:50:39', 'HH24-MI-SS') |
+----------------------------------------------+
| 04-50-39                                     |
+----------------------------------------------+

SELECT TO_CHAR('00-01-01 00:00:00', 'YY-MM-DD HH24:MI:SS');
+-----------------------------------------------------+
| TO_CHAR('00-01-01 00:00:00', 'YY-MM-DD HH24:MI:SS') |
+-----------------------------------------------------+
| 00-01-01 00:00:00                                   |
+-----------------------------------------------------+

SELECT TO_CHAR('99-12-31 23:59:59', 'YY-MM-DD HH24:MI:SS');
+-----------------------------------------------------+
| TO_CHAR('99-12-31 23:59:59', 'YY-MM-DD HH24:MI:SS') |
+-----------------------------------------------------+
| 99-12-31 23:59:59                                   |
+-----------------------------------------------------+

SELECT TO_CHAR('9999-12-31 23:59:59', 'YY-MM-DD HH24:MI:SS');
+-------------------------------------------------------+
| TO_CHAR('9999-12-31 23:59:59', 'YY-MM-DD HH24:MI:SS') |
+-------------------------------------------------------+
| 99-12-31 23:59:59                                     |
+-------------------------------------------------------+

SELECT TO_CHAR('21-01-03 08:30:00', 'Y-MONTH-DY HH:MI:SS');
+-----------------------------------------------------+
| TO_CHAR('21-01-03 08:30:00', 'Y-MONTH-DY HH:MI:SS') |
+-----------------------------------------------------+
| 1-January  -Sun 08:30:00                            |
+-----------------------------------------------------+

From MariaDB 12.0, FM removes following padding:

SELECT CONCAT('/', TO_CHAR('2020-01-06 10:11:12', 'DAY'), '/');
+---------------------------------------------------------+
| CONCAT('/', TO_CHAR('2020-01-06 10:11:12', 'DAY'), '/') |
+---------------------------------------------------------+
| /Monday   /                                             |
+---------------------------------------------------------+

SELECT CONCAT('/', TO_CHAR('2020-01-06 10:11:12', 'FMDAY'), '/');
+-----------------------------------------------------------+
| CONCAT('/', TO_CHAR('2020-01-06 10:11:12', 'FMDAY'), '/') |
+-----------------------------------------------------------+
| /Monday/                                                  |
+-----------------------------------------------------------+

Even numbers of FM enable padding, while odd numbers disable it:

SELECT CONCAT('/', TO_CHAR('2020-01-06 10:11:12', 'FMFMDAY'), '/');
+-------------------------------------------------------------+
| CONCAT('/', TO_CHAR('2020-01-06 10:11:12', 'FMFMDAY'), '/') |
+-------------------------------------------------------------+
| /Monday   /                                                 |
+-------------------------------------------------------------+

SELECT CONCAT('/', TO_CHAR('2020-01-06 10:11:12', 'FMFMFMDAY'), '/');
+---------------------------------------------------------------+
| CONCAT('/', TO_CHAR('2020-01-06 10:11:12', 'FMFMFMDAY'), '/') |
+---------------------------------------------------------------+
| /Monday/                                                      |
+---------------------------------------------------------------+

FM only suppresses following padding:

SELECT CONCAT('/', TO_CHAR('2020-01-06 10:11:12', 'DAYFM'), '/');
+-----------------------------------------------------------+
| CONCAT('/', TO_CHAR('2020-01-06 10:11:12', 'DAYFM'), '/') |
+-----------------------------------------------------------+
| /Monday   /                                               |
+-----------------------------------------------------------+
```
{% endtab %}

{% tab title="< 12.0" %}
```sql
SELECT TO_CHAR('1980-01-11 04:50:39', 'YYYY-MM-DD');
+----------------------------------------------+
| TO_CHAR('1980-01-11 04:50:39', 'YYYY-MM-DD') |
+----------------------------------------------+
| 1980-01-11                                   |
+----------------------------------------------+

SELECT TO_CHAR('1980-01-11 04:50:39', 'HH24-MI-SS');
+----------------------------------------------+
| TO_CHAR('1980-01-11 04:50:39', 'HH24-MI-SS') |
+----------------------------------------------+
| 04-50-39                                     |
+----------------------------------------------+

SELECT TO_CHAR('00-01-01 00:00:00', 'YY-MM-DD HH24:MI:SS');
+-----------------------------------------------------+
| TO_CHAR('00-01-01 00:00:00', 'YY-MM-DD HH24:MI:SS') |
+-----------------------------------------------------+
| 00-01-01 00:00:00                                   |
+-----------------------------------------------------+

SELECT TO_CHAR('99-12-31 23:59:59', 'YY-MM-DD HH24:MI:SS');
+-----------------------------------------------------+
| TO_CHAR('99-12-31 23:59:59', 'YY-MM-DD HH24:MI:SS') |
+-----------------------------------------------------+
| 99-12-31 23:59:59                                   |
+-----------------------------------------------------+

SELECT TO_CHAR('9999-12-31 23:59:59', 'YY-MM-DD HH24:MI:SS');
+-------------------------------------------------------+
| TO_CHAR('9999-12-31 23:59:59', 'YY-MM-DD HH24:MI:SS') |
+-------------------------------------------------------+
| 99-12-31 23:59:59                                     |
+-------------------------------------------------------+

SELECT TO_CHAR('21-01-03 08:30:00', 'Y-MONTH-DY HH:MI:SS');
+-----------------------------------------------------+
| TO_CHAR('21-01-03 08:30:00', 'Y-MONTH-DY HH:MI:SS') |
+-----------------------------------------------------+
| 1-January  -Sun 08:30:00                            |
+-----------------------------------------------------+
```
{% endtab %}
{% endtabs %}

## See Also

* [SQL\_MODE=ORACLE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
