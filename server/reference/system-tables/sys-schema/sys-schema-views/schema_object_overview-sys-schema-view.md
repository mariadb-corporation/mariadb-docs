---
description: >-
  The schema_object_overview view provides a count of different database objects
  (such as tables, views, and routines) within each schema on the server.
---

# schema\_object\_overview Sys Schema View

{% include "../../../../.gitbook/includes/sys-schema-views-are-availa....md" %}

## Description

A count of the number of objects within each schema, sorted by schema and object.

Contains the following columns:

| Column       | Description                    |
| ------------ | ------------------------------ |
| db           | Schema name                    |
| object\_type | Object name                    |
| count        | Count of the number of objects |

## Example

```sql
SELECT * FROM sys.schema_object_overview;
+--------------------+---------------+-------+
| db                 | object_type   | count |
+--------------------+---------------+-------+
| information_schema | SYSTEM VIEW   |    79 |
| mysql              | BASE TABLE    |    30 |
| mysql              | INDEX (BTREE) |    76 |
| mysql              | PROCEDURE     |     2 |
| mysql              | VIEW          |     1 |
| performance_schema | BASE TABLE    |    81 |
| sys                | BASE TABLE    |     1 |
| sys                | FUNCTION      |    22 |
| sys                | INDEX (BTREE) |     1 |
| sys                | PROCEDURE     |    26 |
| sys                | VIEW          |   100 |
+--------------------+---------------+-------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
