---
description: >-
  The Information Schema SPATIAL_REF_SYS table stores information about
  available Spatial Reference Systems (SRS) for geometry data.
---

# Information Schema SPATIAL\_REF\_SYS Table

## Description

The [Information Schema](../) `SPATIAL_REF_SYS` table stores information on each spatial reference system used in the database.

It contains the following columns:

| Column     | Type          | Null | Description                                                                                                               |
| ---------- | ------------- | ---- | ------------------------------------------------------------------------------------------------------------------------- |
| SRID       | smallint(5)   | NO   | An integer value that uniquely identifies each Spatial Reference System within a database.                                |
| AUTH\_NAME | varchar(512)  | NO   | The name of the standard or standards body that is being cited for this reference system.                                 |
| AUTH\_SRID | smallint(5)   | NO   | The numeric ID of the coordinate system in the above authority's catalog.                                                 |
| SRTEXT     | varchar(2048) | NO   | The [Well-known Text Representation](../../../sql-statements/geometry-constructors/wkt/) of the Spatial Reference System. |

Note: See [MDEV-7540](https://jira.mariadb.org/browse/MDEV-7540).

## See Aso

* [information\_schema.GEOMETRY\_COLUMNS](information-schema-geometry_columns-table.md) table.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
