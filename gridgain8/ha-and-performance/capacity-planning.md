---
description: >-
  Techniques for planning and identifying the minimum hardware requirements for a
  GridGain deployment, covering memory, heap, compute, and disk usage.
---

# Capacity Planning

Techniques that can help plan and identify the minimum hardware requirements for a given deployment.

## Overview

When preparing and planning for a system, capacity planning is an integral part of the design. Understanding the memory footprint of the cache will help you decide how much physical memory, how many JVMs, and how many CPUs and servers will be required. In this section we discuss various techniques that can help you plan and identify the minimum hardware requirements for a given deployment.

## Calculating Memory Usage

- Calculate primary data size: multiply the size of one entry in bytes by the total number of entries.
- Multiply that by the number of backups, if you have any.
- Indexes also require memory. Basic use cases will add a 30% increase.
- Add around 20MB per cache. This value can be reduced if you explicitly set `IgniteSystemProperties.IGNITE_ATOMIC_CACHE_DELETE_HISTORY_SIZE` to a smaller value than the default.
- Add around 200-300MB per node for internal memory and reasonable amount of memory for JVM and GC to operate efficiently.

{% hint style="info" %}
Apache Ignite will typically add around 200 bytes overhead to each entry.
{% endhint %}

### Memory Capacity Planning Example

Let's use the following scenario as an example:

{% hint style="info" %}
**Example Specification**

- 2,000,000 objects
- 1,024 bytes per object (1 KB)
- 1 backup
- 4 nodes
{% endhint %}

- Total number of objects X object size X 2 (one primary and one backup copy for each object):

  2,000,000 x 1,024 x 2 = 4,096,000,000 bytes

- Considering indexes:

  4,096,000,000 + (4,096,000,000 x 30%) = 5,078 MB

- Approximate additional memory required by the platform:

  300 MB x 4 = 1,200 MB

- Total size:

  5,078 + 1,200 = 6,278 MB

Hence the anticipated total memory consumption would be just over ~6 GB.

## Calculating Heap Usage

RAM required by GridGain can be significantly different depending on the way you use it. It is hard to calculate specific requirements for your specific set up, but here are basic guidelines:

- Compute tasks will use the amount of heap required to execute the task. The sizing in this case will heavily depend of what your code needs.
- SQL workload will use as much RAM as necessary for heap. It is recommended to set [SQL memory quotas](performance-tuning/sql-memory-management.md) to limit how much memory SQL uses to fit your environment.
- GridGain may work with concurrent queries and tasks. If your configuration uses concurrency, make sure your environment has sufficient space to handle all the tasks being worked on.
- Other workloads typically have a smaller impact on heap usage.
- Large clusters (either in the number of nodes, or in the number of cashes and partitions) will use up more RAM than a smaller cluster, due to using RAM to manage the cluster. If you worry about the impact, use [group caches](https://www.gridgain.com/docs/latest/developers-guide/configuring-caches/cache-groups) and reduce the number of partitions in your clusters.
- Storing large objects may require additional heap, as copies of the objects will be created on the heap during some processes.
- Apart from RAM used for heap and off-heap storage, a small amount of RAM is also utilized by GridGain for its own operations. On average, this will require less space than heap storage.

## Calculating Compute Usage

Calculating compute is generally much harder to estimate without some code already in place.
It is important to understand the cost of a given operation that your application will be performing and multiply this by the number of operations expected at various times.

Published throughput figures are a poor substitute for your own measurements.
Throughput depends on the data model, the mix of operations, the backup and persistence configuration, and the hardware.
Benchmark a multi-node cluster with your own workload and data, on hardware that matches your target deployment, and derive the per-operation cost from those measurements.
See [Performance and Tuning](performance-tuning/general-tips.md) for the practices to apply while benchmarking.

## Calculating Disk Space Usage

When you have [Native Persistence](../architecture/storage/native-persistence.md) enabled, you need to provide enough disk space for each node to accommodate the data required for proper operation. The data includes your application data converted to Ignite's internal format plus auxiliary data such as indexes, WAL files, etc.

The total amount of the required space can be estimated as follows (for [partitioned caches](../architecture/data-modeling/data-partitioning.md)):

- The size of your data when loaded into Ignite (the total amount, it will be distributed among the nodes depending on your cache configuration). Refer to the [Empirical Estimation of Disk Capacity Usage page](disk-capacity-estimation.md) for information on how to get an estimate of the data size. If [backups](../architecture/data-modeling/data-partitioning.md#backup-partitions) are enabled, the backup partitions will take as much space as the total amount of data, so multiply this value by `number of backups + 1`. Divide the resulting number by the number of nodes to get an approximate per node value.
- WAL size per node (10 segments * segment size; defaults to 640 MB).
- [WAL Archive](../architecture/storage/native-persistence.md#write-ahead-log-wal) size per node (either the configured value or 4 times the checkpointing buffer size). See the [Write-Ahead Log page](../architecture/storage/native-persistence.md) for details.

The following table displays how the default maximum WAL archive size is calculated depending on the available RAM (provided that no settings are specified for the data region size, checkpointing buffer size, and WAL archive size). These are the values per node.

| RAM < 5GB | 5GB ≤ RAM < 40GB | RAM > 40GB |
|---|---|---|
| 4 x MIN(RAM/5, 256MB) | RAM / 5 | 8GB |

### Disk Space Usage Example

Let's say you have 300GB of data and plan to have 10 servers with 16GB of RAM each. You enabled persistence and chose to have 2 backup copies.

Let's assume that empirical estimation shows that the total amount of data is 3 times the initial size. The total size of the data loaded in Ignite per node is:

| Metric | Value |
|---|---|
| Data size in Ignite | 180 GB |
| WAL | 640 MB |
| WAL archive | 3.1 GB |
| Size per node | ~ 183.8 GB |

{% hint style="info" %}
Use the spreadsheet to estimate how many servers with a predefined configuration you may need in your cluster.
{% endhint %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
