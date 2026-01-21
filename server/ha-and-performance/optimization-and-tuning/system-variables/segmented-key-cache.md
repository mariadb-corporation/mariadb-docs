# Segmented Key Cache

## About Segmented Key Cache

A segmented key cache is a collection of structures for regular [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) key caches called key cache segments. Segmented key caches mitigate one of the major problems of the simple key cache: thread contention for key cache lock (mutex). With regular key caches, every call of a key cache interface function must acquire this lock. So threads compete for this lock even in the case when they have acquired shared locks for the file and the pages they want to read from are in the key cache buffers.

When working with a segmented key cache any key cache interface function that needs only one page has to acquire the key cache lock only for the segment the page is assigned to. This makes the chances\
for threads not having to compete for the same key cache lock better.

Any page from a file can be placed into a buffer of only one segment. The number of the segment is calculated from the file number and the position of the page in the file, and it's always the same for the\
page. Pages are evenly distributed among segments.

The idea and the original code of the segmented key cache was provided by Fredrik Nylander from Stardoll.com. The code was extensively reworked, improved, and eventually merged into MariaDB by Igor Babaev from Monty Program (now MariaDB Corporation).

You can find some benchmark results comparing various settings on the [Segmented Key Cache Performance](/broken/spaces/WCInJQ9cmGjq1lsTG91E/pages/ySaANiCpRqROWwoll9yo) page.

## Segmented Key Cache Syntax

New global variable: [key\_cache\_segments](../../../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_cache_segments). This variable sets the number of segments in a key cache. Valid values for this variable are whole numbers between `0` and `64`. If the number of segments is set to a number greater than `64` the number of segments will be truncated to 64 and a warning will be issued. A value of `0` means the key cache is a regular (i.e. non-segmented)\
key cache. This is the default. If `key_cache_segments` is`1` (or higher) then the new key cache segmentation code is used. In practice there is no practical use of a single-segment segmented key cache except for testing purposes, and setting`key_cache_segments = 1` should be slower than any other option and should not be used in production.

Other global variables used when working with regular key caches also\
apply to segmented key caches: [key\_buffer\_size](../../../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size),[key\_cache\_age\_threshold](../../../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_cache_age_threshold), [key\_cache\_block\_size](../../../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_cache_block_size), and [key\_cache\_division\_limit](../../../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_cache_division_limit).

## Segmented Key Cache Statistics

Statistics about the key cache can be found by looking at the [KEY\_CACHES](../../../reference/system-tables/information-schema/information-schema-tables/information-schema-key_caches-table.md) table in the [INFORMATION\_SCHEMA](../../../reference/system-tables/information-schema/) database. Columns in this table are:

| Column Name      | Description                                                                                                                     |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| KEY\_CACHE\_NAME | The name of the key cache                                                                                                       |
| SEGMENTS         | total number of segments (set to NULL for regular key caches)                                                                   |
| SEGMENT\_NUMBER  | segment number (set to NULL for any regular key caches and for rows containing aggregation statistics for segmented key caches) |
| FULL\_SIZE       | memory for cache buffers/auxiliary structures                                                                                   |
| BLOCK\_SIZE      | size of the blocks                                                                                                              |
| USED\_BLOCKS     | number of currently used blocks                                                                                                 |
| UNUSED\_BLOCKS   | number of currently unused blocks                                                                                               |
| DIRTY\_BLOCKS    | number of currently dirty blocks                                                                                                |
| READ\_REQUESTS   | number of read requests                                                                                                         |
| READS            | number of actual reads from files into buffers                                                                                  |
| WRITE\_REQUESTS  | number of write requests                                                                                                        |
| WRITES           | number of actual writes from buffers into files                                                                                 |

## See Also

* [Segmented Key Cache Performance](/broken/spaces/WCInJQ9cmGjq1lsTG91E/pages/ySaANiCpRqROWwoll9yo)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
