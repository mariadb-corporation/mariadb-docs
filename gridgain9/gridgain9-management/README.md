---
description: >-
  Guidance for operating a GridGain 9 cluster, covering configuration, storage,
  security, metrics, and recovery.
icon: gear
---

# Administrators Guide

The Administrator's Guide covers the tasks involved in deploying, configuring, and operating a GridGain 9 cluster in production. It describes how cluster and node configuration is managed, how data is stored and distributed, how to secure the cluster, and how to monitor and recover it.

Start with [GridGain Configuration](../reference/configuration/README.md) to learn how configuration is structured and applied, then move on to the storage, security, metrics, and recovery topics as your deployment requires.

{% columns %}
{% column %}
{% content-ref url="installation/" %}
[Installation](installation/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Ways to install and deploy GridGain 9, from ZIP archives and packages to Docker, Kubernetes, and cloud marketplace images.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="upgrade/" %}
[Upgrading GridGain 9](upgrade/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Procedures for upgrading GridGain 9 — full-cluster and rolling upgrades of the cluster, and upgrading client applications.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="migration-from-gridgain-8/" %}
[Migrating from GridGain 8](migration-from-gridgain-8/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Tools and workflows for migrating a cluster, its persistent data, and its applications from GridGain 8 to GridGain 9.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="monitoring/" %}
[Monitoring](monitoring/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Monitor a GridGain 9 cluster with metrics, system views, and exporters, and learn the best practices for keeping a production cluster healthy.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="snapshots/" %}
[Snapshots](snapshots/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Create snapshots of cluster data for backup and recovery, and restore a GridGain 9 cluster to a point in time.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="disaster-recovery/" %}
[Disaster Recovery](disaster-recovery/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Recovering a GridGain 9 cluster after data loss or failure of system groups.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="change-data-capture.md" %}
[Change Data Capture](change-data-capture.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Use GridGain 9 Change Data Capture (CDC) to replicate table changes to external systems such as Apache Iceberg, and from Microsoft SQL Server.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-center-replication/" %}
[Data Center Replication](data-center-replication/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Data center replication (DCR) keeps tables in sync across multiple GridGain 9 clusters through one-way, asynchronous, last-write-wins replication.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-archiving.md" %}
[Data Archiving](data-archiving.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How data archiving in GridGain 9 removes aged data from primary storage after moving it to secondary storage for HTAP workloads.
{% endcolumn %}
{% endcolumns %}
