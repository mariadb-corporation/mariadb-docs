---
description: >-
  Optimizing MEMORY-engine tables, including choosing between B-tree and hash
  indexes.
---

# Optimizing MEMORY Tables

[MEMORY tables](../../../server-usage/storage-engines/memory-storage-engine.md) are a good choice for data that needs to be accessed often, and is rarely updated. Being in memory, it's not suitable for critical data or for storage, but if data can be moved to memory for reading without needing to be regenerated often, if at all, it can provide a significant performance boost.

The [MEMORY Storage Engine](../../../server-usage/storage-engines/memory-storage-engine.md) has a key feature in that it permits its indexes to be either B-tree or Hash. Choosing the best index type can lead to better performance. See [Storage Engine index types](../optimization-and-indexes/storage-engine-index-types.md) for more on the characteristics of each index type.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
