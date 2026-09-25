---
description: >-
  How to configure GridGain data center replication — cluster IDs, sender and
  receiver nodes, cache replication, conflict resolution, and related tuning properties.
---

# Configuring Replication

This chapter explains how to configure your GridGain clusters for data replication.

{% hint style="info" %}
A number of these operations can also be performed by using the [control script](../../reference/cli-tool/README.md#data-center-replication).
{% endhint %}

## Enabling Replication

To enable replication, you need to perform the following steps:

### 1. Set Unique Cluster ID

Each cluster participating in the replication process must have a unique ID.
The ID is specified in the configuration of each node of the cluster and must be the same within each cluster.

The following configuration example shows how to set the cluster ID.

{% tabs %}
{% tab title="XML" %}
```xml

```
{% endtab %}
{% tab title="Java" %}
```java

```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    PluginConfigurations = new[]
    {
         new GridGainPluginConfiguration()
         {
             DataCenterId = 1
         }
     }
};

var ignite = Ignition.Start(cfg);
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

Make sure to set the cluster ID on every node in the master cluster. Similarly, set a different cluster ID on every node of the replica cluster.

### 2. Configure Connection Between Clusters

To connect the master cluster to the replica, configure a few sender nodes in the master cluster and the same number of receiver nodes in the replica cluster.
A sender group is a logical group of nodes identified by a name, in which each node is configured to connect to the nodes in the replica.
To configure a sender group, specify the name of the group in the configuration of each node you want to be a part of the group.

We recommend that you use client nodes as senders and receivers.

#### Sender Nodes

A sender node is a node that can connect to the replica cluster and send data to it.
Configure each node that you want to be a part of a specific sender group.
Basic sender node configuration involves two properties:

- The name of the sender group this node belongs to.
This property is optional.
If it's not specified, the node will be included in the default group, named "<default>", which includes all nodes configured as sender nodes.
- The connection configuration that establishes a connection to the replica cluster. You can have multiple connection configurations, each connecting to different nodes.

The connection configuration parameters are defined in a `DrSenderConnectionConfiguration` object.
The following example illustrates how to configure a node to be a part of the sender group called "group1" and connect to two remote nodes.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration" id="ignite.cfg">
    <!-- we recommend that sender nodes be clients -->
    <property name="clientMode" value="true"/>
    <property name="pluginConfigurations">
        <list>
            <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
                <!-- Unique ID of this cluster -->
                <property name="dataCenterId" value="1"/>
                <property name="drSenderConfiguration">
                    <bean class="org.gridgain.grid.configuration.DrSenderConfiguration">
                        <property name="sslContextFactory">
                            <bean class="org.apache.ignite.ssl.SslContextFactory">
                                <property name="keyStoreType" value="PKCS12"/>
                                <property name="keyStoreFilePath" value="/path/dr/server.p12"/>
                                <property name="keyStorePassword" value="123456"/>
                                <property name="trustStoreType" value="PKCS12"/>
                                <property name="trustStoreFilePath" value="/home/abudnikov/gridgain/configs/dr/trust.p12"/>
                                <property name="trustStorePassword" value="123456"/>
                            </bean>
                        </property>
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
                </property>
            </bean>
        </list>
    </property>
</bean>
```
{% endtab %}
{% tab title="Java" %}
```java

```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    PluginConfigurations = new[]
    {
        new GridGainPluginConfiguration
        {
            DataCenterId = 1,
            DrSenderConfiguration = new DrSenderConfiguration
            {
                SenderGroups = new[] { "group1" },
                ConnectionConfiguration = new[]
                {
                    new DrSenderConnectionConfiguration
                    {
                        DataCenterId = 2,
                        // the addresses of the remote data center's nodes that will receive data updates
                        ReceiverAddresses = new[] { "172.25.4.200:50001" }
                    }
                }
            }
        }
    }
};

var ignite = Ignition.Start(cfg);
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

In the example above, the sender node will connect to one node in the replica cluster.
For redundancy purposes, you can specify the addresses of multiple nodes.
The sender node will try to load balance between all of them.

{% tabs %}
{% tab title="XML" %}
```xml
 <property name="connectionConfiguration">
    <bean class="org.gridgain.grid.dr.DrSenderConnectionConfiguration">

        <!-- the ID of the replica cluster -->
        <property name="dataCenterId" value="2"/>

        <!-- Addresses of the replica cluster's nodes that will receive data -->
         <property name="receiverAddresses">
            <list>
                <value>172.25.4.200:50001</value>
                <value>172.25.4.201:50001</value>
            </list>
        </property>
    </bean>
