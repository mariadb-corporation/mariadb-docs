---
description: >-
  Manage roles in MariaDB Server for streamlined user access control. This
  section explains how to create, assign, and manage roles to simplify privilege
  management and enhance security.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
  tags:
    visible: true
---

# Roles

{% columns %}
{% column %}
{% content-ref url="roles_overview.md" %}
[roles\_overview.md](roles_overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Overview of Role-Based Access Control (RBAC) in MariaDB, which simplifies privilege management by allowing permissions to be grouped into roles and assigned to users.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="system-users-roles-and-privileges.md" %}
[system-users-roles-and-privileges.md](system-users-roles-and-privileges.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Details default system users like mariadb.sys and the PUBLIC role, including their creation, purpose, and special management behaviors.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../reference/sql-statements/account-management-sql-statements/create-role.md" %}
[create-role.md](../../../reference/sql-statements/account-management-sql-statements/create-role.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Create new roles to simplify privilege management. Learn how to define a role that can be assigned to multiple users or other roles.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../reference/sql-statements/account-management-sql-statements/drop-role.md" %}
[drop-role.md](../../../reference/sql-statements/account-management-sql-statements/drop-role.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Remove a role from the system. Learn the syntax to delete defined roles and revoke them from any users or roles that currently hold them.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../reference/sql-functions/secondary-functions/information-functions/current_role.md" %}
[current\_role.md](../../../reference/sql-functions/secondary-functions/information-functions/current_role.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Returns the current role. The current role can be set with SET ROLE or SET DEFAULT ROLE.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../reference/sql-statements/account-management-sql-statements/set-role.md" %}
[set-role.md](../../../reference/sql-statements/account-management-sql-statements/set-role.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Sets the current role for the session. Learn how to enable none, or a specific role to change your current privileges dynamically.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../reference/sql-statements/account-management-sql-statements/set-default-role.md" %}
[set-default-role.md](../../../reference/sql-statements/account-management-sql-statements/set-default-role.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Define the default role for a user. Learn how to configure which role is automatically active when a user connects to the server.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../reference/sql-statements/account-management-sql-statements/grant.md" %}
[grant.md](../../../reference/sql-statements/account-management-sql-statements/grant.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete privilege management guide for MariaDB. Complete GRANT syntax for database, table, and column permissions with roles with comprehensive examples and.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../reference/sql-statements/account-management-sql-statements/revoke.md" %}
[revoke.md](../../../reference/sql-statements/account-management-sql-statements/revoke.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Remove privileges or roles. Learn how to withdraw previously granted permissions from users or roles to restrict access and secure the database.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../reference/system-tables/the-mysql-database-tables/mysql-roles_mapping-table.md" %}
[mysql-roles\_mapping-table.md](../../../reference/system-tables/the-mysql-database-tables/mysql-roles_mapping-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The mysql.roles_mapping table manages role assignments, linking user accounts to the roles they have been granted.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../reference/system-tables/information-schema/information-schema-tables/information-schema-applicable_roles-table.md" %}
[information-schema-applicable\_roles-table.md](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-applicable_roles-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The Information Schema APPLICABLE_ROLES table shows the role authorizations that the current user may use, detailing grantable and default status.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../reference/system-tables/information-schema/information-schema-tables/information-schema-enabled_roles-table.md" %}
[information-schema-enabled\_roles-table.md](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-enabled_roles-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The Information Schema ENABLED_ROLES table lists all roles that are currently enabled for the current session, including nested roles.
{% endcolumn %}
{% endcolumns %}
