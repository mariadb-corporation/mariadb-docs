---
description: >-
  Spring Data R2DBC batch with MariaDB Connector/R2DBC loops over statements via
  DatabaseClient.execute, replacing the native io.r2dbc.spi.Batch class
  unavailable in this framework.
---

# Batch Operations with MariaDB Connector/R2DBC (Spring Data)

### Overview

Java developers can use MariaDB Connector/R2DBC to connect to MariaDB database products using the Reactive Relational Database Connectivity (R2DBC) API. R2DBC operations are non-blocking, which makes it more scalable than Java's standard JDBC API. MariaDB Connector/R2DBC can be used with the very popular Spring Data R2DBC framework, which can provide support for repositories, object mapping, and transaction management.

### Batch Operations

Spring Data R2DBC has no built-in support for batch operations as the native API does with the io.r2dbc.spi.Batch class. With Spring Data R2DBC, batch operations can be performed by looping over a List of SQL statements and invoking DatabaseClient.execute(String sql) for each SQL statement.

### Code Example: Batching DML and DDL

DML (Data Manipulation Language) refers to all SQL-data statements in the SQL standard (ISO/IEC 9075-2:2016), for example, [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete), [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert), [REPLACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/replace), [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select), and [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update).

DDL (Data Definition Language) refers to all SQL-schema statements in the SQL standard (ISO/IEC 9075-2:2016), for example [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table), [CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/tables/create-table), [DROP TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/tables/drop-table), [CREATE DATABASE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-database), and [TRUNCATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/truncate-table).

The following example shows how to use a batch operation to duplicate the example table created in [Setup for Examples](setup-for-connector-r2dbc-examples-spring-data.md):

```java
//Module Imports
import java.util.Arrays;
import java.util.List;
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

         // Create a list or batch of SQL statements
         List<String> batch = Arrays.asList(
               "CREATE DATABASE IF NOT EXISTS test;",
               "CREATE TABLE IF NOT EXISTS test.contact_copy(id INT PRIMARY KEY AUTO_INCREMENT,first_name VARCHAR(50),last_name VARCHAR(50),email VARCHAR(250)) ENGINE=InnoDB;",
               "INSERT INTO test.contact_copy SELECT * FROM test.contact;");

         //Run the batch of SQL statements
         batch.forEach(stmt -> client.execute(stmt)
               .fetch()
               .rowsUpdated()
               .as(StepVerifier::create)
               .expectNextCount(1)
               .verifyComplete());

      } catch (IllegalArgumentException e) {
         e.printStackTrace();
      } catch (io.r2dbc.spi.R2dbcNonTransientResourceException e) {
         e.printStackTrace();
      } finally {

      }
   }
}
```

After running the application App, confirm the table has been created:

```sql
USE test;
SHOW TABLES;
```

```
+----------------+
| Tables_in_test |
+----------------+
| contact        |
| contact_copy   |
+----------------+
```

```sql
DESCRIBE contact_copy;
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

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
