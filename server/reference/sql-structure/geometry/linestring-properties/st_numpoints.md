# ST\_NUMPOINTS

## Syntax

```bnf
ST_NumPoints(ls)
NumPoints(ls)
```

## Description

Returns the number of [Point](../../../sql-statements/geometry-constructors/geometry-constructors/point.md) objects in the [LineString](../../../sql-statements/geometry-constructors/geometry-constructors/linestring.md)\
value `ls`.

`ST_NumPoints()` and `NumPoints()` are synonyms.

## Examples

```sql
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT NumPoints(GeomFromText(@ls));
+------------------------------+
| NumPoints(GeomFromText(@ls)) |
+------------------------------+
|                            3 |
+------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
