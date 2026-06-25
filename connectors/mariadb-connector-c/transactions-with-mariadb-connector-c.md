---
description: >-
  MariaDB Connector/C supports multi-statement transactions with manual commit
  and rollback by disabling auto-commit with mysql_autocommit() on the
  connection.
---

# Transactions with MariaDB Connector/C

Developers can use MariaDB Connector/C to perform basic DML (Data Manipulation Language) operations inside a transaction with MariaDB database products.

## Auto-Commit Behavior

By default, MariaDB Connector/C enables auto-commit. When auto-commit is enabled, each SQL statement is executed in its own transaction.

## Multi-Statement Transactions

MariaDB Connector/C supports multi-statement transactions when auto-commit is disabled.

Disable auto-commit by calling [`mysql_autocommit()`](api-functions/mysql_autocommit.md) with a `mode` of `0`:

```c
mysql_autocommit(conn, 0);
```

When auto-commit is disabled, a new transaction is automatically started when the current transaction is manually committed or rolled back. The application does not need to manually start each new transaction with [START TRANSACTION](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/start-transaction) or [BEGIN](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/begin-end).

The transaction can be manually managed by performing the following operations:

* Commit the transaction by calling [`mysql_commit()`](api-functions/mysql_commit.md) or using [COMMIT](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/commit).
* Roll back the transaction by calling [`mysql_rollback()`](api-functions/mysql_rollback.md) or using [ROLLBACK](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/rollback).
* Re-enable auto-commit by calling [`mysql_autocommit()`](api-functions/mysql_autocommit.md) with a `mode` of `1`.

## Code Example: DML in a Transaction

[UPDATE](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update), [INSERT](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert), and [DELETE](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) are DML operations that modify data in a table.

The following code demonstrates how to execute several [UPDATE](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) statements on the [example table](setup-for-examples.md) within a single transaction with auto-commit disabled. All of the updates are committed together; if any update fails, the transaction is rolled back so none of them are applied.

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mysql.h>

// Update a contact's email by first name using the prepared statement
static void update_contact(MYSQL_STMT *stmt, const char *email, const char *first_name)
{
   MYSQL_BIND bind[2];
   memset(bind, 0, sizeof(bind));
   bind[0].buffer_type = MYSQL_TYPE_STRING;
   bind[0].buffer = (char *) email;
   bind[0].buffer_length = strlen(email);
   bind[1].buffer_type = MYSQL_TYPE_STRING;
   bind[1].buffer = (char *) first_name;
   bind[1].buffer_length = strlen(first_name);

   if (mysql_stmt_bind_param(stmt, bind) || mysql_stmt_execute(stmt))
      fprintf(stderr, "Error updating contact: %s\n", mysql_stmt_error(stmt));
}

int main(int argc, char *argv[])
{
   // Initialize Connection
   MYSQL *conn;
   if (!(conn = mysql_init(0)))
   {
      fprintf(stderr, "unable to initialize connection struct\n");
      exit(1);
   }

   // Connect to the database
   if (!mysql_real_connect(
         conn, "mariadb.example.net", "db_user", "db_user_password",
         "test", 3306, NULL, 0))
   {
      fprintf(stderr, "Error connecting to Server: %s\n", mysql_error(conn));
      mysql_close(conn);
      exit(1);
   }

   // Disable auto-commit to start a user-managed transaction
   mysql_autocommit(conn, 0);

   // Prepare the UPDATE statement once and reuse it
   MYSQL_STMT *stmt = mysql_stmt_init(conn);
   if (mysql_stmt_prepare(stmt,
         "UPDATE test.contacts SET email=? WHERE first_name=?", -1))
   {
      fprintf(stderr, "Error preparing statement: %s\n", mysql_stmt_error(stmt));
      exit(1);
   }

   // Apply several updates within the transaction
   update_contact(stmt, "johnsmith@example.com",   "John");
   update_contact(stmt, "jonsmith@example.com",    "Jon");
   update_contact(stmt, "johnnysmith@example.com", "Johnny");

   // Commit the transaction; roll back on failure
   if (mysql_commit(conn))
   {
      fprintf(stderr, "Error committing transaction: %s\n", mysql_error(conn));
      mysql_rollback(conn);
   }

   // Close the statement and the connection
   mysql_stmt_close(stmt);
   mysql_close(conn);

   return 0;
}
```

The query below confirms the [UPDATE](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update) of the [example table](setup-for-examples.md):

```sql
SELECT * FROM test.contacts;
```

```sql
+----+------------+-----------+-------------------------+
| id | first_name | last_name | email                   |
+----+------------+-----------+-------------------------+
|  1 | John       | Smith     | johnsmith@example.com   |
|  2 | Jon        | Smith     | jonsmith@example.com    |
|  3 | Johnny     | Smith     | johnnysmith@example.com |
+----+------------+-----------+-------------------------+
```

{% @marketo/form formId="4316" %}
