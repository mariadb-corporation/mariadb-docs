---
description: >-
  Reference for the SHOW CATALOGS statement, which lists all available catalogs
  on the server.
---

# SHOW CATALOGS

{% include "../../../.gitbook/includes/catalogs.md" %}

## Syntax

```bnf
SHOW CATALOGS
    [LIKE 'pattern' | WHERE expr]
```

## Description

`SHOW CATALOGS` lists the [catalogs](./) on the MariaDB server host.\
The `LIKE` clause, if present on its own, indicates which catalog names to match. The `WHERE` and `LIKE` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](../../../reference/sql-statements/administrative-sql-statements/show/extended-show.md).

You see only use `SHOW CATALOGS` have the [CATALOG privilege](../../../reference/sql-statements/account-management-sql-statements/grant.md). Only users of the 'def' schema can have this privilege.

If the server was started with the [--skip-show-database](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#skip_show_database) option, you cannot use this statement unless you have the [SHOW DATABASES privilege](../../../reference/sql-statements/account-management-sql-statements/grant.md#show-databases).

The list of results returned by `SHOW CATALOGS` is based on directories in the data directory, which is how MariaDB implements catalogs. It only list directories that have a `mysql` directory.

The [Information Schema Catalogs table](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-catalog-table.md) also contains catalog information.

## Examples

```
+---------+--------------------+
| Catalog | Comment            |
+---------+--------------------+
| c1      | This is catalog c1 |
| cat2    |                    |
| def     | default catalog    |
+---------+--------------------+
```

```sql
SHOW CATALOGS LIKE 'c%';
+--------------+--------------------+
| Catalog (c%) | Comment            |
+--------------+--------------------+
| c1           | This is catalog c1 |
| cat2         |                    |
+--------------+--------------------+
```

## See Also

* [CREATE CATALOG](create-catalog.md)
* [Character Sets and Collations](../../../reference/data-types/string-data-types/character-sets/supported-character-sets-and-collations.md)
* [Information Schema CATALOG Table](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-catalog-table.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
