# ST\_IsValid

**MariaDB starting with** [**11.8**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-8-series/what-is-mariadb-118)

ST\_IsValid was added in [MariaDB 11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-11-8-series/what-is-mariadb-118).

## Syntax

```bnf
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

A [POINT](../../../sql-statements/geometry-constructors/geometry-constructors/point.md) requires both x and y coordinates:

```
SELECT ST_IsValid(ST_GeomFromText('POINT (0)'));  
ERROR 3037 (22023): Invalid GIS data provided to function st_isvalid.
```

## See Also

* [Geometry Constructors](../geometry-constructors/)
* [ST\_AsText](../wkt/st_astext.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
