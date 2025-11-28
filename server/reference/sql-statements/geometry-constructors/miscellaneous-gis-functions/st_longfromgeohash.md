---
description: >-
  Decode a Geohash to retrieve the longitude. This function returns the
  longitude coordinate (X-axis) from a given Geohash string.
---

# ST\_LongFromGeoHash

{% hint style="info" %}
ST\_LongFromGeoHash is available from [MariaDB 12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.0-rolling-releases/what-is-mariadb-120).
{% endhint %}

## Syntax

```sql
ST_LongFromGeoHash(geohash)
```

## Description

Decodes a given `geohash` string and returns the longitude in the interval \[180, -180].

If the argument is NULL, the return value is NULL. If the argument is invalid, an ER\_INCORRECT\_TYPE error is thrown.

The [ST\_GeoHash](st_geohash.md) function can be used to generate geohashes.

## Examples

```sql
SELECT ST_LongFromGeoHash('zzzzzzzzz'), ST_LongFromGeoHash('sj248j248j248j2');           
+---------------------------------+---------------------------------------+
| ST_LongFromGeoHash('zzzzzzzzz') | ST_LongFromGeoHash('sj248j248j248j2') |
+---------------------------------+---------------------------------------+
|                             180 |                                     0 |
+---------------------------------+---------------------------------------+
```

## See Also

* [ST\_GeoHash](st_geohash.md)
* [ST\_LatFromGeoHash](st_latfromgeohash.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
