---
description: >-
  Developer-facing how-to for building applications on GridGain 8 — configuration,
  APIs, SQL, distributed computing, data structures, and more.
icon: code
---

# Usage

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
{% content-ref url="colocating-computations.md" %}
[Colocating Computations with Data](colocating-computations.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to colocate computations with data in GridGain using affinityCall and affinityRun, by key or partition, plus entry processors.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="continuous-queries.md" %}
[Using Continuous Queries](continuous-queries.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to use continuous queries in GridGain to monitor cache modifications, including local listeners, initial queries, remote filters and transformers.
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
{% content-ref url="data-streaming.md" %}
[Data Streaming](data-streaming.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to use the GridGain Data Streaming API to inject large volumes of data into a cluster, with stream receivers, transformers, and visitors.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="logging.md" %}
[Configuring Logging](logging.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to configure logging in GridGain, including JUL, Log4j2, Log4j, JCL, SLF4J, and Logback, plus suppressing sensitive information.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="messaging.md" %}
[Topic-Based Messaging with GridGain](messaging.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Topic-based, cluster-wide messaging in GridGain using the IgniteMessaging interface to publish and subscribe to messages.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="near-caches.md" %}
[Near Caches](near-caches.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configuring near caches in GridGain to store recently or frequently accessed data on the local node, statically and dynamically.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="setup.md" %}
[Setting Up](setup.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to set up GridGain, including system requirements, binary and Maven installation, Docker, work directory, and enabling optional modules.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="starting-nodes.md" %}
[Starting and Stopping Nodes](starting-nodes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to start server and client nodes in GridGain, shut them down gracefully, set JVM options, and use node lifecycle events.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="transactions.md" %}
[Performing Transactions](transactions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to perform transactions in GridGain, including concurrency modes and isolation levels, deadlock detection, JTA, and handling failed transactions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="understanding-configuration.md" %}
[Understanding Configuration](understanding-configuration.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Different ways of configuring a GridGain cluster, including Spring XML configuration and programmatic configuration.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="vector-search.md" %}
[Vector Search](vector-search.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to index and search vectors stored in cache fields in GridGain, including vector fields, vector queries, and similarity functions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="clustering/" %}
[Clustering and Cluster Activation](clustering/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configuring how GridGain nodes discover each other and form a cluster, including TCP/IP and ZooKeeper discovery, network settings, and client nodes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="code-deployment/" %}
[Code Deployment](code-deployment/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Overview of code deployment in GridGain, covering how user code and classes are made available across cluster nodes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="configuring-caches/" %}
[Configuring Caches](configuring-caches/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configuring GridGain caches, including atomicity modes, cache groups, backups, data compression, expiry policies, data distribution, and on-heap caching.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-structures/" %}
[Data Structures](data-structures/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain provides distributed implementations of common data structures, including atomic types, sequences, latches, locks, semaphores, queues, and sets.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="distributed-computing/" %}
[Distributed Computing](distributed-computing/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain distributes computations across cluster nodes in a balanced and fault-tolerant manner, with support for the MapReduce pattern, cluster groups, load balancing, and job scheduling.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="events/" %}
[Working with Events](events/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Overview of working with events in GridGain, including the available event types and how to listen to them.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="key-value-api/" %}
[Using Key-Value Cache API](key-value-api/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use the GridGain key-value cache API to perform basic cache operations, work with binary objects, and run scan and index queries.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="machine-learning/" %}
[Machine Learning](machine-learning/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Overview of the GridGain Machine Learning module and the algorithms it provides.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="memory-configuration/" %}
[Memory Configuration](memory-configuration/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configuring GridGain memory usage, including data regions, eviction policies, and page replacement policies.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="persistence/" %}
[Persistence](persistence/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure how GridGain persists cache data to external stores — third-party databases and custom cache store implementations.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="sql/" %}
[Working with SQL](sql/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Work with GridGain's distributed SQL database, including the SQL API, schemas, indexes, joins, custom functions, and combined SQL and key-value access.
{% endcolumn %}
{% endcolumns %}
