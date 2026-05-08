---
description: >-
  MariaDB Connector/R2DBC Spring Data wraps MariadbConnectionFactory in
  DatabaseClient, providing a higher-level reactive interface for executing
  queries against MariaDB.
---

# Connect with MariaDB Connector/R2DBC (Spring Data)

## Overview

Java developers can use MariaDB Connector/R2DBC to establish client connections with MariaDB database products.

## Creating a Database Client

Connections are created, used, and managed using several classes:

| Class                                              | Description                                                   |
| -------------------------------------------------- | ------------------------------------------------------------- |
| org.mariadb.r2dbc.MariadbConnectionFactory         | Creates client connections.                                   |
| org.mariadb.r2dbc.MariadbConnectionConfiguration   | Configures client connections for the connection factory.     |
| io.r2dbc.spi.Connection                            | Implements the R2DBC client connection.                       |
| org.springframework.data.r2dbc.core.DatabaseClient | Creates a higher level, reactive client for Reactive Streams. |

## Code Example: Connect

The following example shows how to use the DatabaseClient class to connect and execute queries:

```java
// Module Imports
import org.mariadb.r2dbc.MariadbConnectionConfiguration;
import org.mariadb.r2dbc.MariadbConnectionFactory;
import org.springframework.data.r2dbc.core.DatabaseClient;

import reactor.test.StepVerifier;

// Main Application Class
public class App {

   // Connection Configuration
   private static MariadbConnectionConfiguration conf;
   private static MariadbConnectionFactory connFactory;
   private static DatabaseClient client;

   // Main Process
   public static void main(String[] args) {

      try {
         // Configure the Connection
         conf = MariadbConnectionConfiguration.builder()
              .host("192.0.2.1").port(3306)
              .username("db_user").password("db_user_password")
              .database("test").build();

         // Instantiate a Connection Factory
         connFactory = new MariadbConnectionFactory(conf);

         // Instantiate a Database Client
         client = DatabaseClient.create(connFactory);

         // Create a Database Table

         client.execute("CREATE TABLE IF NOT EXISTS test.contact" + "(id INT PRIMARY KEY AUTO_INCREMENT,"
               + "first_name VARCHAR(25)," + "last_name VARCHAR(25)," + "email VARCHAR(25)) ENGINE=InnoDB")
               .fetch()
               .rowsUpdated()
               .as(StepVerifier::create)
               .expectNextCount(1)
               .verifyComplete();

      } catch (IllegalArgumentException e) {
         e.printStackTrace();
      } catch (io.r2dbc.spi.R2dbcNonTransientResourceException e) {
         e.printStackTrace();
      } finally {

      }
   }
}
```

After running the application App, verify that the table has been created:

```sql
SHOW TABLES;
```

```
+----------------+
| Tables_in_test |
+----------------+
| contact        |
+----------------+
```

```sql
DESCRIBE contact;
```

```
+------------+-------------+------+-----+--------------------------+
| Field      | Type        | Null | Key | Default  | Extra         |
+------------+-------------+------+-----+----------+---------------+
| id         | int(11)     | NO   | PRI | NULL     | auto_increment|
| first_Name | varchar(25) | YES  |     | NULL     |               |
| last_Name  | varchar(25) | YES  |     | NULL     |               |
| email      | varchar(25) | YES  |     | NULL     |               |
+------------+-------------+------+-----+----------+---------------+
```

## Connection Pools

A `DatabaseClient` uses the underlying `ConnectionFactory` to get and release connections for each database operation without affinity to a particular connection across the multiple operations. When using Spring's R2DBC layer, a custom connection pool could be configured using an implementation provided by a third party.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>


{% @marketo/form formId="4316" %}
