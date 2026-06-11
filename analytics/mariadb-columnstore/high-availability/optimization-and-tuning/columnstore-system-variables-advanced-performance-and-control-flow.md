# Columnstore System Variables: Advanced Performance and Control Flow

MariaDB ColumnStore offers a powerful set of advanced system variables designed to give administrators fine-grained control over performance, memory management, and query execution flow. While the default settings are optimized for general use, highly concurrent workloads or complex analytical queries—such as heavy aggregations and massive joins—often require specific hardware trade-offs.

The variables detailed below, typically configured within `columnstore.xml`, allow you to scale data transfer throughput, optimize disk-based operations when memory is exhausted, and implement flow control mechanisms to protect critical components like the Execution Manager (ExeMgr) from being overloaded.

## Control Flow Settings

Control Flow attempts to prevent ExeMgr facility overload. Multiple primprocs bombard the exemgr receiver queue, which utilizes parameters to enable and disable control flow. If a byte limit is hit, exemgr tells all the primprocs to slow down and queue up into a sender queue.

* `DECFlowControlEnableBytesThresh`: Controls how soon the sender queue is enabled. A smaller value means it is enabled sooner, preventing exemgr from overflowing by routing jobs slower via the sender queue. The default is `50000000`.
* `DECFlowControlDisableBytesThresh`: Acts as the threshold to disable flow control. The default is `10000000`.
* `BPPSendThreadBytesThresh`: Affects the depth of the sender queue in bytes. The default is `250000000`.
* `BPPSendThreadMsgThresh`: Affects the depth of the queue by message threshold. The default is `100`.

## Connection and Threading Variables

*   `ConnectionsPerPrimProc`: Connections to primproc can be increased via columnstore.xml to scale the throughput of data transfer. This is particularly useful for heavy group bys that send lots of original data to exemgr. The default is `2`.

    ```bash
    sudo mcsSetConfig PrimitiveServers ConnectionsPerPrimProc 4
    ```
* `ThreadPoolSize`: Specifies the size of the UM processing thread pool where all UM-based algorithms spawn threads.
* `NumThreads`: Increases the number of parallel reading threads to utilize full disk capacity. The default is `MIN( # of cores , 32 )`.
* `NumCores`: Specifies how many parallel threads will be spawned by different parts of the Hash Join algorithm running in UM. The default is the number of cores in the system or in the cgroup assigned.
* `ProcessorThreadsPerScan`: The number of jobs issued to process each extent. Increasing this will utilize more CPU. The default is `16`.

## Memory and Cache Settings

* `NumBlocksPct`: Specifies the percentage of physical memory to utilize for disk block caching. The sum of NumBlocksPct and TotalUmMemory should typically not exceed 75% of physical memory. The default is `50`.
* `TotalUmMemory`: Specifies the percentage of physical memory to utilize for joins, intermediate results, and set operations. The default is 25%.
* `MemoryCheckPercent`: The max real memory to limit the growth of buffers to, after which the system will self-shut down. The default is `95`.
* `NumCaches`: The number of concurrent query caches used by PM to reduce contention accessing block cache resources. The default is `1`.

## Disk-Based Operation Variables

* `columnstore_diskjoin_bucketsize`: Roughly the size of a file to be stored on disk when doing a disk-based join. The default is roughly 100MB. Using an SSD or NVME for the temp directory can allow for a 2x or 3x increase to speed up joins.
* `AllowDiskBasedJoin`: Controls the option to use disk-based joins. Enabling this allows for larger joins by leveraging `/tmp/columnstore_tmp_files/aggregates/` instead of exhausting memory. The default is `N`.
* `AllowDiskBasedAggregation`: Enables queries to use disk for intermediate data when the memory needed for the aggregation exceeds the memory limit on the server, allowing the query to complete without an IDB-2001 error. The default is `N`.

## Job and System Request Variables

* `RequestSize`: Controls the number of extents retrieved per request/job. Increasing the `RequestSize` means each thread handles more work per job, improving overall throughput by achieving higher concurrency. The default is `1`.
* `MaxOutstandingRequests`: The number of outstanding request messages sent by UM to PMs, with every message processing up a multiple of 8192 records. The default is `20`.
* `SystemConfig.DBRMSnapshotInterval`: Controls how often workernode@1 calls `saveState()` to store a copy of the Extent Map. Setting this value to something small implicitly affects `do_confirm()` , which is called synchronously on every Extent Map change and blocks all writes whilst it is working. The default is `100000`.
