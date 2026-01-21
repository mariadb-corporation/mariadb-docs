---
description: >-
  Check if a geometry is valid. This function returns 1 if the geometry complies
  with OGC specifications (e.g., no self-intersections), 0 otherwise.
---

# ST\_IsValid

{% hint style="info" %}
ST\_IsValid is available from [MariaDB 12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.0-rolling-releases/what-is-mariadb-120).
{% endhint %}

## Syntax

```sql
ST_IsValid(g)
```

## Description

Given a geometry input, returns 1 if the argument is geometrically valid according to the OGC specifications, 0 if the argument is not geometrically valid.

Unlike [ST\_Validate](st_validate.md), requires valid GIS data, or `ERROR 3037 (22023): Invalid GIS data provided to function st_isvalid` is returned.

## Examples

```sql
SELECT ST_IsValid(ST_GeomFromText('LINESTRING (0 0, 1 1)'));
+------------------------------------------------------+
| ST_IsValid(ST_GeomFromText('LINESTRING (0 0, 1 1)')) |
+------------------------------------------------------+
|                                                    1 |
+------------------------------------------------------+

SELECT ST_IsValid(ST_GeomFromText('LINESTRING (0 0, 0 0)'));
+------------------------------------------------------+
| ST_IsValid(ST_GeomFromText('LINESTRING (0 0, 0 0)')) |
+------------------------------------------------------+
|                                                    0 |
+------------------------------------------------------+
```

A [POINT](../geometry-constructors/point.md) requires both x and y co-ordinates:

```sql
SELECT ST_IsValid(ST_GeomFromText('POINT (0)'));  
ERROR 3037 (22023): Invalid GIS data provided to function st_isvalid.
```

## See Also

* [Geometry Constructors](../)
* [ST\_AsText](../wkt/st_astext.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
