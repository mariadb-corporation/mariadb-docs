---
description: >-
  Use Spring Data JDBC repositories with GridGain 9 through the IgniteDialect —
  Maven setup, entities, repositories, custom queries, and pagination.
---

# GridGain With Spring Data

## Overview

Spring Data Framework provides a unified and widely used API that allows abstracting an underlying data storage from the application layer. Spring Data helps you avoid locking to a specific database vendor, making it easy to switch from one database to another with minimal efforts. GridGain supports Spring Data JDBC by implementing `IgniteDialect`.

{% hint style="info" %}
GridGain's Spring Data integration is based on Spring Data JDBC, not Spring Data JPA. This provides better performance and more predictable behavior, as it avoids the complexity and overhead of ORM frameworks.
{% endhint %}

## Prerequisites

- Java 17 or higher
- Spring Boot 3.0 or higher
- Spring Data JDBC 3.0 or higher

## Limitations

- GridGain does not auto-generate primary keys. You need to provide ID values explicitly.
- Locking clauses (`@Lock`) are not supported.
- Single query loading for related entities is not supported.
- Composite keys are not supported.

## Maven Configuration

Spring Data integration requires three dependencies:

- `spring-data-ignite` provides the SQL dialect for Ignite-compatible query generation;
- `spring-boot-starter-data-jdbc` provides the Spring Data JDBC framework.

The `pom.xml` example below shows how you can add spring support:

{% code title="pom.xml" %}
```xml
<repositories>
    <repository>
        <id>GridGain External Repository</id>
        <url>https://www.gridgainsystems.com/nexus/content/repositories/external</url>
    </repository>
</repositories>

<dependencies>
    <!-- GridGain Spring Data support -->
    <dependency>
        <groupId>org.gridgain</groupId>
        <artifactId>spring-data-ignite</artifactId>
        <version>9.1</version>
    </dependency>

    <!-- Spring Boot Starter for JDBC -->
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-data-jdbc</artifactId>
    </dependency>
</dependencies>
```
{% endcode %}

## Configuration

### Application Properties

Configure both the GridGain client connection and JDBC datasource in your `application.properties`:

{% code title="application.properties" %}
```properties
# JDBC datasource configuration
spring.datasource.url=jdbc:ignite:thin://127.0.0.1:10800
spring.datasource.driver-class-name=org.apache.ignite.jdbc.IgniteJdbcDriver
```
{% endcode %}

### Dialect Provider Registration

Spring Data JDBC needs to generate database-specific SQL for operations like pagination, identity columns, and certain functions. The `spring-data-ignite` artifact includes an `IgniteDialectProvider` that teaches Spring Data how to generate Ignite-compatible SQL.

The dialect provider is registered via Spring's SPI mechanism. Create the file `src/main/resources/META-INF/spring.factories` with the following content:

{% code title="spring.factories" %}
```properties
org.springframework.data.jdbc.repository.config.DialectResolver$JdbcDialectProvider=org.apache.ignite.data.IgniteDialectProvider
```
{% endcode %}

Without this configuration, Spring Data falls back to generic ANSI SQL, which works for basic queries but may fail for database-specific operations.

## Defining Entities

Define entity classes that map to GridGain tables. Use standard Spring Data annotations:

{% hint style="info" %}
The example below uses the @Id and @Table annotations from Spring. Make sure your IDE imports the correct annotation to avoid possible conflict with GridGain annotations.
{% endhint %}

{% code title="Person.java" %}
```java
import org.springframework.data.annotation.Id;
import org.springframework.data.relational.core.mapping.Table;

@Table("Person")
public class Person {

    @Id
    private Long id;
    private String firstName;
    private String lastName;
    private Integer age;

    // Constructors
    public Person() {}

    public Person(Long id, String firstName, String lastName, Integer age) {
        this.id = id;
        this.firstName = firstName;
        this.lastName = lastName;
        this.age = age;
    }

    // Getters and setters
    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }
}
```
{% endcode %}

{% hint style="warning" %}
The table referenced by the entity class must exist in the GridGain cluster before you start working with it. Spring Data does not automatically create tables.
{% endhint %}

Create the corresponding table in GridGain:

```sql
CREATE TABLE Person (
    id BIGINT PRIMARY KEY,
    firstName VARCHAR,
    lastName VARCHAR,
    age INT
);
```

## Defining Repositories

Define repository interfaces by extending Spring Data repository interfaces:

