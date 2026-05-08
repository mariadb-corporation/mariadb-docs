---
description: >-
  Spring Data R2DBC DML with MariaDB Connector/R2DBC uses DatabaseClient
  methods execute, select, insert, update, and delete for reactive INSERT,
  SELECT, UPDATE, and DELETE.
---

# DML with MariaDB Connector/R2DBC (Spring Data)

## Overview

Java developers can use MariaDB Connector/R2DBC to connect to MariaDB database products using the Reactive Relational Database Connectivity (R2DBC) API. R2DBC operations are non-blocking, which makes it more scalable than Java's standard JDBC API. MariaDB Connector/R2DBC can be used with the very popular Spring Data framework, which can provide support for repositories, object mapping, and transaction management.

## DML Operations

DML (Data Manipulation Language) refers to all SQL-data statements in the SQL standard (ISO/IEC 9075-2:2016), for example, [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete), [INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert), [REPLACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/replace), [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select), and [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update).

With Spring Data, DML operations can be performed by invoking the following methods:

| Method                             | Description                 |
| ---------------------------------- | --------------------------- |
| DatabaseClient.execute(String sql) | Execute any DML statement.  |
| DatabaseClient.select()            | Execute a SELECT statement. |
| DatabaseClient.insert()            | Execute a INSERT statement. |
| DatabaseClient.update()            | Execute a UPDATE statement. |
| DatabaseClient.delete()            | Execute a DELETE statement. |

## Code Example: INSERT, UPDATE, DELETE

[INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert), [UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/update), and [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) are DML (Data Manipulation Language) operations that modify the data in a table.

The following example shows how to insert data into the example table created in [Setup for Examples](setup-for-connector-r2dbc-examples-spring-data.md).

To update or delete data, replace the `INSERT` statement in the code example with an `UPDATE`, or `DELETE` statement:

```java
//Module Imports
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
         conf = MariadbConnectionConfiguration.builder()
              .host("192.0.2.1").port(3306)
              .username("db_user").password("db_user_password")
              .database("test").build();

         // Instantiate a Connection Factory
         connFactory = new MariadbConnectionFactory(conf);

         // Instantiate a Database Client
         client = DatabaseClient.create(connFactory);

         // Add First Contact
         client.insert()
            .into(Contact.class)
            .using(new Contact(1, "Kai", "Devi", "kai.devi@example.com"))
            .then()
            .as(StepVerifier::create)
            .verifyComplete();

         // Add Second Contact
         client.insert()
            .into(Contact.class)
            .using(new Contact(2, "Lee", "Wang", "kai.devi@example.com"))
            .then()
            .as(StepVerifier::create)
            .verifyComplete();

         // Add Third Contact
         client.insert()
            .into(Contact.class)
            .using(new Contact(3, "Dani", "Smith", "dani.smith@example.com"))
            .then()
            .as(StepVerifier::create)
            .verifyComplete();

      } catch (IllegalArgumentException e) {
         e.printStackTrace();
      } catch (io.r2dbc.spi.R2dbcNonTransientResourceException e) {
         e.printStackTrace();
      }
   }
}
```

* To update or delete data, use the update() or delete() methods, instead of the insert() method.
* To execute a specific DML statement, use the execute() method.

Confirm the data was properly inserted by using MariaDB Client to execute a `SELECT` statement.

Example output:

```sql
SELECT * FROM test.contact;
```

```
+----+------------+-----------+------------------------+
| id | first_name | last_name | email                  |
+----+------------+-----------+------------------------+
|  1 | John       | Smith     | john.smith@example.com |
+----+------------+-----------+------------------------+
```

## Code Example: SELECT

`SELECT` is a DML (Data Manipulation Language) operation that reads the data from a table.

The following example shows how to select data from the example table created in [Setup for Examples](setup-for-connector-r2dbc-examples-spring-data.md):

```java
//Module Imports
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
         conf = MariadbConnectionConfiguration.builder()
              .host("192.0.2.1").port(3306)
              .username("db_user").password("db_user_password")
              .database("test").build();

         // Instantiate a Connection Factory
         connFactory = new MariadbConnectionFactory(conf);

         // Instantiate a Database Client
         client = DatabaseClient.create(connFactory);

         // Select all rows
         client.select()
            .from(Contact.class)
            .fetch().all()
            .doOnNext(it -> System.out.println(it))
            .as(StepVerifier::create)
            .expectNextCount(3)
            .verifyComplete();

         // Select the first row
         client.select()
            .from(Contact.class)
            .fetch().first()
            .doOnNext(it -> System.out.println(it))
            .as(StepVerifier::create)
            .expectNextCount(1)
            .verifyComplete();

         // Select all rows with explicit query
         client.execute("SELECT id, first_name,last_name,email FROM contact")
            .as(Contact.class)
            .filter(s -> s.fetchSize(25))
            .fetch().all()
            .doOnNext(it -> System.out.println(it))
            .as(StepVerifier::create)
            .expectNextCount(3)
            .verifyComplete();

         // Select single column
         client.select()
            .from(Contact.class)
            .map((row, rowMetadata) -> row.get("first_name", String.class))
            .all()
            .doOnNext(it -> System.out.println(it))
            .as(StepVerifier::create)
            .expectNextCount(3)
            .verifyComplete();

      } catch (IllegalArgumentException e) {
         e.printStackTrace();
      } catch (io.r2dbc.spi.R2dbcNonTransientResourceException e) {
         e.printStackTrace();
      }
   }
}
```

Example output:

```java
//Output from first query
Contact [id=1, first_name=Kai, last_name=Devi, email=kai.devi@example.com]
Contact [id=2, first_name=Lee, last_name=Wang, email=lee.wang@example.com]
Contact [id=3, first_name=Dani, last_name=Smith, email=dani.smith@example.com]

//Output from second query
Contact [id=1, first_name=Kai, last_name=Devi, email=kai.devi@example.com]

//Output from third query
Contact [id=1, first_name=Kai, last_name=Devi, email=kai.devi@example.com]
Contact [id=2, first_name=Lee, last_name=Wang, email=lee.wang@example.com]
Contact [id=3, first_name=Dani, last_name=Smith, email=dani.smith@example.com]

//Output from fourth query
Kai
Lee
Dani
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
