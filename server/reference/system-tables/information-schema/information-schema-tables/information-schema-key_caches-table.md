---
description: >-
  The Information Schema KEY_CACHES table displays statistics about the
  segmented key cache, including block usage and read/write requests.
---

# Information Schema KEY\_CACHES Table

The [Information Schema](../) `KEY_CACHES` table shows statistics about the [segmented key cache](../../../../ha-and-performance/optimization-and-tuning/system-variables/segmented-key-cache.md).

It contains the following columns:

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

## Example

```sql
SELECT * FROM information_schema.KEY_CACHES \G
********************** 1. row **********************
KEY_CACHE_NAME: default
SEGMENTS: NULL
SEGMENT_NUMBER: NULL
     FULL_SIZE: 134217728
    BLOCK_SIZE: 1024
   USED_BLOCKS: 36
 UNUSED_BLOCKS: 107146
  DIRTY_BLOCKS: 0
 READ_REQUESTS: 40305
         READS: 21
WRITE_REQUESTS: 19239
        WRITES: 358
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
