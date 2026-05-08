---
description: >-
  Set up the test database, contact table, and user account required by the
  MariaDB Connector/R2DBC native API code examples in this documentation
  section.
---

# Setup for Connector/R2DBC Examples (Native API)

## Overview

The examples in this MariaDB Connector/R2DBC documentation depend on a database test and table contact.

## Create the Schema

1. Create a test database if one does not exist with the CREATE DATABASE statement:

```sql
CREATE DATABASE IF NOT EXISTS test;
```

1. Create an example table test.contact with the CREATE TABLE statement:

```sql
CREATE TABLE IF NOT EXISTS test.contact(
   id INT PRIMARY KEY AUTO_INCREMENT,
   first_name VARCHAR(25),
   last_name VARCHAR(25),
   email VARCHAR(25)) ENGINE=InnoDB;
```

## Create the User

1. Create a user account to test connectivity with the CREATE USER statement:

```sql
CREATE USER 'connr2dbc_test'@'192.0.2.50'
   IDENTIFIED BY 'db_user_password';
```

1. Ensure that the user account has privileges to access the tables with the GRANT statement:

```sql
GRANT ALL PRIVILEGES
   ON test.*
   TO 'connr2dbc_test'@'192.0.2.50';
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>


{% @marketo/form formId="4316" %}
