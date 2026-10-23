---
description: >-
  Attaching GridGain 8 and GridGain 9 clusters to GridGain Control Center, and
  which clusters Control Center monitors.
hidden: true
---

# Attaching Clusters

Control Center is designed to work with GridGain 8 and GridGain 9 clusters you run in your environment. GridGain 8 ships with Control Center Agent by default.

This section describes how you can attach clusters to Control Center.

{% hint style="warning" %}
Control Center does not monitor Apache Ignite 2, Apache Ignite 3, or GridGain Community Edition clusters. For these clusters, Control Center does not collect metrics and blocks cluster actions, and the cluster remains in the cluster list with the data that Control Center has already saved. The only action available is updating the cluster license. A banner on every page reads: "Monitoring is not supported for Apache Ignite and GridGain Community Edition clusters. Update your license to Enterprise or Ultimate Edition."
{% endhint %}

{% content-ref url="connect-gridgain9-cluster.md" %}
[connect-gridgain9-cluster.md](connect-gridgain9-cluster.md)
{% endcontent-ref %}

{% content-ref url="connect-gridgain-cluster.md" %}
[connect-gridgain-cluster.md](connect-gridgain-cluster.md)
{% endcontent-ref %}
