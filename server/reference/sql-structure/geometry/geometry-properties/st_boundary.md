# ST\_BOUNDARY

## Syntax

```bnf
ST_BOUNDARY(g)
BOUNDARY(g)
```

## Description

Returns a geometry that is the closure of the combinatorial boundary of the geometry value _`g`_.

BOUNDARY() is a synonym.

## Examples

```sql
SELECT ST_AsText(ST_Boundary(ST_GeomFromText('LINESTRING(3 3,0 0, -3 3)')));
+----------------------------------------------------------------------+
| ST_AsText(ST_Boundary(ST_GeomFromText('LINESTRING(3 3,0 0, -3 3)'))) |
+----------------------------------------------------------------------+
| MULTIPOINT(3 3,-3 3)                                                 |
+----------------------------------------------------------------------+

SELECT ST_AsText(ST_Boundary(ST_GeomFromText('POLYGON((3 3,0 0, -3 3, 3 3))')));
+--------------------------------------------------------------------------+
| ST_AsText(ST_Boundary(ST_GeomFromText('POLYGON((3 3,0 0, -3 3, 3 3))'))) |
+--------------------------------------------------------------------------+
| LINESTRING(3 3,0 0,-3 3,3 3)                                             |
+--------------------------------------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
