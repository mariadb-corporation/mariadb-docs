# ST\_ENDPOINT

## Syntax

```bnf
ST_EndPoint(ls)
EndPoint(ls)
```

## Description

Returns the [Point](../../../sql-statements/geometry-constructors/geometry-constructors/point.md) that is the endpoint of the [LineString](../../../sql-statements/geometry-constructors/geometry-constructors/linestring.md) value `ls`.

`ST_EndPoint()` and `EndPoint()` are synonyms.

## Examples

```sql
SET @ls = 'LineString(1 1,2 2,3 3)';

SELECT AsText(EndPoint(GeomFromText(@ls)));
+-------------------------------------+
| AsText(EndPoint(GeomFromText(@ls))) |
+-------------------------------------+
| POINT(3 3)                          |
+-------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
