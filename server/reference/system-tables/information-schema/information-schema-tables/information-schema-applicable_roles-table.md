---
description: >-
  The Information Schema APPLICABLE_ROLES table shows the role authorizations
  that the current user may use, detailing grantable and default status.
---

# Information Schema APPLICABLE\_ROLES Table

The [Information Schema](../) `APPLICABLE_ROLES` table shows the [role authorizations](../../../../security/user-account-management/roles/) that the current user may use.

It contains the following columns:

<table data-header-hidden="false" data-header-sticky><thead><tr><th>Column</th><th>Description</th></tr></thead><tbody><tr><td>GRANTEE</td><td>Account that the role was granted to.</td></tr><tr><td>ROLE_NAME</td><td>Name of the role.</td></tr><tr><td>IS_GRANTABLE</td><td>Whether the role can be granted or not.</td></tr><tr><td>IS_DEFAULT</td><td>Whether the role is the user's default role or not</td></tr></tbody></table>

The current role is in the [ENABLED\_ROLES](information-schema-enabled_roles-table.md) Information Schema table.

## Example

```sql
SELECT * FROM information_schema.APPLICABLE_ROLES;
+----------------+-------------+--------------+------------+
| GRANTEE        | ROLE_NAME   | IS_GRANTABLE | IS_DEFAULT |
+----------------+-------------+--------------+------------+
| root@localhost | journalist  | YES          | NO         |
| root@localhost | staff       | YES          | NO         |
| root@localhost | dd          | YES          | NO         |
| root@localhost | dog         | YES          | NO         |
+----------------+-------------+--------------+------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
