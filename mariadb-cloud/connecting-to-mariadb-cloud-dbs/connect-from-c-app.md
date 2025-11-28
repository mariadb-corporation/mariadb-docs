# Connect From C App

MariaDB Connector/C enables C and C++ applications to establish client connections to MariaDB Cloud over TLS. MariaDB Connector/C is a native connector that is written in C.

### First [Install MariaDB Connector/C](https://mariadb.com/docs/server/connect/programming-languages/c/install/)

MariaDB Connector/C enables C and C++ applications to establish client connections to MariaDB Cloud and MariaDB database products over TLS.

Additional information on MariaDB Connector/C is available in the [MariaDB Connector/C Documentation](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c).

## Connection Info

The connection is configured via the information that is initially acquired from the MariaDB Cloud Portal pages:

| Function               | Option/Argument | Where to find it                                                                                                      |
| ---------------------- | --------------- | --------------------------------------------------------------------------------------------------------------------- |
| mysql\_real\_connect() | host argument   | The fully Qualified Domain Name from the "Connect" window in the MariaDB Cloud portal                                 |
| mysql\_real\_connect() | user argument   | The desired username, which might be the default username in the Service Credentials view                             |
| mysql\_real\_connect() | passwd argument | The user's password, which might be the default password in the Service Credentials view if it was not yet customized |
| mysql\_real\_connect() | port argument   | The Read-Write Port or Read-Only Port from the "Connect" window in the MariaDB Cloud portal                           |

## Code Example

The following code demonstrates how to use MariaDB Connector/C to connect to SkySQL. This example uses the [example database and user account](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c/setup-for-examples):

```c
#include <stdio.h>
#include <stdlib.h>
#include <mysql.h>

int main (int argc, char* argv[])
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
         conn,                 // Connection
         "example.skysql.com", // Host
         "db_user",            // User account
         "db_user_password",   // User password
         "test",               // Default database
         3006,                 // Port number
         NULL,                 // Path to socket file
         0                     // Additional options
      ))
   {
      // Report the failed-connection error & close the handle
      fprintf(stderr, "Error connecting to Server: %s\n", mysql_error(conn));
      mysql_close(conn);
      exit(1);
   }

   // Use the Connection
   // ...

   // Close the Connection
   mysql_close(conn);

   return 0;
}
```
