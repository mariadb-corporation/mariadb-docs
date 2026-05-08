---
description: >-
  Set up the test database, contacts and accounts tables, and a user account
  required by the MariaDB Connector/Python code examples in this
  documentation.
---

# Setup for Examples

The examples in this MariaDB Connector/Python documentation depend on a database `test` and tables `contacts` and `accounts`.

## Create the Schema

1.  Create a `test` database if one does not exist with the [CREATE DATABASE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-database) statement:

    ```sql
    CREATE DATABASE IF NOT EXISTS test;
    ```
2.  Create tables in the `test` database for testing basic and advanced operations with [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) statements:

    ```sql
    CREATE TABLE test.contacts (
       id INT PRIMARY KEY AUTO_INCREMENT,
       first_name VARCHAR(25),
       last_name VARCHAR(25),
       email VARCHAR(100)
    ) ENGINE=InnoDB;

    CREATE TABLE test.accounts (
       id INT PRIMARY KEY AUTO_INCREMENT,
       first_name VARCHAR(25),
       last_name VARCHAR(25),
       email VARCHAR(100),
       amount DECIMAL(15,2) CHECK (amount >= 0.0),
       UNIQUE (email)
    ) ENGINE=InnoDB;
    ```

## Create the User

1.  Create a user account to test connectivity with the [CREATE USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/create-user) statement:

    ```sql
    CREATE USER 'db_user'@'192.0.2.1'
       IDENTIFIED BY 'db_user_password';
    ```
2.  Ensure that the user account has privileges to access the tables with the [GRANT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant) statement:

    ```sql
    GRANT SELECT, INSERT, UPDATE, DELETE, DROP
       ON test.contacts
       TO 'db_user'@'192.0.2.1';

    GRANT SELECT, INSERT, UPDATE, DELETE, DROP
       ON test.accounts
       TO 'db_user'@'192.0.2.1';
    ```

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