</property>
```
{% endtab %}
{% tab title="Java" %}
```java
DrSenderConfiguration drSenderCfg = new DrSenderConfiguration();
drSenderCfg.setSenderGroups("group1");

// the addresses of the remote replica cluster's nodes that will receive data updates 
drSenderCfg.setConnectionConfiguration(new DrSenderConnectionConfiguration().setDataCenterId((byte) 2)
        .setReceiverAddresses("172.25.4.200:50001", "172.25.4.201:50001"));

```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    PluginConfigurations = new[]
    {
        new GridGainPluginConfiguration
        {
            DataCenterId = 1,
            DrSenderConfiguration = new DrSenderConfiguration
            {
                SenderGroups = new[] { "group1" },
                ConnectionConfiguration = new[]
                {
                    new DrSenderConnectionConfiguration
                    {
                        DataCenterId = 2,
                        // the addresses of the remote data center's nodes that will receive data updates
                        ReceiverAddresses = new[] { "172.25.4.200:50001", "172.25.4.201:50001" }
                    }
                }
            }
        }
    }
};
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

The connection parameters that can be specified in the `DrSenderConnectionConfiguration` object include:

| Parameter | Description |
|---|---|
| `dataCenterId` | Replica cluster ID, must be a value between 1 and 31. |
| `receiverAddresses` | A list of endpoints in the replica cluster this node will connect to. The nodes in the replica must be configured to listen on the specified ports. See [Receiver Nodes](#receiver-nodes). |
| `localOutboundAddress` | The network interface to use for cross-cluster communication. |
| `loadBalancingMode` | The load balancing policy that is used to distribute batches across the nodes in the replica cluster if more than one address is configured. Possible values include:<br>- `DR_RANDOM` — Default. Random load balancing policy.<br>- `DR_ROUND_ROBIN` — Round-robin load balancing policy. |

#### Receiver Nodes

For each sender node in the master cluster, your replica cluster must have a node (or multiple nodes) that will receive data from that sender node. This node is called a _receiver node_.

To configure a node as a receiver, define the `drReceiverConfiguration` property of the `GridGainConfiguration` plugin. Below is an example of a receiver node configuration.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration" id="ignite.cfg">
    <!-- we recommend that receiver nodes be clients -->
    <property name="clientMode" value="true"/>

    <property name="pluginConfigurations">
        <list>
            <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
                <!-- Unique ID of this cluster -->
                <property name="dataCenterId" value="2"/>
                <!--
                Setting up receiver node specific parameters.
                -->
                <property name="drReceiverConfiguration">
                    <bean class="org.gridgain.grid.configuration.DrReceiverConfiguration">
                        <!-- TCP port receiver node of this cluster is bound to. -->
                        <property name="localInboundPort" value="50001"/>

                        <property name="messageQueueLimit" value="10000"/>
                    </bean>
                </property>
            </bean>
        </list>
    </property>
    <!-- other properties -->
</bean>
```
{% endtab %}
{% tab title="Java" %}
```java

```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    PluginConfigurations = new[]
    {
        new GridGainPluginConfiguration
        {
            DataCenterId = 1,
            DrReceiverConfiguration = new DrReceiverConfiguration
            {
                LocalInboundPort = 50001
            }
        }
    }
};

var ignite = Ignition.Start(cfg);
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

Below are some important parameters of the receiver node configuration:

| Parameter | Description |
|---|---|
| messageQueueLimit | The maximum number of batches in the queue on the receiver node that haven't been processed. If the queue is growing, it means that the receiver node gets more data than it can handle. When the limit is exceeded, the node will stop accepting new messages from the master cluster until the queue size drops below that value. The default value is 0, which means that the queue can grow indefinitely. We recommend you should set this parameter to 10,000 to avoid OutOfMemory errors on the receiver node. |

