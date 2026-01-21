---
description: >-
  Tests if two geometries are spatially related according to a given DE-9IM
  intersection matrix pattern.
---

# ST\_RELATE

## Syntax

```sql
ST_Relate(g1, g2, i)
```

## Description

Returns true if Geometry `g1` is spatially related to Geometry`g2` by testing for intersections between the interior, boundary and exterior of the two geometries as specified by the values in intersection matrix pattern `i`.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
