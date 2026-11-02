---
description: >-
  How to manage SQL query memory in GridGain 9 using node and query memory
  quotas and memory offloading to run large queries safely.
---

# SQL Memory Management

GridGain provides ways of managing large queries safely and reliably that allow you to run any queries without risking running out of memory.

## Memory Quotas

Memory quotas can be used to prevent GridGain nodes from running out of memory when executing SQL queries that return large result sets. A query loads objects from tables or caches into memory. If there are too many objects, the objects are too large, or multiple large queries are executed on the node at the same time, the JVM can run out of memory. When memory quotas are configured, the SQL engine imposes a limit on the heap memory available to queries.

Quotas are configured for each node individually. You can have different limits on different nodes, depending on the amount of RAM available to the nodes. Additionally, you can set a cluster-wide limit to how much of the memory quota can be used up by a single SQL query.

Memory quota size can be configured in:

- Kilobytes - append 'K' or 'k', for example: 10k, 400K;
- Megabytes - append 'M' or 'm', for example: 60m, 420M;
- Gigabytes - append 'G' or 'g', for example: 7g, 2G;
- Percent of heap - append the '%' sign, for example: 45%, 80%.

### Node-Wide Memory Quota

By default, a quota for SQL queries is set to 60% of the heap memory available to the node. You can change this limit by setting the `sql.nodeMemoryQuota` node configuration property. To disable the memory quota, set it to 0. You can use the CLI tool to set it:

```bash
node config update --url http://localhost:10300 ignite.sql.nodeMemoryQuota="1000M"
```

If the node memory quota is exceeded, the query is interrupted and the `SQL query ran out of memory: Node quota was exceeded` error is returned.

### Query-Wide Memory Quota

By default, each individual query can use the entire memory quota. This may be undesirable in environments that run multiple large queries in parallel. You can use the `sql.statementMemoryQuota` cluster configuration property to limit the amount of memory that can be allocated to a single query.

```bash
cluster config update --url http://localhost:10300 ignite.sql.statementMemoryQuota="10M"
```

If the statement memory quota is exceeded, the query is interrupted and the `SQL query ran out of memory: Statement quota was exceeded` error is returned.

## Memory Offloading

Sometimes, it may be necessary to run queries that require more space than is available in memory. By default, these queries will reach a memory quota and fail. To avoid this, you can enable memory offloading on the cluster. If enabled, any data that is required for the query and cannot fit into memory will instead be stored on disk. This will cause the query to be executed slower, but be able to handle larger amounts of data.

To enable memory offloading, update cluster configuration:

```bash
cluster config update ignite.sql.offloadingEnabled=true
```

Once it is enabled, data limits and paths for offloading can be configured for each individual node.

### Offloaded Data Limit

By default, GridGain will not limit offloaded data. This may mean that especially large queries fill the disk and issues due to running out of disk space. To avoid this, you can configure local data limits for each node. These limits can be configured in:

- Kilobytes - append 'K' or 'k', for example: 10k, 400K;
- Megabytes - append 'M' or 'm', for example: 60m, 420M;
- Gigabytes - append 'G' or 'g', for example: 7g, 2G;

For example, the following configuration will only allow 10 Gigabytes to be offloaded to the drive:

```bash
node config update ignite.sql.offloadingDataLimit="10G"
```

Node restart is required to update this configuration.

### Offloaded Data Path

By default, the data will be stored in the `sql_offloading` folder. You can configure the path to the data on the node by setting the `offloadingDataDir` configuration parameter. You can provide an absolute path to the folder, or the relative path from the node's `work` directory.

```bash
node config update ignite.sql.offloadingDataDir="/home/GG9/offloadingFolder"
```

Node restart is required to update this configuration.
