---
description: >-
  Spring Data repositories with MariaDB Connector/R2DBC use ReactiveCrudRepository
  and JavaConfig to implement reactive CRUD, with ApplicationConfig, Entity,
  Repository, and Service classes.
---

# Repositories with MariaDB Connector/R2DBC (Spring Data)

## Overview

Java developers can use MariaDB Connector/R2DBC to connect to MariaDB database products using the Reactive Relational Database Connectivity (R2DBC) API. R2DBC operations are non-blocking, which makes R2DBC more scalable than Java's standard JDBC API. MariaDB Connector/R2DBC can be used with the very popular Spring Data framework, which can provide support for repositories, object mapping, and transaction management.

Spring Data Repositories technology is an abstraction that implements a data access layer over the underlying datastore. Spring Data Repositories reduce the boilerplate code required to access a datastore. Spring Data repositories can be used with the MariaDB/R2DBC connector.

## Code Example: Example Application

The following example depends on the environment created in [Setup for Examples](setup-for-connector-r2dbc-examples-spring-data.md).

## Repository Classes Used

In the sections below, we will build an example application that uses a Spring Data Repository. Some annotations that scan packages for repository classes require that the classes be in a named package rather than the default package. The classes in this example application will be in the springdata package.

The example application contains the following classes:

| Class                                                                                                                      | Description                                                                    |
| -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| [springdata.ApplicationConfig](repositories-with-mariadb-connector-r2dbc-spring-data.md#create-a-javaconfig-configuration) | The JavaConfig configuration class that enables Spring Data repositories.      |
| [springdata.Contact](repositories-with-mariadb-connector-r2dbc-spring-data.md#adapting-the-entity)                         | The Entity class that models the table.                                        |
| [springdata.ContactRepository](repositories-with-mariadb-connector-r2dbc-spring-data.md#create-a-repository)               | The Repository interface.                                                      |
| [springdata.RepositoryService](repositories-with-mariadb-connector-r2dbc-spring-data.md#create-a-service)                  | The Service class that performs CRUD (Create, Read, Update Delete) operations. |

## Adapting the Entity

We will need to adapt the entity class [previously created](application-development-with-mariadb-connector-r2dbc-spring-data.md#code-example-create-an-entity) for Spring Data Repositories:

```java
package springdata;

// Imports the @Id annotation type, which demarcates an identifier.
//Module Imports
import org.springframework.data.annotation.Id;

// This is an Entity class
// It has the same name as the text.contact table
public class Contact {

   // The class members correspond to columns
   // in the test.contact table
   private int id;
   private String first_name;
   private String last_name;
   private String email;

   // Constructor
   public Contact() {
   }

   // Constructor
   public Contact(String first_name, String last_name, String email) {

      this.first_name = first_name;
      this.last_name = last_name;
      this.email = email;
   }

   // Constructor
   public Contact(int id, String first_name, String last_name, String email) {
      this.id = id;
      this.first_name = first_name;
      this.last_name = last_name;
      this.email = email;
   }

   // The @Id annotation indicates that this field
   // is the primary key column
   @Id
   public int getId() {
      return id;
   }

   public String getFirst_name() {
      return first_name;
   }

   public String getLast_name() {
      return last_name;
   }

   public String getEmail() {
      return email;
   }

   @Override
   public String toString() {
      return "Contact [id=" + id + ", first_name=" + first_name + ", last_name=" + last_name + ", email=" + email
            + "]";
   }
}
```

## The changes are:

* The entity class is in the springdata package instead of the default package. Spring Data Repositories require repository related classes and interfaces to be in a named package instead of the default package to be able to scan for them.
* The entity class includes a constructor that defines parameters for all the fields except the identifier id field. \* \* \* This constructor will be used to add new contacts in [Creating a Service Class](repositories-with-mariadb-connector-r2dbc-spring-data.md).
* The entity class also includes a no-args default constructor.

## Create a Repository

The org.springframework.data.repository.reactive.ReactiveCrudRepository interface is the entrypoint for Spring Data R2DBC repositories. The ReactiveCrudRepository interface is used for generic CRUD operations on a repository for a specific type. This repository follows reactive paradigms and uses Project Reactor types which are built on top of Reactive Streams.

The ReactiveCrudRepository interface provides methods listed in following table:

| Method                                          | Description                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| save(S entity)                                  | Saves a given entity. Returns a Mono for the saved entity. Use the returned instance for further operations as the save operation might have changed the entity instance completely. The save(S entity) method updates an existing entity if the Entity object arguments include the identifier field. The save(S entity) method adds a new entity if the Entity object arguments do not include the identifier field. |
| saveAll(Iterable ~~entities)~~                  | Saves all given entities. It returns a Flux emitting the saved entities.                                                                                                                                                                                                                                                                                                                                               |
| saveAll(Publisher ~~entityStream)~~             | Saves all given entities. It returns a Flux emitting the saved entities..                                                                                                                                                                                                                                                                                                                                              |
| findById(ID id)                                 | Retrieves an entity by its id. It returns a Mono emitting the entity with the given id or Mono.empty() if none found.                                                                                                                                                                                                                                                                                                  |
| findById(Publisher id)                          | Retrieves an entity by its id supplied by a Publisher. It returns a Mono emitting the entity with the given id or Mono.empty() if none found.                                                                                                                                                                                                                                                                          |
| findAll()                                       | Returns all instances of the type. It returns a Flux emitting all entities.                                                                                                                                                                                                                                                                                                                                            |
| findAllById(Iterable ids)                       | Returns all instances of the type T with the given ids. If some or all ids are not found, no entities are returned for these ids. Note that the order of elements in the result is not guaranteed. It returns a Flux emitting the found entities. The size can be equal or less than the number of given ids.                                                                                                          |
| findAllById(Publisher idStream)                 | Returns all instances of the type T with the given ids supplied by a Publisher. If some or all ids are not found, no entities are returned for these ids. Note that the order of elements in the result is not guaranteed. It returns a Flux emitting the found entities.                                                                                                                                              |
| count()                                         | Returns the number of entities available. It returns a Mono emitting the number of entities.                                                                                                                                                                                                                                                                                                                           |
| deleteById(ID id)                               | Deletes the entity with the given id. It returns a Mono signaling when operation has completed.                                                                                                                                                                                                                                                                                                                        |
| deleteById(Publisher id)                        | Deletes the entity with the given id supplied by a Publisher. It returns a Mono signaling when operation has completed.                                                                                                                                                                                                                                                                                                |
| delete(T entity)                                | Deletes a given entity. It returns a Mono signaling when operation has completed.                                                                                                                                                                                                                                                                                                                                      |
| deleteAll(Iterable\<? extends T> entities)      | Deletes the given entities. It returns a Mono signaling when operation has completed.                                                                                                                                                                                                                                                                                                                                  |
| deleteAll(Publisher\<? extends T> entityStream) | Deletes the given entities supplied by a Publisher. It returns a Mono signaling when operation has completed.                                                                                                                                                                                                                                                                                                          |
| deleteAll()                                     | Deletes all entities managed by the repository. It returns a Mono signaling when operation has completed.                                                                                                                                                                                                                                                                                                              |

The sample repository class is listed:

```java
package springdata;

//Module Imports
import reactor.core.publisher.Flux;
import org.springframework.data.r2dbc.repository.Query;
import org.springframework.data.repository.reactive.ReactiveCrudRepository;

// ReactiveCrudRepository<Contact, Integer>:
//   Entity Class: Contact
//   Data type of identifier: Integer
interface ContactRepository extends ReactiveCrudRepository<Contact, Integer> {

   // The Query annotation provides an SQL statement corresponding to the method
   @Query("select id, first_name, last_name, email from contact c where c.first_name = :first_name")
   Flux<Contact> findByFirstname(String firstname);

   @Query("select id, first_name, last_name, email from contact c where c.id = :id")
   Flux<Contact> findById(int id);
}
```

* The findByFirstname(String firstname) method finds entities matching a given first name.
* The findById(int id) method finds entities matching a given id.
* An implementation class for the ContactRepository interface is not provided as the Spring Data Repositories framework generates the implementation class as needed.

## Create a JavaConfig Configuration

A JavaConfig configuration class is used to enable Spring Data Repositories. A JavaConfig configuration class is a plain old Java object (POJO). A POJO is an ordinary Java object without any special constraints of Java object models or conventions. The sample configuration file used is listed:

```java
package springdata;

//Module Imports
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;
import org.springframework.data.r2dbc.config.AbstractR2dbcConfiguration;
import org.springframework.data.r2dbc.repository.config.EnableR2dbcRepositories;

import io.r2dbc.spi.ConnectionFactories;
import io.r2dbc.spi.ConnectionFactory;

@Configuration
@EnableR2dbcRepositories(basePackageClasses = ContactRepository.class)
@ComponentScan(basePackageClasses = RepositoryService.class)
class ApplicationConfig extends AbstractR2dbcConfiguration {
   @Bean
   public ConnectionFactory connectionFactory() {
      return ConnectionFactories.get("r2dbc:mariadb://connr2dbc_test:db_user_password@192.0.2.50:3306/test");
   }
}
```

* The configuration class ApplicationConfig extends the AbstractR2dbcConfiguration class and provides only one method connectionFactory(), which is used by the Spring Data Repositories framework to obtain a ConnectionFactory instance to the MariaDB database using a R2DBC driver
* The ApplicationConfig extends the AbstractR2dbcConfiguration class, which is the base class for Spring Data R2DBC configuration containing bean declarations that must be registered for Spring Data R2DBC.
* The ApplicationConfig class is annotated with @Configuration, which indicates that a class declares @Bean annotated methods and may be processed by the Spring container to generate bean definitions and service requests for those beans at runtime.
* The ApplicationConfig class is annotated with @EnableR2dbcRepositories, which indicates the reactive relational repositories should be activated using R2DBC. A base package class is specified as ContactRepository.class using the basePackageClasses annotation attribute. If no base package is configured through either value(), basePackages(), or basePackageClasses() it will scan the package of the annotated class.
* The ApplicationConfig class is annotated with @ComponentScan, which configures component scanning directives for use with @Configuration classes. A base package class is specified as RepositoryService.class using the basePackageClasses annotation attribute. With the @ComponentScan set, the RepositoryService.class is used within the Spring Data Repositories framework. If no base package is configured through either value(), basePackages(), or basePackageClasses() it will scan the package of the annotated class, which must be a named package and not the default package.
* The connectionFactory() method returns a ConnectionFactory instance and is annotated with @Bean to indicate that the method produces a bean to be managed by the Spring container. A new ConnectionFactory is created using the static method ConnectionFactories.get(String url).

The R2DBC Connection URL format is `r2dbc:driver[:protocol]://[user:password@]host[:port][/path][?option=value]`

## Create a Service

A service class is used to perform CRUD operations with the Spring Data R2DBC repository. The following develops a service application to test the Spring Data R2DBC repository:

```java
package springdata;

//Module Imports
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationContext;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;
import org.springframework.stereotype.Service;

import reactor.test.StepVerifier;

// The @Service annotation indicates that the class is a "Service".
// Spring Data Repositories framework auto-discovers the service class
// through classpath scanning because we have set the @ComponentScan
// annotation in ApplicationConfig to scan for RepositoryService.class.
@Service
public class RepositoryService {

   // The @Autowired annotation indicates that the field is to be autowired
   // by Spring's dependency injection facilities.
   @Autowired
   private static ContactRepository repository;

   // The ApplicationContext provides Bean factory methods for
   // accessing application components.
   private static ApplicationContext ctx;

   public static void main(String[] args) {

      try {
         // The AnnotationConfigApplicationContext class is a standalone application context,
         // accepting component classes as input, in particular @Configuration-annotated
         // classes such as the ApplicationConfig class we developed.
         ctx = new AnnotationConfigApplicationContext(ApplicationConfig.class);

         // Returns the bean instance that uniquely matches the ContactRepository.class
         repository = ctx.getBean(ContactRepository.class);
         RepositoryService repoService = new RepositoryService();
         repoService.crud();
      } catch (Exception e) {
         System.out.println();
      } finally {
         // ...
      }
   }

   public void crud() {

      // Print number of rows
      System.out.println("Number of contacts in database is " + repository.count().block());

      // Delete all data
      repository.deleteAll().block();

      // Print number of rows again
      System.out.println("Number of contacts in database is " + repository.count().block());

      // Insert one row
      // ID is auto-generated
      Contact contact = new Contact("John", "Smith", "john.smith@gmail.com");
      repository.save(contact)
         .as(StepVerifier::create)
         .expectNextCount(1)
         .verifyComplete();

      // Insert another row
      // ID is auto-generated
      contact = new Contact("Johnny", "Smith", "johnny.smith@gmail.com");
      repository.save(contact)
         .as(StepVerifier::create)
         .expectNextCount(1)
         .verifyComplete();

      // Insert another row
      // ID is auto-generated
      contact = new Contact("Joe", "Smith", "joe.smith@gmail.com");
      repository.save(contact)
         .as(StepVerifier::create)
         .expectNextCount(1)
         .verifyComplete();

      // Print all rows
      repository.findAll()
         .doOnNext(it -> System.out.println(it)).as(StepVerifier::create)
         .expectNextCount(3)
         .verifyComplete();

      // Print rows with first name "John"
      repository.findByFirstname("John")
         .doOnNext(it -> System.out.println(it))
         .as(StepVerifier::create)
         .expectNextCount(1)
         .verifyComplete();

      // Print row with ID 1
      repository.findById(1)
         .doOnNext(it -> System.out.println(it))
         .as(StepVerifier::create)
         .expectNextCount(1)
         .verifyComplete();

       // Update email for contact with id 1
      // ID is explicitly provided
      contact = new Contact(1, "John", "Smith", "johnsmith@gmail.com");
      repository.save(contact)
         .as(StepVerifier::create)
         .expectNextCount(1)
         .verifyComplete();

      // Print rows with first name "John"
      repository.findByFirstname("John")
         .doOnNext(it -> System.out.println(it))
         .as(StepVerifier::create)
         .expectNextCount(1)
         .verifyComplete();
   }
}
```

* To update an existing contact, create a Contact entity instance with the all-args constructor, which is the constructor that defines all fields including the identifier field id as parameters. Subsequently, call method `ReactiveCrudRepository.save(S entity)` to save the entity. To verify that the contact has been updated call the `ReactiveCrudRepository.findByFirstname` method.

## Test the Service

Run the service class `springdata.RepositoryService` and for the sample table data and the sample application the following output is made:

```
Number of contacts in database is 0
Number of contacts in database is 0
Contact [id=1, first_name=John, last_name=Smith, email=john.smith@example.com]
Contact [id=2, first_name=Johnny, last_name=Smith, email=johnny.smith@example.com]
Contact [id=3, first_name=Joe, last_name=Smith, email=joe.smith@example.com]
Contact [id=1, first_name=John, last_name=Smith, email=john.smith@example.com]
Contact [id=1, first_name=John, last_name=Smith, email=john.smith@example.com]
Contact [id=1, first_name=John, last_name=Smith, email=johnsmith@example.com]
```

Run a SQL query to verify the test.contact table data we started with got deleted and three new contacts are added:

```sql
SELECT * FROM test.contact;
```

```
+----+------------+-----------+---------------------------+
| id | first_name | last_name | email                     |
+----+------------+-----------+---------------------------+
|  1 | John       | Smith     | johnsmith@example.com     |
+----+------------+-----------+---------------------------+
|  2 | Johnny     | Smith     | johnny.smith@example.com  |
+----+------------+-----------+---------------------------+
|  3 | Joe        | Smith     | joe.smith@example.com     |
+----+------------+-----------+---------------------------+
```

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>


{% @marketo/form formId="4316" %}
