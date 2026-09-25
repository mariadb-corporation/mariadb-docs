---
description: >-
  How to set up GridGain, including system requirements, binary and Maven
  installation, Docker, work directory, and enabling optional modules.
---

# Setting Up

## System Requirements

{% include "../.gitbook/includes/gg8-prereqs.md" %}

## Running GridGain with Java 11 or later

{% include "../.gitbook/includes/gg8-java9.md" %}

## Using Binary Distribution

- Download the appropriate binary package from [GridGain downloads](https://www.gridgain.com/resources/download).
- Unzip the archive into a directory.
- (Optional) Set the `IGNITE_HOME` environment variable to point to the
installation folder and make sure there is no trailing `/` in the path.

## Using Maven

The easiest way to start developing with GridGain is to use Maven.

- Add GridGain’s External Repository to the maven configuration file
(see the configuration example below).
- Set the `gridgain.version` property to the actual version you want to
use.
- Add the `gridgain-core` dependency for GridGain Enterprise Edition, or `gridgain-ultimate` for Ultimate Edition.

{% tabs %}
{% tab title="Enterprise Edition" %}
```xml
<properties>
    <gridgain.version>8.10</gridgain.version>
</properties>

<repositories>
    <repository>
        <id>GridGain Repository</id>
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

    <dependency>
        <groupId>org.gridgain</groupId>
        <artifactId>ignite-indexing</artifactId>
        <version>${gridgain.version}</version>
    </dependency>

    <!-- GridGain Enterprise Edition features -->
    <dependency>
        <groupId>org.gridgain</groupId>
        <artifactId>gridgain-core</artifactId>
        <version>${gridgain.version}</version>
    </dependency>

</dependencies>

```
{% endtab %}

{% tab title="Ultimate Edition" %}
```xml
<properties>
    <gridgain.version>8.10</gridgain.version>
</properties>

<repositories>
    <repository>
        <id>GridGain Repository</id>
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

    <dependency>
        <groupId>org.gridgain</groupId>
        <artifactId>ignite-indexing</artifactId>
        <version>${gridgain.version}</version>
    </dependency>

    <!-- GridGain Ultimate Edition features. -->
    <dependency>
        <groupId>org.gridgain</groupId>
        <artifactId>gridgain-ultimate</artifactId>
        <version>${gridgain.version}</version>
    </dependency>

</dependencies>
```
{% endtab %}
{% endtabs %}

## Using Docker

If you want to run GridGain in Docker, refer to the [Docker Deployment](../gridgain8-management/installation/installing-using-docker.md) section.

## Configuring Work Directory

GridGain uses a work directory to store your application data (if you use the [Native Persistence](../architecture/storage/native-persistence.md) feature), index files, metadata information, logs, and other files. The default work directory is as follows:

- `$IGNITE_HOME/work`, if the `IGNITE_HOME` system property is defined. This is the case when you start GridGain using the `bin/ignite.sh` script from the distribution package.
- `./ignite/work`, this path is relative to the directory where you launch your application.

There are several ways you can change the default work directory:

1. As an environmental variable:

   ```text
   export IGNITE_WORK_DIR=/path/to/work/directory
   ```

2. In the node configuration:

   {% tabs %}
   {% tab title="XML" %}
   ```xml
   <bean class="org.apache.ignite.configuration.IgniteConfiguration">
       <property name="workDirectory" value="/path/to/work/directory"/>
       <!-- other properties -->
   </bean>
   ```
   {% endtab %}

   {% tab title="Java" %}
   ```java
   IgniteConfiguration igniteCfg = new IgniteConfiguration();

   //setting the work directory
   igniteCfg.setWorkDirectory("/path/to/work/directory");
   ```
   {% endtab %}

   {% tab title="C#/.NET" %}
   ```csharp
   var cfg = new IgniteConfiguration
   {
       WorkDirectory = "/path/to/work/directory"
   };
   ```
   {% endtab %}

   {% tab title="C++" %}
   ```cpp
   IgniteConfiguration cfg;

   cfg.igniteHome = "/path/to/work/directory";
   ```
   {% endtab %}
   {% endtabs %}

## Enabling Modules

GridGain ships with a number of modules that provide various functionality. You can enable modules one by one, as required.

All modules are included in the binary distribution, but by default they are disabled (except for `ignite-core`, `ignite-spring`, `ignite-indexing`, and `ignite-opencensus`).
Modules can be found in the `lib/optional` directory of the distribution package (each module is located in a separate sub-directory).

Depending on how you use GridGain, you can enable modules using one of the following methods:

- If you use the binary distribution, move the `lib/optional/{module-dir}` to the `lib` directory before starting the node.
- Add libraries from `lib/optional/{module-dir}` to the classpath of your application.
- Add a module as a Maven dependency to your project.

  ```xml
  <dependency>
      <groupId>org.gridgain</groupId>
      <artifactId>ignite-indexing</artifactId>
      <version>${gridgain.version}</version>
  </dependency>
  ```

The following modules are available:

|Module’s artifactId |Description|
|---|---|
|control-center-agent| Connects the cluster to [GridGain Control Center]({tools}/control-center) for monitoring and management. Must be enabled on all server nodes. Requires Java 17 or later.|
|gridgain-bulkload|Support for SQL `COPY FROM INTO` statement that can be used to import or export data in csv, parquet, and iceberg formats. See [COPY INTO](../reference/sql/operational-commands.md#copy-into) for details.|
|gridgain-sql| Support for JSON functions.  See [JSON Functions](../reference/sql/functions/json-functions.md) for details.|
|gridgain-vector-query| Support for vector storage and indexing. See [Vector Storage](vector-search.md) for details.|
|ignite-aop | GridGain AOP module provides capability to turn any Java method to a distributed closure by adding @Gridify annotation to it.|
|ignite-aws |Cluster discovery on AWS S3. Refer to [Amazon S3 IP Finder](clustering/discovery-in-the-cloud.md#amazon-s3-ip-finder) for details.|
|ignite-cassandra-serializers | The GridGain Cassandra Serializers module provides additional serializers to store objects as BLOBs in Cassandra. The module could be used as in conjunction with the GridGain Cassandra Store module.|
|ignite-cassandra-store | GridGain Cassandra Store provides a CacheStore implementation backed by the  Cassandra database.|
|ignite-cloud | *Deprecated.* GridGain Cloud provides Apache jclouds implementations of the IP finder for TCP discovery. This module is deprecated and will be removed in a future release. Use one of the other IP finders described in [Discovery in the Cloud](clustering/discovery-in-the-cloud.md) instead.|
|ignite-direct-io | GridGain Direct IO is a plugin that provides a page store with the ability to write and read cache partitions in O_DIRECT mode.|
|ignite-gce | GridGain GCE provides Google Cloud Storage based implementations of IP finder for TCP discovery.|
|ignite-hibernate-core | *Deprecated.* Shared classes for the GridGain Hibernate L2 cache integration. The Hibernate integration modules are deprecated and will be removed in a future release.|
|ignite-hibernate_4.2 | *Deprecated.* GridGain Hibernate provides a Hibernate L2 cache implementation based on GridGain In-Memory Data Grid. This module is deprecated and will be removed in a future release. Use the `ignite-hibernate-7.4` module instead.|
|ignite-hibernate_5.1 | *Deprecated.* GridGain Hibernate provides a Hibernate L2 cache implementation based on GridGain In-Memory Data Grid. This module is deprecated and will be removed in a future release. Use the `ignite-hibernate-7.4` module instead.|
|ignite-hibernate-7.4 | GridGain Hibernate 7.4 module provides a Hibernate L2 (second-level) cache implementation based on the GridGain In-Memory Data Grid for Hibernate ORM 7.4. Supports `READ_ONLY`, `READ_WRITE`, and `NONSTRICT_READ_WRITE` concurrency strategies.|
|ignite-indexing | [SQL querying and indexing](sql/indexes.md)|
|ignite-jcl |Support for the Jakarta Common Logging (JCL) framework.|
|ignite-jta |Integration of GridGain transactions with JTA.|
|ignite-kafka | GridGain Kafka Streamer provides capability to stream data from Kafka to GridGain caches.|
|ignite-kubernetes | GridGain Kubernetes module provides a TCP Discovery IP Finder that uses a dedicated Kubernetes service for IP addresses lookup of GridGain pods containerized by Kubernetes.|
|ignite-log4j2 |Support for Log4j2|
|ignite-lucene-8 |Lucene 8 library. Required for running GridGain on Java 8.|
|ignite-lucene-9 |Lucene 9 library. Provides full text and vector search on Java 11 and 17.|
|ignite-lucene-10 |Lucene 10 library. Provides full text and vector search on Java 21 and later.|
|ignite-ml | GridGain ML Grid provides machine learning features and relevant data structures and methods of linear algebra, including on heap and off heap, dense and sparse, local and distributed implementations. Refer to the [Machine Learning](machine-learning/ml.md) documentation for details.|
|ignite-opentelemetry | Support for exporting metrics to an [OpenTelemetry Protocol (OTLP)](https://opentelemetry.io/docs/specs/otlp/) compatible backend. See [OpenTelemetry](../reference/monitoring/generic-metrics.md#opentelemetry) for information on configuring the exporter..|
|ignite-osgi | This module provides bridging components to make GridGain run seamlessly inside an OSGi container such as Apache Karaf.|
|ignite-osgi-karaf | This module contains a feature repository to facilitate installing GridGain into an Apache Karaf container.|
|ignite-osgi-paxlogging | This module is an OSGi fragment that exposes the following packages from the Pax Logging API bundle:<br><br>• org.apache.log4j.varia<br>• org.apache.log4j.xml<br><br>These packages are required when installing the ignite-log4j bundle, and are not exposed by default by the Pax Logging API - the logging framework used by Apache Karaf.|
|ignite-rest-http | GridGain REST-HTTP starts a Jetty-based server within a node that can be used to execute tasks and/or cache commands in grid using HTTP-based [RESTful APIs](../reference/rest-api/README.md).|
|ignite-schedule | This  module provides functionality for scheduling jobs locally using UNIX cron-based syntax.|
|ignite-slf4j | Support for [SLF4J logging framework](logging.md#using-slf4j).|
|ignite-spring-data_2.2 | GridGain Spring Data provides an integration with the Spring Data framework. The `_2.2` suffix in the module name is historical and is kept so that existing dependency coordinates continue to work.|
|ignite-urideploy | GridGain URI Deploy module provides capabilities to deploy tasks from different sources such as File System, HTTP, or even Email.|
|ignite-web | GridGain Web allows you to start nodes inside any web container based on servlet and servlet context listener. In addition, this module provides capabilities to cache web sessions in a GridGain cache.|
|ignite-zookeeper | GridGain ZooKeeper provides a TCP Discovery IP Finder that uses a ZooKeeper directory to discover other GridGain nodes.|

## Configuration Recommendations

Below are some recommended configuration tips aimed at making it easier for
you to operate a GridGain cluster or develop applications with GridGain.

### Setting Work Directory

If you are going to use either binary distribution or Maven, you are
encouraged to set up the work directory for GridGain.
The work directory is used to store metadata information, index files, your application data (if you use the [Native Persistence](../architecture/storage/native-persistence.md) feature), logs, and other files.
We recommend you always set up the work directory.

### Recommended Logging Configuration

Logs play an important role when it comes to troubleshooting and finding what went wrong. Here are a few general tips on how to manage your log files:

- Do not store log files in the `/tmp` folder. This folder is cleared up every time the server is restarted.
- Make sure that there is enough space available on the storage where the log files are stored.
- Archive old log files periodically to save on storage space.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
