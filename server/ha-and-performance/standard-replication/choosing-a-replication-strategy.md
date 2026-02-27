# Choosing a Replication Strategy

Choosing the right replication strategy in MariaDB is less about the underlying technology itself and more about which specific "pain point" your architecture needs to solve: preventing downtime, accelerating slow reads, securing data across distances, or aggregating data for analytics.

This guide helps you determine which replication method and format to choose for your cluster, and what trade-offs you will make.

## Overview of Replication Methods

Before mapping out specific use cases, it is important to understand the four primary replication protocols available in the MariaDB ecosystem:

### Asynchronous Replication (Primary-Replica)

```mermaid
graph TD
    subgraph Client Application
        W[Content Admins / Writers]
        R[Web Traffic / Readers]
    end

    subgraph Database Cluster
        P[(Primary Node)]
        R1[(Replica 1)]
        R2[(Replica 2)]
        R3[(Replica N)]
    end

    %% Write Path
    W -- "1. Write Transaction" --> P
    P -- "2. Commit Locally & Confirm Success" --> P
    
    %% Async Replication Path (Dashed lines to represent background/delay)
    P -. "3. Background Stream (Replication Lag)" .-> R1
    P -. "3. Background Stream (Replication Lag)" .-> R2
    P -. "3. Background Stream (Replication Lag)" .-> R3

    %% Read Path
    R -- "Read" --> R1
    R -- "Read" --> R2
    R -- "Read" --> R3

    %% Styling
    classDef primary fill:#f9d0c4,stroke:#333,stroke-width:2px;
    classDef replica fill:#d4e6f1,stroke:#333,stroke-width:1px;
    classDef app fill:#f9e79f,stroke:#333,stroke-width:1px;
    
    class P primary;
    class R1,R2,R3 replica;
    class W,R app;
```

The standard method where the primary node commits a transaction locally and streams it to replicas in the background. This method is ideal for read-heavy applications, such as a high-traffic news website where a single primary database handles content updates while multiple replicas serve read-only web traffic to millions of visitors.\
While a momentary delay before a new article appears on all servers is an acceptable trade-off for massive read scalability, this inherent replication lag means users might occasionally read stale data. Furthermore, if the primary server crashes before the background stream catches up, the most recent updates will be permanently lost.

### Semisynchronous Replication

```mermaid
sequenceDiagram
    autonumber
    actor Client as Client App (e.g., Checkout)
    participant Primary as Primary Database
    participant Replica as Replica Database (Backup)

    Client->>Primary: Send Write Transaction
    Primary->>Primary: Prepare & Write to Binary Log
    
    rect rgb(255, 235, 235)
        Note over Primary,Replica: Write Latency Penalty (Round-Trip)
        Primary->>Replica: Stream Transaction Data
        Note right of Primary: Primary pauses and WAITS
        Replica->>Replica: Securely write to Relay Log
        Replica-->>Primary: Send Acknowledgment (ACK)
    end
    
    Primary->>Primary: Commit to Storage Engine
    Primary-->>Client: Confirm Commit Success
    
    Note over Primary, Replica: Crash Caveat: If Primary fails before/during commit, <br/> failover is complex and may require log truncation.
```

A middle ground where the primary waits for at least one replica to acknowledge receipt of the data before confirming a commit. This setup is well-suited for systems like an e-commerce checkout spanning two nearby data centers, where ensuring at least one backup server has securely logged a transaction prevents a "lost order" if the primary loses power.

However, this increased data integrity comes with a strict write latency penalty while the primary waits for the round-trip acknowledgment from the replica. Additionally, if the primary crashes, failover can be complex and might still involve data loss or require truncating the binary log, depending on the server's specific wait configuration.

### Virtually Synchronous Replication (Galera Cluster)

```mermaid
sequenceDiagram
    autonumber
    actor ClientA as Doctor/App A
    actor ClientB as Nurse/App B
    participant Node1 as Galera Node 1 (Primary)
    participant Node2 as Galera Node 2 (Primary)
    participant Node3 as Galera Node 3 (Slowest Node)

    Note over Node1, Node3: True High Availability: All nodes are Active Primaries

    ClientA->>Node1: Write Transaction (e.g., Update Record X)
    Node1->>Node1: Execute Optimistically (Local)
    
    rect rgb(230, 240, 255)
        Note over Node1, Node3: Certification & Replication Phase
        par Broadcast Write-Set
            Node1->>Node2: Send Write-Set
        and
            Node1->>Node3: Send Write-Set
        end
        
        Node2-->>Node1: Certification Passed (ACK)
        Note right of Node3: Trade-off: Write performance dictated by slowest node
        Node3-->>Node1: Certification Passed (Delayed ACK)
    end
    
    Note over Node1, Node3: Guarantee: 100% Up-to-date (Zero Data Loss)
    
    par Simultaneous Commit
        Node1->>Node1: Commit
    and
        Node2->>Node2: Commit
    and
        Node3->>Node3: Commit
    end
    
    Node1-->>ClientA: Confirm Commit Success

    rect rgb(255, 235, 235)
        Note over ClientB, Node3: Trade-off: High Contention Workloads
        ClientB->>Node2: Tries to update SAME Record X simultaneously
        Node2->>Node2: Write-Set Certification Fails (Conflict detected)
        Node2-->>ClientB: Transaction Rollback / Deadlock Error
    end
```

