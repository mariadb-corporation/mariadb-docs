---
description: >-
  GridGain 9.1.8 is a public release featuring AWS KMS encryption and improved continuous queries, along with cumulative improvements since 9.1.0.
---

# GridGain 9.1.8 Release Notes

## Overview

GridGain 9.1.8 is a public release that features AWS KMS encryption, improved continuous query management and logging.

As a public release, it also includes cumulative improvements since 9.1.0, now available to users of community edition.

## Known Issues

### Array Node Configuration Update at Runtime

In this release, you cannot add new values to configurations defined as arrays via CLI or REST API at runtime. This affects the following properties:

- `ignite.clientConnector.listenAddresses`
- `ignite.failureHandler.handler.ignoredFailureTypes`
- `ignite.network.listenAddresses`
- `ignite.network.nodeFinder.netClusterNodes`
- `ignite.nodeAttributes.nodeAttributes`
- `ignite.storage.profiles`
- `ignite.system.properties`

To add new values to these properties, define them in the initial node configuration and restart the node. By default, the node loads the configuration from the `{GRIDGAIN_HOME}/etc/gridgain-config.conf` file.

This issue will be fixed in an upcoming release.

## Major Changes

This release has the following major changes:

### Closeable Table Views

Starting with this release, all table views are `AutoCloseable` and can be wrapped in a `try-with-resources` statement.

