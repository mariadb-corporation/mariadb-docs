# System\`s Users, Roles, and Privileges

{% hint style="info" %}
**Important:** The `PUBLIC` role is created implicitly by `GRANT` statements and its creation is not logged, distinguishing it from standard system principals.
{% endhint %}

MariaDB automatically creates several users and roles for administrative and internal server functions. 

## System Users

These user accounts are created by the `mariadb-install-db` script during the initial server setup.

### `root@localhost`

| **Creation**   | Created automatically by `mariadb-install-db`.                                                                                                                                                                                                  |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Purpose**    | Serves as the primary administrative account for initial server setup and management.                                                                                                                                                           |
| **Management** | It is highly recommended to secure this account immediately after installation. _Standard security practices include setting a strong password, renaming the account, or removing it entirely in favor of other named administrative accounts._ |

### `mariadb-sys@localhost`

| **Creation**   | Created automatically by `mariadb-install-db`.                                                                         |
| -------------- | ---------------------------------------------------------------------------------------------------------------------- |
| **Purpose**    | A mandatory system user required for internal server operations, such as executing scheduled events.                   |
| **Management** | <p>This user account is essential for server functionality and is protected; </p><p><em>it cannot be dropped.</em></p> |

## System Roles

These roles are built into the server and have special behaviors.

### The `PUBLIC` Role

The `PUBLIC` role is a special, built-in concept that represents every user on the server.

#### **Creation**

The `PUBLIC` role is created implicitly by the server the first time a `GRANT ... TO PUBLIC` statement is executed. It is not created with `CREATE ROLE`.

#### **Purpose**

It provides a convenient way to grant privileges server-wide without having to grant them to each user individually. Privileges granted to `PUBLIC` are inherited by all existing and future users.

#### **Management & Security:**

* Because the `PUBLIC` role is created implicitly, its creation is **not written to the audit log or binary log** as a standard DDL event. This is a critical detail for security auditing.
* The `PUBLIC` role cannot be explicitly dropped with `DROP ROLE`.
* To audit the privileges that apply to all users, you must check the grants for `PUBLIC` directly.

#### **Syntax Examples:**

```sql
-- Grant a privilege to all users
GRANT SELECT ON my_app.reports TO PUBLIC;

-- View privileges granted to PUBLIC
SHOW GRANTS FOR PUBLIC;

-- Revoke a privilege from all users
REVOKE SELECT ON my_app.reports FROM PUBLIC;
```
