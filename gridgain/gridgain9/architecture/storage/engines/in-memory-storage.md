---
description: >-
  Configure the GridGain 9 volatile (in-memory) storage engine, its profile
  properties, eviction settings, and Raft log storage budget.
---

# Volatile Storage

## Overview

GridGain Volatile storage is designed to provide a quick and responsive storage without guarantees of data persistence.

When it is enabled for the data region, GridGain stores all data in the data region in RAM. Data will be lost on cluster shutdown, so make sure to have a separate data region for persistent storage.

## Profile Configuration

Each GridGain storage engine can have several storage profiles. Each profile has the following properties:

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|aimem.initSizeBytes|268435456|Initial memory region size in bytes, when the used memory size exceeds this value, new chunks of memory will be allocated.|Yes|Yes|Min 256Mb, max defined by the addressable memory limit of the OS|
|aimem.maxSizeBytes|268435456|Maximum memory region size in bytes.|Yes|Yes|Min 256Mb, max defined by the addressable memory limit of the OS|
|aimem.eviction.mode|DISABLED|Eviction mode.|Yes|No|- DISABLED - Eviction is disabled.<br>- HISTORY_ONLY - Only historical versions of rows are evicted.<br>- RANDOM - Historical versions of rows are evicted first, followed by the eviction of the most recent row versions, which are chosen randomly.|
|aimem.eviction.threshold|90%|Threshold for eviction initiation. A number with a dimension identifier:<br>- % - percentage of aimem.maxSize<br>- k - Kb<br>- m - Mb<br>- g - Gb<br>For instance, "90%" means that the page memory starts eviction only after 90% of the data region is occupied.|Yes|No|- 0-100%<br>- 0-9223372036854775807k/m/g|
|aimem.eviction.lwmUpdateInterval|60000|Frequency of the low watermark update in milliseconds.|Yes|No|1 - inf|
|aimem.eviction.interval|60000|Interval between the data eviction iterations.|Yes|No|1 - inf|
|aimem.eviction.lwmThreshold|1000|If the low watermark is less than evictionLwmThreshold from the current timestamp, the row eviction is triggered.|Yes|No|0 - inf|
|aimem.eviction.batchSize|60000|Eviction batch size in rows.|Yes|No|1 - inf|

## Configuration Example

In GridGain 9, you can create and maintain configuration in either HOCON or JSON. The configuration file has a single root "node," called `ignite`. All configuration sections are children, grandchildren, etc., of that node. The example below shows how to configure one data region that uses volatile storage.

```json
{
  "ignite" : {
    "storage" : {
      "profiles" : [
        {
           "engine": "aimem",
           "name": "default_aimem",
           "eviction": {
             "batchSize": 200,
             "interval": 60000,
             "lwmThreshold": 1000,
             "lwmUpdateInterval": 60000,
             "mode": "DISABLED",
             "threshold": "90%"
           },
           "initSizeBytes": 268435456,
           "maxSizeBytes": 268435456
          }
      ]
    }
  }
}
```

You can then use the profile (in this case, `aimemory`) in your distribution zone configuration.

## Log Storage Budget

Volatile table partitions use [Raft](../../raft-consensus.md) for consensus. Each partition maintains a Raft log. You can configure the number of log entries kept in memory by allocating a _log storage budget_.

Budget types and their parameters are configured using the following properties:

|Property|Default|Description|Acceptable Values|
|---|---|---|---|
|raft.volatileRaft.logStorageBudget.name|`unlimited`|Budget type for the volatile Raft log.|- `unlimited` - all log entries are kept in memory. Nothing is ever spilled to disk.<br>- `entry-count` - caps the number of in-memory log entries at the value specified by `entriesCountLimit`. When the cap is reached and a new entry must be appended, the oldest in-memory entries are spilled to disk to make room.|
|raft.volatileRaft.logStorageBudget.entriesCountLimit||Maximum number of log entries allowed in memory at once. Only applicable to `entry-count` budget type. When the limit is reached, the oldest in-memory entries are spilled to disk into the node's work directory.|1 - inf|

### Log Storage Budget Configuration Example

```json
{
  "ignite": {
    "raft": {
      "volatileRaft": {
        "logStorageBudget": {
          "name": "unlimited"
        }
      }
    }
  }
}
```
