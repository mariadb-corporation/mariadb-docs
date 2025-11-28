---
description: >-
  Checks if the LineString is a ring. Returns 1 if the LineString is both closed
  (start equals end) and simple (no self-intersection).
---

# ST\_IsRing

## Syntax

```sql
ST_IsRing(g)
IsRing(g)
```

## Description

Returns true if a given [LINESTRING](../geometry-constructors/linestring.md) is a ring, that is, both [ST\_IsClosed](st_isclosed.md) and [ST\_IsSimple](st_issimple.md). A simple curve does not pass through the same point more than once. However, see [MDEV-7510](https://jira.mariadb.org/browse/MDEV-7510).

`St_IsRing()` and `IsRing()` are synonyms.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
