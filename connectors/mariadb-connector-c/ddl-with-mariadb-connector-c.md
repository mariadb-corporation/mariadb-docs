---
description: >-
  MariaDB Connector/C supports DDL operations such as CREATE TABLE, ALTER
  TABLE, and TRUNCATE TABLE, letting C applications modify database schema by
  executing SQL statements with mysql_query().
---

# DDL with MariaDB Connector/C

C and C++ developers can use MariaDB Connector/C to perform basic DDL (Data Definition Language) operations with MariaDB database products.

## DDL Operations

DDL (Data Definition Language) refers to all SQL-schema statements in the SQL standard (ISO/IEC 9075-2:2016).

Some examples of DDL include [ALTER TABLE](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table), [CREATE TABLE](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-usage/tables/create-table), [DROP TABLE](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-usage/tables/drop-table), [CREATE DATABASE](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-database), and [TRUNCATE TABLE](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/truncate-table).

In MariaDB Connector/C, DDL statements are executed with [`mysql_query()`](api-functions/mysql_query.md) (or [`mysql_real_query()`](api-functions/mysql_real_query.md) for statements that contain binary data or null bytes).

## Code Example: ALTER TABLE

[ALTER TABLE](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) is a DDL operation that changes an existing table.

The following code demonstrates how to execute `ALTER TABLE` on the [example table](setup-for-examples.md):

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
         conn,                  // Connection
         "mariadb.example.net", // Host
         "db_user",             // User account
         "db_user_password",    // User password
         "test",                // Default database
         3306,                  // Port number
         NULL,                  // Path to socket file
         0                      // Additional options
      ))
   {
      fprintf(stderr, "Error connecting to Server: %s\n", mysql_error(conn));
      mysql_close(conn);
      exit(1);
   }

   // Execute the ALTER TABLE statement
   if (mysql_query(conn, "ALTER TABLE test.contacts RENAME COLUMN first_name TO f_name"))
   {
      fprintf(stderr, "Error altering table: %s\n", mysql_error(conn));
      mysql_close(conn);
      exit(1);
   }

   // Close the Connection
   mysql_close(conn);

   return 0;
}
```

Confirm the table was altered by using [MariaDB Client](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client) to execute a [DESCRIBE](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/describe) statement on the same table:

```sql
DESC contacts;
```

```sql
+-----------+--------------+------+-----+---------+----------------+
| Field     | Type         | Null | Key | Default | Extra          |
+-----------+--------------+------+-----+---------+----------------+
| id        | int(11)      | NO   | PRI | NULL    | auto_increment |
| f_name    | varchar(25)  | YES  |     | NULL    |                |
| last_name | varchar(25)  | YES  |     | NULL    |                |
| email     | varchar(100) | YES  |     | NULL    |                |
+-----------+--------------+------+-----+---------+----------------+
```

## Code Example: TRUNCATE TABLE

[TRUNCATE TABLE](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/truncate-table) is a DDL operation that deletes all data from an existing table.

To truncate the table instead, replace the `ALTER TABLE` statement in the code example above with:

```c
   if (mysql_query(conn, "TRUNCATE test.contacts"))
   {
      fprintf(stderr, "Error truncating table: %s\n", mysql_error(conn));
      mysql_close(conn);
      exit(1);
   }
```

The following query confirms that `TRUNCATE TABLE` deleted all rows from the [example table](setup-for-examples.md):

```sql
SELECT * FROM test.contacts;
```

```sql
Empty set (0.000 sec)
```

{% @marketo/form formId="4316" %}
