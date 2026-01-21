---
description: >-
  Calculates the shortest distance between two geometries. Returns the minimum
  Euclidean distance between any two points in the geometries.
---

# ST\_DISTANCE

## Syntax

```sql
ST_DISTANCE(g1,g2)
```

## Description

Returns the distance between two geometries, or null if not given valid inputs.

## Example

```sql
SELECT ST_Distance(POINT(1,2),POINT(2,2));
+------------------------------------+
| ST_Distance(POINT(1,2),POINT(2,2)) |
+------------------------------------+
|                                  1 |
+------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
