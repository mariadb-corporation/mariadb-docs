---
description: >-
  Returns a Point guaranteed to lie on the surface of the given geometry. This
  standard function finds a representative point strictly within the geometry's
  area.
---

# ST\_POINTONSURFACE

## Syntax

```sql
ST_PointOnSurface(g)
PointOnSurface(g)
```

## Description

Given a geometry, returns a [POINT](point.md) guaranteed to intersect a surface. However, see [MDEV-7514](https://jira.mariadb.org/browse/MDEV-7514).

ST\_PointOnSurface() and PointOnSurface() are synonyms.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
