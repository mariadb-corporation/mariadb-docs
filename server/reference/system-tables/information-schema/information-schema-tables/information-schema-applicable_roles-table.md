---
description: >-
  The Information Schema APPLICABLE_ROLES table shows the role authorizations
  that the current user may use, detailing grantable and default status.
---

# Information Schema APPLICABLE\_ROLES Table

The [Information Schema](../) `APPLICABLE_ROLES` table shows the [role authorizations](../../../../security/user-account-management/roles/) that the current user may use.

It contains the following columns:

| Column        | Description                                        |
| ------------- | -------------------------------------------------- |
| GRANTEE       | Account that the role was granted to.              |
| ROLE\_NAME    | Name of the role.                                  |
| IS\_GRANTABLE | Whether the role can be granted or not.            |
| IS\_DEFAULT   | Whether the role is the user's default role or not |

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
