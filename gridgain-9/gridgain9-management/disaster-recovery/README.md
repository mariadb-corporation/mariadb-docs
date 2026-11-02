---
description: >-
  Recovering a GridGain 9 cluster after data loss or failure of system groups.
---

# Disaster Recovery

Disaster recovery covers the procedures for restoring a GridGain 9 cluster to a working state after partition data loss or the failure of critical system groups. These are operational tasks you run when normal fault tolerance has been exceeded — for the concepts behind fault tolerance, see [Cluster Fault Tolerance](../../architecture/cluster-fault-tolerance.md).

{% columns %}
{% column %}
{% content-ref url="data-recovery.md" %}
[Data Recovery](data-recovery.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Disaster recovery operations for GridGain 9 data partitions — minority and majority offline scenarios, partition loss, and partition states.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="system-groups-recovery.md" %}
[System Groups Recovery](system-groups-recovery.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Disaster recovery operations for GridGain 9 system RAFT groups — recovering the Cluster Management Group and the Metastorage Group after permanent majority loss.
{% endcolumn %}
{% endcolumns %}
