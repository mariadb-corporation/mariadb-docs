---
description: >-
  MariaDB Connector/C++ supports multi-statement transactions with manual
  commit, rollback, and savepoints by disabling auto-commit on the
  sql::Connection object.
---

# Transactions with MariaDB Connector/C++

Developers can use MariaDB Connector/C++ to perform basic DML (Data Manipulation Language) operations inside a transaction with MariaDB database products.

## Auto-Commit Behavior

By default, MariaDB Connector/C++ enables auto-commit. When auto-commit is enabled, each SQL statement is executed in its own transaction.

Confirm the `auto-commit` is enabled by calling `sql::Connection::getAutoCommit():`

```c++
bool isAutoCommit = conn->getAutoCommit();
```

## Multi-Statement Transactions

MariaDB Connector/C++ supports multi-statement transactions when the `auto-commit` is disabled.

Disable auto-commit by calling `sql::Connection::setAutoCommit():`

```c++
conn->setAutoCommit(false);
```

When auto-commit is disabled, a new transaction is automatically started when the current transaction is manually committed or rolled back. It means the application does not need to manually start each new transaction with [START TRANSACTION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/start-transaction) or [BEGIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/clientserver-protocol/replication-protocol/begin_load_query_event).

The transaction can be manually managed by performing the following operations:

* Setting the transaction isolation by calling `sql::Connection::setTransactionIsolation()` or using [SET TRANSACTION ISOLATION LEVEL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set-transaction).
* Set the transaction to read-only by calling `sql::Connection::setReadOnly()` or using [SET TRANSACTION READ ONLY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set-transaction).
* Create a `savepoint` by calling `sql::Connection::setSavepoint()` or using [SAVEPOINT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/savepoint).
* Release a `savepoint` by calling `sql::Connection::releaseSavepoint()` or using [RELEASE SAVEPOINT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/savepoint).
* Roll back to a `savepoint` by calling `sql::Connection::rollback()` with the savepoint or using [ROLLBACK TO SAVEPOINT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/savepoint).
* Commit the transaction by calling `sql::Connection::commit()` or using [COMMIT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/commit).
* Roll back the transaction by calling `sql::Connection::rollback()` or using [ROLLBACK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/rollback).

## Code Example: DML in Transaction

[UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update), [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert), and [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) are DML (Data Manipulation Language) operations that modify data in a table.

The following code demonstrates how to execute [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) on the [example table](setup-for-connector-cpp-examples.md) within a transaction with auto-commit disabled.

To insert or delete data, replace the [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) statement in the code example with an [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert) or [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) statement:

```sql
// Includes
#include <iostream>
#include <mariadb/conncpp.hpp>

void updateContact(std::shared_ptr<sql::PreparedStatement> &stmnt,
                   sql::SQLString first_name,
                   sql::SQLString email)
{
   try {
      // Bind variables to prepared statement parameters
      // Note that the index starts at 1--not 0
      stmnt->setString(1, email);
      stmnt->setString(2, first_name);

      // Execute Statement
      stmnt->executeUpdate();
   }

   // Catch Exception
   catch (sql::SQLException &e) {
      std::cerr << "Error updating contact: "
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

      // Use Connection to update contacts with a transaction
      try {
         // Disabling ``auto-commit`` mode automatically starts a new user managed transaction.
         conn->setAutoCommit(false);

         // Create a PreparedStatement
         // Use a smart pointer for extra safety
         std::shared_ptr<sql::PreparedStatement> stmnt(conn->prepareStatement(
                  "UPDATE test.contacts SET email=? WHERE first_name = ?"
               )
            );

         std::string contacts[3][2] = {
               { "John", "johnsmith@example.com" },
               { "Jon", "jonsmith@example.com" },
               { "Johnny", "johnnysmith@example.com" }
            };

         for (int row { 0 }; row < 3; ++row) {
            updateContact(stmnt, contacts[row][0], contacts[row][1]);
         }

         // Commit the transaction
         conn->commit();
      }
      catch (sql::SQLException &e) {
         std::cerr << "Error updating contact with a transaction: "
            << e.what() << std::endl;

         // Rollback the transaction
         conn->rollback();
      }

      // Close Connection
      conn->close();
   }
   catch (sql::SQLException &e) {
      std::cerr << "SQL exception in the database: "
         << e.what() << std::endl;

      // Exit (Failed)
      return 1;
   }

   // Exit (Success)
   return 0;
}
```

The query below confirms the [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) of the [example table](setup-for-connector-cpp-examples.md):

```sql
SELECT * FROM test.contacts;
```

```sql
+----+------------+-----------+-------------------------+
| id | first_name | last_name | email                   |
+----+------------+-----------+-------------------------+
|  1 | John       | Smith     | johnsmith@example.com   |
+----+------------+-----------+-------------------------+
|  2 | Jon        | Smith     | jonsmith@example.com    |
+----+------------+-----------+-------------------------+
|  3 | Johnny     | Smith     | johnnysmith@example.com |
+----+------------+-----------+-------------------------+
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
