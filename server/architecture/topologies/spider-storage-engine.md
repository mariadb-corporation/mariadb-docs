---
description: >-
  Scale MariaDB horizontally with the Spider storage engine, which shards
  tables across remote nodes through virtual federated tables.
---

# Spider Storage Engine

### Spider Topologies

#### Spider Federated

MariaDB Enterprise Spider enables reading from and writing to tables on remote Enterprise Server nodes. It uses the Spider storage engine for "virtual" Federated Spider Tables, querying Data Tables on Data Nodes (which use non-Spider engines) via a MariaDB foreign data wrapper. This solution supports transactions and is available with Enterprise Server 10.3+.

```mermaid
flowchart LR
    accTitle: Spider Federated topology
    accDescr {
        A client connects to a Spider Node, a MariaDB Enterprise Server running the Spider
        storage engine and holding virtual Federated Spider Tables. Using the MariaDB Spider
        federation (a foreign data wrapper), the Spider Node reads from and writes to a Data
        Table on a separate Data Node, which is another MariaDB Enterprise Server running a
        non-Spider storage engine.
    }
    Client["Client"]
    Spider[("Spider Node<br/>Enterprise Server")]
    Data[("Data Node<br/>Enterprise Server")]
    Client --> Spider
    Spider <-->|"rw · Spider MariaDB federation"| Data
    classDef node fill:#e2f0f2,stroke:#0a5a6b,stroke-width:2px,color:#111;
    classDef client fill:#eeeeee,stroke:#333333,stroke-width:2px,color:#111;
    class Spider,Data node
    class Client client
```

_Spider Federated: a Spider Node reads from and writes to a Data Table on a remote Data Node via the Spider MariaDB federation._

<ul><li><strong>Read from and write to tables on remote ES nodes</strong></li><li>Spider Node uses Spider storage engine for Federated Spider Tables</li><li>Federated Spider Table is a "virtual" table</li><li>Spider uses MariaDB foreign data wrapper to query Data Table on Data Node</li><li>Data Node uses non-Spider storage engine for Data Tables</li><li>Supports transactions</li><li>Enterprise Server 10.3+, Enterprise Spider</li></ul>

#### Spider Sharded

MariaDB Enterprise Spider facilitates horizontal scalability by sharding tables. It uses the Spider storage engine for partitioned "virtual" Sharded Spider Tables, querying Data Tables on Data Nodes (using non-Spider engines) for each partition via a MariaDB foreign data wrapper. This solution supports transactions and is available with Enterprise Server 10.3+.

```mermaid
flowchart LR
    accTitle: Spider Sharded topology
    accDescr {
        A client connects to a Spider Node, a MariaDB Enterprise Server running the Spider
        storage engine and holding a partitioned virtual Sharded Spider Table. Using the
        MariaDB foreign data wrapper, the Spider Node reads from and writes to a Data Table on
        each of several Data Nodes, one per partition (shard); every Data Node is a MariaDB
        Enterprise Server running a non-Spider storage engine.
    }
    Client["Client"]
    Spider[("Spider Node<br/>Enterprise Server")]
    S1[("Data Node<br/>shard 1")]
    S2[("Data Node<br/>shard 2")]
    S3[("Data Node<br/>shard 3")]
    Client --> Spider
    Spider <-->|"rw · Spider sharding"| S1
    Spider <-->|"rw · Spider sharding"| S2
    Spider <-->|"rw · Spider sharding"| S3
    classDef node fill:#e2f0f2,stroke:#0a5a6b,stroke-width:2px,color:#111;
    classDef client fill:#eeeeee,stroke:#333333,stroke-width:2px,color:#111;
    class Spider,S1,S2,S3 node
    class Client client
```

_Spider Sharded: a Spider Node distributes the partitions of a virtual sharded table across multiple Data Nodes (shards) via the Spider foreign data wrapper._

<ul><li><strong>Shard tables for horizontal scalability</strong></li><li>Spider Node uses Spider storage engine for Sharded Spider Tables</li><li>Sharded Spider Table is a partitioned "virtual" table</li><li>Spider uses MariaDB foreign data wrapper to query Data Tables on Data Nodes for each partition</li><li>Data Node uses non-Spider storage engine for Data Tables</li><li>Supports transactions</li><li>Enterprise Server 10.3+, Enterprise Spider</li></ul>

{% include "../../.gitbook/includes/license-copyright-mariadb.md" %}

{% @marketo/form formId="4316" %}
