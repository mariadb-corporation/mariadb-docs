---
description: >-
  Optimize large tables in MariaDB Server with partitioning. Learn how to divide
  tables into smaller, manageable parts for improved performance, easier
  maintenance, and scalability.
---

# Partitioning Tables

{% columns %}
{% column %}
{% content-ref url="partitioning-overview.md" %}
[partitioning-overview.md](partitioning-overview.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Complete Partitioning Overview guide for MariaDB. Complete reference documentation for implementation, configuration, and usage for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="partition-pruning-and-selection.md" %}
[partition-pruning-and-selection.md](partition-pruning-and-selection.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Understand how the optimizer automatically prunes irrelevant partitions and how to explicitly select partitions in your queries for efficiency.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="partition-maintenance.md" %}
[partition-maintenance.md](partition-maintenance.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Discover administrative tasks for managing partitions, such as adding, dropping, reorganizing, and coalescing them to keep your data optimized.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="partitioning-types/partitioning-types-overview.md" %}
[partitioning-types-overview.md](partitioning-types/partitioning-types-overview.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
An introduction to the various partitioning strategies available in MariaDB, helping you choose the right method for your data distribution needs. For a complete list of partitioning types, [see this page](partitioning-types/).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="partitioning-limitations.md" %}
[partitioning-limitations.md](partitioning-limitations.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
This page outlines constraints when using partitioning, such as the maximum number of partitions and restrictions on foreign keys and query cache usage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="partitions-files.md" %}
[partitions-files.md](partitions-files.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Learn how MariaDB stores partitioned tables on the filesystem, typically creating separate .ibd files for each partition when using InnoDB.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="partitions-metadata.md" %}
[partitions-metadata.md](partitions-metadata.md)
{% endcontent-ref %}


{% endcolumn %}

{% column %}
Understand how to retrieve metadata about partitions using the `INFORMATION_SCHEMA.PARTITIONS` table to monitor row counts and storage usage.
{% endcolumn %}
{% endcolumns %}
