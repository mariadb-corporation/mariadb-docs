---
description: >-
  MariaDB Exa deployment options: proof-of-concept via Docker or Community
  Exasol (2 VCPU, 200 GB), and clustered MPP production with three or more
  16-VCPU/256-GB nodes plus optional HA.
icon: wrench
---

# Deployment

You can deploy MariaDB Exa in one of the following ways.

## Proof of Concept via Docker or Community Exasol

For testing or proof-of-concept environments, Exasol can be deployed (via Docker or Virtual Box with an OVA file).

This mode simplifies setup, but does not provide MPP[^1] benefits, high availability or real performance testing. These options are limited to using 2 VCPU[^2]s and 200G of data, and come with MariaDB's CDC[^3] solution and MaxScale integration.

## Clustered MPP Deployment

In production, MariaDB Exa is deployed as a cluster of nodes.

* Minimum 3 node deployments of 16 VCPUs, 256 GB RAM nodes.
* Optional standby nodes for High Availability.

Data is automatically distributed across nodes, using MariaDB Exa internal partitioning and replication for fault tolerance.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}

[^1]: Massive Parallel Processing — analytical database designed for fast, large-scale SQL analytics

[^2]: Virtual CPU

[^3]: Change Data Capture — scenarios for integrating MariaDB Exa for analytical workloads and data pipelines
