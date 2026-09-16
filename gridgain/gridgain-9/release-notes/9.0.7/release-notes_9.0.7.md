---
description: >-
  GridGain 9.0.7 limits implicit SQL type casting and adds fair partition
  distribution, selective CSV import, and license monitoring.
---

# GridGain 9.0.7 Release Notes

## Overview

GridGain 9.0.7 includes a number of new features improving performance and stability.

## Major Changes

### Limited Implicit SQL Type Casting

Starting with this release, implicit type casting in SQL is limited to within the same type family. The following conversions are available:

| Type Family | Available Types |
|---|---|
| Boolean | `BOOLEAN` |
| Numeric | `TINYINT`, `SMALLINT`, `INT`, `BIGINT`, `DECIMAL`, `FLOAT`, `DOUBLE` |
| Character String | `VARCHAR`, `CHAR` |
| Binary String | `VARBINARY` `BINARY` |
| Date | `DATE` |
| Time | `TIME` |
| Datetime | `TIMESTAMP`, `TIMESTAMP WITH LOCAL TIME ZONE` |
| UUID | `UUID` |

### Fair Partition Distribution

Starting with this release, GridGain 9 will use fair distribution algorithm for partition allocation. This change provides more even data distribution across the cluster and less partition reallocation, especially when the low number of partitions is used.

As part of this change, default partition count is now calculated dynamically based on the number of nodes in the cluster and replica factor. The formula for the calculation is: `(dataNodesCount * coresOnNode * 2) / replicaFactor`.

### ZIP Installation Console Log

Starting with this release, ZIP installation of GridGain 9 provides log output to console in addition to writing it to the log file. This behavior can be configured in the *etc/gridgain.java.util.logging.properties* file by removing java.util.logging.ConsoleHandler or `java.util.logging.ConsoleHandler, java.util.logging.FileHandler` log handler.

## New Features

### Selective Import From CSV

In this release, a new option is added that allows you to import only some columns from a CSV file. The command behavior depends on if the CSV file has headers or not.

- If there is a header, CSV columns will be mapped to table columns with the same name, for example:

  ```sql
  /* Import data from CSV with column headers */
  COPY FROM '/path/to/dir/data.csv'
  INTO Table1 (name, age)
  FORMAT CSV
  ```

- If there is no header, CSV columns will be mapped to table columns from the start. In the example below, only the first two CSV columns will be imported and mapped to `name` and `age` columns:

  ```sql
  /* Import data from CSV without column headers  */
  COPY FROM '/path/to/dir/data.csv'
  INTO Table1 (name, age)
  ```

### License Monitoring

A number of features were added to improve license monitoring in this release.

- New license events can track when the license is applied or expires, or when actions violating the license are attempted.
- Available license features can now be tracked via REST at the new `/management/v1/license` endpoint.
- License system view now includes license edition.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-25554 | CLI Tool | Fixed an issue with connect command failing when executed outside of REPL mode. |
| IGN-25539 | CLI Tool | Improved error message for invalid configuration. |
| IGN-25401 | SQL | You can now specify default value for columns with UUID data type. |
| IGN-25370 | SQL | Implicit data type casting between different data type families is now prohibited. |
| IGN-25169 | General | Improved RAFT log performance. |
| IGN-25108 | General | CMG nodes now handle network messages in a separate thread pool. |
| GG-40657 | Licenses | Added EDITION field to license system view. |
| GG-40541 | Cluster Data Snapshots and Recovery | Incremental snapshot restoration now uses correct timestamp if data was updated multiple times between snapshots. |
| GG-40507 | Cluster Affinity and Baseline Topology | Optimal number of partitions is now automatically calculated for newly created distribution zones, if not specified. |
| GG-40500 | Cluster Affinity and Baseline Topology | Added fair distribution algorithm. |
| GG-40413 | Cluster Security | Added new authentication thread pool configuration parameters. |
| GG-39873 | Licenses | Added a new /management/v1/license endpoint that can be used to check available features. |
| GG-39822 | Licenses | Added license-related events. |
| GG-39753 | CLI Tool | You can now select which columns to import from CSV files when using COPY INTO command. |
| GG-39602 | CLI Tool | User now gets disconnected when their password changes. |
| GG-39457 | Cluster Data Snapshots and Recovery | Incremental snapshots now support schema changes between snapshots. |

## Known Limitations

### Delay on DDL Requests

DDL requests, such as `CREATE TABLE`, take a few seconds each to complete. Because of that, large database initialization scripts may take longer than expected. This will be addressed in an upcoming release.

### Performance of GridGain 8 Applications

Some scenarios may see lower performance when moving to GridGain 9. This is a temporary limitation, and the performance in these scenarios will be improved in upcoming versions.

### High-Availability with Two Data Copies

When a partition loses majority of its copies, it becomes unavailable. This behavior is required for split-brain protection. Because of this, in a distribution zone with 2 data replicas, losing one node may lead to partial unavailability.

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
