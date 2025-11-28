---
description: >-
  Check if one MBR is covered by another. Returns 1 if the MBR of the first
  geometry is entirely contained within the MBR of the second geometry.
---

# MBRCoveredBy

{% hint style="info" %}
MBRCoveredBy is available from [MariaDB 12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.0-rolling-releases/what-is-mariadb-120).
{% endhint %}

## Syntax

```sql
MBRCoveredBy(g1, g2)
```

## Description

Returns 1 if the [minimum bounding rectangle](mbr-definition.md) of `g1` is covered by the minimum bounding rectangle of `g2`, otherwise 0.

Returns `NULL` If any argument is `NULL`, or an argument is an empty geometry.

## Examples

```sql
SET @g1a = ST_GeomFromText('Point(5 6)');
SET @g1b = ST_GeomFromText('Point(5 11)');
SET @g2 = ST_GeomFromText('Polygon((0 0,0 10,10 10,10 0,0 0))');

SELECT MBRCoveredby(@g1a,@g2), MBRCoveredby(@g1b,@g2);
+------------------------+------------------------+
| MBRCoveredby(@g1a,@g2) | MBRCoveredby(@g1b,@g2) |
+------------------------+------------------------+
|                      1 |                      0 |
+------------------------+------------------------+
```

## See Also

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
