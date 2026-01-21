---
description: >-
  The Information Schema REFERENTIAL_CONSTRAINTS table contains metadata about
  foreign keys, including update and delete rules.
---

# Information Schema REFERENTIAL\_CONSTRAINTS Table

The [Information Schema](../) `REFERENTIAL_CONSTRAINTS` table contains information about [foreign keys](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/foreign-keys.md). The single columns are listed in the [KEY\_COLUMN\_USAGE](information-schema-key_column_usage-table.md) table.

It has the following columns:

| Column                      | Description                                                                                                                     |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| CONSTRAINT\_CATALOG         | Always def.                                                                                                                     |
| CONSTRAINT\_SCHEMA          | Database name, together with CONSTRAINT\_NAME identifies the foreign key.                                                       |
| CONSTRAINT\_NAME            | Foreign key name, together with CONSTRAINT\_SCHEMA identifies the foreign key.                                                  |
| UNIQUE\_CONSTRAINT\_CATALOG | Always def.                                                                                                                     |
| UNIQUE\_CONSTRAINT\_SCHEMA  | Database name, together with UNIQUE\_CONSTRAINT\_NAME and REFERENCED\_TABLE\_NAME identifies the referenced key.                |
| UNIQUE\_CONSTRAINT\_NAME    | Referenced key name, together with UNIQUE\_CONSTRAINT\_SCHEMA and REFERENCED\_TABLE\_NAME identifies the referenced key.        |
| MATCH\_OPTION               | Always NONE.                                                                                                                    |
| UPDATE\_RULE                | The Update Rule; one of CASCADE, SET NULL, SET DEFAULT, RESTRICT, NO ACTION.                                                    |
| DELETE\_RULE                | The Delete Rule; one of CASCADE, SET NULL, SET DEFAULT, RESTRICT, NO ACTION.                                                    |
| TABLE\_NAME                 | Table name from the TABLE\_CONSTRAINTS table.                                                                                   |
| REFERENCED\_TABLE\_NAME     | Referenced key table name, together with UNIQUE\_CONSTRAINT\_SCHEMA and UNIQUE\_CONSTRAINT\_NAME identifies the referenced key. |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
