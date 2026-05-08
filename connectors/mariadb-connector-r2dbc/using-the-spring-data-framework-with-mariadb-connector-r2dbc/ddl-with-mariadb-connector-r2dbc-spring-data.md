---
description: >-
  Spring Data R2DBC DDL with MariaDB Connector/R2DBC uses
  DatabaseClient.execute to run schema statements including CREATE TABLE and
  ALTER TABLE within the Spring reactive framework.
---

# DDL with MariaDB Connector/R2DBC (Spring Data)

### Overview

Java developers can use MariaDB Connector/R2DBC to connect to MariaDB database products using the Reactive Relational Database Connectivity (R2DBC) API. R2DBC operations are non-blocking, which makes it more scalable than Java's standard JDBC API. MariaDB Connector/R2DBC can be used with the very popular Spring Data framework, which can provide support for repositories, object mapping, and transaction management.

### DDL Operations

DDL (Data Definition Language) refers to all SQL-schema statements in the SQL standard (ISO/IEC 9075-2:2016).

Some examples of DDL include [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table), [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table), [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/drop/drop-table), [CREATE DATABASE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-database), and [TRUNCATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/truncate-table).

With Spring Data, DDL operations can be performed by invoking the following methods:

| Method                             | Description                |
| ---------------------------------- | -------------------------- |
| DatabaseClient.execute(String sql) | Execute any DDL statement. |

### Code Example: CREATE TABLE

CREATE TABLE is a DDL (Data Definition Language) operation that creates a new table.

Complete the [Setup for Examples](setup-for-connector-r2dbc-examples-spring-data.md) and [Create the Entity class](application-development-with-mariadb-connector-r2dbc-spring-data.md#code-example-create-an-entity) before using the example.

The following example shows how to execute a CREATE TABLE statement:

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

         client.execute("CREATE OR REPLACE TABLE test.contact" + "(id INT PRIMARY KEY AUTO_INCREMENT,"
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

After running the application App, verify the table has been created:

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
DESC contact;
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

### Code Example: TRUNCATE TABLE

The following code example truncates the test.contact table created above.

`TRUNCATE` is a DDL (Data Definition Language) operation that deletes all data from an existing table and resets the `AUTO_INCREMENT` column counter to 0:

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

         // Truncate Database Table

         client.execute("TRUNCATE TABLE test.contact").fetch()
               .rowsUpdated().as(StepVerifier::create).expectNextCount(1).verifyComplete();
      } catch (IllegalArgumentException e) {
         e.printStackTrace();
      } catch (io.r2dbc.spi.R2dbcNonTransientResourceException e) {
         e.printStackTrace();
      } finally {
      }
   }

}
```

* A connection factory is used to create an instance of DatabaseClient to connect to the database.
* The `DROP` and `CREATE` privileges are needed to truncate a table as `TRUNCATE` is a DDL statement that drops the table and creates a new table with the same table definition, in effect deleting all data.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
