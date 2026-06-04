# ST\_OVERLAPS

## Syntax

```bnf
ST_OVERLAPS(g1,g2)
```

## Description

Returns `1` or `0` to indicate whether geometry _`g1`_ spatially overlaps geometry _`g2`_.

The term spatially overlaps is used if two geometries of equal dimensions intersect and their\
intersection results in a geometry of the same dimension but not equal to\
either of the given geometries.

ST\_OVERLAPS() uses object shapes, while [OVERLAPS()](overlaps.md), based on the original MySQL implementation, uses object bounding rectangles.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