For the complete list of parameters, refer to the `org.gridgain.grid.configuration.DrReceiverConfiguration` javadoc.

#### Active-Active Mode

In the active-active mode, both clusters send data to each other.
It means that each cluster must have sender nodes and receiver nodes.
The sender nodes in cluster 1 will connect to the receivers in cluster 2, and the sender nodes in cluster 2 will connect to the receiver nodes in cluster 1.

You can configure the same node to be both a sender and a receiver by combining the configuration properties described in the two previous sections.

```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration" id="ignite.cfg">
    <!-- we recommend that sender nodes be clients -->
    <property name="clientMode" value="true"/>
    <property name="pluginConfigurations">
        <list>
            <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
                <!-- Unique ID of this cluster -->
                <property name="dataCenterId" value="1"/>
                <property name="drSenderConfiguration">
                    <bean class="org.gridgain.grid.configuration.DrSenderConfiguration">
                        <property name="sslContextFactory">
                            <bean class="org.apache.ignite.ssl.SslContextFactory">
                                <property name="keyStoreType" value="PKCS12"/>
                                <property name="keyStoreFilePath" value="/path/dr/server.p12"/>
                                <property name="keyStorePassword" value="123456"/>
                                <property name="trustStoreType" value="PKCS12"/>
                                <property name="trustStoreFilePath" value="/path/dr/trust.p12"/>
                                <property name="trustStorePassword" value="123456"/>
                            </bean>
                        </property>
                        <!-- this node is part of group1 -->
                        <property name="senderGroups">
                            <list>
                                <value>group1</value>
                            </list>
                        </property>
                        <!-- connection configuration -->
                        <property name="connectionConfiguration">
                            <bean class="org.gridgain.grid.dr.DrSenderConnectionConfiguration">
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
                </property>
                <!-- receiver node parameters -->
                <property name="drReceiverConfiguration">
                    <bean class="org.gridgain.grid.configuration.DrReceiverConfiguration">
                        <!-- TCP port receiver node of this cluster is bound to. -->
                        <property name="localInboundPort" value="50001"/>
                    </bean>
                </property>
            </bean>
        </list>
    </property>
</bean>
```

#### Encryption

There are two ways to encrypt communication between the master and replica clusters:

- [Enable SSL globally](../../security/ssl-tls.md).
- Enable SSL for data replication exclusively.

In this section, we'll explain the second method.

To enable SSL for data replication, you need to provide an `SslContextFactory` in both sender node and receiver node configurations.

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration" id="ignite.cfg">
    <!-- we recommend that sender nodes be clients -->
    <property name="clientMode" value="true"/>
    <property name="pluginConfigurations">
        <list>
            <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
                <!-- Unique ID of this cluster -->
                <property name="dataCenterId" value="1"/>
                <property name="drSenderConfiguration">
                    <bean class="org.gridgain.grid.configuration.DrSenderConfiguration">
                        <property name="sslContextFactory">
                            <bean class="org.apache.ignite.ssl.SslContextFactory">
                                <property name="keyStoreType" value="PKCS12"/>
                                <property name="keyStoreFilePath" value="/path/dr/server.p12"/>
                                <property name="keyStorePassword" value="123456"/>
                                <property name="trustStoreType" value="PKCS12"/>
                                <property name="trustStoreFilePath" value="/home/abudnikov/gridgain/configs/dr/trust.p12"/>
                                <property name="trustStorePassword" value="123456"/>
                            </bean>
                        </property>
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
                </property>
            </bean>
        </list>
    </property>
</bean>
```
{% endtab %}
{% tab title="Java" %}
```java
DrSenderConfiguration drSenderCfg = new DrSenderConfiguration();
drSenderCfg.setSenderGroups("group1");

// the addresses of the remote replica cluster's nodes that will receive data updates 
drSenderCfg.setConnectionConfiguration(new DrSenderConnectionConfiguration().setDataCenterId((byte) 2)
        .setReceiverAddresses("172.25.4.200:50001"));

drSenderCfg.setUseIgniteSslContextFactory(false);

