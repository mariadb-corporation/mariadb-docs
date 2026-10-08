---
description: >-
  Advanced MariaDB ColumnStore system variables in Columnstore.xml for tuning
  control flow, connections and threading, memory and cache, disk-based
  operations, and job and system requests.
---

# ColumnStore System Variables: Advanced Performance and Control Flow

MariaDB ColumnStore offers a powerful set of advanced system variables designed to give administrators fine-grained control over performance, memory management, and query execution flow. While the default settings are optimized for general use, highly concurrent workloads or complex analytical queries—such as heavy aggregations and massive joins—often require specific hardware trade-offs.

The variables detailed below, configured in `Columnstore.xml`, allow you to scale data transfer throughput, optimize disk-based operations when memory is exhausted, and implement flow control mechanisms to protect critical components like the Execution Manager (ExeMgr) from being overloaded.

`Columnstore.xml` groups variables into sections, and some variable names appear in more than one section with different effects. Each entry below names its section. Pass the section and the variable name to `mcsGetConfig` and `mcsSetConfig`:

```bash
sudo mcsGetConfig <section> <variable>
sudo mcsSetConfig <section> <variable> <value>
```

## Control Flow Settings

Control Flow attempts to prevent ExeMgr facility overload. Multiple primprocs bombard the exemgr receiver queue, which utilizes parameters to enable and disable control flow. If a byte limit is hit, exemgr tells all the primprocs to slow down and queue up into a sender queue.

These variables belong to the `FlowControl` section. The shipped `Columnstore.xml` has no `FlowControl` section; `mcsSetConfig` creates it when you set the first variable.

* `DECFlowControlEnableBytesThresh`: Controls how soon the sender queue is enabled. A smaller value means it is enabled sooner, preventing exemgr from overflowing by routing jobs slower via the sender queue. The default is `50000000`.
* `DECFlowControlDisableBytesThresh`: Acts as the threshold to disable flow control. The default is `10000000`.
* `BPPSendThreadBytesThresh`: Affects the depth of the sender queue in bytes. The default is `250000000`.
* `BPPSendThreadMsgThresh`: Affects the depth of the queue by message threshold. The default is `100`.

{% hint style="warning" %}
Setting `DECFlowControlEnableBytesThresh` has no effect: ColumnStore always uses the default of `50000000`. The other three flow-control variables work as described.
{% endhint %}

## Connection and Threading Variables

*   `ConnectionsPerPrimProc` (in the `PrimitiveServers` section): Connections to primproc can be increased via columnstore.xml to scale the throughput of data transfer. This is particularly useful for heavy group bys that send lots of original data to exemgr. The default is `2`.

    ```bash
    sudo mcsSetConfig PrimitiveServers ConnectionsPerPrimProc 4
    ```
* `ThreadPoolSize` (in the `JobList` section): Specifies the size of the UM processing thread pool where all UM-based algorithms spawn threads. The default is `1000`, as set in the shipped `Columnstore.xml`; if you remove the entry, ColumnStore uses `100`. Don't confuse it with `ThreadPoolSize` in the `ExeMgr1` section, which sets the number of ExeMgr server threads.
* `NumThreads` (in the `DBBC` section): Sets the number of I/O threads that read disk blocks into the block cache. Increase it to make fuller use of disk capacity. The default is `MIN( 2 × cores , 32 )`, taking the core count from the cgroup where one applies. Valid values are `1` to `256`; setting the variable explicitly overrides the 32-thread cap.
* `NumCores` (in the `JobList` section): Sets the core count that the UM uses to size its threads: the number of Hash Join threads and scan-receive threads, and the default number of row-aggregation and window-function threads. The default is the number of cores in the system or in the cgroup assigned. To change only the number of Hash Join threads, set `NumThreads` in the `HashJoin` section instead.
*   `NumCores` (in the `PrimitiveServers` section): Sets the core count that PrimProc uses to size its threads: the number of threads that process primitive jobs (`2 × cores`) and the default number of I/O threads (`NumThreads` in the `DBBC` section). The default is the number of cores in the system or in the cgroup assigned.

    {% hint style="info" %}
    The two `NumCores` variables are independent. Setting `NumCores` in the `PrimitiveServers` section doesn't change the number of Hash Join threads; it changes the number of PrimProc I/O and primitive-job threads.
    {% endhint %}
* `ProcessorThreadsPerScan` (in the `JobList` section): The number of jobs issued to process each extent. Increasing this will utilize more CPU. The default is `16`.

## Memory and Cache Settings

*   `NumBlocksPct` (in the `DBBC` section): Sets the size of the disk block cache as a percentage of physical memory. To set an absolute size instead, add a size suffix such as `m` (megabytes) or `g` (gigabytes), for example `16g`. The default is `20`, as set in the shipped `Columnstore.xml`; if you remove the entry, ColumnStore uses `70`. Leave enough memory for `TotalUmMemory`, `mariadbd`, and the operating system.

    ```bash
    sudo mcsSetConfig DBBC NumBlocksPct 30
    ```
* `TotalUmMemory` (in the `HashJoin` section): Specifies the percentage of physical memory to utilize for joins, intermediate results, and set operations. The default is `65%`.
* `MemoryCheckPercent` (in the `SystemConfig` section): The max real memory to limit the growth of buffers to, after which the system will self-shut down. The default is `95`.
* `NumCaches` (in the `DBBC` section): The number of concurrent query caches used by PM to reduce contention accessing block cache resources. The default is `1`.

{% hint style="info" %}
ColumnStore 23.10.4 changed the shipped defaults of `NumBlocksPct` from `50` to `20` and `TotalUmMemory` from `25%` to `65%`. An upgrade keeps your existing `Columnstore.xml`, so a system upgraded from an earlier version keeps its previous values.
{% endhint %}

## Disk-Based Operation Variables

* `columnstore_diskjoin_bucketsize` (a MariaDB Server system variable, not a `Columnstore.xml` setting; set it with `SET`): Roughly the size of a file to be stored on disk when doing a disk-based join. The default is roughly 100MB. Using an SSD or NVME for the temp directory can allow for a 2x or 3x increase to speed up joins.
* `AllowDiskBasedJoin` (in the `HashJoin` section): Controls the option to use disk-based joins. Enabling this allows for larger joins by leveraging `/tmp/columnstore_tmp_files/joins/` (or the `joins/` subdirectory of `SystemTempFileDir` in the `SystemConfig` section, if set) instead of exhausting memory. The default is `N`.
* `AllowDiskBasedAggregation` (in the `RowAggregation` section): Enables queries to use disk for intermediate data when the memory needed for the aggregation exceeds the memory limit on the server, allowing the query to complete without an IDB-2001 error. The default is `N`.

## Job and System Request Variables

* `RequestSize` (in the `JobList` section): Controls the number of extents retrieved per request/job. Increasing the `RequestSize` means each thread handles more work per job, improving overall throughput by achieving higher concurrency. The default is `1`.
* `MaxOutstandingRequests` (in the `JobList` section): The number of outstanding request messages sent by UM to PMs, with every message processing up a multiple of 8192 records. The default is `20000`, as set in the shipped `Columnstore.xml`; if you remove the entry, ColumnStore calculates a value from the number of PMs and cores, with a minimum of `20`.
* `DBRMSnapshotInterval` (in the `SystemConfig` section): Controls how often workernode@1 calls `saveState()` to store a copy of the Extent Map. Setting this value to something small implicitly affects `do_confirm()` , which is called synchronously on every Extent Map change and blocks all writes whilst it is working. The default is `100000`.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
