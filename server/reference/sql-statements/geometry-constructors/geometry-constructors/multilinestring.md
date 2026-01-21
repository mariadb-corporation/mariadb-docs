---
description: >-
  Constructs a MultiLineString value from a list of WKB LineString arguments.
  This function creates a collection of multiple line strings.
---

# MULTILINESTRING

## Syntax

```sql
MultiLineString(ls1,ls2,...)
```

## Description

Constructs a WKB MultiLineString value using [WKB](../wkb/) [LineString](linestring.md) arguments. If any argument is not a WKB LineString, the return value is`NULL`.

## Example

```sql
CREATE TABLE gis_multi_line (g MULTILINESTRING);
INSERT INTO gis_multi_line VALUES
 (MultiLineStringFromText('MULTILINESTRING((10 48,10 21,10 0),(16 0,16 23,16 48))')),
 (MLineFromText('MULTILINESTRING((10 48,10 21,10 0))')),
 (MLineFromWKB(AsWKB(MultiLineString(LineString(Point(1, 2), 
    Point(3, 5)), LineString(Point(2, 5),Point(5, 8),Point(21, 7))))));
```

MultiLineString\_Example:

```sql
CREATE TABLE mlstr_example (
  m MULTILINESTRING
);
```

```sql
INSERT INTO mlstr_example VALUES
  (ST_MultiLineStringFromText(
    'MULTILINESTRING((0 40, 0 20, 6 30, 12 20, 12 40),
    (15 40, 15 20, 25 20, 30 25, 30 35, 25 40, 15 40))')),
  (ST_MLineFromText('MULTILINESTRING((0 0, 1 1, 2 2))')),
  (MultiLineString(
    LineString(Point(0, 40), Point(0, 20)),
    LineString(Point(6, 30), Point(12, 20), Point(12, 40))));
```

```sql
INSERT INTO mlstr_example VALUES
  (MultiLineStringFromText(
    'MULTILINESTRING((0 40, 0 20, 6 30, 12 20, 12 40),
    (15 40, 15 20, 25 20, 30 25, 30 35, 25 40, 15 40))')),
  (MLineFromText('MULTILINESTRING((0 0, 1 1, 2 2))')),
  (MultiLineString(
    LineString(Point(0, 40), Point(0, 20)),
    LineString(Point(6, 30), Point(12, 20), Point(12, 40))));
```

```sql
SELECT ST_AsWKT(m) FROM mlstr_example;
```

```sql
+-------------------------------------------------------------------------------------------+
| ST_AsWKT(m)                                                                               |
+-------------------------------------------------------------------------------------------+
| MULTILINESTRING((0 40,0 20,6 30,12 20,12 40),(15 40,15 20,25 20,30 25,30 35,25 40,15 40)) |
| MULTILINESTRING((0 0,1 1,2 2))                                                            |
| MULTILINESTRING((0 40,0 20),(6 30,12 20,12 40))                                           |
+-------------------------------------------------------------------------------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
