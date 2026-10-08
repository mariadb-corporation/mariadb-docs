---
description: >-
  The mysql.columns_priv table records column-level privileges granted to users,
  detailing specific access rights for individual columns.
---

# mysql.columns\_priv Table

The `mysql.columns_priv` table contains information about column-level privileges. The table can be queried and although it is possible to directly update it, it is best to use [GRANT](../../sql-statements/account-management-sql-statements/grant.md) for setting privileges.

Note that the MariaDB privileges occur at many levels. A user may be granted a privilege at the column level, but may still not have permission on a table level, for example. See [privileges](../../sql-statements/account-management-sql-statements/grant.md) for a more complete view of the MariaDB privilege system.

The [INFORMATION\_SCHEMA.COLUMN\_PRIVILEGES](../information-schema/information-schema-tables/information-schema-column_privileges-table.md) table derives its contents from `mysql.columns_priv`.

This table uses the [Aria](../../../server-usage/storage-engines/aria/) storage engine.

The `mysql.columns_priv` table contains the following fields:

| Field        | Type                                            | Null | Key | Default            | Description                                                                                                                                 |
| ------------ | ----------------------------------------------- | ---- | --- | ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Host         | char(60)                                        | NO   | PRI |                    | Host (together with User, Db , Table\_name andColumn\_name makes up the unique identifier for this record.                                  |
| Db           | char(64)                                        | NO   | PRI |                    | Database name (together with User, Host , Table\_name andColumn\_name makes up the unique identifier for this record.                       |
| User         | char(80)                                        | NO   | PRI |                    | User (together with Host, Db , Table\_name andColumn\_name makes up the unique identifier for this record.                                  |
| Table\_name  | char(64)                                        | NO   | PRI |                    | Table name (together with User, Db , Host andColumn\_name makes up the unique identifier for this record.                                   |
| Column\_name | char(64)                                        | NO   | PRI |                    | Column name (together with User, Db , Table\_name andHost makes up the unique identifier for this record.                                   |
| Timestamp    | timestamp                                       | NO   |     | CURRENT\_TIMESTAMP |                                                                                                                                             |
| Column\_priv | set('Select', 'Insert', 'Update', 'References') | NO   |     |                    | The privilege type. See [Column Privileges](../../sql-statements/account-management-sql-statements/grant.md#column-privileges) for details. |

The [Acl\_column\_grants](../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#acl_column_grants) status variable indicates how many rows the `mysql.columns_priv` table contains.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
