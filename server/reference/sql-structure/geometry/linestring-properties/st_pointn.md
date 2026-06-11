# ST\_POINTN

## Syntax

```bnf
ST_PointN(ls,N)
PointN(ls,N)
```

## Description

Returns the N-th [Point](../../../sql-statements/geometry-constructors/geometry-constructors/point.md) in the [LineString](../../../sql-statements/geometry-constructors/geometry-constructors/linestring.md) value `ls`.\
Points are numbered beginning with `1`.

`ST_PointN()` and `PointN()` are synonyms.

## Examples

```sql
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT AsText(PointN(GeomFromText(@ls),2));
+-------------------------------------+
| AsText(PointN(GeomFromText(@ls),2)) |
+-------------------------------------+
| POINT(2 2)                          |
+-------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
