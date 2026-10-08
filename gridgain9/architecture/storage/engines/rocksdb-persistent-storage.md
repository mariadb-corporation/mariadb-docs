---
description: >-
  Configure the experimental GridGain 9 RocksDB persistent storage engine, based
  on an LSM tree and suited to high write throughput.
---

# RocksDB Storage

RocksDB is a persistent storage engine based on LSM tree. It is best used in environments with a large number of write requests.

{% hint style="info" %}
RocksDB storage currently is considered as experimental.
{% endhint %}

## Profile Configuration

Each GridGain storage engine can have several storage profiles. Each profile has the following properties:

|Property|Default|Description|
|---|---|---|
|engine||The name of the storage engine.|
|sizeBytes|`256 * 1024 * 1024`|Sets the space allocated to the storage profile, in bytes.|
|writeBufferSizeBytes|`64 * 1024 * 1024`|Size of rocksdb write buffer.|
|numShardBits|`-1`|The cache is sharded to 2^numShardBits shards, by hash of the key.|

## Configuration Example

In GridGain 9, you can create and maintain configuration in either HOCON or JSON. The configuration file has a single root "node," called `ignite`. All configuration sections are children, grandchildren, etc., of that node. The example below shows how to configure a storage profile with RocksDB storage:

```json
{
  "ignite" : {
    "storage" : {
      "profiles" : [
        {
          "name" : "rocks_profile",
          "engine" : "rocksDb",
          "sizeBytes" : 2560000
        }
      ]
    }
  }
}
```

You can then use the profile (in this case, `rocks_profile`) in your distribution zone configuration.
