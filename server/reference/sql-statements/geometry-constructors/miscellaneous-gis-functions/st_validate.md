---
description: >-
  Validate and optionally return a geometry. This function checks if a geometry
  is valid according to OGC rules; it returns the geometry if valid, or NULL if
  not.
---

# ST\_Validate

{% hint style="info" %}
ST\_Validate is available from [MariaDB 12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.0-rolling-releases/what-is-mariadb-120).
{% endhint %}

## Syntax

```sql
ST_Validate(g)
```

## Description

The function checks that a given geometry is compliant with the Well-Known Binary (WKB) format and Spatial Reference System Identifier (SRID) syntax, and is geometrically valid.

It returns the geometry if it's valid, or NULL if not.

The function is useful to filter out invalid geometry data.

## Examples

A [POINT](../geometry-constructors/point.md) requires both x and y co-ordinates:

```sql
SELECT ST_ASTEXT(ST_VALIDATE(ST_GeomFromText('POINT(1 0)')));          
+-------------------------------------------------------+
| ST_ASTEXT(ST_VALIDATE(ST_GeomFromText('POINT(1 0)'))) |
+-------------------------------------------------------+
| POINT(1 0)                                            |
+-------------------------------------------------------+

SELECT ST_ASTEXT(ST_VALIDATE(ST_GeomFromText('POINT(1)')));  
+-----------------------------------------------------+
| ST_ASTEXT(ST_VALIDATE(ST_GeomFromText('POINT(1)'))) |
+-----------------------------------------------------+
| NULL                                                |
+-----------------------------------------------------+
```

## See Also

* [Geometry Constructors](../)
* [ST\_AsText](../wkt/st_astext.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
