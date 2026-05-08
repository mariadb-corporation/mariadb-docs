---
description: >-
  Set up the test database and user account required by MariaDB Connector/C
  code examples, including schema creation SQL and privilege grants for
  db_user.
---

# Setup for Examples

Examples in this MariaDB Connector/C documentation depend on a database `test` and table `contacts`.

## Create the Schema

Create the example database and table:

> ```sql
> CREATE DATABASE IF NOT EXISTS test;
>
> CREATE TABLE test.contacts (
>    id INT PRIMARY KEY AUTO_INCREMENT,
>    first_name VARCHAR(25),
>    last_name VARCHAR(25),
>    email VARCHAR(100)) ENGINE=InnoDB;
> ```

## Create the User

Create a user `db_user` with privileges to execute the examples:

> ```sql
> CREATE USER IF NOT EXISTS db_user@192.0.2.1
>     IDENTIFIED BY 'db_user_password';
> ```
>
> ```sql
> GRANT ALL PRIVILEGES ON test.* TO db_user@192.0.2.1;
> ```

### Password Guidance

Passwords should meet your organization's password policies. If your MariaDB Enterprise Server instance has a password validation plugin installed, the password must also meet the configured requirements.

By default, MariaDB Enterprise Server installs the [simple\_password\_check](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/simple-password-check-plugin) plugin, configured with system variables:

* [simple\_password\_check\_digits](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/simple-password-check-plugin#simple_password_check_digits)
* [simple\_password\_check\_letters\_same\_case](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/simple-password-check-plugin#simple_password_check_letters_same_case)
* [simple\_password\_check\_minimal\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/simple-password-check-plugin#simple_password_check_minimal_length)
* [simple\_password\_check\_other\_characters](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/simple-password-check-plugin#simple_password_check_other_characters) system variables.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
