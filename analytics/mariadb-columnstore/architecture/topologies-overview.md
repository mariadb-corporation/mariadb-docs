---
description: >-
  MariaDB offers varied deployment topologies by workload and technology, each
  named and diagrammed with benefits listed. Custom configurations are also
  supported.
---

# Topologies Overview

MariaDB products can be deployed in many different topologies. The topologies described in this section are representative of the overall structure. MariaDB products can be deployed to form other topologies, leverage advanced product capabilities, or combine the capabilities of multiple topologies.

Topologies are the arrangements of nodes and links to achieve a purpose. This documentation describes a few of the many topologies that can be deployed using MariaDB database products.

We group topologies by workload (transactional, analytical, or hybrid) and technologies (Enterprise Spider). Single-node topologies are listed separately.

To help you select the correct topology:

* Each topology is named, and this name is used consistently throughout the documentation.
* A thumbnail diagram provides a small-scale summary of the topology's architecture.
* Finally, we provide a list of the benefits of the topology.

Although multiple topologies are listed on this page, the listed topologies are not the only options. MariaDB products are flexible, configurable, and extensible, so it is possible to deploy different topologies that combine the capabilities of multiple topologies listed on this page. The topologies listed on this page are primarily intended to be representative of the most commonly requested use cases.

## Transactional (OLTP)

### Primary/Replica Topology

| Diagram                                                             | Features                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](../../.gitbook/assets/es-primary-replica-topology-no-title.png) | <p><strong>MariaDB Replication</strong></p><ul><li>Highly available</li><li>Asynchronous or semi-synchronous replication</li><li>Automatic failover via MaxScale</li><li>Manual provisioning of new nodes from backup</li><li>Scales read via MaxScale.</li><li>Enterprise Server 10.3+, MaxScale 2.5+</li></ul> |

### Galera Cluster Topology

| Diagram                                                            | Features                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](../../.gitbook/assets/es-galera-cluster-topology-no-title.png) | <p><strong>Galera Cluster Topology Multi-Primary Cluster Powered by Galera for Transactional/OLTP Workloads</strong></p><ul><li>InnoDB Storage Engine</li><li>Highly available</li><li>Virtually synchronous, certification-based replication</li><li>Automated provisioning of new nodes (IST/SST)</li><li>Scales reads via MaxScale Enterprise Server 10.3+, MariaDB Enterprise Cluster (powered by Galera), MaxScale 2.5+</li></ul> |

## Analytical (OLAP, Data Warehousing, DSS)

### ColumnStore Shared Local Storage Topology

| Diagram                                                                   | Features                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](<../../.gitbook/assets/es-columnstore-topology-nfs-no-title (1).png>) | <p><strong>Columnar storage engine with shared local storage</strong></p><ul><li>Highly available</li><li>Automatic failover via MaxScale and CMAPI</li><li>Scales reads via MaxScale</li><li>Bulk data import</li><li>Enterprise Server, Enterprise ColumnStore, MaxScale</li><li>Optional <a href="columnstore-read-replicas.md">Read Replica topology</a></li></ul> |

### ColumnStore Object Storage Topology

| Diagram                                                            | Features                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](../../.gitbook/assets/es-columnstore-topology-s3-no-title.png) | <p><strong>Columnar storage engine with S3-compatible object storage</strong></p><ul><li>Highly available</li><li>Automatic failover via MaxScale and CMAPI</li><li>Scales reads via MaxScale</li><li>Bulk data import</li><li>Enterprise Server, Enterprise ColumnStore, MaxScale</li></ul> |

## Hybrid Workloads

### HTAP Topology

| Diagram                                                                 | Features                                                                                                                                                                                                                                                              |
| ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](../../.gitbook/assets/es-columnstore-htap-topology-s3-no-title.png) | <ul><li>Single-stack hybrid transactional/analytical workloads</li><li>ColumnStore for analytics with scalable S3-compatible object storage</li><li>InnoDB for transactions• Cross-engine JOINs</li><li>Enterprise Server, Enterprise ColumnStore, MaxScale</li></ul> |

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
