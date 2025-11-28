---
description: >-
  Create a Point geometry from a Geohash. This function decodes a Geohash string
  into a Point object representing the location's center.
---

# ST\_PointFromGeoHash

{% hint style="info" %}
ST\_PointFromGeoHash is available from [MariaDB 12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.0-rolling-releases/what-is-mariadb-120).
{% endhint %}

## Syntax

```sql
ST_PointFromGeoHash(geohash, srid)
```

## Description

Takes a given `geohash` string and returns a point where the x is the longitude and the y is the latitude.

The latitude is returned as a numeric value in the interval \[180, -180]. The longitude is returned as a numeric value in the interval \[90, -90]. If the argument is NULL, the return value is NULL. If the argument is invalid, an ER\_GIS\_INVALID\_DATA is thrown.

## Examples

```sql
SELECT ST_ASTEXT(ST_POINTFROMGEOHASH("s00twy01mtw037m",0));
+-----------------------------------------------------+
| ST_ASTEXT(ST_POINTFROMGEOHASH("s00twy01mtw037m",0)) |
+-----------------------------------------------------+
| POINT(1 1)                                          |
+-----------------------------------------------------+

SELECT ST_ASTEXT(ST_POINTFROMGEOHASH(ST_GEOHASH(180,90,20),0));
+---------------------------------------------------------+
| ST_ASTEXT(ST_POINTFROMGEOHASH(ST_GEOHASH(180,90,20),0)) |
+---------------------------------------------------------+
| POINT(180 90)                                           |
+---------------------------------------------------------+
```

## See Also

* [ST\_GeoHash](st_geohash.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
