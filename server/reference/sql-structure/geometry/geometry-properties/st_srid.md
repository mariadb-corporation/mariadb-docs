# ST\_SRID

## Syntax

```bnf
ST_SRID(g)
SRID(g)
```

## Description

Returns an integer indicating the Spatial Reference System ID for the\
geometry value g.

In MariaDB, the SRID value is just an integer associated with the\
geometry value. All calculations are done assuming Euclidean (planar)\
geometry.

`ST_SRID()` and `SRID()` are synonyms.

## Examples

```sql
SELECT SRID(GeomFromText('LineString(1 1,2 2)',101));
+-----------------------------------------------+
| SRID(GeomFromText('LineString(1 1,2 2)',101)) |
+-----------------------------------------------+
|                                           101 |
+-----------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