Only views for [near caches](../../developers-guide/near-cache.md#configuring-near-cache) require closing to ensure correct resource cleanup and must be wrapped in a `try-with-resources` statement.

```java
// Using try-with-resources statement to safely handle a near cache.
public static void demonstrateNearCacheClient() throws Exception {
    try (IgniteClient client = IgniteClient.builder()
            .addresses("127.0.0.1:10800")
            .build()) {

        // Configure near cache options.
        NearCacheOptions nearCacheOptions = NearCacheOptions
                .builder()
                .expireAfterAccess(5000)
                .expireAfterUpdate(100000)
                .maxEntries(100)
                .build();

        // Create table view configuration.
        TableViewOptions tableViewOptions = TableViewOptions
                .builder()
                .nearCacheOptions(nearCacheOptions)
                .build();

        try (RecordView<Tuple> accounts = client.tables().table("accounts").recordView(tableViewOptions)) {
            // Work with the near cache.
        }
    }
}
```

## New Features and Changes

These features were added in this release:

### AWS KMS Encryption

When using [encryption](../../administrators-guide/security/tde.md) on the cluster, you can now set up [AWS KMS](https://docs.aws.amazon.com/kms/) provider. When used, AWS will manage your keys and provide them as required.

The example below shows how to create a provider and use it on the cluster:

```json
{
    "ignite" : {
        "encryption" : {
            "enabled" : true,
            "activeProvider" : "aws",
            "providers" : [{
                "name" : "aws",
                "type" : "aws_kms",
                "keyId" : "my_key"
            }]
        }
    }
}
```

### Skipping Old Entries in Continuous Queries

A new `skipOldEntries` option was added to [continuous queries](../../developers-guide/continuous-queries.md). When set to `true`, `TableRowEvent#oldEntry()` will return `null` for `TableRowEventType#UPDATED` events. This option can be used to reduce the network load and avoid resending old entries.

```java
var options = ContinuousQueryOptions.builder()
        .pollIntervalMs(10)
        .pageSize(pageSize)
        .skipOldEntries(true)
        .build();

view.queryContinuously(subscriber, options);
```

## Improvements and Fixed Issues in This Release

This release features the following improvements:

| Issue ID | Category | Description |
|---|---|---|
| IGN-28660 | CLI Tool | When invoking the same command in REPL mode with a node name or URL option, and then without the option, the command no longer remembers the option value from the first invocation. |
| IGN-28600 | General | Logs for node failures now include context identifier. |
| IGN-28578 | General | Improved error messages for failures during cluster initialization. |
| IGN-28511 | Distributed Computing | Fixed default Java based marshaling to byte arrays in compute jobs. |
| IGN-28502 | Distributed Computing | Job failed event is now logged when compute job fails due to the absence of available worker nodes. |
| IGN-28449 | Distributed Computing | Added events for MapReduce tasks. |
| IGN-28319 | Disaster Recovery | You can now restart partitions via REST API. |
| IGN-28318 | Disaster Recovery | Added a CLI option to restart partitions with cleanup. |
| IGN-28203 | SQL | Added support for GROUPING aggregate function. |
| IGN-27967 | Distributed Computing | Canceled compute jobs now correctly have the CANCELED status. |
| GG-44710 | General | Improved invalid license error message. |
| GG-44693 | Platforms and Clients | Python Client now supports Python 3.9. |
| GG-44528 | General | DDL command execution is now forbidden during rolling upgrade. |
| GG-44345 | General | Added ContinuousQueryOptions.skipOldEntries option to reduce the amount of transferred data when old values are not needed. |
| GG-43621 | Cluster Storage Engine | Implemented closable API for table views. |
| GG-38740 | Cluster Storage Engine | Added support for AWS KMS. |

## Cumulative Major Changes

The following major changes were implemented in one of the releases between 9.1.0 and 9.1.8. If you are already using one of those releases, see the release notes for individual releases for the list of changes.

### Partition Colocation

This release features a major rework of how partitions are distributed to the nodes and organized.

With partition colocation enabled by default for new clusters, partitions with the same index for all tables in the same distribution zone will now be stored on the same node and use the same RAFT group. This change results in improved performance, as the cluster requires fewer resources to manage distribution zones.

For nodes started with persistent storage from previous versions, partition colocation will be disabled by default. Due to major changes in partitions management, persistent storage from previous versions is not compatible with colocation. We recommend recreating persistent storage on a new 9.1.4 or later cluster and manually migrating data to it.

If you receive the incompatible colocation mode error when the node attempts to join the cluster, clear the persistent data on the node and explicitly set the replication mode by setting the `IGNITE_ZONE_BASED_REPLICATION` system property to true (to enable colocation mode) or false (to disable colocation mode).

### Configuration Changes

This release features a major rework of node and cluster configuration, making configuration names more consistent and reorganizing some parameters.

Below is the summary of the changes:

- All configuration property names now include the units used.
- A number of default values were changed to better work in real environments

Previously used configuration is temporarily supported for backwards compatibility and should be replaced by new configuration options.

### CREATE ZONE Syntax Changes

The  [CREATE ZONE](../../sql-reference/distribution-zones.md) and [ALTER ZONE](../../sql-reference/distribution-zones.md#alter-zone) command syntax was significantly reworked. All additional parameters (specified in the `WITH` parameter) are now part of common syntax.

Below is the example of creating a distribution zone:

```sql
-- Previously used syntax.
CREATE ZONE IF NOT EXISTS "myExampleZone" WITH STORAGE_PROFILES='default', REPLICAS=3, PARTITIONS=2;

-- Current syntax.
CREATE ZONE IF NOT EXISTS "myExampleZone" (REPLICAS 3, PARTITIONS 2) STORAGE PROFILES['default'];
```

Previously used syntax is temporarily supported for backwards compatibility and should be replaced by new syntax.

### Changed Syntax for Getting Nodes in Java

The `ignite.clusterNodes()` method was deprecated in this release and is replaced by `ignite.cluster().nodes()` method. This method now returns nodes in the logical topology.

The `clusterNodes()` will temporarily continue to work for backwards compatibility, however we recommend changing your code to use the new method.

```java
Ignite ignite = node.api();

// Deprecated method for getting cluster nodes
var oldClusterNodes = ignite.clusterNodes();

// New method for getting cluster nodes
var newClusterNodes = ignite.cluster().nodes();
```

### Extended Critical Worker Timeouts

This release increases default timeout values for critical workers. The following values are changed:

- `ignite.system.criticalWorkers.livenessCheckIntervalMillis` changed from 200 to 2000 milliseconds,
- `ignite.system.criticalWorkers.maxAllowedLagMillis` changed from 500 to 5000 milliseconds,
- `ignite.system.criticalWorkers.nettyThreadsHeartbeatIntervalMillis` changed from 100 to 1000 milliseconds.

## Cumulative Features Since 9.1.0

These features were added in one of the releases between 9.1.0 and 9.1.8. If you are already using one of those releases, see the release notes for individual releases for the list of features added in them.

### Near Caches

This release reintroduces support for near caches in GridGain 9. Near caches provide a way to store data locally on your clients and avoid lengthy network queries for latest data from the cluster.

You can configure near cache for any [table view](../../developers-guide/table-api.md#basic-table-operations). Data will be queried from the cluster when it is read, and stored locally for the configured duration for repeated access.

Just like with table views, it is recommended to use `try-with-resources` statement to avoid any possible memory leaks.

Below is a simple example of configuring near cache for a table:

```java
NearCacheOptions nearCacheOptions = NearCacheOptions
  .builder()
  .expireAfterAccess(5000)
  .expireAfterUpdate(100000)
  .maxEntries(100)
  .build();
TableViewOptions tableViewOptions = TableViewOptions
  .builder()
  .nearCacheOptions(nearCacheOptions)
  .build();
QualifiedName myTable = QualifiedName.parse("PUBLIC.accounts");
try (KeyValueView<Tuple, Tuple> kvView = client.tables().table(myTable).keyValueView(tableViewOptions)) {
    ...
}
```

For more information on near caches, as well as limitations, see [Near Cache](../../developers-guide/near-cache.md) documentation.

### Python Client

This release brings the first version of the Python client. The client API is experimental and may change in subsequent releases. Currently, the Python client is exclusively dedicated to working with distributed maps.

You can install the python client from pip by installing `pygridgain` of version 9 or later:

```bash
pip install pygridgain>=9
```

The following example demonstrates how you can use the client to create a map, add a value to it, and get it back:

```python
async with AsyncClient(address) as client:
    await client.connect()
    print("client connected")
    binary_map = await client.structures().get_or_create_binary_map('myMap')
    await binary_map.put(b'1', b'Hello World')
    value_exists = await binary_map.contains(b'1')
    print(f"Does 1 exist on the cluster: {value_exists}")
    print(await binary_map.get(b'1'))
```

For more information about Python client, see [client documentation](../../developers-guide/clients/python-client.md).

### Change Data Capture

This release features the first implementation of change data capture. You can now use it to configure replication of data to Iceberg. Once configured all updates to GridGain tables will be automatically propagated to Iceberg.

To start CDC replication:

- Configure data source:
  ```bash
  cdc source create --name gridgain_source --type gridgain --tables PUBLIC.MY_TABLE1
  ```

- Configure data sink:
  ```bash
  cdc sink create --name iceberg_sink --type Iceberg
  ```

- Create a replication that uses previously configured sink and source:
  ```bash
  cdc replication create --name my_replication --source gridgain_source --sink iceberg_sink
  ```

- Start the replication:
  ```bash
  cdc replication start --name my_replication
  ```

### Snapshot Encryption

Starting with this release, if [data encryption](../../administrators-guide/security/tde.md) is enabled on the cluster, your snapshots will also be encrypted.

You can also manually set snapshot encryption when creating them by using the `encryption-provider` parameter.

```bash
cluster snapshot create --type=full --tables=PERSON --destination=relative-path-example --encryption-provider=keystore
```

### .NET Distributed Computing

This release adds support for .NET compute jobs and stream receivers. You can now implement your jobs and receivers in .NET (C#, F#, and others), deploy them to the cluster, and run them from any supported client or language.

Here is an example of a simple compute job:

```csharp
JobDescriptor<string, string> jobDesc = JobDescriptor.Of(new HelloJob()) with { DeploymentUnits = [...] };
var jobTarget = JobTarget.AnyNode(await client.GetClusterNodesAsync());
var jobExec = await client.Compute.SubmitAsync(jobTarget, jobDesc, arg: "world");

public class HelloJob : IComputeJob<string, string>
{
    public ValueTask<string> ExecuteAsync(IJobExecutionContext context, string arg, CancellationToken cancellationToken) =>
        ValueTask.FromResult("Hello " + arg);
}
```

### Archiving Data in Secondary Storage

When using secondary storage, you can configure your tables to delete data from primary storage when it is no longer in active use. To do this, you specify the `ARCHIVE AT` condition with a ttl of when the data should be removed from primary storage, for example:

```sql
CREATE TABLE IF NOT EXISTS Person (
  id int primary key,
  name varchar,
  ttl TIMESTAMP WITH LOCAL TIME ZONE)
  ZONE zone1 SECONDARY ZONE secondary_zone SECONDARY STORAGE PROFILE 'columnar_storage' ARCHIVE AT ttl;
```

Once data is archived, it will no longer be available in primary storage, but can still be accessed from secondary storage. To make sure data is read from secondary storage, you can use the `/*+ use_secondary_storage */` sql hint.

```sql
SELECT * FROM Person /*+ use_secondary_storage */
```

### Partition Awareness for Client SQL

With this release, clients will benefit from [partition awareness](../../developers-guide/clients/overview.md#partition-awareness) for SQL queries, significantly improving their performance.

### New Distribution Zone QUORUM_SIZE Parameter

You can now manually set the required number of available replicas in the distribution zone by setting the `QUORUM_SIZE` parameter. If at any point there are fewer replicas available than set in the `QUORUM_SIZE`, the consensus is lost and updating the table will be impossible until the required number is once again available. Previously written data will still be available.

You can set the quorum size to a specific number.

Below is the example of setting quorum size:

```sql
CREATE ZONE IF NOT EXISTS exampleZone (REPLICAS 3, QUORUM SIZE 3) STORAGE PROFILES['default'];
```

### Improved Migration Tools

This release features major changes in migration tools:

- A new way of configuring mapping between caches and tables during [DCR from GridGain 8](../../migration-from-gg-8/dcr-from-gg8.md) was added. By using it, you can map key and value cache fields separately, as well as ignore the fields that are not required. The example below shows how you can configure mapping:
  ```
  dr-service-config = {
    cacheMapping = [
      {
        cache = "cacheName"
        table = "schemaName.tableName"
        keyFields = [
          { field = "K1", column = "COL_1" }
          { field = "K2", column = "COL_2" }
          { field = "K3", column = "COL_3" }
        ]
        valueFields = [
          { field = "V1", column = "COL_4" }
          { field = "V2", column = "COL_5" }
          { field = "V3", column = "COL_6" }
          { field = "V4", ignore = true }
        ]
      }
    ]
  }
  ```

- [Code adapter](../../migration-from-gg-8/codebase-migration.md) now supports migration of GridGain 8 ScanQueries.

### Creating Caches From Java

With this release, you can use the `@Cache` annotation in Java to create caches from Java classes. You can create caches from Key-Value POJOs. Once a cache is created, you can work with it as described in [cache](../../developers-guide/cache.md) documentation.

```java
class PojoKey {
    @Id
    Integer id;

    @Id(SortOrder.DESC)
    @Column(value = "id_str", length = 20)
    String idStr;
}

@Cache(
    value = "kv_pojo",
    zone = @Zone(
		value = "zone_test",
		replicas = 2,
		storageProfiles = "default"
   ),
    colocateBy = { @ColumnRef("id"), @ColumnRef("id_str") },
    indexes = { @Index(value = "ix", columns = {
                    @ColumnRef(value = "f_name"),
                    @ColumnRef(value = "l_name") })
    }
)
class PojoValue {
    @Column("f_name")
    String firstName;

    @Column("l_name")
    String lastName;

    String str;
}

Table myTable = ignite.catalog().createCache(PojoKey.class, PojoValue.class);

KeyValueView<PojoKey, PojoValue> view =  myTable.keyValueView(PojoKey.class, PojoValue.class);
```

### Removing All Data From Tables

New `removeAll()` and `deleteAll()` methods can be used to remove all data from key-value and record views respectively.

For example:

```java
KeyValueView<AccountKey, Account> kvView = client.tables()
        .table("accounts")
        .keyValueView(AccountKey.class, Account.class);

AccountKey key = new AccountKey(123456);

Account value = new Account(
        "John",
        "Smith",
        100.00d
);

kvView.put(null, key, value);

kvView.removeAll(null)
```

### Batched Execution Cancellation

The `executeBatch()` and `executeBatchAsync()` methods now return cancellation token that can be used to cancel these operations.

### New Method to Get Local Node

With this release, you can use the new `ignite.cluster().localNode()` method to quickly get the local [embedded node](../../quick-start/embedded-mode.md).

### Logging Improvement

This release features major effort in improving logging in GridGain 9. A large number of errors that previously caused unexpected exceptions are now correctly caught, categorized and reported with a [correct code](../../administrators-guide/handling-exceptions.md).

### COPY INTO batchSize Parameter

With this release, you can choose how many entries are processed at a time when executing the `COPY INTO` operation. By default, 1024 entries are batched. If you want to change the value, use the `batchSize` parameter:

```sql
/* Import data from CSV with custom quotation character */
COPY FROM '/path/to/dir/data.csv'
INTO Table1 (name, age)
FORMAT CSV
WITH 'batchSize'='2048';
```

### Mapping Empty Values in COPY INTO Command

With this release, you can configure how empty values are mapped on import, and `null` values are mapped to on export. You do this by adding the `null` parameter and assigning a new value.

```sql
/* Import data from CSV with custom quotation character */
COPY FROM '/path/to/dir/data.csv'
INTO Table1 (name, age, empty)
FORMAT CSV
WITH 'null'='no data'
```

### Cluster Topology Metrics

This release includes new cluster topology metrics, that provide information about node name, id and version, as well as cluster name, id, and number of nodes in the cluster. For more information about these sources, see [Available Metrics](../../administrators-guide/metrics/metrics-list.md).

### Improved SSL Support

This release introduces support for SSL in [Python DB API](../../developers-guide/clients/python.md) and [ODBC Driver](../../developers-guide/sql/odbc/odbc-driver.md). You can now securely connect to your cluster from both.

To securely connect from python DB API, specify the ssl key file and certificate in the connection configuration:

```python
pyignite_dbapi.connect(
	address='127.0.0.1',
	use_ssl=True,
	ssl_keyfile='<path_to_ssl_keyfile.pem>',
	ssl_certfile='<path_to_ssl_certfile.pem>'
)
```

For ODBC driver, specify it in the connection string:

```
DRIVER={Apache Ignite 3};ADDRESS=localhost:10800;SCHEMA=yourSchemaName;SSL_MODE=require;SSL_KEY_FILE=<path_to_ssl_keyfile.pem>;SSL_CERT_FILE=<path_to_ssl_certfile.pem>
```

### Extended Metrics

This release includes multiple new metrics that can enhance monitoring your clusters:

- New SQL thread pool metrics
- New sql query execution metrics.
- Extended data region metrics.
- A new data center replication lag metric.

For a full list of metrics, see the [Available Metrics](../../administrators-guide/metrics/metrics-list.md).

### Improved Monitoring

This release features multiple improvements to cluster monitoring:

- New `ClockSkewExceedingMaxClockSkew` metric can be used to monitor clock drift.
- A set of new compute events allows for easier monitoring of your distributed computing jobs.

## Cumulative Improvements and Fixed Issues

The following improvements have been implemented in one of the releases between 9.1.0 and 9.1.8. If you are already using one of those releases, see the release notes for individual releases for the list of improvements.

| Issue ID | Category | Description |
|---|---|---|
| IGN-24188 | General | OS information is now logged on node start. |
| IGN-25361 | Distributed Computing | .NET: Added support for IIgniteTuple as Compute and Data Streamer Receiver inputs and outputs. |
| IGN-25513 | SQL | Fixed an error that caused the query to fail if SET clause of the UPDATE statement included sub-queries. |
| IGN-25829 | Platforms and Clients | .NET: Added overloads with `CancellationToken` to SQL and Compute APIs. |
| IGN-25928 | General | Fixed a rare data corruption during concurrent remove operations, when multiple clients try to remove data from the same index tree in multiple threads. |
| IGN-26396 | General | Fixed potential rebalancing failure caused by catalog compaction. |
| IGN-26455 | Distributed Computing | Added new compute task events. |
| IGN-26565 | SQL | Improved type checking in LIMIT and OFFSET clauses. |
| IGN-26731 | General | Added QUORUM_SIZE parameter for distribution zones. |
| IGN-26772 | General | Added a new ignite.raft.disruptors.queueSize node configuration property. |
| IGN-26924 | SQL | You can now cancel batched queries. |
| IGN-27005 | Distributed Computing | Clients: fixed causality guarantees for compute jobs and streamer receiver. When a client runs a job or receiver which updates table data, the changes can now be observed from that client immediately. |
| IGN-27053 | SQL | Calcite version updated from 1.38.0 to 1.39.0. |
| IGN-27055 | SQL | Reworked CREATE ZONE command syntax. |
| IGN-27139 | SQL | When using the FORCE_INDEX hint, you will now receive an error if index name is incorrect. |
| IGN-27170 | SQL | You can now only specify year up to year 9999 in temporal data types. |
| IGN-27274 | SQL | Time values are now truncated consistently. |
| IGN-27276 | SQL | The __part system column is now case-insensitive. |
| IGN-27320 | SQL | Improved validation of timestamp literals in SQL queries. |
| IGN-27336 | General | Fixed an issue that could cause partitions recovery to time out. |
| IGN-27365 | General | Metastorage compaction no longer prevents other operations from reading data. |
| IGN-27371 | CLI Tool | Fixed an issue that caused SQL queries to return table column names instead of aliases in CLI tools. |
| IGN-27418 | Distributed Computing | Added a dedicated error IGN-COMPUTE-14 code for cancelling compute jobs. |
| IGN-27422 | SQL | Added support for UUID literal. |
| IGN-27427 | SQL | SQL_QUERIES system view now returns the same query as was submitted. |
| IGN-27447 | Platforms and Clients | Updated Netty from version 4.1.119.Final to version 4.2.4.Final. |
| IGN-27448 | Platforms and Clients | Added support for distributed computing in .NET client. |
| IGN-27449 | Platforms and Clients | Added .NET compute jobs support: implemented jobs in .NET (C#), deployment of dlls in deployment units, calls from any language or client. |
| IGN-27456 | General | You can now pass numerals in configuration without quoting them. |
| IGN-27457 | CLI Tool | Improved error message that is thrown when a node fails to initialize. |
| IGN-27480 | General | Page throttling limits are now configurable. |
| IGN-27482 | General | Fixed a rare case that could lead to data loss during partition rebalancing. |
| IGN-27483 | General | Lower throttling limit increased to 50%, and upper throttling limit reduced to 75%. |
| IGN-27514 | Platforms and Clients | .NET: Added synchronous Dispose method to ITransaction. |
| IGN-27589 | SQL | Updated Calcite from version 1.39 to version 1.40. |
| IGN-27591 | Distributed Computing | .NET: Improved platform job execution performance by caching assembly load contexts and job type information. |
| IGN-27609 | SQL | Fixed an issue that caused inconsistent behavior of the JOIN command that has sub-queries in the ON clause referencing the right table of the JOIN. |
| IGN-27631 | SQL | You now need to commit the explicit transaction in the script for it to be executed. |
| IGN-27632 | Platforms and Clients | Added support for .NET data streamer receiver implementations. |
| IGN-27650 | SQL | Fixed incorrect parsing of DATE, TIME, TIMESTAMP, and TIMESTAMP WITH LOCAL TIME ZONE in the CAST(string AS <datetime type> FORMAT 'format-string') operation. |
| IGN-27676 | Data Streamer | Data Streamer: fixed the receiver API. Added `payloadMarshaller`, `argumentMarshaller`, `resultMarshaller`. Added `DataStreamerReceiverDescriptor<T, A, R>`. Deprecated `ReceiverDescriptor<A>`. Added new `DataStreamerTarget#streamData` overload with `DataStreamerReceiverDescriptor` and deprecated the old one. |
| IGN-27677 | Distributed Data Streamer | .NET: Added payload, argument and result marshallers to data streamer APIs. |
| IGN-27702 | SQL | Added support for EXPLAIN MAPPING FOR command. |
| IGN-27724 | Platforms and Clients | C++ client now supports heartbeats. |
| IGN-27725 | General | Added removeAll() and deleteAll() methods to key-value and record view APIs. |
| IGN-27727 | General | Improved log messages when a node in the cluster stops. |
| IGN-27742 | SQL | Fixed an issue that caused the createTableAsync method to not fetch the table when using non-default schema. |
| IGN-27787 | SQL | Improved EXPLAIN command output. |
| IGN-27820 | SQL | JDBC driver now provides correct metadata for all available schemas. |
| IGN-27821 | Platforms and Clients | C++ client: Added support for configuring transaction timeouts. |
| IGN-27835 | SQL | Changed the column name resolution algorithm for columns with the same name during JOIN operation. An index with a $ separator is now added to the column to avoid collision. |
| IGN-27840 | Distributed Data Streamer | Fixed data streamer to respect backpressure in auto-flush timer. |
| IGN-27856 | Cluster Metrics & Monitoring | Names of JMX beans showing metrics now include the name of Ignite node. |
| IGN-27860 | Cluster SQL Engine | The Limit node on top of Sort node is now merged into Sort node. |
| IGN-27861 | SQL | In the EXPLAIN command output, offset and fetch attributes now have consistent meaning in Sort and Limit sections. |
| IGN-27911 | SQL | SQL queries from clients now benefit from partition awareness. |
| IGN-27917 | SQL | Added CURRENT_USER SQL function. |
| IGN-27922 | General | Added `IgniteCluster` interface with `nodes()` and `localNode()` methods. Deprecated `Ignite#clusterNodes`. Fixed `nodes()` to return only members of logical topology. |
| IGN-27950 | General | Nodes now reliably destroy dropped tables after restart. |
| IGN-27957 | General | Added data region metrics for aipersist storage engine. |
| IGN-27959 | Configuration | You can now use old configuration from before 9.1.0 release after update. |
| IGN-27964 | General | Added sql thread pool metrics. |
| IGN-27966 | Metrics and Monitoring | Added CpuLoad metric to os metric source and UpTime metric to jvm metric source. |
| IGN-27984 | Cluster SQL Engine | Fixed partition pruning for tables that have keys of the TIMESTAMP WITH LOCAL TIME ZONE data type. |
| IGN-28014 | General | Colocation is now enabled for new clusters. |
| IGN-28044 | SQL | TIME and TIMESTAMP data types conversion now correctly accounts for required precision. |
| IGN-28074 | Platforms & Clients | Added SSL support for ODBC driver. |
| IGN-28077 | Platforms & Clients | Added SSL support to Python DB API Driver. |
| IGN-28098 | SQL | Fixed an issue that caused an exception to be thrown while comparing different numerics during index scan. |
| IGN-28113 | Cluster SQL Engine | Fixed an issue that caused time values to be incorrectly trimmed when converted to string via getString method of JDBC ResultSet. |
| IGN-28137 | General | You can now disable distribution zone scaling. |
| IGN-28154 | General | CREATE ZONE command now checks if the relevant storage profile exists. |
| IGN-28175 | Cluster Storage Engine | Added extended transaction metrics. |
| IGN-28201 | General | Fixed incorrect estimation of partition sizes for zone-based partitions. |
| IGN-28221 | Platforms & Clients | .NET: Added ISql.ExecuteBatchAsync for batch DML (INSERT/UPDATE/DELETE) execution. |
| IGN-28269 | General | Log metric exporter configuration is extended with new parameters that can be used to change the format of output and the list of logged metrics. |
| IGN-28270 | General | Nodes now export some metrics to the log by default. |
| IGN-28273 | Platforms & Clients | .NET: Fixed serialization-related issues in UpsertAll and data streamer in certain scenarios. |
| IGN-28284 | Cluster SQL Engine | Fixed output formatting for CAST AS VARCHAR FORMAT queries. |
| IGN-28309 | Cluster SQL Engine | Fixed an issue that caused sql queries to hang when a UNION operator was used for a large number of tables. |
| IGN-28346 | Cluster SQL Engine | Fixed an ArrayIndexOutOfBounds exception that happened when merge operation included JOINs. |
| IGN-28366 | General | Fixed a possible deadlock during data rebalancing when a node leaves under heavy load and returns to the cluster after a long time. |
| IGN-28368 | General | CLI tool now displays metric source names in alphabetic order. |
| IGN-28375 | General | The changes in ignite.gc.lowWatermark.updateIntervalMillis configuration are now applied immediately. |
| IGN-28447 | Distributed Computing | Added compute job events. |
| IGN-28451 | General | Warning is now printed to log when MAX_CLOCK_SKEW value is exceeded. |
| IGN-28452 | Cluster Storage Engine | Added a new metric for clock drift. |
| IGN-28521 | Cluster Storage Engine | Node configuration file is no longer updated on node start. |
| IGN-28527 | Cluster Storage Engine | Improved log information about possible thread blocking. |
| IGN-28529 | Cluster SQL Engine | Improved the performance of SQL LEFT JOIN queries with non-equal predicates. |
| IGN-28535 | General | Increased default timeouts for critical workers. |
| IGN-28576 | General | Fixed a possible memory leak in event sink. |
| GG-39340 | Cluster Storage Engine | You can now configure encryption parameters for DEKs (Data Encryption Key). |
| GG-39659 | Migration Tools | Added support for ScanQueries in GridGain 8 code adapter. |
| GG-41861 | Cluster Architecture | You can now create caches by using Catalog API. |
| GG-42333 | Builds and Deliveries | Added Linux ARM64 support for Columnar store. |
| GG-42486 | Cluster Storage Engine | Updated RocksDB from 8.11.3.2 to 9.10.0.1. |
| GG-42537 | Cluster SQL Engine | Improved error message that is returned when trying to set unsupported expression as DEFAULT. |
| GG-42671 | Cluster SQL Engine | Data expiry is now checked every 30 seconds. |
| GG-42727 | Cluster Data Replication | Added a metric that can be used to track lag between source and target of data center replication. |
| GG-42841 | Cluster Storage Engine | Fixed a rare race when GridGain is restarted with columnar storage enabled. |
| GG-42853 | Cluster Data Snapshots and Recovery | Added configurable direct memory limits for snapshot restoration process. |
| GG-42945 | Cluster SQL Engine | Fixed an issue causing a query to fail when ON clause of join contains scalar sub-query referencing left side of a join. |
| GG-43002 | GridGain Integrations | Kafka source: Fixed potential endless polling loop. |
| GG-43037 | Cluster Storage Engine | You can now use the ARCHIVE_AT condition to only remove data from primary storage. |
| GG-43078 | Cluster Storage Engine | Fixed an issue with columnar storage on Mac systems with ARM architecture. |
| GG-43097 | Cluster Data Snapshots and Recovery | Point-in-time recovery now operates on a per-table basis. |
| GG-43099 | Cluster Data Snapshots and Recovery | Point-in-time recovery commands now use --id parameter. |
| GG-43116 | Cluster Storage Engine | Fixed an issue that caused an exception when invalid encryption configuration is provided on node startup. |
| GG-43136 | Cluster SQL Engine | Fixed an issue with creating sequences in SQL scripts |
| GG-43141 | General | Fixed an issue that caused data center replication to fail when using JDK 17. |
| GG-43142 | Cluster Data Replication | Data center replication now considers table schemas. |
| GG-43143 | Cluster Data Replication | Fixed an issue that could lead to OOM error during data center replication. |
| GG-43153 | Cluster SQL Engine | Improved error message when COPY command does not find a table or column. |
| GG-43163 | GridGain Integrations | Kafka sink: Fixed LocalDate conversion with Avro converter. |
| GG-43177 | Cluster SQL Engine | Improved performance of COPY FROM command when exporting data into parquet format. |
| GG-43195 | General | Updated json-smart from version 2.4.7 to version 2.5.2. |
| GG-43244 | Cluster Data Snapshots and Recovery | Fixed a false-positive error that happened when clearing snapshot tombstones. |
| GG-43256 | Cluster Continuous Queries | C++: Added watermark API to the CQ event batches. Added options to process empty batches. |
| GG-43282 | Cluster SQL Engine | Added support for batchSize parameter to COPY FROM command. |
| GG-43342 | Cluster Metrics & Monitoring | Added sql query execution metrics. |
| GG-43392 | Builds and Deliveries | RPM packages are now correctly signed. |
| GG-43402 | Cluster Storage Engine | Added requirements for distribution zone used for secondary storage. |
| GG-43419 | Cluster Storage Engine | Cluster nodes will no longer start if there are storage profiles with storage engines that are forbidden by the provided license in the node configuration. |
| GG-43534 | Cluster Continuous Queries | Fixed continuous query returning incorrect results on primary replica miss. |
| GG-43561 | Cluster Metrics & Monitoring | Added data region metrics. |
| GG-43568 | Cluster Storage Engine | Near caches are now supported in embedded mode. |
| GG-43606 | Cluster Data Snapshots and Recovery | Global status of snapshot is now printed in allNodes mode. |
| GG-43610 | Cluster SQL Engine | You can now install GridGain DR connector from Docker. |
| GG-43611 | Cluster Storage Engine | Near Cache now supports getAll() and containsAll() operations. |
| GG-43626 | SQL | Updated parquet-avro to version 1.15.2. |
| GG-43642 | SQL | Added support for automatic conversion of values of legacy java time api during DCR from GridGain 8. |
| GG-43757 | Cluster Storage Engine | Added automatic updates to Near Cache using continuous queries. |
| GG-43814 | Cluster Rolling Upgrade | Fixed an issue that prevented older node from joining GridGain 9.1.2 cluster during rolling upgrade. |
| GG-43835 | Cluster Data Snapshots and Recovery | Fixed an issue that could lead to some data not being restored from snapshots. |
| GG-43850 | Cluster Continuous Queries | Continuous queries will continue to publish events after the table is dropped for short period until corresponding storage is destroyed. |
| GG-43851 | Platforms & Clients | Added Python 3 client. |
| GG-43852 | Distributed Data Structures | Distributed maps can now be created from java clients. |
| GG-43854 | Platforms & Clients | Python Client: Introduced Heartbeats. |
| GG-43858 | Distributed Data Structures | Improved Ignite native types mapping in map structures API. |
| GG-43906 | Cluster Deployment | Added KEDA configuration to Helm chart. |
| GG-43990 | Cluster SQL Engine | Fixed the issue when compaction process could get stuck after dropping distribution zone. |
| GG-44001 | Builds and Deliveries | Updated httpclient5 to version 5.4.3. |
| GG-44008 | Cluster Storage Engine | Fixed a rare issue that caused a node to be unable to join a cluster after complete cluster restart due to errors in metastore. |
| GG-44042 | Builds and Deliveries | Update Kafka client dependency from 3.9.0 to 3.9.1. |
| GG-44067 | Cluster Continuous Queries | Added ContinuousQueryOptions.partitions option to query only certain partitions. |
| GG-44127 | Cluster Continuous Queries | Added an CQ option for configuring an executor for async delivery and execution of subscriber methods. |
| GG-44169 | Distributed Data Structures | You can now specify the distribution zone the distributed map will be stored at. |
| GG-44170 | Distributed Data Structures | You can now specify the non-standard storage engine for distributed maps. |
| GG-44178 | Cluster SQL Engine | You can now configure basic authentication for DR connector. |
| GG-44187 | Cluster Continuous Queries | Java thin: fixed continuous query compatibility with older servers. |
| GG-44188 | Cluster Continuous Queries | .NET client can now handle CQ events coming after table dropped. |
| GG-44330 | Cluster Data Snapshots and Recovery | Requesting a snapshot for a future timestamp now gets rejected. |
| GG-44340 | Cluster Storage Engine | Fixed a rare scenario where select with projection could fail. |
| GG-44343 | Cluster Deployment | Added BOOTSTRAP_NODE_CONFIG variable for docker compose file. |
| GG-44379 | Builds and Deliveries | Added -XX:+PerfDisableSharedMem JVM parameter to bootstrap configuration to improve performance in certain scenarios. |
| GG-44404 | General | Fixed NullPointerException when logging address binding error for data center replication. |
| GG-44459 | Builds and Deliveries | Updated Apache Commons Lang3 dependency to v3.18.0. |
| GG-44621 | Cluster Storage Engine | Fixed data inconsistency issues when using columnar storage in Docker. |
| GG-44631 | Cluster Storage Engine | Updated RocksDB to version 10.2.1. |
| GG-44644 | Cluster SQL Engine | Added an ability to configure complex data mapping during data migration from GridGain 8. |
| GG-44646 | Cluster Storage Engine | Updated RocksDB to version 10.2.1. |
| GG-44820 | Cluster Storage Engine | BOOTSTRAP_NODE_CONFIG variable is no longer required to start GridGain via docker compose. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.0`, `9.1.1`, `9.1.2`, `9.1.3`, `9.1.4`, `9.1.5`, `9.1.6`, `9.1.7`

## Known Limitations

### Data Restoration After Data Rebalance

Currently, data rebalance may cause partition distribution to change and cause issues with snapshots and data recovery. In particular:

- It is currently not possible to restore a `LOCAL` snapshot if data rebalance happened after snapshot creation. This will be addressed in one of the upcoming releases.
- It is currently not possible to perform point-in-time recovery if data rebalance happened after table creation. This will be addressed in one of the upcoming releases.

### SQL Performance in Complex Scenarios

There are known issues with the performance of SQL read-write transactions in complex read-write scenarios. These issues will be addressed in an upcoming releases.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