SslContextFactory sslContextFactory = new SslContextFactory();
sslContextFactory.setKeyStoreFilePath("/path/to/server.p12");
sslContextFactory.setKeyStorePassword("123456".toCharArray());

sslContextFactory.setTrustStoreFilePath("/path/to/trust.p12");
sslContextFactory.setTrustStorePassword("123456".toCharArray());

drSenderCfg.setSslContextFactory(sslContextFactory);

```
{% endtab %}
{% endtabs %}

### 3. Configure Caches

Once the connection between the clusters is configured, you can configure a specific cache to be replicated through this connection. This is done by specifying the sender group name in the cache's configuration.

To configure replication for a specific cache, you must complete the following steps:

- In the master cluster: Specify a sender group in the configuration of the cache. Data updates in that cache will be sent to the replica cluster through that sender group.
- In the replica cluster: Create a cache with the same name.
- Repeat this procedure for all caches you want to replicate.

Below is an example configuration of a cache in the master cluster. The cache will be replicated through the sender group ("group1") that we defined in the [2. Configure Connection Between Clusters]() section.

{% tabs %}
{% tab title="XML" %}
```xml
<property name="cacheConfiguration">
    <bean class="org.apache.ignite.configuration.CacheConfiguration">
        <!-- Setting up basic cache parameters -->
        <property name="name" value="myCache"/>
        <property name="cacheMode" value="PARTITIONED"/>
        <property name="backups" value="1"/>

        <property name="pluginConfigurations">
            <bean class="org.gridgain.grid.configuration.GridGainCacheConfiguration">
                <!--
                    Activate cache replication.
                -->
                <property name="drSenderConfiguration">
                    <bean class="org.gridgain.grid.cache.dr.CacheDrSenderConfiguration">
                        <property name="senderGroup" value="group1"/>
                    </bean>
                </property>

                <!-- Other parameters. -->
            </bean>
        </property>
    </bean>
</property>
```
{% endtab %}
{% tab title="Java" %}
```java

```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
var cfg = new CacheConfiguration()
{
    CacheMode = CacheMode.Partitioned,
    Name = "myCache",
    AtomicityMode = CacheAtomicityMode.Atomic,
    PluginConfigurations = new[]
    {
        new GridGainCachePluginConfiguration
        {
            DrSenderConfiguration = new CacheDrSenderConfiguration
            {
                SenderGroup = "group1",
                BatchSendSize = 4 * 1024
            }
        }
    }
};

var cache = ignite.GetOrCreateCache<int, string>(cfg);
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

For the complete list of parameters, refer to the `org.gridgain.grid.cache.dr.CacheDrSenderConfiguration` javadoc.

The replica cluster must have a corresponding cache with the same name.
Define a cache in the replica cluster and activate the `GridGainCacheConfiguration` plugin in the cache's configuration.
The cache in the replica cluster can have configuration properties that are different from those in the master cluster (because only data is replicated, not configuration parameters).
If you want to replicate data to a cache with identical configuration, you must copy the cache configuration parameters from the master cluster.

Below is an example configuration of the cache configuration in the replica cluster:

{% tabs %}
{% tab title="XML" %}
```xml
<property name="cacheConfiguration">
    <bean class="org.apache.ignite.configuration.CacheConfiguration">
        <!-- Setting up basic cache parameters -->
        <property name="name" value="myCache"/>
        <property name="cacheMode" value="PARTITIONED"/>
        <property name="backups" value="1"/>

        <!-- Setting up DR related cache parameters -->
        <property name="pluginConfigurations">
            <bean class="org.gridgain.grid.configuration.GridGainCacheConfiguration">
                <property name="drReceiverEnabled" value="true"/>
            </bean>
        </property>
    </bean>
</property>
```
{% endtab %}
{% tab title="Java" %}
```java

```
{% endtab %}
{% endtabs %}

#### Dynamically Created Caches

If you want to replicate a dynamically created cache, you need to set the sender group for that cache and make sure that the corresponding cache is created in the replica cluster. The following procedure outlines the steps involved in this process.

1. For caches created via the Java API, specify a sender group by calling the `CacheDrSenderConfiguration.setSenderGroup(String)` method, as shown in the example below.

   {% tabs %}
   {% tab title="Java" %}
   ```java

   ```
   {% endtab %}
   {% tab title="C#/.NET" %}
   ```csharp
