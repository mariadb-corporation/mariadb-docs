---
description: >-
  MariaDB Connector/C supports batch (bulk) operations by binding an array of
  parameter sets to a single prepared statement, sending many rows to the
  server in one execution.
---

# Batch Operations with MariaDB Connector/C

C and C++ developers can use MariaDB Connector/C to perform batch (bulk) operations with MariaDB database products. A batch operation binds an array of parameter sets to a single [prepared statement](api-prepared-statement-functions/) and sends them to the server in one execution, which is more efficient than executing the statement once per row.

## Array Binding

MariaDB Connector/C implements batch operations through array binding. Instead of binding a single value to each statement parameter, the application binds an array of values per parameter and tells the connector how many rows to send:

* [`mysql_stmt_attr_set()`](api-prepared-statement-functions/mysql_stmt_attr_set.md) with `STMT_ATTR_ARRAY_SIZE` sets the number of rows in the batch. This is the only attribute required for a batch.

The connector supports two ways of laying out the bound values in memory:

* **Column-wise binding (the default).** Without `STMT_ATTR_ROW_SIZE`, each parameter's buffer is treated as an array of values, one per row — a contiguous array for fixed-length types, or an array of pointers for variable-length types such as strings.
* **Row-wise binding.** Setting [`mysql_stmt_attr_set()`](api-prepared-statement-functions/mysql_stmt_attr_set.md) with `STMT_ATTR_ROW_SIZE` to the size, in bytes, of one row makes the connector stride through an array of structures, where each row's values are stored together in a single `struct`.

Each bound parameter uses an indicator variable to describe its value. For null-terminated strings, the indicator is `STMT_INDICATOR_NTS`; other indicators include `STMT_INDICATOR_NULL` for `NULL` values and `STMT_INDICATOR_DEFAULT` for default values.

## Code Example: Batch Insert

The following code inserts several contacts into the [example table](setup-for-examples.md) in a single batch using row-wise binding. Each contact is stored in a `struct`, and an indicator variable accompanies each string to mark it as null-terminated:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mysql.h>

// One row of parameters, with an indicator variable for each string
struct st_contact {
   char first_name[25]; char first_ind;
   char last_name[25];  char last_ind;
   char email[100];     char email_ind;
};

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

   // The batch of rows to insert. Each string is null-terminated,
   // so its indicator is STMT_INDICATOR_NTS.
   struct st_contact data[] = {
      { "John",   STMT_INDICATOR_NTS, "Smith", STMT_INDICATOR_NTS, "john.smith@example.com",   STMT_INDICATOR_NTS },
      { "Jon",    STMT_INDICATOR_NTS, "Smith", STMT_INDICATOR_NTS, "jon.smith@example.com",    STMT_INDICATOR_NTS },
      { "Johnny", STMT_INDICATOR_NTS, "Smith", STMT_INDICATOR_NTS, "johnny.smith@example.com", STMT_INDICATOR_NTS }
   };
   unsigned int array_size = 3;
   size_t row_size = sizeof(struct st_contact);

   // Initialize and prepare the statement
   MYSQL_STMT *stmt = mysql_stmt_init(conn);
   if (mysql_stmt_prepare(stmt,
         "INSERT INTO test.contacts(first_name, last_name, email) VALUES (?, ?, ?)", -1))
   {
      fprintf(stderr, "Error preparing statement: %s\n", mysql_stmt_error(stmt));
      exit(1);
   }

   // Bind the first row; the connector strides through the array using row_size
   MYSQL_BIND bind[3];
   memset(bind, 0, sizeof(bind));
   bind[0].buffer_type = MYSQL_TYPE_STRING;
   bind[0].buffer = &data[0].first_name;
   bind[0].u.indicator = &data[0].first_ind;
   bind[1].buffer_type = MYSQL_TYPE_STRING;
   bind[1].buffer = &data[0].last_name;
   bind[1].u.indicator = &data[0].last_ind;
   bind[2].buffer_type = MYSQL_TYPE_STRING;
   bind[2].buffer = &data[0].email;
   bind[2].u.indicator = &data[0].email_ind;

   // Set the batch size and the row stride
   mysql_stmt_attr_set(stmt, STMT_ATTR_ARRAY_SIZE, &array_size);
   mysql_stmt_attr_set(stmt, STMT_ATTR_ROW_SIZE, &row_size);

   // Bind and execute the batch in a single call
   if (mysql_stmt_bind_param(stmt, bind) || mysql_stmt_execute(stmt))
   {
      fprintf(stderr, "Error executing batch: %s\n", mysql_stmt_error(stmt));
      exit(1);
   }

   // Close the statement and the connection
   mysql_stmt_close(stmt);
   mysql_close(conn);

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

## See Also

For more batch insert examples, including column-wise binding, see [Prepared Statement Examples](api-prepared-statement-functions/prepared-statement-examples/):

* [Bulk Insert (Row-wise Binding)](api-prepared-statement-functions/prepared-statement-examples/bulk-insert-row-wise-binding.md)
* [Bulk Insert (Column-wise Binding)](api-prepared-statement-functions/prepared-statement-examples/bulk-insert-column-wise-binding.md)

{% @marketo/form formId="4316" %}