A multi-primary solution where all active nodes must receive and accept a transaction before it commits, guaranteeing zero data loss and true high availability. This is the "gold standard" for environments like a critical healthcare records system hosted within a single enterprise data center, where every updated record is applied simultaneously across all nodes so users always see 100% up-to-date information.

The trade-off for this consistency is that write performance is entirely dictated by the slowest node in the cluster. Additionally, high-contention workloads with multiple clients writing to the same rows on different nodes can result in frequent transaction rollbacks or cluster deadlocks.

### Quorum Replication (MariaDB Enterprise Cluster)

```mermaid
sequenceDiagram
    autonumber
    actor Client as Financial App
    participant NY as Leader Node (New York)
    participant LON as Follower Node (London)
    participant TOK as Follower Node (Tokyo)

    Note over NY, TOK: Raft Quorum: 3 Nodes Total (Majority = 2)

    Client->>NY: Write Transaction (e.g., Transfer Funds)
    NY->>NY: Append to local log (1st vote)
    
    rect rgb(230, 255, 230)
        Note over NY, LON: Fast Path (Quorum Reached)
        par Broadcast Log Entry
            NY->>LON: Replicate Log Entry
        and
            NY->>TOK: Replicate Log Entry
        end
        
        LON-->>NY: Acknowledgment (2nd vote - Fast WAN)
        
        Note over NY, LON: Majority (2 of 3) achieved!
        NY->>NY: Commit Transaction
        NY-->>Client: Confirm Commit Success
    end

    rect rgb(245, 245, 245)
        Note over NY, TOK: Ignored Lag (Furthest Data Center)
        TOK-->>NY: Acknowledgment (Slow WAN)
        Note right of NY: Tokyo's lag does not affect<br/>the client's write latency.
        TOK->>TOK: Commit Transaction locally
    end
```

A Raft-based solution that requires acknowledgment from a _majority_ of nodes (a quorum) rather than all of them, providing robust fault tolerance with faster write performance across wide-area networks.

For example, a globally distributed financial application spanning data centers in New York, London, and Tokyo only needs agreement from two of the three regions to commit data, keeping the application fast by effectively ignoring the network lag of the furthest data center.

### Replication Methods Comparison Matrix

| Replication Method      | Write Performance                         | Data Safety (Node Crash)                           | Automatic Failover                         | Ideal Architectural Fit                                          |
| ----------------------- | ----------------------------------------- | -------------------------------------------------- | ------------------------------------------ | ---------------------------------------------------------------- |
| Asynchronous            | Fastest (No waiting for replicas)         | High Risk (Potential data loss if primary crashes) | No (Requires external tools like MaxScale) | Read-heavy applications and distant Disaster Recovery.           |
| Semisynchronous         | Fast (Waits for only 1 replica)           | Low Risk (Data is backed up before commit)         | No (Requires external tools like MaxScale) | Environments needing strong data safety without full clustering. |
| Virtually Sync (Galera) | Slowest (Dictated by the slowest node)    | Zero Data Loss (All nodes are identical)           | Yes (Built-in cluster membership)          | Local High Availability (Single Data Center).                    |
| Quorum (Raft)           | Fast / Moderate(Dictated by the majority) | Zero Data Loss(Majority quorum agreed)             | Yes (Automated leader election)            | Geo-Distributed High Availability (Multi-Data Center).           |

## Choosing a Strategy by Use Case

Identify your primary architectural challenge below to discover the best-fit replication topology.

### High Availability (HA) & Fault Tolerance

{% hint style="info" %}
Zero data loss and automatic failover. If one server dies, another takes over instantly without impacting the application.
{% endhint %}

* Galera Cluster (Virtually Synchronous): The "gold standard" for local high availability. It is a synchronous, multi-primary solution where every node has the exact same data at the same time.
  * _Trade-off:_ Write latency is dictated by the slowest node, as all active nodes must acknowledge the transaction.
