---
description: >-
  How to start and manage a GridGain 9 cluster from a Java project using
  embedded mode.
---

# Starting With Embedded Mode

In most scenarios, you would use GridGain CLI tool to start and manage your GridGain cluster. However, in some scenarios it is preferable to manage the cluster from a Java project. Starting and working with the cluster from code is called "embedded mode".

This tutorial covers how you can start GridGain 9 from your Java project.

{% hint style="info" %}
Unlike in GridGain 8, nodes in GridGain 9 are not separated into client and server nodes. Nodes started from embedded mode will be used to store data by default.
{% endhint %}

## Prerequisites

{% include "../../.gitbook/includes/prereqs-java.md" %}

## Add GridGain to Your Project

First, you need to add GridGain to your project. The easiest way to do this is by using Maven:

```xml
<build>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <configuration>
                <source>11</source>
                <target>11</target>
            </configuration>
        </plugin>
    </plugins>
</build>

<repositories>
    <repository>
        <id>GridGain External Repository</id>
        <url>https://maven.gridgain.com/nexus/content/repositories/external</url>
    </repository>
</repositories>

<dependencies>
    <dependency>
        <groupId>org.gridgain</groupId>
        <artifactId>ignite-api</artifactId>
        <version>9.1</version>
    </dependency>

    <dependency>
        <groupId>org.gridgain</groupId>
        <artifactId>ignite-runner</artifactId>
        <version>9.1</version>
    </dependency>
</dependencies>
```

## Prepare GridGain Configuration

To start a GridGain node, you will need to provide a configuration file. For this tutorial, you can [download](https://gridgain.com/sdk/gridgain9/9.1/gridgain-config.conf) a simple configuration file, but in real environments we recommend creating one that suits your needs. For more information on node configuration, see [node configuration parameters](../administrators-guide/config/node-config.md) documentation.

## Pass Additional JVM Parameters

The following JVM parameters must be passed to your application to make proprietary SDK APIs available. These parameters are required for all supported Java versions:

```
--add-opens=java.base/java.lang=ALL-UNNAMED
--add-opens=java.base/java.lang.invoke=ALL-UNNAMED
--add-opens=java.base/java.lang.reflect=ALL-UNNAMED
--add-opens=java.base/java.io=ALL-UNNAMED
--add-opens=java.base/java.nio=ALL-UNNAMED
--add-opens=java.base/java.math=ALL-UNNAMED
--add-opens=java.base/java.util=ALL-UNNAMED
--add-opens=java.base/java.time=ALL-UNNAMED
--add-opens=java.base/jdk.internal.misc=ALL-UNNAMED
--add-opens=java.base/jdk.internal.access=ALL-UNNAMED
--add-opens=java.base/sun.nio.ch=ALL-UNNAMED
--add-opens=java.base/sun.security.x509=ALL-UNNAMED
-Dio.netty.tryReflectionSetAccessible=true
-ea
```

## Start GridGain Server Nodes

To start a GridGain node, use the following code snippet:

```java
Path myConfig = Path.of("conf/gridgain-config.conf");
Path myWorkDir = Path.of("/home/gridgain");

IgniteServer node = IgniteServer.start("node", myConfig, myWorkDir);
```

This code snippet starts a GridGain node with the name `node` that uses the configuration from the file specified in the `configPath` parameter and stores data in the folder specified in the `workDir` parameter. When the node is started, this method returns an instance of `IgniteServer` class that can be used to work with the node.

### Passing Configuration as String

Alternatively, you can pass the configuration as a string in the `start()` method. This way, you do not need a separate configuration file, however node configuration will be locked to the one provided at node start.

{% hint style="warning" %}
When starting the node with a configuration provided in a string, the node configuration will be read-only. To update it, restart the node with the new configuration.
{% endhint %}

```java
Path myWorkDir = Path.of("/home/gridgain");

IgniteServer node = IgniteServer.start("node", "{\"ignite\":{\"network\":{\"port\":3344,\"nodeFinder\":{\"netClusterNodes\":[\"localhost:3344\"]}}}}", myWorkDir);
```

## Initiate a Cluster

Started nodes find each other by default, but they do not form an intractable cluster unless the cluster is initiated. You need to initiate the cluster to activate the node. If there are multiple nodes, once the cluster is activated, they will form a topology and automatically distribute workload between each other.

Use the code snippet below to initiate a cluster:

```java
String license = Files.readString(Path.of("conf/license.conf"));

InitParameters initParameters = InitParameters.builder()
    .metaStorageNodeNames("node")
    .clusterName("cluster")
    .license(license)
    .build();

node.initCluster(initParameters);
```

{% hint style="info" %}
Provide your license by using the `license()` method, which accepts the contents of the license file, not a path to it. Use the `clusterConfiguration()` method for cluster configuration.
{% endhint %}

## Get an Ignite Instance

Now that the cluster is started, you can get an instance of the `Ignite` class:

```java
Ignite ignite = node.api();
```

This instance can be used to start working with the cluster. The future will be returned once the cluster is active.

In the following example, you interact with the cluster using the SQL API:

```java
Ignite ignite = node.api();
ignite.sql().execute(null,
        "CREATE TABLE IF NOT EXISTS Person (id int primary key, name varchar, age int);");
ignite.sql().execute(null, "INSERT INTO Person (id, name, age) VALUES (1, 'Person', 501);");
try (ResultSet<SqlRow> rs = ignite.sql().execute(null, "SELECT id, name, age from Person;")) {
    while (rs.hasNext()) {
        SqlRow row = rs.next();
        System.out.println("    "
                + row.value(1) + ", "
                + row.value(2));
    }
}
```

{% hint style="info" %}
Session is closable, but it is safe to skip `close()` method for DDL and DML queries, as they do not keep cursor open.
{% endhint %}

More examples of working with GridGain can be found in the [examples](https://github.com/apache/ignite-3/tree/main/examples) repository.

## Next Steps

From here, you may want to:

- Check out the [Developers guide](../developers-guide/table-api.md) page for more information on available APIs
- Try out our [examples](https://github.com/apache/ignite-3/tree/main/examples)
