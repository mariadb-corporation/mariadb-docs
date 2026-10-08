---
description: >-
  GridGain 9 uses a flat role-based access control (RBAC) model that grants
  privileges to roles and assigns roles to users to manage cluster access.
---

# Role-Based Authorization

{% hint style="info" %}
This feature is only available as a part of GridGain 9 Enterprise and Ultimate editions.
{% endhint %}

GridGain 9 uses a flat Role-Based Access Control (RBAC) model for managing access to cluster resources.

## How RBAC Works

In GridGain 9, access control follows the following rules:

- Users cannot receive privileges directly;
- Instead, privileges are granted to roles;
- Roles are then assigned to users;
- Users inherit all privileges from their assigned roles.

This model ensures consistent permission management across the cluster.

### Object Ownership

GridGain 9 does not implement object ownership. No user "owns" a table, schema, or any other resource.

If required, you can provide ownership-like capabilities by fine-tuning the privileges:

1. Create a role with management privileges for the specific object;
2. Add `GRANT_PRIVILEGE` permission to allow privilege delegation;
3. Assign the role to the user.

### Object Hierarchy

Object privileges have the following hierarchy:

```
ALL
  └── CLUSTER
       └── Schema
            ├── Table
            ├── View
            ├── Index
            └── Sequence
```

When you grant a privilege on a parent object, it automatically applies to all child objects. For example, `SELECT_FROM_TABLE` privilege on schema `PUBLIC` allows user to execute `SELECT` statement on all tables in that schema. This includes both existing tables and tables that will be created in the future, as permissions are checked when the user attempts access.

{% hint style="info" %}
When no object is specified for singleton actions like `READ_CLUSTER_CONFIG`, the default object is `CLUSTER`.
{% endhint %}

## Object Name Resolution

When specifying objects in GRANT statements, the following syntax rules apply:

- No dot in the name means the schema, for example: `PUBLIC`;
- One dot means the table in the schema, for example: `PUBLIC.CUSTOMERS`

{% hint style="warning" %}
By default, all names are in upper case. Use double quotes for mixed-case or special characters, for example: `PUBLIC."Orders"`
{% endhint %}

## User Configuration

Users and their roles are configured by using CLI or SQL. You can see the full list of CLI commands in the [GridGain CLI Tool](../reference/cli-tool.md) section, and SQL commands in [DDL reference](../reference/sql/ddl.md).

In most cases, the workflow would involve creating a role, assigning it some privileges and then assigning them to a user.

### CLI Example

The example below shows how you can configure role-based access

- Create a new user:

  ```bash
  user create --password=myPassword myUser
  ```

- Create a new role on the cluster:

  ```bash
  role create sampleRole
  ```

- Grant a new privilege to the role. In this case, we will allow users with this role to create tables, but you can see the full list of roles in the [User Permissions and Roles](user-permissions-and-roles.md) section.

  ```bash
  role privilege grant --action=CREATE_TABLE --on=PUBLIC --to=sampleRole
  ```

- The role now has the required permission, you can assign it to the user:

  ```bash
  user role assign --role=sampleRole --to=myUser
  ```

The `myUser` user will have the permissions to use the `CREATE TABLE` SQL statement.

```bash
connect http://127.0.0.1:10300 --username myUser --password myPassword
sql "CREATE TABLE IF NOT EXISTS PUBLIC.Person (id int primary key,  city varchar,  name varchar,  age int,  company varchar)"
```

## SQL Example

This example demonstrates setting up access control for a typical organization with different departments and access requirements.

```sql
-- Create a new role
CREATE ROLE SAMPLEROLE;

-- Grant table creation privileges on the PUBLIC schema to the new role
GRANT PRIVILEGES CREATE_TABLE ON PUBLIC TO SAMPLEROLE;

-- Create a new user for this example
CREATE USER MYUSER IDENTIFIED WITH plain_password BY 'pass';

-- Assign SAMPLEROLE to MYUSER
GRANT SAMPLEROLE TO MYUSER;

-- Display all privileges granted to MYUSER
SHOW GRANTS FOR MYUSER;
```
