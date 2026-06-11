# ST\_IsRing

## Syntax

```bnf
ST_IsRing(g)
IsRing(g)
```

## Description

Returns true if a given [LINESTRING](../../../sql-statements/geometry-constructors/geometry-constructors/linestring.md) is a ring, that is, both [ST\_IsClosed](st_isclosed.md) and [ST\_IsSimple](st_issimple.md). A simple curve does not pass through the same point more than once. However, see [MDEV-7510](https://jira.mariadb.org/browse/MDEV-7510).

`St_IsRing()` and `IsRing()` are synonyms.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
