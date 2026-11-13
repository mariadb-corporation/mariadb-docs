---
description: >-
  Client and API changes when upgrading from GridGain 9.1 to 9.2: Java 21 for client libraries, the removed PartitionManager and RecordSupportInternal, and the data center replication REST API.
---

# Client and API Changes

GridGain 9.2 requires Java 21 for the Java client and the libraries that embed it. It also removes the deprecated `PartitionManager` API and the `RecordSupportInternal` class, and tightens the data center replication REST API.

## Client Libraries Need Java 21

The Java thin client, the JDBC driver, the Spring Boot starter, Spring Data, Hibernate, and the Kafka Connect connectors of 9.2 are compiled for Java 21. Run the applications and the Kafka Connect workers that use them on Java 21 or later. The .NET, C++, and Python clients and the ODBC driver need no JDK. See [Java 21 or Later](platform-and-packaging.md#java-21-or-later).

For how clients and servers of different versions work together, see [Client Upgrade](../../upgrade/client-upgrade.md).

## PartitionManager Removed

The deprecated `PartitionManager` interface and the `Table.partitionManager()` method are removed. Use `PartitionDistribution`, which has the same methods.

In Java, change the call and the declared type:

```java
// 9.1
PartitionManager manager = table.partitionManager();

// 9.2
PartitionDistribution distribution = table.partitionDistribution();
```

The methods `partitions()`, `primaryReplicas()`, `primaryReplica(Partition)`, `partition(Tuple)`, and `partition(K, Mapper<K>)`, and their `Async` variants, have the same names and signatures on `PartitionDistribution`.

In .NET, `ITable.PartitionManager` and `IPartitionManager` are removed. Use `ITable.PartitionDistribution` and `IPartitionDistribution`. The methods `GetPrimaryReplicasAsync()`, `GetPrimaryReplicaAsync(IPartition)`, `GetPartitionAsync(IIgniteTuple)`, and `GetPartitionAsync<TK>` keep their names. `IPartitionDistribution` adds `GetPrimaryReplicasAsync(IClusterNode)` and `GetPartitionsAsync()`.

The C++ and Python clients do not have this API.

## RecordSupportInternal Removed

The class `org.apache.ignite.table.mapper.RecordSupportInternal` is removed. It was an internal helper and not part of the public API, but it was public in the `marshaller-common` module. If your code uses it, replace it with the JDK methods: `Class.isRecord()`, `Class.getRecordComponents()`, and `clazz.getDeclaredConstructor(componentTypes)` for the canonical constructor. Java records that you use as table row types keep working.

## Data Center Replication REST API

The following changes affect clients that call the data center replication REST API (`/management/v1/dcr`) directly:

- *Stopping tables that are already stopped is an error.* A request to stop specific tables of a running replication returns status 400 with `Table '<schema.table>' is already stopped.` if every requested table is already stopped. In 9.1, the request did nothing and returned `false`. If at least one requested table is still replicating, the request is accepted as before. Stopping a replication that is already stopped already returned 400 in 9.1 (`GG-DCR-13`). Check the state before you stop, or handle the 400 response in your automation.
- *Start and stop report the saved state.* In 9.1, a start or stop request that lost a race with another change could report success without saving the new state. In 9.2, the request is checked against the state that it changed and retried. A concurrent start of a table that is already replicating returns 409.
- *Only documented request fields are read.* Use the field names of the documented API, for example `tables` to select the tables to start or stop, and `authConfig` and `sslConfig` to create a replication. Fields that are not part of the API are ignored.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
