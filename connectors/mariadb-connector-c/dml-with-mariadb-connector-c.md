---
description: >-
  MariaDB Connector/C supports DML operations including INSERT, UPDATE, DELETE,
  and SELECT, using prepared statements and result sets to manipulate data in
  MariaDB databases.
---

# DML with MariaDB Connector/C

C and C++ developers can use MariaDB Connector/C to perform basic DML (Data Manipulation Language) operations with MariaDB database products.

## DML Operations

DML (Data Manipulation Language) refers to all SQL data statements in the SQL standard (_ISO/IEC 9075-2:2016_). Some examples of DML include [DELETE](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete), [INSERT](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert), [REPLACE](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/replace), [SELECT](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select), and [UPDATE](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update).

## Code Example: INSERT, UPDATE, DELETE

[INSERT](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert), [UPDATE](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update), and [DELETE](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) are DML operations that modify the data in a table.

The following code demonstrates how to execute an `INSERT` on the [example table](setup-for-examples.md) using a [prepared statement](api-prepared-statement-functions/), which safely binds user-supplied values to statement parameters.

To update or delete data, replace the `INSERT` statement and bound parameters with an `UPDATE` or `DELETE` statement:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mysql.h>

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

   // Values to insert
   char first_name[] = "John";
   char last_name[]  = "Smith";
   char email[]      = "john.smith@example.com";

   // Initialize and prepare the statement
   MYSQL_STMT *stmt = mysql_stmt_init(conn);
   if (mysql_stmt_prepare(stmt,
         "INSERT INTO test.contacts(first_name, last_name, email) VALUES (?, ?, ?)", -1))
   {
      fprintf(stderr, "Error preparing statement: %s\n", mysql_stmt_error(stmt));
      exit(1);
   }

   // Bind the values to the statement parameters
   MYSQL_BIND bind[3];
   memset(bind, 0, sizeof(bind));
   bind[0].buffer_type = MYSQL_TYPE_STRING;
   bind[0].buffer = first_name;
   bind[0].buffer_length = strlen(first_name);
   bind[1].buffer_type = MYSQL_TYPE_STRING;
   bind[1].buffer = last_name;
   bind[1].buffer_length = strlen(last_name);
   bind[2].buffer_type = MYSQL_TYPE_STRING;
   bind[2].buffer = email;
   bind[2].buffer_length = strlen(email);

   // Execute the statement
   if (mysql_stmt_bind_param(stmt, bind) || mysql_stmt_execute(stmt))
   {
      fprintf(stderr, "Error adding contact: %s\n", mysql_stmt_error(stmt));
      exit(1);
   }

   // Close the statement and the connection
   mysql_stmt_close(stmt);
   mysql_close(conn);

   return 0;
}
```

Confirm the data was inserted by using [MariaDB Client](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client) to execute a [SELECT](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) statement:

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

[SELECT](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) is a DML operation that reads the data from a table.

The following code demonstrates how to execute `SELECT` on the [example table](setup-for-examples.md) and iterate over the result set with [`mysql_fetch_row()`](api-functions/mysql_fetch_row.md):

```c
#include <stdio.h>
#include <stdlib.h>
#include <mysql.h>

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

   // Execute the SELECT statement
   if (mysql_query(conn, "SELECT first_name, last_name, email FROM test.contacts"))
   {
      fprintf(stderr, "Error printing contacts: %s\n", mysql_error(conn));
      mysql_close(conn);
      exit(1);
   }

   // Store and iterate over the result set
   MYSQL_RES *result = mysql_store_result(conn);
   MYSQL_ROW row;
   while ((row = mysql_fetch_row(result)))
   {
      printf("- %s %s <%s>\n", row[0], row[1], row[2]);
   }

   // Free the result set and close the connection
   mysql_free_result(result);
   mysql_close(conn);

   return 0;
}
```

Example output:

```sql
- John Smith <john.smith@example.com>
- Jon Smith <jon.smith@example.com>
- Johnny Smith <johnny.smith@example.com>
```

{% @marketo/form formId="4316" %}
