---
description: >-
  The mysql.roles_mapping table manages role assignments, linking user accounts
  to the roles they have been granted.
---

# mysql.roles\_mapping Table

{% include "../../../.gitbook/includes/system-tables-warning.md" %}

The `mysql.roles_mapping` table contains information about mariaDB [roles](../../../security/user-account-management/roles/).

This table uses the [Aria](../../../server-usage/storage-engines/aria/) storage engine.

The `mysql.roles_mapping` table contains the following fields:

| Field         | Type          | Null | Key | Default | Description                                                                                                                                       |
| ------------- | ------------- | ---- | --- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Host          | char(60)      | NO   | PRI |         | Host (together with User and Role makes up the unique identifier for this record.                                                                 |
| User          | char(80)      | NO   | PRI |         | User (together with Host and Role makes up the unique identifier for this record.                                                                 |
| Role          | char(80)      | NO   | PRI |         | Role (together with Host and User makes up the unique identifier for this record.                                                                 |
| Admin\_option | enum('N','Y') | NO   |     | N       | Whether the role can be granted (see the [CREATE ROLE](../../sql-statements/account-management-sql-statements/create-role.md) WITH ADMIN clause). |

The [Acl\_role\_grants](../../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#acl_role_grants) status variable indicates how many rows the `mysql.roles_mapping` table contains.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
