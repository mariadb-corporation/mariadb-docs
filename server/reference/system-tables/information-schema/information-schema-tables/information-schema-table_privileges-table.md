---
description: >-
  The Information Schema TABLE_PRIVILEGES table lists privileges granted
  specifically at the table level.
---

# Information Schema TABLE\_PRIVILEGES Table

The [Information Schema](../) `TABLE_PRIVILEGES` table contains table privilege information derived from the [mysql.tables\_priv](../../the-mysql-database-tables/mysql-tables_priv-table.md) grant table.

It has the following columns:

| Column          | Description                                                                                                                                                |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GRANTEE         | In the format user\_name@host\_name.                                                                                                                       |
| TABLE\_CATALOG  | Always def.                                                                                                                                                |
| TABLE\_SCHEMA   | Database name.                                                                                                                                             |
| TABLE\_NAME     | Table name.                                                                                                                                                |
| PRIVILEGE\_TYPE | One of SELECT, INSERT, UPDATE, REFERENCES, ALTER, INDEX, DROP or CREATE VIEW.                                                                              |
| IS\_GRANTABLE   | Whether the user has the [GRANT OPTION](../../../sql-statements/account-management-sql-statements/grant.md#the-grant-option-privilege) for this privilege. |

Similar information can be accessed with the [SHOW GRANTS](../../../sql-statements/administrative-sql-statements/show/show-grants.md) statement. See the [GRANT](../../../sql-statements/account-management-sql-statements/grant.md) article for more about privileges.

The table only shows privileges granted on the table level. This differs from the Sys Schema [privileges\_by\_table\_by\_level view](../../sys-schema/sys-schema-views/privileges_by_table_by_level-sys-schema-view.md), which shows all privileges, broken down by table.

For a description of the privileges that are shown in this table, see [table privileges](../../../sql-statements/account-management-sql-statements/grant.md#table-privileges).

## See Also

* [sys.privileges\_by\_table\_by\_level](../../sys-schema/sys-schema-views/privileges_by_table_by_level-sys-schema-view.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
