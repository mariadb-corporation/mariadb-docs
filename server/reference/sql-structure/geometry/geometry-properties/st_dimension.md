# ST\_DIMENSION

## Syntax

```bnf
ST_Dimension(g)
Dimension(g)
```

## Description

Returns the inherent dimension of the geometry value _`g`_. The result can\
be

| Dimension | Definition                               |
| --------- | ---------------------------------------- |
| -1        | empty geometry                           |
| 0         | geometry with no length or area          |
| 1         | geometry with no area but nonzero length |
| 2         | geometry with nonzero area               |

`ST_Dimension()` and `Dimension()` are synonyms.

## Examples

```sql
SELECT Dimension(GeomFromText('LineString(1 1,2 2)'));
+------------------------------------------------+
| Dimension(GeomFromText('LineString(1 1,2 2)')) |
+------------------------------------------------+
|                                              1 |
+------------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from [fill\_help\_tables.sql](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)_</sub>

{% @marketo/form formId="4316" %}
