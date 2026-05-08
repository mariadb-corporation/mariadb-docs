---
description: >-
  Spring Data R2DBC transactions with MariaDB Connector/R2DBC use
  R2dbcTransactionManager and TransactionalOperator for framework-managed
  reactive commit and rollback.
---

# Transactions with MariaDB Connector/R2DBC (Spring Data)

## Overview

Java developers can use MariaDB Connector/R2DBC to connect to MariaDB database products using the Reactive Relational Database Connectivity (R2DBC) API. R2DBC operations are non-blocking, which makes it more scalable than Java's standard JDBC API. MariaDB Connector/R2DBC can be used with the very popular Spring Data framework, which can provide support for repositories, object mapping, and transaction management.

## Transactions

With Spring Data, transactions can be used by utilizing either the R2dbcTransactionManager class or the TransactionAwareConnectionFactoryProxy class. These two classes are mutually exclusive, so they cannot be used together.

## Code Example: Transaction Manager

The following example shows how to perform some changes within a reactive streams transaction. The example uses the table created in [Setup for Examples](setup-for-connector-r2dbc-examples-spring-data.md) and the entity class created in [Create the Entity class](application-development-with-mariadb-connector-r2dbc-spring-data.md#code-example-create-an-entity).

```java
//Module Imports
import org.mariadb.r2dbc.MariadbConnectionConfiguration;
import org.mariadb.r2dbc.MariadbConnectionFactory;
import org.springframework.data.r2dbc.connectionfactory.R2dbcTransactionManager;
import org.springframework.data.r2dbc.core.DatabaseClient;
import org.springframework.transaction.ReactiveTransactionManager;
import org.springframework.transaction.reactive.TransactionalOperator;
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

         ReactiveTransactionManager tm = new R2dbcTransactionManager(connFactory);

         TransactionalOperator operator = TransactionalOperator.create(tm);

         // Instantiate a Client
         client = DatabaseClient.create(connFactory);

         // Update a contact using the transactional operator
         Contact contact = new Contact(1, "Kai", "Devi", "kai.devi@example.com");

         client.update()
         .table(Contact.class)
         .using(contact)
         .then()
         .as(operator::transactional)
         .as(StepVerifier::create)
         .verifyComplete();

         // Update another contact using the transactional operator
         client.execute("UPDATE test.contact SET email = 'lee.wang@example.com' WHERE id = 2")
         .fetch().rowsUpdated()
         .then()
         .as(operator::transactional)
         .as(StepVerifier::create)
         .expectComplete()
         .verify();

      } catch (IllegalArgumentException e) {
         // ...
      } finally {
         // ...
      }
   }
}
```

* The ReactiveTransactionManager is the central interface in Spring's reactive transaction infrastructure. Applications can use this directly, but it is not primarily meant as an API. Typically, it is recommended that applications use ReactiveTransactionManager with either transactional operators or declarative transaction demarcation through AOP. This example uses it with transactional operators.
* The R2dbcTransactionManager class is a ReactiveTransactionManager implementation for a single R2DBC ConnectionFactory. This class can be used in any environment with any R2DBC driver, as long as the setup uses a ConnectionFactory as its Connection factory mechanism. The R2dbcTransactionManager class assumes that a separate, independent Connection can be obtained even during an ongoing transaction.
* The TransactionalOperator is the Operator interface that simplifies programmatic transaction demarcation and transaction exception handling. The central method is transactional, which supports transactional wrapping of functional sequences code. This operator handles the transaction lifecycle and possible exceptions such that neither the ReactiveTransactionCallback implementation nor the calling code needs to explicitly handle transactions.

## Code Example: Proxy

The following example shows how to use the TransactionAwareConnectionFactoryProxy class, which is a proxy for a target R2DBC ConnectionFactory, adding awareness of Spring-managed transactions.

The main benefit of the proxy class is that it allows data access code to be used with either the plain R2DBC API or the DatabaseClient. The DatabaseClient gets transaction participation even without a proxy.

```java
//Module Imports
import org.mariadb.r2dbc.MariadbConnectionConfiguration;
import org.mariadb.r2dbc.MariadbConnectionFactory;
import org.springframework.data.r2dbc.connectionfactory.TransactionAwareConnectionFactoryProxy;
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

         TransactionAwareConnectionFactoryProxy proxy = new TransactionAwareConnectionFactoryProxy(connFactory);

         // Instantiate a Client
         client = DatabaseClient.create(proxy);

         // Update Data
         Contact contact = new Contact(1, "Kai", "Devi", "kai.devi@example.com");

         client.update().table(Contact.class).using(contact).then().as(StepVerifier::create).verifyComplete();

         client.execute("UPDATE test.contact SET email = 'lee.wang@example.com' WHERE id = 2").fetch().rowsUpdated()
         .then().as(StepVerifier::create).expectComplete().verify();

      } catch (IllegalArgumentException e) {
         // ...
      } finally {
         // ...
      }
   }
}
```

* The DatabaseClient is configured with the proxy connection factory that is aware of Spring managed transactions.
* The TransactionAwareConnectionFactoryProxy as a proxy must not be used when using the reactive streams transactions.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>


{% @marketo/form formId="4316" %}