var cacheCfg = new CacheConfiguration()
{
    Name = "myCache",
    PluginConfigurations = new[]
    {
        new GridGainCachePluginConfiguration
        {
            DrSenderConfiguration = new CacheDrSenderConfiguration
            {
                //setting the sender group name
                SenderGroup = "group1"
            }
        }
    }
};
   ```
   {% endtab %}
   {% tab title="C++" %}
   unsupported
   {% endtab %}
   {% endtabs %}

   If you create caches using the [CREATE TABLE](../../reference/sql/ddl.md#create-table) command, the only way to specify the sender group name is to use a predefined cache template.
   You can create a cache template with the desired sender group (and other replication-specific properties) and pass it as a parameter to the CREATE TABLE command.
   The created cache will have the properties of the specified template.
   For more information and examples on how to use cache templates, see the [Cache Template](../../gridgain8-usage/configuring-caches/configuration-overview.md#cache-templates) page.
2. Create a similar cache in the replica(s) that will receive replicated data.
3. Start using the cache. The data will be sent to the replica.
4. If you started putting data into the cache before creating its counterpart in the replica(s), you have to transfer the cache's content to the replica. This will ensure that the remote caches have exactly the same data and sending updates will not cause any issues.

   To do a state transfer for the new cache, use the following code snippet:

   {% tabs %}
   {% tab title="Java" %}
   ```java

   ```
   {% endtab %}
   {% tab title="C#/.NET" %}
   ```csharp
// Gets data center replication API
var dr = ignite.GetDataCenterReplication();

var task = dr.StartStateTransferAsync("myCache", 2);

// Wait while the state transfer is being completed.
task.Wait();
   ```
   {% endtab %}
   {% tab title="C++" %}
   unsupported
   {% endtab %}
   {% endtabs %}

#### Filtering Cache Entries

By default, all entries of the cache are replicated to the replica cluster.
However, you can prevent specific entries from being replicated by providing an entry filter.

An entry filter is set per cache in the master cluster. If the filter returns `true`, the entry will be replicated.
The following code example demonstrates how to set an entry filter.

{% tabs %}
{% tab title="Java" %}
```java
CacheDrSenderConfiguration cacheDrSenderCfg = new CacheDrSenderConfiguration();

cacheDrSenderCfg.setEntryFilter(new CacheDrEntryFilter<Long, String>() {

    @Override
    public boolean accept(CacheDrEntry<Long, String> entry) {

        // ...  

        //return true to replicate the entry 
        return true;
    }
});

GridGainCacheConfiguration ggCacheCfg = new GridGainCacheConfiguration();
ggCacheCfg.setDrSenderConfiguration(cacheDrSenderCfg);

CacheConfiguration<Long, String> cacheCfg = new CacheConfiguration<Long, String>("myCache");
cacheCfg.setPluginConfigurations(ggCacheCfg);

IgniteCache<Long, String> cache = ignite.getOrCreateCache(cacheCfg);
```
{% endtab %}
{% tab title="C#/.NET" %}
```csharp
[Serializable]
class CacheDrEntryFilter : ICacheDrEntryFilter<long, string>
{
    public bool Invoke(ICacheDrEntry<long, string> entry)
    {
        //return true to replicate the entry
        return true;
    }
}

....

var cacheCfg = new CacheConfiguration()
{
    Name = "myCache",
    PluginConfigurations = new[]
    {
        new GridGainCachePluginConfiguration
        {
            DrSenderConfiguration = new CacheDrSenderConfiguration
            {
                EntryFilter = new CacheDrEntryFilter()
            }
        }
    }
};

ignite.GetOrCreateCache<int, string>(cacheCfg);
```
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

#### Full State Transfer over Snapshot

When data center replication works normally, you can let it handle all issues. However, is some rare scenarios, you may want to replicate a cluster state to replica cluster by transferring a snapshot of a master cluster to it, restoring data and then performing an incremental snapshot. To do this:

- Create a [full snapshot](../snapshots/full-incremental-snapshots.md#full-snapshots) of the cluster you want to transfer data from (master cluster).

- Disconnect the remote data center that contains the destination cluster. This can be done by shutting down receiver on the remote data center.

- Copy snapshot to remote data center. Restore snapshot on the remote data center in the destination cluster:

```shell
# Getting a list of all the available snapshots.
# The output will include snapshots' IDs.
{gridgain}/bin/snapshot-utility.sh list

