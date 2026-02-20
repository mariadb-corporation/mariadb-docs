# Performance Related Configuration Settings

A number of system configuration variables exist to allow fine tuning of the system to suit the physical hardware and query characteristics. In general the default values will work relatively well for many cases.

The configuration parameters are maintained in the `/etc/Columnstore.xml` file. In a multiple server deployment these should only be edited on the PM1 server as this will be automatically replicated to other servers by the system. A system restart will be required for the configuration change to take affect.

Convenience utility programs _getConfig_ and _setConfig_ are available to safely update the Columnstore.xml without needing to be comfortable with editing XML files. The -h argument will display usage information.

## Memory Management

### NumBlocksPct

{% tabs %}
{% tab title="Current" %}
The `NumBlocksPct` configuration parameter specifies the percentage of physical memory to utilize for disk block caching. The default value is 25, to ensure enough physical memory.
{% endtab %}

{% tab title="< 23.10" %}
The `NumBlocksPct` configuration parameter specifies the percentage of physical memory to utilize for disk block caching. The default value is 50, to ensure enough physical memory.
{% endtab %}
{% endtabs %}

### TotalUmMemory

{% tabs %}
{% tab title="Current" %}
The `TotalUmMemory` configuration parameter specifies the percentage of physical memory to utilize for joins, intermediate results and set operations. This specifies an upper limit for small table results in joins rather than a pre-allocation of memory. The default value is 50.
{% endtab %}

{% tab title="< 23.10" %}
The `TotalUmMemory` configuration parameter specifies the percentage of physical memory to utilize for joins, intermediate results and set operations. This specifies an upper limit for small table results in joins rather than a pre-allocation of memory. The default value is 25.
{% endtab %}
{% endtabs %}

### Memory Requirements

In a single server or combined deployment, the sum of `NumBlocksPct` and `TotalUmMemory` should typically not exceed 75% of physical memory. With very large memory servers this could be raised but the key point is to leave enough memory for other processes including `mariadbd`.

{% hint style="info" %}
From version 1.2.2, these can be set to static numeric limits instead of percentages by entering a number with 'M' or 'G' at the end to signify MiB or GiB.
{% endhint %}

### InnoDB Buffer Pool Sizing with ColumnStore

When a MariaDB server runs both ColumnStore and InnoDB engines, the traditional rule of dedicating 75-80% of total RAM to the `innodb_buffer_pool_size` is outdated and can trigger the Linux Out-Of-Memory (OOM) killer.

By default, ColumnStore utilizes 75% of the system's available RAM (50% for `NumBlocksPct` and 25% for `TotalUmMemory`). You must ensure that the combined memory allocated to ColumnStore and InnoDB does not exceed your system's total memory, leaving adequate room for the operating system and other overhead.

**Example Sizing (256GB RAM Server):**

* **Total RAM:** 256GB
* **ColumnStore Allocation:** \~192GB (75% default)
* **Remaining RAM:** 64GB

In this scenario, you should set `innodb_buffer_pool_size` to **32GB**, leaving the remaining **32GB** for the OS and other system overhead.

**Validation:** To prevent OOM issues, you must validate that the total memory allocation is less than the memory available to the machine. Verify that the sum of the following configurations is strictly less than your total server memory (checked via `free -g`):

* `HashJoin TotalUmMemory` (checked via `mcsGetConfig`)
* `DBBC NumBlocksPct` (checked via `mcsGetConfig`)
* `innodb_buffer_pool_size` (checked via `mariadb -e "show variables like '%innodb_buffer_pool_size%'"`)

## Query Concurrency - MaxOutstandingRequests

ColumnStore handles concurrent query execution by managing the rate of concurrent batch primitive steps. This is configured using the _MaxOutstandingRequests_ parameter and has a default value of 20. Each batch primitive step is executed within the context of 1 extent column according to this high level process:

* ColumnStore issues up to MaxOutstandingRequests number of batch primitive steps.
* PrimProc processes the request, using many threads and returns its response. These generally take a fraction of a second up to a low number of seconds depending on the amount of Physical I/O and the performance of that storage.
* ColumnStore issues new requests as prior requests complete maintaining the maximum number of outstanding requests.

