---
description: >-
  Connect a C or C++ application to MariaDB using Connector/C. Includes a
  complete code example demonstrating connection initialization,
  mysql_real_connect usage, and cleanup.
---

# Connect with MariaDB Connector/C

MariaDB Connector/C enables C and C++ applications to establish client connections to MariaDB database products over TLS.

## Code Example: Connect

The following code demonstrates how to use MariaDB Connector/C to connect to MariaDB database products. This example uses the [example database and user account](setup-for-examples.md):

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
         "mariadb.example.net",// Host
         "db_user",            // User account
         "db_user_password",   // User password
         "test",               // Default database
         3306,                 // Port number
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

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
