---
description: >-
  The Information Schema TABLE_CONSTRAINTS table describes constraints on
  tables, such as PRIMARY KEY, UNIQUE, and FOREIGN KEY constraints.
---

# Information Schema TABLE\_CONSTRAINTS Table

The [Information Schema](../) `TABLE_CONSTRAINTS` table contains information about tables that have [constraints](../../../sql-statements/data-definition/constraint.md).

It has the following columns:

| Column              | Description                                                           |
| ------------------- | --------------------------------------------------------------------- |
| CONSTRAINT\_CATALOG | Always def.                                                           |
| CONSTRAINT\_SCHEMA  | Database name containing the constraint.                              |
| CONSTRAINT\_NAME    | Constraint name.                                                      |
| TABLE\_SCHEMA       | Database name.                                                        |
| TABLE\_NAME         | Table name.                                                           |
| CONSTRAINT\_TYPE    | Type of constraint; one of UNIQUE, PRIMARY KEY, FOREIGN KEY or CHECK. |

The [REFERENTIAL\_CONSTRAINTS](information-schema-referential_constraints-table.md) table has more information about foreign keys.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
