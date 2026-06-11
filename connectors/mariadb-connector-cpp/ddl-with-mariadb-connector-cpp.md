---
description: >-
  MariaDB Connector/C++ supports DDL operations such as ALTER TABLE and TRUNCATE
  TABLE, letting C++ applications modify database schema using the
  sql::Statement class.
---

# DDL with MariaDB Connector/C++

C++ developers can use MariaDB Connector/C++ to perform basic DDL (Data Definition Language) operations with MariaDB database products.

## DDL Operations

DDL (Data Definition Language) refers to all SQL-schema statements in the SQL standard (ISO/IEC 9075-2:2016).

Some examples of DDL include [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table), [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/tables/create-table), [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/tables/drop-table), [CREATE DATABASE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-database), and [TRUNCATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/truncate-table).

## Code Example: ALTER TABLE

[ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) is a DDL (Data Definition Language) operation that changes an existing table.

The following code demonstrates how to execute [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) on the [example table](mariadb-connector-cpp-sample-application.md):

```sql
// Includes
#include <iostream>
#include <mariadb/conncpp.hpp>

// Function to Alter Table
void alterTable(std::shared_ptr<sql::Statement>  &stmnt)
{
   try {
      // Alter contacts Table
      stmnt->executeUpdate("ALTER TABLE test.contacts RENAME COLUMN first_name TO f_name");
   }

   // Catch Exception
   catch (sql::SQLException& e) {
      std::cerr << "Error altering table: "
         << e.what() << std::endl;
   }
}

// Main Process
int main(int argc, char **argv)
{
   try {
      // Instantiate Driver
      sql::Driver* driver = sql::mariadb::get_driver_instance();

      // Configure Connection
      // The URL or TCP connection string format is
      // ``jdbc:mariadb://host:port/database``.
      sql::SQLString url("jdbc:mariadb://192.0.2.1:3306/test");

      // Use a properties map for the other connection options
      sql::Properties properties({
            {"user", "db_user"},
            {"password", "db_user_password"},
         });

      // Establish Connection
      // Use a smart pointer for extra safety
      std::unique_ptr<sql::Connection> conn(driver->connect(url, properties));

      // Create a Statement
      // Use a smart pointer for extra safety
      std::shared_ptr<sql::Statement>  stmnt(conn->createStatement());

      // Use Statement to alter table
      alterTable(stmnt);

      // Close Connection
      conn->close();
   }

   // Catch Exceptions
   catch (sql::SQLException& e) {
      std::cerr << "Error Connecting to the database: "
         << e.what() << std::endl;

      // Exit (Failed)
      return 1;
   }

   // Exit (Success)
   return 0;
}
```

Confirm the table was properly altered by using [MariaDB Client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client) to execute a [DESC](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/describe) statement on the same table:

```sql
DESC contacts;
```

```sql
+---------------+--------------+------+-----+---------+----------------+
| Field         | Type         | Null | Key | Default | Extra          |
+---------------+--------------+------+-----+---------+----------------+
| id            | int(11)      | NO   | PRI | NULL    | auto_increment |
| f_name        | varchar(25)  | YES  |     | NULL    |                |
| last_name     | varchar(25)  | YES  |     | NULL    |                |
| email         | varchar(100) | YES  |     | NULL    |                |
+---------------+--------------+------+-----+---------+----------------+
```

Code Example: `TRUNCATE TABLE` is a DDL (Data Definition Language) operation that deletes all data from an existing table.

The following code demonstrates how to execute [TRUNCATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/numeric-functions/truncate) on the [example table](setup-for-connector-cpp-examples.md):

```sql
// Includes
#include <iostream>
#include <mariadb/conncpp.hpp>

// Function to Truncate Table
void truncateTable(std::shared_ptr<sql::Statement>  &stmnt)
{
   try {
      // TRUNCATE contacts Table
      stmnt->executeUpdate("TRUNCATE test.contacts");
   }

   // Catch Exception
   catch (sql::SQLException& e) {
      std::cerr << "Error truncating table: "
         << e.what() << std::endl;
   }
}

// Main Process
int main(int argc, char **argv)
{
   try {
      // Instantiate Driver
      sql::Driver* driver = sql::mariadb::get_driver_instance();

      // Configure Connection
      // The URL or TCP connection string format is
      // ``jdbc:mariadb://host:port/database``.
      sql::SQLString url("jdbc:mariadb://192.0.2.1:3306/test");

      // Use a properties map for the other connection options
      sql::Properties properties({
            {"user", "db_user"},
            {"password", "db_user_password"},
         });

      // Establish Connection
      // Use a smart pointer for extra safety
      std::unique_ptr<sql::Connection> conn(driver->connect(url, properties));

      // Create a Statement
      // Use a smart pointer for extra safety
      std::shared_ptr<sql::Statement>  stmnt(conn->createStatement());

      // Use Prepared Statement to truncate table
      truncateTable(stmnt);

      // Close Connection
      conn->close();
   }

   // Catch Exceptions
   catch (sql::SQLException& e) {
      std::cerr << "Error Connecting to the database: "
         << e.what() << std::endl;

      // Exit (Failed)
      return 1;
   }

   // Exit (Success)
   return 0;
}
```

The following query confirms that the [TRUNCATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/numeric-functions/truncate) statement deleted all rows from the [example table](setup-for-connector-cpp-examples.md):

```sql
SELECT * FROM test.contacts;
```

```sql
Empty set (0.000 sec)
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
