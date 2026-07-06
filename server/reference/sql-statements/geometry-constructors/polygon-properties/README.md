---
description: >-
  Learn about POLYGON properties in MariaDB Server. This section details SQL
  functions for retrieving attributes of polygonal spatial objects, such as
  area, perimeter, and the number of rings.
---

# Polygon Properties

{% columns %}
{% column %}
{% content-ref url="centroid.md" %}
[centroid.md](centroid.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for ST_CENTROID. Returns the mathematical centroid of the Polygon or MultiPolygon as a Point geometry.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="polygon-properties-area.md" %}
[polygon-properties-area.md](polygon-properties-area.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for ST_AREA. Returns the double-precision area of the Polygon or MultiPolygon, calculated in its spatial reference system.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="polygon-properties-exteriorring.md" %}
[polygon-properties-exteriorring.md](polygon-properties-exteriorring.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for ST_ExteriorRing. Returns the exterior ring of a Polygon as a LineString.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="polygon-properties-interiorringn.md" %}
[polygon-properties-interiorringn.md](polygon-properties-interiorringn.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for ST_InteriorRingN. Returns the N-th interior ring of a Polygon as a LineString.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="polygon-properties-numinteriorrings.md" %}
[polygon-properties-numinteriorrings.md](polygon-properties-numinteriorrings.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for ST_NumInteriorRings. Returns the number of interior rings in a Polygon geometry.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="st_area.md" %}
[st_area.md](st_area.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Returns the area of a Polygon or MultiPolygon. The result is a double-precision number measured in the geometry's spatial reference units.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="st_centroid.md" %}
[st_centroid.md](st_centroid.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Returns the centroid of a Polygon or MultiPolygon. The result is a Point geometry representing the mathematical center of mass.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="st_exteriorring.md" %}
[st_exteriorring.md](st_exteriorring.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Returns the exterior ring of a Polygon. This function extracts the outer boundary of the polygon as a LineString geometry.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="st_interiorringn.md" %}
[st_interiorringn.md](st_interiorringn.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Returns the N-th interior ring of a Polygon. This function retrieves a specific inner hole of the polygon as a LineString.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="st_numinteriorrings.md" %}
[st_numinteriorrings.md](st_numinteriorrings.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Returns the count of interior rings in a Polygon. This function calculates the total number of inner holes within the polygon.
{% endcolumn %}
{% endcolumns %}