# Restoring the cluster to a specific snapshot passing its ID.
{gridgain}/bin/snapshot-utility.sh restore -id=1483663276482
```

- Reconnect the destination cluster.

- Execute incremental state transfer with specifying snapshot id, which was restored on destination cluster during previous steps, to push the latest updates, which may occurred since snapshot was created, to the remote cluster:

```java
GridGain gg = ignite.plugin(GridGain.PLUGIN_NAME);

GridDr dr = gg.dr();

GridDr.incrementalStateTransfer(String cacheName, long snapshotId, byte dataCenterId);
```

{% hint style="info" %}
Before creating a snapshot on node 1 (sender) you are planning to transfer to node 2 (receiver), disconnect the receiver from the sender to prevent premature transfer of REMOVE and DELETE operations. 
{% endhint %}

{% hint style="info" %}
If the sender node gets restarted in the period between the creation of the snapshot creation and the beginning of full state transfer, the REMOVE and DELETE operations stored in memory will be lost. Make sure you either store the sender data on disk or keep sender online for the above period.
{% endhint %}

## Conflict Resolution

Conflict resolution requirements depend on the replication mode used on your cluster:

- Conflicts should not occur in the *active-passive* replication mode because the replica cluster only receives updates from the master and does not handle user requests. Make sure that the replica cluster does not receive user requests that change the entries in the cache.

- Conflicts can occur in the *active-active* replication mode because clusters both replicate data to each other and handle user requests. This can lead to a situation when a cache entry is updated in both clusters to different values by separate user requests. Since the caches must have identical content, one value has to be rejected.

By default, GridGain attempts to resolve conflicts automatically by comparing the topology version and the order of old and new entries. When the conflict happens between entries from different data centers, GridGain will use the newer entry by default.

You can override default behavior by defining your custom conflict resolution logic with the `CacheConflictResolver` interface. When a conflict is detected and the user-provided implementation of `CacheConflictResolver` is invoked, a special object `CacheConflictContext` is passed to it. This object has all the necessary data to make a decision regarding the conflict.

Conflict resolution can have one of the following outcomes:

| Outcome | Method | Description |
|---|---|---|
| Use New | CacheConflictContext.useNew() | Incoming update always overwrites existing entry. Default value. |
| Use Old | CacheConflictContext.useOld() | Incoming update is always ignored and the existing entry remains unmodified. |
| Merge | CacheConflictContext.merge() | Neither old nor new entry should be used. User provides the new value for cache entry manually. This is treated as an update in the local data center. |

The following example shows how to implement conflict resolver that repeats the default GridGain strategy and how add it to cache configuration:

{% tabs %}
{% tab title="Java" %}
```java
CacheConfiguration<Integer, String> cfg = new CacheConfiguration<>();

GridGainCacheConfiguration cacheCfg = new GridGainCacheConfiguration();

cacheCfg.setConflictResolver(new CacheConflictResolver<Integer, String>() {
    @Override
    public void resolve(CacheConflictContext<Integer, String> cacheConflictContext) {
        // This resolver always uses new values when DC IDs are different
        // You can implement your own conflict resolution strategy
        cacheConflictContext.useNew();
    }
});

cfg.setPluginConfigurations(cacheCfg);

