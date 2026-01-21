---
description: >-
  Decode a Geohash to retrieve the latitude. This function returns the latitude
  coordinate (Y-axis) from a given Geohash string.
---

# ST\_LatFromGeoHash

{% hint style="info" %}
ST\_LatFromGeoHash is available from [MariaDB 12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.0-rolling-releases/what-is-mariadb-120).
{% endhint %}

## Syntax

```sql
ST_LatFromGeoHash(geohash)
```

## Description

Decodes a given `geohash` string and returns the latitude in the interval \[90, -90].

If the argument is NULL, the return value is NULL. If the argument is invalid, an ER\_INCORRECT\_TYPE error is thrown.

The [ST\_GeoHash](st_geohash.md) function can be used to generate geohashes.

## Examples

```sql
SELECT ST_LatFromGeoHash('zzzzzzzzz'), ST_LatFromGeoHash('xvrfxvrfxvrfxvr');
+--------------------------------+--------------------------------------+
| ST_LatFromGeoHash('zzzzzzzzz') | ST_LatFromGeoHash('xvrfxvrfxvrfxvr') |
+--------------------------------+--------------------------------------+
|                             90 |                                   30 |
+--------------------------------+--------------------------------------+
```

## See Also

* [ST\_GeoHash](st_geohash.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
