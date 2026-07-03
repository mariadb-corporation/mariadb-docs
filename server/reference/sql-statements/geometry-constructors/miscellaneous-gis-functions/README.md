---
description: >-
  Explore miscellaneous GIS functions in MariaDB Server. This section details
  various SQL functions that support geographic information system operations
  and spatial data analysis.
---

# Miscellaneous GIS functions

{% columns %}
{% column %}
{% content-ref url="st_collect.md" %}
[st_collect.md](st_collect.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Aggregate multiple geometries into a collection. This function creates a MultiPoint, MultiLineString, MultiPolygon, or GeometryCollection from a set of geometry arguments.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="st_geohash.md" %}
[st_geohash.md](st_geohash.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Generate a Geohash string from a point or coordinates. This function encodes spatial locations into short, alphanumeric strings for efficient indexing and proximity searches.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="st_isvalid.md" %}
[st_isvalid.md](st_isvalid.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Check if a geometry is valid. This function returns 1 if the geometry complies with OGC specifications (e.g., no self-intersections), 0 otherwise.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="st_latfromgeohash.md" %}
[st_latfromgeohash.md](st_latfromgeohash.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Decode a Geohash to retrieve the latitude. This function returns the latitude coordinate (Y-axis) from a given Geohash string.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="st_longfromgeohash.md" %}
[st_longfromgeohash.md](st_longfromgeohash.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Decode a Geohash to retrieve the longitude. This function returns the longitude coordinate (X-axis) from a given Geohash string.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="st_pointfromgeohash.md" %}
[st_pointfromgeohash.md](st_pointfromgeohash.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Create a Point geometry from a Geohash. This function decodes a Geohash string into a Point object representing the location's center.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="st_simplify.md" %}
[st_simplify.md](st_simplify.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Simplify a geometry using the Douglas-Peucker algorithm. This function reduces the number of vertices in a geometry while preserving its general shape, useful for rendering maps.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="st_validate.md" %}
[st_validate.md](st_validate.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Validate and optionally return a geometry. This function checks if a geometry is valid according to OGC rules; it returns the geometry if valid, or NULL if not.
{% endcolumn %}
{% endcolumns %}
