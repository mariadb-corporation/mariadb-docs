---
description: >-
  Guidance for operating a GridGain 9 cluster, covering configuration, storage,
  security, metrics, and recovery.
icon: gear
---

# Management

This section covers the tasks involved in deploying, configuring, and operating a GridGain 9 cluster in production. It describes how cluster and node configuration is managed, how data is stored and distributed, how to secure the cluster, and how to monitor and recover it.

Start with [Cluster Configuration]({gridgain9}/gridgain9-management/cluster-configuration) to learn how configuration is structured and applied, then move on to the storage, security, metrics, and recovery topics as your deployment requires.

{% columns %}
{% column %}
{% content-ref url="{gridgain9}/gridgain9-management/installation" %}
[Installation and Upgrade]({gridgain9}/gridgain9-management/installation)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Ways to install and deploy GridGain 9, from ZIP archives and packages to Docker, Kubernetes, and cloud marketplace images, and procedures for upgrading the cluster and client applications.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{gridgain9}/gridgain9-management/cluster-configuration" %}
[Cluster Configuration]({gridgain9}/gridgain9-management/cluster-configuration)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain 9 cluster and node configuration is structured, stored in HOCON or JSON, and updated from the CLI at startup and during runtime.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{gridgain9}/gridgain9-management/using-the-cli-tool" %}
[Using the CLI Tool]({gridgain9}/gridgain9-management/using-the-cli-tool)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Run the GridGain 9 CLI in interactive or non-interactive mode, and configure its files, JVM properties, and default parameter values.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{gridgain9}/gridgain9-management/backup-and-replication" %}
[Backup, Recovery, and Replication]({gridgain9}/gridgain9-management/backup-and-replication)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Protect and replicate cluster data — snapshots and point-in-time recovery, disaster recovery, change data capture, and data center replication.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{gridgain9}/gridgain9-management/monitoring" %}
[Monitoring]({gridgain9}/gridgain9-management/monitoring)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Monitor a GridGain 9 cluster with metrics, system views, and exporters, and learn the best practices for keeping a production cluster healthy.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="{gridgain9}/gridgain9-management/migration-guides" %}
[Migration Guides]({gridgain9}/gridgain9-management/migration-guides)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Guides for migrating to GridGain 9, including from GridGain 8.
{% endcolumn %}
{% endcolumns %}
