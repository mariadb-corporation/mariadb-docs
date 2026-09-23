---
description: >-
  GridGain 9.0.0 is the first major release of the GridGain 9 platform, rebuilt
  with a new transactional protocol, the Apache Calcite SQL engine, and
  RAFT-based cluster management.
---

# GridGain 9.0.0 Release Notes

## Overview

GridGain 9.0.0 is a major release of the GridGain Platform, built from the ground up with the new technologies and technological developments in mind.

## New Features

### Improved Architecture

GridGain 9 introduces a new transactional protocol and strictly serializable model that provides superior transactional consistency and simplifies distributed transactional application development. Lock-free, transactionally consistent reads support massive application concurrency and scalability.

It also makes use of the RAFT consensus algorithm to manage cluster nodes. With RAFT, several nodes form a cluster management group, automatically managing and monitoring cluster status. This approach provides improved stability for the cluster, as well as out-of the box protection from split-brain.

Additionally, the pluggable storage feature gives developers the flexibility to choose the storage engine based on application needs.

### Enhanced Support for SQL

GridGain 9 prioritizes SQL for interacting with data storage. Transactions are now supported seamlessly across all APIs, including SQL. Strictly serializable SQL transaction capability enables application migration from traditional RDBMS platforms.

The SQL engine is switched to Apache Calcite and most APIs are seamlessly integrated to work with your tables. With Apache Calcite engine, GridGain 9 is now ANSI SQL 2016 compliant (up from ANSI SQL 99 in GridGain 8).

Data schema management is also made more uniform across different APIs in GridGain 9. Now SQL, Key-Value API, and the new Record API all share access to the same schema, making it easy to access the same data from applications with different data models.

### Improved Usability

GridGain 9 now comes in bundled installation packages, allowing you to easily deploy on any container platform or operating system, on-premises or in the cloud.

Cluster and node configuration is reworked in HOCON based format. This allows for much more light-weight configuration files that are also easier to edit. To make things even easier, configuration is now split between cluster and node configuration.

GridGain 9 features the all-new CLI tool that replaces management scripts of previous GridGain versions. This new tool provide a single entry point for all GridGain 9 management from CLI, while also providing the same functionality via REST.

## Installation and Upgrade Information

### Upgrading from GridGain 8

GridGain 9 is a major version update that introduces backwards-incompatible changes. However, it is possible to smoothly migrate all of your data, configuration, and code with only minor changes. GridGain offers migration assistance so the users can execute the upgrade to GridGain 9 as easily as possible. Contact [GridGain Support](http://support.gridgain.com/) for details.

{% hint style="info" %}
Rolling Upgrade from GridGain 8 to GridGain 9 is not supported. Data Center Replication can be used instead to achieve a zero-downtime upgrade.
{% endhint %}

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
