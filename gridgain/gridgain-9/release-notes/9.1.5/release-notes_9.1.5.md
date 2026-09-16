---
description: >-
  GridGain 9.1.5 introduces change data capture, secondary storage archiving, and partition awareness for client SQL, along with Docker Compose changes.
---

# GridGain 9.1.5 Release Notes

## Overview

GridGain 9.1.5 is a release with multiple minor improvements and significant improvements on cluster stability and performance.

## Major Changes

### Docker Compose Changes

This release features a major change in how docker compose files are created. Previously, you had to provide the configuration in the compose file itself. A new `BOOTSTRAP_NODE_CONFIG` environment variable allows you to instead provide a link to the mounted configuration file. You can use this variable to quickly set up initial configuration for nodes from a local configuration file, while keeping the configuration mutable.

{% hint style="warning" %}
Previously used docker compose files that provide node configuration are no longer supported and will need to be updated. If not updated, the nodes will start, however the configuration will not be applied.
{% endhint %}

Below is the example of a simple configuration that mounts the configuration file and used the `BOOTSTRAP_NODE_CONFIG` variable to connect to it:

```yaml
# docker-compose.yml
name: gridgain9

x-gridgain-def: &gridgain-def
  image: gridgain/gridgain9:9.1.5
  environment:
    JVM_MAX_MEM: "4g"
    JVM_MIN_MEM: "4g"
    # The path to node configuration in docker.
    BOOTSTRAP_NODE_CONFIG: /opt/gridgain/bootstrapConfig/node.conf
  volumes:
    # Mounted node.conf file with the node configuration.
    - ${BOOTSTRAP_NODE_CONFIG:-./node.conf}:/opt/gridgain/bootstrapConfig/node.conf
services:
  node1:
    <<: *gridgain-def
    command: --node-name node1
    ports:
      - "10300:10300"  # REST API port
      - "10800:10800"  # Client port
  node2:
    <<: *gridgain-def
    command: --node-name node2
    ports:
      - "10301:10300"
      - "10801:10800"
  node3:
    <<: *gridgain-def
    command: --node-name node3
    ports:
      - "10302:10300"
      - "10802:10800"
```

The above configuration uses the following `node.conf` file:

```json
ignite {
  network {
    port: 3344
    nodeFinder.netClusterNodes = ["node1:3344", "node2:3344", "node3:3344"]
  }
}
```

## New Features

### Change Data Capture

This release features the first implementation of change data capture. You can now use it to configure replication of data to Iceberg. Once configured all updates to GridGain tables will be automatically propagated to Iceberg.

To start CDC replication:

- Configure data source:
  ```bash
  cdc source create --name gridgain_source --type gridgain --tables PUBLIC.MY_TABLE1
  ```

- Configure data sink:
  ```bash
  cdc sink create --name iceberg_sink --type Iceberg
  ```

- Create a replication that uses previously configured sink and source:
  ```bash
  cdc replication create --name my_replication --source gridgain_source --sink iceberg_sink
  ```

- Start the replication:
  ```bash
  cdc replication start --name my_replication
  ```

### Archiving Data in Secondary Storage

When using secondary storage, you can configure your tables to delete data from primary storage when it is no longer in active use. To do this, you specify the `ARCHIVE AT` condition with a ttl of when the data should be removed from primary storage, for example:

```sql
CREATE TABLE IF NOT EXISTS Person (
  id int primary key,
  name varchar,
  ttl TIMESTAMP WITH LOCAL TIME ZONE)
  ZONE zone1 SECONDARY ZONE secondary_zone SECONDARY STORAGE PROFILE 'columnar_storage' ARCHIVE AT ttl;
```

Once data is archived, it will no longer be available in primary storage, but can still be accessed from secondary storage. To make sure data is read from secondary storage, you can use the `/*+ use_secondary_storage */` sql hint.

```sql
SELECT * FROM Person /*+ use_secondary_storage */
```

### Partition Awareness for Client SQL

