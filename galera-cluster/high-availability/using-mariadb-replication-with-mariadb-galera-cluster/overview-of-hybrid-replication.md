# Overview of Hybrid Replication

#### Hybrid Replication in MariaDB

Hybrid replication leverages standard, asynchronous MariaDB Replication to copy data from a synchronous MariaDB Galera Cluster to an external server or another cluster. This configuration establishes a one-way data flow, where the entire Galera Cluster serves as the source (primary) for one or more asynchronous replicas. This advanced setup combines the strengths of both replication methods: synchronous replication ensures high availability within the primary site, while asynchronous replication caters to specific use cases, allowing for flexible data distribution.

## Common Use Cases

Implementing a hybrid replication setup is a powerful technique for solving several common business needs:

| Use Case                     | Description                                                                                                                                             |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Disaster Recovery (DR)       | Galera Cluster provides high availability and automatic failover. Use asynchronous replication for a distant replica, promoting it during site outages. |
| Feeding Analytics/BI Systems | Replicate from OLTP Galera Cluster to a data warehouse or analytics server to run heavy queries without affecting production performance.               |
| Upgrades and Migrations      | Use an asynchronous replica to test new MariaDB versions or migrate to new hardware with minimal downtime.                                              |

## Key Challenges and Considerations

Before implementing a hybrid setup, it is critical to understand the technical challenges:

| Challenge           | Description                                                                                                                                    |
| ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| GTID Management     | Galera Cluster and MariaDB Replication use different GTID formats and implementations, requiring careful configuration to avoid conflicts.     |
| Replication Lag     | The external replica experiences the usual latencies of asynchronous replication, causing it to lag behind the real-time state of the cluster. |
| Failover Complexity | Failover within Galera Cluster is automatic, but failing over to the asynchronous DR replica is manual and requires careful planning.          |

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
