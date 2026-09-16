---
description: >-
  Near-zero downtime migration from GridGain 8 to GridGain 9 using one-way data
  center replication: prepare tables, replicate, monitor, cut over, and roll back.
---

# Data Center Replication from GridGain 8

{% hint style="info" %}
This feature is available only as part of GridGain 8 Enterprise and Ultimate editions.
{% endhint %}

In certain environments, downtime associated with migrating data between GridGain versions is not acceptable. For these scenarios, GridGain provides a one-way data migration tool based on [GridGain 8 Data Center Replication](https://www.gridgain.com/docs/latest/administrators-guide/data-center-replication/introduction). From the GridGain 8 source cluster's perspective, the GridGain 9 cluster appears as another GridGain 8 data center.

After replication is complete, a brief pause is required to stop writes, flush the replication backlog, and switch traffic to GridGain 9. As such, this is a "near-zero downtime" migration, not a seamless one. A brief maintenance window is required during the final cutover to ensure data consistency.

## Migration Workflow Summary

1. Prepare target tables and indexes.
2. Configure the GridGain 8 DR sender and the GridGain 9 DR connector.
3. Start the DR connector.
4. Verify connectivity.
5. Start full state transfer.
6. Monitor replication backlog.
7. Pause writes on GridGain 8.
8. Wait for the backlog to drain.
9. Repoint clients to GridGain 9.
10. Stop replication and clean up replication artifacts.

## Prerequisites

Before starting replication, complete the following:

1. Create an empty target GridGain 9 table for each cache to be replicated.

   By default, fields are matched to columns with the same name. You can manually configure field-to-column mappings if necessary. For caches with a single key or value field, use the `_key` or `_val` field name. See [Mapping a plain-type key cache](dcr-connector.md#mapping-a-plain-type-key-cache) and [Mapping a plain-type value cache](dcr-connector.md#mapping-a-plain-type-value-cache) for details, and [Cache-to-Table Mapping Rules](#cache-to-table-mapping-rules) for default naming.
2. Add a nullable `drVersion` column of type `VARBINARY` to each target GridGain 9 table. This column stores data center replication metadata and can be safely deleted after migration. Replication cannot start without it.
3. Recreate indexes from GridGain 8 on the target GridGain 9 tables. Indexes are not transferred automatically and must be created manually to maintain query performance. See [Recreate indexes](#recreate-indexes) for details.
4. Initialize the GridGain 9 cluster if you have not done so already:

   ```bash
   gridgain9 cluster init --name <cluster-name> --metastorage-group <node-name> --license <path-to-license> --url http://localhost:10300
   ```
5. Contact GridGain [support](https://support.gridgain.com) to enable data center replication for any existing caches you plan to replicate.

## Type Mapping

GridGain 8 and GridGain 9 differ in their support for [data types](../sql-reference/data-types.md). Make sure data is mapped to columns of equivalent types. The table below provides a reference for commonly used types:

| GridGain 8 Type | GridGain 9 Type | Notes |
|---|---|---|
| java.lang.Boolean | BOOLEAN | |
| java.lang.Byte | TINYINT | |
| java.lang.Short | SMALLINT | |
| java.lang.Integer | INT | |
| java.lang.Long | BIGINT | |
| java.lang.Float | REAL | |
| java.lang.Double | DOUBLE | |
| java.math.BigDecimal | DECIMAL(p,s) | Specify precision and scale |
| java.lang.String | VARCHAR | Specify length if needed |
| byte[] | VARBINARY | Specify length if needed |
| java.util.Date | TIMESTAMP WITH LOCAL TIME ZONE | Consider timezone settings |
| java.sql.Time | TIME | Consider timezone settings |
| java.sql.Date | DATE | Consider timezone settings |
| java.sql.Timestamp | TIMESTAMP | Consider timezone settings |
| java.util.UUID | UUID | |

{% hint style="info" %}
Types that are not explicitly mentioned in this table, such as `org.apache.ignite.binary.BinaryObject` or user types, are not supported.
{% endhint %}

## Cache-to-Table Mapping Rules

The DR connector determines the target GridGain 9 table from the *cache name*, not from `QueryEntity.tableName`.

When no `cacheMapping` is configured for a cache, the DR connector:

- Uses the cache name verbatim as the target table name.
- Always targets the `PUBLIC` schema.
- Does not strip the `SQL_PUBLIC_` prefix that GridGain 8 adds to caches backing SQL-created tables.
- Does not support configuring a different default schema.

Examples:

- Cache `SQL_PUBLIC_PERSON` maps to table `PUBLIC.SQL_PUBLIC_PERSON`
- Cache `PersonCache` maps to table `PUBLIC.PersonCache`

If the target table name or schema differs from the source cache name, configure an explicit `cacheMapping` entry in the DR connector configuration.

Examples of cases that require explicit `cacheMapping`:

- Replicating cache `SQL_PUBLIC_PERSON` to table `PUBLIC.PERSON`
- Replicating cache `PersonCache` to table `CUSTOM.PERSON`
- Replicating a cache created programmatically with a `QueryEntity.tableName` value different from the cache name

The DR connector does not read or use `QueryEntity.tableName`. If a cache was created through the programming API with a `QueryEntity` whose `tableName` differs from the cache name, the connector has no knowledge of that mapping and falls back to using the cache name directly.

For additional configuration examples, see [DR Connector](dcr-connector.md).

## Row Replication Algorithm

Inserts/updates/removes from the source GridGain 8 cluster are versioned. If a row or tombstone record in the target GridGain 9 cluster has version `V1`, and the source GridGain 8 cluster sends an insert, update, or remove operation with version `V2` lower than `V1`, the DR connector ignores the operation. Otherwise, the DR connector applies the operation as follows:

| GridGain 8 action | GridGain 9 state | DR connector action |
|---|---|---|
| insert/update entry | key does not exist | insert row |
| insert/update entry | key exists, `drVersion` column is not `NULL` | update row, overwrites all columns |
| insert/update entry | key exists, `drVersion` column is `NULL` | no action |
| remove entry | key exists, `drVersion` column is not `NULL` | create tombstone record in the tombstones table |
| remove entry | key exists, `drVersion` column is `NULL` | no action |
| remove entry | key does not exist | create tombstone record in the tombstones table |

## Prepare GridGain 9 Tables and Indexes

{% hint style="info" %}
You can prepare your tables by using the [Persistent Data Migration](persistent-migration.md) to replicate your caches.
{% endhint %}

Here's an example of migrating a GridGain 8 cache schema to GridGain 9:

- Original GridGain 8 cache:

  ```java
  // GridGain 8 cache with composite key
  public class PersonKey {
      private Long id;
      private String region;
  }

  public class Person {
      private String name;
      private Integer age;
      private BigDecimal salary;
  }
  ```

  {% hint style="info" %}
  The DR connector matches field names case-sensitively. Java class field names are typically lowercase (`id`, `name`), while SQL columns created without quoted identifiers are stored in uppercase (`ID`, `NAME`). If your GridGain 8 cache stores typed Java objects, use explicit `keyFields` / `valueFields` mappings in the connector configuration to map lowercase field names to uppercase column names. See [Field Mapping Rules](dcr-connector.md#field-mapping-rules) for details.
  {% endhint %}
- Creating equivalent GridGain 9 table:

  ```sql
  CREATE TABLE IF NOT EXISTS PUBLIC.PERSON (
      ID BIGINT NOT NULL,
      REGION VARCHAR NOT NULL,
      NAME VARCHAR,
      AGE INT,
      SALARY DECIMAL(10,2),
      drVersion VARBINARY,  -- Required for replication
      PRIMARY KEY (ID, REGION)
  );
  ```

### Recreate Indexes

Since indexes are not automatically transferred during DCR migration, you need to identify existing indexes in GridGain 8 and recreate them in GridGain 9.

To identify indexes in GridGain 8, query the system views:

```sql
-- List all indexes for a specific table
SELECT * FROM SYS.INDEXES
WHERE TABLE_NAME = 'PERSON';
```

Alternatively, you can use the control script to list caches and check which indexes are configured:

```bash
./bin/control.sh --cache list '.*'
```

After identifying the indexes, create them in GridGain 9 before starting replication:

```sql
-- Example: recreating indexes for the PERSON table
CREATE INDEX idx_person_age ON PERSON(AGE);
CREATE INDEX idx_person_name ON PERSON(NAME);
CREATE INDEX idx_person_salary_region ON PERSON(SALARY, REGION);
```

The indexes should be created after table creation but before starting the replication process for optimal performance during data transfer.

## Configuring Replication

### Configure GridGain 8 DR Sender and GridGain 9 DR Connector

Configuring replication to a GridGain 9 cluster on the GridGain 8 side is the same as configuring replication to a GridGain 8 cluster. On the GridGain 9 side, you need to start a connector tool that converts data from GridGain 8 and transfers it to GridGain 9.

Make sure to note the ID of the data center the source cluster is running in. This ID will be used in connector configuration to filter incoming connections.

{% hint style="info" %}
Only `drReceiverConfiguration.dataCenterId` (on the GridGain 9 DR connector) is significant — it must match the `dataCenterId` of the source GridGain 8 cluster that *sends data*. The `dataCenterId` in `DrSenderConnectionConfiguration` is ignored.
{% endhint %}

The example below shows where in GridGain 8 configuration you can find data center ID.

```xml
<bean class="org.gridgain.grid.configuration.GridGainConfiguration">
    <!--
     datacenter id that identifies the source Gridgain 8 cluster.
     This parameter must match the drReceiverConfiguration.datacenterId parameter.
     -->
    <property name="dataCenterId" value="<source-datacenterId>"/>
    <property name="drSenderConfiguration">
        <bean class="org.gridgain.grid.configuration.DrSenderConfiguration">
            <property name="connectionConfiguration">
                <bean class="org.gridgain.grid.dr.DrSenderConnectionConfiguration">
                    <!--
                    datacenterId that identifies the dr connector that writes data to the target Gridgain 9 cluster.
                    -->
                    <property name="dataCenterId" value="<dr-connector-datacenterId>"/>
                    <property name="receiverAddresses">
                        <list>
                            <value>[dr-connector-host]:[dr-connector-port]</value>
                        </list>
                    </property>
                    ...
                </bean>
            </property>
            ...
        </bean>
    </property>
    ...
</bean>
```

The cache-to-table mapping (including whether the connector uses the default `PUBLIC.<cache-name>` mapping or an explicit `cacheMapping`) is configured separately on the DR connector side. See [Cache-to-Table Mapping Rules](#cache-to-table-mapping-rules) and [DR Connector](dcr-connector.md) for additional details and connector-side mapping examples.

For additional information on data center replication in GridGain 8 see [Data Center Replication in GridGain 8](https://www.gridgain.com/docs/latest/administrators-guide/data-center-replication).

### Tombstones

Tombstone time-to-live, configured via the `tombstoneTtl` property, on the receiving side must be the same as or greater than on the sending side. By default, the same value is used in GridGain 8 and GridGain 9 (30 minutes).

If a sender in the source GridGain 8 cluster has larger `tombstoneTtl` than the DR connector, then the following warning is written to the DR connector logs:

```
Sending DataCenter has higher tombstone TTL than Receiving one (remoteTombstoneTTL > localTombstoneTTL) [remoteAddress=<sender-address>, dataCenterId=<dataCenterId>, remoteTombstoneTTL=<sender-TombstoneTTL>, localTombstoneTTL=<dr-connector-TombstoneTTL>]
```

### Ensure That Time Zones Are in Sync

{% hint style="warning" %}
When migrating data from GridGain 8 to GridGain 9, it is required to set the `timeZone` parameter to match the original client's local time. If it does not match, the restored values may differ from the originals.
{% endhint %}

For additional information on configuring and running the DR connector tool, see [DR Connector](dcr-connector.md).

## Starting Replication

### Start the DR Connector

Start the connector tool on GridGain 9 side:

```bash
./start.sh --config-path <path-to-dr-connector-config-file>
```

For additional information on configuring DR connector, see [DR Connector](dcr-connector.md).

### Verify That the DR Connector Is Running

Check the DR connector logs to ensure it is listening on the configured port. Look for the "Listening port" line in the log, signifying that the DR connector is running and ready to receive data on the specified port.
See [Logging Configuration](dcr-connector.md#logging-configuration).

Once the DR connector connects to the GridGain 8 cluster, you can find the connection information in a GridGain 8 sender node's logs:

```
A sender hub has successfully connected to a remote receiver
```

### Check the GridGain 8 Sender Node

Retrieve the ID of a sender node in the source GridGain 8 cluster:

```bash
./bin/control.sh --dr topology
```

Example output:

```
--------------------------------------------------------------------------------
Data Center ID: 1
Topology: 1 server(s), 0 client(s)
Data nodes: <...>
--------------------------------------------------------------------------------
Sender hubs: 1
  nodeId=<sender-node-id>, Address=[<addresses>], Mode=Server
  ...
--------------------------------------------------------------------------------
Receiver hubs: <...>
--------------------------------------------------------------------------------
Other nodes: <...>
--------------------------------------------------------------------------------
Command [DR] finished with code: 0
Control utility has completed execution at: 2026-02-01T01:00:00.279
Execution time: 183 ms
```

Verify that this sender node is configured to send data to the target GridGain 9 cluster:

```bash
./bin/control.sh --dr node <sender-node-id> --config
```

Make sure that the DataCenterId matches the DR connector's address and ID.

```
--------------------------------------------------------------------------------
Data Center ID: <source-datacenterId>
Node addresses: [<addresses>]
Mode=Server, Baseline node
--------------------------------------------------------------------------------
Node is configured to send data to:
  DataCenterId=<dr-connector-datacenterId>, Addresses=[<dr-connector-host>:<dr-connector-port>] <-- displays dr-connector's address and datacenterId
Common configuration:
  StreamerThreadPoolSize=10
  ThreadPoolSize=4
  IncrementalDrThreadPoolSize=4
Sender configuration:
  SenderGroups=[<sender-group>] <-- includes names of sender groups used by replicated caches.
  MaxErrors=10
  MaxFailedConnectAttempts=5
  MaxQueueSize=100
  SocketSendBufferSize=0
  SocketReceiveBufferSize=0
  HealthCheckFrequency=2000
  ReadTimeout=5000
  ReconnectOnFailureTimeout=5000
  SystemRequestTimeout=5000
  StoreSizeBytes=0
  UseIgniteSslContextFactory=true
Command [DR] finished with code: 0
Control utility has completed execution at: 2026-02-01T01:00:00.279
Execution time: 151 ms
```

For additional information on how to configure senders see [Data Center Replication, Configure Connection Between Clusters](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/data-center-replication/configuring-replication#2-configure-connection-between-clusters).

### Verify That Cache Replication Is Enabled

Verify that each source cache has replication enabled by running this command for every source cache:

```bash
./bin/control.sh --dr cache <cache-name> --config
```

Example output:

```
--------------------------------------------------------------------------------
Data Center ID: <source-datacenterId>
--------------------------------------------------------------------------------
1 matching cache(s): [<cache-name>]
Sender configuration for cache "<cache-name>":
  PreferLocalSender=true
  BatchSendSize=0
  BatchSendFrequency=0
  EntryFilter=null
  LoadBalancingMode=DR_RANDOM
  StateTransferThreadsCount=2
  MaxBatches=32
  SenderGroup=<sender-group> <-- refers to the sender group specified in the sender node configuration.
  StateTransferThrottleBytes=10485760
  MaxBackupQueueSize=0
Command [DR] finished with code: 0
Control utility has completed execution at: 2026-02-01T01:00:00.279
Execution time: 185 ms
```

For additional information on how to configure replication for a cache see [Data Center Replication, Configure Caches](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/data-center-replication/configuring-replication#3-configure-caches).

### Initiate Full State Transfer from GridGain 8

Start full state transfer from the source GridGain 8 cluster:

```bash
./bin/control.sh --dr full-state-transfer start
```

The command prompts for confirmation before starting. To skip the prompt (for example, in scripts), add the `--yes` flag.

Alternatively, to start full state transfer for a subset of caches (comma-separated):

```bash
./bin/control.sh --dr full-state-transfer start --caches <cache1>,<cache2>
```

This will transfer data from the source GridGain 8 cluster to the target GridGain 9 cluster.

To list active full-state-transfer states, use the `list` command.

```bash
./bin/control.sh --dr full-state-transfer list
```

Example output while transfer is in progress:

```
--------------------------------------------------------------------------------
Data Center ID: <source-datacenterId>
--------------------------------------------------------------------------------
Full state transfer states:
CacheDrStateTransfer [id=<cache-state-transfer-id>, cacheName=<cache-name>, nodeId=<sender-node-id>, startTime=1770878397721, partitionsTransferred=1023, syncMode=true]
null
Command [DR] finished with code: 0
Control utility has completed execution at: 2026-02-01T01:00:00.279
Execution time: 4848 ms
```

Wait until the full state transfer completes, when that happens, `list` command returns an empty result:

```
--------------------------------------------------------------------------------
Data Center ID: <source-datacenterId>
--------------------------------------------------------------------------------
Full state transfer states:
null
Command [DR] finished with code: 0
Control utility has completed execution at: 2026-02-01T01:00:00.279
Execution time: 3686 ms
```

### Cancel Full State Transfer

To cancel a running full state transfer, use the `cancel` command.

```bash
# <cache-state-transfer-id> obtained from output of `./bin/control.sh --dr full-state-transfer list` command
./bin/control.sh --dr full-state-transfer cancel <cache-state-transfer-id>
```

Example output:

```
Full state transfer canceled, task id=<CacheDrStateTransfer.id>
Command [DR] finished with code: 0
Control utility has completed execution at: 2026-02-01T01:00:00.279
Execution time: 5487 ms
```

### Pause and Resume Replication

To pause replication from the source GridGain 8 cluster, run the `pause` command.

```bash
# dataCenterId specified in DrSenderConnectionConfiguration for the GridGain 9 DR connector
./bin/control.sh --dr pause <dr-connector-datacenterId>
```

{% hint style="info" %}
The `pause` command does not support a `--yes` flag. In non-interactive environments (scripts, CI), pipe confirmation explicitly: `echo 'y' | ./bin/control.sh --dr pause <dr-connector-datacenterId>`.
{% endhint %}

To resume replication from the source GridGain 8 cluster, run the `resume` command.

```bash
# dataCenterId specified in DrSenderConnectionConfiguration for the GridGain 9 DR connector
./bin/control.sh --dr resume <dr-connector-datacenterId>
```

## Monitoring Replication

After full state transfer is started, monitor replication progress to determine when the GridGain 9 cluster is caught up and ready for cutover.

### Check DR Status on GridGain 8

Use the control script to view the current replication status:

```bash
./bin/control.sh --dr node <sender-node-id> --metrics
```

Example output:

```
Data Center ID: <source-datacenterId>
Node addresses: [<addresses>]
Mode=Server, Baseline node
--------------------------------------------------------------------------------
Node is configured to send data to:
  DataCenterId=<dr-connector-datacenterId>, Addresses=[<dr-connector-host>:<dr-connector-port>]
Sender metrics:
  StoreSize=0
  BatchesSent=1
  BatchesReceived=1
  BatchesAcked=1
  AverageBatchAckTime=18.0
  BytesSent=182
  BytesReceived=182
  BytesAcked=236
  EntriesSent=1
  EntriesReceived=1
  EntriesAcked=1
  StoreIsOverflow=false
Command [DR] finished with code: 0
Control utility has completed execution at: 2026-02-01T01:00:00.279
Execution time: 146 ms
```

### Replication JMX Metrics

#### GridGain 8 Sender Node

Check the replication backlog for a cache via JMX MBean attributes at a sender node of the source GridGain 8 cluster:

```
org.apache.ignite.<cache-name>."Data Center Replication"
```

| Attribute name | Description |
|---|---|
| DrBatchWaitingAcknowledgeCount | The number of batches successfully processed by the DR connector |
| DrQueuedKeysCount | The number of entries waiting to be sent. When this value is 0, all updates to the cache have been replicated to the target table. |

#### DR Connector (Per-Cache)

Check JMX MBean attributes of the DR connector for a specific cache:

```
org.apache.ignite.metrics."Data Center Replication".receiver.<dr-connector-datacenterId>.<cache-name>
```

| Attribute name | Description |
|---|---|
| BatchesReceived | The number of batches received. |
| BatchesAcked | The number of batches successfully processed. |
| EntriesReceived | The number of entries received. |
| EntriesAcked | The number of entries successfully processed. |
| MessageQueueLength | The number of batches currently being processed. When this value is 0, all updates to this cache have been replicated to the target table. |

#### DR Connector (All Caches)

Check JMX MBean attributes of the DR connector to check overall replication progress:

```
org.apache.ignite.metrics."Data Center Replication".receiver
```

| Attribute name | Description |
|---|---|
| TotalBatchesAcked | The total number of batches successfully processed across all caches. |
| TotalEntriesReceived | The total number of entries received across all caches. |
| TotalEntriesAcked | The total number of entries successfully processed across all caches. |
| TotalMessageQueueLength | The total number of batches currently being processed across all caches. When this value is 0, all updates from all caches have been replicated to the target cluster. |

### Monitor DR Connector Logs

Errors or warnings in the connector log typically indicate schema mismatches or connectivity issues. See [Troubleshooting](#troubleshooting) for common problems and solutions.
By default dr connector writes logs to `<dr-connector-directory>/log/dr-receiver-0.log`. See [Logging Configuration](dcr-connector.md#logging-configuration).

### Confirm Incremental Sync Is Caught Up

Once the replication backlog on the GridGain 8 side reaches zero:

1. The full state transfer is complete.
2. The connector is now applying incremental updates in near-real time.
3. Any new writes to GridGain 8 will be replicated with minimal delay.

At this point the cluster is ready for cutover. If you continue to write to GridGain 8 during this phase, the backlog will fluctuate but should remain small.

## Cutover

The cutover procedure requires a brief maintenance window to ensure no data is generated during the switch.

{% hint style="danger" %}
Do not allow writes to continue on GridGain 8 during cutover. Any writes performed after backlog validation may not be replicated to GridGain 9.
{% endhint %}

### Pause Writes on GridGain 8

Stop all applications that write to the GridGain 8 cluster. This ensures no new data is generated while you drain the replication backlog.

### Wait for the Backlog to Drain

Monitor the replication backlog for each source cache until it reaches zero. The relevant JMX MBean attributes:

| Source | Attribute path |
|---|---|
| GridGain 8 sender node (per cache) | `org.apache.ignite.<cache-name>."Data Center Replication".DrQueuedKeysCount` |
| DR connector (overall) | `org.apache.ignite.metrics."Data Center Replication".receiver.TotalMessageQueueLength` |

As a CLI alternative to JMX, use the control script to check the sender node metrics. The `StoreSize` field equals the number of entries waiting to be sent:

```bash
./bin/control.sh --dr node <sender-node-id> --metrics
```

```
Sender metrics:
  StoreSize=0       <-- 0 means no pending entries; backlog is drained
  StoreIsOverflow=false
  ...
```

Wait until all of the following are `0`:

- On the GridGain 8 sender: `DrQueuedKeysCount` for every replicated cache.
- On the DR connector: `MessageQueueLength` per cache.
- On the DR connector: `TotalMessageQueueLength` overall.

This confirms that all data written before the pause has been transferred to GridGain 9.

### Verify Row Counts

Compare row counts between GridGain 8 and GridGain 9 to confirm data consistency:

```bash
# Source GridGain 8 cluster
./bin/control.sh --cache list '.*'
```

```
--------------------------------------------------------------------------------
[cacheName=person, ..., cacheSize=<cache-size>, ... ]
Command [CACHE] finished with code: 0
Control utility has completed execution at: 2026-02-01T01:00:00.279
Execution time: 173 ms
```

Check the number of records in the target table by executing the following SQL query:

```bash
# GridGain 9 CLI
./bin/gridgain9 sql --jdbc-url=jdbc:ignite:thin://<gridgain9-host>:<gridgain9-client-port> "SELECT COUNT(*) FROM <target-schema>.<target-table>"
```

Repeat for each replicated table. The counts must match.
Compare results against known values or against the GridGain 8 cluster (which still holds the source data after writes have been paused).

### Repoint Client Applications to GridGain 9

Update your application configuration to connect to the GridGain 9 cluster and restart your applications. The specific steps depend on your deployment, but typically involve changing the connection string or endpoint addresses.

### Confirm That GridGain 9 Is Serving Traffic

Verify that client applications are successfully connected to GridGain 9 and processing requests. Check application logs and run test queries to confirm normal operation.

## Post-Cutover

### Stop Replication

Stop the replication process to the target GridGain 9 cluster on the GridGain 8 source cluster.

```bash
./bin/control.sh --dr pause <dr-connector-datacenterId>
```

For non-interactive use, see the `--yes`-flag note in [Pause and Resume Replication](#pause-and-resume-replication).

```
Warning: this command will pause data center replication for all caches.
Press 'y' to continue . . . y

--------------------------------------------------------------------------------
Data Center ID: <source-datacenterId>
--------------------------------------------------------------------------------
Command [DR] finished with code: 0
Control utility has completed execution at: 2026-02-01T01:00:00.279
Execution time: 1646 ms
```

Then stop the DR connector (see [Stopping the Connector](dcr-connector.md#stopping-the-connector)).

```bash
./stop.sh
```

### Clean Up Replication Artifacts

#### Drop the drVersion Column

The `drVersion` bookkeeping column is no longer needed after migration is complete. Remove it from each replicated table:

```sql
ALTER TABLE <target-schema>.<target-table> DROP COLUMN drVersion;
```

#### Drop the Tombstones Table

Each time DR connector starts, it automatically creates a table named `_DR_TOMBSTONES` in the `PUBLIC` schema to store cache entries removed from the source GridGain 8 cluster.
When replication is complete, this table is no longer needed and can be dropped:

```sql
DROP TABLE PUBLIC._DR_TOMBSTONES;
```

## Rollback

If validation fails *before* client applications have been repointed to GridGain 9, you can roll back to GridGain 8.

### Rollback Procedure

1. Ensure that client applications continue to use the GridGain 8 cluster.
2. Stop the DR connector.
3. Remove data from the target tables in the GridGain 9 cluster.
4. Drop the tombstones table in the GridGain 9 cluster.
5. Investigate and fix the issue that caused validation to fail (for example, schema mismatches or missing data).
6. Restart the migration from the beginning: a new full state transfer is required.

{% hint style="warning" %}
Replication is one-way (GridGain 8 to GridGain 9). Once client applications are writing to GridGain 9, changes cannot be replicated back to GridGain 8. Always validate data thoroughly *before* completing the switch to minimize the risk of needing a rollback.
{% endhint %}

## Troubleshooting

### Problem: Table Does Not Exist (Explicit Mapping)

```
org.apache.ignite.lang.TableNotFoundException: IGN-TBL-2 The table does not exist [name=<target-schema>.<target-table>] TraceId:49932d2f
```

The cache mapping for the source cache refers to a target table that does not exist.

*Actions:*

- Verify the cache mapping for the source cache and update the `table` property to refer to the correct table.
- If the cache mapping is correct, create the target table under the specified qualified name (see [the type mapping table](#type-mapping)).

{% hint style="info" %}
Use the `SYSTEM.TABLES` system view in the target GridGain 9 cluster to check existing tables.
{% endhint %}

### Problem: Table Does Not Exist (Default Mapping)

```
org.apache.ignite.lang.TableNotFoundException: IGN-TBL-2 The table does not exist [name=PUBLIC.<cache-name>] TraceId:49932d2f
```

When no cache mapping is configured for a source cache, the DR connector creates a default mapping that expects a target table with the same name as the cache in the `PUBLIC` schema.

*Action:*

- Verify that a cache mapping for the source cache exists. If no mapping exists, create one and restart the replication.

### Problem: Missing Bookkeeping Column

```
org.apache.ignite.lang.MarshallerException: IGN-MARSHALLING-1 Failed to serialize tuple for table <target-schema>.<target-table>: Value tuple doesn't match schema: schemaVersion=1, extraColumns=[DRVERSION] TraceId:67bcc4fb
```

The target table is missing the required `drVersion` bookkeeping column.

*Action:*

Add the bookkeeping column to the target table:

```sql
ALTER TABLE <target-schema>.<target-table> ADD COLUMN drVersion VARBINARY;
```

Then restart the replication.

### Problem: Value Too Long

```
# string value in the source cache is too long
org.apache.ignite.lang.MarshallerException: IGN-MARSHALLING-1 Failed to serialize row for table <target-schema>.<target-table>. Value too long [column='<column>', type=STRING(<length>)] TraceId:b5c4924b

# string value in the source cache is too long
org.apache.ignite.lang.MarshallerException: IGN-MARSHALLING-1 Failed to serialize row for table <target-schema>.<target-table>. Value too long [column='<column>', type=BYTE_ARRAY(<length>)] TraceId:b5c4924b
```

A source cache entry field contains a value that exceeds the column length in the target table.

*Action:*

Increase the column length in the target table:

```sql
ALTER TABLE <target-schema>.<target-table> ALTER COLUMN <column> SET DATA TYPE <expected-type>(<expected-length>);
```

Then restart the replication.

### Problem: Type Mismatch

```
org.apache.ignite.lang.MarshallerException: IGN-MARSHALLING-1 Value type does not match [column='<column>', expected=<type1>, actual=<type2>] TraceId:3a838ed3
```

There is a type mismatch between the source cache field and the target table column.

*Actions:*

If the source cache contains entries with _the same type_ for the problem field, this is a configuration issue: the target table column must use the correct type mapping (see [the type mapping table](#type-mapping)).

If the source cache contains entries with _different types_ in the problem field, configure a `RowTransformer` to handle entries for this cache.

In both cases, drop the target table and re-create it with the correct column types. Then restart the replication.

### Problem: Column Does Not Allow NULLs

```
org.apache.ignite.lang.MarshallerException: IGN-MARSHALLING-1 Failed to serialize row for table <target-schema>.<target-table>. Column '<column>' does not allow NULLs
```

A source cache entry field contains null values, but the target table column has a `NOT NULL` constraint.

*Actions:*

- If the column is not part of the primary key, drop and re-create the target table without the `NOT NULL` constraint on the affected column. Then restart the replication.
- If the column is part of the primary key, configure an `EntryTransformer` to replace null values with placeholder values. Update the DR connector's cache mapping to use the `EntryTransformer`, restart the DR connector, and then restart the replication.

### Problem: Unsupported User Type

```
Caused by: java.lang.IllegalStateException: Unable to process entries: table=<target-schema>.<target-table>, cache=<cache-name>
        at org.gridgain.internal.dr.DrReceiver.newEntryProcessingException(DrReceiver.java:216)
        at org.gridgain.internal.dr.DrReceiver.processEntries(DrReceiver.java:141)
        ... 27 more
Caused by: java.lang.IllegalStateException: User type is not supported: typeId=368385759
        at org.gridgain.internal.dr.binary.BinaryUtils.unmarshal(BinaryUtils.java:355)
        at org.gridgain.internal.dr.binary.BinaryObject.fieldByOrder(BinaryObject.java:115)
```

A source cache entry field contains a user-defined type that GridGain 9 does not support.

*Action:*

Configure an `EntryTransformer` to convert the user type to one or more supported columns. Adjust the target table schema if needed. Then restart the replication.

### Problem: Network Connectivity Issue Between DR Connector and GridGain 8 / GridGain 9 Cluster

DR connector loses network connectivity with the source GridGain 8 cluster or the target GridGain 9 cluster.

*Action:*

No action is needed. Network connection is reestablished automatically.
