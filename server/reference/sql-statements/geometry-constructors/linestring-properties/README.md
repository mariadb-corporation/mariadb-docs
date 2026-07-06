---
description: >-
  Learn about LINESTRING properties in MariaDB Server. This section details SQL
  functions for retrieving attributes of linear spatial objects, such as length,
  number of points, and start/end points.
---

# LineString Properties

{% columns %}
{% column %}
{% content-ref url="linestring-properties-endpoint.md" %}
[linestring-properties-endpoint.md](linestring-properties-endpoint.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for ST_ENDPOINT. Returns the last point of a LineString geometry.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="glength.md" %}
[glength.md](glength.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for ST_LENGTH. Calculates the length of a LineString or MultiLineString in its associated spatial reference units.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="linestring-properties-numpoints.md" %}
[linestring-properties-numpoints.md](linestring-properties-numpoints.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for ST_NUMPOINTS. Returns the number of points in a LineString geometry.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="linestring-properties-pointn.md" %}
[linestring-properties-pointn.md](linestring-properties-pointn.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for ST_POINTN. Returns the N-th point in a LineString geometry, where N is a 1-based index.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="linestring-properties-startpoint.md" %}
[linestring-properties-startpoint.md](linestring-properties-startpoint.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Synonym for ST_STARTPOINT. Returns the first point of a LineString geometry.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="st_endpoint.md" %}
[st_endpoint.md](st_endpoint.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Returns the end Point of a LineString. This function retrieves the final coordinate in the linear geometry sequence.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="st_numpoints.md" %}
[st_numpoints.md](st_numpoints.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Returns the count of Points in a LineString. This function calculates the total number of vertices defining the line.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="st_pointn.md" %}
[st_pointn.md](st_pointn.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Returns the N-th Point in a LineString. This function retrieves a specific point from the sequence based on its 1-based index.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="st_startpoint.md" %}
[st_startpoint.md](st_startpoint.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Returns the start Point of a LineString. This function retrieves the initial coordinate in the linear geometry sequence.
{% endcolumn %}
{% endcolumns %}
