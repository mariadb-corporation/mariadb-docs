---
description: >-
  Configure GridGain 9 clusters for data center replication with the CLI tool —
  create, start, scope, secure, monitor, and end replications.
---

# Configuring Replication

{% hint style="info" %}
This feature is only available as a part of GridGain 9 Enterprise and Ultimate editions.
{% endhint %}

This chapter explains how to configure your GridGain clusters for data replication by using the [CLI tool](../../ignite-cli-tool.md).

## Preparing for Replication

Data replication pulls updates from a remote cluster, called the *source cluster*. The cluster the data is copied to is called *replica cluster*.

By default, data center replication assumes that the source and replica clusters share the same schema. Pre-existing rows on the replica that have no corresponding row on the source are not affected by replication. When the same row is present on both clusters, GridGain resolves the conflict using the rule described in [Conflict Resolution](conflict-resolution.md).

Any change in source schema will cause the replication to stop. If this happens, update the schema on target manually and resume replication.

{% hint style="info" %}
Data center replication does not create new tables. Prior to starting replication, make sure the tables to be replicated in both the source and the target clusters have the same names and schemas.
{% endhint %}

All `dcr` commands require `MANAGE_DCR` privilege, including read-only `dcr list` and `dcr status` commands. The example below shows how you can grant it to the role:

```sql
GRANT PRIVILEGES MANAGE_DCR TO dcr_admin;
```

## Connecting to Source Server

To connect to a source cluster, use the `dcr create` command:

```bash
dcr create --name replication_name --source-cluster-address=127.0.0.1:10800
```

