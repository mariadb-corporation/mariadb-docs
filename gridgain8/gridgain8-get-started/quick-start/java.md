---
description: >-
  Install GridGain, start a cluster, and run your first Java application, from
  system requirements and Maven setup to a Hello World compute example.
---

# GridGain Quick Start Guide for Java

This chapter explains system requirements for running GridGain, how to install GridGain, start a cluster and run a simple Hello World example.

Since GridGain is built on top of Apache Ignite, GridGain reuses Ignite's system properties, environment properties, startup scripts, etc. wherever possible.

{% hint style="info" %}
[Complimentary, Instructor-Led Developer Training - Apache Ignite Essentials](https://www.gridgain.com/products/services/training/apache-ignite-essentials)

If you are getting started with Ignite or GridGain, we recommend attending [an upcoming training session](https://www.gridgain.com/products/services/training#public-training-listing) to learn about the key design principles for building data-intensive applications.
{% endhint %}

## Prerequisites

{% include "../../.gitbook/includes/gg8-prereqs.md" %}

If you use Java version 11 or later, [Running GridGain with Java 11 or later](#running-gridgain-with-java-11-or-later) for details.

### (Optional) Open Ports

Depending on your environment and what your plan is, you may want to open additional ports. GridGain uses the following ports:

- 47100-47200 — ports used by GridGain nodes to communicate. Specific ports used depend on node configuration.
- 47500-47600 — ports used by GridGain nodes to discover other nodes in the network. Specific ports used depend on node configuration.
- 10800 — the port used for [thin clients]({connectors}/thin-clients/getting-started-with-thin-clients), [JDBC]({connectors}/sql/jdbc/jdbc-driver) and [ODBC]({connectors}/sql/odbc/odbc-driver) connections.
- 8080 — the port used for [REST API](../../reference/rest-api/README.md).
- 11211 — the port used by [control script](../../reference/cli-tool/README.md) calls. This port should only be opened on nodes that need to send control script messages to other nodes.

## Installing GridGain

{% include "../../.gitbook/includes/gg8-installggqsg.md" %}

## Starting a GridGain Node

{% include "../../.gitbook/includes/gg8-startinggg.md" %}

## Running Your First GridGain Application

Once the cluster is started, follow the steps below to run a simple HelloWorld example.

### 1. Add Maven Dependency

The easiest way to get started with GridGain in Java is to use Maven dependency management.

Create a new Maven project with your favorite IDE and add the following dependencies in your project's pom.xml file.

```xml
<properties>
    <gridgain.version>8.10</gridgain.version>
</properties>

<repositories>
    <repository>
        <id>GridGain External Repository</id>
        <url>https://www.gridgainsystems.com/nexus/content/repositories/external</url>
    </repository>
</repositories>

<dependencies>
    <dependency>
        <groupId>org.gridgain</groupId>
        <artifactId>ignite-core</artifactId>
        <version>${gridgain.version}</version>
    </dependency>
    <dependency>
        <groupId>org.gridgain</groupId>
        <artifactId>ignite-spring</artifactId>
        <version>${gridgain.version}</version>
    </dependency>
</dependencies>
```

### 2. HelloWorld.java

Here is a sample HelloWord.java file that prints 'Hello World' and some other environment details on all the server nodes of the cluster. The sample shows how to prepare a cluster configuration with Java APIs, create a sample cache with some data in it, and execute custom Java logic on the server nodes.

```java
public class HelloWorld {
    public static void main(String[] args) throws IgniteException {
        // Preparing IgniteConfiguration using Java APIs
        IgniteConfiguration cfg = new IgniteConfiguration();

        // The node will be started as a client node.
        cfg.setClientMode(true);

        // Classes of custom Java logic will be transferred over the wire from this app.
        cfg.setPeerClassLoadingEnabled(true);

        // Setting up an IP Finder to ensure the client can locate the servers.
        TcpDiscoveryMulticastIpFinder ipFinder = new TcpDiscoveryMulticastIpFinder();
        ipFinder.setAddresses(Collections.singletonList("127.0.0.1:47500..47509"));
        cfg.setDiscoverySpi(new TcpDiscoverySpi().setIpFinder(ipFinder));

        // Starting the node
        Ignite ignite = Ignition.start(cfg);

        // Create an IgniteCache and put some values in it.
        IgniteCache<Integer, String> cache = ignite.getOrCreateCache("myCache");
        cache.put(1, "Hello");
        cache.put(2, "World!");

        System.out.println(">> Created the cache and add the values.");

        // Executing custom Java compute task on server nodes.
        ignite.compute(ignite.cluster().forServers()).broadcast(new RemoteTask());

        System.out.println(">> Compute task is executed, check for output on the server nodes.");

        // Disconnect from the cluster.
        ignite.close();
    }

    /**
     * A compute tasks that prints out a node ID and some details about its OS and JRE.
     * Plus, the code shows how to access data stored in a cache from the compute task.
     */
    private static class RemoteTask implements IgniteRunnable {
        @IgniteInstanceResource
        Ignite ignite;

        @Override public void run() {
            System.out.println(">> Executing the compute task");

            System.out.println(
                "   Node ID: " + ignite.cluster().localNode().id() + "\n" +
                "   OS: " + System.getProperty("os.name") +
                "   JRE: " + System.getProperty("java.runtime.name"));

            IgniteCache<Integer, String> cache = ignite.cache("myCache");

            System.out.println(">> " + cache.get(1) + " " + cache.get(2));
        }
    }
}
```

{% hint style="info" %}
Don't forget to add imports for HelloWorld.java. It should be trivial as long as Maven solves all of the dependencies.

Plus, you might need to add these settings to your pom.xml if the IDE keeps using Java compiler from a version earlier than 1.8:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <configuration>
                <source>1.8</source>
                <target>1.8</target>
            </configuration>
        </plugin>
    </plugins>
</build>
```
{% endhint %}

### 3. Run HelloWorld.java

Run HelloWorld.java. You will see 'Hello World!' and other environment details printed on all the server nodes.

## Next Steps

From here, you may want to:

- Read more about using GridGain
- Use [GridGain Control Center]({tools}/control-center) to monitor your cluster

### Further Examples

{% include "../../.gitbook/includes/gg8-exampleprojects.md" %}

## Running GridGain with Java 11 or Later

{% include "../../.gitbook/includes/gg8-java9.md" %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
