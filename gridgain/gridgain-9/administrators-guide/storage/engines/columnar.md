---
description: >-
  Configure the GridGain 9 columnar storage engine for analytical queries,
  including engine and storage profile parameters.
---

# Columnar Storage

{% hint style="info" %}
Secondary storage profiles and distribution zones are only available as part of the HTAP add-on license.
{% endhint %}

## Overview

GridGain columnar storage is an LSM-tree based storage that is optimized for storing values of a single column for multiple rows. Columnar storage is always used in tandem with aipersist or aimem storage engines. Data is first written to persistent storage, and then replicated to columnar storage. Queries can be executed against the persistent storage, or against columnar storage as required.

{% hint style="warning" %}
Columnar storage only works with [aipersist](aipersist.md) storage engine.
{% endhint %}

## Columnar Storage Engine Configuration

The section below lists the configuration parameters for columnar storage engine:

```json
{
    "ignite": {
        "storage": {
            "engines": {
               "columnar": {
                 "compressingConfiguration" : {
                   "enableLz4Compression": true
                  },
                  "memtableConfiguration" : {
                    "dataRegionSize": 2147483648,
                    "memtableMaxSize": 67108864
                  },
                  "mergeTreeConfiguration": {
                    "mergeTreeFanout": 4,
                    "mergeTreeFirstLevelSize": 262144
                  },
                  "threadPoolConfiguration": {
                    "threadPoolThreadCount": 16
                  }
               }
            }
        }
    }
}
```

The table below describes columnar storage configuration parameters:

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|columnar.compressingConfiguration.enableLz4Compression|true|Defines if Lz4 compression will be used on columnar storage.|Yes|Yes|true, false|
|columnar.memtableConfiguration.dataRegionSize|2147483648|Maximum size of all memory table buffers combined.|Yes|Yes||
|columnar.memtableConfiguration.memtableMaxSize|67108864|Maximum size of a single memory table.|Yes|Yes||
|columnar.mergeTreeConfiguration.mergeTreeFanout|4|The number of times by which the tree grows with each level.|Yes|Yes||
|columnar.mergeTreeConfiguration.mergeTreeFirstLevelSize|262144|The size of entries of the first level of merge tree.|Yes|Yes||
|columnar.threadPoolConfiguration.threadPoolThreadCount|10|Columnar thread-pool size.|Yes|Yes||

## Columnar Storage Profile Configuration

Columnar storage profile only includes the name of the configuration and the engine used:

```json
{
  "ignite" : {
    "storage" : {
      "profiles" : [
        {
          "name" : "columnar_storage",
          "engine" : "columnar"
        }
      ]
    }
  }
}
```

|Property|Default|Description|Changeable|Requires Restart|Acceptable Values|
|---|---|---|---|---|---|
|name||The name of the storage profile. This name will be used to reference the profile.|Yes|Yes||
|engine||The storage engine to use. Must be `columnar` for the profile to use columnar storage.|Yes|Yes||