With this release, clients will benefit from [partition awareness](../../developers-guide/clients/overview.md#partition-awareness) for SQL queries, significantly improving their performance.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-28368 | General | CLI tool now displays metric source names in alphabetic order. |
| IGN-28309 | Cluster SQL Engine | Fixed an issue that caused sql queries to hang when a UNION operator was used for a large number of tables. |
| IGN-28273 | Platforms & Clients | .NET: Fixed serialization-related issues in UpsertAll and data streamer in certain scenarios. |
| IGN-28269 | General | Log metric exporter configuration is extended with new parameters that can be used to change the format of output and the list of logged metrics. |
| IGN-28221 | Platforms & Clients | .NET: Added ISql.ExecuteBatchAsync for batch DML (INSERT/UPDATE/DELETE) execution. |
| IGN-28201 | General | Fixed incorrect estimation of partition sizes for zone-based partitions. |
| IGN-28175 | Cluster Storage Engine | Added extended transaction metrics. |
| IGN-28154 | General | CREATE ZONE command now checks if the relevant storage profile exists. |
| IGN-28137 | General | You can now disable distribution zone scaling. |
| IGN-28098 | SQL | Fixed an issue that caused an exception to be throw while comparing different numerics during index scan. |
| IGN-27911 | SQL | SQL queries from clients now benefit from partition awareness. |
| IGN-27856 | Cluster Metrics & Monitoring | Names of JMX beans showing metrics now include the name of Ignite node. |
| IGN-27677 | Distributed Data Streamer | .NET: Added payload, argument and result marshallers to data streamer APIs. |
| IGN-27371 | CLI Tool | Fixed an issue that caused SQL queries to return table column names instead of aliases in CLI tools. |
| IGN-27320 | SQL | Improved validation of timestamp literals in SQL queries. |
| GG-44459 | Builds and Deliveries | Updated Apache Commons Lang3 dependency to v3.18.0. |
| GG-44343 | Cluster Deployment | Added BOOTSTRAP_NODE_CONFIG variable for docker compose file. |
| GG-44187 | Cluster Continuous Queries | Java thin: fixed continuous query compatibility with older servers. |
| GG-44178 | Cluster SQL Engine | You can now configure basic authentication for DR connector. |
| GG-44127 | Cluster Continuous Queries | Added an CQ option for configuring an executor for async delivery and execution of subscriber methods. |
| GG-43990 | Cluster SQL Engine | Fixed the issue when compaction process could get stuck after dropping distribution zone. |
| GG-43858 | Distributed Data Structures | Improved Ignite native types mapping in map structures API. |
| GG-43852 | Distributed Data Structures | Distributed maps can now be created from java clients. |
| GG-43850 | Cluster Continuous Queries | Continuous queries will continue to publish events after the table is dropped for short period until corresponding storage is destroyed. |
| GG-43757 | Cluster Storage Engine | Added automatic updates to Near Cache using continuous queries. |
| GG-43611 | Cluster Storage Engine | Near Cache now supports getAll() and containsAll() operations. |
| GG-39340 | Cluster Storage Engine | You can now configure encryption parameters for DEKs (Data Encryption Key). |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.0`, `9.1.1`, `9.1.2`, `9.1.3`, `9.1.4`

## Known Limitations

### Rolling Upgrade Under Load

Currently, when performing rolling upgrade it is highly recommended to remove all load from cluster.

### Data Restoration After Data Rebalance

Currently, data rebalance may cause partition distribution to change and cause issues with snapshots and data recovery. In particular:

- It is currently not possible to restore a `LOCAL` snapshot if data rebalance happened after snapshot creation. This will be addressed in one of the upcoming releases.
- It is currently not possible to perform point-in-time recovery if data rebalance happened after table creation. This will be addressed in one of the upcoming releases.

### SQL Performance in Complex Scenarios

There are known issues with the performance of SQL read-write transactions in complex read-write scenarios. These issues will be addressed in an upcoming releases.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
