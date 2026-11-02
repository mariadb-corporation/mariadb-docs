---
description: >-
  GridGain 8.10.0 requires Java 17, moves integrations to current versions and out of the server packages, and extends vector search, the thin clients, and Apache Ignite 2 compatibility.
hidden: true
---

# GridGain 8.10.0 Release Notes

## Overview

GridGain 8.10 is a major release. It raises the Java baseline to Java 17, removes or relocates a number of optional modules and integrations, and moves the Spring, Hibernate, Lucene, Cassandra, and Jetty integrations to current library versions. It adds custom metrics, replication delay metrics for data center replication, vector search on PARTITIONED caches, a MariaDB cache store, and the GridGain Model Context Protocol (MCP) server. It also extends the thin clients and Apache Ignite 2 compatibility.

Upgrading from GridGain 8.9.x requires action. Read [Breaking Changes](#breaking-changes), [Configuration and Default Value Changes](#configuration-and-default-value-changes), and [Security, Permission, and Licensing Changes](#security-permission-and-licensing-changes) before you upgrade a cluster or an embedding application, and work through the checklist in [Installation and Upgrade Information](#installation-and-upgrade-information).

Server-side SQL `COPY` against a file or an object store is now closed by default. This stops configurations that upgrade unchanged, so check it first.

## Breaking Changes

### Java 17 or Later is Required

GridGain 8.10 requires Java 17 or later. GridGain 8.9.x supported Java 8 and later. The requirement is the same on the server and on the client.

| Component | Minimum | How the requirement is enforced |
|---|---|---|
| Server node | Java 17 | `ignite.sh` and `ignite.bat` refuse to start on anything below 17. In 8.9.x the same check refused anything below 8. |
| Control script, and the other `bin` scripts | Java 17 | `control.sh` and `control.bat` apply the same check. |
| Thick client, or an application that embeds a node | Java 17 | Class file version. Loading `ignite-core` on an older Java Virtual Machine (JVM) fails with `UnsupportedClassVersionError`. |
| Java thin client, JDBC thin driver | Java 17 | Class file version. Both ship inside `ignite-core`. |
| .NET client, thick mode | Java 17 | Checked at run time against the JVM that the client starts. A `JAVA_HOME` pointing at an older Java Development Kit (JDK) now fails with `Unsupported Java version: <version>. GridGain requires Java 17 or later.` |
| .NET client, thin mode | No JVM | The thin client is fully managed and starts no JVM. The .NET package targets `netstandard2.0`, `net8.0`, and `net10.0`. |
| C++ client, ODBC driver | No JVM | Native, no Java requirement. |
| Control Center agent | Java 17 | Class file version. An agent embedded in an application raises that application's floor to Java 17. |
| A node on the Lucene 10 line | Java 21, or 22 | `ignite-lucene-10` is compiled for Java 21 and `ignite-lucene-10-java22` for Java 22. This applies to the server only. See [Lucene 8 Removed, and a Lucene 10 Line Added](#lucene-8-removed-and-a-lucene-10-line-added). |

Upgrade the JVM on every server node, every client application, and every application that embeds GridGain before you upgrade to 8.10.

GridGain 8.10.0 supports Java 17, 21, and 25.

### Removed and Replaced Modules

The following modules are removed in 8.10.0:

| Removed module | Replacement | Deprecated in |
|---|---|--|
| `ignite-hibernate-4.2`, `ignite-hibernate-5.1`, `ignite-hibernate-5.3`, `ignite-hibernate-core` | `ignite-hibernate-7.4` (Hibernate 7.4 second-level cache) | 8.9.35 |
| `ignite-spring-6` | `ignite-spring`, built against Spring 7 | Not deprecated in the 8.9.x line |
| `ignite-spring-data_2.2` | `ignite-spring-data`, built against Spring Data 4.1. See [Spring Data Module Renamed](#spring-data-module-renamed). |  |
| `ignite-rest-http` on Jetty 9.4, and the optional `ignite-rest-http-jetty-12` module | `ignite-rest-http`, which now runs on Jetty 12. See [REST HTTP Module Runs on Jetty 12](#rest-http-module-runs-on-jetty-12). | 8.9.39 |
| `ignite-lucene-8` | `ignite-lucene-9`, which stays the default, or the Lucene 10 line | Not deprecated in the 8.9.x line |
| `ignite-aop`, and the Gridify API in `ignite-core` | The compute API | 8.9.37 |
| `ignite-cloud` (`TcpDiscoveryCloudIpFinder`) | Another IP finder | 8.9.37 |
| `ignite-aws` (S3 checkpoint service provider interface (SPI), S3, ELB, and ALB IP finders) | The Apache Ignite `ignite-aws-ext` extension | 8.9.39 |
| `ignite-ssh` | The Apache Ignite `ignite-ssh-ext` extension | Not deprecated in the 8.9.x line |
| `ignite-ml`, and the Spark, XGBoost, and MLeap model parsers | The Apache Ignite `ignite-ml-ext` extension | 8.9.38 |
| `ignite-mesos` | None | 8.9.39 |
| `ignite-yardstick` | None | |
| `gridgain-diagnostic`, `gridgain-tools`, `gridgain-yardstick` (Enterprise and Ultimate) | None | |

The following modules are new in this release:

- `ignite-hibernate-7.4`
- `ignite-spring-data`
- `ignite-lucene-10`, `ignite-lucene-10-java22`, and `lucene-9-10-common`
- `gridgain-vector-query-common` and `gridgain-vector-query-lucene-10` (Enterprise and Ultimate)

### Integrations Moved Out of the Server Packages

The server packages no longer carry every integration. If you script a copy of a folder from `integration/` or `libs/optional/` into `libs/`, check it against this table:

| Integration | Location in 8.9.x | Location in 8.10.0 |
|---|---|---|
| Oracle GoldenGate (`gridgain-goldengate`, `gridgain-goldengate-12.2`, `gridgain-goldengate-19`) | `integration/` of the server package | `integration/` of the separate `gridgain-integrations-<version>.zip` download |
| Kafka Connect (`gridgain-kafka-connect`) | `integration/gridgain-kafka-connect` | The [`gridgain/gridgain-kafka-connect`](https://www.confluent.io/hub/gridgain/gridgain-kafka-connect) Confluent Hub component only. `copy-dependencies.sh` is removed. |
| `ignite-hibernate-7.4` | `libs/optional` | Maven only (`org.gridgain:ignite-hibernate-7.4`) |
| `ignite-spring-data`, `ignite-spring-data-commons` | `libs/optional` | Maven only (`org.gridgain:ignite-spring-data`) |
| `ignite-opencensus` | `libs`, enabled by default | `libs/optional`, disabled by default |
| `gridgain-bulkload` | `libs/optional` | `libs/optional`, with a smaller set of dependencies |

The Oracle GoldenGate integrations run on the GoldenGate host, not on a GridGain node. Take them from the integrations download whose version matches your cluster.

For Kafka Connect, use the Confluent Hub component version that matches your cluster. On an Ultimate Edition cluster, also copy `libs/gridgain-ultimate/*.jar` from the server package into the component's `lib` directory on every Kafka Connect worker.

`ignite-hibernate-7.4` and `ignite-spring-data` are application libraries that a node never loads. If code that uses them runs on a standalone node, such as in a compute task, put the artifacts and their dependencies into the node's `libs` directory yourself.

A node that configures `OpenCensusTracingSpi` or `OpenCensusMetricExporterSpi` now fails at startup with `ClassNotFoundException` until you move `libs/optional/ignite-opencensus` into `libs`. With the module disabled, the third-party libraries it bundles, such as Guava, gRPC, and the Prometheus client, are no longer on the classpath of every node. If your own code on the node relies on them, ship them with your code. In Docker images, add `ignite-opencensus` to `OPTION_LIBS`.

`gridgain-bulkload` no longer bundles the AWS SDK `bundle` jar, the Hadoop YARN and HDFS libraries, or the Snowflake JDBC driver. Snowflake is not a supported source. If you allow-listed `jdbc:snowflake:` or `SnowflakeCatalog`, put a Snowflake JDBC driver into `libs/gridgain-bulkload` on every node that uses it.

### Hibernate 7.4 Only

The Hibernate second-level cache implementation now targets Hibernate 7.4. Applications on Hibernate 4.2, 5.1, or 5.3 must move to Hibernate 7.4 or stay on GridGain 8.9.x.

### Spring 7 Only

GridGain 8.10 builds against Spring Framework 7.0.9 and Spring Data 4.1. The `ignite-spring` and `ignite-spring-data` modules are compiled to Java 17 bytecode and target Spring 7. Spring 5 and Spring 6 are no longer supported.

An application that embeds GridGain through Spring must be on Spring 7. Otherwise, stay on GridGain 8.9.x, which keeps the Spring 5 and Spring 6 modules.

### Spring Data Module Renamed

The `ignite-spring-data_2.2` module is renamed to `ignite-spring-data`, and its package moves from `org.apache.ignite.springdata22` to `org.apache.ignite.springdata`.

Update the artifact ID in your build files, and update the imports of `IgniteRepository`, `@EnableIgniteRepositories`, `@RepositoryConfig`, `@Query`, and the other classes of the module.

### Control Center Agent Requires Spring 7 and Jakarta WebSocket

The Control Center agent is built against Spring 7 and Jakarta WebSocket (Tyrus 2), and the emulator module is removed.

An agent embedded in a Spring 5 or Spring 6 application does not start. Upgrade the host application to Spring 7, or keep using the 8.9.x agent.

### REST HTTP Module Runs on Jetty 12

The `ignite-rest-http` module now runs on Jetty 12 and requires Java 17 or later. The Jetty 9.4 REST module is removed, and so is the separate `ignite-rest-http-jetty-12` module that GridGain 8.9.38 and 8.9.39 shipped as an option. The module keeps the `ignite-rest-http` artifact name, so dependency declarations do not change.

A configuration that does not set `ConnectorConfiguration.setJettyPath()` needs no changes. A custom `jetty.xml` file written for Jetty 9.4 does not load on Jetty 12. Migrate it as follows:

- Rename the `threadpool` argument of the `Server` constructor to `threadPool`, or remove the name and pass the argument by position.
- Remove the `<Set name="handler">` block that uses `HandlerCollection` or `HandlerList`. Both classes were removed in Jetty 12, and GridGain installs its own REST handler.

The Jetty 12 module supports XML configuration and HTTPS, including mutual TLS.

### Cassandra Store Uses the DataStax Driver 4

The Cassandra store moves from DataStax Java driver 3.2 to 4.17 (`com.datastax.oss.driver.*`), and from `cassandra-all` 3.11 to 5.0.8, which is required for Java 17. Native protocol versions 1 and 2 are dropped by the driver, so Cassandra 2.1 or later is required, and `setProtocolVersion(1)` or `setProtocolVersion(2)` now fails with `Incorrect protocol version`. Cassandra 3 clusters must be upgraded 3 -> 4 -> 5.

The `DataSource` configuration API changed:

- `setLocalDataCenter()` is now required whenever you specify explicit contact points and do not set a custom load balancing policy. A node that leaves it unset fails with `Cassandra local datacenter is not specified for the data source`.
- Policies are configured by class rather than by instance: `setLoadBalancingPolicyClass()`, `setReconnectionPolicyClass()`, `setRetryPolicyClass()`, `setAddressTranslatorClass()`, and `setSpeculativeExecutionPolicyClass()` replace the former `setLoadBalancingPolicy()`, `setReconnectionPolicy()`, `setRetryPolicy()`, `setAddressTranslator()`, and `setSpeculativeExecutionPolicy()`.
- `setPoolingOptions()`, `setSocketOptions()`, and `setNettyOptions()` are removed. Use `setConfigFile()` and a driver configuration file instead.
- `setSslOptions()` is replaced by `setSslEngineFactory()`.
- `setCollectMetrix()` and `setJmxReporting()` are removed.
- `user` and `password` are now mutually exclusive with `credentials`. Setting both fails the data source with `Both 'user'/'password' and 'credentials' are set for the data source`.

Update the `DataSource` bean definitions in your Spring XML configuration accordingly.

Previously serialized `DataSource` instances, such as those held by dynamically created caches, cannot be read by 8.10. Deserialization fails with `Unsupported DataSource serialization format version`. Drop and recreate those caches.

Large transactions may now hit the Cassandra `batch_size_fail_threshold` setting.

Only the embedded test server is unsupported on Windows. The runtime client is unaffected.

### Lucene 8 Removed, and a Lucene 10 Line Added

The `ignite-lucene-8` module is removed. If you still run it (the Java 8 workaround documented for GridGain 8.9.18 and later put it in `libs`), move to the Lucene 9 line before you upgrade.

The Lucene 9 line, with `ignite-lucene-9` enabled in `libs`, remains the default for vector search and text search. The binary distribution also ships the Lucene 10.4 line in `libs/optional`, disabled by default, because it requires Java 21:

- `ignite-lucene-10` - Java 21 or later.
- `ignite-lucene-10-java22` - Java 22 or later. Adds the no-copy vector scorer, which is opt-in even on a supported JDK.

For vector search, newer lines give higher performance: Lucene 10 is faster than Lucene 9, and a newer Java version is faster than an older one. The best performance comes from the `ignite-lucene-10-java22` line on Java 22 or later with the no-copy vector scorer enabled.

A node runs exactly one Lucene line. The two carry the same class names, so they cannot share a classpath. To switch a node to Lucene 10, stop the node and remove `libs/ignite-lucene-9`. Move exactly one of the Lucene 10 module folders from `libs/optional` to `libs`. For vector search, also replace `libs/gridgain-vector-query` with `libs/optional/gridgain-vector-query-lucene-10`. Then start the node. In Docker images, set the `LUCENE_LINE` environment variable to `10` or `10-java22` instead.

Use the same line on every node. A cluster running both answers one vector query with different recall depending on which node serves it.

Switching lines does not migrate or invalidate anything on disk. A GridGain Lucene index is held in memory and rebuilt from cache data.

### Gridify API Removed

The Gridify API is removed from `ignite-core`, together with the `ignite-aop` module. This covers the `org.apache.ignite.compute.gridify` package, including the `@Gridify`, `@GridifySetToSet`, and `@GridifySetToValue` annotations and their AOP aspects.

Replace Gridify usage with the compute API. The API was deprecated in 8.9.37.

### SSH Support Moves to an Apache Ignite Extension

The `ignite-ssh` module is removed. `IgniteCluster.startNodes()` remains in the API, but the SSH implementation behind it now comes from the Apache Ignite `ignite-ssh-ext` extension.

If you use `startNodes()`, add `ignite-ssh-ext` to the node classpath. GridGain still resolves the SSH implementation by the class name `org.apache.ignite.internal.util.nodestart.IgniteSshHelperImpl`, and a node without it on the classpath still reports the missing component as `ignite-ssh`.

### Cloud and AWS IP Finders Removed

The `ignite-cloud` module, including `TcpDiscoveryCloudIpFinder`, is removed. It was deprecated in 8.9.37. Use the JDBC, static, or Kubernetes IP finders instead.

The `ignite-aws` module is removed, together with the S3 checkpoint SPI, the S3, ELB, and ALB IP finders, and the S3 IP finder encryption services. It was deprecated in 8.9.39. Add the Apache Ignite `ignite-aws-ext` extension to the classpath instead.

The Kubernetes IP finder remains in 8.10.0. It now uses Jackson 3.

### Machine Learning Module Removed

The `ignite-ml` module is removed, together with the `ignite-ml-spark-model-parser`, `ignite-ml-xgboost-model-parser`, and `ignite-ml-mleap-model-parser` modules. The public `org.apache.ignite.ml` API was deprecated in 8.9.38. Use the Apache Ignite `ignite-ml-ext` extension instead.

### Local Store Removed

Local store support is removed: the `@CacheLocalStore` annotation, `CacheFileLocalStore` and `CacheFileLocalStoreWriteMode` (Enterprise and Ultimate), and the `IGNITE_LOCAL_STORE_KEEPS_PRIMARY_ONLY` system property. They were deprecated in 8.9.39. Use native persistence or a regular `CacheStore` instead, and remove the system property from your start scripts.

### C++ Client Requires C++14

The C++ client now requires C++14, and the autotools build is removed. Build the client and the applications that use it with a C++14-capable compiler through CMake.

### Evaluation License Distributions are no Longer Built

The `eval/` license files are removed, and so are the three evaluation-license assembly descriptors that produced the Enterprise, Ultimate, and z/OS `-evallic` archives. Those archives are no longer built.

### No Community Edition Build

GridGain 8.10 has no Community Edition build.

## Configuration and Default Value Changes

### SFTP Snapshot Transport Verifies the Host Key by Default

The `strictHostKeyChecking` property of `SftpConfiguration` now defaults to `true`. In 8.9.x it defaults to `false`.

Before the first snapshot transfer to an SSH File Transfer Protocol (SFTP) destination, either populate the known hosts file that `knownHostsPath` points at, or set `strictHostKeyChecking` to `false` explicitly. Otherwise, transfers fail.

### Vector Search Limits

Vector search now enforces limits that reject queries instead of accepting them:

- The maximum number of vector dimensions defaults to 4096. Raise the `GRIDGAIN_VECTOR_MAX_DIMENSIONS` property if you index wider vectors. It applies to indexes created after it is set.
- A single vector query may ask for at most 10,000 neighbors, set by `GRIDGAIN_VECTOR_MAX_K`. A query above the limit, or with a neighbor count that is not positive, is rejected.

### Java Thin Client Timeouts Have Default Values

The Java thin client now has default timeouts. The handshake timeout defaults to 10 seconds, and the request timeout defaults to 60 seconds. In 8.9.x, both timeouts were infinite by default.

A request that takes longer than 60 seconds, such as a large query, a compute task, or a data streamer flush, now fails with a timeout. To keep the previous behavior, set `ClientConfiguration.setHandshakeTimeout(0)` and `ClientConfiguration.setRequestTimeout(0)` explicitly.

### Thin Client DNS Resolution

The Java thin client now resolves its configured addresses through `DnsClientAddressFinder` by default. When an address resolves to several IP addresses, the client uses all of them instead of a single address. This affects host names backed by multiple A records or round-robin DNS.

The client also re-resolves its addresses in the background every 30 seconds, and reinitializes its channels when the result changes. Use the new `ClientConfiguration.setBackgroundReResolveAddressesInterval()` property to change the interval.

The .NET thin client uses the same hostname resolution logic.

### Java Thin Client Transactions are Partition-Aware

Java thin client transactions are partition-aware, and a transaction now starts lazily. `txStart()` no longer sends a `TX_START` message. The message is deferred until the first cache operation inside the transaction, so that the transaction can be mapped to the affinity node. Applications are not expected to notice. A transaction that performs no cache operation now never reaches the server. An error that used to surface at `txStart()` surfaces at the first operation instead. To opt out, disable partition awareness.

### .NET Transactions are Async-Local

The current .NET transaction is now stored per async flow instead of per thread, so `async` and `await` code works inside a thin client transaction block. This changes two rare cases:

- Work started from inside a transaction with `Task.Run` or `ThreadPool.QueueUserWorkItem` now sees the ambient transaction and can enlist in it.
- A thick client transaction is bound to the thread that started it. If an async continuation resumes on another thread, GridGain now fails with `InvalidOperationException` instead of reporting no transaction.

To restore the per-thread behavior, set the `IGNITE_TX_USE_THREAD_LOCAL` environment variable to `true`.

### .NET Thin Client Load Balancing

The .NET thin client no longer sends every request that is not partition-aware through one default connection. Such requests are now spread across the live connections in a round-robin fashion, which changes how the client load is distributed across server nodes.

### Binary Metadata Fields are Matched by Field ID

When binary metadata is merged, fields are now matched by field ID, as computed by the configured ID mapper, instead of by name. Field names that differ only in a way the ID mapper ignores, such as letter case, now denote the same field instead of creating a duplicate. The type of a field can no longer be changed by registering it under another name. The affinity key field name is compared through the ID mapper too. A binary object builder rejects a value of a different type for an existing field.

The new behavior applies only when every node in the cluster supports it, so a mixed 8.9 and 8.10 cluster keeps merging by name. Metadata that the cluster has already accepted is not changed. To turn the new behavior off, set the `IGNITE_BINARY_METADATA_MERGE_BY_FIELD_ID_FEATURE` system property to `false`.

### JMX Exposes Object Metrics as Strings

`ObjectMetric` values are now exposed through Java Management Extensions (JMX) as strings. JMX tools that read these attributes receive a string instead of an opaque object.

### Clearer Startup Errors and Warnings for Stale Properties

An unknown property in the Spring XML configuration has always failed node startup. GridGain 8.10 replaces the opaque Spring message with `Configuration property <Bean>.<property> does not exist`, which names the bean and the property. The property is typically an Apache Ignite-only property left behind by a migration.

GridGain also keeps a registry of Apache Ignite `IGNITE_*` system properties that have no effect in GridGain. It logs a warning for each one that is set at node start, pointing at the migration guide.

Clean up any leftover Apache Ignite properties in your configuration before upgrading.

## Security, Permission, and Licensing Changes

### Server-Side SQL COPY is Now Disabled by Default

The file and object-store side of server-side SQL `COPY` is secure by default in GridGain 8.10, and it is rejected by default. To use it after the upgrade, an operator must do all three of the following:

1. Enable the feature. Set `fileAccessEnabled` to `true` on the new `ImportExportConfiguration` block of the per-node GridGain plugin configuration. It defaults to `false`, and an absent `GridGainConfiguration` or an absent block is treated as fully closed.
2. Populate the allow-lists. Every allow-list on that block starts empty, and an empty list forbids the corresponding access: `importRoots` for local directories, `allowedS3Buckets` and `allowedS3Endpoints` for S3, `allowedCatalogUris` for Iceberg catalogs, and `allowedIcebergClasses` for Iceberg catalog implementation classes.
3. Grant the new `COPY_FROM_FILE` and `COPY_TO_FILE` security permissions to every role that runs server-side `COPY`.

`ImportExportConfiguration` is node-local. It is never distributed over discovery, so a `COPY` can succeed or fail depending on which node the client connected to. Configure it identically on every node.

Point `importRoots` at dedicated directories, never at the node work directory: `COPY_TO_FILE` overwrites files inside a root.

{% hint style="warning" %}
This affects every existing `COPY FROM` and `COPY TO` statement that reads or writes a file or an object store. Those statements stop working on 8.10 until the configuration above is in place. Client-side `COPY` is unaffected.
{% endhint %}

### COPY ... FORMAT JDBC Restrictions

`COPY ... FORMAT JDBC` now validates the JDBC URL before it opens a connection:

- Only the `jdbc:mariadb:`, `jdbc:mysql:`, and `jdbc:postgresql:` URL schemes are accepted by default. In-JVM drivers, such as `jdbc:h2:` and `jdbc:gg-h2:`, are always rejected. To change the list of accepted schemes, set the `GRIDGAIN_BULKLOAD_JDBC_ALLOWED_URL_SCHEMES` system property or environment variable on the node.
- URLs with connection parameters that load classes, deserialize Java objects, or read local files, such as `INIT`, `allowLoadLocalInfile`, `autoDeserialize`, and `socketFactory`, are rejected.
- `${VAR}` placeholders in the `url`, `user`, and `password` properties are no longer expanded by default. To allow expansion, list the permitted environment variables in the `GRIDGAIN_BULKLOAD_JDBC_ENV_ALLOWLIST` system property or environment variable on the node.
- To restrict the hosts that a URL can connect to, set the `GRIDGAIN_BULKLOAD_JDBC_ALLOWED_HOSTS` system property or environment variable on the node. The host check is disabled by default.

These settings are read from the node only, never from the SQL statement. Configure them identically on every node.

### REST Scan Query Filter Classes Require an Allow-List

The `EXECUTE_SCAN_QUERY` REST command now instantiates a filter class only if the class is listed in the new `IGNITE_REST_SCAN_QUERY_FILTER_CLASSES` system property. The list is empty by default, so a scan query that passes a `className` parameter is rejected until you allow that class.

Set the property to a comma-separated list of fully qualified class names. Names are matched exactly. Package names and prefixes do not match. The property can also be set as an environment variable. Set it to the same value on every node that has the REST connector enabled, because the check runs on the node that receives the request.

### REST Error Responses no Longer Include Stack Traces

REST error responses no longer return the server stack trace to the client. Clients that parse the stack trace from an error response must use the error message instead.

### Thin Client Continuous Query Filters Go Through the Class Filter

Remote filters and transformers that a thin client sends with a continuous query are now checked against the marshaller class filter (`IGNITE_MARSHALLER_WHITELIST` and `IGNITE_MARSHALLER_BLACKLIST`) on every path. If you use a class filter, make sure it allows the filter classes of your continuous queries.

### Stricter Header Verification for Visor Data Transfer Objects

The header check that `VisorDataTransferObject` performs when it deserializes a payload is corrected. The previous check masked the header with the magic number itself, so a header that merely shared bits with the magic number passed. GridGain 8.10 masks the version byte off and compares the full magic number.

No action is required. The serialized form is unchanged, so a mixed 8.9 and 8.10 cluster and an older control script both keep working. A malformed or foreign payload is now rejected where it could previously slip through.

### MariaDB License Keys

GridGain 8.10 accepts license keys in the MariaDB license key format, both at node start and through `GridProduct.updateLicense()`. A MariaDB license key must carry an expiry date, and a key without one is rejected. XML license files are unaffected: an XML license without an expiry date still does not expire.

A MariaDB license key can enable soft mode. With soft mode, a license violation is logged and recorded as an event, but it does not stop the node or fail a client.

### Custom Metrics Permission

The new `CUSTOM_METRICS_MANAGE` permission is required to create and remove custom metric registries when security is enabled. See [Custom Metrics](#custom-metrics).

### License Terms

GridGain 8.10 is distributed under the MariaDB Software License Terms. The distribution ships them in `licenses/LICENSE`, together with a root `COPYRIGHT` file. The Apache License 2.0 and Community Edition license files are removed from the distribution.

## Deprecation Notice

The following configuration is deprecated but still works. Migrate at your convenience.

| Deprecated | Replacement |
|---|---|
| `DataStorageConfiguration.setSystemRegionInitialSize()` and `setSystemRegionMaxSize()` | `SystemDataRegionConfiguration` |
| `ClientConfiguration.getTimeout()` and `setTimeout()` | `getHandshakeTimeout()` and `getRequestTimeout()`, `setHandshakeTimeout()` and `setRequestTimeout()` |
| `ClientConfiguration.isPartitionAwarenessEnabled()` and `setPartitionAwarenessEnabled()` | `isAffinityAwarenessEnabled()` and `setAffinityAwarenessEnabled()` |
| `ClientCacheConfiguration.getRebalanceBatchSize()`, `getRebalanceBatchesPrefetchCount()`, `getRebalanceThrottle()`, `getRebalanceTimeout()`, and their setters | The equivalent `IgniteConfiguration` properties |
| `ClientCacheConfiguration.getRebalanceDelay()` and `setRebalanceDelay()` | Baseline topology |
| `ClientCacheConfiguration.getDefaultLockTimeout()` and `setDefaultLockTimeout()` | None - the property has no effect |

When `getTimeout()` is used with differing handshake and request timeouts, a warning is written to the log.

`IgniteConfiguration.getDefaultQueryTimeout()` and `setDefaultQueryTimeout()` are new in this release and ship deprecated. They are Apache Ignite source-compatibility aliases, added so that Apache Ignite code compiles unchanged. Use `SqlConfiguration.getDefaultQueryTimeout()` and `SqlConfiguration.setDefaultQueryTimeout()` in new code.

## New Features

### GridGain MCP Server

GridGain 8.10 introduces the GridGain MCP server, which lets AI agents and assistants that support MCP discover a cluster and run read-only SQL queries against it. The server ships as its own download and as a container image. It supports TLS, mutual TLS, and authentication, limits the rate of tool calls, and writes a local audit log of tool calls with rotation and expiry.

### MariaDB Cache Store

The new `MariaDBCacheStoreFactory` creates a cache store backed by a MariaDB database, with the MariaDB dialect applied automatically. It supports write-behind.

### Importing a Database Schema

The new `schema-import.sh` and `schema-import.bat` scripts read the table definitions of an external database over JDBC and generate the matching GridGain data definition language (DDL) statements. They can apply the generated schema to a cluster and load the data with `COPY` statements.

`COPY ... FORMAT JDBC` can now load data from a MariaDB database.

### Custom Metrics

You can now register your own metrics. The new experimental `Ignite.metrics()` method returns an `IgniteMetrics` instance that creates, lists, and removes custom metric registries on the local node. Custom registries are exposed by the metric exporters with the `custom.` prefix. Custom metrics are not persisted and must be registered again after a node restart.

When security is enabled, creating and removing a custom registry requires the new `CUSTOM_METRICS_MANAGE` permission. Registry and metric names are limited to 256 characters by default. Use the `IGNITE_CUSTOM_METRICS_MAX_NAME_LENGTH` system property to change the limit.

### Replication Delay Metrics for Data Center Replication

The receiver hub now reports how long replicated updates take to arrive from each source data center, for each cache, and whether the clocks of the two data centers disagree. The metrics are available in the `dr.receiver.trace.dc<ID>.<cacheName>` registry.

To carry the timing information, data center replication uses a new version of its protocol. The sender and the receiver negotiate the protocol version, the batch format, and the protocol features, so a data center on 8.10 keeps replicating to and from a data center on an earlier version. Batches from an earlier sender carry no timing information and are counted in the `LegacyBatchesOnV2Session` metric. A non-zero value is expected during a rolling upgrade and while batches stored before the upgrade are sent.

Data center replication sender monitoring is also extended: `DrSenderInMetrics` and `DrSenderOutCacheMetrics` carry additional counters, and the sender's debug logging is throttled.

### Vector Search

- Vector search works on PARTITIONED caches. A vector query is sent to every node, each node searches its primary partitions, and the results are merged into the top-k.
- Similarity scores are returned with query results through `ScoredCacheEntry`.
- Vector queries take a single parameter object that carries the filter, the keys-only flag, the oversample factor, and the search beam width (`efSearch`).
- Hierarchical Navigable Small World (HNSW) build parameters, `M` and `efConstruction`, can be set per index.
- Vectors can be stored as `int8`, with a configurable segment target, query thread count, and deleted-vector budget.
- Binary quantization is supported, node-wide through `GRIDGAIN_VECTOR_BINARY_QUANTIZATION` or per index. A per-index storage choice always wins over the node-wide property, and either only applies to indexes built after it is set.
- On Java 22 or later, the `ignite-lucene-10-java22` line can score vectors directly in off-heap memory instead of copying them to the heap.
- Vector search performance improves with newer Lucene and Java versions. Lucene 10 on Java 22 or later gives the best performance.
- Lucene 10 vector query caching has configurable segment-size thresholds.
- The thin client vector protocol moves to version 2. Thin clients can set the search beam width, request similarity scores, omit values from result rows, and pass a field filter and an oversample factor.

### Java Thin Client

The Java thin client adds the following:

- A data streamer, and an asynchronous `ClientDataStreamer.flush()`.
- SQL cache creation.
- Service awareness, and `serviceProxy()` with a `ServiceCallContext`.
- `ClientCache.sizeLong()`, `withPartitionRecover()`, and partition-aware `getAll()`.
- Lifecycle events.
- Asynchronous overloads for atomic longs, atomic sequences, sets, cluster operations, and services.

The client sends a `user-agent` attribute in the handshake, and authorization errors now include a description.

### .NET Client

The .NET client adds the following:

- Asynchronous API parity with the Java API, including asynchronous service calls.
- `IAsyncDisposable` support.
- `IAsyncEnumerable` for query cursors, continuous queries, and the data streamer.
- `CommitAsync()` and `RollbackAsync()` for thin client transactions.
- `HandshakeTimeout` and `RequestTimeout` properties.
- `IDataStreamerClient.AddAsync()`, `ICacheClient.WithSkipStore()`, and `ICacheClient.WithPartitionRecover()`.
- Separate baseline auto-adjust APIs for scale-up and scale-down.

The NuGet package and the archive now ship `netstandard2.0`, `net8.0`, and `net10.0` targets, and the API carries nullable reference type annotations. The change is additive, but projects that enable nullable reference types may see new warnings.

### C++ Client and ODBC Driver

C++ thin client `GetAll` operations now use partition awareness.

The ODBC driver supports protocol version 2.13.0. When `PROTOCOL_VERSION` is not set explicitly, the driver negotiates the version with the server and falls back to an older version if needed.

### Apache Ignite 2 Compatibility

- Apache Ignite thin clients and the Apache Ignite JDBC thin driver can connect to GridGain servers. GridGain servers support the service caller context, compute task node IDs, and continuous query `EXPIRED` events sent by Apache Ignite thin clients.
- The Apache Ignite 2 snapshot API is supported, including cancel, restore, and status operations, and the matching `control.sh --snapshot` commands.
- Apache Ignite 2 change data capture write-ahead log (WAL) records can be read.
- The REST API accepts a `keepBinary` query parameter.
- The JSON permission parser tolerates `SecurityPermission` names that exist only in Apache Ignite.

### Core API

Service call interceptors, the `@ServiceContextResource` annotation, `BinaryObject.size()`, `SystemDataRegionConfiguration`, and a set of Apache Ignite source-compatibility alias methods are added.

### Baseline Auto-Adjust Scale-Up and Scale-Down Timeouts

Baseline auto-adjust now takes separate timeouts for scale-up and scale-down events. The single combined timeout still works, and the split is exposed on every surface:

- `IgniteCluster.baselineAutoAdjustEnabled()`, `baselineAutoAdjustTimeout()`, and `baselineAutoAdjustStatus()` take an `AutoAdjustMode` argument.
- The control script adds the `scale_up_auto_adjust` and `scale_down_auto_adjust` subcommands of `--baseline`.
- `BaselineAutoAdjustMXBean` exposes per-direction enablement, timeouts, time-until-adjust, and task state.
- The .NET `ICluster` API takes the same `AutoAdjustMode`.

### Control Script and REST

No REST command and no control script command was removed or renamed in this release. The control script adds the `--system-view` command, the Apache Ignite 2 compatible `--snapshot` commands, and the baseline auto-adjust scale-up and scale-down options.

### Metrics and System Views

No system view, metric, or metric registry was removed or renamed in this release. New metrics are added for the following:

- Node network unavailability.
- Data region evictions, and cache group inserted and removed bytes.
- Cache metrics carried over from Apache Ignite.
- The TCP communication connection pool and the client connector.
- Partition-aware request hits and misses.
- Index operations, and page read and page replace times.
- Transaction deadlocks.
- Snapshot creation, restore, and check operations.

The following system views are added:

- `SNAPSHOT` - the metadata of the snapshots stored on the local node.
- `SQL_PLANS_HISTORY` - the history of SQL query plans.
- `CACHE_LOCKS` and `CACHE_EXPLICIT_LOCKS` - cache entry locks.
- `PLUGINS` - the plugins configured on the node.

The cache group I/O statistics system view gains two columns, `INSERTED_BYTES` and `REMOVED_BYTES`.

The `IGNITE_TCP_COMM_MSG_QUEUE_WARN_SIZE` and `IGNITE_BPLUS_TREE_DISABLE_METRICS` system properties are added.

### Kafka Sink Skip Store

The Kafka sink connector has a new `skipStore` configuration property. Set it to `true` to write data to the cache without passing it to the configured cache store.

## Improvements and Fixed Issues

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-52767 | Builds and Deliveries | Docker images now accept the `LUCENE_LINE` environment variable, which switches the node from the Lucene 9 line to the Lucene 10 line. |
| GG-52680 | Builds and Deliveries | The distribution now ships the MariaDB Software License Terms. The Apache License 2.0 and Community Edition license files are removed. |
| GG-52547 | General | Updated the stax2-api dependency to version 4.3.0. |
| GG-52531 | Modules and Packaging | The Kubernetes IP finder now uses Jackson 3. |
| GG-52530 | General | Updated Jackson 2 to version 2.22.4. |
| GG-52499 | Platforms & Thin Clients | .NET: Thin client: Fixed `Dispose` becoming unresponsive when background endpoint discovery retries against a stopped cluster. |
| GG-52436 | General | Updated multiple third-party dependencies. |
| GG-52281 | Platforms & Thin Clients | Added support for the Apache Ignite JDBC thin driver connecting to GridGain servers. |
| GG-52249 | Licensing | `GridProduct.updateLicense()` now accepts MariaDB license keys. |
| GG-52121 | Cluster Architecture | Removed local store support. |
| GG-51989 | Platforms & Thin Clients | Address lists now parse and print IPv6 addresses correctly, with clearer parse errors. |
| GG-51945 | Vector Search | Thin clients can pass a field filter and an oversample factor to a vector query. |
| GG-51923 | Platforms & Thin Clients | Fixed the server failing to parse compute task node IDs sent by Apache Ignite 2.x thin clients. |
| GG-51720 | Platforms & Thin Clients | ODBC: The driver now negotiates the protocol version with the server and falls back to an older version if `PROTOCOL_VERSION` is not set explicitly. |
| GG-51652 | General | Updated the Jackson, DJL, Bouncy Castle, AWS SDK, and Hibernate ORM dependencies. |
| GG-51647 | Cluster REST API | The REST HTTP module now runs on Jetty 12 and requires Java 17. The Jetty 9.4 REST module is removed. |
| GG-51631 | Platforms & Thin Clients | Fixed the server not sending continuous query `EXPIRED` events to Apache Ignite 2.x thin clients. |
| GG-51597 | Cluster Metrics & Monitoring | `ObjectMetric` values are now exposed through JMX as strings. |
| GG-51575 | GridGain Integrations | Removed the Mesos integration module. |
| GG-51528 | Platforms & Thin Clients | .NET: Fixed `DataStreamer.DisposeAsync` completion guarantees. |
| GG-51475 | Platforms & Thin Clients | Java thin client: Added SQL cache creation. |
| GG-51473 | Platforms & Thin Clients | Java thin client: Added service awareness. |
| GG-51378 | Platforms & Thin Clients | Added support for the service caller context sent by Apache Ignite Java thin clients. |
| GG-51369 | Modules and Packaging | Removed the `ignite-yardstick` module. |
| GG-51306 | Vector Search | Added configurable segment-size thresholds for Lucene 10 vector query caching. |
| GG-51303 | Modules and Packaging | Removed the `ignite-ml` module. Use the `ignite-ml-ext` Apache Ignite extension instead. |
| GG-51272 | Platforms & Thin Clients | .NET: Thin client: Added round-robin balancing for requests that are not partition-aware. |
| GG-51193 | Cluster Data Replication | Added replication delay and clock skew metrics for data center replication. |
| GG-51186 | Cluster Metrics & Monitoring | Added the `SQL_PLANS_HISTORY` system view, which shows the history of SQL query plans. |
| GG-51178 | Cluster Data Snapshots and Recovery | Added the `SNAPSHOT` system view, which shows the metadata of local snapshots. |
| GG-51145 | Platforms & Thin Clients | C++: Migrated to C++14. |
| GG-51116 | Modules and Packaging | `ignite-spring-data` and `ignite-spring-data-commons` no longer ship in `libs/optional`. Take them from Maven instead. |
| GG-51115 | Modules and Packaging | `ignite-hibernate-7.4` no longer ships in `libs/optional`. Take it from Maven instead. |
| GG-51114 | GridGain Integrations | `gridgain-kafka-connect` now ships only as a Confluent Hub component. |
| GG-51113 | GridGain Integrations | Moved the Oracle GoldenGate integrations out of the server packages into the integrations download. |
| GG-51110 | Builds and Deliveries | Added a separate integrations download. |
| GG-51109 | Modules and Packaging | Moved `ignite-opencensus` from `libs` to `libs/optional`. |
| GG-51108 | Modules and Packaging | Removed the Hadoop and Snowflake dependencies from `gridgain-bulkload`. |
| GG-51107 | Modules and Packaging | Removed the AWS SDK `bundle` jar from `gridgain-bulkload`. |
| GG-51066 | Cluster Metrics & Monitoring | Custom metric and registry names are now limited in length. |
| GG-51064 | Cluster Security | Added the `CUSTOM_METRICS_MANAGE` permission. |
| GG-51061 | Cluster Metrics & Monitoring | Added the custom metrics API. |
| GG-51057 | Platforms & Thin Clients | Java thin client: Cache argument validation errors are no longer wrapped in other exceptions. |
| GG-50943 | Vector Search | Added `int8` vector storage, a configurable segment target, query thread count, and deleted-vector budget. |
| GG-50942 | Vector Search | Vector queries now take a single parameter object with the filter, keys-only flag, and oversample factor. |
| GG-50928 | Platforms & Thin Clients | Java and .NET thin clients now send a `client.user-agent` attribute in the handshake. |
| GG-50925 | Platforms & Thin Clients | Added support for Apache Ignite thin clients connecting to GridGain servers. |
| GG-50765 | Platforms & Thin Clients | Java thin client: Internal retries no longer block the common `ForkJoinPool` while they wait for network requests. |
| GG-50709 | Modules and Packaging | Renamed the `ignite-spring-data_2.2` module to `ignite-spring-data`. |
| GG-50696 | Platforms & Thin Clients | Improved partition awareness for bulk operations in thin clients. |
| GG-50687 | Modules and Packaging | The examples now compile to Java 17. |
| GG-50628 | Cluster Control Script | The schema import scripts can load data into the imported tables with `COPY` statements. |
| GG-50593 | Platforms & Thin Clients | Java thin client: Added an asynchronous variant of `ClientDataStreamer.flush()`. |
| GG-50555 | Modules and Packaging | Removed the Gridify API from `ignite-core`. |
| GG-50497 | Modules and Packaging | Removed the internal `gridgain-yardstick` and `benchmark-yardstick` modules. Neither was published to Maven or shipped in a distribution. |
| GG-50496 | Modules and Packaging | Removed the internal `gridgain-tools` module. It was never published to Maven or shipped in a distribution. |
| GG-50494 | Modules and Packaging | Removed the internal `gridgain-diagnostic` module. It was never published to Maven or shipped in a distribution. |
| GG-50453 | Cluster Security | Thin client continuous query filters are now checked against the marshaller class filter on every path. |
| GG-50444 | Control Center Agent | The Control Center agent now runs on Spring 7 and Jakarta WebSocket (Tyrus 2). |
| GG-50436 | Platforms & Thin Clients | .NET: Added `ICacheClient.WithPartitionRecover`. |
| GG-50434 | Platforms & Thin Clients | .NET: Added `ICacheClient.WithSkipStore`. |
| GG-50382 | Cluster SQL Engine | `COPY ... FORMAT JDBC` now restricts JDBC URL schemes and connection parameters, and no longer expands environment variables by default. |
| GG-50369 | GridGain Integrations | Kafka sink: Added the `skipStore` configuration property. |
| GG-50326 | Modules and Packaging | Removed the `ignite-spring-6` module. `ignite-spring` now targets Spring 7. |
| GG-50287 | Platforms & Thin Clients | Java thin client: Added `withPartitionRecover()` to the cache API. |
| GG-50269 | Modules and Packaging | Removed the `ignite-aws` module. Use the `ignite-aws-ext` Apache Ignite extension instead. |
| GG-50267 | Platforms & Thin Clients | .NET: Thin client: Added support for `async`/`await` in transaction blocks. |
| GG-50220 | Modules and Packaging | The Spring Data module now targets Spring Data 4.1 on Spring 7. |
| GG-50052 | Platforms & Thin Clients | Java thin client: Improved security-related error messages. |
| GG-50047 | Platforms & Thin Clients | Java thin client: Added default values for the handshake and request timeouts. |
| GG-50030 | Platforms & Thin Clients | C++: `GetAll` operations now use partition awareness. |
| GG-50029 | Platforms & Thin Clients | .NET: Thin client: Improved `GetAll` performance with a partition-aware per-node split. |
| GG-50024 | Control Center Agent | The Control Center agent now requires JDK 17 or later. |
| GG-49999 | Licensing | MariaDB license keys without an expiry date are now rejected. |
| GG-49995 | Modules and Packaging | Removed the optional `ignite-ssh` module. |
| GG-49970 | Platforms & Thin Clients | .NET: Added `IDataStreamerClient.AddAsync` for fully asynchronous streaming. |
| GG-49956 | Vector Search | Fixed a `CorruptIndexException` on text and vector indexes. |
| GG-49920 | Cluster Security | Improved tolerance to Apache Ignite permissions that GridGain does not know. |
| GG-49829 | Cluster Discovery | Fixed discovery repeatedly retrying a peer that accepts a connection and drops it on Java 17. |
| GG-49820 | Cluster Metrics & Monitoring | Added page read time and page replace time metrics. |
| GG-49762 | Cluster Data Snapshots and Recovery | Added support for the Apache Ignite 2 snapshot API for restore, cancel, and status operations. |
| GG-49741 | Platforms & Thin Clients | .NET: Added separate baseline auto-adjust APIs. |
| GG-49715 | Platforms & Thin Clients | Java thin client: Added asynchronous overloads to the `ClientServices` API. |
| GG-49714 | Platforms & Thin Clients | Java thin client: Added asynchronous overloads to the `ClientCluster` API. |
| GG-49712 | Platforms & Thin Clients | Java thin client: Added asynchronous overloads to the `ClientIgniteSet` API. |
| GG-49711 | Platforms & Thin Clients | Java thin client: Added asynchronous overloads to the `ClientAtomicSequence` API. |
| GG-49710 | Platforms & Thin Clients | Java thin client: Added asynchronous overloads to the `ClientAtomicLong` API. |
| GG-49673 | Vector Search | Added a no-copy vector scorer for the Lucene 10 line on Java 22 or later. |
| GG-49668 | Vector Search | A vector query now rejects a neighbor count that is not positive or exceeds the `GRIDGAIN_VECTOR_MAX_K` limit. |
| GG-49664 | Cluster SQL Engine | Server-side `COPY` against a file or an object store is now disabled by default and requires the new `COPY_FROM_FILE` and `COPY_TO_FILE` permissions. |
| GG-49663 | Cluster REST API | REST error responses no longer include server stack traces. |
| GG-49660 | Cluster REST API | The REST scan query command now accepts only filter classes listed in the `IGNITE_REST_SCAN_QUERY_FILTER_CLASSES` system property. |
| GG-49650 | Cluster Data Replication | Added support for reading Apache Ignite 2 change data capture WAL records. |
| GG-49603 | Platforms & Thin Clients | .NET: Thin client: Added `CommitAsync` and `RollbackAsync`. |
| GG-49600 | Cluster Metrics & Monitoring | Added the `tx.txDeadlocks` metrics. |
| GG-49588 | Platforms & Thin Clients | .NET: Thin client: Added `HandshakeTimeout` and `RequestTimeout`. |
| GG-49567 | GridGain Integrations | Updated the Cassandra serializers dependencies. |
| GG-49566 | GridGain Integrations | The Cassandra store now uses DataStax Java driver 4.17.0 and Cassandra 5.0.8. |
| GG-49548 | Vector Search | Vector queries on PARTITIONED caches now run on every node and merge the results. |
| GG-49547 | Vector Search | Vector search now works on PARTITIONED caches for local queries. |
| GG-49543 | Vector Search | HNSW `M` and `efConstruction` can now be set per index. |
| GG-49541 | Vector Search | Vector indexes now accept up to 4096 dimensions by default, configurable with `GRIDGAIN_VECTOR_MAX_DIMENSIONS`. |
| GG-49538 | Cluster Metrics & Monitoring | Added the `snapshot`, `snapshot-restore`, and `snapshot-check` metric registries. |
| GG-49537 | Cluster Metrics & Monitoring | Added metrics for index operations. |
| GG-49536 | Cluster Metrics & Monitoring | Added metrics for partition-aware request hits and misses. |
| GG-49535 | Cluster Metrics & Monitoring | Added metrics for the TCP communication connection pool. |
| GG-49534 | Cluster Metrics & Monitoring | Added cache metrics. |
| GG-49520 | Cluster Control Script | Added control script commands and baseline MXBean methods that control baseline auto-adjust separately for scale-up and scale-down. |
| GG-49474 | Cluster Data Snapshots and Recovery | Added a compatibility layer for Apache Ignite 2 snapshot creation scripts and clients. |
| GG-49429 | Vector Search | Added binary quantization with full-precision rescoring. |
| GG-49389 | Cluster Control Script | Added the `--system-view` command. |
| GG-49388 | Cluster REST API | Added the `keepBinary` REST query parameter. |
| GG-49387 | Cluster Metrics & Monitoring | Added the `txDeadlocks` transaction metric. |
| GG-49386 | Platforms & Thin Clients | Java thin client: `ClientConfiguration` now supports separate handshake and request timeouts. |
| GG-49330 | Cluster Service Grid | Service implementations can now inject their `ServiceContext` through the new `@ServiceContextResource` annotation. |
| GG-49327 | GridGain Integrations | Removed the Hibernate integration modules for Hibernate 4.2, 5.1, and 5.3. |
| GG-49286 | Vector Search | Thin client vector queries can set the search beam width, return a similarity score with each row, and omit values from result rows. |
| GG-49285 | Vector Search | Vector query results now expose the similarity score of each match through the `ScoredCacheEntry` interface. |
| GG-49270 | Platforms & Thin Clients | .NET: Added continuous query overloads that expose the event stream as `IAsyncEnumerable`. |
| GG-49269 | Platforms & Thin Clients | .NET: Added `AddAsync(IAsyncEnumerable)` to `IDataStreamerClient`. |
| GG-49229 | Modules and Packaging | JDK 17 or later is now required to build and run GridGain. |
| GG-49130 | General | Apache Ignite system properties that GridGain does not support are now logged as warnings at node start. |
| GG-49129 | General | An unknown property in the Spring XML configuration now fails startup with a message that names the bean and the property. |
| GG-49117 | Platforms & Thin Clients | .NET: Added asynchronous support to services: service interfaces and implementations can now use `Task`, `Task<T>`, `ValueTask`, and `ValueTask<T>` method signatures. |
| GG-49066 | Platforms & Thin Clients | Java thin client: Added the `ClientStartEvent`, `ClientStopEvent`, and `ClientFailEvent` lifecycle events. |
| GG-49065 | Cluster Service Grid | Added support for service call interceptors. |
| GG-49064 | Platforms & Thin Clients | Java thin client: `ClientServices.serviceProxy()` now accepts a `ServiceCallContext`. |
| GG-49063 | Platforms & Thin Clients | Java thin client: Added `ClientCache.sizeLong()` and `sizeLongAsync()`, which return the cache size as a `long`. |
| GG-49062 | Binary Objects | Added `BinaryObject.size()`, which returns the size in bytes of the serialized binary form of the object. |
| GG-49060 | General | Improved configuration compatibility with Apache Ignite. |
| GG-49043 | Platforms & Thin Clients | .NET: Added nullable reference type annotations. |
| GG-48579 | Cluster Control Script | Added the `schema-import.sh` and `schema-import.bat` scripts, which generate GridGain DDL from the schema of an external database. |
| GG-48577 | Cluster SQL Engine | `COPY ... FORMAT JDBC` can now load data from MariaDB. |
| GG-48573 | GridGain Integrations | Added a MariaDB cache store. |
| GG-48571 | Licensing | Added license soft mode. |
| GG-48567 | Licensing | Added support for the MariaDB license key format. |
| GG-48504 | Platforms & Thin Clients | Java thin client: Transactional operations are now partition-aware. |
| GG-48502 | Platforms & Thin Clients | Java thin client: When a host name resolves to several addresses, the client now connects to all of them. |
| GG-48501 | Platforms & Thin Clients | .NET: Improved hostname resolution logic. |
| GG-48494 | Platforms & Thin Clients | .NET: Thin client: Added continuous query overloads that expose the event stream as `IAsyncEnumerable`. |
| GG-48493 | Platforms & Thin Clients | .NET: Added `IAsyncEnumerable<T>` to query cursors, so that SQL, scan, and cache query results can be streamed asynchronously. |
| GG-48492 | Platforms & Thin Clients | .NET: Added `IAsyncDisposable` support to cursors, queries, and transactions. |
| GG-48491 | Platforms & Thin Clients | .NET: Added asynchronous methods for all I/O-bound thin client APIs. |
| GG-48490 | Platforms & Thin Clients | .NET: Added nullable reference type annotations. |
| GG-48489 | Platforms & Thin Clients | .NET: Added `net8.0` and `net10.0` binaries to the NuGet and archive deployments. |
| GG-48454 | Platforms & Thin Clients | Java thin client: Added support for data streaming. |
| GG-48357 | Cluster Metrics & Monitoring | Added the `CACHE_LOCKS`, `CACHE_EXPLICIT_LOCKS`, and `PLUGINS` system views. |
| GG-44256 | Platforms & Thin Clients | Fixed a possible `NullPointerException` when a thin client starts a transaction. |
| GG-43641 | Binary Objects | Binary metadata fields and the affinity key are now matched by field ID instead of by name. |
| GG-41738 | Platforms & Thin Clients | Fixed the thin client not receiving the stack trace when a compute task fails in the map phase. |
| GG-40177 | Platforms & Thin Clients | Java thin client: `ClientConnectionException` now includes the address of the server. |
| GG-37683 | Platforms & Thin Clients | Java thin client: Deprecated the rebalance-related methods of `ClientCacheConfiguration`. |
| GG-37127 | Cluster Baseline Topology | Added a Java API that controls baseline auto-adjust separately for scale-up and scale-down. |
| GG-35947 | Cluster Storage Engine | Added methods that set the system data region configuration. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

### Older GridGain Versions Compatibility

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.9.16`, `8.9.16-p1`, `8.9.16-p2`, `8.9.16-p3`, `8.9.17`, `8.9.17-p1`, `8.9.18`, `8.9.19`, `8.9.20`, `8.9.20-p1`, `8.9.21`, `8.9.22`, `8.9.22-p1`, `8.9.22-p2`, `8.9.23`, `8.9.24`, `8.9.25`, `8.9.26`, `8.9.27`, `8.9.28`, `8.9.29`, `8.9.30`, `8.9.31`, `8.9.32`, `8.9.33`, `8.9.34`, `8.9.35`, `8.9.36`, `8.9.37`, `8.9.38`, `8.9.39`

{% hint style="info" %}
Rolling upgrade is only possible if both nodes have the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` property manually set to the same value. Due to the change to the default value, rolling upgrade will fail unless actions are taken.
{% endhint %}

### Older Thin Clients Compatibility

In most cases, older versions of thin clients should be compatible with newer versions of GridGain.
Below is the list of versions of thin clients that are tested for compatibility with the latest version.
The compatibility also means that you can safely update from any version on the list to any subsequent version.

`8.9.16`, `8.9.16-p1`, `8.9.16-p2`, `8.9.16-p3`, `8.9.17`, `8.9.17-p1`, `8.9.18`, `8.9.19`, `8.9.20`, `8.9.20-p1`, `8.9.21`, `8.9.22`, `8.9.22-p1`, `8.9.22-p2`, `8.9.23`, `8.9.24`, `8.9.25`, `8.9.26`, `8.9.27`, `8.9.28`, `8.9.29`, `8.9.30`, `8.9.31`, `8.9.32`, `8.9.33`, `8.9.34`, `8.9.35`, `8.9.36`, `8.9.37`, `8.9.38`, `8.9.39`

### Apache Ignite Versions Compatibility

Below is a list of versions that are tested for basic compatibility with the current version. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`2.11.1`, `2.12.0`, `2.13.0`,  `2.14.0`,  `2.15.0`,  `2.16.0`,  `2.17.0`,  `2.18.0`

Apache Ignite thin clients are not compatible with GridGain. When switching to GridGain, follow the [migration instructions](https://www.gridgain.com/docs/gridgain8/latest/installation-guide/migrating-from-ignite) to switch to GridGain clients.

### Known Limitations

#### LEFT OUTER JOIN Behavior Change in GridGain 8.9.31

GridGain 8.9.31 fixes an issue in which the `WHERE` conditions could be incorrectly pushed down into the right branch of LEFT OUTER JOIN operations during query optimization. This optimization could cause queries to return incorrect results by effectively converting `LEFT OUTER JOIN` operations into `INNER JOIN`.

Starting with GridGain 8.9.31, the query optimizer correctly prevents `WHERE` conditions from being pushed down into the right branch of `LEFT OUTER JOIN`, ensuring that queries return the correct results according to SQL standards.

If your environment expects incorrect results, you set the new `DIGNITE_FORCE_PUSHDOWN_CONDITIONS_TO_LEFT_JOIN` system property to `true` on each node in your cluster. Review all affected queries and update them as needed before removing this property.

#### Changed Permissions for Control Center Agent in GridGain 8.9.4 and Later

GridGain 8.9.4 introduced stricter permissions checking for Control Center Agent. When running secured clusters, some actions that previously were available without permissions, will now require additional permissions.

Before updating, make sure to provide the [required permissions](https://www.gridgain.com/docs/control-center/latest/gg8/auth/authorization-permissions), otherwise some actions may become unavailable.

#### New TRACING_CONFIGURATION_UPDATE Permission in GridGain 8.9.2 and Later

GridGain 8.9.2 introduced the `TRACING_CONFIGURATION_UPDATE` [permission](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/security/authorization-permissions). If you were using security on a cluster before updating to this version, make sure that you provide the permissions to control utilities or users who need to update cluster permissions. Otherwise, they will not be able to update

#### Changed Default Values in GridGain 8.9.1 and Later

{% hint style="danger" %}
The change to `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` prevents rolling upgrade from earlier versions to GridGain 8.9.1 unless the value is manually configured to be `false`. For more information on changing service processor implementation, see [Services](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/services/services#new-igniteservices-framework) documentation.
{% endhint %}

If you are updating from GridGain 8.8.X or 8.9.0, a large number of default values have been changed.

These changes may affect the stability or performance of your cluster if you are using default values.

We recommend checking the list below to make sure the changes do not have an adverse effect, and setting the value manually if necessary.

- Service processor now use event-driven implementation by default. You can keep the old behavior by setting the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLE` property to `false`. Make sure that all nodes in the cluster are set to the same value. See [Services](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/services/services#new-igniteservices-framework) documentation for more information.
- Data region metrics are now enabled by default. This may have a minor (within 2%) adverse effect on performance. You can keep the old behavior by setting the `DataRegionConfiguration.metricsEnabled` value to `false`.
- Data storage metrics are now enabled by default. This may have a minor (within 2%) adverse effect on performance. You can keep the old behavior by setting the `DataStorageConfiguration.metricsEnabled` value to `false`.
- `TcpCommunicationSpi` communication protocol now has a limit of 4096 messages for the outgoing messages queue by default.
- Atomic operations are now not allowed in transactions by default. You can keep the old behavior by setting the `IGNITE_ALLOW_ATOMIC_OPS_IN_TX` value to `true`.
- Logs are now in verbose mode by default. You can use the `-q` command line argument in the `ignite.sh` script to keep current log behavior.
- SQL queries are now loaded lazily by default. This reduces memory consumption on medium and large queries and potentially improves garbage collection performance. You can keep the old behavior by setting the `SqlFieldsQuery.setLazy(false)`.
- Cache entries are now read from primary partitions by default, even if an entry is available on the node in a backup partition. This may have a minor performance impact, but significantly increases cluster stability. You can keep the old behavior by setting the `readFromBackup` property to `true`.
- Partition map exchange transactions now time out after 1 minute instead of 0 (infinite) by default. You can keep the old timeout by setting the `TX_TIMEOUT_ON_PARTITION_MAP_EXCHANGE` setting to 0.
- Data streamer now overwrites entries by default. You can keep the old behavior by setting the `stmr.allowOverwrite` property to `false`.
- TCP discovery now uses static IP finder `TcpDiscoveryVmIpFinder` by default. To keep the old behavior, set the IP finder to use [multicast IP finder](https://www.gridgain.com/docs/gridgain8/latest/developers-guide/clustering/tcp-ip-discovery#multicast-ip-finder).
- Checkpointing process now starts upon reaching 75% of `minWalArchiveSize` instead of 25%. You can keep the old behavior by setting the `IGNITE_CHECKPOINT_TRIGGER_ARCHIVE_SIZE_PERCENTAGE` system variable to `0.25`.
