---
description: >-
  MariaDB ColumnStore hardware requirements for development and production:
  CPU cores, RAM, storage type (HDD vs SSD), filesystem and DBRoot drive
  layout, network, and bare-metal vs virtual deployment guidance.

---

# MariaDB ColumnStore Hardware Guide

## Overview

MariaDB ColumnStore is designed for analytical workloads and scales linearly with hardware resources. While the performance generally improves with more CPU cores, memory, and servers, understanding the minimum hardware specifications is crucial for successful deployment, especially in development and production environments.

MariaDB ColumnStore's performance directly benefits from additional hardware resources:

* **More CPU cores** enable greater parallel processing, improving query processing time.
* **More memory** allows for more data caching (reducing I/O), and more servers enable a larger distributed architecture.
* **HDDs vs. SSDs:** SSD[^1]s don't deliver as much benefit as you might assume because ColumnStore is optimized towards block streaming, which usually performs well enough on HDD[^2]s.
* **Bare metal vs. virtual servers:** Bare metal servers are recommended — they provide additional performance because ColumnStore can fully consume CPU cores and memory.

## Minimum Hardware Recommendations

The specifications differentiate between a basic development environment and a production-ready setup:

### **For Development Environments**

* **CPU:** A minimum of **8 CPU cores**.
* **Memory (RAM):** A minimum of **32 GB**.
* **Storage:** Local disk storage is acceptable for development purposes.

### **For Production Environments**

* **CPU:** A minimum of **64 CPU cores**.
  * This recommendation underscores the highly parallel nature of ColumnStore, which can effectively utilize a large number of cores for analytical processing.
* **Memory (RAM):** A minimum of **128 GB**.
  * Adequate memory is critical for caching data and intermediate results, directly impacting query performance.
* **Storage:** **StorageManager (S3)** is recommended.
  * This implies leveraging cloud-object storage (like AWS S3 or compatible services) for scalable and durable data persistence in production.

## Storage and Filesystem

### Filesystem Choice

A well-tuned `ext4` filesystem is comparable to ZFS for ColumnStore. Treat the choice as an operational preference — snapshots, compression, checksums, and the filesystem your team already operates confidently — rather than as a ColumnStore performance lever.

ColumnStore does not rely on the filesystem to cache its data. Reads are served from ColumnStore's own disk block cache, and direct I/O is enabled by default (`PrimitiveServers/DirectIO` is set to `y` in the shipped `Columnstore.xml`). The size of the block cache is set by `DBBC/NumBlocksPct`.

### DBRoot Drive Layout

Giving the DBRoot its own dedicated drives remains a valid recommendation, but how much it helps depends on the workload's I/O pattern.

In ColumnStore 5 and later, each node has exactly one DBRoot. These are the paths that carry ColumnStore I/O, and the `Columnstore.xml` entries that set them:

| Purpose | Default path | Configuration entry |
| --- | --- | --- |
| Column data (DBRoot) | `/var/lib/columnstore/data1` | `SystemConfig/DBRoot1` |
| Bulk-load staging | `/var/log/mariadb/columnstore/data/bulk` | `WriteEngine/BulkRoot` |
| Join and aggregation temporary files | `/tmp/columnstore_tmp_files` | `SystemConfig/SystemTempFileDir` |
| Logs | `/var/log/mariadb/columnstore` | — |

The DBRoot holds the column data and is the first path to move to dedicated storage. Separating the temporary-file and bulk-staging paths from the DBRoot keeps write-heavy bulk loads and disk-based joins from competing with column scans for the same device.

{% hint style="danger" %}
Do not point `SystemTempFileDir` at a directory that holds anything else. On start, ExeMgr deletes the entire `joins` and `aggregates` subdirectories and recreates them, to make sure no files are left behind.
{% endhint %}

### More Drives or More I/O Threads

Whether to add drives or add threads depends on whether storage is actually saturated:

* **If I/O is the bottleneck**, consider additional drives, or RAID 10.
* **If I/O is not the bottleneck**, raise the number of ColumnStore I/O threads instead, by setting `DBBC/NumThreads`.

By default, ColumnStore creates `MIN( 2 × cores , 32 )` I/O threads, taking the core count from the cgroup where one applies. Because the cap binds from 16 cores upward, a production node built to the 64-core recommendation above already runs at the 32-thread ceiling. Setting `DBBC/NumThreads` explicitly overrides that cap; valid values are `1` to `256`:

```bash
sudo mcsSetConfig DBBC NumThreads 64
```

For the other tuning variables in the same area, see [ColumnStore System Variables: Advanced Performance and Control Flow](../high-availability/optimization-and-tuning/columnstore-system-variables-advanced-performance-and-control-flow.md).

## Network Interconnectivity

Network interconnectivity plays a role for multi-server deployments.

* **Minimum Network:** A minimum of a **1 Gigabit (1G) network** is recommended.
  * This facilitates efficient data transfer between nodes via TCP/IP for replication and query processing across the distributed architecture. For optimal performance in heavy-load scenarios, higher bandwidth (for instance, 10G or more) is highly beneficial.

Adhering to these minimum specifications will provide a baseline for ColumnStore functionality. For specific workload requirements, it's always advisable to conduct performance testing and scale hardware accordingly.

## AWS Instance Sizes <a href="#aws-instance-sizes" id="aws-instance-sizes"></a>

For AWS, ColumnStore internal testing generally uses `m4.4xlarge` instance types as a cost-effective middle ground. The `R4.8xlarge` has also been tested, and performs about twice as fast for about twice the price.

## See Also

* [MariaDB ColumnStore Overview](https://mariadb.com/products/columnstore/)
* [MariaDB documentation: MariaDB ColumnStore](../)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}

[^1]: Solid state drive

[^2]: Hard disk drive
