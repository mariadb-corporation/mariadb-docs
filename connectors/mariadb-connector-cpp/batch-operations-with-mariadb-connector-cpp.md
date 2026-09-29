---
description: >-
  MariaDB Connector/C++ supports batch (bulk) operations by queuing commands on
  a sql::Statement or sql::PreparedStatement with addBatch() and sending them
  to the server in a single executeBatch() call.
---

# Batch Operations with MariaDB Connector/C++

C++ developers can use MariaDB Connector/C++ to perform batch (bulk) operations with MariaDB database products. MariaDB Connector/C++ implements the JDBC API, so a batch is built by queuing commands on a statement and then sending the whole queue to the server in a single execution, which is more efficient than executing each command on its own.

## The Batch API

Batches are queued and executed with the following `sql::Statement` and `sql::PreparedStatement` methods:

| Method | Description |
| ------ | ----------- |
| `sql::Statement::addBatch(const SQLString& sql)` | Queues a literal SQL statement. |
| `sql::PreparedStatement::addBatch()` | Queues the parameter values currently set on the prepared statement. |
| `sql::Statement::executeBatch()` | Sends the queued commands and returns a `const sql::Ints&` of update counts. |
| `sql::Statement::executeLargeBatch()` | The same as `executeBatch()`, returning a `const sql::Longs&` for update counts that exceed the range of a 32-bit integer. |
| `sql::Statement::clearBatch()` | Discards the queued commands without executing them. |

`sql::PreparedStatement` derives from `sql::Statement`, so `executeBatch()`, `executeLargeBatch()`, and `clearBatch()` are available on both classes. `sql::Ints` and `sql::Longs` are the connector's array wrappers for `int32_t` and `int64_t`, and both support iteration with `begin()` and `end()`.

The returned array contains one update count for each queued command, in the order the commands were added. Two of the values are constants rather than row counts:

* `sql::Statement::SUCCESS_NO_INFO` (`-2`) — the command succeeded, but the server did not report the number of affected rows.
* `sql::Statement::EXECUTE_FAILED` (`-3`) — the command failed.

## Code Example: Prepared Statement Batch

The following code inserts several contacts into the [example table](setup-for-connector-cpp-examples.md) in a single batch. Each row's values are bound to the prepared statement and queued with `addBatch()`, and the whole batch is sent with one `executeBatch()` call:

```c++
// Includes
#include <iostream>
#include <mariadb/conncpp.hpp>

// Function to queue a Contact
void queueContact(std::unique_ptr<sql::PreparedStatement> &stmnt,
   sql::SQLString first_name,
   sql::SQLString last_name,
   sql::SQLString email)
{
   // Bind variables to prepared statement parameters
   // Note that the index starts at 1--not 0
   stmnt->setString(1, first_name);
   stmnt->setString(2, last_name);
   stmnt->setString(3, email);

   // Queue the current parameter values as one row of the batch
   stmnt->addBatch();
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

      // Use a properties map for the other connection options.
      // useBulkStmts enables the dedicated bulk protocol for this connection.
      sql::Properties properties({
            {"user", "db_user"},
            {"password", "db_user_password"},
            {"useBulkStmts", "true"},
         });

      // Establish Connection
      // Use a smart pointer for extra safety
      std::unique_ptr<sql::Connection> conn(driver->connect(url, properties));

      // Create a PreparedStatement
      // Use a smart pointer for extra safety
      std::unique_ptr<sql::PreparedStatement> stmnt(
            conn->prepareStatement(
               "INSERT INTO test.contacts(first_name, last_name, email) VALUES (?, ?, ?)"
            )
         );

      // Queue each row of the batch
      queueContact(stmnt, "John", "Smith", "john.smith@example.com");
      queueContact(stmnt, "Jon", "Smith", "jon.smith@example.com");
      queueContact(stmnt, "Johnny", "Smith", "johnny.smith@example.com");

      // Send the whole batch in a single execution
      const sql::Ints& counts = stmnt->executeBatch();

      // One update count per queued row, in the order the rows were added
      for (const int32_t& count : counts)
      {
         std::cout << "Affected rows: " << count << std::endl;
      }

      // Discard the queued rows before reusing the statement for a new batch
      stmnt->clearBatch();

      // Close Connection
      conn->close();
   }

   // Catch a batch failure
   catch (sql::BatchUpdateException& e) {
      std::cerr << "Error executing batch: "
         << e.what() << std::endl;

      // Exit (Failed)
      return 1;
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

Confirm the rows were inserted by using [MariaDB Client](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client) to execute a [SELECT](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) statement:

```sql
SELECT * FROM test.contacts;
```

```sql
+----+------------+-----------+--------------------------+
| id | first_name | last_name | email                    |
+----+------------+-----------+--------------------------+
|  1 | John       | Smith     | john.smith@example.com   |
|  2 | Jon        | Smith     | jon.smith@example.com    |
|  3 | Johnny     | Smith     | johnny.smith@example.com |
+----+------------+-----------+--------------------------+
```

{% hint style="info" %}
Every parameter must be set before each `addBatch()` call. If any parameter is unset, the connector raises an `sql::SQLException` reporting how many parameters the statement expects.
{% endhint %}

## Code Example: Statement Batch

An `sql::Statement` batches literal SQL instead of parameter sets, which is useful for grouping statements that take no parameters, such as [DDL](ddl-with-mariadb-connector-cpp.md) changes. Queue each statement with the `addBatch()` overload that takes an `sql::SQLString`:

```c++
// Create a Statement
// Use a smart pointer for extra safety
std::unique_ptr<sql::Statement> stmnt(conn->createStatement());

