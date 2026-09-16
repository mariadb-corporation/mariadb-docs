---
description: >-
  Run GridGain 8 client code against a GridGain 9 cluster with the migration
  adapter, configure the client connection, and rewrite collocated compute jobs.
---

# Codebase Migration

The GridGain 9 code follows patterns that are significantly different from those in GridGain 8. As a temporary measure, you can run your code via the code adapter.

Simple client code can be used to work with the GridGain 9 cluster by adding the migration adapter to your clients, both thick and thin. The adapter will run as an intermediary between your code and GridGain 9. You can keep using GridGain 8 APIs, and the adapter will convert the requests to the cluster dynamically.

However, this approach is limited to simpler code bases and causes a performance loss on higher load environments. More complex code needs to be migrated to GridGain 9 to be properly supported.

To start using the migration adapter:

- Add the migration adapter dependency to your project:

  ```xml
  <dependency>
    <groupId>org.gridgain.ignite</groupId>
    <artifactId>migration-tools-adapter</artifactId>
    <version>1.0</version>
  </dependency>
  ```
- Create the GridGain 9 client instance:

  ```java
  // Create a client instance configured to connect to your GridGain 9 cluster.
  // Ignite3Client.builder() returns an IgniteProxy, a proxy for the real GridGain 9 client, that the adapter builders accept.
  var ignite3Client = Ignite3Client.builder()
      .addresses("127.0.0.1:10800")
      .build();

  // Create your desired Ignite 2 interface.

  // Thick client
  try (IgniteAdapter adapter = IgniteAdapter.builder(ignite3Client)
      .allowExtraFields(true)
      .build()) {
      //...
  }

  // Client
  try (IgniteClient adapter = IgniteClientAdapter.builder(ignite3Client)
      .allowExtraFields(true)
      .build()) {
      //...
  }
  ```

In the above code:

