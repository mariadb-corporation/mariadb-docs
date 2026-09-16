---
description: >-
  GridGain 9.0.4 introduces a new license format and a single ignite root
  configuration node, along with user object serialization for compute jobs.
---

# GridGain 9.0.4 Release Notes

## Overview

GridGain 9.0.4 is focused on improving CLI reporting and cluster performance.

## Major Changes

### License Format Change

In this release, the license format was changed and a license for 9.0.3 or earlier cannot be used. When updating to this or later release, contact us for an updated license.

### New Root Configuration Node

All GridGain configuration is now combined under a single `ignite` root node. When reusing previously created configuration, add the root node to configuration, for example:

In GridGain 9.0.3 or earlier:

```bash
node config update network.nodeFinder.netClusterNodes=["localhost:3344", "otherHost:3344"]
```

In GridGain 9.0.4 or later:

```bash
node config update ignite.network.nodeFinder.netClusterNodes=["localhost:3344", "otherHost:3344"]
```

## New Features

### User Object Serialization

You can now define a marshaller for your custom POJOs in Compute jobs. By default, the POJOs are marshalled to binary tuples, and automatically unmarshalled. Alternatively, you can specify the custom marshaller on both the server and the client to handle your objects in a specific way.

### Configuration for Storing CMG and Metastore

You can now use node configuration to set folders where the following is stored:

- The folder storing CMG information: `ignite.system.cmgPath`;
- The folder storing metastorage information: `ignite.system.metastoragePath`.
- The folder storing partitions: `ignite.system.partitionsBasePath`.
- The folder storing RAFT logs for partitions: `ignite.system.partitionsLogPath`.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-25363 | Configuration | A new ignite root configuration element was added for cluster configuration. |
| IGN-25359 | CLI Tool | Improved parameter autocompletion in CLI. |
| IGN-25354 | General | A number of configuration parameters were renamed. |
| IGN-25305 | General | Improved transaction performance. |
| IGN-25299 | General | Improved log messages when raft client tries to access a node that is not present in topology. |
| IGN-25103 | SQL | Fixed implicit conversion to DECIMAL for some SQL functions. |
| IGN-24969 | General | .NET: Added IMarshaller and JobDescriptor.Marshaller APIs to enable custom compute argument and result serialization. |
| IGN-24887 | General | You can now store CMG, metastore and partitions in separate folders. |
| IGN-24805 | Configuration | A new ignite root configuration element was added for node configuration. |

## Known Limitations

### Delay on DDL Requests

DDL requests, such as `CREATE TABLE`, take a few seconds each to complete. Because of that, large database initialization scripts may take longer than expected. This will be addressed in upcoming versions.

### Performance of GridGain 8 Applications

Some scenarios may see lower performance when moving to GridGain 9. This is a temporary limitation, and the performance in these scenarios will be improved in upcoming versions.

### High-Availability with Two Data Copies

When a partition loses majority of its copies, it becomes unavailable. This behavior is required for split-brain protection. Because of this, in a distribution zone with 2  data replicas, losing one node may lead to partial unavailability.

To achieve both split-brain protection and full availability with one node down, use 3 or more replicas.

Upcoming versions will add a high-availability mode that support full availability with one node down when using 2 replicas.

### Data Center Replication with Multiple Data Centers

Complex Data Center Replication topologies (for example, the ones involving cycles) of 3 or more data centers are not supported. This will be addressed in an upcoming release.

### GridGain 8 Features

The following features of GridGain 8 are not available in this version, and will be added in upcoming versions:

- Rack-Awareness
- SQL Offloading
- Tracing
- Service Grid
- Write-Behind Caching

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
