---
description: >-
  MariaDB Connector/C++ supports DML operations including INSERT, UPDATE,
  DELETE, and SELECT, using prepared statements and result sets to
  manipulate data in MariaDB databases.
---

# DML with MariaDB Connector/C++

C++ developers can use MariaDB Connector/C++ to perform basic DML (Data Manipulation Language) operations with MariaDB database products.

## DML Operations

DML (Data Manipulation Language) refers to all SQL data statements in the SQL standard (_ISO/IEC 9075-2:2016_). Some examples of DML include [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete), [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert), [REPLACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/replace), [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select), and [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update).

## Code Example: INSERT, UPDATE, DELETE

[INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert), [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update), and [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) are DML (Data Manipulation Language) operations that modify the data in a table.

The following code demonstrates how to execute an `INSERT` on the [example table](setup-for-connector-cpp-examples.md).

To update or delete data, replace the `INSERT` statement in the code example with an `UPDATE` or `DELETE` statement:

```sql
// Includes
#include <iostream>
#include <mariadb/conncpp.hpp>

// Function to Add Contact
void addContact(std::shared_ptr<sql::PreparedStatement> &stmnt,
   sql::SQLString first_name,
   sql::SQLString last_name,
   sql::SQLString email)
{
   try {
      // Bind variables to prepared statement parameters
      // Note that the index starts at 1--not 0
      stmnt->setString(1, first_name);
      stmnt->setString(2, last_name);
      stmnt->setString(3, email);

      // Execute Statement
      stmnt->executeUpdate();
   }

   // Handle Exceptions
   catch (sql::SQLException &e) {
      std::cerr << "Error adding contact to database: "
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

      // Created a PreparedStatement
      // Use a smart pointer for extra safety
      std::shared_ptr<sql::PreparedStatement> stmnt(
            conn->prepareStatement(
               "INSERT INTO test.contacts(first_name, last_name, email) VALUES (?, ?, ?)"
            )
         );

      // Use prepared statement to add data
      addContact(stmnt, "John", "Smith", "john.smith@example.com");

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

Confirm the data was properly inserted by using [MariaDB Client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client) to execute a [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) statement:

```sql
SELECT * FROM test.contacts;
```

```sql
+----+------------+-----------+------------------------+
| id | first_name | last_name | email                  |
+----+------------+-----------+------------------------+
|  1 | John       | Smith     | john.smith@example.com |
+----+------------+-----------+------------------------+
```

## Code Example: SELECT

[SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) is a DML (Data Manipulation Language) operation that reads the data from a table.

The following code demonstrates how to execute `SELECT` on the [example table](setup-for-connector-cpp-examples.md):

```sql
// Includes
#include <iostream>
#include <mariadb/conncpp.hpp>

// Function to print Contacts
void printContacts(std::shared_ptr<sql::Statement> &stmnt)
{
   try {
      // Execute SELECT Statement
      std::unique_ptr<sql::ResultSet> res(
            stmnt->executeQuery("SELECT first_name, last_name, email FROM test.contacts")
         );

      // Loop over Result-set
      while (res->next())
      {
         // Retrieve Values and Print Contacts
         std::cout << "- "
            << res->getString("first_name")
            << " "
            << res->getString("last_name")
            << " <"
            << res->getString("email")
            << ">"
            << std::endl;
      }
   }

   // Catch Exception
   catch (sql::SQLException& e) {
      std::cerr << "Error printing contacts: "
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
      std::shared_ptr<sql::Statement> stmnt(conn->createStatement());

      printContacts(stmnt);

      // Close Connection
      conn->close();
   }

   // Catch Exceptions
   catch (sql::SQLException &e) {
      std::cerr << "Error Connecting to the database: "
         << e.what() << std::endl;

      // Exit (Failed)
      return 1;
   }

   // Exit (Success)
   return 0;
}
```

Example output:

```sql
- John Smith <john.smith@example.com>
- Jon Smith <jon.smith@example.com>
- Johnny Smith <johnny.smith@example.com>
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
