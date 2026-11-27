---
description: >-
  Client and API changes in the GridGain 9.1 to 9.2 upgrade: Java 21, removed PartitionManager and RecordSupportInternal, and the data center replication REST API.
---

# Client and API Changes

GridGain 9.2 requires Java 21 for the Java client and the libraries that embed it, removes the `PartitionManager` API and the `RecordSupportInternal` class, and renames fields in the data center replication REST API.

## Client Libraries Need Java 21

The Java thin client, the JDBC driver, the Spring and Hibernate integrations, and the Kafka Connect connectors need Java 21 or later in the JVM that runs them. See [Java 21 or Later](platform-and-packaging.md#java-21-or-later) and [Project Setup](../../../gridgain9-development/project-setup.md).

Upgrade the cluster before the clients, because an older client keeps working against a newer server. See [Client Upgrade](../../upgrade/client-upgrade.md).

## PartitionManager Removed

The deprecated `PartitionManager` interface and the `Table.partitionManager()` method are removed. Use `PartitionDistribution`, which has the same methods, including the `Async` variants. `Table.partitionDistribution()` already exists in 9.1.29, so you can change the code before the upgrade. See [Table API](../../../gridgain9-development/table-api.md) and [Data Partitioning](../../../architecture/storage/data-partitioning.md).

In Java, change the call and the declared type:

```java
// 9.1
PartitionManager manager = table.partitionManager();

// 9.2
PartitionDistribution distribution = table.partitionDistribution();
```

In .NET, `ITable.PartitionManager` and `IPartitionManager` are removed. Use `ITable.PartitionDistribution` and `IPartitionDistribution`, which keep the method names. `IPartitionDistribution` also has `GetPrimaryReplicasAsync(IClusterNode)` and `GetPartitionsAsync()`, which are available since 9.1.29.

The C++ and Python clients do not have this API.

## RecordSupportInternal Removed

The class `org.apache.ignite.table.mapper.RecordSupportInternal` is removed. It was an internal class, so most applications are not affected. If yours imports it, replace it with the JDK methods: `Class.isRecord()`, `Class.getRecordComponents()`, and `clazz.getDeclaredConstructor(componentTypes)` for the canonical constructor. Java records that you use as table row types keep working. See the section on tuples, POJOs, and records in [Table API](../../../gridgain9-development/table-api.md).

## Data Center Replication REST API

This section applies if you call the data center replication REST API (`/management/v1/dcr`) directly. For data center replication, see [Data Center Replication](../../data-center-replication/README.md) and [Configuring Replication](../../data-center-replication/configuring-replication.md).

### Rename Request Fields

9.1 accepted two names for some request fields. 9.2 accepts only the current name and ignores an old one without an error, so the request is read as if the field were missing. The current names already work on 9.1.29, and responses do not change. The old names were not in the published REST specification, so most automation is not affected.

| Request | Old name | Name to use |
| --- | --- | --- |
| Create replication | `sourceClusterAuthConfig`, `sourceClusterSslConfig` | `authConfig`, `sslConfig` |
| Start and stop | `tableList` | `tables` |

### Handle Stopping Stopped Tables

If every table in a request to stop specific tables is already stopped, the request now returns status 400 with `Table '<schema.table>' is already stopped.` In 9.1 it did nothing and returned `false`. If at least one table is still replicating, the request is accepted as before. Stopping a whole replication that is already stopped returned 400 in 9.1 too. Check the state first, or handle the 400 response.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
