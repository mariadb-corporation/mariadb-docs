---
description: >-
  GridGain 9.0.16 is a stability release that standardizes system view column
  names, adds the INDEX_COLUMNS system view, and updates DCR command syntax.
---

# GridGain 9.0.16 Release Notes

## Overview

GridGain 9.0.16 is a stability release that is dedicated to improving user experience and fixing usability issues.

## Major Changes

### DCR Syntax Changes

With this release, all [Data Center Replication](../../administrators-guide/data-center-replication/configuring-replication.md) commands are updated to consistently use the `--name` parameter to specify the replication name. Previous behavior is temporarily supported for backwards compatibility, but is deprecated and will be removed at some point later.

### Standardized System Views

Prior to this release, different system views could have slightly different names for similar columns. This release includes an extensive update for column naming scheme across system views, making system view columns more consistent.

Old system view names remain temporarily available for backwards compatibility, but are deprecated and will be removed at some point later.

Refer to the [System Views](../../administrators-guide/metrics/system-views.md) documentation for current system views. The [System View Changes in GridGain 9.0.16](#system-view-changes-in-gridgain-9016) section provides information on system view changes in this release.

## New Features

### New INDEX_COLUMNS System View

A new INDEX_COLUMNS system view allows for quick access to information about all index columns across the cluster.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-27054 | SQL | Fixed incorrect type coercion for quantify operators. |
| IGN-27046 | SQL | Fixed an issue that caused SQL ORDER BY command to return unsorted results. |
| IGN-27018 | General | Improves logging in cases of CMG disaster recovery. |
| IGN-26982 | SQL | Fixed an issue that caused sql queries to hang when using MergeJoin[type=RIGHT]. |
| IGN-26961 | General | Fixed an issue that could cause a negative error code. |
| IGN-26906 | SQL | Improved consistency of execution for single-statement scripts. |
| IGN-26897 | SQL | Names of similar columns in system views are now more consistent. |
| IGN-26848 | Platforms and Clients | Improved logging of client connections. |
| IGN-26797 | SQL | Improved error message that is sent when attempting to use unsupported SQL statements. |
| IGN-26643 | SQL | Added a new INDEX_COLUMNS system view. |
| IGN-26493 | SQL | VARBINARY and VARCHAR types now support up to 2147483648 precision. |
| GG-42391 | Cluster Data Snapshots and Recovery | Fixed an issue that prevented snapshot restoration after data rebalancing. |
| GG-42230 | Platforms & Clients | You can now use python DB API client from pip. |
| GG-42224 | CLI Tool | All DCR commands now use --name parameter to specify replication name. |
| GG-42117 | General | Default user in Docker images in now not root. |

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

In GridGain 9.0.16 we made a polishing pass on naming of system view columns. A large number of columns were renamed to improve clarity and consistency across all system views. Old column names are temporarily available for backwards compatibility, but are deprecated and will be removed in a later release.

The table below includes the changes you need to do to continue using system views:

| System View | Old Name | New Name |
|---|---|---|
| COMPUTE_TASKS | ID | COMPUTE_TASK_ID |
| COMPUTE_TASKS | STATUS | COMPUTE_TASK_STATUS |
| COMPUTE_TASKS | CREATE_TIME | COMPUTE_TASK_CREATE_TIME |
| COMPUTE_TASKS | START_TIME | COMPUTE_TASK_START_TIME |
| COMPUTE_TASKS | FINISH_TIME | COMPUTE_TASK_FINISH_TIME |
| GLOBAL_PARTITION_STATES | STATE | PARTITION_STATE |
| INDEXES | TYPE | INDEX_TYPE |
| INDEXES | IS_UNIQUE | IS_UNIQUE_INDEX |
| INDEXES | COLUMNS | INDEX_COLUMNS |
| INDEXES | STATUS | INDEX_STATE |
| LICENSES | ID | LICENSE_ID |
| LICENSES | EDITION | LICENSE_EDITION |
| LICENSES | INFOS | LICENSE_COMMON_INFO |
| LICENSES | LIMITS | LICENSE_LIMITS |
| LICENSES | FEATURES | LICENSE_FEATURES |
| LOCKS | TRANSACTION_ID | TX_ID |
| LOCKS | LOCK_MODE | MODE |
| SEQUENCES | ID | SEQUENCE_ID |
| SEQUENCES | NAME | SEQUENCE_NAME |
| SEQUENCES | DATA_TYPE | SEQUENCE_DATA_TYPE |
| SEQUENCES | INCREMENT | SEQUENCE_INCREMENT |
| SEQUENCES | MINIMUM_VALUE | SEQUENCE_MINIMUM_VALUE |
| SEQUENCES | MAXIMUM_VALUE | SEQUENCE_MAXIMUM_VALUE |
| SEQUENCES | START_VALUE | SEQUENCE_START_VALUE |
| SEQUENCES | CACHE_VALUE | SEQUENCE_CACHE_VALUE |
| SQL_QUERIES | ID | QUERY_ID |
| SQL_QUERIES | PHASE | QUERY_PHASE |
| SQL_QUERIES | TYPE | QUERY_TYPE |
| SQL_QUERIES | SCHEMA | QUERY_DEFAULT_SCHEMA |
| SQL_QUERIES | START_TIME | QUERY_START_TIME |
| SQL_QUERIES | PARENT_ID | PARENT_QUERY_ID |
| SQL_QUERIES | STATEMENT_NUM | QUERY_STATEMENT_ORDINAL |
| SYSTEM_VIEWS | ID | VIEW_ID |
| SYSTEM_VIEWS | SCHEMA | SCHEMA_NAME |
| SYSTEM_VIEWS | NAME | VIEW_NAME |
| SYSTEM_VIEWS | TYPE | VIEW_TYPE |
| SYSTEM_VIEW_COLUMNS | NAME | VIEW_NAME |
| SYSTEM_VIEW_COLUMNS | TYPE | COLUMN_TYPE |
| SYSTEM_VIEW_COLUMNS | NULLABLE | IS_NULLABLE_COLUMN |
| SYSTEM_VIEW_COLUMNS | PRECISION | COLUMN_PRECISION |
| SYSTEM_VIEW_COLUMNS | SCALE | COLUMN_SCALE |
| SYSTEM_VIEW_COLUMNS | LENGTH | COLUMN_LENGTH |
| TABLES | SCHEMA | SCHEMA_NAME |
| TABLES | NAME | TABLE_NAME |
| TABLES | ID | TABLE_ID |
| TABLES | PK_INDEX_ID | TABLE_PK_INDEX_ID |
| TABLES | COLOCATION_KEY_INDEX | TABLE_COLOCATION_COLUMNS |
| TABLES | ZONE | ZONE_NAME |
| TABLE_COLUMNS | SCHEMA | SCHEMA_NAME |
| TABLE_COLUMNS | TYPE | COLUMN_TYPE |
| TABLE_COLUMNS | NULLABLE | IS_NULLABLE_COLUMN |
| TABLE_COLUMNS | PREC | COLUMN_PRECISION |
| TABLE_COLUMNS | SCALE | COLUMN_SCALE |
| TABLE_COLUMNS | LENGTH | COLUMN_LENGTH |
| TRANSACTIONS | COORDINATOR_NODE | COORDINATOR_NODE_ID |
| TRANSACTIONS | STATE | TRANSACTION_STATE |
| TRANSACTIONS | ID | TRANSACTION_ID |
| TRANSACTIONS | START_TIME | TRANSACTION_START_TIME |
| TRANSACTIONS | TYPE | TRANSACTION_TYPE |
| TRANSACTIONS | PRIORITY | TRANSACTION_PRIORITY |
| ZONES | NAME | ZONE_NAME |
| ZONES | PARTITIONS | ZONE_PARTITIONS |
| ZONES | REPLICAS | ZONE_REPLICAS |
| ZONES | CONSISTENCY_MODE | ZONE_CONSISTENCY_MODE |

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
