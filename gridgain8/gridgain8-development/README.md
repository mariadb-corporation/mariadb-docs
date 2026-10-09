---
description: >-
  Developer-facing how-to for building applications on GridGain 8 — configuration,
  APIs, SQL, distributed computing, data structures, and more.
icon: code
---

# Development

This guide is targeted at developers and architects who create applications on top of the GridGain or Apache Ignite products. Both products are available as libraries that you can integrate into your own application.

{% hint style="info" %}
[Complimentary, Instructor-Led Developer Training - Apache Ignite Essentials](https://www.gridgain.com/products/services/training/apache-ignite-essentials)

If you are getting started with Ignite or GridGain, we recommend attending [an upcoming training session](https://www.gridgain.com/products/services/training#public-training-listing) to learn about the key design principles for building data-intensive applications.
{% endhint %}

## GridGain and Apache Ignite

{% include "../.gitbook/includes/gg8-intro-gg-ignite.md" %}

## Programming Languages

{% include "../.gitbook/includes/gg8-intro-languages.md" %}

{% columns %}
{% column %}
{% content-ref url="project-setup.md" %}
[Project Setup](project-setup.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to set up GridGain, including system requirements, binary and Maven installation, Docker, work directory, and enabling optional modules.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="caches-and-memory/" %}
[Caches and Memory](caches-and-memory/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure how GridGain stores data in memory and on disk — caches, data regions, persistence, and near caches.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="accessing-data/" %}
[Data Access](accessing-data/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Read and write data in GridGain — the key-value and SQL APIs, vector search, transactions, continuous queries, and data streaming.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="cross-platform-interoperability.md" %}
[Cross-Platform Interoperability](cross-platform-interoperability.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How .NET, Java, and C++ platforms interoperate in a mixed GridGain cluster, including type compatibility and calling a .NET service from Java.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="distributed-computing-and-services/" %}
[Distributed Computing and Services](distributed-computing-and-services/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Run computations and services across the cluster — the compute APIs, data colocation, services, and code deployment.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="messaging-and-events/" %}
[Messaging and Events](messaging-and-events/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Communicate across the cluster — topic-based messaging and listening to cluster events.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-structures/" %}
[Distributed Data Structures](data-structures/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain provides distributed implementations of common data structures, including atomic types, sequences, latches, locks, semaphores, queues, and sets.
{% endcolumn %}
{% endcolumns %}
