# Analyzing Queries in ColumnStore

The `calGetStats()` function provides execution resource statistics for the most recent query run within the current user session. Because MariaDB ColumnStore leverages a distributed columnar architecture instead of traditional row-based indexes, evaluating these metrics helps database administrators verify the efficiency of table scans, memory cache hits, and filter performance.

## Core Query Execution Metrics

When analyzing query performance, three primary tracking values indicate how efficiently data is being isolated across the processing layers:

### Physical I/O (`PIO` / `ApproxPhyI/O`)

* Definition: The total count of 8 KB blocks read directly from physical disk subsystems or external cloud storage to satisfy the query execution plan.
* Analysis Context: High values represent a cold cache state where data blocks must be fetched from persistent storage. Successive executions of identical or overlapping query workloads should result in this metric dropping to `0` as the blocks populate the local performance memory cache.

### Logical I/O (`LIO` / `BlocksTouched`)

* Definition: The total number of logical 8 KB blocks processed during query execution, also formally known as Blocks Touched.
* Analysis Context: This value captures every block examined by the engine primitives—including blocks retrieved from memory cache pools as well as those read from disk. A disproportionately high count relative to the number of rows returned indicates that the query is evaluating wide data segments to isolate its results.

### Partition Blocks Eliminated (`PBE` / `PartitionBlocksEliminated`)

* Definition: The number of 8 KB column blocks successfully bypassed by the query processor using the metadata value ranges tracked inside the Extent Map.
* Analysis Context: ColumnStore registers minimum and maximum thresholds for every data extent to skip chunks that cannot contain records matching your `WHERE` filter parameters. A high block elimination count indicates highly optimized query targeting. If this value registers as `0` for a heavily filtered query, the engine was forced to scan every block for that column, implying the data on disk is not logically ordered or grouped by that filter criteria.

## Query Analysis Sequence

Execute the following steps within an active database session to measure baseline query I/O and verify if block elimination is occurring properly:

1.  Clear the performance cache (Optional for cold-run simulation):

    ```sql
    SELECT calFlushCache();
    ```
2.  Run the target query statement:

    ```sql
    SELECT COUNT(*), region_id FROM orders WHERE region_id = 4 GROUP BY region_id;
    ```
3.  Retrieve the metrics summary for the execution:

    ```sql
    SELECT calGetStats();
    ```

    _Example Output String:_

    Plaintext

    ```
    Query Stats: MaxMemPct-0;NumTempFiles-0;TempFileSpace-0B;ApproxPhyI/O-1931;CacheI/O-2446;BlocksTouched-2443;PartitionBlocksEliminated-48;MsgBytesIn-73KB;MsgBytesOut-1KB;Mode-Distributed
    ```
