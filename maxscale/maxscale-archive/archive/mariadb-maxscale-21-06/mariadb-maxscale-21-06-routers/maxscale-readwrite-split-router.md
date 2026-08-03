# MaxScale Read/Write Split Router

MariaDB MaxScale is a database proxy that extends the high availability, scalability, and security of MariaDB Server while at the same time simplifying application development by decoupling it from underlying database infrastructure. It includes multiple routers that each support different use cases.

| Router                                                                                                                                   | Description                                                                                                                                                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Read/Write Split Router](../../../../maxscale-use-cases/readwrite-split-router-usage/understanding-maxscales-readwrite-split-router.md) | • Performs query-based load balancing. • Each client connected to MaxScale is mapped to multiple connections to different back-end database servers. • Routes write queries to connection to primary server. • Routes read queries to connection to replica server. |

| Feature                                                                                    | Read/Write Split Router |
| ------------------------------------------------------------------------------------------ | ----------------------- |
| Supports MariaDB Replication deployments                                                   | Yes                     |
| Supports Galera Cluster deployments                                                        | Yes                     |
| Supports Multi-Node Enterprise ColumnStore deployments                                     | Yes                     |
| Performs query-based load balancing                                                        | Yes                     |
| Routes client connections to multiple servers simultaneously                               | Yes                     |
| Routes write queries to primary and read queries to replicas                               | Yes                     |
| Automatically reconnects clients to the new primary after failover or switchover           | Yes                     |
| Automatically replays transactions on the new primary after failover or switchover         | Yes                     |
| Automatically retries failed queries                                                       | Yes                     |
| Enforces causal reads to avoid reading stale data caused by slave lag                      | Yes                     |
| Performs connection-based load balancing                                                   | No                      |
| Routes client connections to configured server type                                        | No                      |
| Mitigates the effect of primary failures by acting as a Binlog Server                      | No                      |
| Reduces bandwidth requirements of primary server in environments with many replica servers | No                      |
| Replicates from MariaDB to a Kafka broker                                                  | No                      |

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
