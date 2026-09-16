---
description: >-
  GridGain 9.0.3 adds incremental snapshots, SQL sequences, and cache expiry
  policies.
---

# GridGain 9.0.3 Release Notes

## Overview

GridGain 9.0.3 is focused on improving CLI reporting and cluster performance.

## New Features

### Incremental Snapshots

With this release, you can make incremental [snapshots](../../administrators-guide/snapshots/snapshots-and-recovery.md). Incremental snapshots automatically find the previous snapshot for the specified tables and create a snapshot of all data since that point of time. For example:

```bash
cluster snapshot create --type=full --all

....

cluster snapshot create --type=incremental --all
```

### Sequences

With this release, you can create a sequence that will be incremented or decremented automatically. These sequences can then be used to automatically fill the column in your tables.

To use sequences, create them with the SQL `CREATE SEQUENCE` command and then use [sequence functions](../../sql-reference/operators-and-functions.md#sequence-functions)

```sql
CREATE SEQUENCE IF NOT EXISTS defaultSequence;

CREATE TABLE IF NOT EXISTS Person (
  id bigint default NEXTVAL('defaultSequence') primary key ,
  city_id bigint,
  name varchar,
  age int,
  company varchar
);

INSERT INTO Person (city_id, name, age, company) values (1, 'John', 30, 'newCorp'), (2, 'Jane', 24, 'oldCorp')
```

### Cache Expiry

[Expiry policies](../../developers-guide/expiry-policies.md) can now also be configured for caches. You can create the `ttl` column and use the `EXPIRE AT` clause to remove the rows at the specified time:

```sql
CREATE CACHE Accounts (
    accountNumber INT PRIMARY KEY,
    firstName VARCHAR,
    lastName VARCHAR,
    balance DOUBLE,
    ttl timestamp DEFAULT CURRENT_TIMESTAMP + INTERVAL '2' HOURS
) WITH PRIMARY_ZONE = 'CACHES' EXPIRE AT ttl;
```

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-25261 | Platforms and Clients | .NET: Tuples no longer require to have columns in the same order to be considered equal. |
| IGN-25173 | Distributed Computing | Added TaskDescriptor to Compute API. |
| IGN-25113 | SQL | Added support for FORMAT clause of CAST operator. |
| IGN-25019 | Platforms and Clients | .NET: Fixed host name support in ClusterNode.Address. |
| IGN-24717 | General | Improved error message when trying to connect to uninitialized cluster. |
| IGN-24446 | Distributed Computing | .NET: Added MapReduce Compute API. |
| IGN-24329 | Platforms and Clients | Fixed an issue with key-value API not working with tables that have a single column. |
| IGN-21178 | Platforms and Clients | CPP: Added TLS support in C++ clients. |
| IGN-21176 | SQL | Fixed an issue that caused a new row to be inserted instead of updating an existing row. |

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