This scheme allows for large queries to use all available resources when not otherwise being consumed and for smaller queries to execute with minimal delay. Lower values optimize for higher throughput of smaller queries while a larger value optimizes for response time of that query. The default value should work well under most circumstances however the value should be increased as the number of nodes is increased.

How many Queries are running and how many queries are currently in the queue can be checked with

```sql
SELECT calgetsqlcount();
```

## Join Tuning - PmMaxMemorySmallSide

ColumnStore maintains statistics for table and utilizes this to determine which is the larger table of the two. This is based both on the number of blocks in that table and estimation of the predicate cardinality. The first step is to apply any filters as appropriate to the smaller table and returning this data set to memory. The size of this data set is compared against the configuration parameter _`PmMaxMemorySmallSide`_ which has a default value of 64 (MB). This value can be set all the way up to 4GB. This default allows for approximately 1M rows on the small table side to be joined against billions (or trillions) on the large table side. If the size of the small data set is less than _PmMaxMemorySmallSide_ the dataset is sent to PrimProc for creation of a distributed hashmap. Thus this setting is important to tuning of joins and whether the operation can be distributed or not. This should be set to support your largest expected small table join size up to available memory:

* Although this will increase the size of data between nodes to support the join, it means that the join and subsequent aggregates are pushed down, scaled out, and a smaller data set is returned back.
* In a multiple server deployment, the sizing should be based from available physical memory on the servers, how much memory to reserve for block caching, and the number of simultaneous join operations that can be expected to run times the average small table join data size.

### Multi-Table Join Tuning

The above logic for a single table join extrapolates out to multi table joins where the small table values are precalculated and performed as one single scan against the large table. This works well for the typical star schema case joining multiple dimension tables with a large fact table. For some join scenarios it may be necessary to sequence joins to create the intermediate datasets for joining, this would happen for instance with a snowflake schema structure. In some extreme cases it may be hard for the optimizer to be able to determine the most optimal join path. In this case a hint is available to force a join ordering. The `INFINIDB_ORDERED` hint will force the first table in the from clause to be considered the largest table and override any statistics based decision, for example:

```sql
SELECT /*! INFINIDB_ORDERED */ r_regionkey     
FROM region r, customer c, nation n    
WHERE r.r_regionkey = n.n_regionkey      
AND n.n_nationkey = c.c_nationkey
```

{% hint style="danger" %}
Note: `INFINIDB\_ORDERED` is deprecated and does not work anymore for ColumnStore 1.2 and above.
{% endhint %}

use `set infinidb_ordered_only=ON;`

and for 1.4 `set columnstore_ordered_only=ON;`

### Disk-Based Joins - AllowDiskBasedJoin

When a join is very large and exceeds the _`PmMaxMemorySmallSide`_ setting, it is performed in memory. For very large joins, this could exceed the available memory, in which case this is detected and a query error reported. Several configuration parameters are available to enable and configure usage of disk overflow should this occur:

* AllowDiskBasedJoin – Controls the option to use disk Based joins or not. Valid values are Y (enabled) or N (disabled). By default, this option is disabled.
* TempFileCompression – Controls whether the disk join files are compressed or noncompressed. Valid values are `Y` (use compressed files) or `N` (use non-compressed files).
* TempFilePath – The directory path used for the disk joins. By default, this path is the tmp directory for your installation (i.e., `/tmp/columnstore_tmp_files/`). Files (named `infinidb-join-data*`) in this directory will be created and cleaned on an as-needed basis. The entire directory is removed and recreated by `ExeMgr` at startup. It is strongly recommended that this directory be stored on a dedicated partition.

A MariaDB global or session variable is available to specify a memory limit at which point the query is switched over to disk-based joins:

* `infinidb_um_mem_limit` - Memory limit in MB per user (i.e., switch to disk-based join if this limit is exceeded). By default, this limit is not set (value of 0).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