// Queue each statement
stmnt->addBatch("INSERT INTO test.contacts(first_name, last_name, email) "
                "VALUES ('John', 'Smith', 'john.smith@example.com')");
stmnt->addBatch("INSERT INTO test.contacts(first_name, last_name, email) "
                "VALUES ('Jon', 'Smith', 'jon.smith@example.com')");

// Send the whole batch in a single execution
const sql::Ints& counts = stmnt->executeBatch();
```

Empty strings are rejected: passing one to `addBatch()` raises an `sql::SQLException`.

## Execution Strategies

MariaDB Connector/C++ has several ways to send a batch to the server, and the strategy it chooses depends on the connection options, the statement, and whether the query can be rewritten. The relevant [connection parameters](connect-with-mariadb-connectorcpp.md) are:

| Parameter | Default | Description |
| --------- | ------- | ----------- |
| `useBulkStmts` | `false` | Uses the dedicated MariaDB bulk execution protocol, which sends the whole batch as a single command and can be much faster. Requires MariaDB Server 10.2.7 or later. |
| `rewriteBatchedStatements` | `false` | Rewrites a batch of `INSERT` statements into a single multi-values `INSERT`, or, where that is not possible, into semicolon-separated statements. Takes precedence over `useBulkStmts`. |
| `useBatchMultiSend` | `false` | Sends the batch to the server in groups, reading the results afterward, instead of waiting for each result before sending the next command. The group size is set by `useBatchMultiSendNumber`, which defaults to `100`. Mainly useful when the client is distant from the server. |
| `continueBatchOnError` | `true` | Controls whether the connector executes the rest of the batch after a command fails, or stops at the first failure. |

By default MariaDB Connector/C++ uses client-side prepared statements, and for a batch on one of those it picks the first applicable strategy in this order:

1. If `rewriteBatchedStatements` is enabled and the statement can be rewritten as a multi-values `INSERT`, the batch is sent as one query — `INSERT INTO X(a,b) VALUES (1,2), (3,4), ...`.
2. If `rewriteBatchedStatements` is enabled and the statement can be rewritten as multiple statements, the batch is sent either through the bulk protocol, when `useBulkStmts` also allows it, or as semicolon-separated statements — `INSERT INTO X(a,b) VALUES (1,2);INSERT INTO X(a,b) VALUES (3,4); ...`.
3. If `useBulkStmts` is enabled, the batch is sent through the bulk protocol.
4. Otherwise, the connector sends the commands individually.

When `useServerPrepStmts` is enabled, batches are instead sent through the server's batched execution path, which the connector uses when either `useBulkStmts` or `useBatchMultiSend` is enabled, and otherwise falls back to executing each queued parameter set in turn.

Two restrictions apply to the faster strategies. Neither the bulk protocol nor the multi-values rewrite is used when the statement was created with `sql::Statement::RETURN_GENERATED_KEYS`, and the bulk protocol is not used when any parameter was set as a stream. In both cases the connector falls back to a slower strategy rather than failing.

{% hint style="info" %}
Enabling `rewriteBatchedStatements` also disables `useServerPrepStmts`, because a rewritten batch is prepared on the client. It additionally requires the multi-statement capability, which the connector negotiates with the server on connection.
{% endhint %}

## Clearing the Batch

Call `clearBatch()` explicitly when reusing a prepared statement for a second batch. A prepared statement in MariaDB Connector/C++ 1.1 does not reliably discard its queued parameter sets after a successful `executeBatch()`, so without `clearBatch()` the earlier rows can be sent again with the next batch.

## Error Handling

When a batch fails, `executeBatch()` and `executeLargeBatch()` throw an `sql::BatchUpdateException`, which derives from `sql::SQLException`. Catch `sql::BatchUpdateException` before `sql::SQLException` if you want to handle a batch failure separately.

{% hint style="warning" %}
In MariaDB Connector/C++ 1.1, the `sql::BatchUpdateException` does not carry the per-command update counts, so the exception cannot be used to determine which command in the batch failed.
{% endhint %}

## See Also

* [DML with MariaDB Connector/C++](dml-with-mariadb-connector-cpp.md) — executing single `INSERT`, `UPDATE`, `DELETE`, and `SELECT` statements.
* [Transactions with MariaDB Connector/C++](transactions-with-mariadb-connector-cpp.md) — grouping statements into a transaction.
* [Connect with MariaDB Connector/C++](connect-with-mariadb-connectorcpp.md) — the full list of connection parameters.
* [Batch Operations with MariaDB Connector/C](../mariadb-connector-c/batch-operations-with-mariadb-connector-c.md) — the equivalent array-binding API in MariaDB Connector/C.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
