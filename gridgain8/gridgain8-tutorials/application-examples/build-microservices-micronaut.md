---
description: >-
  Build a Micronaut microservice backed by an Apache Ignite in-memory database, then deploy the service and a two-node cluster in Docker.
---

# Build Microservices With Micronaut and Ignite

## Introduction

This tutorial walks you through the process of creating a simple Micronaut microservice that uses Apache Ignite as an in-memory database. The service provides information about the world's most populated cities by processing user HTTP requests and querying data from a distributed Ignite cluster. At the end of the tutorial, you deploy the microservice in Docker in your local environment. You can then easily launch the solution, with minimal changes, in a cloud environment.

You can find a complete implementation of the microservice [in the GitHub repository](https://github.com/GridGain-Demos/ignite-micronaut-demo). Depending on your preference, you can build the service from the ground up, learning about all the nuances, or you can download the GitHub project and run the finished implementation.

## Prerequisites

- **Java Development Kit**, version 8 or later
- **[Micronaut CLI](https://micronaut-projects.github.io/micronaut-starter/latest/guide/#installation)**
- **[Apache Maven 3.0](https://maven.apache.org)** or later
- **Docker 19** or later (install [Docker Desktop Community 2.3](https://www.docker.com/products/docker-desktop) or later for simplicity)
- **[Docker Compose 1.25](https://docs.docker.com/compose/install/)** or later
- Your favorite IDE, such as IntelliJ IDEA, or Eclipse

## What You Will Learn

- How to create an Ignite thin client singleton with Micronaut dependency injection
- How to expose a Micronaut controller that queries Ignite with SQL
- How to start a two-node Ignite cluster and load the World sample database
- How to deploy the microservice and cluster together in Docker

## Generate the Application Project

Start by creating a Maven project for the microservice implementation and accompanying Docker files.

To expedite this step, open a terminal window and use [Micronaut CLI](https://micronaut-projects.github.io/micronaut-starter/latest/guide/#installation) to generate a project structure:

```bash
mn create-app org.gridgain.demo.ignite-micronaut-demo -b=maven -l=java
```

Open the project with your favorite IDE and edit the `{project}/pom.xml` file by adding the `ignite-core` library to the list of the project dependencies:

```xml
<dependency>
  <groupId>org.apache.ignite</groupId>
  <artifactId>ignite-core</artifactId>
  <version>2.8.1</version>
</dependency>
```

## Create the Ignite Thin Client Singleton

Micronaut implements the [JSR-330: Dependency Injection for Java](http://javax-inject.github.io/javax-inject/) specification, which supports the `@Singleton` annotation. With that annotation, you can easily create a single instance of an Ignite thin client connection and share it across all your Micronaut controllers.

Add the following singleton implementation to the `{project}/src/main/java/org/gridgain/demo` folder:

```java
package org.gridgain.demo;

@Singleton
public class IgniteClientConnection {

    private IgniteClient client;

    @PostConstruct
    public void init() {
        ClientConfiguration cfg = new ClientConfiguration();

        cfg.setAddresses(Application.IGNITE_SERVER_ADDRESS);
        cfg.setPartitionAwarenessEnabled(true);

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

- The first inquiry to the singleton automatically calls the `init()` method. The method creates an instance of the Ignite thin client.
- The `cfg.setAddresses(Application.IGNITE_SERVER_ADDRESS)` parameter passes the IP address of an Ignite server node that the client needs to connect to. `Application.IGNITE_SERVER_ADDRESS` represents the environment variable that you are about to add to the application logic.
- The `cfg.setPartitionAwarenessEnabled(true)` setting enables the [partition-awareness feature of Ignite](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/thin-clients/getting-started-with-thin-clients#partition-awareness) that allows the thin client to send query requests directly to the node that owns the requested record. If your network is configured so that the client can communicate only to the server with the `Application.IGNITE_SERVER_ADDRESS` address, disable this property.

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

import io.micronaut.core.annotation.Introspected;

@Introspected
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

Complete the microservice implementation by adding the controller class into the `{project}/src/main/java/org/gridgain/demo` location:

```java
package org.gridgain.demo;

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

- The `@Inject IgniteClientConnection` client directive injects an instance of your Ignite thin client singleton during the controller-creation process.
- The `List<City> listCities(int population)` method intercepts user requests, queries data from Ignite and sends backs a sorted result.

## Start the Ignite Cluster and Load the Sample Database

In the last few sections of the tutorial, you deploy the whole solution, including an Ignite cluster and the just-completed Micronaut microservice in Docker. Start by adding the `ignite-cluster.yaml` Docker Compose configuration file into the project root folder:

```yaml
version: '3.7'
services:
  ignite_server_node:
    image: apacheignite/ignite:2.8.1
    environment:
      - IGNITE_WORK_DIR=/opt/ignite/work
    networks:
      - ignite_net
    volumes:
      - ../work:/opt/ignite/work

networks:
  ignite_net:
    driver: bridge
```

Bootstrap a two-node Ignite cluster and load the World database records:

1. Open a terminal window, navigate to the project root, and use the following Docker Compose command to launch the cluster:

   ```bash
   docker-compose -p cluster -f ignite-cluster.yaml up --scale ignite_server_node=2 -d
   ```
1. Connect to the first server node's container:

   ```bash
   docker exec -it cluster_ignite_server_node_1 bash
   ```
1. Once inside of the container, go to the `bin` folder of the Ignite installation directory:

   ```bash
   cd apache-ignite/bin/
   ```
1. Connect to the cluster with the SQLLine tool that was shipped with Ignite

   ```bash
   ./sqlline.sh --verbose=true -u jdbc:ignite:thin://127.0.0.1/
   ```
1. Create the World database schema and load the sample data by using the script that is shipped with every Ignite release:

   ```bash
   !run ../examples/sql/world.sql
   ```
1. Exit the container by closing the SQLLine connection (`!q`) and the bash session (`exit`).

## Build and Deploy the Micronaut Microservice

As with the cluster, you deploy the microservice in the Docker environment.

First, create a Docker image:

1. Go to the project's root folder and build the microservice with Maven:

   ```bash
   mvn clean package
   ```
1. Create a Docker image named `ignite-micronaut-app` (note, the project has the required Dockerfile, which was generated by Micronaut CLI):

   ```bash
   docker build -t ignite-micronaut-app .
   ```

Second, start the microservice from the image:

1. Get the IP address of the first server node:

   ```bash
   docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' cluster_ignite_server_node_1
   ```
1. Replace the `<YOUR_IP_ADDRESS>` parameter in the following command with the first server node's IP address and launch the service in Docker:

   ```bash
   docker run -p 8080:8080 --env igniteServerAddress=<YOUR_IP_ADDRESS>:10800 --name ignite-micronaut-app --network cluster_ignite_net ignite-micronaut-app
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
- Shutdown the Ignite cluster:

  ```bash
  docker-compose -p cluster -f ignite-cluster.yaml down
  ```

## Bonus Task

Create a similar application but deploy it as a [serverless function](https://docs.micronaut.io/latest/guide/#serverlessFunctions) in your favorite cloud environment. When the solution is workable, upload it to GitHub and claim an award by sending a [direct message to the tutorial author](https://twitter.com/denismagda).

## Related

- [Building Microservices With Micronaut and Apache Ignite](https://github.com/GridGain-Demos/ignite-micronaut-demo) for the complete reference implementation
