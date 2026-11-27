---
description: >-
  Create and configure GridGain 9 distribution zones to control how tables are
  partitioned, replicated, and distributed across cluster nodes.
---

# Distribution Zones

## What is a Distribution Zone?

Distribution zones in GridGain are entities that combine sets of tables and define:

- How these tables are distributed across the cluster, how many copies of data are made, how the data is partitioned, how partitions are assigned to nodes.

- On which cluster nodes these tables will be stored.

- How the cluster reacts to nodes entering or leaving the cluster, e.g. whether the tables will automatically start using a new node when the cluster is scaled up.

- Starting with GridGain 9.2, how the replicas of each partition are spread across [fault domains](#fault-domains), groups of nodes that are likely to fail together.

Distribution zones are not equivalent to the concept of availability zone commonly used in cloud computing.

Availability zone is a set of infrastructure resources with independent hardware, networking, power, and is often physically separated from other availability zones.

GridGain cluster often spans across multiple availability zones, and distribution zones also typically span across multiple availability zones. That way, tables can continue to be available even if one of the availability zones goes down.

## Default Zone

GridGain 9 provides a `default` distribution zone that is preconfigured, but is not created on startup. When a table is created without specifying the distribution zone, the zone is created first, and the table is added to it. Following this, the distribution zone stores data from tables when they are not configured to use a different zone, or if a [different default zone](../../reference/sql/distribution-zones.md#alter-zone-set) is not configured.

This distribution zone has 25 partitions, 1 partition replica and does not adjust itself to existing nodes leaving the cluster. For production purposes, we recommend manually creating and configuring a new distribution zone adjusted for your purposes.

## Creating and Using Zones

Distribution zones in GridGain 9 are created by using the SQL `CREATE ZONE` command. When creating a zone, you must specify the [Storage Profile](README.md) to use. The storage profile determines what storage engine will be used, and storage properties.

The example below creates a primary distribution zone with the default storage profile:

```sql
CREATE ZONE PrimaryZone (PARTITIONS 25) STORAGE PROFILES ['default'];
```

### Using Secondary Zones

You can also create a secondary zone for a table. There are several limitations for secondary zones:

- Tables cannot reference the same zone as both primary and secondary.
- Secondary zones should have the same amount of partitions as the primary zones.
- Secondary zones cannot be modified. Scale up and scale down parameters must be set to `2147483647`.

Example below shows how to create a secondary zone considering the limitations above:

```sql
CREATE ZONE SecondaryZone (PARTITIONS 25, AUTO SCALE UP 2147483647, AUTO SCALE DOWN 2147483647) STORAGE PROFILES ['columnar_storage'];
```

Then you can create a table with both primary and secondary zones:

```sql
CREATE TABLE Person (
id int primary key,
city_id int,
name varchar,
age int,
company varchar
) PRIMARY ZONE PrimaryZone PRIMARY STORAGE PROFILE 'default'
SECONDARY ZONE SecondaryZone SECONDARY STORAGE PROFILE 'columnar_storage';
```

## Configuring Data Replication

You can control the number of partitions (how many pieces the data is split into) and replicas (how many copies of data are stored) by using the `PARTITIONS` and `REPLICAS` options.

If not specified, the distribution zone creates `(dataNodesCount * coresOnNode * 2) / replicaFactor` partitions, and does not create copies of data. The `dataNodesCount` is the estimated number of nodes that will be in the distribution zone when it  is created, according to its [filter](#node-filtering), its [storage profiles](README.md), and, starting with GridGain 9.2, its [replica filter attribute](#fault-domains). At least 1 partition is always created.

In the example below, the tables will be split into 50 partitions, and each partition will have 3 copies of itself stored on the cluster:

```sql
CREATE ZONE IF NOT EXISTS exampleZone (PARTITIONS 50, REPLICAS 3) STORAGE PROFILES ['default'];
```

Partitions with the same number for all tables in the zone are always stored on the same nodes within the distribution zone.

### Replicated Zones

For scenarios requiring maximum data availability, you can create a replicated zone by specifying `ALL` as the number of replicas. This automatically scales the number of replicas to match the number of nodes in your cluster, placing a copy of every partition on every node.

```sql
CREATE ZONE exampleZone (REPLICAS ALL) STORAGE PROFILES ['default'];
```

When you create a replicated zone, GridGain ensures that each partition has a replica on every node in the cluster. As new nodes join the cluster, they automatically receive replicas and become learners in the RAFT groups until the zone adjusts its configuration.

#### Combining Replicated and Standard Zones

A common pattern is to use replicated zones for reference data and standard zones with fewer replicas for transactional data:

```sql
-- Replicated zone for reference data
CREATE ZONE RefDataZone (REPLICAS ALL) STORAGE PROFILES ['default'];

-- Standard zone for transactional data
CREATE ZONE TransactionalZone (REPLICAS 3) STORAGE PROFILES ['default'];

-- Reference table in replicated zone
CREATE TABLE Countries (
  id int PRIMARY KEY,
  code varchar(2),
  name varchar(100)
) ZONE RefDataZone;

-- Transactional table in standard zone
CREATE TABLE Orders (
  id int PRIMARY KEY,
  customer_id int,
  country_code varchar(2),
  amount decimal
) ZONE TransactionalZone;
```

This approach gives you local access to reference data while keeping storage requirements reasonable for high-volume transactional data.

### Storage Profiles

When creating a distribution zone, you can define a set of [storage profiles](README.md) that can be used by tables in this zone. You cannot alter storage profiles after the distribution zone was created. To create a Distribution Zone that will use one or multiple Storage Profiles, use the following SQL command:

```sql
CREATE ZONE exampleZone (PARTITIONS 2, REPLICAS 3) STORAGE PROFILES ['profile1', 'profile3'];
```

In this case, the table created in this distribution zones can only use `profile1` or `profile3`.

### Quorum Size

You can set the `QUORUM SIZE` parameter to fine-tune the number of replicas that must be available for the zone to remain operational.

GridGain automatically configures the minimum recommended number of replicas for your distribution zone. `3` data replicas are required for quorum if the distribution zone has 5 or more replicas, 2 if there are between 2 and 4 replicas, or 1 if only one data replica exists.

There are the following limitations to quorum sizes depending on the number of replicas:

* *Minimum* value: `1` if there is only one replica and `2` if there is more than one.
* *Maximum* value: half the total number of replicas rounded up.

The example below shows how you can configure quorum size:

```sql
CREATE ZONE exampleZone (REPLICAS 9, QUORUM SIZE 5) STORAGE PROFILES ['default'];
```

{% hint style="info" %}
It is recommended to use odd number of replicas as your quorum size.
{% endhint %}

### Node Filtering

Distribution zones can get node attributes that can be specified in [node configuration](../../reference/configuration/node-configuration-parameters.md), and dynamically distribute data only to nodes that have the specified attributes. This can be used, for example, to only process data from the application on nodes with SSD drives. If no node matches the filter, the data will be stored on all nodes instead. Distribution zone filter uses JSONPath rules.

The example below creates a new `storage` attribute and sets it to `SSD`:

```bash
node config update -n defaultNode ignite.userAttributes.storage="SSD"
```

The example below creates a distribution zone that only stores data on nodes that have the SSD attribute:

```sql
CREATE ZONE IF NOT EXISTS exampleZone (NODES FILTER '$[?(@.storage == "SSD")]') STORAGE PROFILEs ['default'];
```

You can change the distribution zone filter by using the `ALTER ZONE` command, for example:

```sql
ALTER ZONE exampleZone SET DATA_NODES_FILTER='$[?(@.storage == "HDD")]';
```

If you no longer need to filter the data nodes, set the filter to match all nodes:

```sql
ALTER ZONE exampleZone SET DATA_NODES_FILTER='$..*';
```

### Fault Domains

{% hint style="info" %}
This feature is only available as a part of GridGain 9 Enterprise and Ultimate editions.
{% endhint %}

{% hint style="info" %}
Fault domains are available in GridGain 9.2 and later.
{% endhint %}

By default, GridGain stores the replicas of a partition on different nodes, but does not take into account which nodes are likely to fail together. If all nodes that store a partition fail together, the partition becomes unavailable.

A *fault domain* is a group of nodes that are likely to fail together. When you configure fault domains for a distribution zone, GridGain spreads the replicas of each partition across the fault domains. When one fault domain fails, the other fault domains still hold replicas of each partition. If the distribution zone has enough replicas and fault domains, they hold the majority of the replicas, and the data stays available. For the requirements, see [Planning Fault Domains](#planning-fault-domains).

Fault domains are defined by a [node attribute](../../reference/configuration/node-configuration-parameters.md#node-attributes): all nodes that have the same value of the attribute belong to the same fault domain, and each value of the attribute is a separate fault domain. To configure fault domains:

1. Set the attribute on each node that should store the data of the distribution zone, and restart the node to apply the change. The example below adds the node to the `rack1` fault domain:

   ```bash
   node config update -n defaultNode ignite.userAttributes.rack="rack1"
   ```

2. Specify the name of the attribute in the `REPLICA FILTER ATTRIBUTE` parameter of the distribution zone. The example below creates a distribution zone that spreads 3 replicas of each partition across the fault domains defined by the `rack` attribute:

   ```sql
   CREATE ZONE IF NOT EXISTS exampleZone (REPLICAS 3, REPLICA FILTER ATTRIBUTE 'rack') STORAGE PROFILES ['default'];
   ```

A distribution zone can use only one replica filter attribute. The name of the attribute and its values are case-sensitive.

#### How Replicas are Spread Across Fault Domains

GridGain spreads the replicas of each partition across the fault domains as evenly as possible. The replicas of the [consensus group](data-partitioning.md#replica-number) are spread in the same way.

The table below shows how replicas of each partition are placed in a cluster with 3 fault domains that have at least 2 nodes each:

| Replicas | Quorum Size | Replicas in Fault Domains |
| --- | --- | --- |
| 2 | 2 | One replica in each of two fault domains. |
| 3 | 2 | One replica in each fault domain. All replicas are in the consensus group. |
| 5 | 2 | One consensus group replica in each fault domain. Two learners are in two different fault domains. |
| 5 | 3 | One replica in each fault domain, and two more replicas in two different fault domains. All replicas are in the consensus group. |
| 6 | 2 | Two replicas in each fault domain: one consensus group replica and one learner. |

In a [replicated zone](#replicated-zones), every node stores a replica, so fault domains only define where the replicas of the consensus group are placed.

#### Planning Fault Domains

When planning fault domains, consider the following:

- Use at least 3 replicas and at least 3 fault domains, and make sure that each fault domain has enough nodes for its share of replicas: the number of replicas divided by the number of fault domains, rounded up. In this case, no fault domain holds the majority of the consensus group, and each partition keeps the majority when one fault domain fails. With 2 fault domains, one of them always holds at least half of the consensus group, so the partitions lose the majority when this fault domain fails.
- Use the same number of nodes in all fault domains. In this case, the distribution of replicas between nodes is fair. If fault domains have different numbers of nodes, the distribution can deviate from fair.
- Fault domains only apply to data partitions. The nodes of the [cluster management group](../cluster-lifecycle.md#cluster-management-group) and the [metastorage group](../cluster-lifecycle.md#cluster-metastorage-group) are selected when the cluster is initialized. Select them so that no fault domain holds the majority of the nodes of either group.

GridGain logs the `Fault domain constraint is relaxed or makes the partition distribution unfair` warning when one fault domain holds two or more replicas of the consensus group of a partition, and this is at least half of the group. The loss of such a fault domain makes the partition lose the majority. The same message at the `INFO` level reports an uneven load of the nodes that is caused by fault domains of different sizes.

#### Nodes Without the Attribute

Nodes that do not have the replica filter attribute, or have an empty or whitespace-only value of it, do not belong to any fault domain and are not used to store the data of the distribution zone. GridGain lists these nodes in the `Nodes without a value of the replica filter attribute are not data nodes of the zone` log message.

A node stores the data of the distribution zone only if it has the attribute, matches the [node filter](#node-filtering), and has the [storage profiles](#storage-profiles) of the zone. A `CREATE ZONE` or `ALTER ZONE` command that sets the attribute fails if no node in the cluster meets all these conditions. The same check runs when `ALTER ZONE` changes the node filter of a distribution zone that uses the attribute.

If the number of such nodes is less than the number of replicas, each partition has only as many replicas as there are such nodes.

#### Changing Fault Domains

You can configure fault domains for an existing distribution zone, or use a different attribute to define them, by using the `ALTER ZONE` command:

```sql
ALTER ZONE exampleZone SET (REPLICA FILTER ATTRIBUTE 'rack');
```

Before you configure fault domains for a distribution zone that already stores data, set the attribute on all nodes that must keep the data of the zone. The nodes without the attribute stop storing the data of the zone, and their replicas move to other nodes.

To stop using fault domains, drop the attribute:

```sql
ALTER ZONE exampleZone DROP REPLICA FILTER ATTRIBUTE;
```

After these commands, GridGain recalculates the partition distribution without waiting for the [scale up or scale down delay](#cluster-scaling), and starts [partition rebalance](data-partitioning.md#partition-rebalance) for the partitions whose replicas must move.

You cannot set, change, or drop the attribute of a distribution zone that a table uses as a [secondary zone](#using-secondary-zones).

To move a node to a different fault domain, change the value of the attribute in the node configuration and restart the node. GridGain then redistributes the replicas in the same way as when a node joins the cluster.

You can find the attribute used by the distribution zone in the `ZONE_REPLICA_FILTER_ATTRIBUTE` column of the `system.zones` [system view](../../reference/monitoring/system-views.md#zones).

### High Availability

By default, GridGain ensures strong consistency of data in the cluster. To do this, it requires the majority of [replicas of data partitions](distribution-zones.md) to be available. As partitions are spread across the nodes, it is possible to lose the majority of nodes that hold data for the data region, leading to all operations in the data region being stopped until the majority can be safely restored. This ensures that no data is lost.

In high load environments, this behavior may be undesirable, as it interrupts writing data at the cost of negating a minor chance of losing data together with the nodes that left the cluster. For this scenario, GridGain provides high availability zones. If a zone has high availability enabled, and the majority of nodes with data from it leave the cluster, the data on them is considered lost and, after a short delay in case the nodes return, the cluster continues to handle read and write requests normally.

High availability mode can only be enabled when distribution zone is created. To do this, use the following SQL command:

```sql
CREATE ZONE IF NOT EXISTS exampleZone (REPLICAS 3, CONSISTENCY MODE 'HIGH AVAILABILITY') STORAGE PROFILEs ['default'];
```

## Cluster Scaling

The number of active nodes in the cluster can dynamically change during its operation, as more nodes are added or nodes are taken down for maintenance or leave the cluster unexpectedly. You can configure whether and when GridGain adjusts the distribution zone to match the new cluster topology after a node enter or leaves the cluster.

Often it is a good idea to provide a buffer period before redistribution begins, allowing in-progress operations to complete. To control this behavior, you can specify the following parameters:

- `AUTO SCALE UP` - specifies the delay in seconds between nodes joining the cluster and the start of distribution zone adjustment to include the new nodes. This parameter is set to 0 seconds by default (immediate scale up).
- `AUTO SCALE DOWN` - specifies the delay in seconds between nodes leaving the cluster and the start of distribution zone adjustment to exclude the departed nodes. This parameter is set to `OFF` by default (no automatic scale-down occurs).

The example below shows how you can configure cluster scaling delay:

```sql
CREATE ZONE IF NOT EXISTS exampleZone (AUTO SCALE UP 300, AUTO SCALE DOWN 300) STORAGE PROFILES['default'];
```

Once distribution zone scaling is configured, you can disable it by specifying `OFF` in the corresponding parameter, for example:

```sql
ALTER ZONE exampleZone SET (AUTO SCALE DOWN OFF);
```

Alternatively, you can use the `zone datanodes reset` command to force the cluster to adjust the zone or zones immediately.

```bash
zone datanodes reset --zone-names=ZONE_NAME_1,ZONE_NAME_2
```

### Considerations for Zone Size

All tables stored in the distribution zone share resources. As the result, it is recommended to consider how large distribution zone needs to be.

As partitions are colocated on the same nodes, assigning tables commonly accessed together to the same distribution zone can reduce the overhead required for transmitting query results between nodes, and allows colocated [compute jobs](../../gridgain9-development/distributed-computing/about-distributed-computing.md).

However, if a table is under heavy load, it may negatively affect the performance when working with other tables in the same distribution zone. In most scenarios, this should not be a significant concern and correct data distribution for your scenarios should be prioritized.

## Checking Distribution Zone Properties

Distribution zone properties can be viewed through the `system.zones` [system view](../../reference/monitoring/system-views.md). You can use the following SQL command to get it:

```sql
SELECT * from system.zones;
```

The command lists information about all distribution zones on the cluster.

## Adjusting Distribution Zones

To change distribution zone parameters, use the `ALTER ZONE` command. You can use the same parameters as when creating the zone. For example:

```sql
ALTER ZONE IF EXISTS exampleZone SET (REPLICAS 5);
```

## Example Zone Usage

In this example, we create a distribution zone and then create 2 tables that will be colocated on the same zone.

```sql
CREATE ZONE IF NOT EXISTS EXAMPLEZONE (PARTITIONS 20, REPLICAS 3) STORAGE PROFILES ['default'];

CREATE TABLE IF NOT EXISTS Person (
  id int primary key,
  city_id int,
  name varchar,
  age int,
  company varchar
) PRIMARY ZONE EXAMPLEZONE;

CREATE TABLE IF NOT EXISTS Account (
  id int primary key,
  name varchar,
  amount int
) PRIMARY ZONE EXAMPLEZONE;
```

## See Also

- [Design a Schema for Distributed SQL](../../gridgain9-get-started/learning-paths/schema-design-for-distributed-sql/schema-distributed-sql.md)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
