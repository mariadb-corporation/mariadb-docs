---
icon: chart-mixed
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
---

# HA & DR

This section introduces MariaDB Cloud's robust, multi-layered capabilities for high availability (HA) and disaster recovery (DR). These features ensure data resilience, consistency, and continuous availability for mission-critical workloads in the event of regional outages or infrastructure failures. MariaDB Cloud leverages semi-synchronous replication, intelligent proxy-based failover, and cross-region or cross provider replication to enable durable, highly available deployments with minimal configuration.

## HA & Replicated Topology

MariaDB Cloud's intelligent proxy-based failover and semi-synchronous replication provide high availability, load balancing, and support for casual read configurations.

{% content-ref url="../high-availability-dr/ha-and-replicated-topology.md" %}
[ha-and-replicated-topology.md](../high-availability-dr/ha-and-replicated-topology.md)
{% endcontent-ref %}

## Global Replication

Configures and implements cross-region or multi-cloud disaster recovery with Global Replication. This includes automating backup restoration, deploying additional services, and configuring replication across various regions or cloud providers to ensure high availability and failover beyond a single region.&#x20;

{% content-ref url="Setup Global Replication.md" %}
[Setup Global Replication.md](<Setup Global Replication.md>)
{% endcontent-ref %}
