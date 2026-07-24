# MariaDB Platform Use Cases

_This section outlines various topologies for MariaDB deployment, emphasizing flexibility and configurations to meet diverse use cases. Key topologies include Primary/Replica for transactional workloads with features like asynchronous replication and failover management, and Galera Cluster offering a multi-primary architecture with synchronous replication. Both topologies leverage MaxScale for scaling and are compatible with Enterprise Server 10.3+ and MaxScale 2.5+. The guide also introduces the ColumnStore Object Storage for analytical processing, focusing on OLAP and data warehousing needs._

MariaDB products can be deployed in many different topologies, arrangements of products and components to achieve a purpose. MariaDB products can also be deployed to form other topologies, leverage advanced product capabilities, or combine the capabilities of multiple topologies.

Topologies are the arrangement of nodes and links to achieve a purpose. This documentation describes a few of the many topologies that can be deployed using MariaDB database products.

We group topologies by workload (transactional, analytical, hybrid) and technologies (Enterprise Spider). Single-node topologies are listed separately.

To help you select the correct topology:

* Each topology is named and this name is used consistently throughout the documentation.
* A thumbnail diagram provides a small-scale summary of the topology's architecture.
* Finally, we provide a list of the benefits of the topology.

Although multiple topologies are listed on this page, the listed topologies are not the only options. MariaDB products are flexible, configurable, and extensible, so it possible to deploy different topologies that combine the capabilities of multiple topologies listed on this page. The topologies listed on this page are primarily intended to be representative of the most commonly requested use cases.

In the diagrams, ES is short for Enterprise Server.

## Transactional (OLTP)

### Primary/Replica

MariaDB Replication offers high availability through asynchronous or semi-synchronous methods. It supports automatic failover via MaxScale (2.5+) and read scaling. New nodes require manual provisioning from backup. This solution is available with Enterprise Server 10.3+.

**Add note about primary/replica vs. master/slave**

```mermaid
flowchart TD
    accTitle: MaxScale routing to an ES primary and two replicas
    accDescr {
        A MaxScale proxy routes read-write traffic to one primary Enterprise Server node and
        read-only traffic to two replica nodes. The primary replicates asynchronously or
        semi-synchronously to both replicas using MariaDB Replication. There are three ES
        nodes total: one primary and two replicas, with no separate storage layer.
    }
    R1[("ES<br/>replica")]
    P[("ES<br/>primary")]
    R2[("ES<br/>replica")]
    MX["MariaDB MaxScale"]
    MX -->|ro| R1
    MX -->|rw| P
    MX -->|ro| R2
    P -->|"MariaDB Replication<br/>(async or semi-sync)"| R1
    P -->|"MariaDB Replication<br/>(async or semi-sync)"| R2
    classDef node fill:#e2f0f2,stroke:#0a5a6b,stroke-width:2px,color:#111;
    classDef primary fill:#cde8ea,stroke:#0a5a6b,stroke-width:3px,color:#111;
    class MX,R1,R2 node
    class P primary
```

_MaxScale routes reads to two replicas and writes to a primary, which replicates to both replicas._

<ul><li><strong>MariaDB Replication</strong></li><li>Highly available</li><li>Asynchronous or semi-synchronous replication</li><li>Automatic failover via MaxScale</li><li>Manual provisioning of new nodes from backup</li><li>Scales reads via MaxScale</li><li>Enterprise Server 10.3+, MaxScale 2.5+</li></ul>

### Galera Cluster

MariaDB Enterprise Cluster, powered by Galera, provides a highly available, multi-primary solution for transactional/OLTP workloads using the InnoDB storage engine. It features virtually synchronous, certification-based replication, automated node provisioning (IST/SST), and scales reads via MaxScale. It's compatible with Enterprise Server 10.3+ and MaxScale 2.5+.

```mermaid
flowchart TD
    accTitle: MaxScale routing to a three-node ES Galera cluster
    accDescr {
        A MaxScale proxy routes read-only traffic to two nodes and read-write traffic to one
        node across a three-node MariaDB Enterprise Server cluster. All three nodes form a
        multi-primary Galera cluster, replicating virtually synchronously with each other
        using certification-based replication. There is no separate storage layer.
    }
    N1[("ES node")]
    N2[("ES node")]
    N3[("ES node")]
    MX["MariaDB MaxScale"]
    MX -->|ro| N1
    MX -->|rw| N2
    MX -->|ro| N3
    N1 <-->|"Galera<br/>(virtually sync)"| N2
    N2 <-->|"Galera<br/>(virtually sync)"| N3
    N1 <-->|"Galera<br/>(virtually sync)"| N3
    classDef node fill:#e2f0f2,stroke:#0a5a6b,stroke-width:2px,color:#111;
    class MX,N1,N2,N3 node
```

_MaxScale routes to three ES nodes that replicate synchronously with each other as a Galera cluster._

<ul><li><strong>Multi-Master Cluster Powered by Galera for Transactional/OLTP Workloads</strong></li><li>InnoDB Storage Engine</li><li>Highly available</li><li>Virtually synchronous, certification-based replication</li><li>Automated provisioning of new nodes (IST/SST)</li><li>Scales reads via MaxScale</li><li><p>Enterprise Server 10.3+, MariaDB Enterprise Cluster</p><p>(powered by Galera), MaxScale 2.5+</p></li></ul>

### Analytical (OLAP, Data Warehousing, DSS)

#### ColumnStore Object Storage

MariaDB Enterprise ColumnStore offers a highly available, columnar storage engine with S3-compatible object storage for data warehousing and analytics. It features automatic failover via MaxScale and CMAPI, read scaling through MaxScale, and efficient bulk data import. It's supported on Enterprise Server 10.5 and 10.6 with corresponding ColumnStore and MaxScale versions.

