---
description: >-
  GridGain 8.5.10 introduces substantial improvements to Data Center Replication, including a disk-based sender store, new start/stop and pause/resume semantics, replication events, and JMX management.
hidden: true
---

# GridGain 8.5.10 Release Notes

## What's New in This Release

### Introduction

This release introduces a number of substantial improvements to the [Data Center Replication](https://www.gridgain.com/docs/latest/administrators-guide/data-center-replication/introduction) feature and multiple bugfixes.

### Data Center Replication Improvements

#### Changes In Behavior

- The default implementation of the sender storage has changed from an in-memory store to a disk-based one. All updates in the master cluster are now stored on disk on the sender nodes before they are transmitted to the remote cluster. The directory on the file system where data updates are stored can be configured using the `DrSenderFsStore.directoryPath` property. The default value points to a directory inside the node's working directory. However, we recommend that you configure the directory explicitly.

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
              <!-- DR storage -->
              <property name="store">
                  <bean class="org.gridgain.grid.dr.store.fs.DrSenderFsStore">
                      <property name="directoryPath" value="/path/to/store"/>
                  </bean>
              </property>
              <!-- The ID of the remote cluster -->
              <property name="dataCenterId" value="2"/>
              <!-- Addresses of the remote cluster's receiver nodes -->
              <property name="receiverAddresses">
                  <list>
                      <value>172.25.4.200:50001</value>
                  </list>
              </property>
          </bean>
      </property>
  </bean>
  ```

- When the sender store gets full or becomes corrupted, the replication process will stop. You will have to start it manually and do a full state transfer after addressing the problem that caused the issue. Refer to the [Managing and Monitoring Replication](#managing-and-monitoring-replication) section.

- The `GridDr.pause()`/`GridDr.resume()` methods were deprecated and replaced with `GridDr.stopReplication()`/`GridDr.startReplication()`.

  The `stopReplication()` method terminates the replication process: cache updates will stop being processed. The `startReplication()` method resumes the replication process, i. e. cache updates will start to be processed again. If during the break the data in the cache has changed, you will need to do a full state transfer.

  {% hint style="info" %}
  The corresponding methods available through the [JMX beans](#managing-and-monitoring-replication) were renamed as well.
  {% endhint %}

- Added capability to pause/resume the replication process on the sender nodes. These operations can be performed via the JMX beans.

  {% hint style="danger" %}
  Do not confuse the pause/resume operations with the `GridDr.pause()`/`GridDr.resume()` methods, which have been deprecated.
  {% endhint %}

  Unlike the `GridDr.stopReplication()` methods, the pause operation will not terminate the process; instead, the sender node where the method is called will stop sending the updates to the remote cluster. The updates will continue to be processed and will be accumulated in the sender storage on that node. To resume the process of sending the updates to the remote cluster, perform the resume operation on the sender node.

  Refer to the [Managing and Monitoring Replication](#managing-and-monitoring-replication) section for the information on how you can pause/resume replication using JMX beans.

  {% hint style="warning" %}
  If you want to pause replication, you will have to pause and resume it on every sender node.
  {% endhint %}

- Added adaptive throttling feature that allows for adjusting the data transfer rate between data nodes and sender nodes, and between sender nodes and receiver nodes depending on the workload.

#### Managing and Monitoring Replication

This release introduces a number of changes in the JMX beans to support management operations and monitoring.

The following JMX Bean provides information about the replication process of a specific cache. The bean can be obtained on any node that hosts the cache.

**MBean's ObjectName:**

`group=**[cache name]**,name="Cache data replication"`

**Attributes:**

| Attribute | Type | Description | Scope |
|---|---|---|---|
| DrSenderGroup | String | The name of the sender group. | Global |
| DrStatus | String | The status of the replication process for this cache. | Global |
| DrQueuedKeysCount | int | The number of entries that are waiting to be sent to the sender node. | Node |
| DrSenderHubsCount | int | The number of sender nodes available for the cache. | Global |

**Operations:**

| Operation | Description |
|---|---|
| start | Start the replication process for this cache. |
| stop | Stop the replication process for this cache. |
| transferTo (id) | Perform a full state transfer of the content of this cache to the given remote cluster ID. |

The following MBean can be obtained on a sender node and allows you to pause/resume the replication process on that node.

**MBean's ObjectName:**

`group="Data Center Replication",name="Sender Hub"`

**Operations:**

| Operation | Description |
|---|---|
| pause (id) | Pause replication for the given remote cluster ID. This operation will stop sending updated to the remote cluster. The updates will be stored in the sender storage on that node until the replication is resumed. |
| pause | Pause replication for all remote clusters. |
| resume (id) | Resume replication for the given remote cluster ID. |
| resume | Resume replication for all remote clusters. |

#### Events

A number of event types related to data replication were added. The events are described in the following table.

| Event Type | Event Description | Where Event Is Fired |
|---|---|---|
| EVT_DR_REMOTE_DC_NODE_CONNECTED | A sender node connects to the node in the replica cluster. | The sender node. |
| EVT_DR_REMOTE_DC_NODE_DISCONNECTED | A sender node loses connection to the node in the remote cluster. The sender will try to connect to another receiver node if more than one are configured. If no receiver is available, the sender will try to reconnect after the period defined in the `DrSenderConfiguration.reconnectOnFailureTimeout` property. | The sender node. |
| EVT_DR_CACHE_REPLICATION_STOPPED | Replication of a specific cache is stopped due to any reason. A full state transfer is required before resuming the replication process. | All nodes that host the primary partitions of the cache. |
| EVT_DR_CACHE_REPLICATION_STARTED | Replication of a specific cache is started. | All nodes that host the primary partitions of the cache. |
| EVT_DR_CACHE_FST_STARTED | A full state transfer for a specific cache is started. | All nodes that host the primary partitions of the cache. |
| EVT_DR_CACHE_FST_FAILED | A full state transfer for a specific cache fails. | All nodes that host the primary partitions of the cache. |
| EVT_DR_STORE_OVERFLOW | A sender node cannot store entries to the sender storage because the storage is full. Manual restart and a full state transfer may be required after the issue is fixed. | The sender node. |
| EVT_DR_DC_REPLICATION_RESUMED | Replication to a specific cluster is resumed on a sender node. | The sender node. |

To listen to replication events, use the following code snippet:

```java
IgniteConfiguration cfg = new IgniteConfiguration();

// Enable the event
cfg.setIncludeEventTypes(org.gridgain.grid.events.EventType.EVT_DR_CACHE_REPLICATION_STOPPED);

// Enable data replication
cfg.setPluginConfigurations(new GridGainConfiguration().setDataCenterId(new Integer(1).byteValue()));

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

#### Enabling Replication for Existing Caches

If you have caches that had been created before you configured replication, there is no way to add data replication parameters to those caches, because cache configuration cannot be changed dynamically. To overcome this limitation, we introduced the `GG_DR_FORCE_DC_ID` system property.

If you restart the cluster with this property enabled, all caches that do not have data replication parameters will acquire the default replication configuration and will be replicated via the [default sender group](https://www.gridgain.com/docs/latest/administrators-guide/data-center-replication/configuring-replication#sender-nodes) (named "<default>").

The property must be set to the cluster ID of the current master cluster (the value of `GridGainConfiguration.dataCenterId`).

{% hint style="warning" %}
You must perform a full state transfer for all the caches that you want to replicate.
{% endhint %}

All caches created without data replication configuration in the master cluster with this property enabled, will automatically obtain the default replication configuration and will be replicated through the default sender group.

If you remove the `GG_DR_FORCE_DC_ID` property and restart the cluster, the caches without data replication configuration will stop being replicated.

{% hint style="info" %}
The property must be added to the startup parameters of all nodes in the cluster, including the client nodes. Otherwise, the client nodes won't be able to join the cluster.
{% endhint %}

### Removed/Deprecated

The `GridDr.pause()` and `GridDr.resume()` methods in the `GridDr` interface have been deprecated. Use `GridDr.stopReplication()`/`GridDr.startReplication()` methods instead.

## Installation and Upgrade Information

### Compatibility with Client Nodes Version 8.4.x

There is a known issue with running server nodes version 8.5.10 and client nodes version 8.4.x in one cluster. We strongly recommend that you upgrade your client nodes to version 8.5.10 first and then upgrade server nodes in a rolling upgrade fashion. If this is not possible, then consider the workaround below:

- Enable [persistence in the default data region](https://www.gridgain.com/docs/latest/developers-guide/persistence/native-persistence#configuration) in the client nodes' configuration. Perform this procedure for every client application.
- Upgrade server nodes to version 8.5.10 in a rolling upgrade fashion.

### Upgrade Procedure

If you are not using Data Center Replication and want to upgrade without enabling Data Center Replication, refer to the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades.

If you are upgrading from a cluster with Data Center Replication already configured, a regular rolling upgrade should be enough.

If you want to enable Data Center Replication during the upgrade, below is a modified rolling upgrade procedure designed to achieve this goal. You will need to use the `GG_DR_FORCE_DC_ID` system property described in the [Enabling Replication for Existing Caches](#enabling-replication-for-existing-caches) section. Before attempting to upgrade your master cluster, decide which node will be used as sender nodes and receivers nodes. Refer to the [official documentation](https://www.gridgain.com/docs/latest/administrators-guide/data-center-replication/configuring-replication) on data center replication.

1. Start a replica cluster on version 8.5.10 with Data Center Replication configured.
2. Stop one server node in the master cluster.
3. Upgrade the node to version 8.5.10 and configure it either as a sender node or receiver node. Add the `GG_DR_FORCE_DC_ID=<your cluster id>` set to the ID of the master cluster (`GridGainConfiguration.dataCenterId`).
4. Repeat steps 2 and 3 for all remaining server nodes in the master cluster.

## Known Issues

| Issue ID | Description |
|---|---|
| GG-24425 | Deactivation of the cluster can lead to an exception being thrown on the sender nodes, which will cause the sender nodes to hang. If this happens, you need to restart the sender nodes. To avoid this, stop the sender nodes first, if possible, before deactivating the cluster. |
| GG-24212 | Log messages about starting the replication process can be misleading. When executing a stop command, you may see the following message: "Data center replication executes a stop task".<br><br>To monitor the success of start and stop operations, look for the following messages:<br><br>- "Data center replication is stopped ..."<br>- "Data center replication is started ..." |
| GG-24136 | The commands issued using `control.sh` script can throw exceptions on the client nodes that run GridGain prior to version 8.5.10.<br><br>Possible workarounds include:<br><br>- Use the [JMX Beans](#managing-and-monitoring-replication) to manage replication.<br>- Use the Java API to manage replication.<br>- Update the clients to GridGain version 8.5.10. |
| GG-23095 | Using the now deprecated methods `pause()` and `resume()` can lead to data not being replicated. Use the `startReplication()`/`stopReplication()` methods instead. |
| GG-24311 | Creating index for the columns that were changed using ALTER TABLE DROP/ADD COLUMN commands can lead to B+Tree corruption. |

## Fixed Issues

### GridGain Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-24065 | Team / SE Common | Replaced AtomicLong[] with AtomicLongArray in pages list to reduce heap pressure |

### GridGain Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-23742 | DR | Fixed DR overflow events for REMOVE_OLDEST mode. |
| GG-23533 | Team / Transactions & PME Common | Added DR_ACK_MISSING_CACHES to allow DR make progress in case there are errors on receiver due to missing caches. |
| GG-23342 | DR | Added metrics to show DR sender/receiver pending queues size. |
| GG-23300 | DR | Change default DrStore mode to STOP. |
| GG-23238 | Control.(sh\|bat) | Added data center replication API to the control utility. |
| GG-23209 | DR | Change default DrStore mode to STOP. |
| GG-23044 | DR | DR: Add correctly named methods for DR start\stop. |
| GG-23041 | DR | DR: Fix broken DR pause\resume semantic. |
| GG-23036 | DR | Prevent possible deadlock in DR during node left and cache stop in the same moment |
| GG-23034 | DR, WC | Web Console: Added support for alerts on DR events. |
| GG-23020 | DR, SQL | Fixed data center replication for caches created via DDL. |
| GG-23007 | DR | Improve logging for the Data Center Replication component. |
| GG-22990 | DR | Adaptive DR throttling added. |
| GG-22983 | DR | Bugfix: stop replication for cache that doesn't exists at the receiver DC. |
| GG-22979 | DR | Data Replication now uses file-system based implementation of Sender Store by default. It has default work directory, but it is recommended to configure it explicitly on production environments. |
| GG-22978 | DR | Stop DR replication in case sender hub with in memory store went down. |
| GG-22977 | DR | New method named 'resetState' has been added to DrSender interface. It resets all internal state of sender hub including clearing store and internal queues. |
| GG-22885 | DR | Deprecated and ignored GridGainCacheConfiguration.drReceiverEnabled flag due to invalid behavior |
| GG-22884 | DR | Added events for DR. |
| GG-22883 | DR | Added DR full state transfer operation to cache MBean. |
| GG-22880 | DR | Added ability to change full state transfer throttle per node at runtime. |
| GG-22879 | DR | DR: delete files with successfully sent (ACK is received) data. |

## Related Information

### We Value Your Feedback

The GridGain documentation team is focused on constantly improving the product documentation. Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://www.gridgain.com/docs/latest/getting-started/what-is-gridgain) for more information.
