---
description: >-
  The MariaDB Connector/R2DBC native API supports connection pooling via
  r2dbc-pool, holding reactive connections open for reuse and configuring
  them with ConnectionPoolConfiguration.
---

# Connection Pools with MariaDB Connector/R2DBC (Native API)

Connection pools enable the reuse of database connections to minimize the performance overhead of connecting to the database and the churn of opening and closing connections.

Connection pools hold connections open in a pool. When the process is done with the connection, it is returned to the pool rather than closed, allowing MariaDB Connector/R2DBC to acquire a connection as needed.

Connection pools require [r2dbc-pool](https://github.com/r2dbc/r2dbc-pool). Refer to the [Installation](install-mariadb-connector-r2dbc.md) page for more details.

## Connection Pool Classes

Connection pools are created, used, and managed using several classes:

| Class                                            | Description                                               |
| ------------------------------------------------ | --------------------------------------------------------- |
| org.mariadb.r2dbc.MariadbConnectionFactory       | Creates client connections.                               |
| org.mariadb.r2dbc.MariadbConnectionConfiguration | Configures client connections for the connection factory. |
| io.r2dbc.pool.ConnectionPoolConfiguration        | Configures the connection pool.                           |
| io.r2dbc.pool.ConnectionPool                     | Implements the R2DBC connection pool.                     |
| io.r2dbc.spi.Connection                          | Implements the R2DBC client connection.                   |

## Code Example: Initialize Connection Pool

The following code example initializes a connection pool:

```java
// Module Imports
import java.time.Duration;
import io.r2dbc.pool.ConnectionPool;
import io.r2dbc.pool.ConnectionPoolConfiguration;
import org.mariadb.r2dbc.MariadbConnectionConfiguration;
import org.mariadb.r2dbc.MariadbConnectionFactory;

public class App {

   // Attributes
   private MariadbConnectionFactory connFactory;
   private ConnectionPool pool;

   // Main Process
   public static void main(String[] args) {

      App  app = new App();
      app.createConnectionPool();
   }

   public void createConnectionPool() {

      try {
         // Configure and Create Connection Factory
         MariadbConnectionConfiguration factoryConfig = MariadbConnectionConfiguration
            .builder().host("192.0.2.1").port(3306)
            .username("db_user").password("db_user_password")
            .database("test").build();

         this.connFactory = new MariadbConnectionFactory(factoryConfig);

         // Configure Connection Pool
         ConnectionPoolConfiguration poolConfig = ConnectionPoolConfiguration
            .builder(connFactory)
            .maxIdleTime(Duration.ofMillis(1000))
            .maxSize(20)
            .build();

         this.pool = new ConnectionPool(poolConfig);
      }
      // Catch Exception
       catch (IllegalArgumentException e) {
         System.err.println("Issue creating connection pool");
         e.printStackTrace();
      } finally {
         // Close Connection
         pool.close();
      }
   }
}
```

* The maxIdleTime(Duration maxIdleTime) method sets the maximum idle time. The value must not be null and must not be negative, though it could be 0. If the value is invalid, the method throws an IllegalArgumentException, which is handled in the catch block. The default value is 30 minutes.
* The maxSize(int maxSize) method sets the maximum connection pool size. The value must be greater than 0. If the value is invalid, the method throws an IllegalArgumentException, which is handled in the catch block. The default value is 10.

## Code Example: Retrieve Connections

When using a connection pool, you can retrieve connections from the connection pool using the create() method.

The following code example retrieves a connection from a connection pool. The code to initialize the connection pool is in [Initialize Connection Pools](connection-pools-with-mariadb-connector-r2dbc-native-api.md#code-example-initialize-connection-pool):

```java
// Module Imports
import java.time.Duration;
import io.r2dbc.pool.ConnectionPool;
import io.r2dbc.pool.ConnectionPoolConfiguration;
import org.mariadb.r2dbc.MariadbConnectionConfiguration;
import org.mariadb.r2dbc.MariadbConnectionFactory;
import io.r2dbc.spi.Connection;

public class App {

   // Attributes
   private MariadbConnectionFactory connFactory;
   private static ConnectionPool pool;
   private Connection conn;

   // Main Process
   public static void main(String[] args) {

     App app = new App();
      app.createConnectionPool();
      app.setConnection(pool);
   }

   public void createConnectionPool() {

      try {
         // Configure and Create Connection Factory
         MariadbConnectionConfiguration factoryConfig = MariadbConnectionConfiguration
            .builder().host("192.0.2.1").port(3306)
            .username("db_user").password("db_user_password")
            .database("test").build();

         this.connFactory = new MariadbConnectionFactory(factoryConfig);

         // Configure Connection Pool
         ConnectionPoolConfiguration poolConfig = ConnectionPoolConfiguration
            .builder(connFactory)
            .maxIdleTime(Duration.ofMillis(1000))
            .maxSize(20)
            .build();

         this.pool = new ConnectionPool(poolConfig);
      }
      // Catch Exception
       catch (IllegalArgumentException e) {
         System.err.println("Issue creating connection pool");
         e.printStackTrace();
      }
   }

   public void setConnection(ConnectionPool pool) {

      // Set Connection
      this.conn = pool.create().block();
      //Use Connection
      //...
   }
}
```

## Code Example: Close Connection

When you are done with a connection retrieved from the pool, close it using the close() method:

```java
// Return Connection to the Pool
conn.close();
```

Connections retrieved from connection pools are returned to the pool when closed. The pool keeps a certain pre-configured number of connections available for use. If a connection is retrieved with the create() method again, a connection from the pool is returned.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
