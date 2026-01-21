---
description: >-
  Returns a geometry representing the difference between two geometries. The
  result contains points from the first geometry that are not in the second.
---

# ST\_DIFFERENCE

## Syntax

```sql
ST_DIFFERENCE(g1,g2)
```

## Description

Returns a geometry representing the point set difference of the given geometry values.

## Example

```sql
SET @g1 = POINT(10,10), @g2 = POINT(20,20);

SELECT ST_AsText(ST_Difference(@g1, @g2));
+------------------------------------+
| ST_AsText(ST_Difference(@g1, @g2)) |
+------------------------------------+
| POINT(10 10)                       |
+------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
