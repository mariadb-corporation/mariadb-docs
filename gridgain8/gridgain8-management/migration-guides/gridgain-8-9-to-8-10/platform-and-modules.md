---
description: >-
  Platform changes when upgrading from GridGain 8.9 to 8.10: Java 17, removed modules and integrations, upgraded dependencies, and distribution and packaging changes.
---

# Platform, Modules, and Packaging Changes

## Java 17 or Later

GridGain 8.10 requires Java 17 or later and supports Java 17, 21, and 25. GridGain 8.9.x supported Java 8, 11, 17, and (starting with 8.9.10) 21. The requirement applies to servers, thick clients, applications that embed a node, the Java thin client, and the JDBC thin driver.

- `ignite.sh`, `ignite.bat`, `control.sh`, and `control.bat` refuse to start on a JVM older than 17.
- The .NET client in thick mode starts a JVM and fails if `JAVA_HOME` points at an older JDK. The .NET thin client, the C++ client, and the ODBC driver do not use a JVM.
- An application that embeds the Control Center agent also needs Java 17.

Install Java 17 or later on every server host before you upgrade, and move each application to Java 17 before it uses the 8.10 libraries. A running 8.9 node can stay on its current Java until you restart it from the 8.10 distribution.

## Removed Modules and Integrations

This section applies if your application or configuration uses one of the modules below.

The following modules are removed in GridGain 8.10. Take the action in the *What to use instead* column, or stay on GridGain 8.9.x.

