---
description: >-
  Reference of GridGain event types, describing when and where each event is
  generated and how to use them.
---

# Events

This page describes different event types, when and where they are generated, and how you can use them.

You can always find the most complete and up to date list of events in the javadocs: [Ignite events](https://www.gridgain.com/sdk/8.10/javadoc/org/apache/ignite/events/EventType.html) and [GridGain Enterprise events](https://www.gridgain.com/sdk/8.10/javadoc/org/gridgain/grid/events/EventType.html).

## General Information

All events implement the `Event` interface.
You may want to cast each event to the specific class to get extended information about the action the event was triggered by.
For example, the 'cache update' action triggers an event that is an instance of the `CacheEvent` class, which contains the information about the data that was modified, the ID of the subject that triggered the event, etc.

All events contain information about the node where the event was generated.
For example, when you execute an `IgniteClosure` job, the `EVT_JOB_STARTED` and `EVT_JOB_FINISHED` events contain the information about the node where the closure was executed.

```java
IgniteEvents events = ignite.events();

UUID uuid = events.remoteListen(new IgniteBiPredicate<UUID, JobEvent>() {
    @Override
    public boolean apply(UUID uuid, JobEvent e) {

        System.out.println("nodeID = " + e.node().id() + ", addresses=" + e.node().addresses());

        return true; //continue listening
    }
}, null, EventType.EVT_JOB_FINISHED);

```

{% hint style="warning" %}
**Event Ordering**

The order of events in the event listener is not guaranteed to be the same as the order in which they were generated.
{% endhint %}

### SubjectID

Some events contain the `subjectID` field, which represents the ID of the entity that initiated the action:

- When the action is initiated by a server or client node, the `subjectID` is the ID of that node.
- When the action is done by a thin client, JDBC/ODBC/REST client, the `subjectID` is generated when the client connects to the cluster and remains the same as long as the client is connected to the cluster.

Check the specific event class to learn if the `subjectID` field is present.

If you use GridGain Enterprise or Ultimate edition and enable authentication, `subjectID` allows you to get the user name that the node or client used to connect to the cluster.
This capability can be used for [auditing purposes](../../security/auditing-events.md).

## Cluster Activation Events

Cluster activation events are instances of the [ClusterActivationEvent](https://www.gridgain.com/sdk/8.10/javadoc/org/apache/ignite/events/ClusterActivationEvent.html) class.
Cluster activation events are generated when the cluster is activated or deactivated. They contain the list of baseline nodes at the moment of the event.

|Event Type | Event Description | Where Event Is Fired|
|---|---|---|
|EVT_CLUSTER_ACTIVATED | The cluster is activated (including when auto-activated). | All cluster nodes.|
|EVT_CLUSTER_DEACTIVATED | The cluster is deactivated. | All cluster nodes.|

## Baseline Autoadjustment Events

Baseline autoadjustment events are instances of the [BaselineConfigurationChangedEvent](https://www.gridgain.com/sdk/8.10/javadoc/org/apache/ignite/events/BaselineConfigurationChangedEvent.html) class.
They are generated when the baseline autoadjustment configuration changes. Each event carries the auto-adjust "enabled" flag (`isAutoAdjustEnabled()`) and the timeout in milliseconds (`autoAdjustTimeout()`) for the affected scale direction.

|Event Type | Event Description | Where Event Is Fired|
|---|---|---|
|EVT_BASELINE_SCALE_UP_AUTO_ADJUST_ENABLED_CHANGED | The scale-up autoadjustment "enabled" flag is changed by a user request. | All cluster nodes.|
|EVT_BASELINE_SCALE_UP_AUTO_ADJUST_AWAITING_TIME_CHANGED | The scale-up autoadjustment timeout is changed by a user request. | All cluster nodes.|
|EVT_BASELINE_SCALE_DOWN_AUTO_ADJUST_ENABLED_CHANGED | The scale-down autoadjustment "enabled" flag is changed by a user request. | All cluster nodes.|
|EVT_BASELINE_SCALE_DOWN_AUTO_ADJUST_AWAITING_TIME_CHANGED | The scale-down autoadjustment timeout is changed by a user request. | All cluster nodes.|

## Cache Lifecycle Events

Cache Lifecycle events are instances of the [CacheEvent](https://www.gridgain.com/sdk/8.10/javadoc/org/apache/ignite/events/CacheEvent.html) class.
Each cache lifecycle event is associated with a specific cache and has a field that contains the name of the cache.

| Event Type | Event Description | Where Event Is Fired|
|---|---|---|
| EVT_CACHE_STARTED | A cache is started on a specific node.<br>Each server node holds an internal instance of a cache.<br>This event is fired when the instance is created, which includes the following actions:<br><br>• A cluster with existing caches is activated. The event is generated for every cache on all server nodes where the cache is configured.<br>• A server node joins the cluster with existing caches (the caches are started on that node).<br>• When you create a new cache dynamically by calling `Ignite.getOrCreateCache(...)` or similar methods. The event is fired on all nodes that host the cache.<br>• When you obtain an instance of a cache on a client node.<br>• When you create a cache via the [CREATE TABLE](../../reference/sql/ddl.md#create-table) command. | All nodes where the cache is started.|
| EVT_CACHE_STOPPED | This event happens when a cache is stopped, which includes the following actions:<br><br>• The cluster is deactivated. All caches on all server nodes are stopped.<br>• `IgniteCache.close()` is called. The event is triggered on the node where the method is called.<br>• A SQL table is dropped.<br>• If you call `cache = Ignite.getOrCreateCache(...)` and then call `Ignite.close()`, the `cache` is also closed on that node. | All nodes where the cache is stopped.|
| EVT_CACHE_NODES_LEFT | All nodes that host a specific cache have left the cluster. This can happen when a cache is deployed on a subset of server nodes or when all server nodes leave the cluster and only client nodes remain. | All remaining nodes.|

## Cache Events

Cache events are instances of the [CacheEvent](https://www.gridgain.com/sdk/8.10/javadoc/org/apache/ignite/events/CacheEvent.html) class and
represent the operations on cache objects, such as 'get', 'put', 'remove', 'lock', etc.

Each event contains the information about the cache, the key that is accessed by the operation, the value before and after the operation (if applicable), etc.

Cache events are also generated when you use DML commands.

| Event Type | Event Description | Where Event Is Fired|
|---|---|---|
| EVT_CACHE_OBJECT_PUT | An object is put to a cache. This event is fired for every invocation of `IgniteCache.put()`. The bulk operations, such as `putAll(...)`, produce multiple events of this type. | The primary and backup nodes for the entry.|
| EVT_CACHE_OBJECT_READ | An object is read from a cache.<br>This event is not emitted when you use [scan queries](../key-value-api/using-scan-queries.md) (use [Cache Query Events](#cache-query-events) to monitor scan queries). | The node where read operation is executed.<br>It can be either the primary or backup node (the latter case is only possible when [reading from backups is enabled](../configuring-caches/configuration-overview.md)).<br>In transactional caches, the event can be generated on both the primary and backup nodes depending on the concurrency and isolation levels.|
| EVT_CACHE_OBJECT_REMOVED | An object is removed from a cache. | The primary and backup nodes for the entry.|
| EVT_CACHE_OBJECT_LOCKED | A lock is acquired on a specific key.<br>Locks can be acquired only on keys in transactional caches.<br>User actions that acquire a lock include the following cases:<br><br>• The user explicitly acquires a lock by calling `IgniteCache.lock()` or `IgniteCache.lockAll()`.<br>• A lock is acquired for every atomic (non-transactional) data modifying operation (put, update, remove). In this case, the event is triggered on both primary and backup nodes for the key.<br>• Locks are acquired on the keys accessed within a transaction (depending on the [concurrency and isolation levels](../transactions.md#concurrency-modes-and-isolation-levels)). | The primary or/and backup nodes for the entry depending on the [concurrency and isolation levels](../transactions.md#concurrency-modes-and-isolation-levels).|
| EVT_CACHE_OBJECT_UNLOCKED | A lock on a key is released. | The primary node for the entry.|
| EVT_CACHE_OBJECT_EXPIRED | The event is fired when a cache entry expires. This happens only if an [expiry policy](../configuring-caches/expiry-policies.md) is configured.  | The primary and backup nodes for the entry.|
| EVT_CACHE_ENTRY_CREATED | This event is triggered when GridGain creates an internal entry for working with a specific object from a cache. We don't recommend using this event. If you want to monitor cache put operations, the `EVT_CACHE_OBJECT_PUT` event should be enough for most cases. | The primary and backup nodes for the entry.|
| EVT_CACHE_ENTRY_DESTROYED | This event is triggered when GridGain destroys an internal entry that was created for working with a specific object from a cache.<br>We don't recommend using it.<br>Destroying the internal entry does not remove any data from the cache.<br>If you want to monitor cache remove operations, use the `EVT_CACHE_OBJECT_REMOVED` event. | The primary and backup nodes for the entry.|

## Cache Query Events

There are two types of events that are related to cache queries:

- Cache query object read events, which are instances of the [CacheQueryReadEvent](https://www.gridgain.com/sdk/8.10/javadoc/org/apache/ignite/events/CacheQueryReadEvent.html) class.
- Cache query executed events, which are instances of the [CacheQueryExecutedEvent](https://www.gridgain.com/sdk/8.10/javadoc/org/apache/ignite/events/CacheQueryExecutedEvent.html) class.

| Event Type | Event Description | Where Event Is Fired|
|---|---|---|
| EVT_CACHE_QUERY_OBJECT_READ | An object is read as part of a query execution. This event is generated for every object that matches the [query filter](../key-value-api/using-scan-queries.md#executing-scan-queries). | The primary node of the object that is read.|
| EVT_CACHE_QUERY_EXECUTED  |  This event is generated when a query is executed. | All server nodes that host the cache.|

## Class and Task Deployment Events

Deployment events are instances of the [DeploymentEvent](https://www.gridgain.com/sdk/8.10/javadoc/org/apache/ignite/events/DeploymentEvent.html) class.

| Event Type | Event Description | Where Event Is Fired|
|---|---|---|
| EVT_CLASS_DEPLOYED | A class (non-task) is deployed on a specific node. | The node where the class is deployed.|
| EVT_CLASS_UNDEPLOYED | A class is undeployed. | The node where the class is undeployed.|
| EVT_CLASS_DEPLOY_FAILED | Class deployment failed. |The node where the class is to be deployed.|
| EVT_TASK_DEPLOYED | A task class is deployed on a specific node. | The node where the class is deployed.|
| EVT_TASK_UNDEPLOYED | A task class is undeployed on a specific node.|The node where the class is undeployed.|
| EVT_TASK_DEPLOY_FAILED | Class deployment failed.|The node where the class is to be deployed.|

## Discovery Events

Discovery events occur when nodes (both servers and clients) join or leave the cluster, including cases when nodes leave due to a failure.

Discovery events are instances of the [DiscoveryEvent](https://www.gridgain.com/sdk/8.10/javadoc/org/apache/ignite/events/DiscoveryEvent.html) class.

| Event Type | Event Description | Where Event Is Fired|
|---|---|---|
| EVT_NODE_JOINED | A node joins the cluster. | All nodes in the cluster (other than the one that joined).|
| EVT_NODE_LEFT | A node leaves the cluster. |All remaining nodes in the cluster.|
| EVT_NODE_FAILED | The cluster detects that a node left the cluster in a non-graceful way. | All remaining nodes in the cluster.|
| EVT_NODE_SEGMENTED | This happens on a node that decides that it was segmented. | The node that is segmented.|
| EVT_CLIENT_NODE_DISCONNECTED | A client node loses connection to the cluster.  | The client node that disconnected from the cluster.|
| EVT_CLIENT_NODE_RECONNECTED | A client node reconnects to the cluster.| The client node that reconnected to the cluster.|

## Task Execution Events

Task execution events are associated with different stages of [task execution](../distributed-computing/map-reduce.md).
They are also generated when you execute [simple closures](../distributed-computing/distributed-computing.md) because internally a closure is treated as a task that produces a single job.

Task Execution events are instances of the [TaskEvent](https://www.gridgain.com/sdk/8.10/javadoc/org/apache/ignite/events/TaskEvent.html) class.

| Event Type | Event Description | Where Event Is Fired|
|---|---|---|
| EVT_TASK_STARTED | A task is started. `IgniteCompute.execute()` or other method is called   | The node that initiates the task.|
| EVT_TASK_REDUCED | This event represents the 'reduce' stage of the task execution flow.  | The node where the task was started.|
| EVT_TASK_FINISHED | The execution of the task finishes. | The node where the task was started.|
| EVT_TASK_FAILED | The task failed  | The node where the task was started.|
| EVT_TASK_TIMEDOUT |  The execution of the task timed out. This can happen when `Ignite.compute().withTimeout(...)` to execute tasks. When a task times out, it cancels all jobs that are being executed. It also generates the `EVT_TASK_FAILED` event.| The node where the task was started.|
| EVT_TASK_SESSION_ATTR_SET | A job sets an attribute in the [session](../distributed-computing/map-reduce.md#distributed-task-session). | The node where the job is executed.|

Job Execution events are instances of the [JobEvent](https://www.gridgain.com/sdk/8.10/javadoc/org/apache/ignite/events/JobEvent.html) class.
The job execution events are generated at different stages of job execution and are associated with particular instances of the job.
The event contains information about the task that produced the job (task name, task class, etc.).

| Event Type | Event Description | Where Event Is Fired|
|---|---|---|
| EVT_JOB_MAPPED | A job is mapped to a specific node. Mapping happens on the node where the task is started. This event is generated for every job produced in the "map" stage. | The node that started the task.|
| EVT_JOB_QUEUED | The job is added to the queue on the node to which it was mapped. | The node where the job is scheduled for execution.|
| EVT_JOB_STARTED | Execution of the job started.| The node where the job is executed.|
| EVT_JOB_FINISHED | Execution of the job finished. This also includes cases when the job is cancelled.| The node where the job is executed.|
| EVT_JOB_RESULTED | The job returned a result to the node from which it was sent. | The node where the task was started.|
| EVT_JOB_FAILED | Execution of a job fails. If the job failover strategy is configured (default), this event is accompanied by the `EVT_JOB_FAILED_OVER` event. | The node where the job is executed.|
| EVT_JOB_FAILED_OVER | The job was failed over to another node. | The node that started the task.|
| EVT_JOB_TIMEDOUT | The job timed out. ||
| EVT_JOB_REJECTED | The job is rejected. The job can be rejected if a [collision spi](../distributed-computing/job-scheduling.md) is configured. | The node where the job is rejected.|
| EVT_JOB_CANCELLED | The job was cancelled. | The node where the job is being executed.|

## Cache Rebalancing Events

Cache Rebalancing events (all except for `EVT_CACHE_REBALANCE_OBJECT_LOADED` and `EVT_CACHE_REBALANCE_OBJECT_UNLOADED`) are instances of the [CacheRebalancingEvent](https://www.gridgain.com/sdk/8.10/javadoc/org/apache/ignite/events/CacheRebalancingEvent.html) class.

Rebalancing occurs on a per cache basis; therefore, each rebalancing event corresponds to a specific cache.
The event contains the name of the cache.

The process of moving a single cache partition from Node A to Node B consists of the following steps:

1. Node A supplies a partition (REBALANCE_PART_SUPPLIED). The objects from the partition start to move to node B.
2. Node B receives the partition data (REBALANCE_PART_LOADED).
3. Node A removes the partition from its storage (REBALANCE_PART_UNLOADED).

| Event Type | Event Description | Where Event Is Fired|
|---|---|---|
| EVT_CACHE_REBALANCE_STARTED | The rebalancing of a cache starts. | All nodes that host the cache.|
| EVT_CACHE_REBALANCE_STOPPED | The rebalancing of a cache stops. | All nodes that host the cache.|
| EVT_CACHE_REBALANCE_PART_LOADED | A cache's partition is loaded on the new node. This event is fired for every partition that participates in the cache rebalancing.| The node where the partition is loaded.|
| EVT_CACHE_REBALANCE_PART_UNLOADED |A cache's partition is removed from the node after it has been loaded to its new destination. | The node where the partition was held before the rebalancing process started.|
| EVT_CACHE_REBALANCE_OBJECT_LOADED | An object is moved to a new node as part of cache rebalancing. | The node where the object is loaded.|
| EVT_CACHE_REBALANCE_OBJECT_UNLOADED | An object is removed from a node after it has been moved to a new node.| The node from which the object is removed.|
| EVT_CACHE_REBALANCE_PART_DATA_LOST | A partition that is to be rebalanced is lost, for example, due to a node failure. ||
| EVT_CACHE_REBALANCE_PART_SUPPLIED | A node supplies a cache partition as part of the rebalancing process. | The node that owns the partition.|

## Transaction Events

Transaction events are instances of the [TransactionStateChangedEvent](https://www.gridgain.com/sdk/8.10/javadoc/org/apache/ignite/events/TransactionStateChangedEvent.html) class.
They allow you to get notification about different stages of transaction execution. Each event contains the `Transaction` object this event is associated with.

| Event Type | Event Description | Where Event Is Fired|
|---|---|---|
| EVT_TX_STARTED | A transaction is started. Note that in transactional caches, each atomic operation executed outside a transaction is considered a transaction with a single operation. | The node where the transaction was started.|
| EVT_TX_COMMITTED | A transaction is committed. |  The node where the transaction was started.|
| EVT_TX_ROLLED_BACK | A transaction is rolled back. |The node where the transaction was executed.|
| EVT_TX_SUSPENDED |  A transaction is suspended.|The node where the transaction was started.|
| EVT_TX_RESUMED | A transaction is resumed. |The node where the transaction was started.|

## SQL Query Finish Events

These events are instances of the [QueryExecutionFinishedEvent](https://www.gridgain.com/sdk/8.10/javadoc/org/apache/ignite/events/QueryExecutionFinishedEvent.html) class.
They allow you to get notification when query execution finishes, regardless of query success or failure.

| Event Type | Event Description | Where Event Is Fired|
|---|---|---|
| EVT_QUERY_FINISHED | This event is generated when query execution finishes. | The node where the query was executed.|

## Partition State Validation Events

Partition state validation events are instances of the [PartitionsStateValidationEvent](https://www.gridgain.com/sdk/8.10/javadoc/org/apache/ignite/events/PartitionsStateValidationEvent.html) class.
They are generated when the cluster coordinator validates partition states during a partition map exchange (PME) and report whether partition states are consistent across the cluster.

| Event Type | Event Description | Where Event Is Fired|
|---|---|---|
| EVT_PARTITIONS_STATE_VALIDATION_SUCCEEDED | Partition state validation completed successfully and partition states are consistent across the cluster. | The coordinator node only.|
| EVT_PARTITIONS_STATE_VALIDATION_FAILED | Partition state validation failed because one or more partitions have inconsistent states. The event reports the affected caches and partitions. | The coordinator node only.|

## License Events

{% hint style="warning" %}
Available only in GridGain Enterprise and Ultimate Editions.
{% endhint %}

License events are instances of the [LicenseEvent](https://www.gridgain.com/sdk/8.10/javadoc/org/gridgain/grid/events/LicenseEvent.html) class.

| Event Type | Event Description | Where Event Is Fired|
|---|---|---|
| EVT_LIC_CLEARED | This event is generated when license violation has been removed. | All cluster nodes.|
| EVT_LIC_VIOLATION | License restrictions are violated. | All cluster nodes.|
| EVT_LIC_GRACE_EXPIRED | The grace period is coming to an end. | All cluster nodes.|

## Authentication Events

{% hint style="warning" %}
Available only in GridGain Enterprise and Ultimate Editions.
{% endhint %}

Authentication events are generated when a user tries to connect to the cluster protected by authentication.
There are two types of authentication events, each type indicating whether the user was authenticated successfully or not.

Authentication events are instances of the [AuthenticationEvent](https://www.gridgain.com/sdk/8.10/javadoc/org/gridgain/grid/events/AuthenticationEvent.html) class.
Each event contains the type of the user (`AuthenticationEvent.subjectType()`), which can be either a remote node or a remote client, and the user name that was used to log in.

| Event Type | Event Description | Where Event Is Fired|
|---|---|---|
| EVT_AUTHENTICATION_SUCCEEDED | A user is successfully authenticated in the cluster. | The node to which the entity is connected and where the authentication happened.|
| EVT_AUTHENTICATION_FAILED | User authentication failed. | The node where the authentication happened.|

## Authorization Events

{% hint style="warning" %}
Available only in GridGain Enterprise and Ultimate Editions.
{% endhint %}

Authorization events represent authorization checks performed when a user tries to execute an operation.
The check either succeeds or fails.

Authorization events are instances of the [AuthorizationEvent](https://www.gridgain.com/sdk/8.10/javadoc/org/gridgain/grid/events/AuthorizationEvent.html) class.
Each event contains information about the user and the operation that was performed (`AuthorizationEvent.operation()`).
Refer to the [authorization and permissions](../../security/authorization-permissions.md) page for the list of operations that could require authorization.

| Event Type | Event Description | Where Event Is Fired|
|---|---|---|
| EVT_AUTHORIZATION_SUCCEEDED | A user is successfully authorized to execute an operation. The event contains the type of operation.| The node where the operation is performed.|
| EVT_AUTHORIZATION_FAILED | A user is denied permission to execute an operation. | The node where the operation is attempted.|

## Data Replication Events

Refer to the [Data Replication documentation](../../gridgain8-management/data-center-replication/managing-and-monitoring.md#data-replication-events).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
