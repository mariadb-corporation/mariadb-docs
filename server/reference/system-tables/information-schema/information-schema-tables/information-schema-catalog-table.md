---
description: >-
  The Information Schema CATALOG table stores information about catalogs on the
  server, including default character sets and collations.
---

# Information Schema CATALOG Table

{% hint style="info" %}
This table is available as of MariaDB 12.0.
{% endhint %}

The [Information Schema](../) `CATALOG` table stores information about [catalogs](../../../../security/user-account-management/catalogs/) on the server.

It contains the following columns:

| Column                        | Description                                                                                      |
| ----------------------------- | ------------------------------------------------------------------------------------------------ |
| CATALOG\_NAME                 | Catalog name.                                                                                    |
| DEFAULT\_CHARACTER\_SET\_NAME | Default [character set](../../../data-types/string-data-types/character-sets/) for the database. |
| DEFAULT\_COLLATION\_NAME      | Default [collation](../../../data-types/string-data-types/character-sets/).                      |
| SCHEMA\_COMMENT               | Catalog comment                                                                                  |

## Example

```sql
MariaDB [def.test]> SELECT * FROM INFORMATION_SCHEMA.CATALOGS\G
*************************** 1. row ***************************
              CATALOG_NAME: c1
DEFAULT_CHARACTER_SET_NAME: latin1
    DEFAULT_COLLATION_NAME: latin1_swedish_ci
           CATALOG_COMMENT: This is catalog c1
*************************** 2. row ***************************
              CATALOG_NAME: cat2
DEFAULT_CHARACTER_SET_NAME: latin1
    DEFAULT_COLLATION_NAME: latin1_swedish_ci
           CATALOG_COMMENT: 
*************************** 3. row ***************************
              CATALOG_NAME: def
DEFAULT_CHARACTER_SET_NAME: latin1
    DEFAULT_COLLATION_NAME: latin1_swedish_ci
           CATALOG_COMMENT: default catalog
...
```

## See Also

* [SHOW CATALOGS](../../../../security/user-account-management/catalogs/show-catalogs.md)
* [SHOW CREATE CATALOG](../../../../security/user-account-management/catalogs/show-create-catalog.md)
* [CREATE CATALOG](../../../../security/user-account-management/catalogs/create-catalog.md)
* [DROP CATALOG](../../../../security/user-account-management/catalogs/drop-catalog.md)
* [Character Sets and Collations](../../../data-types/string-data-types/character-sets/supported-character-sets-and-collations.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
