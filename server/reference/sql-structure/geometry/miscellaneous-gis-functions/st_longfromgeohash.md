# ST\_LongFromGeoHash

**MariaDB starting with** [**11.8**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-8-series/what-is-mariadb-118)

ST\_LongFromGeoHash was added in [MariaDB 11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-8-series/what-is-mariadb-118).

## Syntax

```bnf
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
