---
description: >-
  List stored packages. View metadata about the interface part of
  Oracle-compatible packages in the database.
---

# SHOW PACKAGE STATUS

## Syntax

```sql
SHOW PACKAGE STATUS
    [LIKE 'pattern' | WHERE expr]
```

## Description

The `SHOW PACKAGE STATUS` statement returns characteristics of stored package specifications, such as the database, name, type, creator, creation and modification dates, and character set information. A similar statement, [SHOW PACKAGE BODY STATUS](show-package-body-status.md), displays information about stored package bodies (i.e. implementations).

The `LIKE` clause, if present, indicates which package names to match. The `WHERE` and `LIKE` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](extended-show.md).

The [ROUTINES table](../../../system-tables/information-schema/information-schema-tables/information-schema-routines-table.md) in the INFORMATION\_SCHEMA database contains more detailed information.

## Examples

```sql
SHOW PACKAGE STATUS LIKE 'pkg1'\G
*************************** 1. row ***************************
                  Db: test
                Name: pkg1
                Type: PACKAGE
             Definer: root@localhost
            Modified: 2018-02-27 14:38:15
             Created: 2018-02-27 14:38:15
       Security_type: DEFINER
             Comment: This is my first package
character_set_client: utf8
collation_connection: utf8_general_ci
  Database Collation: latin1_swedish_ci
```

## See Also

* [SHOW PACKAGE BODY](show-package-body-status.md)
* [SHOW CREATE PACKAGE](show-create-package.md)
* [CREATE PACKAGE](../../data-definition/create/create-package.md)
* [DROP PACKAGE](../../data-definition/drop/drop-package.md)
* [Oracle SQL\_MODE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
