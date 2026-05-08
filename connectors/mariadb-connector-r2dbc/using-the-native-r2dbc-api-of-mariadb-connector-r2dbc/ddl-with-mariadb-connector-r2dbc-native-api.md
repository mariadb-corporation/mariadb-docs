---
description: >-
  DDL operations with the MariaDB Connector/R2DBC native API execute schema
  statements such as CREATE TABLE and ALTER TABLE reactively using
  io.r2dbc.spi.Statement and io.r2dbc.spi.Result.
---

# DDL with MariaDB Connector/R2DBC (Native API)

## Overview

Java developers can use MariaDB Connector/R2DBC to connect to MariaDB database products using the Reactive Relational Database Connectivity (R2DBC) API. R2DBC operations are non-blocking, which makes R2DBC more scalable than Java's standard JDBC API.

DDL (Data Definition Language) refers to all SQL-schema statements in the SQL standard (ISO/IEC 9075-2:2016).

Some examples of DDL include [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table), [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table), [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table), [CREATE DATABASE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-database), and [TRUNCATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/numeric-functions/truncate).

## DDL Operations

With R2DBC, DDL statements are performed with the following classes:

| Class                  | Description                                   |
| ---------------------- | --------------------------------------------- |
| io.r2dbc.spi.Statement | Creates a statement to execute on the server. |
| io.r2dbc.spi.Result    | Contains the result-set from the server.      |

## Code Example: ALTER TABLE

ALTER TABLE is a DDL (Data Definition Language) operation that makes changes to an existing table. The following example changes the example table created in [Setup for Examples](setup-for-connector-r2dbc-examples-native-api.md).

```java
//Module Imports
import org.mariadb.r2dbc.MariadbConnectionConfiguration;
import org.mariadb.r2dbc.MariadbConnectionFactory;
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
      // Initialize Connection Factory
      initConnectionFactory();

      // Alter Contacts Table
      alterContactsTable();
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
         System.err.println("Issue encountered while creating  connection factory");
         e.printStackTrace();
      }
   }

   public static void alterContactsTable() {
      try {
         //Initialize a Connection
         conn = connFactory.create().block();

         //Create and run a Statement
         Mono.from(
            conn.createStatement("ALTER TABLE test.contact CHANGE COLUMN first_name f_name VARCHAR(25)").execute()
         ).subscribe();
      }
      // Catch Exception
      catch (java.lang.IllegalArgumentException e) {
         System.err.println("Issue altering contact table");
         e.printStackTrace();
      } finally {
         // Close Connection
         conn.close();
      }
   }
}
```

Confirm the table was properly altered by using MariaDB Client to execute a DESC statement on the same table:

```sql
DESC test.contact;
```

```
+-----------+-------------+------+-----+---------+----------------+
| Field     | Type        | Null | Key | Default | Extra          |
+-----------+-------------+------+-----+---------+----------------+
| id        | int(11)     | NO   | PRI | NULL    | auto_increment |
| f_name    | varchar(25) | YES  |     | NULL    |                |
| last_name | varchar(25) | YES  |     | NULL    |                |
| email     | varchar(25) | YES  |     | NULL    |                |
+-----------+-------------+------+-----+---------+----------------+
```

## Code Example: TRUNCATE TABLE

The following example shows how to truncate the example table created in [Setup for Examples](setup-for-connector-r2dbc-examples-native-api.md).

TRUNCATE is a DDL (Data Definition Language) operation that deletes all data from an existing table and resets the AUTO\_INCREMENT column counter to 0:

```java
//Module Imports
import org.mariadb.r2dbc.MariadbConnectionConfiguration;
import org.mariadb.r2dbc.MariadbConnectionFactory;
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

      // Truncate table
      truncateTable();
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
      } finally {
         // ...
      }
   }

   public static void truncateTable() {
      try {

         //Initialize a Connection
         conn = connFactory.create().block();

         // Initialize and run a Statement

         Mono.from(
            conn.createStatement("TRUNCATE test.contact").execute()
         ).subscribe();
      }
      // Catch Exception
      catch (java.lang.IllegalArgumentException e) {
         System.err.println("Issue truncating contact table");
         e.printStackTrace();
      } finally {
         // Close Connection
         conn.close();
      }
   }
}
```

Confirm the table was properly truncated by using MariaDB Client to execute a SELECT statement on the same table:

```sql
SELECT * FROM test.contact;
```

```
Empty set (0.000 sec)
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
