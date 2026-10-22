---
description: >-
  Platform changes when upgrading from GridGain 8.9 to 8.10: Java 17, removed modules and integrations, upgraded dependencies, and distribution and packaging changes.
---

# Platform, Modules, and Packaging Changes

This topic covers the Java baseline, the modules and integrations that GridGain 8.10 removes, the dependencies that move to current versions, and the changes to the distribution layout.

## Java 17 or Later

This section applies to every upgrade.

GridGain 8.10 requires Java 17 or later and supports Java 17, 21, and 25. GridGain 8.9.x supported Java 8, 11, 17, and (starting with 8.9.10) 21. On Java 8, full text search and vector search were not available, and Lucene 9 required replacing `libs/ignite-lucene-9` with `libs/optional/ignite-lucene-8` (see [Lucene](#lucene)). Every artifact is compiled to Java 17 bytecode, so the requirement applies to servers, thick clients, applications that embed a node, the Java thin client, and the JDBC thin driver.

- `ignite.sh`, `ignite.bat`, `control.sh`, and `control.bat` refuse to start on a JVM older than 17.
- The .NET client in thick mode starts a JVM and fails if `JAVA_HOME` points at an older JDK. The .NET thin client, the C++ client, and the ODBC driver do not use a JVM.
- An application that embeds the Control Center agent also needs Java 17.

Upgrade the JVM on every node and every application before you upgrade GridGain.

<!-- CHECK: the per-component enforcement list is from the 8.10.0-b1 release notes. Verified in source: compiler target 17 in parent/pom.xml, and build.sh refuses a JDK older than 17. The scripts' version check was not re-read. -->

## Removed Modules and Integrations

This section applies if your application or configuration uses one of the modules below.

The following modules are removed in GridGain 8.10. Take the action in the *What to use instead* column, or stay on GridGain 8.9.x.

| Removed | What to use instead | Deprecated in 8.9.x |
| --- | --- | --- |
| `ignite-hibernate-4.2`, `ignite-hibernate-5.1`, `ignite-hibernate-5.3`, `ignite-hibernate-core` | `ignite-hibernate-7.4`. See [Hibernate 7 Only](#hibernate-7-only). | 8.9.35 |
| `ignite-spring-6` | `ignite-spring` on Spring 7. See [Spring 7 Only](#spring-7-only). | Not deprecated |
| `ignite-lucene-8` | `ignite-lucene-9`, or the Lucene 10 line in `libs/optional`. See [Lucene](#lucene). | Not deprecated |
| `ignite-aop` and the Gridify API in `ignite-core` | The [compute API](../../../gridgain8-development/distributed-computing/distributed-computing.md). See [Gridify API Removed](#gridify-api-removed). | 8.9.37 |
| `ignite-cloud` (`TcpDiscoveryCloudIpFinder`) | Another [IP finder](../../clustering/discovery-in-the-cloud.md). | 8.9.37 |
| `ignite-ssh` | Contact GridGain Support if you use `IgniteCluster.startNodes()`. See [SSH Module Removed](#ssh-module-removed). | Not deprecated |
| `ignite-aws` (S3 checkpoint SPI, S3, ELB, and ALB IP finders, S3 IP finder encryption) | The Apache Ignite `ignite-aws-ext` extension. See [AWS Module Removed](#aws-module-removed). | 8.9.39 |
| `ignite-mesos` | None. Mesos deployments stay on 8.9.x. | 8.9.39 |
| `ignite-web` (Web Session Clustering: `WebSessionFilter`, `ServletStartup`, `ServletContextListenerStartup`) | None. Applications that cluster HTTP sessions through GridGain stay on 8.9.x. | Not deprecated |
| `ignite-ml`, `ignite-ml-spark-model-parser`, `ignite-ml-xgboost-model-parser`, `ignite-ml-mleap-model-parser` | The Apache Ignite `ignite-ml-ext` extension or the standalone GridGain ML download. See [Machine Learning Module Removed](#machine-learning-module-removed). | 8.9.38 |
| `gridgain-diagnostic`, `gridgain-tools`, `gridgain-yardstick` (Enterprise and Ultimate) | None. | Not deprecated |
| Local store support (`@CacheLocalStore`, `CacheFileLocalStore`) | Native persistence or a regular `CacheStore`. See [Local Store Support Removed](#local-store-support-removed). | `IGNITE_LOCAL_STORE_KEEPS_PRIMARY_ONLY` and `CacheFileLocalStore` in 8.9.39 |

The following modules are not removed in 8.10 and still ship in `libs/optional`: `ignite-cassandra-store`, `ignite-cassandra-serializers`, `ignite-kubernetes`, `ignite-zookeeper`, `ignite-gce`, `ignite-jta`, `ignite-yarn`, `ignite-compress`, and `ignite-direct-io`.

<!-- CHECK: the 8.9.x deprecation versions for Hibernate (8.9.35), Gridify (8.9.37) and ignite-cloud (8.9.37) come from the Confluence page. Verified in origin/8.9-master: GG-51560 (ignite-aws), GG-51574 (Mesos), GG-52246 (local store) are merged for 8.9.39. The 8.10.0-b2 release notes say Mesos was "Not deprecated in the 8.9.x"; the source wins, so the table says 8.9.39. -->
<!-- DECISION (2026-10-22): the source is the reference where it conflicts with release notes or Confluence. -->

<!-- CHECK: gridgain-diagnostic/-tools/-yardstick removal verified (no such modules in ggprivate master). -->
<!-- DECISION (2026-10-22): ignite-web will be removed by the time this guide is released, so the row stays. Re-check master before publishing. Background: ignite-web is NOT removed in source yet. On origin/master e85742c4003, modules/web (artifactId ignite-web) is still in the root pom.xml and assembly/libs/README.txt:86 lists it. The removal ticket is GG-51845 (In Progress, master-next, no PR or branch yet). Its Definition of Done needs Support/Product sign-off that no customer uses it and a deprecation cycle before removal. The row stays because the removal is expected before this guide is published; confirm that it happened, and take the row out if it did not. Conflicting signals: GG-52208 (Open) is a customer request (EU Commission) for ignite-web on WebLogic 15, and it says the module was "marked for removal in 8.10 and deprecation in 8.9". In origin/8.9-master, WebSessionFilter and ServletStartup have no @Deprecated and the module README has no deprecation note, which matches the "Not deprecated" column. -->

### Gridify API Removed

This section applies if you use `@Gridify`.

The Gridify API is removed from `ignite-core`, together with the `ignite-aop` module. This covers the `org.apache.ignite.compute.gridify` package, including `@Gridify`, `@GridifySetToSet`, and `@GridifySetToValue`. Replace Gridify usage with the [compute API](../../../gridgain8-development/distributed-computing/distributed-computing.md).

### SSH Module Removed

This section applies if you start remote nodes with `IgniteCluster.startNodes()` or `startNodesAsync()`.

The `ignite-ssh` module is removed and no longer ships in `libs/optional`. The `org.gridgain:ignite-ssh` artifact is no longer published. `IgniteCluster.startNodes()` and `startNodesAsync()` remain in the API, but they need an SSH implementation on the node classpath. Without one, `startNodes()` throws an `IgniteCheckedException` with the message `Failed to create Ignite component (consider adding ignite-ssh module to classpath)`.

Contact GridGain Support before you upgrade.

<!-- DECISION (Dmitry Baranov via user, 2026-10-21): the guide does not name the Apache ignite-ssh-ext extension. Customers who need SSH contact GridGain, which provides an external extension. Do not add instructions to build ignite-ssh-ext (it is not published to Maven Central and has no release tag), and do not document the JAVA_HOME or setsid differences: they belong to the extension that GridGain supplies. Verified in source (origin/master e85742c4003): modules/ssh is absent, IgniteCluster.startNodes(...) and IgniteSshHelper remain in core, IgniteComponentType.SSH loads org.apache.ignite.internal.util.nodestart.IgniteSshHelperImpl by name, and the exception text comes from IgniteComponentType.componentException. No 8.9 deprecation notice (GG-50505 closed as Won't Do). -->

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

- *Maven coordinates.* `org.gridgain:ignite-aws` stops resolving, so a Maven or Gradle build fails. Use `org.apache.ignite:ignite-aws-ext` instead. The group ID is different, and the classes keep their `org.apache.ignite.*` packages, so imports do not change. You do not need an `<exclusion>`: the extension declares `org.apache.ignite:ignite-core` with `provided` scope, which is not transitive.
- *Region setter.* `AwsKmsEncryptionService` has only `setRegion(Region)` in the extension, and no `setRegion(String)`. A Spring XML file that passes a plain region string fails. Use a `RegionUtils.getRegion` factory bean instead.
- *Older dependencies.* The extension (1.0.0) pulls in older libraries at compile scope than `ignite-aws` does: AWS SDK 1.11.75, `jackson-databind` 2.12.4, `httpclient` 4.5.1, and `bcprov-ext-jdk15on` 1.69. Check them against your security requirements before you switch. This is not a security upgrade.
- *AWS Encryption SDK version.* The extension's KMS support works only with AWS Encryption SDK 1.x. It pins 1.3.2, which has no key commitment (CVE-2020-8897), and it fails with `NoSuchMethodError` on the 2.x SDK that `ignite-aws` ships. If your application uses the 2.x SDK, it cannot use the extension's KMS service.
- *S3 IP finder with `AwsKmsEncryptionService`.* The extension cannot decrypt the key-committed ciphertext that `ignite-aws` wrote with AWS Encryption SDK 2.4.0, and `ignite-aws` rejects the extension's ciphertext. Nodes on the two modules cannot read each other's entries, and the failure stops a node from joining. Switch every node, thick clients included, at once, and set a fresh `keyPrefix` on the IP finder. Entries that the old nodes left in the bucket are not cleaned up by the new ones. This cannot be done as a rolling upgrade. The symmetric and asymmetric key services do not use the SDK and are not affected.

<!-- CHECK: AWS text from GG-51561 and the merged PRs gridgain#4166 (removal, master) and #4187 (8.9 deprecation, with the README and javadoc notes). Verified in source: modules/aws is absent on origin/master e85742c4003 and present with @Deprecated on origin/8.9-master; the extension's AwsKmsEncryptionService has only setRegion(Region) and the extension pins aws-encryption-sdk-java 1.3.2 (apache/ignite-extensions modules/aws-ext); ignite-aws-ext 1.0.0 is on Maven Central; its pom declares ignite-core with provided scope. The dependency versions, the NoSuchMethodError on the 2.x SDK, CVE-2020-8897, and the two-way ciphertext incompatibility are from the @deprecated javadoc merged in #4187 (AwsKmsEncryptionService, TcpDiscoveryS3IpFinder); merged PRs are treated as the source of truth, and they are not run. Apache Ignite made the same move in 2.12.0. -->

### Machine Learning Module Removed

This section applies if you use `ignite-ml` or one of its model parsers.

The `ignite-ml` module is removed together with `ignite-ml-spark-model-parser`, `ignite-ml-xgboost-model-parser`, and `ignite-ml-mleap-model-parser`. The module was deprecated in 8.9.38: every public type in `org.apache.ignite.ml.**` carries `@Deprecated`.

Switch to the Apache Ignite `ignite-ml-ext` extension (version 1.0.0, tested against GridGain 8.9 and 8.10) or to the standalone GridGain ML download.

<!-- CHECK: the tested-against statement is from a GG-51303 comment of 2026-09-24 (ignite-ml-ext-1.0.0, the only release). The user-facing wording of "supported" must be confirmed with Product. -->

### Local Store Support Removed

This section applies if you use `@CacheLocalStore`, `CacheFileLocalStore`, or the `IGNITE_LOCAL_STORE_KEEPS_PRIMARY_ONLY` system property.

The local store is removed: `@CacheLocalStore`, `CacheFileLocalStore` (Enterprise), and the `IGNITE_LOCAL_STORE_KEEPS_PRIMARY_ONLY` system property no longer exist. Use native persistence or a regular `CacheStore`, and remove the system property from your start scripts.

## Dependency Upgrades

### Hibernate 7 Only

This section applies if you use the Hibernate second-level cache.

The Hibernate second-level cache module targets Hibernate 7.4 and is named `ignite-hibernate-7.4`. Applications on Hibernate 4.2, 5.1, or 5.3 must move to Hibernate 7.4 or stay on GridGain 8.9.x.

### Spring 7 Only

This section applies if your application embeds GridGain through Spring.

GridGain 8.10 builds against Spring Framework 7.0.9 and Spring Data 4.1.0. The `ignite-spring` and `ignite-spring-data` modules are compiled to Java 17 bytecode and target Spring 7. Spring 5 and Spring 6 are no longer supported, and `ignite-spring-6` is removed.

An application that embeds GridGain through Spring must be on Spring 7. Otherwise, stay on GridGain 8.9.x, which keeps the Spring 5 and Spring 6 modules.

The Control Center agent also runs on Spring 7 (7.0.9) and Tyrus 2. An agent embedded in an application on Spring 5 or Spring 6 does not start. Upgrade the host application or keep using the 8.9.x agent.

### Spring Data Module Renamed

This section applies if you use `ignite-spring-data_2.2`.

The `ignite-spring-data_2.2` module is renamed to `ignite-spring-data`, and its package changes from `org.apache.ignite.springdata22` to `org.apache.ignite.springdata`.

1. Change the artifact ID in your build files from `ignite-spring-data_2.2` to `ignite-spring-data`.
2. Update the imports of `IgniteRepository`, `@EnableIgniteRepositories`, `@RepositoryConfig`, `@Query`, and the other classes of the module.

### Lucene

This section applies if you run `ignite-lucene-8`, or if you want to use Lucene 10.

The `ignite-lucene-8` module is removed. If you still run it (the Java 8 workaround documented for GridGain 8.9.18 and later put it in `libs`), move to the Lucene 9 line before you upgrade. Do not copy `ignite-lucene-8` to the 8.10 distribution.

The 8.10 package ships two Lucene lines. The Lucene 9 line (Lucene 9.10.0) is active by default, and the Lucene 10 line (Lucene 10.4.0) is in `libs/optional`, where it stays inactive until you move it. There is no separate Lucene 10 download. If you upgrade without changing anything, the node behaves as it did on 8.9: `ignite-lucene-9` is in `libs` and serves full-text and vector search.

| Folder in `libs/optional` | Requires | Editions |
| --- | --- | --- |
| `ignite-lucene-10` | JDK 21 or later | Community, Enterprise, Ultimate |
| `ignite-lucene-10-java22` | JDK 22 or later. Adds an opt-in scorer that reads vectors from off-heap memory. See the `README.txt` in the folder for the JVM options. | Community, Enterprise, Ultimate |
| `gridgain-vector-query-lucene-10` | The Lucene 10 line. Pairs with it only. | Enterprise, Ultimate |

The z/OS package does not ship the Lucene 10 line.

The Lucene 10 line replaces `ignite-lucene-9`, it does not add to it. The two use the same class names, so a node must run exactly one line, and every node in a cluster must run the same line. Two lines on one classpath fail to link at the first index the node touches. A cluster that mixes them returns different vector search recall depending on which node serves the query, because Lucene 10.4 scores a small segment exhaustively where Lucene 9.10 walks a graph.

To switch a node to Lucene 10:

1. Stop the node.
2. Remove the `libs/ignite-lucene-9` folder.
3. Move one of `ignite-lucene-10` (JDK 21 or later) or `ignite-lucene-10-java22` (JDK 22 or later) from `libs/optional` into `libs`.
4. If you use vector search on Enterprise or Ultimate, replace `libs/gridgain-vector-query` with `libs/optional/gridgain-vector-query-lucene-10`.
5. Start the node.

Finish the upgrade to 8.10 on the Lucene 9 line first, and switch lines afterward on every node. Switching during the rolling upgrade would put two lines in one cluster.

To go back to Lucene 9, reverse the steps. The Lucene index is held in memory and rebuilt from the cache data, so switching lines does not migrate or invalidate anything on disk.

<!-- CHECK: the Lucene 10 layout and the switching steps follow the open PRs for GG-51314 (gridgain/gridgain#4229, ggprivate/ggprivate#2525, ggprivate-tc#210), which are not merged. Verified from the diffs: ignite-lucene-10 and ignite-lucene-10-java22 go to libs/optional in the CE descriptors, gridgain-vector-query-lucene-10 in the EE and ULT descriptors only, zOS unchanged, and the switching text is the new modules/lucene-10/README.txt. Not run, and the 8.10.0-master-20261019 build does not have these folders. Re-check the editions, the folder names, and the step that replaces libs/gridgain-vector-query against an unpacked package after the merge. -->
<!-- TODO RE: the README tells the user to "restore libs/ignite-lucene-9" to go back, but step 2 deletes it, and nothing says where to get it from. The rollback paragraph above assumes the folder was moved to libs/optional instead. Confirm, or change step 2 here. Also confirm whether libs/gridgain-vector-query is in libs or libs/optional by default in 8.10. -->

### Jetty 12 Is the Only REST Implementation

This section applies if you use a custom Jetty XML file with the REST connector.

The `ignite-rest-http` module now runs on Jetty 12 (12.0.40) and requires Java 17. The Jetty 9.4 module is removed, and so is the separate `ignite-rest-http-jetty-12` module that GridGain 8.9.x shipped as an option. The module keeps the `ignite-rest-http` artifact name, so dependency declarations do not change.

A configuration that does not set `ConnectorConfiguration.setJettyPath(...)` needs no changes. A custom Jetty XML file written for Jetty 9.4 does not load on Jetty 12, and the node fails to start with `Failed to start Jetty HTTP server` and `IllegalStateException: No matching constructor class org.eclipse.jetty.server.Server`. Migrate it as follows:

1. Rename the `threadpool` argument of the `Server` constructor to `threadPool`, or remove the name and pass the argument by position. A named argument that matches no constructor parameter makes the whole constructor unmatchable.
2. Remove the `<Set name="handler">` block that uses `HandlerCollection` or `HandlerList`. Both classes are removed in Jetty 12, and GridGain installs its own REST handler after your file is applied.

The `DOCTYPE` declaration needs no change.

For HTTPS and mutual TLS, use `org.eclipse.jetty.util.ssl.SslContextFactory$Server` with `SslConnectionFactory` and `HttpConnectionFactory`. `SecureRequestCustomizer` checks the SNI host name by default. Set `sniHostCheck` to `false` on it if the certificate name does not match the bind address. The client certificate chain is available to the REST handler through the SSL session data, not through the Jetty 9 `X509_ATTRIBUTE`.

<!-- CHECK: the HTTPS and mutual-TLS notes are condensed from modules/rest-http/MIGRATION.md (master) and were not run. Decide whether to include the full HTTPS XML example from MIGRATION.md or link to the REST API page. Each of the two Jetty XML edits alone was not tried; the failure and the fix were verified with both edits together. -->

### Cassandra Store Uses the DataStax Driver 4

This section applies if you use the Cassandra store.

The Cassandra store moves from DataStax Java driver 3.2 to 4.17 (`com.datastax.oss.driver.*`) and from `cassandra-all` 3.11 to 5.0.8. Cassandra 2.1 or later is required, and Cassandra 3 clusters must be upgraded 3 → 4 → 5.

The `DataSource` configuration API changed:

- `setLocalDataCenter()` is required when you specify explicit contact points and no custom load balancing policy.
- Policies are configured by class: `setLoadBalancingPolicyClass()`, `setReconnectionPolicyClass()`, `setRetryPolicyClass()`, `setAddressTranslatorClass()`, and `setSpeculativeExecutionPolicyClass()` replace the former instance-based setters.
- `setPoolingOptions()`, `setSocketOptions()`, and `setNettyOptions()` are removed. Use `setConfigFile()` and a driver configuration file.
- `setSslOptions()` is replaced by `setSslEngineFactory()`.
- `user` and `password` are mutually exclusive with `credentials`. Set one or the other.

Update the `DataSource` bean definitions in your Spring XML configuration. Previously serialized `DataSource` instances (those held by dynamically created caches) cannot be read by 8.10. Drop and recreate those caches. Large transactions may reach the Cassandra `batch_size_fail_threshold` setting.

<!-- CHECK: verified in source: driver 4.17.0, cassandra-all 5.0.8, setLoadBalancingPolicyClass / setConfigFile / setSslEngineFactory / setLocalDataCenter present; setPoolingOptions / setSocketOptions / setNettyOptions absent (present on 8.9). Not verified: error messages, setCollectMetrix / setJmxReporting removal, credentials exclusivity, the serialized-DataSource failure, and the batch-size threshold. The text follows the 8.10.0-b1 release notes and the GG-49566 release note summary. -->

## Distribution and Packaging Changes

This section applies to every upgrade, because you build the 8.10 `libs` folder from the new distribution.

- *Integrations move out of the server packages.* The Oracle GoldenGate integrations and the Kafka Connect connector no longer ship in the server package and are not in an `integration` folder. Get them from the integrations download, Maven, or Confluent Hub. `gridgain-kafka-connect` is shipped only as its own artifact.
- *Maven-only modules.* `ignite-hibernate-7.4` and `ignite-spring-data` are published to Maven only and are no longer in `libs/optional`. If you copy these jars into `libs`, take them from Maven.
- *OpenCensus.* `ignite-opencensus` moves from `libs` to `libs/optional`. To keep OpenCensus tracing, move the `ignite-opencensus` folder back into `libs`.
- *Control Center agent.* `control-center-agent` moves from `libs` to `libs/optional`. A node started from the 8.10 distribution does not load the agent, and does not connect to Control Center, until you move the `control-center-agent` folder into `libs`.
- *Spring Data commons.* `ignite-spring-data-commons` is no longer in `libs/optional`. Like `ignite-spring-data` in the previous bullet, it is published to Maven only. Take the commons dependency from Maven if you copied it.
- *Bulk load.* `gridgain-bulkload` stays in `libs/optional` of the server packages. It is not moved to the integrations download. Its dependency set is smaller (about 93 MB instead of about 857 MB): the single AWS SDK bundle jar is replaced by the individual AWS clients that bulk load uses, so reading from S3 still works, and the Hadoop, Snowflake, and Iceberg dependency closures are reduced. The Snowflake JDBC driver (`snowflake-jdbc`) is no longer in `libs/optional/gridgain-bulkload`. Snowflake was never a supported source, and both paths to it are closed by default: `jdbc:snowflake:` is not in the schemes that `COPY ... FORMAT JDBC` accepts (see [Server-Side SQL COPY](security-and-licensing.md#server-side-sql-copy)), and `SnowflakeCatalog` is not in `importExport.allowedIcebergClasses`, which is empty by default. The change affects you only if you added `jdbc:snowflake:` to `GRIDGAIN_BULKLOAD_JDBC_ALLOWED_URL_SCHEMES` or `SnowflakeCatalog` to `importExport.allowedIcebergClasses`. In that case, put a Snowflake JDBC driver next to the module yourself.
- *No evaluation license archives.* The Enterprise, Ultimate, and z/OS evaluation-license archives are no longer built.
- *Examples.* Examples are no longer part of the source repository. They are published in the public `gg8-examples` repository and are still bundled into the packages.
- *C++ client.* The C++ client requires C++14, and the autotools build is removed. Build the C++ client with CMake.

<!-- CHECK: the Snowflake text is from GG-51118 and GG-51108 (the default scheme list is JdbcProperties.DFLT_ALLOWED_SCHEMES = mariadb, mysql, postgresql, with a pinning test JdbcPropertiesTest.rejectsSnowflakeSchemeByDefault). Not run. Check that allowedIcebergClasses is the right name next to allowedCatalogUris in the COPY section, which does not list it. -->
<!-- CHECK: compared the 8.9.38 and 8.10.0-master-20261019 distributions: control-center-agent moved from libs to libs/optional (the agent log line was seen on 8.9 only; that the 8.10 node does not connect without it is from the folder layout, not run). -->
<!-- CHECK: ignite-spring-data-commons is in 8.9.38 libs/optional and absent from the 8.10 master build. The module still exists on master (modules/spring-data-commons), and assembly/dependencies-apache-ignite.xml excludes both org.gridgain:ignite-spring-data and org.gridgain:ignite-spring-data-commons from the distribution, so it is Maven-only. -->
<!-- CHECK: in the 8.10 master build, libs/optional has no ignite-aws, ignite-hibernate-7.4, or ignite-spring-data, has ignite-opencensus, and has no integration/ folder. GG-51112 (gridgain-bulkload to the integrations download) was closed on 2026-10-17 by Dmitry Baranov as "decided not to do this": bulkload stays in libs/optional, and the size was solved by GG-51107 (the awssdk bundle fat jar is dropped, the granular s3, sts, and glue clients stay) and GG-51108 (857 MB to about 93 MB). Narrowing the dependency set further is GG-52384. The integrations download itself was not part of the verified build. -->
<!-- TODO Unison/RE: link to the integrations download (GG-51118 is the Docs ticket for this upgrade guide section, owner Dmitry Baranov). The list of what leaves libs/optional and integration/ is settled: GG-51115 and GG-51116 (ignite-hibernate-7.4 and ignite-spring-data, Maven only) are Resolved, GG-51112 (bulkload) is not done, and the GoldenGate and Kafka Connect integrations are out of the server packages. -->