| Removed | What to use instead | Deprecated in 8.9.x |
| --- | --- | --- |
| `ignite-hibernate-4.2`, `ignite-hibernate-5.1`, `ignite-hibernate-5.3`, `ignite-hibernate-core` | `ignite-hibernate-7.4`. See [Hibernate 7 Required](#hibernate-7-required). | 8.9.35 |
| `ignite-spring-6` | `ignite-spring` on Spring 7. See [Spring 7 Required](#spring-7-required). | Not deprecated |
| `ignite-lucene-8` | `ignite-lucene-9`, or the Lucene 10 line in `libs/optional`. See [Lucene](#lucene). | Not deprecated |
| `ignite-aop` and the Gridify API in `ignite-core` | The [compute API](../../../gridgain8-development/distributed-computing/distributed-computing.md). See [Gridify API Removed](#gridify-api-removed). | 8.9.37 |
| `ignite-cloud` (`TcpDiscoveryCloudIpFinder`) | Another [IP finder](../../clustering/discovery-in-the-cloud.md). | 8.9.37 |
| `ignite-ssh` | Contact GridGain Support if you use `IgniteCluster.startNodes()`. See [SSH Module Removed](#ssh-module-removed). | Not deprecated |
| `ignite-aws` (S3 checkpoint SPI, S3, ELB, and ALB IP finders, S3 IP finder encryption) | The Apache Ignite `ignite-aws-ext` extension. See [AWS Module Removed](#aws-module-removed). | 8.9.39 |
| `ignite-mesos` | None. Mesos deployments stay on 8.9.x. | 8.9.39 |
| `ignite-ml`, `ignite-ml-spark-model-parser`, `ignite-ml-xgboost-model-parser`, `ignite-ml-mleap-model-parser` | The Apache Ignite `ignite-ml-ext` extension or the standalone GridGain ML download. See [Machine Learning Module Removed](#machine-learning-module-removed). | 8.9.38 |
| `gridgain-diagnostic`, `gridgain-tools`, `gridgain-yardstick` (Enterprise and Ultimate) | None. | Not deprecated |
| Local store support (`@CacheLocalStore`, `CacheFileLocalStore`) | Native persistence or a regular `CacheStore`. See [Local Store Support Removed](#local-store-support-removed). | `IGNITE_LOCAL_STORE_KEEPS_PRIMARY_ONLY` and `CacheFileLocalStore` in 8.9.39 |

The following modules are not removed in 8.10 and still ship in `libs/optional`: `ignite-cassandra-store`, `ignite-cassandra-serializers`, `ignite-kubernetes`, `ignite-zookeeper`, `ignite-gce`, `ignite-jta`, `ignite-yarn`, `ignite-compress`, and `ignite-direct-io`.


### Gridify API Removed

This section applies if you use `@Gridify`.

The Gridify API is removed from `ignite-core`, together with the `ignite-aop` module. This covers the `org.apache.ignite.compute.gridify` package, including `@Gridify`, `@GridifySetToSet`, and `@GridifySetToValue`. Replace Gridify usage with the [compute API](../../../gridgain8-development/distributed-computing/distributed-computing.md).

### SSH Module Removed

This section applies if you start remote nodes with `IgniteCluster.startNodes()` or `startNodesAsync()`.

The `ignite-ssh` module is removed and no longer ships in `libs/optional`. The `org.gridgain:ignite-ssh` artifact is no longer published. `IgniteCluster.startNodes()` and `startNodesAsync()` remain in the API, but they need an SSH implementation on the node classpath. Without one, `startNodes()` throws an `IgniteException` with the message `Failed to create Ignite component (consider adding ignite-ssh module to classpath)`.

Contact GridGain Support before you upgrade.

### AWS Module Removed

This section applies if you use the S3 checkpoint SPI, or the S3, ELB, or ALB IP finders.

The `ignite-aws` module is removed. It contained the following classes, which are no longer bundled:

- `org.apache.ignite.spi.checkpoint.s3.S3CheckpointSpi`
- `org.apache.ignite.spi.discovery.tcp.ipfinder.s3.TcpDiscoveryS3IpFinder`
- `org.apache.ignite.spi.discovery.tcp.ipfinder.elb.TcpDiscoveryElbIpFinder`
- `org.apache.ignite.spi.discovery.tcp.ipfinder.elb.TcpDiscoveryAlbIpFinder`
- The `EncryptionService` classes that the S3 IP finder uses: `AsymmetricKeyEncryptionService`, `SymmetricKeyEncryptionService`, and `AwsKmsEncryptionService`.

A configuration that references any of them fails with `ClassNotFoundException` until the Apache Ignite `ignite-aws-ext` extension is on the classpath. These classes are marked `@Deprecated` in GridGain 8.9.39, and the javadoc carries the migration notes below.

The extension defines the same class names as `ignite-aws`, so do not use both. Remove `ignite-aws` first (the `libs/ignite-aws` folder of a standalone node, or the `ignite-aws` dependency of a Maven project), and only then add `ignite-aws-ext`. If both are on the classpath, two jars define the same classes and the classpath order decides which one is loaded.

The extension is not a drop-in replacement:

- *Maven coordinates.* `org.gridgain:ignite-aws` stops resolving, so a Maven or Gradle build fails. Use `org.apache.ignite:ignite-aws-ext:1.0.0` instead. The group ID is different, and the classes keep their `org.apache.ignite.*` packages, so imports do not change. You do not need an `<exclusion>`: the extension declares `org.apache.ignite:ignite-core` with `provided` scope, which is not transitive.
- *Region setter.* `AwsKmsEncryptionService` has only `setRegion(Region)` in the extension, and no `setRegion(String)`. A Spring XML file that passes a plain region string fails. Use a `RegionUtils.getRegion` factory bean instead.
- *Older dependencies.* The extension (1.0.0) bundles older libraries than `ignite-aws`, including AWS SDK 1.11.75 and `jackson-databind` 2.12.4. Check them against your security requirements before you switch.
- *AWS Encryption SDK version.* The extension's KMS support works only with AWS Encryption SDK 1.x (it pins 1.3.2, without key commitment) and fails with `NoSuchMethodError` on the 2.x SDK that `ignite-aws` ships. If your application uses the 2.x SDK, it cannot use the extension's KMS service.
- *S3 IP finder with `AwsKmsEncryptionService`.* The extension cannot decrypt the key-committed ciphertext that `ignite-aws` wrote with AWS Encryption SDK 2.4.0, and `ignite-aws` rejects the extension's ciphertext. Nodes on the two modules cannot read each other's entries, and the failure stops a node from joining. Switch every node, thick clients included, at once, and set a fresh `keyPrefix` on the IP finder. Entries that the old nodes left in the bucket are not cleaned up by the new ones. This cannot be done as a rolling upgrade. The symmetric and asymmetric key services do not use the SDK and are not affected.

### Machine Learning Module Removed

This section applies if you use `ignite-ml` or one of its model parsers.

The `ignite-ml` module is removed together with `ignite-ml-spark-model-parser`, `ignite-ml-xgboost-model-parser`, and `ignite-ml-mleap-model-parser`. The module was deprecated in 8.9.38: every public type in `org.apache.ignite.ml.**` carries `@Deprecated`.

Switch to the Apache Ignite `ignite-ml-ext` extension (version 1.0.0, tested against GridGain 8.9 and 8.10) or to the standalone GridGain ML download.

### Local Store Support Removed

This section applies if you use `@CacheLocalStore`, `CacheFileLocalStore`, or the `IGNITE_LOCAL_STORE_KEEPS_PRIMARY_ONLY` system property.

The local store is removed: `@CacheLocalStore`, `CacheFileLocalStore` (Enterprise), and the `IGNITE_LOCAL_STORE_KEEPS_PRIMARY_ONLY` system property no longer exist. Use native persistence or a regular `CacheStore`, and remove the system property from your start scripts.

## Dependency Upgrades

### Hibernate 7 Required

This section applies if you use the Hibernate second-level cache.

The Hibernate second-level cache module targets Hibernate 7.4 and is named `ignite-hibernate-7.4`. Applications on Hibernate 4.2, 5.1, or 5.3 must move to Hibernate 7.4 or stay on GridGain 8.9.x.

### Spring 7 Required

This section applies if your application embeds GridGain through Spring.

GridGain 8.10 builds against Spring Framework 7.0.9 and Spring Data 4.1.0. The `ignite-spring` and `ignite-spring-data` modules are compiled to Java 17 bytecode and target Spring 7. Spring 5 and Spring 6 are no longer supported, and `ignite-spring-6` is removed.

An application that embeds GridGain through Spring must be on Spring 7. Otherwise, stay on GridGain 8.9.x, which keeps the Spring 5 and Spring 6 modules.

The Control Center agent also runs on Spring 7 (7.0.9) and Tyrus 2. An agent embedded in an application on Spring 5 or Spring 6 does not start. Upgrade the host application or keep using the 8.9.x agent.

The `ignite-spring-data_2.2` module is also renamed to `ignite-spring-data`, and its package changes from `org.apache.ignite.springdata22` to `org.apache.ignite.springdata`.

1. Change the artifact ID in your build files from `ignite-spring-data_2.2` to `ignite-spring-data`.
2. Update the imports of `IgniteRepository`, `@EnableIgniteRepositories`, `@RepositoryConfig`, `@Query`, and the other classes of the module.

### Lucene

This section applies if you run `ignite-lucene-8`, or if you want to use Lucene 10.

The `ignite-lucene-8` module is removed. If you still run it (the Java 8 workaround documented for GridGain 8.9.18 and later put it in `libs`), move to the Lucene 9 line before you upgrade. Do not copy `ignite-lucene-8` to the 8.10 distribution.

The 8.10 package ships two Lucene lines. The Lucene 9 line (Lucene 9.10.0) is active by default, and the Lucene 10 line (Lucene 10.4.0) is in `libs/optional`, where it stays inactive until you move it. There is no separate Lucene 10 download. If you upgrade without changing anything, the node behaves as it did on 8.9: `ignite-lucene-9` is in `libs` and serves full-text search. Vector search also needs `gridgain-vector-query` (Enterprise and Ultimate), which ships in `libs/optional`, as in 8.9.x, until you move it into `libs`.

| Folder in `libs/optional` | Requires | Editions |
| --- | --- | --- |
| `ignite-lucene-10` | JDK 21 or later | Enterprise, Ultimate |
| `ignite-lucene-10-java22` | JDK 22 or later. Adds an opt-in scorer that reads vectors from off-heap memory. See the `README.txt` in the folder for the JVM options. | Enterprise, Ultimate |
| `gridgain-vector-query-lucene-10` | The Lucene 10 line. Pairs with it only. | Enterprise, Ultimate |

The z/OS package does not ship the Lucene 10 line.

The Lucene 10 line replaces `ignite-lucene-9`, it does not add to it. The two use the same class names, so a node must run exactly one line, and every node in a cluster must run the same line. Two lines on one classpath fail to link at the first index the node touches (for example with `NoSuchFieldError`), and so does a Lucene 10 line paired with the Lucene 9 vector module (`ClassNotFoundException: ...Lucene99HnswScalarQuantizedVectorsFormat`). A cluster that mixes them returns different vector search recall depending on which node serves the query, because Lucene 10.4 scores a small segment exhaustively where Lucene 9.10 walks a graph.

To switch a node to Lucene 10:

1. Stop the node.
2. Move the `libs/ignite-lucene-9` folder out of `libs`, for example to `libs/optional`. Do not delete it: no other folder of the package holds it, and you need it to go back.
3. Move one of `ignite-lucene-10` (JDK 21 or later) or `ignite-lucene-10-java22` (JDK 22 or later) from `libs/optional` into `libs`.
4. If you use vector search on Enterprise or Ultimate, move `libs/gridgain-vector-query` back to `libs/optional`, and move `libs/optional/gridgain-vector-query-lucene-10` into `libs`.
5. Start the node.

Finish the upgrade to 8.10 on the Lucene 9 line first, and switch lines afterward on every node. Switching during the rolling upgrade would put two lines in one cluster.

To go back to Lucene 9, reverse the steps: move the Lucene 10 folders back to `libs/optional`, and move `ignite-lucene-9` (and `gridgain-vector-query`, if you use it) back into `libs`. The Lucene index is held in memory and rebuilt from the cache data, so switching lines does not migrate or invalidate anything on disk.

### Jetty 12 Is the Only REST Implementation

This section applies if you use a custom Jetty XML file with the REST connector.

The `ignite-rest-http` module now runs on Jetty 12 (12.0.40) and requires Java 17. The Jetty 9.4 module is removed, and so is the separate `ignite-rest-http-jetty-12` module that GridGain 8.9.x shipped as an option. The module keeps the `ignite-rest-http` artifact name, so dependency declarations do not change.

A configuration that does not set `ConnectorConfiguration.setJettyPath(...)` needs no changes. A custom Jetty XML file written for Jetty 9.4 does not load on Jetty 12, and the node fails to start with `Failed to start Jetty HTTP server` and `IllegalStateException: No matching constructor class org.eclipse.jetty.server.Server`. Migrate it as follows:

1. Rename the `threadpool` argument of the `Server` constructor to `threadPool`, or remove the name and pass the argument by position. A named argument that matches no constructor parameter makes the whole constructor unmatchable.
2. Remove the `<Set name="handler">` block that uses `HandlerCollection` or `HandlerList`. Both classes are removed in Jetty 12, and GridGain installs its own REST handler after your file is applied.

The `DOCTYPE` declaration needs no change.

For HTTPS and mutual TLS, use `org.eclipse.jetty.util.ssl.SslContextFactory$Server` with `SslConnectionFactory` and `HttpConnectionFactory`. `SecureRequestCustomizer` checks the SNI host name by default. Set `sniHostCheck` to `false` on it if the certificate name does not match the bind address. The client certificate chain is available to the REST handler through the SSL session data, not through the Jetty 9 `X509_ATTRIBUTE`.

### Cassandra Store Uses the DataStax Driver 4

This section applies if you use the Cassandra store.

The Cassandra store moves from DataStax Java driver 3.2 to 4.17 (`com.datastax.oss.driver.*`). Cassandra 2.1 or later is required: native protocol v1 and v2 are no longer supported, and `DataSource.setProtocolVersion()` accepts versions 3 to 6.

The `DataSource` configuration API changed:

- `setLocalDataCenter()` is required when you specify explicit contact points and no custom load balancing policy.
- Policies are configured by class: `setLoadBalancingPolicyClass()`, `setReconnectionPolicyClass()`, `setRetryPolicyClass()`, `setAddressTranslatorClass()`, and `setSpeculativeExecutionPolicyClass()` replace the former instance-based setters.
- `setPoolingOptions()`, `setSocketOptions()`, and `setNettyOptions()` are removed. Use `setConfigFile()` and a driver configuration file.
- `setSslOptions()` is replaced by `setSslEngineFactory()`.
- `user` and `password` are mutually exclusive with `credentials`. Set one or the other.

Update the `DataSource` bean definitions in your Spring XML configuration. Previously serialized `DataSource` instances (those held by dynamically created caches) cannot be read by 8.10. Drop and recreate those caches. Large transactions may reach the Cassandra `batch_size_fail_threshold` setting.

## Distribution and Packaging Changes

You build the 8.10 `libs` folder from the new distribution.

- *Integrations move out of the server packages.* The `integration` folder is no longer in any server package. The Oracle GoldenGate integrations (`gridgain-goldengate`, `gridgain-goldengate-12.2`, and `gridgain-goldengate-19`) are in the separate `gridgain-integrations-<version>.zip` download, under the same `integration/` paths. They run on the Oracle GoldenGate host, not on a GridGain node, so copy the folder for your GoldenGate version to that host and follow its `README.txt`. `gridgain-kafka-connect` is not in any zip. Install it from Confluent Hub with `confluent-hub install gridgain/gridgain-kafka-connect:latest`, using the component version that matches your cluster. The `copy-dependencies.sh` script is removed. On an Ultimate Edition cluster, copy `libs/gridgain-ultimate/*.jar` from the server package into the component's `lib/` folder on every Kafka Connect worker. For source connectors with `failoverPolicy=BACKLOG`, also put `gridgain-kafka-connect-<version>.jar` from the component's `lib/` folder into `libs` of every GridGain server node, together with the Kafka `connect-api` and `kafka-clients` jars that match your Connect workers' Kafka version.
- *Maven-only modules.* `ignite-hibernate-7.4`, `ignite-spring-data`, and `ignite-spring-data-commons` are published to Maven only and are no longer in `libs/optional`. They are application libraries that a node does not load, so most deployments only need to depend on them from Maven. If code that uses them runs on a standalone node (for example, a compute task), copy the artifacts and their dependencies into `libs`, skipping jars that `libs` already has.
- *OpenCensus.* `ignite-opencensus` moves from `libs` to `libs/optional`. To keep OpenCensus tracing, move the `ignite-opencensus` folder back into `libs`.
- *Control Center agent.* `control-center-agent` is in `libs/optional` in 8.10. In GridGain 8.9.38 and earlier it was in `libs`, so a node of those versions loaded it by default. In 8.9.39 it already ships in `libs/optional`. A node started from the 8.10 distribution does not load the agent, and does not connect to Control Center, until you move the `control-center-agent` folder into `libs`.
- *Bulk load.* `gridgain-bulkload` stays in `libs/optional` of the Enterprise, Ultimate, and z/OS packages. You still enable it by moving it into `libs`. It is now under 100 MB instead of several hundred MB. The AWS SDK `bundle` jar, the Hadoop YARN and HDFS dependencies, and `commons-math3` are removed. The granular `s3`, `sts`, and `glue` clients remain, so reading from S3 still works. Snowflake is not a supported source, and the Snowflake JDBC driver (`snowflake-jdbc`) is no longer bundled. If you added `jdbc:snowflake:` to `GRIDGAIN_BULKLOAD_JDBC_ALLOWED_URL_SCHEMES` or `SnowflakeCatalog` to `importExport.allowedIcebergClasses`, put a Snowflake JDBC driver jar in `libs/gridgain-bulkload/` on every node that uses it. GridGain does not ship or support the driver. Both are closed by default (see [Server-Side SQL COPY](security-and-licensing.md#server-side-sql-copy)).
- *No evaluation license archives.* The Enterprise, Ultimate, and z/OS evaluation-license archives are no longer built.
- *Examples.* Examples are no longer part of the source repository. They are published in the public `gg8-examples` repository and are still bundled into the packages.

<!-- TODO Dmitry Baranov (GG-51118, In Progress): add the link to the integrations download. The text here lists what leaves libs/optional and integration/. -->
