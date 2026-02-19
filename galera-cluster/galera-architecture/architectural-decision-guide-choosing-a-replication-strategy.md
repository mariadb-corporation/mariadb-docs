# Architectural Decision Guide: Choosing a Replication Strategy

Choosing the right replication strategy in MariaDB is less about the underlying technology itself and more about which specific "pain point" your architecture needs to solve: preventing downtime, accelerating slow reads, securing data across distances, or aggregating data for analytics.

This guide helps you determine which replication method and format to choose for your cluster, and what trade-offs you will make.

## Choosing a Replication Format

Before choosing a cluster topology, you must establish how the data changes are recorded in the binary log. MariaDB offers three primary replication formats:

* [Row-Based Replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/row-based-replication-with-no-primary-key) (RBR) \[Recommended]: This format replicates the actual row changes rather than the SQL statements. If your goal is "carrier-grade" reliability and absolute data consistency across replicas, RBR is the required choice. While it can consume more memory and network bandwidth, this overhead is negligible for typical OLTP workloads.
* Mixed Format \[Default]: MariaDB makes a best-effort approach, defaulting to Statement-Based Replication but automatically switching to Row-Based Replication when it detects a statement that is not safe to replicate consistently.
* [Statement-Based Replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication) (SBR) \[Fallback Only]: SBR replicates the exact SQL queries executed. While it uses very little CPU and network bandwidth, SBR is generally considered unreliable for modern high-availability setups due to the high risk of data inconsistency. It should only be used as a fallback solution in edge cases where RBR fails (e.g., executing a single query that updates a massive number of rows at once, which would otherwise bloat the [binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log)).

## Choosing a Strategy by Use Case

Once your foundation is set, choose a topology based on your primary architectural goal.

{% tabs %}
{% tab title="High Availability (HA)" %}
{% hint style="info" %}
You need zero data loss and automatic failover. If one server dies, another takes over instantly without impacting the application.
{% endhint %}

* [Galera Cluster](../high-availability/understanding-quorum-monitoring-and-recovery.md) (Virtually Synchronous): The "gold standard" for local high availability. It is a synchronous, multi-primary solution where every node has the exact same data at the same time.
  * _Trade-off:_ Write latency is dictated by the slowest node, as all active nodes must acknowledge the transaction.
* [MariaDB Advanced Cluster](https://mariadb.com/resources/blog/redefining-high-availability-introducing-mariadb-advanced-cluster-technical-preview/) (Quorum/Raft): _(Enterprise Technical Preview)_ Designed for environments that need HA but cannot afford Galera's write latency. It requires acknowledgment from only a _majority_ (quorum) of nodes to commit a write, effectively ignoring network lag from the slowest data centers.
* [Semisynchronous Replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/semisynchronous-replication): A middle ground where the primary server waits for at least one replica to acknowledge receipt of the data before confirming a "success" to the client. It prevents data loss during a crash without the full performance overhead of Galera.
{% endtab %}

{% tab title="Read Scaling" %}
{% hint style="info" %}
Your application has thousands of users browsing (reading) but only a few writing, and you need to offload the read workload to maintain performance.
{% endhint %}

* Primary-Replica (Asynchronous): One "Primary" handles all data changes, while changes are streamed in the background to multiple "Replicas" that handle the read queries. This offers the highest performance for scaling high-traffic apps.&#x20;
  * Trade-off: You risk momentary replication lag and potential data loss if the primary crashes before streaming its latest updates.
{% endtab %}

{% tab title="Disaster Recovery" %}
{% hint style="info" %}
You need a "Plan B" in a different geographic region to survive a total data center outage, or you need a safeguard against catastrophic human error.
{% endhint %}

* [Hybrid Replication](../high-availability/using-mariadb-replication-with-mariadb-galera-cluster/overview-of-hybrid-replication.md) (Geo-DR): Combines methods for the best of both worlds. A synchronous Galera Cluster is used locally for High Availability, while standard asynchronous replication streams data to a distant Disaster Recovery (DR) replica over a WAN.
* [Delayed Replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/delayed-replication) (Human Error DR): A replica that intentionally stays a set amount of time (e.g., one hour) behind the primary. If a user accidentally runs a destructive command like `DROP TABLE`, you can recover the lost data from the delayed replica before the mistake replicates across your infrastructure.
{% endtab %}

{% tab title="Data Analytics" %}
{% hint style="info" %}
You need to pull data from many different live production databases into one centralized location for reporting, without slowing down your production apps.
{% endhint %}

* [Multi-Source Replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/multi-source-replication): One replica is configured to receive data streams from several different primary servers concurrently. This is perfect for populating a centralized Data Warehouse where you can run heavy analytical queries entirely isolated from your live production environments.
{% endtab %}
{% endtabs %}

## The Role of MariaDB MaxScale

Managing replication topologies—especially handling automatic failover and routing in Asynchronous or Semisynchronous environments—can be highly complex.

This is where [MariaDB MaxScale](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-quickstart-guides/maxscale-beginner-guide#introduction) is typically introduced. While not a replication engine itself, MaxScale is an advanced database proxy that sits between your application and your database cluster.

* [Read/Write Splitting](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-tutorials/read-write-splitting): It acts as a traffic cop, automatically routing `SELECT` queries to your replicas and `INSERT`/`UPDATE` queries to your primary.
* [Automated Failover](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-tutorials/automatic-failover-with-mariadb-monitor): If a primary node fails, MaxScale can automatically promote a replica and reroute traffic without application downtime.

{% hint style="info" %}
MaxScale is a commercial MariaDB Enterprise product, which should be factored into your architectural decision-making. For technical implementation details, refer to the [MaxScale documentation](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/).
{% endhint %}

## Quick Comparison Decision Matrix

| Architectural Goal      | Recommended Solution       | Consistency Type              | Key Trade-off / Benefit                              |
| ----------------------- | -------------------------- | ----------------------------- | ---------------------------------------------------- |
| No Downtime (Local HA)  | Galera Cluster             | Synchronous                   | Guarantees zero data loss, but slower writes.        |
| No Downtime (Geo HA)    | MariaDB Advanced Cluster   | Quorum (Raft)                 | Faster writes across WAN, but Enterprise-only.       |
| Read Scaling            | Primary-Replica + MaxScale | Asynchronous                  | Maximum performance, but risks replication lag.      |
| Disaster Recovery (WAN) | Hybrid Replication         | Sync (Local) / Async (Remote) | Safely bridges data centers, but setup is complex.   |
| Reporting / BI          | Multi-Source Replication   | Asynchronous                  | Safely aggregates data without impacting production. |
| Human Error Recovery    | Delayed Replication        | Asynchronous (Delayed)        | Saves against accidental `DROP TABLE`executions.     |
