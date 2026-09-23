---
description: >-
  GridGain 9.0.17 simplifies cluster initialization and adds a multicast node
  finder.
---

# GridGain 9.0.17 Release Notes

## Overview

GridGain 9.0.17 is a stability release that is dedicated to improving user experience and fixing usability issues.

## Major Changes

### Cluster Initialization Changes

This release features major changes in the `cluster init` command.

- The new `--license` parameter should now be used to provide the license file.
- You no longer need to specify cluster metastorage or management group nodes. If not specified, nodes will be selected automatically according to the following logic:
  - If the cluster size is 3 or fewer, all nodes are used for the metastorage group (CMG and metastorage).
  - If the cluster size is 4, three nodes are used to maintain an odd number, improving consensus efficiency.
  - If the cluster size is 5 or more, five nodes are used to balance fault tolerance and overhead.

## New Features

### Multicast Node Finder

This release provides a way to enable optional multicast node finder. When enabled, GridGain uses multicast to discover other nodes. By default, static node finder is used.

To start using multicast node finder:

- Modify the multicast configuration. The example below shows default multicast configuration:

  ```javascript
  ignite {
    network {
      nodeFinder {
        multicast {
          group="239.192.0.0"
          port=47401
          resultWaitTime=500
          ttl=-1
        }
      }
    }
  }
  ```

  You can modify it with the `node config update` command, for example:

  ```bash
  node config update ignite.network.nodeFinder.multicast.group=239.5.0.0
  ```

  Multicast address must be valid. You can learn more in [IANA guidelines](https://datatracker.ietf.org/doc/html/rfc5771) for multicast.

- Enable multicast finder:

  ```bash
  node config update ignite.network.nodeFinder.type=MULTICAST
  ```

Now, this node will be using multicast to find other nodes in the specified multicast group.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-27155 | General | Fixed a rare NPE that could happen when querying the LOCKS system view. |
| IGN-27154 | General | Improved output formatting for metrics exported to log. |
| IGN-27146 | General | The oomBufferSizeBites configuration was renamed to oomBufferSizeBytes. |
| IGN-27136 | General | Fixed an issue that could cause repeated warnings on long-running clusters. |
| IGN-27133 | General | Leases updated message is now correctly printed every 10 updates. |
| IGN-27111 | SQL | STATE column in LOCAL_PARTITION_STATES system view was renamed to PARTITION_STATE. |
| IGN-27103 | General | Fixed a possible exception during data recovery with no data on node. |
| IGN-27023 | Platforms and Clients | Python DB API: Added support for macOS. |
| IGN-27004 | General | Fixed an exception that could happen when primary data replica left the cluster during transaction. |
| IGN-26983 | Platforms and Clients | .NET: Fixed error code string representation. |
| IGN-26813 | General | Added Tuple support to data streamer with receiver as payload, argument, result. |
| IGN-26773 | SQL | BINARY data type is no longer supported. |
| IGN-26742 | Cluster Discovery | Added support for multicast node finder. |
| IGN-26631 | SQL | Fixed an issue that cause incorrect index column sorting when using catalog API. |
| IGN-26374 | General | Metastorage group and cluster name are no longer required to initialize the cluster. |
| IGN-26273 | General | Node names in the cluster must now be unique. |
| GG-42591 | General | Improved Docker image size. |
| GG-42493 | Cluster SQL Engine | TIMESTAMP data type is no longer supported for data expiry. Use TIMESTAMP WITH LOCAL TIME ZONE instead. |
| GG-42372 | Platforms & Clients | .NET: Added GridGain.Extensions.Caching.Ignite package. |
| GG-42269 | Licenses | New --license flag was added to cluster init command. |
| GG-41951 | Cluster Metrics & Monitoring | Fixed NotCompliantMBeanException that could happen after enabling JMX exporter. |
| GG-41467 | GridGain Integrations | Kafka source: added schema evolution support. |

## Known Limitations

### Data Restoration After Data Rebalance

Currently, data rebalance may cause partition distribution to change and cause issues with snapshots and data recovery. In particular:

- It is currently not possible to restore a `LOCAL` snapshot if data rebalance happened after snapshot creation. This will be addressed in one of the upcoming releases.
- It is currently not possible to perform point-in-time recovery if data rebalance happened after table creation. This will be addressed in one of the upcoming releases.

### Data Center Replication with Multiple Data Centers

Complex Data Center Replication topologies (for example, the ones involving cycles) of 3 or more data centers are not supported. This will be addressed in an upcoming releases.

### GridGain 8 Features

The following features of GridGain 8 are not available in this version, and will be added in upcoming versions:

- Rack-Awareness
- Tracing
- Service Grid

### SQL Performance in Complex Scenarios

There are known issues with the performance of SQL read-write transactions in complex read-write scenarios. These issues will be addressed in an upcoming releases.

## Installation and Upgrade Information

### System View Changes in GridGain 9.0.16

In GridGain 9.0.17, we continue to improve system view naming for more clarity and consistency across all system views. In this release, the column in the **LOCAL_PARTITION_STATES** view has been renamed from `STATE` to `PARTITION_STATE`.

The legacy column remains available for backward compatibility but is **deprecated** and will be removed in a future release.

| System View | Old Name | New Name |
|---|---|---|
| LOCAL_PARTITION_STATES | STATE | PARTITION_STATE |

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
