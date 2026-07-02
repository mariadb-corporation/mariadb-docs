---
description: >-
  Optimize MariaDB Server performance with operating system tuning. This section
  covers configuring your OS for improved I/O, memory management, and network
  settings to maximize database efficiency.
---

# Operating System Optimizations

{% columns %}
{% column %}
{% content-ref url="filesystem-optimizations.md" %}
[filesystem-optimizations.md](filesystem-optimizations.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Filesystem choices and settings that affect MariaDB Server performance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="storage-io-buffering-and-persistence.md" %}
[storage-io-buffering-and-persistence.md](storage-io-buffering-and-persistence.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Defines the OS-agnostic terms MariaDB documentation uses for disk I/O — unbuffered I/O, write-through, persist — and shows how each one maps to Unix-like and Windows mechanisms.
{% endcolumn %}
{% endcolumns %}
