---
description: >-
  Learn about Minimum Bounding Rectangles (MBR) in MariaDB Server. This section
  details how to calculate and use MBRs for spatial indexing and efficient
  querying of geometric data.
---

# MBR (Minimum Bounding Rectangle)

{% columns %}
{% column %}
{% content-ref url="mbr-definition.md" %}
[mbr-definition.md](mbr-definition.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand Minimum Bounding Rectangles. An MBR is the smallest rectangle that completely encloses a geometry, defined by its minimum and maximum X and Y coordinates.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mbrcontains.md" %}
[mbrcontains.md](mbrcontains.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Check if one MBR contains another. Returns 1 if the Minimum Bounding Rectangle of the first geometry completely encloses the MBR of the second geometry.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mbrcoveredby.md" %}
[mbrcoveredby.md](mbrcoveredby.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Check if one MBR is covered by another. Returns 1 if the MBR of the first geometry is entirely contained within the MBR of the second geometry.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mbrdisjoint.md" %}
[mbrdisjoint.md](mbrdisjoint.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Check if two MBRs are disjoint. Returns 1 if the Minimum Bounding Rectangles of the two geometries do not intersect or touch at all.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mbrequal.md" %}
[mbrequal.md](mbrequal.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Check if two MBRs are identical. Returns 1 if the Minimum Bounding Rectangles of both geometries share the exact same coordinates.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mbrintersects.md" %}
[mbrintersects.md](mbrintersects.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Check if two MBRs intersect. Returns 1 if the Minimum Bounding Rectangles of the geometries share any portion of space, including boundaries.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mbroverlaps.md" %}
[mbroverlaps.md](mbroverlaps.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Check if two MBRs overlap. Returns 1 if the MBRs intersect but neither completely contains the other, and they have the same dimension.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mbrtouches.md" %}
[mbrtouches.md](mbrtouches.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Check if two MBRs touch. Returns 1 if the MBRs intersect only at their boundaries and do not share any interior points.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mbrwithin.md" %}
[mbrwithin.md](mbrwithin.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Check if one MBR is within another. Returns 1 if the MBR of the first geometry is completely enclosed by the MBR of the second geometry.
{% endcolumn %}
{% endcolumns %}
