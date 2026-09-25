---
description: >-
  How to manage and monitor GridGain data center replication — starting,
  stopping, pausing, JMX beans, events, failure scenarios, and sender storage management.
---

# Managing and Monitoring Replication

This chapter describes how to manage and monitor your GridGain Data Center Replication.

{% hint style="info" %}
You can also manage data center replication by using the [control script](../../reference/cli-tool/README.md#data-center-replication).
{% endhint %}

## Managing Replication Process

The replication process can be managed per cache.

If sender nodes are available, the replication process starts automatically when the master cluster is started. If sender nodes are not available, replication will pause. You will need to start it manually.

### Full State Transfer

Full state transfer is the process of sending the entire cache content to the replica cluster.

Before starting the replication process, you must synchronize the caches in the master and replica clusters.
If you start with empty caches, you do not need to do anything. However, if the caches in the master cluster already have data, you need to perform a _full state transfer_.

You perform a full state transfer as explained in [Using JMX Beans](#using-jmx-beans-to-monitor-and-manage-replication).

### Starting Replication

To start the replication process for a specific cache, use one of the [JMX beans](#using-jmx-beans-to-monitor-and-manage-replication) and perform the `startReplication(cache)` operation.
After performing the start operation, GridGain will start processing data updates that occur in the cache.

### Stopping Replication

The replication process for a particular cache can be stopped either manually or automatically. If GridGain detects that the data cannot be replicated for any reason, the replication process will be stopped automatically.
Possible reasons include:

- The sender nodes configured to replicate data are not available.
- The [sender storage](configuring-replication.md) is full or corrupted.

{% hint style="warning" %}
The replication process must be started manually after being stopped. If the caches in the master cluster were updated during the pause, you must [start the replication process](#starting-replication) again.
{% endhint %}

A manual pause can be performed through the [JMX Bean](#using-jmx-beans-to-monitor-and-manage-replication).

### Pausing and Resuming Replication

You can pause the replication process between the master cluster and a specific replica cluster by suspending the process on the sender nodes.
The sender nodes will stop sending data to the replica and store the updates into the [storage](configuring-replication.md).
All data updates that happen during the pause will be accumulated in the sender storage. When you resume the replication process, the sender nodes will send the accumulated data to the replica cluster.

#### Control.sh Script

You can [pause](../../reference/cli-tool/README.md#dr-pause) and [resume](../../reference/cli-tool/README.md#dr-resume) data center replication by running the corresponding `control.sh` commands on the relevant server nodes.

Because the `pause` operation does not change the process status, the only way to verify that the replication has been paused is by invoking the `paused(dcId)` method on the sender-related MBean with the relevant `dcId` passed as an argument.

#### Full State Transfer Priority

In high load scenarios when using non-incremental replication or when the `GG_INCREMENTAL_DR_USE_REGULAR_STORE` property is enabled, it may be necessary to manage traffic priority. When regular store is used, there are two types of updates:

- Updates for current load being synchronized between the data centers;
- FST updates sequentially copying data for [Full State Transfer](#full-state-transfer).

By default, FST updates are resolved last, and this may lead to a backlog forming. To avoid this, you can dynamically manage replication has a priority. The following options are available:

- `FST_LAST` - regular replication has priority over FST. This policy is used as default.
- `FST_FIRST` FST has priority over regular replication.
- `ROUND_ROBIN` - Regular and FST replications have the same priority and are resolved via round-robin scheduling.
- `FAIR` - Regular and FST batches priority are shared fairly.

You can change the priority during runtime by setting the `dr.sender.store_scan_policy` option from the [control script](../../reference/cli-tool/README.md#property-set):

```shell
$GG_HOME/bin/control.sh --property set --name 'dr.sender.store_scan_policy' --val ROUND_ROBIN
```

#### JMX Beans

The [Using JMX Beans to Monitor and Manage Replication](#using-jmx-beans-to-monitor-and-manage-replication) section explains how to pause/resume replication using JMX beans.

## Using JMX Beans to Monitor and Manage Replication

The following JMX Bean provides information about the replication process of a specific cache. The bean can be obtained on any node that hosts the cache.

**MBean's ObjectName:**

```
group=<Cache_Name>,name="Cache data replication"
```

| Attribute | Type | Description | Scope |
|---|---|---|---|
| DrSenderGroup | String | The sender group name. | Global |
| DrStatus | String | The status of the replication process for this cache. | Global |
| DrQueuedKeysCount | int | The number of entries waiting to be sent to the sender node. | Node |
| DrSenderHubsCount | int | The number of sender nodes available for the cache. | Global |
| pendingQueueSize | long | Number of cache updates in the DR pending queue. | Node |
| backupQueueSize | long | Number of cache updates in the DR backup queue. | Node |

| Operation | Description |
|---|---|
| start | Start the replication process for this cache. |
| stop | Stop the replication process for this cache. |
| transferTo (id) | Perform a full state transfer of the content of this cache to the given replica cluster ID. |

The following MBean can be obtained on a sender node and allows you to pause/resume the replication process on that node.

**MBean's ObjectName:**

```
group="Data Center Replication",name="Sender Hub"
```

| Operation | Description |
|---|---|
| pause (id) | Pause replication for the given replica cluster ID. This operation will stop sending updates to the replica cluster. The updates will be stored in the [sender storage](configuring-replication.md) until the replication is resumed. |
| pause | Pause replication for all replica clusters. |
| resume (id) | Resume replication for the given replica cluster ID. |
| resume | Resume replication for all replica clusters. |
| paused (id) | Return the status of the replication process of a sender node. `True` means that the process has been paused. |

## Synchronizing Storage

When data center replication is enabled on the cache, it automatically replicates updates to caches on the cache to the connected cache. During normal operation, this process does not require user interaction, however you may want to make sure some important updates are replicated. You can do this by using the `flush()` method. This method returns a future that you can use to keep track of the replication process. Once the future is returned, the remote cache is in the same state as the local cache was at the moment the method was called.

```java
IgniteFuture<?> flushFut = gg.dr(myNode).flush("myCache");

flushFut.get();
```

## Troubleshooting

When using data replication, you can monitor various statistics provided through JMX beans and events to make sure that the replication process is running smoothly.

Most common problems that you may want to monitor include:

- [Problem: Size of the sender storage is growing](#problem-size-of-the-sender-storage-is-growing)
- [Problem: Sender storage is full or corrupted](#problem-sender-storage-is-full-or-corrupted)
- [Problem: There are failed batches](#problem-there-are-failed-batches)

### Problem: Size of the sender storage is growing

If the sender storage size on a specific sender node is growing, it means that the sender is not keeping up with the load or there is a problem with the connection to the replica cluster.

**How to monitor:**
Monitor the metric that shows the size of the storage

**Actions:**
Check network capacity or add more sender nodes and/or receivers.

### Problem: Sender storage is full or corrupted

When the sender storage gets full or becomes corrupted (i.e., due to an error), the replication process will stop for all caches.

**How to monitor:**
Listen to the `EVT_DR_STORE_OVERFLOW` or `EVT_DR_STORE_CORRUPTED` events. Refer to the [Data Replication Events](#data-replication-events) section for more information.

**Actions:**
After addressing the issue that caused the sender storage to get full, you have to do a [full state transfer](#full-state-transfer).

### Problem: There are failed batches

{% hint style="info" %}
This problem is only applicable to non-incremental DR. When using incremental DR, the replication is instead paused until it can be resumed.
{% endhint %}

Updated entries are accumulated into batches on the primary nodes; then, each batch is sent to one of the sender nodes.
If no sender is available, the batch will be marked as failed. Failed batches will never be resent.

**How to monitor:**
Monitor the `GridDr.senderCacheMetrics("myCache").batchesFailed()` metric for all caches that are configured to replicate their data.

**Actions:**
Make sure that at least one sender is available to all server nodes in the master cluster.
You will need to do a [full state transfer](#full-state-transfer) to synchronize the cache's content with the replica cluster.

### Problem: The pending queue is growing

Pending queue is used by incremental DR to store data has not yet been sent to a sender. This includes cases when a sender or remote datacenter returns an error and the replication cannot be confirmed.

When using incremental DR, if no sender is available, replication is instead paused until a sender becomes available. In this case, the pending queue may keep growing as no replication is performed.

{% hint style="info" %}
In most scenarios pending queue does not require additional storage. For file-based senders however, additional space will be required to store this data.
{% endhint %}

**How to monitor:**
Monitor the size of the `GridDr.senderCacheMetrics("myCache").pendingQueue()` metric for all caches that are configured to replicate their data.

**Actions:**
Check the status of senders. If any are returning errors, make sure to resolve them. The replication will continue normally once the problems are resolved.

## Data Center Replication Failure Scenarios

The table below covers common failure scenarios during active-passive data transfer and provides basic information on resolving them.

| No. | Master Data Nodes | Sender Group Nodes | Receiver Group Nodes | Replica Data Nodes | Impact on Replication Process | Recovery Process |
|---|---|---|---|---|---|---|
| 1. | All Nodes Down | Up | Up | Up | Replication will stop. | Restart data nodes to resume replication. |
| 2. | Up | At least 1 Up | Up | Up | Replication will continue, primary node will send data by using the active Sender Node. | No action required. |
| 3. | Up | All Nodes Down | Up | Up | Replication Process will be stopped. | If primary cache was not updated after all sender nodes were stopped, replication can be continued after restarting sender nodes. Otherwise, you need to perform full state transferscratch. |
| 4. | Up | Up | At least 1 Up | Up | Replication will continue by using the active receiver node. | No action required. |
| 5. | Up | Up | Down | Up | Replication process will continue until sender storage is filled. | Restart receiver nodes. Replication will resume automatically. |
| 6. | Up | Up | Up | Down | Replication process will continue until `messageQueueLimit` is reached on receiver hub. After that, receiver nodes will stop accepting new messages from Sender. If sender storage becomes full, issues described in case 3 can happen. | Restart replica data nodes. Replication will continue. |
| 7. | Down | Down | Up | Up | Replication will stop. | If sender nodes were stopped first and data was changed before data nodes stopped, full state transfer is required. Otherwise, replication will continue once all nodes are brought back up. |
| 8. | Up | Up | Down | Down | Replication will continue until sender storage is full. | Restart receiver nodes and replica data nodes. sender will start sending accumulated messages. |

## Data Replication Events

In addition to metrics, you can listen to replication-specific events.
DR events must be enabled first and can be handled as regular Ignite events.
To learn how to listen to specific events, refer to the [Working with Events](../../gridgain8-usage/events/listening-to-events.md) section. Replication events may include a collection of `DrUpdateEntry` objects containing information about specific entries that were updated prior to triggering this event.

```java
IgniteConfiguration cfg = new IgniteConfiguration();

// Enable the event
cfg.setIncludeEventTypes(org.gridgain.grid.events.EventType.EVT_DR_CACHE_REPLICATION_STOPPED);

//enable data replication
cfg.setPluginConfigurations(new GridGainConfiguration().setDataCenterId((byte) 1));

Ignite ignite = Ignition.start(cfg);

IgniteEvents events = ignite.events();

// Local listener that listens to local events.
IgnitePredicate<DrCacheReplicationEvent> localListener = evt -> {

    CacheDrPauseReason reason = evt.reason();

    System.out.println("Replication stopped. Reason: " + reason);
    return true; // Continue listening.
};

// Listen to the "replication stopped" events 
events.localListen(localListener, org.gridgain.grid.events.EventType.EVT_DR_CACHE_REPLICATION_STOPPED);
```

The replication event types are defined in the [`org.gridgain.grid.events.EventType`](https://www.gridgain.com/sdk/8.10/javadoc/org/gridgain/grid/events/EventType.html) class and are listed in the following table.

| Event Type | Event Description | Where Event Occurred |
|---|---|---|
| EVT_DR_REMOTE_DC_NODE_CONNECTED | A sender node connects to the node in the replica cluster. | The sender node. |
| EVT_DR_REMOTE_DC_NODE_DISCONNECTED | A sender node loses connection to the node in the replica cluster. The sender will try to connect to another receiver node if more than one is configured. If no receiver is available, the sender will try to reconnect after the period defined in the `DrSenderConfiguration.reconnectOnFailureTimeout` property. | The sender node. |
| EVT_DR_CACHE_REPLICATION_STOPPED | Replication of a specific cache is stopped due to any reason. A [full state transfer](#full-state-transfer) is required before resuming the replication process. | All nodes that host the primary partitions of the cache. |
| EVT_DR_CACHE_REPLICATION_STARTED | Replication of a specific cache is started. | All nodes that host the primary partitions of the cache. |
| EVT_DR_CACHE_FST_STARTED | A full state transfer for a specific cache is started. | All nodes that host the primary partitions of the cache. |
| EVT_DR_CACHE_FST_FAILED | A full state transfer for a specific cache fails. | All nodes that host the primary partitions of the cache. |
| EVT_DR_STORE_OVERFLOW | A sender node cannot store entries to the sender storage because the storage is full. Manual restart and a full state transfer may be required after the issue is fixed. | The sender node. |
| EVT_DR_DC_REPLICATION_RESUMED | Replication to a specific cluster is resumed on a sender node. | The sender node. |
| EVT_DR_RECEIVER_UPDATE_RECEIVED | The receiver node received an update. | The receiver node. |
| EVT_DR_RECEIVER_UPDATE_ACKED | The receiver node sent the acknowledgment message after receiving the update. | The receiver node. |
| EVT_DR_RECEIVER_UPDATE_APPLIED | The receiver node applied the update. | The receiver node. |
| EVT_DR_RECEIVER_UPDATE_FAILED | The receiver node failed to apply the update. | The receiver node. |
| EVT_DR_SENDER_UPDATE_SENT | The sender node sent the update. | The sender node. |
| EVT_DR_SENDER_UPDATE_ACKED | The sender node received the update acknowledgement from the receiver node. | The sender node. |
| EVT_DR_SENDER_UPDATE_FAILED | The sender node failed to send the update, or the receiver node failed to apply the update. | The sender node. |

### Storage Management

{% hint style="info" %}
This section only applies to non-incremental data center replication. New GridGain installations (GridGain 8.8.5 or later) use incremental replication by default.
{% endhint %}

You need to manually configure storage management. Before updates are sent to the replica cluster, they are accumulated in a sender storage in the master cluster.

The sender storage can be configured on a sender node in the connection configuration.
If you configured replication to multiple clusters, we recommend configuring a different storage for each connection.

When the sender storage gets full (this can happen because of a broken connection to the replica cluster) or corrupted, the replication process will stop.
You can listen to the `EVT_DR_STORE_OVERFLOW` or `EVT_DR_STORE_CORRUPTED` events to get notified if this situation occurs. Refer to the [Data Replication Events](#data-replication-events) section.

GridGain ships with two implementations of the sender storage:

- `DrSenderFsStore` - A persistent storage that stores data updates on disk and can survive sender node restarts. This implementation is used by default.
- `DrSenderInMemoryStore` - An in-memory storage that stores data updates in RAM.

To configure a sender storage, use the `DrSenderConnectionConfiguration.setStore(store)` method.
Refer to the examples below for details.

**Disk-Based Storage**

The directory where cache updates are stored can be configured by setting the `DrSenderFsStore.directoryPath` property.
The property has a default value, but we recommend setting it explicitly.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.gridgain.grid.configuration.DrSenderConfiguration">
    <!-- this node is part of group1 -->
    <property name="senderGroups">
        <list>
            <value>group1</value>
        </list>
    </property>
    <!-- connection configuration -->
    <property name="connectionConfiguration">
        <bean class="org.gridgain.grid.dr.DrSenderConnectionConfiguration">
            <!-- dr storage -->
            <property name="store">
                <bean class="org.gridgain.grid.dr.store.fs.DrSenderFsStore">
                    <property name="directoryPath" value="/path/to/store"/>
                </bean>
            </property>
            <!-- the ID of the remote cluster -->
            <property name="dataCenterId" value="2"/>
            <!-- Addresses of the remote cluster's nodes this node will connect to -->
            <property name="receiverAddresses">
                <list>
                    <value>172.25.4.200:50001</value>
                </list>
            </property>
        </bean>
    </property>
</bean>
```
{% endtab %}
{% tab title="Java" %}
```java
DrSenderConfiguration drSenderCfg = new DrSenderConfiguration();
drSenderCfg.setSenderGroups("group1");

// the addresses of the replica cluster's nodes that will receive data updates 
DrSenderConnectionConfiguration senderConnectionCfg = new DrSenderConnectionConfiguration()
        .setDataCenterId((byte) 2).setReceiverAddresses("172.25.4.200:50001");
senderConnectionCfg.setStore(new DrSenderFsStore().setDirectoryPath("/path/to/storage"));

drSenderCfg.setConnectionConfiguration(senderConnectionCfg);
```
{% endtab %}
{% endtabs %}

**In-Memory Storage**

When in-memory implementation of the sender storage is used on a sender node and the node goes down, replication will stop.
All updates that the storage kept when it went down will be lost, and you will have to do a [full state transfer](#starting-replication) before starting it again.

**Custom Implementation**

In addition to the two implementation of the storage described above, you can add a custom storage by implementing the `org.gridgain.grid.dr.store.DrSenderStore` interface.
If you intend the storage to persist updates, annotate the implementation with the `@org.gridgain.grid.dr.store.DurableStore` annotation.
In this case, the replication process will not be stopped if the sender node with this storage goes down.
The process will wait for the storage to be available again.
Once the storage is available, the updates the storage kept when it went down will be sent to the replica cluster.

{% hint style="info" %}
If your `DrSenderConfiguration` configuration has multiple connections with durable and non-durable storages, then the sender will treat the storages as durable only if all storages are annotated with `@DurableStorage`.
{% endhint %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
