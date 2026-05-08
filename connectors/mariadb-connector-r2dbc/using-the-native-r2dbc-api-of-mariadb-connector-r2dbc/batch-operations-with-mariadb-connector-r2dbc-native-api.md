---
description: >-
  Batch operations with the MariaDB Connector/R2DBC native API group
  multiple DML statements into a single io.r2dbc.spi.Batch to reduce
  per-statement network overhead.
---

# Batch Operations with MariaDB Connector/R2DBC (Native API)

Java developers can use MariaDB Connector/R2DBC to connect to MariaDB database products using the Reactive Relational Database Connectivity (R2DBC) API. R2DBC operations are non-blocking, which makes R2DBC more scalable than Java's standard JDBC API.

## Batch Operations

In cases where you need to execute multiple statements at a time, rather than a single statement, MariaDB Connector/R2DBC supports batch operations. With batch operations, you can group several statements together, which can improve performance.

With R2DBC, batch operations are performed using the following class:

| Class              | Description                |
| ------------------ | -------------------------- |
| io.r2dbc.spi.Batch | Executes batch operations. |

## Code Example: Batching DML

DML (Data Manipulation Language) refers to all SQL-data statements in the SQL standard (ISO/IEC 9075-2:2016). The following example shows how to use a batch operation to add data to the example table created in [Setup for Examples](setup-for-connector-r2dbc-examples-native-api.md) and return data from the table (batching operations do not permit binding parameters):

```java
//Module Imports
import org.mariadb.r2dbc.MariadbConnectionConfiguration;
import org.mariadb.r2dbc.MariadbConnectionFactory;
import io.r2dbc.spi.Batch;
import io.r2dbc.spi.Connection;
import reactor.core.publisher.Flux;

//Main Application Class
public class App {
     // Connection Configuration
     private static MariadbConnectionConfiguration conf;
     private static MariadbConnectionFactory connFactory;
     private static Connection conn;

     // Main Process
     public static void main(String[] args) {
         //Initialize Connection Factory
         initConnectionFactory();

         // Add and Select Contacts in a batch operation
         addAndSelectContacts();
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

         } catch (java.lang.IllegalArgumentException e) {
             System.err.println("Issue encountered while getting connection");
             e.printStackTrace();
         }
     }

     public static void addAndSelectContacts() {
         try {
             //Initialize a Connection
             conn = connFactory.create().block();
             //Create a Batch Object
             Batch batch = conn.createBatch();
             batch = batch.add("INSERT INTO test.contact (" + "first_name, last_name, email)  VALUES" + "('Kai', 'Devi', 'kai.devi@example.com'), "
                          + "('Lee', 'Wang', 'lee.wang@example.com'), " + "('Dani', 'Smith', 'dani.smith@example.com')").add("SELECT * FROM test.contact");

             for (String contact_entry : Flux.from(batch.execute()).flatMap( res -> res.map( (row, metadata) -> {
                     return String.format("- %s %s <%s>",
                         row.get(1, String.class), // Get First Name
                         row.get(2, String.class), // Get Last Name
                         row.get(3, String.class)); // Get Email
                     })).toIterable()) {
                 System.out.println(contact_entry);
             }
         }
         // Catch Exception
         catch (IllegalArgumentException e) {
             System.err.println("Issue running operation");
             e.printStackTrace();
         } finally {// Close Connection
             conn.close();
         }
     }
 }
```

## Example Output:

```
- Walker Percy <w.percy@example.com>
 - Flannery OConnor <f.oconnor@example.com>
 - Kate Chopin <k.chopin@example.com>
```

## Code Example: Batching DDL

DDL (Data Definition Language) refers to all SQL-schema statements in the SQL standard (ISO/IEC 9075-2:2016). The following example shows how to use a batch operation to duplicate the example table created in [Setup for Examples](setup-for-connector-r2dbc-examples-native-api.md) (batching operations do not permit binding parameters):

```java
//Module Imports
import org.mariadb.r2dbc.MariadbConnectionConfiguration;
import org.mariadb.r2dbc.MariadbConnectionFactory;
import io.r2dbc.spi.Batch;
import io.r2dbc.spi.Connection;
import reactor.core.publisher.Mono;

//Main Application Class
public class App {

   // Connection Configuration
   private static MariadbConnectionConfiguration conf;
   private static MariadbConnectionFactory connFactory;
   private static Connection conn;

  // Main Process
   public static void main(String[] args) {

      //Initialize Connection Factory
      initConnectionFactory();

      // Initialize the schema
      initializeSchema();

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

   public static void initializeSchema() {

      try {
         //Initialize a Connection
         conn = connFactory.create().block();

         //Create a Batch Object
         Batch batch = conn.createBatch();
         batch = batch.add("CREATE DATABASE IF NOT EXISTS test")
               .add("CREATE TABLE IF NOT EXISTS " +
                    "test.contact_copy (" +
                    "id INT PRIMARY KEY AUTO_INCREMENT," +
                     "first_name VARCHAR(50)," +
                     "last_name VARCHAR(50)," +
                     "email VARCHAR(250)" +
                     ") ENGINE=InnoDB")
               .add("INSERT INTO test.contact_copy SELECT * FROM test.contact");
         Mono.from(batch.execute()).subscribe();
      }
      // Catch Exception
      catch (IllegalArgumentException e) {
         System.err.println("Issue running operation");
         e.printStackTrace();
      }finally { // Close Connection
          conn.close();
      }
   }
}
```

Confirm that the batch operation was properly executed by using [MariaDB Client](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client) to execute a [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) statement against the [information\_schema.TABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables) table, and another against the newly created test.contact\_copy table:

```sql
SELECT TABLE_SCHEMA, TABLE_NAME, ENGINE
   FROM information_schema.TABLES
   WHERE TABLE_SCHEMA='test'
   AND TABLE_NAME='contact_copy';
```

```
+--------------+--------------+--------+
| TABLE_SCHEMA |  TABLE_NAME  | ENGINE |
+--------------+--------------+--------+
| test         | contact_copy | InnoDB |
+--------------+--------------+--------+
```

```sql
SELECT * FROM contact_copy;
```

```
+----+------------+-----------+------------------------+
| id | first_name | last_name | email                  |
+----+------------+-----------+------------------------+
| 1  | Kai        | Devi      | kai.devi@example.com   |
| 2  | Lee        | Wang      | lee.wang@example.com   |
| 3  | Dani       | Smith     | dani.smith@example.com |
+----+------------+-----------+------------------------+
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
