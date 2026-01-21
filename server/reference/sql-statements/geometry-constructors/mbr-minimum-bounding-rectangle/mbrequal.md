---
description: >-
  Check if two MBRs are identical. Returns 1 if the Minimum Bounding Rectangles
  of both geometries share the exact same coordinates.
---

# MBREqual

## Syntax

```sql
MBREqual(g1,g2)
MBREquals(g1,g2)
```

## Description

Returns 1 or 0 to indicate whether the [Minimum Bounding Rectangles](mbr-definition.md) of the two geometries g1 and g2 are the same.

`MBREquals` is a synonym.

## Examples

```sql
SET @g1=GEOMFROMTEXT('LINESTRING(0 0, 1 2)');
SET @g2=GEOMFROMTEXT('POLYGON((0 0, 0 2, 1 2, 1 0, 0 0))');
SELECT MbrEqual(@g1,@g2);
+-------------------+
| MbrEqual(@g1,@g2) |
+-------------------+
|                 1 |
+-------------------+

SET @g1=GEOMFROMTEXT('LINESTRING(0 0, 1 3)');
SET @g2=GEOMFROMTEXT('POLYGON((0 0, 0 2, 1 4, 1 0, 0 0))');
SELECT MbrEqual(@g1,@g2);
+-------------------+
| MbrEqual(@g1,@g2) |
+-------------------+
|                 0 |
+-------------------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
