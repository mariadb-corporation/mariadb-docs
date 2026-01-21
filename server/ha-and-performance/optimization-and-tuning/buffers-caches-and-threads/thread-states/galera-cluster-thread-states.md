# Galera Cluster Thread States

This article documents thread states that are specific to [MariaDB Enterprise Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/) and appear in the [SHOW PROCESSLIST](../../../../reference/sql-statements/administrative-sql-statements/show/show-processlist.md) when nodes are performing cluster-specific operations. These states enable monitoring of session status within clustered environments.&#x20;

The following table lists the thread states present in Galera Cluster and their descriptions:

| Thread State                    | Description                                                                                                                         |
| ------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| waiting to execute in isolation | The thread is waiting to execute a transaction in isolation mode.                                                                   |
| waiting for TOI DDL             | The thread is waiting for a Total Order Isolation Data Definition Language (DDL) operation to complete.                             |
| waiting for flow control        | The thread is paused due to Galera flow control, which regulates replication throughput.                                            |
| waiting for certification       | The transaction is waiting for Galera transaction certification before it can be applied to avoid conflict with other transactions. |

These states contribute in the identification of synchronization delays and performance bottlenecks in a Galera Cluster framework.

> These states were introduced in MariaDB Enterprise Server 11.4 and are also available in MariaDB Community Server 11.0.3 and later.

## See Also

* [SHOW PROCESSLIST](../../../../reference/sql-statements/administrative-sql-statements/show/show-processlist.md)
* [Galera Cluster Flow Control](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/performance-tuning/flow-control-in-galera-cluster)
* [MariaDB Galera Cluster Overview](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/)
* [What's New in MariaDB Enterprise Server 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/11.4/whats-new)