```mermaid
flowchart TD
    accTitle: MaxScale routing to three ES ColumnStore nodes sharing S3 object storage
    accDescr {
        A MaxScale proxy routes read-only traffic to two ES ColumnStore nodes and read-write
        traffic to one node. Each of the three ES nodes runs a ColumnStore storage-engine
        layer, and all three ColumnStore layers share a single S3-compatible object storage
        bucket for their data.
    }
    E1[("ES")]
    E2[("ES")]
    E3[("ES")]
    C1[("ColumnStore")]
    C2[("ColumnStore")]
    C3[("ColumnStore")]
    S3[("S3")]
    MX["MariaDB MaxScale"]
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
    classDef storage fill:#fdebd0,stroke:#8a5a00,stroke-width:2px,color:#111;
    class MX,E1,E2,E3,C1,C2,C3 node
    class S3 storage
```

_MaxScale routes to three ES/ColumnStore nodes, all sharing S3-compatible object storage._

<ul><li><strong>Columnar storage engine with S3-compatible object storage</strong></li><li>Highly available</li><li>Automatic failover via MaxScale and CMAPI</li><li>Scales reads via MaxScale</li><li>Bulk data import</li><li>Enterprise Server 10.5, Enterprise ColumnStore 5, MaxScale 2.5</li><li>Enterprise Server 10.6, Enterprise ColumnStore 23.02, MaxScale 22.08</li></ul>

#### ColumnStore Shared Local Storage

MariaDB Enterprise ColumnStore, utilizing shared local storage, delivers a highly available columnar solution. It features automatic failover via MaxScale and CMAPI, scales reads through MaxScale, and enables bulk data imports. This setup is compatible with Enterprise Server 10.5 and 10.6, alongside specific Enterprise ColumnStore and MaxScale versions.

```mermaid
flowchart TD
    accTitle: MaxScale routing to three ES ColumnStore nodes sharing NFS storage
    accDescr {
        A MaxScale proxy routes read-only traffic to two ES ColumnStore nodes and read-write
        traffic to one node. Each of the three ES nodes runs a ColumnStore storage-engine
        layer, and all three ColumnStore layers share a single NFS storage volume for their
        data.
    }
    E1[("ES")]
    E2[("ES")]
    E3[("ES")]
    C1[("ColumnStore")]
    C2[("ColumnStore")]
    C3[("ColumnStore")]
    NFS[("NFS")]
    MX["MariaDB MaxScale"]
    MX -->|ro| E1
    MX -->|rw| E2
    MX -->|ro| E3
    E1 --- C1
    E2 --- C2
    E3 --- C3
    NFS -.-> C1
    NFS -.-> C2
    NFS -.-> C3
    classDef node fill:#e2f0f2,stroke:#0a5a6b,stroke-width:2px,color:#111;
    classDef storage fill:#fdebd0,stroke:#8a5a00,stroke-width:2px,color:#111;
    class MX,E1,E2,E3,C1,C2,C3 node
    class NFS storage
```

_MaxScale routes to three ES/ColumnStore nodes, all sharing NFS storage._

<ul><li><strong>Columnar storage engine with shared local storage</strong></li><li>Highly available</li><li>Automatic failover via MaxScale and CMAPI</li><li>Scales reads via MaxScale</li><li>Bulk data import</li><li>Enterprise Server 10.5, Enterprise ColumnStore 5, MaxScale 2.5</li><li>Enterprise Server 10.6, Enterprise ColumnStore 23.02, MaxScale 22.08</li></ul>

### Hybrid Workloads

#### HTAP

MariaDB's single-stack solution handles hybrid transactional/analytical workloads by combining ColumnStore for analytics with S3-compatible object storage and InnoDB for transactions. It supports cross-engine JOINs for comprehensive queries. This offering is available with Enterprise Server 10.5 or 10.6, paired with specific Enterprise ColumnStore and MaxScale versions.

```mermaid
flowchart TD
    accTitle: MaxScale routing HTAP traffic to a single ES node with ColumnStore and InnoDB
    accDescr {
        A MaxScale proxy routes read-write HTAP traffic to a single Enterprise Server node.
        That node reads and writes to both a ColumnStore engine for OLAP queries and an
        InnoDB engine for OLTP queries. InnoDB replicates to ColumnStore through HTAP
        Replication, and ColumnStore stores its data on S3-compatible object storage.
    }
    ES[("ES")]
    CS[("ColumnStore")]
    IN[("InnoDB")]
    S3[("S3")]
    MX["MariaDB MaxScale"]
    MX -.->|"rw (HTAP)"| ES
    ES ---|"rw (OLAP)"| CS
    ES ---|"rw (OLTP)"| IN
    IN -->|"HTAP Replication"| CS
    S3 -.-> CS
    classDef node fill:#e2f0f2,stroke:#0a5a6b,stroke-width:2px,color:#111;
    classDef storage fill:#fdebd0,stroke:#8a5a00,stroke-width:2px,color:#111;
    class MX,ES,CS,IN node
    class S3 storage
```

_MaxScale routes HTAP traffic to one ES node, which fans out to ColumnStore and InnoDB with replication between them._

<ul><li><strong>Single-stack hybrid transactional/analytical workloads</strong></li><li>ColumnStore for analytics with scalable S3-compatible object storage</li><li>InnoDB for transactions</li><li>Cross-engine JOINs</li><li>Enterprise Server 10.5, Enterprise ColumnStore 5, MaxScale 2.5</li><li>Enterprise Server 10.6, Enterprise ColumnStore 23.02, MaxScale 22.08</li></ul>

{% @marketo/form formId="4316" %}
