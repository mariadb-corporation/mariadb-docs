---
description: >-
  The Information Schema GEOMETRY_COLUMNS table describes the geometry columns
  in tables, providing details on spatial reference systems and geometry types.
---

# Information Schema GEOMETRY\_COLUMNS Table

## Description

The [Information Schema](../) `GEOMETRY_COLUMNS` table provides support for Spatial Reference systems for GIS data.

It contains the following columns:

<table data-header-hidden="false" data-header-sticky><thead><tr><th>Column</th><th>Type</th><th>Null</th><th>Description</th></tr></thead><tbody><tr><td>F_TABLE_CATALOG</td><td>VARCHAR(512)</td><td>NO</td><td>Together with F_TABLE_SCHEMA and F_TABLE_NAME, the fully qualified name of the featured table containing the geometry column.</td></tr><tr><td>F_TABLE_SCHEMA</td><td>VARCHAR(64)</td><td>NO</td><td>Together with F_TABLE_CATALOG and F_TABLE_NAME, the fully qualified name of the featured table containing the geometry column.</td></tr><tr><td>F_TABLE_NAME</td><td>VARCHAR(64)</td><td>NO</td><td>Together with F_TABLE_CATALOG and F_TABLE_SCHEMA, the fully qualified name of the featured table containing the geometry column.</td></tr><tr><td>F_GEOMETRY_COLUMN</td><td>VARCHAR(64)</td><td>NO</td><td>Name of the column in the featured table that is the geometry golumn.</td></tr><tr><td>G_TABLE_CATALOG</td><td>VARCHAR(512)</td><td>NO</td><td></td></tr><tr><td>G_TABLE_SCHEMA</td><td>VARCHAR(64)</td><td>NO</td><td>Database name of the table implementing the geometry column.</td></tr><tr><td>G_TABLE_NAME</td><td>VARCHAR(64)</td><td>NO</td><td>Table name that is implementing the geometry column.</td></tr><tr><td>G_GEOMETRY_COLUMN</td><td>VARCHAR(64)</td><td>NO</td><td></td></tr><tr><td>STORAGE_TYPE</td><td>TINYINT(2)</td><td>NO</td><td>Binary geometry implementation. Always 1 in MariaDB.</td></tr><tr><td>GEOMETRY_TYPE</td><td>INT(7)</td><td>NO</td><td>Integer reflecting the type of geometry stored in this column (see table below).</td></tr><tr><td>COORD_DIMENSION</td><td>TINYINT(2)</td><td>NO</td><td>Number of dimensions in the spatial reference system. Always 2 in MariaDB.</td></tr><tr><td>MAX_PPR</td><td>TINYINT(2)</td><td>NO</td><td>Always 0 in MariaDB.</td></tr><tr><td>SRID</td><td>SMALLINT(5)</td><td>NO</td><td>ID of the Spatial Reference System used for the coordinate geometry in this table. It is a foreign key reference to the <a href="information-schema-spatial_ref_sys-table.md">SPATIAL_REF_SYS table</a>.</td></tr></tbody></table>

## Storage\_type

The integers in the `storage_type` field match the geometry types as follows:

| Integer | Type            |
| ------- | --------------- |
| 0       | GEOMETRY        |
| 1       | POINT           |
| 3       | LINESTRING      |
| 5       | POLYGON         |
| 7       | MULTIPOINT      |
| 9       | MULTILINESTRING |
| 11      | MULTIPOLYGON    |

## Example

```sql
CREATE TABLE g1(g GEOMETRY(9,4) REF_SYSTEM_ID=101);

SELECT * FROM information_schema.GEOMETRY_COLUMNS\G
*************************** 1. row ***************************
  F_TABLE_CATALOG: def
   F_TABLE_SCHEMA: test
     F_TABLE_NAME: g1
F_GEOMETRY_COLUMN: 
  G_TABLE_CATALOG: def
   G_TABLE_SCHEMA: test
     G_TABLE_NAME: g1
G_GEOMETRY_COLUMN: g
     STORAGE_TYPE: 1
    GEOMETRY_TYPE: 0
  COORD_DIMENSION: 2
          MAX_PPR: 0
             SRID: 101
```

## See also

* The [SPATIAL\_REF\_SYS](information-schema-spatial_ref_sys-table.md) table.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
