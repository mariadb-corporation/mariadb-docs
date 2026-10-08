---
description: >-
  Tuning key_buffer_size for servers with mostly MyISAM tables.
---

# Optimizing key\_buffer\_size

[key\_buffer\_size](../../../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size) is a [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) variable which determines the size of the index buffers held in memory, which affects the speed of index reads. Note that Aria tables by default make use of an alternative setting, [aria-pagecache-buffer-size](../../../server-usage/storage-engines/aria/aria-system-variables.md).

A good rule of thumb for servers consisting particularly of MyISAM tables is for about 25% or more of the available server memory to be dedicated to the key buffer.

A good way to determine whether to adjust the value is to compare the [key\_read\_requests](server-status-variables.md#key_read_requests) value, which is the total value of requests to read an index, and the [key\_reads](server-status-variables.md#key_reads) values, the total number of requests that had to be read from disk.

The ratio of key\_reads to key\_read\_requests should be as low as possible, 1:100 is the highest acceptable, 1:1000 is better, and 1:10 is terrible.

The effective maximum size might be lower than what is set, depending on the server's available physical RAM and the per-process limit determined by the operating system.

If you don't make use of MyISAM tables at all, you can set this to a very low value, such as 64K.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
