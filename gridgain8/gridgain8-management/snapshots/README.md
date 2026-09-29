---
description: >-
  Overview of GridGain snapshots and recovery: full and incremental snapshots,
  point-in-time recovery, network backups, heterogeneous recovery, and tooling.
---

# Snapshots and Recovery

GridGain provides the ability to create snapshots of the data stored in a cluster and later use them to recover the cluster. This section describes how to create, manage, and recover from snapshots.

The following topics are covered:

{% columns %}
{% column %}
{% content-ref url="full-incremental-snapshots.md" %}
[Full and Incremental Snapshots](full-incremental-snapshots.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to create, restore, and secure full and incremental GridGain snapshots with the Java API and the snapshot utility, including the creation flow.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="heterogeneous-recovery.md" %}
[Heterogeneous Recovery](heterogeneous-recovery.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to restore GridGain snapshots and continuous archives on a cluster with a different size and topology, from local snapshots, network backups, or PITR.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="network-backups.md" %}
[Network Backups](network-backups.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How to create, restore, and remove GridGain network backups on NAS, NFS, or SFTP storage, including SFTP location configuration and JKS key setup.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="point-in-time-recovery.md" %}
[Point-in-Time Recovery](point-in-time-recovery.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain Point-in-Time Recovery (PITR) uses continuous WAL archiving to restore a cluster to any past moment, with requirements and limitations.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="snapshots-and-recovery.md" %}
[Data Snapshots and Recovery](snapshots-and-recovery.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
GridGain Ultimate Edition snapshots and recovery for Ignite native persistence, including how they differ from Apache Ignite snapshots.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="snapshots-management-tool.md" %}
[Snapshots Management Tool](snapshots-management-tool.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Reference for the GridGain snapshot-utility command-line tool — its commands, connection/output/SSL parameters, exit codes, command arguments, and error codes.
{% endcolumn %}
{% endcolumns %}
