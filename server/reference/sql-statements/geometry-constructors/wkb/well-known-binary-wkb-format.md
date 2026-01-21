---
description: >-
  Understand the standard binary format for geometry. This overview explains how
  WKB represents spatial data types for storage and exchange.
---

# Well-Known Binary (WKB) Format

WKB stands for Well-Known Binary, a format for representing geographical and geometrical data.

WKB uses 1-byte unsigned integers, 4-byte unsigned integers, and 8-byte double-precision numbers.

* The first byte indicates the byte order. 00 for big endian, or 01 for little endian.
* The next 4 bytes indicate the geometry type. Values from 1 to 7 indicate whether the type is Point, LineString, Polygon, MultiPoint, MultiLineString, MultiPolygon, or GeometryCollection respectively.
* The 8-byte floats represent the co-ordinates.

Take the following example, a sequence of 21 bytes each represented by two hex digits:

```
000000000140000000000000004010000000000000
```

* It's big endian
  * 000000000140000000000000004010000000000000
* It's a POINT
  * 000000000140000000000000004010000000000000
* The X co-ordinate is 2.0
  * 000000000140000000000000004010000000000000
* The Y-co-ordinate is 4.0
  * 000000000140000000000000004010000000000000

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
