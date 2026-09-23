---
description: >-
  GridGain 9.0.14 introduces the Python DB API driver, point-in-time recovery,
  new transaction timeout parameters, and improved DDL performance.
---

# GridGain 9.0.14 Release Notes

## Overview

GridGain 9.0.14 is a release that brings a large number of new features and several major behavior changes.

## New Features

### Python DB API Driver

This release introduces Python DB API Driver that can be used to work with GridGain database from Python. The DB API Driver uses the [Python Database API](https://peps.python.org/pep-0249/) to establish connection to a GridGain cluster and work with it.

The driver is available from pip:

```bash
pip install pygridgaindbapi
```

Once installed, you can establish connection and work with your cluster, for example:

```python
addr =['127.0.0.1:10800']
conn = pygridgain_dbapi.connect(address=addr, timeout=1)
cursor = conn.cursor()
cursor.execute('CREATE TABLE Person(id int primary key, name varchar, age int)')
```

For more information on using Python DB API, see the [Python Database API Driver](../../developers-guide/clients/python.md) section.

### Point in Time Recovery

With this release, you can restore data to any point in time above the [low watermark](../../administrators-guide/storage/data-partitions.md#version-storage). Older data below the low watermark can be restored by using [snapshots](../../administrators-guide/snapshots/snapshots-and-recovery.md).

To start point in time recovery, use the `recovery` command, for example:

```bash
recovery tables start --tables Person,PUBLIC.Accounts --timestamp 2024-09-10T10:53:00+01:00
```

### New Transaction Timeout Parameters

New `readOnlyTimeout` and `readWriteTimeout` transaction timeout parameters can be used to fine-tune maximum transaction times individually for read only and read-write transactions on your cluster.

### Improved DDL Performance

This release features significant improvement in performance of DDL commands. These commands are now implicitly batched where possible, significantly speeding up database set up.

### New Privileges

This release expands support for fine-tuned user access control, with new roles for controlling what users can cancel jobs, queries and transactions, as well as improved control over permissions over point in time recovery.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-26733 | CLI Tool | CLI in docker now uses UTF-8 encoding. |
| IGN-26669 | Platforms and Clients | .NET: Fixed read-only transaction timestamp propagation. |
| IGN-26652 | General | Improved error message on request timeout. |
| IGN-26581 | General | New transaction parameters were added to manage transaction timeouts. |
| IGN-26492 | SQL | Fixed an issue that allowed creating VARCHAR fields larger than 65536 characters. |
| IGN-26491 | SQL | Fixed an issue that allowed inserting too long values into VARBINARY fields while truncating length. |
| IGN-25697 | General | Improved logging during node startup. |
| IGN-25658 | General | Cluster and node configurations no longer allow duplicate keys. |
| IGN-24824 | SQL | Improved performance of DDL queries. |
| IGN-24728 | SQL | Fixed an issue with incorrect log10 calculation in SQL. |
| GG-41896 | Migration Tools | Fixed an issue that prevented DCR from working for tables with lower-case names. |
| GG-41853 | Cluster SQL Engine | Fixed an issue when caches were referred to as tables in error messages. |
| GG-40963 | Cluster SQL Engine | New privileges were added for managing user permissions for stopping transactions, queries and jobs. |
| GG-40659 | Cluster SQL Engine | Improved SQL error message consistency. |
| GG-40497 | Cluster Data Snapshots and Recovery | New permissions were added for managing what users can perform PITR operations. |
| GG-36930 | Cluster Security | Snapshot management now correctly checks for permissions. |

## Known Limitations

### Data Center Replication with Multiple Data Centers

Complex Data Center Replication topologies (for example, the ones involving cycles) of 3 or more data centers are not supported. This will be addressed in an upcoming release.

### GridGain 8 Features

The following features of GridGain 8 are not available in this version, and will be added in upcoming versions:

- Rack-Awareness
- Tracing
- Service Grid

### SQL Performance in Complex Scenarios

There are known issues with the performance of SQL read-write transactions in complex read-write scenarios. These issues will be addressed in an upcoming release.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