{% code title="PersonRepository.java" %}
```java
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;
import java.util.List;

@Repository
public interface PersonRepository extends CrudRepository<Person, Long> {

    // Derived query methods
    List<Person> findByFirstName(String firstName);

    // ...

}
```
{% endcode %}

Spring Data automatically implements these methods based on their names. No additional code is required.

## Using Repositories

Inject and use repositories in your Spring components:

{% code title="PersonService.java" %}
```java
@Service
public class PersonService {

    @Autowired
    private PersonRepository repository;

    public List<Person> findByFirstName(String firstName) {
        return repository.findByFirstName(firstName);
    }

    // ...
}
```
{% endcode %}

## Custom Queries

For complex queries that cannot be expressed through method names, use the `@Query` annotation:

{% code title="Java" %}
```java
@Repository
public interface PersonRepository extends CrudRepository<Person, Long> {

    @Query("SELECT * FROM Person WHERE age > :minAge AND lastName LIKE :pattern")
    List<Person> findByCustomQuery(@Param("minAge") Integer minAge,
                                    @Param("pattern") String pattern);

    @Query("SELECT * FROM Person WHERE firstName = ?1 OR lastName = ?2")
    List<Person> findByFirstOrLastName(String firstName, String lastName);

    @Query("SELECT COUNT(*) FROM Person WHERE age BETWEEN :minAge AND :maxAge")
    long countByAgeRange(@Param("minAge") Integer minAge,
                         @Param("maxAge") Integer maxAge);

    // Using positional parameters
    @Query("SELECT id FROM Person WHERE age > ?1 ORDER BY age DESC")
    List<Long> findIdsByAge(Integer minAge, Pageable pageable);
}
```
{% endcode %}

{% hint style="info" %}
Use named parameters (`:paramName`) or positional parameters (`?1`, `?2`) in your queries. Named parameters require the `@Param` annotation.
{% endhint %}

## Pagination and Sorting

GridGain supports pagination and sorting through Spring Data's standard interfaces:

### Sorting

{% code title="Java" %}
```java
@Repository
public interface PersonRepository extends CrudRepository<Person, Long> {

    // Method name-based sorting
    List<Person> findByLastNameOrderByAgeDesc(String lastName);

    // Using Sort parameter
    List<Person> findByLastName(String lastName, Sort sort);

    Iterable<Person> findAll(Sort sort);
}

// Usage
List<Person> persons = repository.findByLastName("Smith",
    Sort.by(Sort.Direction.DESC, "age"));

List<Person> allPersons = (List<Person>) repository.findAll(
    Sort.by("lastName").ascending()
        .and(Sort.by("firstName").ascending())
);
```
{% endcode %}

### Pagination

{% code title="Java" %}
```java
@Repository
public interface PersonRepository extends PagingAndSortingRepository<Person, Long>,
                                          CrudRepository<Person, Long> {

    // Page-based pagination
    Page<Person> findByLastName(String lastName, Pageable pageable);

    // Slice-based pagination (no total count)
    Slice<Person> findByFirstName(String firstName, Pageable pageable);
}

// Usage
@Service
public class PersonService {

    @Autowired
    private PersonRepository repository;

    public Page<Person> getPersonsPage(int page, int size) {
        Pageable pageable = PageRequest.of(page, size, Sort.by("lastName"));
        return repository.findByLastName("Smith", pageable);
    }

    public List<Person> getFirstPage() {
        Pageable pageable = PageRequest.of(0, 10);
        Page<Person> page = repository.findAll(pageable);

        System.out.println("Total elements: " + page.getTotalElements());
        System.out.println("Total pages: " + page.getTotalPages());
        System.out.println("Current page: " + page.getNumber());

        return page.getContent();
    }
}
```
{% endcode %}

{% hint style="info" %}
`Page` executes an additional count query to determine the total number of elements, while `Slice` does not. Use `Slice` for better performance when you don't need the total count.
{% endhint %}

## Authentication

When authentication is enabled on the GridGain cluster, configure credentials for both the client and JDBC connections:

{% code title="application.properties" %}
```properties
# GridGain client authentication
ignite.client.addresses=127.0.0.1:10800
ignite.client.auth.basic.username=myuser
ignite.client.auth.basic.password=mypassword

# JDBC datasource with authentication
spring.datasource.url=jdbc:ignite:thin://127.0.0.1:10800
spring.datasource.driver-class-name=org.apache.ignite.jdbc.IgniteJdbcDriver
spring.datasource.username=myuser
spring.datasource.password=mypassword
```
{% endcode %}
