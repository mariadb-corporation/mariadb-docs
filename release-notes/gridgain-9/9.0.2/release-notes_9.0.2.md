---
description: >-
  GridGain 9.0.2 improves CLI reporting and cluster performance and adds a SQL
  partition filter column.
---

# GridGain 9.0.2 Release Notes

## Overview

GridGain 9.0.2 is focused on improving CLI reporting and cluster performance.

## New Features

### Support for SQL Partition Filter

In this release, a system `__part` column was added to tables. You can use this column to perform `SELECT` operations on a specific partition, for example:

```sql
SELECT city_id, id FROM Person WHERE '__part'=23;
```

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| GG-39947 | CLI | Improved CLI error message for uninitialized cluster. |
| GG-39939 | Licenses | License signature is now obscured in cluster configuration. |
| GG-39814 | CLI | Tables argument is now optional for dcr stop command. |
| GG-39812 | CLI | Improved dcr create command error. |
| GG-39769 | General | Updated rocksdbjni from version 8.11.3.1 to 9.2.1.1. |

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
