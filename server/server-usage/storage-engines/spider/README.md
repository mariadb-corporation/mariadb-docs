---
description: >-
  Explore the Spider storage engine in MariaDB Server. Learn how to shard data
  across multiple MariaDB and MySQL servers, enabling horizontal scaling and
  distributed database solutions.
---

# Spider

{% columns %}
{% column %}
{% content-ref url="spider-storage-engine-overview.md" %}
[spider-storage-engine-overview.md](spider-storage-engine-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An introduction to the Spider storage engine, which provides built-in sharding by linking to tables on remote MariaDB servers, supporting partitioning and XA transactions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spider-storage-engine-introduction/" %}
[spider-storage-engine-introduction](spider-storage-engine-introduction/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains the architecture of Spider, where a "Spider node" processes queries and distributes them to one or more "Data nodes" that actually store the data.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spider-differences-between-spiderformysql-and-mariadb.md" %}
[spider-differences-between-spiderformysql-and-mariadb.md](spider-differences-between-spiderformysql-and-mariadb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This page outlines the differences between the standalone SpiderForMySQL distribution and the version integrated into MariaDB Server, including version correspondence and feature availability.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spider-feature-matrix.md" %}
[spider-feature-matrix.md](spider-feature-matrix.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A matrix listing the features supported by Spider, including sharding, partitioning, XA transactions, and support for various SQL statements and functions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spider-use-cases.md" %}
[spider-use-cases.md](spider-use-cases.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Describes common use cases for Spider, such as horizontal sharding for scalability, consolidating data from multiple sources, and migrating data between servers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spider-installation.md" %}
[spider-installation.md](spider-installation.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A guide to installing the Spider storage engine on Debian/Ubuntu and other Linux distributions, including loading the plugin and configuring data nodes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spider-cluster-management.md" %}
[spider-cluster-management.md](spider-cluster-management.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Covers advanced management topics like executing direct SQL on backends, copying tables between nodes, and monitoring the cluster using status variables.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spider-case-studies.md" %}
[spider-case-studies.md](spider-case-studies.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A list of real-world companies and projects using Spider for high-volume data handling, gaming, and analytics, illustrating its scalability.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spider-benchmarks.md" %}
[spider-benchmarks.md](spider-benchmarks.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Performance benchmark results for Spider, demonstrating its throughput and latency characteristics under various workloads compared to other configurations.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="information-schema-spider_wrapper_protocols-table.md" %}
[information-schema-spider_wrapper_protocols-table.md](information-schema-spider_wrapper_protocols-table.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Describes the SPIDER_WRAPPER_PROTOCOLS table, which lists the available foreign data wrappers (like `mysql`) that Spider can use to connect to remote servers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spider-storage-engine-core-concepts.md" %}
[spider-storage-engine-core-concepts.md](spider-storage-engine-core-concepts.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains the fundamental concepts behind Spider, including its architecture as a proxy storage engine, sharding capabilities, and support for XA transactions across data nodes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spider-system-variables.md" %}
[spider-system-variables.md](spider-system-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Comprehensive list of system variables to configure Spider globally or per session, affecting connection timeouts, buffering, and query pushdown strategies.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spider-table-parameters.md" %}
[spider-table-parameters.md](spider-table-parameters.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A reference for table-level parameters in Spider, which can be set via the COMMENT or CONNECTION string to control connection settings, monitoring, and query behavior.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spider-functions/" %}
[spider-functions](spider-functions/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore Spider functions in MariaDB Server. Learn about the specialized functions that enhance data access and manipulation across sharded and distributed databases using the Spider storage engine.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="spider-faq.md" %}
[spider-faq.md](spider-faq.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Frequently asked questions about Spider, covering troubleshooting common errors, configuration best practices, and architectural questions regarding HA and sharding.
{% endcolumn %}
{% endcolumns %}
