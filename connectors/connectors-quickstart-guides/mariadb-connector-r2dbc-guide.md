---
description: Quickstart guide for MariaDB Connector/R2DBC
---

# MariaDB Connector/R2DBC Guide

MariaDB Connector/R2DBC allows Java developers to connect to MariaDB and MySQL databases using the Reactive Relational Database Connectivity (R2DBC) API. This enables non-blocking, asynchronous database operations, which are beneficial for building scalable and responsive applications.

#### 1. Installation

Add the necessary dependency to your project's `pom.xml` (Maven) or `build.gradle` (Gradle) file. Choose the dependency based on the R2DBC Specification you are targeting.

**a. For R2DBC 1.0.0 Specification (Recommended for new projects):**

XML

```xml
<dependency>
    <groupId>org.mariadb</groupId>
    <artifactId>r2dbc-mariadb</artifactId>
    <version>1.4.1</version> </dependency>
```

Gradle

```gradle
// Gradle
implementation 'org.mariadb:r2dbc-mariadb:1.4.1' // Use the latest stable version
```

**b. For R2DBC 0.9.1 Specification (for compatibility):**

XML

```xml
<dependency>
    <groupId>org.mariadb</groupId>
    <artifactId>r2dbc-mariadb-0.9.1-spec</artifactId>
    <version>1.4.1</version> </dependency>
```

Gradle

```gradle
// Gradle
implementation 'org.mariadb:r2dbc-mariadb-0.9.1-spec:1.4.1' // Use the latest stable version
```

#### 2. Basic Usage (Native R2DBC)

This example demonstrates how to establish a connection, execute a query, and process results using the reactive API.

Code snippet

```java
import io.r2dbc.spi.ConnectionFactories;
import io.r2dbc.spi.ConnectionFactory;
import io.r2dbc.spi.ConnectionFactoryOptions;
import io.r2dbc.spi.Connection;
import io.r2dbc.spi.Result;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

import static io.r2dbc.spi.ConnectionFactoryOptions.DATABASE;
import static io.r2dbc.spi.ConnectionFactoryOptions.DRIVER;
import static io.r2dbc.spi.ConnectionFactoryOptions.HOST;
import static io.r2dbc.spi.ConnectionFactoryOptions.PASSWORD;
import static io.r2dbc.spi.ConnectionFactoryOptions.PORT;
import static io.r2dbc.spi.ConnectionFactoryOptions.USER;
import org.mariadb.r2dbc.MariadbConnectionConfiguration;
import org.mariadb.r2dbc.MariadbConnectionFactory;

public class MariaDBR2DBCQuickstart {

    public static void main(String[] args) {
        // Option 1: Using ConnectionFactoryOptions Builder (Recommended for explicit configuration)
        MariadbConnectionConfiguration conf = MariadbConnectionConfiguration.builder()
                .host("localhost")
                .port(3306)
                .username("your_username")
                .password("your_password")
                .database("your_database_name")
                .build();
        ConnectionFactory factory = new MariadbConnectionFactory(conf);

        // Option 2: Using a R2DBC Connection URL
        // ConnectionFactory factory = ConnectionFactories.get("r2dbc:mariadb://your_username:your_password@localhost:3306/your_database_name");

        Mono<Connection> connectionMono = Mono.from(factory.create());

        // --- Example: Select Data ---
        connectionMono
            .flatMapMany(connection ->
                Flux.from(connection.createStatement("SELECT id, name FROM your_table_name WHERE status = ?")
                                   .bind(0, "active") // Bind parameter by index
                                   .execute())
                    .flatMap(result -> result.map((row, rowMetadata) -> {
                        int id = row.get("id", Integer.class);
                        String name = row.get("name", String.class);
                        return "ID: " + id + ", Name: " + name;
                    }))
                    .doFinally(signalType -> Mono.from(connection.close()).subscribe()) // Close connection when done
            )
            .doOnNext(System.out::println) // Print each row
            .doOnError(Throwable::printStackTrace) // Handle errors
            .blockLast(); // Block to ensure the main thread waits for completion (for quickstart example)


        // --- Example: Insert Data ---
        connectionMono
            .flatMap(connection ->
                Mono.from(connection.createStatement("INSERT INTO your_table_name (name, status) VALUES (?, ?)")
                                   .bind(0, "New Item")
                                   .bind(1, "pending")
                                   .execute())
                    .flatMap(Result::getRowsUpdated) // Get number of affected rows
                    .doFinally(signalType -> Mono.from(connection.close()).subscribe()) // Close connection
            )
            .doOnNext(rowsUpdated -> System.out.println("Rows inserted: " + rowsUpdated))
            .doOnError(Throwable::printStackTrace)
            .block(); // Block for simplicity in quickstart


        System.out.println("MariaDB R2DBC operations completed.");
    }
}
```

**Before Running:**

1. Replace `your_username`, `your_password`, `your_database_name`, and `your_table_name` with your actual MariaDB server details.
2. Ensure you have a MariaDB server running and a database/table set up.
3. Add `reactor-core` dependency if not already present, as R2DBC heavily relies on Project Reactor.

#### 3. Connection Strings

MariaDB Connector/R2DBC supports a standard R2DBC URL format for connection:

`r2dbc:mariadb://[username[:password]@]host[:port][/database][?option=value]`

Example:

r2dbc:mariadb://user:pass@localhost:3306/mydb?useBatchMultiSend=true

#### 4. Spring Data R2DBC

MariaDB Connector/R2DBC also integrates seamlessly with the Spring Data R2DBC framework, providing a higher-level abstraction for reactive database access, including repositories and entity mapping.

#### Further Resources:

* [MariaDB Connector/R2DBC GitHub Repository](https://github.com/mariadb-corporation/mariadb-connector-r2dbc)
* [R2DBC Specification](https://r2dbc.io/spec/)
* [Spring Data R2DBC Documentation](https://www.google.com/search?q=https://docs.spring.io/spring-data/relational/reference/r2dbc/index.html\&authuser=1)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
