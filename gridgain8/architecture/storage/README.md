---
description: >-
  GridGain's storage options for keeping data beyond RAM, including native
  persistence for durable on-disk storage and swapping as an extension of memory.
---

# Persistence

This section covers how GridGain stores data beyond RAM. It describes [Native Persistence](native-persistence.md), which durably stores all data on disk and loads as much as it can into RAM for processing, and [Swapping](swapping.md), which lets the operating system move in-memory data to disk to avoid out-of-memory errors.

{% columns %}
{% column %}
{% content-ref url="native-persistence.md" %}
[Native Persistence](native-persistence.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain Native (Ignite) Persistence — how data partitions, checkpointing, and write-ahead logging keep data durable on disk, and how to configure them.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="swapping.md" %}
[Swapping](swapping.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain uses operating-system swapping to move in-memory data to disk as an extension of RAM, and how to enable it in the data region configuration.
{% endcolumn %}
{% endcolumns %}
