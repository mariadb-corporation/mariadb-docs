---
description: >-
  The Information Schema GEOMETRY_COLUMNS table describes the geometry columns
  in tables, providing details on spatial reference systems and geometry types.
---

# Information Schema GEOMETRY\_COLUMNS Table

## Description

The [Information Schema](../) `GEOMETRY_COLUMNS` table provides support for Spatial Reference systems for GIS data.

It contains the following columns:

| Column              | Type         | Null | Description                                                                                                                                                                                     |
| ------------------- | ------------ | ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| F\_TABLE\_CATALOG   | VARCHAR(512) | NO   | Together with F\_TABLE\_SCHEMA and F\_TABLE\_NAME, the fully qualified name of the featured table containing the geometry column.                                                               |
| F\_TABLE\_SCHEMA    | VARCHAR(64)  | NO   | Together with F\_TABLE\_CATALOG and F\_TABLE\_NAME, the fully qualified name of the featured table containing the geometry column.                                                              |
| F\_TABLE\_NAME      | VARCHAR(64)  | NO   | Together with F\_TABLE\_CATALOG and F\_TABLE\_SCHEMA, the fully qualified name of the featured table containing the geometry column.                                                            |
| F\_GEOMETRY\_COLUMN | VARCHAR(64)  | NO   | Name of the column in the featured table that is the geometry golumn.                                                                                                                           |
| G\_TABLE\_CATALOG   | VARCHAR(512) | NO   |                                                                                                                                                                                                 |
| G\_TABLE\_SCHEMA    | VARCHAR(64)  | NO   | Database name of the table implementing the geometry column.                                                                                                                                    |
| G\_TABLE\_NAME      | VARCHAR(64)  | NO   | Table name that is implementing the geometry column.                                                                                                                                            |
| G\_GEOMETRY\_COLUMN | VARCHAR(64)  | NO   |                                                                                                                                                                                                 |
| STORAGE\_TYPE       | TINYINT(2)   | NO   | Binary geometry implementation. Always 1 in MariaDB.                                                                                                                                            |
| GEOMETRY\_TYPE      | INT(7)       | NO   | Integer reflecting the type of geometry stored in this column (see table below).                                                                                                                |
| COORD\_DIMENSION    | TINYINT(2)   | NO   | Number of dimensions in the spatial reference system. Always 2 in MariaDB.                                                                                                                      |
| MAX\_PPR            | TINYINT(2)   | NO   | Always 0 in MariaDB.                                                                                                                                                                            |
| SRID                | SMALLINT(5)  | NO   | ID of the Spatial Reference System used for the coordinate geometry in this table. It is a foreign key reference to the [SPATIAL\_REF\_SYS table](information-schema-spatial_ref_sys-table.md). |

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
