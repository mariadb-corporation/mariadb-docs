---
description: >-
  Operate a GridGain 8 cluster — installation and upgrade, cluster
  configuration, snapshots and recovery, data center replication, monitoring, and migration.
icon: gears
---

# Management

Welcome to GridGain cluster management. This section is designed for people tasked with GridGain and/or Ignite cluster administration.

Once you've installed GridGain or Ignite, you will want or need to perform many different administrative tasks — everything from migration and security, to deploying, monitoring, and upgrading your clusters. Some of the topics are useful right away, and others you may not need until later (or not at all, depending on your use case).

{% hint style="info" %}
[Complimentary Developer Training - Control Center Essentials](https://www.gridgain.com/products/services/training/how-monitor-and-manage-apache-ignite-gridgain-control-center)

Join our upcoming live, instructor-led Control Center training session and learn how to troubleshoot performance issues and optimize your cluster with ease.
{% endhint %}

## GridGain and Ignite

{% include "../.gitbook/includes/gg8-intro-gg-ignite.md" %}

## Programming Languages

{% include "../.gitbook/includes/gg8-intro-languages.md" %}

## Related Documentation

If you're looking for information about installing the product or getting started, see the [Getting Started Guide](../gridgain8-get-started/README.md) and the [Installation Guide](installation/README.md).

If you're looking for information on how to build an application, see the [Development](../gridgain8-development/README.md) section.

If you're looking to learn more about performance or troubleshooting, see the [Tuning and Troubleshooting](../tuning-and-troubleshooting/README.md) section.

{% columns %}
{% column %}
{% content-ref url="installation/" %}
[Installation and Upgrade](installation/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Install and start GridGain — system requirements, the binary distribution, starting a node with default or custom configuration, and deployment options.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="cluster-configuration/" %}
[Cluster Configuration](cluster-configuration/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure and run GridGain cluster nodes — node configuration, logging, starting and stopping nodes, and how nodes discover each other and form a cluster.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="licensing-and-support/" %}
[Licensing and Support](licensing-and-support/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Manage GridGain licenses and understand the product lifecycle — Enterprise and Ultimate license files, the versioning and support-lifecycle policy, and SWID tags.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="backup-and-replication/" %}
[Backup, Recovery, and Replication](backup-and-replication/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Protect and replicate cluster data — snapshots and point-in-time recovery, cross-datacenter replication, and cache update conflict resolution.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="monitoring/" %}
[Monitoring](monitoring/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Overview of monitoring and metrics in GridGain, including the available monitoring methods, metric configuration, and distributed tracing.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="cluster-maintenance/" %}
[Cluster Maintenance](cluster-maintenance/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Keep a running GridGain cluster healthy — control the CPU and memory a node uses, reclaim disk space through persistence defragmentation, and isolate a node in maintenance mode.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="migration-guides/" %}
[Migration Guides](migration-guides/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Guides for migrating to GridGain 8 from other data platforms, including Apache Ignite 2.x and Oracle Coherence.
{% endcolumn %}
{% endcolumns %}
