---
description: >-
  Create the schema and user account prerequisites for MariaDB Connector/C++
  documentation examples, including the test database, contacts table, and
  appropriate GRANT statements.
---

# Setup for Connector/C++ Examples

Examples in the MariaDB Connector/C++ documentation depend on a database `test` and `table` contacts.

## Create the Schema

1. Create a `test` database if one does not exist with the [CREATE DATABASE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-database) statement:

```sql
CREATE DATABASE IF NOT EXISTS test;
```

1. Create tables in the `test` database for testing basic and advanced operations with [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/tables/create-table) statements:

```sql
CREATE TABLE test.contacts (
 id INT PRIMARY KEY AUTO_INCREMENT,
 first_name VARCHAR(25),
 last_name VARCHAR(25),
 email VARCHAR(100)) ENGINE=InnoDB;
```

## Create the User

1. Create a user account to test connectivity with the [CREATE USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/create-user) statement:

```sql
CREATE USER IF NOT EXISTS 'db_user'@'192.0.2.1'
 IDENTIFIED BY 'db_user_password';
```

1. Ensure that the user account has privileges to access the tables with the [GRANT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant) statement:

```sql
GRANT ALL PRIVILEGES
 ON test.*
 TO 'db_user'@'192.0.2.1';
```

### Password Guidance

Passwords should meet your organization's password policies. If your MariaDB Enterprise Server instance has a password validation plugin installed, the password must also meet the configured requirements.

By default, MariaDB Enterprise Server installs the `simple_password_check` plugin, configured with system variables:

* [simple\_password\_check\_digits](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/simple-password-check-plugin)
* [simple\_password\_check\_letters\_same\_case](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/simple-password-check-plugin)
* [simple\_password\_check\_minimal\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/simple-password-check-plugin)
* [simple\_password\_check\_other\_characters](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/simple-password-check-plugin) system variables.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
