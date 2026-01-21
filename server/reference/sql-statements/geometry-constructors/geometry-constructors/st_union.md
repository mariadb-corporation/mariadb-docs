---
description: >-
  Returns a geometry representing the point set union of two geometries. This
  function merges multiple spatial objects into a single geometry.
---

# ST\_UNION

## Syntax

```sql
ST_UNION(g1,g2)
```

## Description

Returns a geometry that is the union of the geometry _`g1`_ and geometry _`g2`_.

## Examples

```sql
SET @g1 = GEOMFROMTEXT('POINT (0 2)');

SET @g2 = GEOMFROMTEXT('POINT (2 0)');

SELECT ASTEXT(ST_UNION(@g1,@g2));
+---------------------------+
| ASTEXT(ST_UNION(@g1,@g2)) |
+---------------------------+
| MULTIPOINT(2 0,0 2)       |
+---------------------------+
```

```sql
SET @g1 = GEOMFROMTEXT('POLYGON((0 0,0 3,3 3,3 0,0 0))');

SET @g2 = GEOMFROMTEXT('POLYGON((2 2,4 2,4 4,2 4,2 2))');

SELECT ASTEXT(ST_UNION(@g1,@g2));
+------------------------------------------------+
| ASTEXT(ST_UNION(@g1,@g2))                      |
+------------------------------------------------+
| POLYGON((0 0,0 3,2 3,2 4,4 4,4 2,3 2,3 0,0 0)) |
+------------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
