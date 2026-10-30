---
description: >-
  Build a Micronaut microservice backed by a GridGain in-memory database, then deploy the service and a two-node cluster in Docker.
---

# Build Microservices With Micronaut and GridGain

## Introduction

This tutorial walks you through the process of creating a simple Micronaut microservice that uses GridGain 8 as an in-memory database. The service provides information about the world's most populated cities by processing user HTTP requests and querying data from a distributed GridGain cluster. At the end of the tutorial, you deploy the microservice in Docker in your local environment. You can then easily launch the solution, with minimal changes, in a cloud environment.

## Prerequisites

- **Java Development Kit**, version 17 or later
- **[Micronaut CLI](https://micronaut-projects.github.io/micronaut-starter/latest/guide/#installation)**, version 4.10. This tutorial uses Micronaut 4.10, which builds on Java 17. Micronaut 5 build plugins require a newer Java (25).
- **[Apache Maven 3.9](https://maven.apache.org)** or later
- **[Docker](https://www.docker.com/products/docker-desktop)** with Docker Compose V2 (the `docker compose` command)
- **GridGain 8.10** trial license file (`gridgain-license.xml`) and the SQL script `examples/sql/world.sql`, both from the GridGain 8.10 binary distribution
- Your favorite IDE, such as IntelliJ IDEA, or Eclipse

## What You Will Learn

- How to create a GridGain thin client singleton with Micronaut dependency injection
- How to expose a Micronaut controller that queries GridGain with SQL
- How to start a two-node GridGain cluster and load the World sample database
- How to deploy the microservice and cluster together in Docker

## Generate the Application Project

Start by creating a Maven project for the microservice implementation and accompanying Docker files.

To expedite this step, open a terminal window and use [Micronaut CLI](https://micronaut-projects.github.io/micronaut-starter/latest/guide/#installation) to generate a project structure:

```bash
mn create-app org.gridgain.demo.ignite-micronaut-demo -b=maven -l=java
```

Open the project with your favorite IDE and edit the `{project}/pom.xml` file:

1. Add the GridGain repository next to the existing `central` repository:

   ```xml
   <repository>
     <id>GridGain External Repository</id>
     <url>https://www.gridgainsystems.com/nexus/content/repositories/external</url>
   </repository>
   ```

1. Add the `gridgain-core` library, which includes the thin client, to the list of the project dependencies:

   ```xml
   <dependency>
     <groupId>org.gridgain</groupId>
     <artifactId>gridgain-core</artifactId>
     <version>8.10.0</version>
   </dependency>
   ```

## Create the GridGain Thin Client Singleton

Micronaut implements the [JSR-330: Dependency Injection for Java](http://javax-inject.github.io/javax-inject/) specification, which supports the `@Singleton` annotation. With that annotation, you can easily create a single instance of a GridGain thin client connection and share it across all your Micronaut controllers.

Add the following singleton implementation to the `{project}/src/main/java/org/gridgain/demo` folder:

```java
package org.gridgain.demo;

import jakarta.annotation.PostConstruct;
import jakarta.annotation.PreDestroy;
import jakarta.inject.Singleton;
import org.apache.ignite.Ignition;
import org.apache.ignite.client.IgniteClient;
import org.apache.ignite.configuration.ClientConfiguration;

@Singleton
public class IgniteClientConnection {

    private IgniteClient client;

    @PostConstruct
    public void init() {
        ClientConfiguration cfg = new ClientConfiguration();

        cfg.setAddresses(Application.IGNITE_SERVER_ADDRESS);
        cfg.setAffinityAwarenessEnabled(true);

        client = Ignition.startClient(cfg);
    }

    public IgniteClient getClient() {
        return client;
    }

    @PreDestroy
    public void close() {
        try {
            client.close();
        }
        catch (Exception e) {
            e.printStackTrace();
        }
    }
}
```

- The first inquiry to the singleton automatically calls the `init()` method. The method creates an instance of the GridGain thin client.
- The `cfg.setAddresses(Application.IGNITE_SERVER_ADDRESS)` parameter passes the address of a GridGain server node that the client needs to connect to. `Application.IGNITE_SERVER_ADDRESS` represents the environment variable that you are about to add to the application logic.
- The `cfg.setAffinityAwarenessEnabled(true)` setting enables the [partition-awareness feature of GridGain](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/thin-clients/getting-started-with-thin-clients#partition-awareness) that allows the thin client to send query requests directly to the node that owns the requested record. If your network is configured so that the client can communicate only to the server with the `Application.IGNITE_SERVER_ADDRESS` address, disable this property.

Open `{project}/src/main/java/org/gridgain/demo/Application.java` class that Micronaut CLI generated and change its default implementation by adding the logic that is related to the `Application.IGNITE_SERVER_ADDRESS` variable:

```java
package org.gridgain.demo;

import io.micronaut.runtime.Micronaut;

public class Application {
    public static String IGNITE_SERVER_ADDRESS = "127.0.0.1:10800";

    public static void main(String[] args) {
        if (System.getenv("igniteServerAddress") != null)
            IGNITE_SERVER_ADDRESS = System.getenv("igniteServerAddress");

        Micronaut.run(Application.class, args);
    }
}
```

## Introduce the Micronaut Controller

The controller needs to respond to user requests that are in the `http://localhost:8080/cities?population=800000` format by returning all cities with a population that is equal to or greater than the population parameter.

Add `org.gridgain.demo.City` POJO class into the `{project}/src/main/java/org/gridgain/demo` folder that will be used by the controller's logic:

```java
package org.gridgain.demo;

import io.micronaut.serde.annotation.Serdeable;

@Serdeable
public class City {
    private Integer id;

    private String name;

    private String countryCode;

    private String district;

    private Integer population;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCountryCode() {
        return countryCode;
    }

    public void setCountryCode(String countryCode) {
        this.countryCode = countryCode;
    }

    public String getDistrict() {
        return district;
    }

    public void setDistrict(String district) {
        this.district = district;
    }

    public int getPopulation() {
        return population;
    }

    public void setPopulation(int population) {
        this.population = population;
    }
}
```

The `@Serdeable` annotation lets Micronaut Serialization convert `City` objects to JSON.

Complete the microservice implementation by adding the controller class into the `{project}/src/main/java/org/gridgain/demo` location:

```java
package org.gridgain.demo;

import io.micronaut.http.MediaType;
import io.micronaut.http.annotation.Controller;
import io.micronaut.http.annotation.Get;
import io.micronaut.http.annotation.Produces;
import jakarta.inject.Inject;
import java.util.ArrayList;
import java.util.List;
import org.apache.ignite.cache.query.FieldsQueryCursor;
import org.apache.ignite.cache.query.SqlFieldsQuery;

@Controller("/cities")
public class CityController {
    @Inject
    IgniteClientConnection client;

    @Get
    @Produces(MediaType.TEXT_JSON)
    public List<City> listCities(int population) {
        if (population <= 0)
            return null;

        FieldsQueryCursor<List<?>> cursor = client.getClient().query(
            new SqlFieldsQuery(
                "SELECT name, countryCode, population FROM City " +
                "WHERE population >= ? ORDER BY population DESC")
                .setSchema("PUBLIC")
                .setArgs(population));

        List<City> response = new ArrayList<>(cursor.getColumnsCount());

        for (List<?> row: cursor.getAll()) {
            City city = new City();

            city.setName((String)row.get(0));
            city.setCountryCode((String)row.get(1));
            city.setPopulation((Integer)row.get(2));

            response.add(city);
        }

        return response;
    }
}
```

- The `@Inject IgniteClientConnection` client directive injects an instance of your GridGain thin client singleton during the controller-creation process.
- The `List<City> listCities(int population)` method intercepts user requests, queries data from GridGain and sends backs a sorted result.

## Start the GridGain Cluster and Load the Sample Database

In the last few sections of the tutorial, you deploy the whole solution, including a GridGain cluster and the just-completed Micronaut microservice in Docker. Start by preparing three files in a `cluster` folder next to your project:

1. Copy your `gridgain-license.xml` file and the `examples/sql/world.sql` script from the GridGain 8.10 distribution to the `cluster` folder. The Docker image does not include the examples.
1. Add the `ignite-config.xml` file. The default multicast discovery does not connect nodes in a Docker bridge network, so the configuration lists the service name of the server nodes, which Docker resolves to every node container:

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <beans xmlns="http://www.springframework.org/schema/beans"
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          xsi:schemaLocation="http://www.springframework.org/schema/beans
          http://www.springframework.org/schema/beans/spring-beans.xsd">

       <bean class="org.apache.ignite.configuration.IgniteConfiguration">
           <property name="discoverySpi">
               <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
                   <property name="ipFinder">
                       <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                           <property name="addresses">
                               <list>
                                   <value>ignite_server_node:47500..47509</value>
                               </list>
                           </property>
                       </bean>
                   </property>
               </bean>
           </property>
       </bean>
   </beans>
   ```

1. Add the `ignite-cluster.yaml` Docker Compose configuration file:

   ```yaml
   services:
     ignite_server_node:
       image: gridgain/enterprise:8.10.0
       environment:
         - CONFIG_URI=/config/ignite-config.xml
       networks:
         - ignite_net
       volumes:
         - ./ignite-config.xml:/config/ignite-config.xml:ro
         - ./gridgain-license.xml:/opt/gridgain/gridgain-license.xml:ro
         - ./world.sql:/opt/gridgain/world.sql:ro

   networks:
     ignite_net:
       driver: bridge
   ```

Bootstrap a two-node GridGain cluster and load the World database records:

1. Open a terminal window, navigate to the `cluster` folder, and use the following Docker Compose command to launch the cluster:

   ```bash
   docker compose -p cluster -f ignite-cluster.yaml up --scale ignite_server_node=2 -d
   ```

1. Wait about half a minute, then check that the two nodes formed one cluster. Look for `servers=2` in the log of the second node:

   ```bash
   docker logs cluster-ignite_server_node-2 2>&1 | grep "Topology snapshot"
   ```

1. Connect to the first server node's container:

   ```bash
   docker exec -it cluster-ignite_server_node-1 bash
   ```

1. Once inside of the container, go to the `bin` folder of the GridGain installation directory:

   ```bash
   cd /opt/gridgain/bin
   ```

1. Connect to the cluster with the SQLLine tool that is shipped with GridGain:

   ```bash
   ./sqlline.sh --verbose=true -u jdbc:ignite:thin://127.0.0.1/
   ```

1. Create the World database schema and load the sample data by using the script that you mounted into the container:

   ```bash
   !run ../world.sql
   ```

1. Exit the container by closing the SQLLine connection (`!q`) and the bash session (`exit`).

## Build and Deploy the Micronaut Microservice

As with the cluster, you deploy the microservice in the Docker environment.

First, create a Docker image:

1. Go to the project's root folder and build the microservice with Maven:

   ```bash
   mvn clean package
   ```

1. Add a file named `Dockerfile` to the project's root folder. The GridGain thin client needs access to a JDK internal package (`java.nio`) on Java 17 and later, so the `java` command opens it:

   ```dockerfile
   FROM eclipse-temurin:17-jre
   COPY target/ignite-micronaut-demo-0.1.jar app.jar
   EXPOSE 8080
   ENTRYPOINT ["java", "--add-opens=java.base/java.nio=ALL-UNNAMED", "-jar", "app.jar"]
   ```

1. Create a Docker image named `ignite-micronaut-app`:

   ```bash
   docker build -t ignite-micronaut-app .
   ```

Second, start the microservice from the image in the same Docker network as the cluster. Use the `ignite_server_node` service name as the server address, so that you do not need to look up a container IP address:

```bash
docker run -p 8080:8080 --env igniteServerAddress=ignite_server_node:10800 --name ignite-micronaut-app --network cluster_ignite_net ignite-micronaut-app
```

## Query Most Populated Cities

Now your cluster and microservice are up-and-running and ready to process user requests.

Go ahead and request a list of the cities with a population equal to or greater than eight million by opening the following URL in a browser or with `curl`:

```bash
curl http://localhost:8080/cities?population=8000000
```

The response should be as follow:

```bash
[{"name":"Mumbai (Bombay)","countryCode":"IND","population":10500000},
{"name":"Seoul","countryCode":"KOR","population":9981619},
{"name":"São Paulo","countryCode":"BRA","population":9968485},
{"name":"Shanghai","countryCode":"CHN","population":9696300},
{"name":"Jakarta","countryCode":"IDN","population":9604900},
{"name":"Karachi","countryCode":"PAK","population":9269265},
{"name":"Istanbul","countryCode":"TUR","population":8787958},
{"name":"Ciudad de México","countryCode":"MEX","population":8591309},
{"name":"Moscow","countryCode":"RUS","population":8389200},
{"name":"New York","countryCode":"USA","population":8008278}]
```

Play with the `population` parameter to get cities with different populations.

## Terminate the Microservice and the Cluster

Use the following commands to shut down the demo and free up resources:

- Stop the Micronaut microservice:

  ```bash
  docker container stop ignite-micronaut-app
  ```
- If you're not planning to bring the service back later, remove the application container:

  ```bash
  docker container rm ignite-micronaut-app
  ```
- Shutdown the GridGain cluster:

  ```bash
  docker compose -p cluster -f ignite-cluster.yaml down
  ```

## Bonus Task

Create a similar application but deploy it as a [serverless function](https://docs.micronaut.io/latest/guide/#serverlessFunctions) in your favorite cloud environment. When the solution is workable, upload it to GitHub and claim an award by sending a [direct message to the tutorial author](https://twitter.com/denismagda).
