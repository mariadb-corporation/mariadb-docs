---
description: >-
  Instructions for running the `mariadb-install-db` script on Unix-like systems
  to initialize the MariaDB data directory and system tables.
---

# Installing System Tables on Unix

`mariadb-install-db` initializes the MariaDB data directory and creates the [system tables](../../../../reference/system-tables/) in the [mysql](../../../../reference/system-tables/the-mysql-database-tables/) database, if they do not exist. MariaDB uses these tables to manage [privileges](../../../../reference/sql-statements/account-management-sql-statements/grant.md#privilege-levels), [roles](../../../../security/user-account-management/roles/), and [plugins](../../../../reference/plugins/). It also uses them to provide the data for the [help](../../../../reference/sql-statements/administrative-sql-statements/help-command.md) command in the [mariadb](../../../../clients-and-utilities/mariadb-client/mariadb-command-line-client.md) client.

[mariadb-install-db](../../../../clients-and-utilities/deployment-tools/mariadb-install-db.md) works by starting MariaDB Server's `mysqld` process in [--bootstrap](../../../starting-and-stopping-mariadb/mariadbd-options.md) mode and sending commands to create the [system tables](../../../../reference/system-tables/) and their content.

There is a version specifically for Windows, [mysql\_install\_db.exe](mariadb-install-db-exe.md).

To invoke `mariadb-install-db`, use the following syntax:

```bash
mariadb-install-db --user=mysql
```

For the options supported by [mariadb-install-db](../../../../clients-and-utilities/deployment-tools/mariadb-install-db.md), see [mariadb-install-db: Options](../../../../clients-and-utilities/deployment-tools/mariadb-install-db.md#options).

For the option groups read by [mariadb-install-db](../../../../clients-and-utilities/deployment-tools/mariadb-install-db.md), see [mariadb-install-db: Option Groups](../../../../clients-and-utilities/deployment-tools/mariadb-install-db.md#option-groups).

See [mariadb-install-db: Installing System Tables](../../../../clients-and-utilities/deployment-tools/mariadb-install-db.md#installing-system-tables) for information on the installation process.

See [mariadb-install-db: Troubleshooting Issues](../../../../clients-and-utilities/deployment-tools/mariadb-install-db.md#troubleshooting-issues) for information on how to troubleshoot the installation process.

## See Also

* [mariadb-install-db](../../../../clients-and-utilities/deployment-tools/mariadb-install-db.md)
* The Windows version of `mariadb-install-db`: [mysql\_install\_db.exe](mariadb-install-db-exe.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
