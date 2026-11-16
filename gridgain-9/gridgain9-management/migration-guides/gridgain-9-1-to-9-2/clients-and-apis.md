---
description: >-
  Client and API changes when upgrading from GridGain 9.1 to 9.2: Java 21 for client libraries, the removed PartitionManager and RecordSupportInternal, and the data center replication REST API.
---

# Client and API Changes

GridGain 9.2 requires Java 21 for the Java client and the libraries that embed it. It also removes the deprecated `PartitionManager` API and the `RecordSupportInternal` class, and renames fields in the data center replication REST API.

## Client Libraries Need Java 21

The Java thin client, the JDBC driver, the Spring Boot starter, Spring Data, Hibernate, and the Kafka Connect connectors of 9.2 are compiled for Java 21. Run the applications and the Kafka Connect workers that use them on Java 21 or later. The .NET, C++, and Python clients and the ODBC driver need no JDK. See [Java 21 or Later](platform-and-packaging.md#java-21-or-later) and [Project Setup](../../../gridgain9-development/project-setup.md).

Clients and servers upgrade independently. Upgrade the cluster first, because an older client keeps working against a newer server. See [Client Upgrade](../../upgrade/client-upgrade.md).

## PartitionManager Removed

The deprecated `PartitionManager` interface and the `Table.partitionManager()` method are removed. Use `PartitionDistribution`, which has the same methods. The methods `partitions()`, `primaryReplicas()`, `primaryReplica(Partition)`, `partition(Tuple)`, and `partition(K, Mapper<K>)`, and their `Async` variants, keep their names and signatures. `Table.partitionDistribution()` already exists in 9.1.29, so you can change the code before the upgrade. See [Table API](../../../gridgain9-development/table-api.md) and [Data Partitioning](../../../architecture/storage/data-partitioning.md).

In Java, change the call and the declared type:

```java
// 9.1
PartitionManager manager = table.partitionManager();

// 9.2
PartitionDistribution distribution = table.partitionDistribution();
```

In .NET, `ITable.PartitionManager` and `IPartitionManager` are removed. Use `ITable.PartitionDistribution` and `IPartitionDistribution`. The methods `GetPrimaryReplicasAsync()`, `GetPrimaryReplicaAsync(IPartition)`, `GetPartitionAsync(IIgniteTuple)`, and `GetPartitionAsync<TK>` keep their names. `IPartitionDistribution` adds `GetPrimaryReplicasAsync(IClusterNode)` and `GetPartitionsAsync()`.

The C++ and Python clients do not have this API.

## RecordSupportInternal Removed

The class `org.apache.ignite.table.mapper.RecordSupportInternal` is removed. It was an internal class that was public in the `marshaller-common` module. If your code uses it, replace it with the JDK methods: `Class.isRecord()`, `Class.getRecordComponents()`, and `clazz.getDeclaredConstructor(componentTypes)` for the canonical constructor. Java records that you use as table row types keep working. See the section on tuples, POJOs, and records in [Table API](../../../gridgain9-development/table-api.md).

## Data Center Replication REST API

This section applies if you call the data center replication REST API (`/management/v1/dcr`) directly. For data center replication, see [Data Center Replication](../../data-center-replication/README.md) and [Configuring Replication](../../data-center-replication/configuring-replication.md).

- *Old request field names are no longer accepted.* 9.1 accepted two names for some request fields. 9.2 accepts only the current names. It ignores an old name without an error, so a request that still sends one is read as if the field were missing. These old names were not part of the published REST specification, so most automation is not affected. The current names already work on 9.1.29, so you can change your requests before the upgrade. Responses do not change.

  | Request | Old name | Name to use |
  | --- | --- | --- |
  | Create replication | `sourceClusterAuthConfig`, `sourceClusterSslConfig` | `authConfig`, `sslConfig` |
  | Start and stop | `tableList` | `tables` |

- *Stopping tables that are already stopped is an error.* If every table in a request to stop specific tables is already stopped, the request returns status 400 with `Table '<schema.table>' is already stopped.` In 9.1 it did nothing and returned `false`. If at least one table is still replicating, the request is accepted as before. Stopping a replication that is already stopped returned 400 in 9.1 too (`GG-DCR-13`). Check the state before you stop, or handle the 400 response in your automation.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