IgniteCache<Integer, String> cache = ignite.getOrCreateCache(cfg);
```
{% endtab %}
{% tab title="C#/.NET" %}
unsupported
{% endtab %}
{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
Your `ConflictResolver` implementation should make a decision based only on data that can be extracted from `CacheConflictContext`. It should not rely on any other information that can vary across different nodes. Relying on such data (for example, local time on the node) may lead to data divergence as nodes will use inconsistent data for conflict resolution.
{% endhint %}

## Expiry Policy

Data Center Replication will not work correctly if the cache in the master cluster and its counterpart in the replica cluster use different expiry policies or if an accessed-based expiry policy is used.

Here is what happens in both cases when an expiry policy is used for a cache:

* Each entry has an expiration time that is defined by the expiry policy. When an entry is created, the expiration time of that entry is calculated by the master cluster and propagated to the replica cluster(s) together with the entry. The expiry policy itself is not transferred. In this case, the entry in the replica will expire based on the expiration time calculated by the master cluster.

* In the case when the expiry policy is based on the last access time, if an entry is read in the master cluster, its expiration time will be updated. However, the expiration time in the replica cluster will not be updated, because read operations are not propagated to the replica (because they don’t change the data). Therefore, the entry in the replica cluster will be deleted when its expiration time ends, while the entry in the master cluster won’t.

## Tombstone TTL

To ensure correctness of DR when deletes are present, you may need to tune the `DEFAULT_TOMBSTONE_TTL` property. The value of this property must be greater than the maximum expected lag between the sender and receiver clusters. It's usually defined by the maximum amount of time you expect the replication to be down due to external causes.  Setting the tombstone TTL too short can cause inconsistencies between sender and receiver clusters if updates or deletions are not replicated before the tombstones expire.

For example, if you need the DR to continue normally after the network between DC1 and DC2 has been down for 1 hour, your `DEFAULT_TOMBSTONE_TTL` value must be at least 1 hour. If the DR is down for more than `DEFAULT_TOMBSTONE_TTL`, you may need to perform a full-state transfer (FST) to make the clusters consistent again.

You can either perform a full FST or run it only for caches that have lost consistency. To identify affected caches, check the cluster logs: for each affected cache, GridGain writes a warning message that includes the cache name.

{% hint style="info" %}
Before performing FST, you must clear all data from the affected receiver caches.
{% endhint %}

To clear caches on the receiver node, do one of the following:

- Use `cache.clear()` to remove all entries from the cache.

- Destroy and then recreate the cache on the receiver cluster.

- Destroy the cache and restore it from a recent snapshot.

Only after the receiver cache has been cleared, you should initiate FST to restore a consistent state with the sender cache.

## Avoiding Multipath Updates

If multiple clusters in the topology are connected to each other with active-active replication, clusters will send transitive updates to other clusters in the topology after receiving them, causing the same update to be replicated multiple times. Even if these updates are not required, data nodes will always try to send them, creating extra load within the cluster, as only sender nodes are aware of data replication topology.

To avoid this, enable the `GG_DR_DISABLE_TRANSITIVE_UPDATES` property on all clusters you do not want to send transitive updates. The property must be enabled on all nodes in the cluster. If enabled, updates the cluster receives from other clusters will not be propagated from it.

{% hint style="info" %}
This property applies only to incremental active-active replication.
{% endhint %}

## Increasing Replication Message Size Limit

DR sender and receiver hubs reject a replication message that declares a size larger than the
`GG_DR_MAX_MESSAGE_SIZE` property (128 MB or 134217728 bytes by default). Raise the value only if your replication needs larger batches.

## Switching to Incremental Replication

Newer clusters use incremental datacenter replication by default. If you configured replication in older releases (GridGain 8.8.4 or earlier), it may use an older approach. When updating to a newer GridGain version, you need to switch to incremental DR.

To perform the update:

- Stop DataCenter Replication for the cluster in one or both of the following ways:
 * Use the `stopReplication`.
 * Stop all sender nodes.
- Perform a [rolling upgrade](../upgrade/rolling-upgrades.md) on the cluster.
- Re-enable Datacenter Replication. Most of Dataceter Replication configuration parameters, values and classes are compatible, outdated params will be ignored.
- Perform the same set of actions on each cluster you need to update.

{% hint style="warning" %}
You may lose the results of a `REMOVE` operation when restoring from a snapshot older than the [Tombstone TTL](#tombstone-ttl) property value. To mitigate this risk, make the Tombstone TTL duration longer than the snapshot creation interval defined by the backup/snapshot policy. Alternatively, make this value larger than the time required for snapshot creation and recovery combined, and make sure you take a snapshot whenever necessary.
{% endhint %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