- Setting `allowExtraFields` to `true` (default) allows extra fields in the Java client adapter. If you [migrate a cache in the PACK_EXTRA mode](persistent-migration.md#migrating-persistent-data), you can access additional fields in that cache - those that were not converted directly to columns.
- Setting `allowNonDefaultConstructors` to `true` (`false by default`) enables mapping Java classes that do not define a default constructor. This is not supported natively in GridGain 9. Therefore, we encourage you to implement default constructors in your data classes instead of allowing non-default constructors. The latter relies on unsafe mechanisms and introduces a modest performance penalty.
- `tableTypeRegistry` provides mappings between tables and the corresponding Java classes. In GridGain 8, this information is persisted to a system view, which can be overridden locally by individual records. Currently, the default implementation is stored in a persistent table.

Now you can use the `thinClient` or `thickClient` the same way as you would use an instance of the GridGain 8 client.

## Configuring the Client Connection

The `Ignite3Client.builder()` method accepts the following configuration options. All values other than `addresses` have sensible defaults; override them only when needed.

| Option | Default | Description |
|---|---|---|
| `addresses(String... addresses)` | Required | Host-port pairs of GridGain 9 server nodes, for example `"127.0.0.1:10800"`. When the port is omitted, `10800` is used. |
| `connectTimeout(long ms)` | 5000 | Socket-level connect timeout, in milliseconds. |
| `backgroundReconnectInterval(long ms)` | 30000 | How often the client tries to repair secondary connections to the cluster, in milliseconds. |
| `heartbeatInterval(long ms)` | 1000 | Keep-alive ping frequency, in milliseconds. |
| `heartbeatTimeout(long ms)` | 5000 | How long the client waits for a server response to a heartbeat, in milliseconds. |
| `operationTimeout(long ms)` | 0 (no timeout) | Per-request timeout, in milliseconds. `0` disables the timeout. |
| `metricsEnabled(boolean)` | false | Exposes client metrics via JMX when set to `true`. |
| `sqlPartitionAwarenessMetadataCacheSize(int)` | 1024 | Maximum number of cached entries used for partition-aware SQL routing. |
| `name(String)` | None | Optional client name used to distinguish multiple clients in JMX. |
| `backgroundReResolveAddressesInterval(long ms)` | 30000 | How often the client re-resolves the configured addresses via DNS, in milliseconds. |

## Collocated Compute and Partition-Local Queries

In GridGain 8, you could pin a compute job to a specific partition using `ComputeTask` with `setPartition` on the job context. GridGain 9 provides two approaches to achieve the same result, both based on running a job on the node that owns a partition and then querying only that partition's rows using the `__PARTITION_ID` virtual SQL column.

### Option 1: Broadcast to Table Partitions (Recommended)

Use `BroadcastJobTarget.table()` with `JobExecutionContext.partition()`. This is the preferred approach because GridGain routes each job instance to the node currently holding its partition, and `context.partition()` is always non-null, so execution is guaranteed to be local.

```java
JobDescriptor<Void, Long> partitionQueryJob = JobDescriptor.builder(PartitionQueryJob.class)
        .units(new DeploymentUnit(DEPLOYMENT_UNIT_NAME, DEPLOYMENT_UNIT_VERSION))
        .build();

Collection<Long> partitionCounts = client.compute().execute(table("Person"), partitionQueryJob, null);

long totalPersons = partitionCounts.stream().mapToLong(Long::longValue).sum();

System.out.println("\nTotal person count across all partitions: " + totalPersons);
```

Inside the job, read `context.partition()` to get the partition assigned to this instance, then filter rows with `__PARTITION_ID`:

```java
/**
 * Job that counts persons in a single table partition using the {@code __PARTITION_ID} virtual SQL column.
 *
 * <p>Designed for use with {@link BroadcastJobTarget#table}: one instance runs per partition,
 * {@code context.partition()} is always non-null, and the SQL query reads only local data.
 */
public static class PartitionQueryJob implements ComputeJob<Void, Long> {
    /** {@inheritDoc} */
    @Override
    public CompletableFuture<Long> executeAsync(JobExecutionContext context, Void arg) {
        Partition partition = context.partition();

        assert partition != null : "Partition must be non-null when using BroadcastJobTarget.table()";

        long count = 0;

        try (ResultSet<SqlRow> rs = context.ignite().sql().execute(
                (Transaction) null,
                "SELECT COUNT(*) FROM Person WHERE __PARTITION_ID = ?",
                partition.id()
        )) {
            if (rs.hasNext()) {
                count = rs.next().longValue(0);
            }
        }

        return completedFuture(count);
    }
}
```

### Option 2: MapReduce over Partition Distribution

Use `PartitionDistribution` to enumerate partitions in the split phase of a `MapReduceTask`, then dispatch one job per partition to its primary replica node:

```java
/**
 * MapReduce task that counts persons across all partitions of the {@code Person} table.
 *
 * <p>The split phase uses {@link PartitionDistribution#primaryReplicas()} to get the current primary replica node
 * for each partition, then creates one {@link PartitionPersonCountJob} per partition targeted at that node.
 * The reduce phase sums the per-partition counts.
 */
public static class PersonCountByPartitionTask implements MapReduceTask<Void, Long, Long, Long> {
    /** {@inheritDoc} */
    @Override
    public CompletableFuture<List<MapReduceJob<Long, Long>>> splitAsync(
            TaskExecutionContext taskContext,
            Void input) {
        // Run a SQL query to advance the node's observable timestamp tracker to the current
        // server time. MapReduce jobs are submitted server-side using the node's own tracker
        // (not the client's). Without this step, individual jobs may use a read timestamp
        // that predates inserts committed by the client before the task was submitted.
        try (ResultSet<SqlRow> rs = taskContext.ignite().sql().execute("SELECT COUNT(*) FROM Person")) {
            while (rs.hasNext()) {
                rs.next();
            }
        }

        JobDescriptor<Long, Long> jobDescriptor = JobDescriptor.builder(PartitionPersonCountJob.class)
                .units(new DeploymentUnit(DEPLOYMENT_UNIT_NAME, DEPLOYMENT_UNIT_VERSION))
                .build();

        Map<Partition, ClusterNode> primaryReplicas = taskContext.ignite().tables()
                .table("Person")
                .partitionDistribution()
                .primaryReplicas();

        List<MapReduceJob<Long, Long>> jobs = new ArrayList<>();

        for (Map.Entry<Partition, ClusterNode> entry : primaryReplicas.entrySet()) {
            jobs.add(MapReduceJob.<Long, Long>builder()
                    .jobDescriptor(jobDescriptor)
                    .nodes(Set.of(entry.getValue()))
                    .args(entry.getKey().id())
                    .build());
        }

        return completedFuture(jobs);
    }

    /** {@inheritDoc} */
    @Override
    public CompletableFuture<Long> reduceAsync(TaskExecutionContext taskContext, Map<UUID, Long> results) {
        return completedFuture(results.values().stream().mapToLong(Long::longValue).sum());
    }
}
```

Each job receives the partition ID as its argument and queries only that partition:

```java
/**
 * Job that counts persons in a single partition, identified by partition ID passed as the job argument.
 *
 * <p>The {@code __PARTITION_ID} virtual SQL column is used to filter rows to those belonging to the target
 * partition. The partition ID is provided by {@link PersonCountByPartitionTask} during the split phase.
 */
public static class PartitionPersonCountJob implements ComputeJob<Long, Long> {
    /** {@inheritDoc} */
    @Override
    public CompletableFuture<Long> executeAsync(JobExecutionContext context, Long partitionId) {
        long count = 0;

        try (ResultSet<SqlRow> rs = context.ignite().sql().execute(
                null,
                "SELECT COUNT(*) FROM Person WHERE __PARTITION_ID = ?",
                partitionId
        )) {
            if (rs.hasNext()) {
                count = rs.next().longValue(0);
            }
        }

        return completedFuture(count);
    }
}
```

{% hint style="info" %}
`PartitionDistribution.primaryReplicas()` captures partition locations at a point in time. If a partition is reassigned between the split phase and job execution, the job may run on a non-primary node and the SQL query will not be local. Use `BroadcastJobTarget.table()` (Option 1) when local execution must be guaranteed.
{% endhint %}

### How to Run a Local Query

Both approaches use the `__PARTITION_ID` virtual column (type `BIGINT`) to restrict a query to a single partition's rows. This is how you achieve the equivalent of GridGain 8's collocated queries without cross-node data movement:

```sql
SELECT * FROM Person WHERE __PARTITION_ID = ?
```

Pass the partition ID returned by `partition.id()` (Option 1) or the `long` ID passed as the job argument (Option 2) as the query parameter.
