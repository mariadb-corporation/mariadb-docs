---
description: >-
  Operate a GridGain 8 cluster — installation and upgrade, snapshots and
  recovery, data center replication, monitoring, and migration.
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

If you're looking for information on how to build an application, see the [Usage Guide](../gridgain8-usage/README.md).

If you're looking to learn more about performance or troubleshooting, see the [HA and Performance Guide](../ha-and-performance/performance-tuning/general-tips.md).

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
{% content-ref url="versioning-and-support-lifecycle.md" %}
[Versioning and Support Lifecycle](versioning-and-support-lifecycle.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain's Major.Minor.Maintenance versioning convention, the standard support lifecycle, and the release support dates for GridGain platform versions.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="upgrade/" %}
[Upgrade](upgrade/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Upgrade a GridGain 8 cluster — a standard version upgrade, or a rolling upgrade that keeps the cluster available throughout.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="software-identification.md" %}
[Software Identification (SWID)](software-identification.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain Software Identification (SWID) tags — ISO 19770-2 XML artifacts that identify the product for software asset management tools, and where to find them.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="licensing.md" %}
[Licensing](licensing.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to specify, switch, update, and manage GridGain Enterprise and Ultimate Edition license files, including Java dependencies and license expiration.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="snapshots/" %}
[Snapshots and Recovery](snapshots/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Overview of GridGain snapshots and recovery: full and incremental snapshots, point-in-time recovery, network backups, heterogeneous recovery, and tooling.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="data-center-replication/" %}
[Data Center Replication](data-center-replication/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain data center replication lets you replicate data caches between multiple data centers and recover quickly when a data center goes offline.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="conflict-resolution.md" %}
[Conflict Resolution](conflict-resolution.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain resolves cache update conflicts, including automatic resolution and the CacheConflictResolver interface for custom conflict handling.
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
{% content-ref url="resource-control.md" %}
[GridGain Resource Control](resource-control.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to limit the CPU and memory a GridGain node uses on Linux with systemd, Docker, and taskset/cpuset to control the licensed core footprint.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="persistence-defragmentation.md" %}
[Persistence Defragmentation](persistence-defragmentation.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to reclaim disk space from GridGain persistent storage by scheduling and running defragmentation on cluster nodes with the control script.
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
