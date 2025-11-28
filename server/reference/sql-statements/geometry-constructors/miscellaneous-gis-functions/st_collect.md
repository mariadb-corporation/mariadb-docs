---
description: >-
  Aggregate multiple geometries into a collection. This function creates a
  MultiPoint, MultiLineString, MultiPolygon, or GeometryCollection from a set of
  geometry arguments.
---

# ST\_Collect

{% hint style="info" %}
ST\_Collect is available from [MariaDB 12.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/release-notes-mariadb-12.0-rolling-releases/what-is-mariadb-120).
{% endhint %}

## Syntax

```sql
ST_Collect(g)
```

## Description

ST\_Collect is an aggregate function that can also be used as a window function.

Given multiple geometries, returns the aggregation of the distinct geometry arguments. This function also supports the DISTINCT option. If DISTINCT is used, it returns the aggregation of the distinct geometry arguments.

The resulting value type is chosen using the following policy:

* If all arguments are [Point](../geometry-constructors/point.md) values, the result is a [MultiPoint](../geometry-constructors/multipoint.md) value.
* If all arguments are LineString values, the result is a MultiLineString value.
* If all arguments are Polygon values, the result is a MultiPolygon value.
* Otherwise, the result is a GeometryCollection value.

If there are multiple geometry arguments and those arguments are in the same spatial reference system (SRS), the return value is in that SRS. If those arguments are not in the same SRS, an `ER_GIS_DIFFERENT_SRIDS_AGGREGATION` error occurs.

## Examples

Multiple [Point](../geometry-constructors/point.md) geometries aggregated into a [MultiPoint](../geometry-constructors/multipoint.md) geometry:

```sql
CREATE OR REPLACE TABLE t1 ( running_number INTEGER NOT NULL
  AUTO_INCREMENT, grouping_condition INTEGER, location GEOMETRY , PRIMARY KEY (
  running_number));

INSERT INTO t1 ( grouping_condition, location ) VALUES
  ( 0,ST_GEOMFROMTEXT('POINT(0 0)',4326)),
  ( 1,ST_GEOMFROMTEXT('POINT(0 0)',4326)),
  ( 0,ST_GEOMFROMTEXT('POINT(1 0)',4326)),
  ( 1,ST_GEOMFROMTEXT('POINT(2 0)',4326)),
  ( 0,ST_GEOMFROMTEXT('POINT(3 0)',4326));

SELECT ST_EQUALS( (SELECT ST_COLLECT( location ) AS t FROM t1), 
  ST_GEOMFROMTEXT('MULTIPOINT(0 0,0 0,1 0,2 0,3 0) ',4326)) AS equals;
+--------+
| equals |
+--------+
|      1 |
+--------+
```

## See Also

* [Geometry Constructors](../)
* [ST\_AsText](../wkt/st_astext.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
