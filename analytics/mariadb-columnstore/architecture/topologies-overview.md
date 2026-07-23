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

```mermaid
flowchart TD
    accTitle: MaxScale routing reads and writes across a MariaDB primary/replica topology
    accDescr {
        A MaxScale proxy routes write traffic to a single primary MariaDB Enterprise Server node
        and read traffic to two replica nodes. The primary replicates its changes to both
        replicas using asynchronous or semi-synchronous MariaDB Replication.
    }
    MX["MariaDB MaxScale"]
    R1[("ES — Replica")]
    P[("ES — Primary")]
    R2[("ES — Replica")]
    MX -->|ro| R1
    MX -->|rw| P
    MX -->|ro| R2
    P -->|"MariaDB Replication (async/semi-sync)"| R1
    P -->|"MariaDB Replication (async/semi-sync)"| R2
    classDef node fill:#e2f0f2,stroke:#0a5a6b,stroke-width:2px,color:#111;
    classDef primary fill:#ffe3b0,stroke:#8a4b00,stroke-width:3px,color:#111;
    classDef proxy fill:#f0e2f5,stroke:#5b1a70,stroke-width:2px,color:#111;
    class MX proxy
    class R1,R2 node
    class P primary
```

_MaxScale routes reads to two replicas and writes to one primary, which replicates to both._

<p><strong>MariaDB Replication</strong></p>

<ul><li>Highly available</li><li>Asynchronous or semi-synchronous replication</li><li>Automatic failover via MaxScale</li><li>Manual provisioning of new nodes from backup</li><li>Scales read via MaxScale.</li><li>Enterprise Server 10.3+, MaxScale 2.5+</li></ul>

### Galera Cluster Topology

```mermaid
flowchart TD
    accTitle: MaxScale routing to a three-node Galera Cluster
    accDescr {
        A MaxScale proxy routes write traffic to one MariaDB Enterprise Server node and read
        traffic to the other two. All three nodes belong to a Galera Cluster and stay
        synchronized with each other through virtually synchronous, certification-based Galera
        replication, so any node can accept writes.
    }
    MX["MariaDB MaxScale"]
    N1[("ES")]
    N2[("ES")]
    N3[("ES")]
    MX -->|ro| N1
    MX -->|rw| N2
    MX -->|ro| N3
    N2 -->|Galera| N1
    N2 -->|Galera| N3
    classDef node fill:#e2f0f2,stroke:#0a5a6b,stroke-width:2px,color:#111;
    classDef proxy fill:#f0e2f5,stroke:#5b1a70,stroke-width:2px,color:#111;
    class MX proxy
    class N1,N2,N3 node
```

_MaxScale routes to three Galera Cluster nodes that replicate virtually synchronously with each other._

<p><strong>Galera Cluster Topology Multi-Primary Cluster Powered by Galera for Transactional/OLTP Workloads</strong></p>

<ul><li>InnoDB Storage Engine</li><li>Highly available</li><li>Virtually synchronous, certification-based replication</li><li>Automated provisioning of new nodes (IST/SST)</li><li>Scales reads via MaxScale Enterprise Server 10.3+, MariaDB Enterprise Cluster (powered by Galera), MaxScale 2.5+</li></ul>

## Analytical (OLAP, Data Warehousing, DSS)

### ColumnStore Shared Local Storage Topology

| Diagram                                                                   | Features                                                                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![](<../../.gitbook/assets/es-columnstore-topology-nfs-no-title (1).png>) | <p><strong>Columnar storage engine with shared local storage</strong></p><ul><li>Highly available</li><li>Automatic failover via MaxScale and CMAPI</li><li>Scales reads via MaxScale</li><li>Bulk data import</li><li>Enterprise Server, ColumnStore, MaxScale</li><li>Optional <a href="columnstore-read-replicas.md">Read Replica topology</a></li></ul> |

### ColumnStore Object Storage Topology

```mermaid
flowchart TD
    accTitle: MaxScale routing to three ColumnStore nodes backed by S3 object storage
    accDescr {
        A MaxScale proxy routes write traffic to one MariaDB Enterprise Server and ColumnStore
        node and read traffic to two others. All three ColumnStore nodes share the same data by
        reading from and writing to a common S3-compatible object storage bucket.
    }
    MX["MariaDB MaxScale"]
    E1[("ES")]
    E2[("ES")]
    E3[("ES")]
    C1[("ColumnStore")]
    C2[("ColumnStore")]
    C3[("ColumnStore")]
    S3[("S3 object storage")]
    MX -->|ro| E1
    MX -->|rw| E2
    MX -->|ro| E3
    E1 --- C1
    E2 --- C2
    E3 --- C3
    S3 -.-> C1
    S3 -.-> C2
    S3 -.-> C3
    classDef node fill:#e2f0f2,stroke:#0a5a6b,stroke-width:2px,color:#111;
    classDef proxy fill:#f0e2f5,stroke:#5b1a70,stroke-width:2px,color:#111;
    classDef storage fill:#fdf3c7,stroke:#8a6d00,stroke-width:2px,color:#111;
    class MX proxy
    class E1,E2,E3,C1,C2,C3 node
    class S3 storage
```

_MaxScale routes to three ColumnStore nodes that all read and write the same S3 object storage._

<p><strong>Columnar storage engine with S3-compatible object storage</strong></p>

<ul><li>Highly available</li><li>Automatic failover via MaxScale and CMAPI</li><li>Scales reads via MaxScale</li><li>Bulk data import</li><li>Enterprise Server, ColumnStore, MaxScale</li></ul>

## Hybrid Workloads

### HTAP Topology

```mermaid
flowchart TD
    accTitle: MaxScale routing to a single HTAP server splitting analytical and transactional storage
    accDescr {
        A MaxScale proxy routes HTAP read/write traffic to a single MariaDB Enterprise Server
        node. That node writes analytical queries to a ColumnStore engine backed by S3 object
        storage, and transactional queries to an InnoDB engine. InnoDB replicates its data to
        ColumnStore using HTAP Replication so both engines can be queried with cross-engine joins.
    }
    MX["MariaDB MaxScale"]
    ES[("ES")]
    CS[("ColumnStore")]
    IDB[("InnoDB")]
    S3[("S3 object storage")]
    MX -.->|"rw (HTAP)"| ES
    ES ---|"rw (OLAP)"| CS
    ES ---|"rw (OLTP)"| IDB
    IDB -->|HTAP Replication| CS
    S3 -.-> CS
    classDef node fill:#e2f0f2,stroke:#0a5a6b,stroke-width:2px,color:#111;
    classDef proxy fill:#f0e2f5,stroke:#5b1a70,stroke-width:2px,color:#111;
    classDef storage fill:#fdf3c7,stroke:#8a6d00,stroke-width:2px,color:#111;
    class MX proxy
    class ES,CS,IDB node
    class S3 storage
```

_MaxScale routes HTAP traffic to one server that replicates from InnoDB to S3-backed ColumnStore._

<ul><li>Single-stack hybrid transactional/analytical workloads</li><li>ColumnStore for analytics with scalable S3-compatible object storage</li><li>InnoDB for transactions• Cross-engine JOINs</li><li>Enterprise Server, ColumnStore, MaxScale</li></ul>

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
