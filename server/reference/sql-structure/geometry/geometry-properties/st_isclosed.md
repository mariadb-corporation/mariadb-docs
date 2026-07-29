# ST\_ISCLOSED

## Syntax

```bnf
ST_IsClosed(g)
IsClosed(g)
```

## Description

Returns 1 if a given [LINESTRING's](../../../sql-statements/geometry-constructors/geometry-constructors/linestring.md) start and end points are the same, or 0 if they are not the same. Before [MariaDB 10.1.5](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.5), returns NULL if not given a LINESTRING. After [MariaDB 10.1.5](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/10.1.5), returns -1.

`ST_IsClosed()` and `IsClosed()` are synonyms.

## Examples

```sql
SET @ls = 'LineString(0 0, 0 4, 4 4, 0 0)';
SELECT ST_ISCLOSED(GEOMFROMTEXT(@ls));
+--------------------------------+
| ST_ISCLOSED(GEOMFROMTEXT(@ls)) |
+--------------------------------+
|                              1 |
+--------------------------------+

SET @ls = 'LineString(0 0, 0 4, 4 4, 0 1)';
SELECT ST_ISCLOSED(GEOMFROMTEXT(@ls));
+--------------------------------+
| ST_ISCLOSED(GEOMFROMTEXT(@ls)) |
+--------------------------------+
|                              0 |
+--------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
