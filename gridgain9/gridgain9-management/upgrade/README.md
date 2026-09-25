---
description: >-
  Procedures for upgrading GridGain 9 — full-cluster and rolling upgrades of the
  cluster, and upgrading client applications.
---

# Upgrading GridGain 9

This section describes how to upgrade GridGain 9. Choose a full-cluster upgrade when you can take the whole cluster offline, a rolling upgrade to move between versions without downtime, or follow the client upgrade guidance to update your applications independently of the cluster.

{% columns %}
{% column %}
{% content-ref url="full-cluster-upgrade.md" %}
[Full-Cluster Upgrade](full-cluster-upgrade.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Upgrade a GridGain 9 cluster by stopping every node, replacing the binaries, and restarting the cluster on the new version.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="rolling-upgrade.md" %}
[Rolling Upgrade](rolling-upgrade.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Move a GridGain 9 cluster between versions without downtime by rolling nodes one at a time, then committing the upgrade.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="client-upgrade.md" %}
[Client Upgrade](client-upgrade.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
How GridGain 9 clients and servers upgrade independently, the compatibility model between versions, and the recommended client-upgrade procedure.
{% endcolumn %}
{% endcolumns %}
