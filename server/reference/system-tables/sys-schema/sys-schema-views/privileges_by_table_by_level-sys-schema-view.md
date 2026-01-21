---
description: >-
  The privileges_by_table_by_level view lists granted privileges broken down by
  table and the level (Global, Schema, or Table) at which they were granted.
---

# privileges\_by\_table\_by\_level Sys Schema View

{% include "../../../../.gitbook/includes/sys-schema-views-are-availa....md" %}

{% hint style="info" %}
This view is available from MariaDB 11.4.
{% endhint %}

## Description

Shows granted privileges broken down by table on which they allow access and level on which they were granted.

For example, if a user `x` has `SELECT` privilege granted `ON db.*`, this view will list all tables in the `db` schema with the user `x` having `SELECT` privilege on them. This is different from [INFORMATION\_SCHEMA.TABLE\_PRIVILEGES](../../information-schema/information-schema-tables/information-schema-table_privileges-table.md), which only lists privileges granted on the table level.

| Column        | Description                                                                                                                                                                                                  |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| TABLE\_SCHEMA | Database name.                                                                                                                                                                                               |
| TABLE\_NAME   | Table name.                                                                                                                                                                                                  |
| GRANTEE       | [Account name](../../../sql-statements/account-management-sql-statements/create-user.md#account-names) that was [granted](../../../sql-statements/account-management-sql-statements/grant.md) the privilege. |
| PRIVILEGE     | [Privilege](../../../sql-statements/account-management-sql-statements/grant.md), such as SELECT or DROP.                                                                                                     |
| LEVEL         | [Privilege level](../../../sql-statements/account-management-sql-statements/grant.md), such as GLOBAL or SCHEMA.                                                                                             |

## Example

```sql
SELECT * FROM sys.privileges_by_table_by_level;
+--------------+------------+---------------------------+----------------+--------+
| TABLE_SCHEMA | TABLE_NAME | GRANTEE                   | PRIVILEGE      | LEVEL  |
+--------------+------------+---------------------------+----------------+--------+
...
| test         | t2         | 'root'@'localhost'        | SELECT         | GLOBAL |
| test         | t1         | 'root'@'localhost'        | SELECT         | GLOBAL |
| test         | t3         | 'root'@'localhost'        | SELECT         | GLOBAL |
| test         | t2         | 'root'@'localhost'        | INSERT         | GLOBAL |
| test         | t1         | 'root'@'localhost'        | INSERT         | GLOBAL |
| test         | t3         | 'root'@'localhost'        | INSERT         | GLOBAL |
| test         | t2         | 'root'@'localhost'        | UPDATE         | GLOBAL |
| test         | t1         | 'root'@'localhost'        | UPDATE         | GLOBAL |
| test         | t3         | 'root'@'localhost'        | UPDATE         | GLOBAL |
| test         | t2         | 'root'@'localhost'        | DELETE         | GLOBAL |
| test         | t1         | 'root'@'localhost'        | DELETE         | GLOBAL |
| test         | t3         | 'root'@'localhost'        | DELETE         | GLOBAL |
| test         | t2         | 'root'@'localhost'        | CREATE         | GLOBAL |
| test         | t1         | 'root'@'localhost'        | CREATE         | GLOBAL |
| test         | t3         | 'root'@'localhost'        | CREATE         | GLOBAL |
| test         | t2         | 'root'@'localhost'        | DROP           | GLOBAL |
| test         | t1         | 'root'@'localhost'        | DROP           | GLOBAL |
| test         | t3         | 'root'@'localhost'        | DROP           | GLOBAL |
| test         | t2         | 'root'@'localhost'        | REFERENCES     | GLOBAL |
| test         | t1         | 'root'@'localhost'        | REFERENCES     | GLOBAL |
| test         | t3         | 'root'@'localhost'        | REFERENCES     | GLOBAL |
| test         | t2         | 'root'@'localhost'        | INDEX          | GLOBAL |
| test         | t1         | 'root'@'localhost'        | INDEX          | GLOBAL |
| test         | t3         | 'root'@'localhost'        | INDEX          | GLOBAL |
| test         | t2         | 'root'@'localhost'        | ALTER          | GLOBAL |
| test         | t1         | 'root'@'localhost'        | ALTER          | GLOBAL |
| test         | t3         | 'root'@'localhost'        | ALTER          | GLOBAL |
| test         | t2         | 'root'@'localhost'        | SHOW VIEW      | GLOBAL |
| test         | t1         | 'root'@'localhost'        | SHOW VIEW      | GLOBAL |
| test         | t3         | 'root'@'localhost'        | SHOW VIEW      | GLOBAL |
| test         | t2         | 'root'@'localhost'        | TRIGGER        | GLOBAL |
| test         | t1         | 'root'@'localhost'        | TRIGGER        | GLOBAL |
| test         | t3         | 'root'@'localhost'        | TRIGGER        | GLOBAL |
| test         | t2         | 'root'@'localhost'        | DELETE HISTORY | GLOBAL |
| test         | t1         | 'root'@'localhost'        | DELETE HISTORY | GLOBAL |
| test         | t3         | 'root'@'localhost'        | DELETE HISTORY | GLOBAL |
| test         | t2         | 'PUBLIC'@''               | SELECT         | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | SELECT         | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | SELECT         | SCHEMA |
| test         | t2         | 'PUBLIC'@''               | INSERT         | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | INSERT         | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | INSERT         | SCHEMA |
| test         | t2         | 'PUBLIC'@''               | UPDATE         | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | UPDATE         | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | UPDATE         | SCHEMA |
| test         | t2         | 'PUBLIC'@''               | DELETE         | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | DELETE         | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | DELETE         | SCHEMA |
| test         | t2         | 'PUBLIC'@''               | CREATE         | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | CREATE         | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | CREATE         | SCHEMA |
| test         | t2         | 'PUBLIC'@''               | DROP           | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | DROP           | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | DROP           | SCHEMA |
| test         | t2         | 'PUBLIC'@''               | REFERENCES     | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | REFERENCES     | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | REFERENCES     | SCHEMA |
| test         | t2         | 'PUBLIC'@''               | INDEX          | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | INDEX          | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | INDEX          | SCHEMA |
| test         | t2         | 'PUBLIC'@''               | ALTER          | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | ALTER          | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | ALTER          | SCHEMA |
| test         | t2         | 'PUBLIC'@''               | SHOW VIEW      | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | SHOW VIEW      | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | SHOW VIEW      | SCHEMA |
| test         | t2         | 'PUBLIC'@''               | TRIGGER        | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | TRIGGER        | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | TRIGGER        | SCHEMA |
| test         | t2         | 'PUBLIC'@''               | DELETE HISTORY | SCHEMA |
| test         | t1         | 'PUBLIC'@''               | DELETE HISTORY | SCHEMA |
| test         | t3         | 'PUBLIC'@''               | DELETE HISTORY | SCHEMA |
+--------------+------------+---------------------------+----------------+--------+
```

## See Also

* [GRANT](../../../sql-statements/account-management-sql-statements/grant.md) (description of the privileges and how to grant them)
* [INFORMATION\_SCHEMA.TABLE\_PRIVILEGES](../../information-schema/information-schema-tables/information-schema-table_privileges-table.md)
* [MDEV-24486](https://jira.mariadb.org/browse/MDEV-24486)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
