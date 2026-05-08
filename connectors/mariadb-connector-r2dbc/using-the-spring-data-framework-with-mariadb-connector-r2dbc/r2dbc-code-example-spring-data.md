---
description: >-
  Complete Java code example using MariaDB Connector/R2DBC with Spring Data
  R2DBC to query a MariaDB table via DatabaseClient and reactive
  StepVerifier result assertions.
---

# R2DBC Code Example (Spring Data)

## Overview

The following example uses the Spring Data R2DBC framework to select data from the table defined in [Setup for Example](setup-for-connector-r2dbc-examples-spring-data.md). Complete information on [using Connector/R2DBC with the Spring Data framework](./) is available.

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
             !SILO=ent!
             .host("192.0.2.1").port(3306)
             !SILO=sky!
             .host("example.skysql.net").port(5509)
             !END-SILO!
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
        client.execute("SELECT first_name FROM contact")
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
     } finally {
     }
  }
}
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>


{% @marketo/form formId="4316" %}
