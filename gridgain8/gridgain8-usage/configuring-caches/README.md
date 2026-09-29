---
description: >-
  Configuring GridGain caches, including atomicity modes, cache groups, backups,
  data compression, expiry policies, data distribution, and on-heap caching.
---

# Configuring Caches

{% columns %}
{% column %}
{% content-ref url="atomicity-modes.md" %}
[Atomicity Modes](atomicity-modes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain cache atomicity modes — ATOMIC, TRANSACTIONAL, and TRANSACTIONAL_SNAPSHOT — and how to enable transactional support for a cache.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="cache-groups.md" %}
[Cache Groups](cache-groups.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Using GridGain cache groups to share internal structures between caches, reducing memory usage and speeding up topology events in large deployments.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuration-overview.md" %}
[Overview](configuration-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to set GridGain cache configuration parameters, with a configuration example, the full parameter reference, and cache templates.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuring-backups.md" %}
[Configuring Partition Backups](configuring-backups.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configuring the number of partition backup copies for a GridGain cache and choosing between synchronous and asynchronous backup write modes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-compression.md" %}
[Data Compression](data-compression.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Dictionary-based cache data compression in GridGain using Zstandard or gzip, including configuration, ZSTD dictionary tuning, and limitations.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="expiry-policies.md" %}
[Expiry Policies](expiry-policies.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configuring expiry policies for GridGain caches, including eager TTL and resetting the expiration timeout with the touch operation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="managing-data-distribution.md" %}
[Managing Data Distribution](managing-data-distribution.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Controlling how GridGain distributes cache partitions across nodes using node filters, attribute-based filters, and backup filters.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="on-heap-caching.md" %}
[On-Heap Caching](on-heap-caching.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Enabling on-heap caching in GridGain and configuring on-heap eviction policies — LRU, FIFO, and Sorted — to manage the on-heap cache size.
{% endcolumn %}
{% endcolumns %}
