# ST\_STARTPOINT

## Syntax

```bnf
ST_StartPoint(ls)
StartPoint(ls)
```

## Description

Returns the [Point](../../../sql-statements/geometry-constructors/geometry-constructors/point.md) that is the start point of the [LineString](../../../sql-statements/geometry-constructors/geometry-constructors/linestring.md) value `ls`.

`ST_StartPoint()` and `StartPoint()` are synonyms.

## Examples

```sql
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT AsText(StartPoint(GeomFromText(@ls)));
+---------------------------------------+
| AsText(StartPoint(GeomFromText(@ls))) |
+---------------------------------------+
| POINT(1 1)                            |
+---------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
