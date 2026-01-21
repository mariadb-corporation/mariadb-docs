---
description: >-
  Truncate a date. In Oracle mode, this function truncates a date value to a
  specified unit of measure.
---

# TRUNC

{% hint style="info" %}
Introduced in [MariaDB 12.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/12.2/mariadb-12.2-changes-and-improvements).
{% endhint %}

## Syntax

```sql
TRUNC(date[,fmt])
```

## Description

Returns a [DATETIME](../../data-types/date-and-time-data-types/datetime.md) truncated according to `fmt`.

**Supported formats:**

Truncate to day: `DD`, `DDD`, `J`\
Truncate to month: `MM`, `MON`, `MONTH`, `RM`\
Truncate to year: `SYEAR`, `SYYYY`, `Y`,`YEAR`, `YY`, `YYY`, `YYYY`

## Examples

```sql
SELECT TRUNC('2025-09-24 12:43','DD');
+--------------------------------+
| TRUNC('2025-09-24 12:43','DD') |
+--------------------------------+
| 2025-09-24 00:00:00            |
+--------------------------------+

SELECT TRUNC('2025-09-24 12:43','MM');
+--------------------------------+
| TRUNC('2025-09-24 12:43','MM') |
+--------------------------------+
| 2025-09-01 00:00:00            |
+--------------------------------+

SELECT TRUNC('2025-09-24 12:43','YY');
+--------------------------------+
| TRUNC('2025-09-24 12:43','YY') |
+--------------------------------+
| 2025-01-01 00:00:00            |
+--------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