This command will create the replication on the replica cluster, but not start the replication process yet. You can review the configuration and make sure the source cluster is prepared for replication prior to [Starting Replication](#starting-replication). No additional configuration on source cluster is required.

You can also specify multiple nodes from the same cluster, in which case GridGain will connect to the first node listed, or the first node that it can establish connection to. It then establishes background connections to other nodes and uses those connections if the connection to the primary node fails:

```bash
dcr create --name replication_name --source-cluster-address=127.0.0.1:10800,127.0.0.1:10801,127.0.0.2:10800
```

This command creates a connection, but does not start replication on its own. The name of the replication will be used later to address it in the commands.

## Starting Replication

### Active-Passive Replication

To start replication, use the `dcr start` command:

```bash
dcr start --name replication_name --schema=PUBLIC --all
```

The cluster will start the data replication process from the cluster running on the `127.0.0.1` address, and will copy all tables from the `PUBLIC` schema.

To replicate all tables from all schemas, omit `--schema`:

```bash
dcr start --name replication_name --all
```

When the replication is first started, GridGain performs a special operation called full state transfer, copying the existing data from the source cluster to the replica cluster.

Afterwards, updates committed on the source cluster are continuously applied to the replica cluster.

{% hint style="warning" %}
The source cluster must keep its historical data available for longer than replication needs to reach it, or replication stops. GridGain relies on the source cluster retaining data back to the point in time that replication is reading from. If the source garbage-collects that data first, replication stops with an error and does not resume on its own.

To prevent this, set `ignite.gc.lowWatermark.dataAvailabilityTimeMillis` on the source cluster so that it comfortably exceeds the time needed to copy the largest replicated table and any expected replication lag. If replication has already stopped for this reason, increase the period and restart replication. For details, see [Low Watermark and Garbage Collection](../storage/low-watermark.md).
{% endhint %}

You can configure more specific replication by limiting the scope or nodes that are allowed to participate as described in the [Replication Configuration](#replication-configuration) section.

### Active-Active Replication

The only difference between starting active-passive and active-active replication is that you need to configure the both clusters to replicate data to each other.

The example below assumes that you have 2 nodes on addresses `127.0.0.1` and `127.0.0.2` that belong to different clusters. Then, it configures replication on both clusters targeting each other.

```bash
connect http://127.0.0.1:10300
dcr create --name replication_name --source-cluster-address=127.0.0.2:10800
dcr start --name replication_name --schema=PUBLIC --all
disconnect

connect http://127.0.0.2:10300
dcr create --name replication_name --source-cluster-address=127.0.0.1:10800
dcr start --name replication_name --schema=PUBLIC --all
```

#### Conflict Resolution

If the data was updated on both clusters before the data was replicated, the update with a later timestamp will be kept.

### One-Time Replication

In some scenarios, it is not necessary to copy data dynamically. Instead, you can `flush` data once. When running the `flush` command, you specify the replication time in ISO format. All data up to that point will be replicated, and then the replication will stop automatically.

```bash
dcr flush --name replication_name --flush-point=2024-10-01T12:00:00+01:00
```

## Replication Configuration

### Limiting Replicating Nodes

Each replication runs on a single elected *worker node* on the replica cluster. By default, any node in the replica cluster is eligible to be elected. Because the worker node carries the load of pulling and applying changes, you may want to restrict the role to a subset of nodes — for example, to keep replication off nodes that handle latency-sensitive application traffic. To do this, list the eligible node names in `--replication-nodes` when creating the replication. GridGain elects the worker from this list and re-elects from the remaining list members if the current worker leaves the cluster.

```bash
dcr create --name replication_name --source-cluster-address=127.0.0.2:10800 --replication-nodes=defaultNode,otherNode
```

### Limiting Replication Scope

Replication is tracked on a per-table basis, so you can replicate data only from some tables in the cluster. To do this, use the `tables` option instead of `all`.

To replicate specific tables from a single schema, specify `--schema` and use unqualified table names:

```bash
dcr start --name replication_name --schema=CUSTOMER1 --tables=ORDERS,PRODUCTS,INVENTORY
```

To replicate specific tables from the `PUBLIC` schema, omit `--schema` (unqualified table names default to `PUBLIC`):

```bash
dcr start --name replication_name --tables=ORDERS,PRODUCTS,INVENTORY
```

To replicate tables from multiple schemas in one command, use fully-qualified table names (`SCHEMA.TABLE`). You can mix qualified and unqualified names — unqualified names default to the `PUBLIC` schema:

```bash
dcr start --name replication_name --tables=CUSTOMER1.ORDERS,CUSTOMER2.ORDERS,CONFIG
```

You can add more tables to the replication process after it is started by running `dcr start` again for the new tables:

```bash
dcr start --name replication_name --schema=CUSTOMER1 --tables=INVOICES,PAYMENTS
```

You can stop replication of specific tables as well:

```bash
dcr stop --name replication_name --schema=CUSTOMER1 --tables=ORDERS
```

In this case, the replication will continue for all other tables.

### Replication on Secured Clusters

If your cluster has security enabled, you need to provide user credentials to the `dcr create` command to establish secure connection and authorization. The user needs to have a role with permissions that allow them to read and write to the tables that are being replicated.

```bash
dcr create --name replication_auth  --source-cluster-address=127.0.0.1:10800 --username admin --password myPass

dcr start --name replication_auth --schema=PUBLIC --all
```

If your cluster is further secured by using SSL, you need to provide keystore and truststore that will be used to connect to it in the `dcr create` command:

```bash
dcr create --name replication_ssl --source-cluster-address=127.0.0.1:10800 --keyStorePath=path-to-keystore --keyStorePassword=myPass --trustStorePath=path-to-truststore --trustStorePassword=myPass

dcr start --name replication_ssl --schema=PUBLIC --all
```

## Checking Replication Status

You can list the currently existing replications by using the `list` command:

```bash
dcr list
```

This command lists all existing replications and their statuses. You can get more in-depth information on each replication by using the `status` command:

```bash
dcr status --name replication_name
```

## Ending Replication

To stop replication, first stop the replication process for all tables:

```bash
dcr stop --name replication_name --all
```

This stops the replica cluster from pulling further updates, but does not delete the replication configuration. Replication can be resumed by running `dcr start` again on the same name.

To completely remove the replications, use the `delete` command:

```bash
dcr delete --name replication_name
```

This will permanently delete the replication configuration. If replication is recreated, it will need to first synchronize the clusters, instead of resuming where it stopped before.
