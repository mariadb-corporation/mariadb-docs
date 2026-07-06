---
description: >-
  Dive into advanced configurations for MariaDB Server performance. This section
  covers in-depth tuning parameters, optimization strategies, and best practices
  to maximize speed and efficiency.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
  tags:
    visible: true
---

# Advanced Configuration

Articles of how to setup your MariaDB optimally on different systems

{% columns %}
{% column %}
{% content-ref url="atomic-write-support.md" %}
[atomic-write-support.md](atomic-write-support.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains the concept of atomic writes in MariaDB, which improve performance and data integrity on SSDs by bypassing the InnoDB doublewrite buffer, supported on devices like Fusion-io and Shannon SSDs.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuring-linux-for-mariadb.md" %}
[configuring-linux-for-mariadb.md](configuring-linux-for-mariadb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Guidance on tuning Linux kernel settings for MariaDB performance, including I/O schedulers (using `none` or `mq-deadline`), open file limits, and core file sizes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuring-mariadb-for-optimal-performance.md" %}
[configuring-mariadb-for-optimal-performance.md](configuring-mariadb-for-optimal-performance.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete MariaDB performance tuning: innodb_buffer_pool_size, aria_pagecache_buffer_size, thread_handling configuration, and SHOW GLOBAL STATUS monitoring.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuring-swappiness.md" %}
[configuring-swappiness.md](configuring-swappiness.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Recommendations for setting the Linux `vm.swappiness` kernel parameter (ideally to 1) to prevent the OS from swapping out MariaDB memory pages, which degrades performance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="fusion-io/" %}
[fusion-io](fusion-io/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Introduction to using Fusion-io flash memory cards with MariaDB to significantly boost I/O throughput and reduce latency, including benefits like atomic write support.
{% endcolumn %}
{% endcolumns %}