* MariaDB Enterprise Cluster (Quorum/Raft): _(Enterprise Technical Preview)_ Designed for environments that need HA but cannot afford Galera's write latency. It requires acknowledgment from only a _majority_ (quorum) of nodes to commit a write, effectively ignoring network lag from the slowest data centers.
* Semisynchronous Replication: A middle ground where the primary server waits for at least one replica to acknowledge receipt of the data before confirming a "success" to the client. It prevents data loss during a crash without the full performance overhead of Galera.

### Read Scaling & Performance

{% hint style="info" %}
The application has thousands of users browsing (reading) but only a few writing, and you need to offload the read workload to maintain performance.
{% endhint %}

* Primary-Replica (Asynchronous): One "Primary" handles all data changes, while changes are streamed in the background to multiple "Replicas" that handle the read queries. This offers the highest performance for scaling high-traffic apps.
  * Trade-off: You risk momentary replication lag and potential data loss if the primary crashes before streaming its latest updates.

### Geographic Distribution & Disaster Recovery

{% hint style="info" %}
You need a "Plan B" in a different geographic region to survive a total data center outage, or you need a safeguard against catastrophic human error.
{% endhint %}

* Hybrid Replication (Geo-DR): Combines methods for the best of both worlds. A synchronous Galera Cluster is used locally for High Availability, while standard asynchronous replication streams data to a distant Disaster Recovery (DR) replica over a WAN.
* Delayed Replication (Human Error DR): A replica that intentionally stays a set amount of time (e.g., one hour) behind the primary. If a user accidentally runs a destructive command like `DROP TABLE`, you can recover the lost data from the delayed replica before the mistake replicates across your infrastructure.

### Data Aggregation & Analytics

{% hint style="info" %}
To pull data from many different live production databases into one centralized location for reporting, without slowing down your production apps.
{% endhint %}

* Multi-Source Replication: One replica is configured to receive data streams from several different primary servers concurrently. This is perfect for populating a centralized Data Warehouse where you can run heavy analytical queries entirely isolated from your live production environments.

## The Role of MariaDB MaxScale

Managing replication topologies manually can be highly complex. MariaDB MaxScale is an advanced database proxy that sits between your application and your database cluster to automate traffic routing and failover across any replication method:

* In Asynchronous / Semisynchronous Setups: MaxScale acts as a traffic cop, automatically routing `SELECT`queries to your replicas and `INSERT`/`UPDATE` queries to your primary. If the primary fails, MaxScale can automatically promote a replica and reroute traffic without application downtime.
* In Galera Cluster Setups: MaxScale transparently masks node failures or evictions by routing traffic only to healthy nodes. It can also perform intelligent read/write splitting across the cluster to optimize overall throughput.
* In MariaDB Enterprise Cluster Setups: MaxScale automatically detects the current Raft leader to ensure writes are routed appropriately, while load balancing read queries across the follower nodes.

{% hint style="info" %}
MaxScale is a commercial MariaDB Enterprise product, which should be factored into your architectural decision-making. For technical implementation details, refer to the MaxScale documentation.
{% endhint %}

### Quick Comparison Decision Matrix

| Architectural Goal          | Recommended Solution        | Consistency Type              | Key Trade-off / Benefit                                                   |
| --------------------------- | --------------------------- | ----------------------------- | ------------------------------------------------------------------------- |
| No Downtime (Local HA)      | Galera Cluster              | Synchronous                   | Guarantees zero data loss, but slower writes.                             |
| No Downtime (Geo HA)        | MariaDB Enterprise Cluster  | Quorum (Raft)                 | Faster writes across WAN, none                                            |
| Data Safety (Middle Ground) | Semisynchronous Replication | Semisynchronous               | Prevents data loss during crash, but introduces a slight latency penalty. |
| Read Scaling                | Primary-Replica + MaxScale  | Asynchronous                  | Maximum performance, but risks replication lag.                           |
| Disaster Recovery (WAN)     | Hybrid Replication          | Sync (Local) / Async (Remote) | Safely bridges data centers, but setup is complex.                        |
| Reporting / BI              | Multi-Source Replication    | Asynchronous                  | Safely aggregates data without impacting production.                      |
| Human Error Recovery        | Delayed Replication         | Asynchronous (Delayed)        | Saves against accidental `DROP TABLE`executions.                          |

## Choosing a Binary Log Format

Once you select your replication strategy, you must configure how data changes are recorded in the MariaDB binary log. For most high-availability architectures, Row-Based Replication (RBR) or Mixed Format is required to ensure absolute data consistency across replicas.

Statement-Based Replication (SBR) should generally be avoided in HA setups due to reliability concerns, acting only as a fallback for specific bulk-update operations.
