---
description: >-
  Generate a Geohash string from a point or coordinates. This function encodes
  spatial locations into short, alphanumeric strings for efficient indexing and
  proximity searches.
---

# ST\_GeoHash

{% hint style="info" %}
ST\_GeoHash is available from [MariaDB 12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.0-rolling-releases/what-is-mariadb-120).
{% endhint %}

## Syntax

```sql
ST_GeoHash(longitude, latitude, max_length)
ST_GeoHash(point, max_length)
```

## Description

Returns the geohash corresponding to the input values, or NULL if any argument is NULL. Geohashes encode latitude and longitude coordinates into a text string made up only of numeric and lowercase latin letter characters.

The `longitude` parameter is a numeric value in the interval \[180, -180]. `latitude` is a numeric value in the interval \[90, -90].

In the case of `point`, the x coordinate is treated as the latitude and the y coordinate is treated as the latitude. The same constraints apply.

The `max_length` parameter is the upper limit on the resulting string size and cannot exceed 100.

The [ST\_LatFromGeoHash](st_latfromgeohash.md) function decodes a given geohash and returns the latitude.

## Examples

```sql
SELECT ST_GeoHash(ST_GeomFromText('POINT(1 1)'),15), ST_GeoHash(0,30,15);
+----------------------------------------------+---------------------+
| ST_GeoHash(ST_GeomFromText('POINT(1 1)'),15) | ST_GeoHash(0,30,15) |
+----------------------------------------------+---------------------+
| s00twy01mtw037m                              | sj248j248j248j2     |
+----------------------------------------------+---------------------+
```

## See Also

* [ST\_LatFromGeoHash](st_latfromgeohash.md)
* [Geometry Constructors](../)
* [ST\_GeomFromText](../wkt/st_geomfromtext.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
