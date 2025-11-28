---
description: >-
  The Information Schema SCHEMATA table stores information about databases on
  the server, including default character sets and collations.
---

# Information Schema SCHEMATA Table

The [Information Schema](../) `SCHEMATA` table stores information about databases on the server.

It contains the following columns:

| Column                        | Description                                                                                                                                                           |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| CATALOG\_NAME                 | Always def.                                                                                                                                                           |
| SCHEMA\_NAME                  | Database name.                                                                                                                                                        |
| DEFAULT\_CHARACTER\_SET\_NAME | Default [character set](../../../data-types/string-data-types/character-sets/) for the database.                                                                      |
| DEFAULT\_COLLATION\_NAME      | Default [collation](../../../data-types/string-data-types/character-sets/).                                                                                           |
| SQL\_PATH                     | Always NULL.                                                                                                                                                          |
| SCHEMA\_COMMENT               | Database comment. From [MariaDB 10.5.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1050-release-notes). |

## Example

{% tabs %}
{% tab title="Current" %}
```sql
SELECT * FROM INFORMATION_SCHEMA.SCHEMATA\G
...
*************************** 2. row ***************************
              CATALOG_NAME: def
               SCHEMA_NAME: presentations
DEFAULT_CHARACTER_SET_NAME: latin1
    DEFAULT_COLLATION_NAME: latin1_swedish_ci
                  SQL_PATH: NULL
            SCHEMA_COMMENT: Presentations for conferences
...
```
{% endtab %}

{% tab title="< 10.5.0" %}
```sql
SELECT * FROM INFORMATION_SCHEMA.SCHEMATA\G
*************************** 1. row ***************************
              CATALOG_NAME: def
               SCHEMA_NAME: information_schema
DEFAULT_CHARACTER_SET_NAME: utf8
    DEFAULT_COLLATION_NAME: utf8_general_ci
                  SQL_PATH: NULL
*************************** 2. row ***************************
              CATALOG_NAME: def
               SCHEMA_NAME: mysql
DEFAULT_CHARACTER_SET_NAME: latin1
    DEFAULT_COLLATION_NAME: latin1_swedish_ci
                  SQL_PATH: NULL
*************************** 3. row ***************************
              CATALOG_NAME: def
               SCHEMA_NAME: performance_schema
DEFAULT_CHARACTER_SET_NAME: utf8
    DEFAULT_COLLATION_NAME: utf8_general_ci
                  SQL_PATH: NULL
*************************** 4. row ***************************
              CATALOG_NAME: def
               SCHEMA_NAME: test
DEFAULT_CHARACTER_SET_NAME: latin1
    DEFAULT_COLLATION_NAME: latin1_swedish_ci
                  SQL_PATH: NULL
...
```
{% endtab %}
{% endtabs %}

## See Also

* [CREATE DATABASE](../../../sql-statements/data-definition/create/create-database.md)
* [ALTER DATABASE](../../../sql-statements/data-definition/alter/alter-database.md)
* [DROP DATABASE](../../../sql-statements/data-definition/drop/drop-database.md)
* [SHOW CREATE DATABASE](../../../sql-statements/administrative-sql-statements/show/show-create-database.md)
* [SHOW DATABASES](../../../sql-statements/administrative-sql-statements/show/show-databases.md)
* [Character Sets and Collations](../../../data-types/string-data-types/character-sets/supported-character-sets-and-collations.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
