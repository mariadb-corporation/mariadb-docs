---
description: >-
  The setup_objects table configures which database objects (tables, stored
  programs) are instrumented, enabling filtering by schema or name.
---

# Performance Schema setup\_objects Table

## Description

The `setup_objects` table determines whether objects are monitored by the performance schema or not. By default limited to 100 rows, this can be changed by setting the [performance\_schema\_setup\_objects\_size](../performance-schema-system-variables.md#performance_schema_setup_objects_size) system variable when the server starts.

It contains the following columns:

| Column         | Description                                                                                                                      |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| OBJECT\_TYPE   | Type of object to instrument, currently only . Currently, only TABLE', for base table.                                           |
| OBJECT\_SCHEMA | Schema containing the object, either the literal or % for any schema.                                                            |
| OBJECT\_NAME   | Name of the instrumented object, either the literal or % for any object.                                                         |
| ENABLED        | Whether the object's events are instrumented or not. Can be disabled, in which case monitoring is not enabled for those objects. |
| TIMED          | Whether the object's events are timed or not. Can be modified.                                                                   |

When the Performance Schema looks for matches in the `setup_objects`, there may be more than one row matching, with different `ENABLED` and `TIMED` values. It looks for the most specific matches first, that is, it will first look for the specific database and table name combination, then the specific database, only then falling back to a wildcard for both.

Rows can be added or removed from the table, while for existing rows, only the `TIMED` and `ENABLED` columns can be updated. By default, all tables except those in the `performance_schema`, `information_schema` and `mysql` databases are instrumented.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
