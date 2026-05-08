---
description: >-
  Connecting to MariaDB with the native R2DBC API uses
  MariadbConnectionConfiguration and MariadbConnectionFactory to create and
  manage reactive client connections via io.r2dbc.spi.Connection.
---

# Connect with MariaDB Connector/R2DBC (Native API)

Java developers can use MariaDB Connector/R2DBC to establish client connections with MariaDB database products.

## Code Example: Connect

Connections are created, used, and managed using the following Java classes:

| Class                                            | Description                                               |
| ------------------------------------------------ | --------------------------------------------------------- |
| org.mariadb.r2dbc.MariadbConnectionFactory       | Creates client connections.                               |
| org.mariadb.r2dbc.MariadbConnectionConfiguration | Configures client connections for the connection factory. |
| io.r2dbc.spi.Connection                          | Implements the R2DBC client connection.                   |

The following code example connects to a server using the database and user account created in [Setup for Examples](setup-for-connector-r2dbc-examples-native-api.md):

```java
// Module Imports
import org.mariadb.r2dbc.MariadbConnectionConfiguration;
import org.mariadb.r2dbc.MariadbConnectionFactory;
import io.r2dbc.spi.Connection;

// Main Application Class
public class App {
   // Connection Configuration
   private static MariadbConnectionConfiguration conf;
   private static MariadbConnectionFactory connFactory;
   private static Connection conn;

   // Main Process
   public static void main(String[] args) {
      //Initialize Connection Factory
      initConnectionFactory();

     //Initialize a Connection
     conn = connFactory.create().block();

      // Use the connection
      //conn.
   }

   public static void initConnectionFactory() {
      try {
         // Configure the Connection
         conf = MariadbConnectionConfiguration.builder()
              .host("192.0.2.1").port(3306)
              .username("db_user").password("db_user_password")
              .database("test").build();

         // Instantiate a Connection Factory
         connFactory = new MariadbConnectionFactory(conf);

      }
      catch (java.lang.IllegalArgumentException e) {
         System.err.println("Issue encountered while getting connection");
         e.printStackTrace();
      }
   }
}
```

* The connection must be configured for either host/port or socket, but it cannot be configured for both host/port and socket.
* For maximum portability, connections should be used synchronously.
* Objects created by a connection are only valid as long as the connection remains open.
* When configuring a connection, R2DBC applications should use the appropriate methods such as beginTransaction(), setAutoCommit(boolean), and setTransactionIsolationLevel(IsolationLevel) to change transaction properties. Applications should not execute SQL commands directly to change the connection configuration when a R2DBC method is available.
* New connections are by default created in auto-commit mode.
* When you are done with a connection, close it to free resources. Close the connection using the close() method.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
