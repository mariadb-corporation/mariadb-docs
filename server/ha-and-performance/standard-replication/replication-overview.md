---
description: >-
  Explore the core concepts of MariaDB standard replication. Learn about the
  primary-replica architecture, data redundancy strategies, and how to scale
  read operations effectively.
---

# Replication Overview

{% hint style="info" %}
In MariaDB 11.8, the default character set and collation have changed. This has implications on replicating to older replicas, particularly replicas running MariaDB 10.6 or older.

See [this section](../../reference/data-types/string-data-types/character-sets/setting-character-sets-and-collations.md#default-character-set-and-collation-changes) for details, and how to configure MariaDB 11.8+ primaries to replicate to older replicas.
{% endhint %}

## Overview

Replication is a feature allowing the contents of one or more servers (called primaries) to be mirrored on one or more servers (called replicas).

You can exert control over which data to replicate. All databases, one or more databases, or tables within a database can each be selectively replicated.

The main mechanism used in replication is the [binary log](../../server-management/server-monitoring-logs/binary-log/). If binary logging is enabled, all updates to the database (data manipulation and data definition) are written into the binary log as binlog events. Replicas read the binary log from each primary in order to access the data to replicate. A [relay log](../../server-management/server-monitoring-logs/binary-log/relay-log.md) is created on the replica, using the same format as the binary log, and this is used to perform the replication. Old relay log files are removed when no longer needed.

A replica server keeps track of the position in the primary's binlog of the last event applied on the replica. This allows the replica server to re-connect and resume from where it left off after replication has been temporarily stopped. It also allows a replica to disconnect, be cloned and then have the new replica resume replication from the same primary.

Primaries and replicas do not need to be in constant communication with each other. It's quite possible to take servers offline or disconnect from the network, and when they come back, replication will continue where it left off.

## Replication Formats

There are three kinds of replication format – essentially, they're binary log formats, and therefore documented on this page: [Binary Log Formats](../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md):

* Statement-based replication (SBR)
* Row-based replication (RBR)
* Mixed replication

## Replication Uses

Replication is used in a number of common scenarios. Uses include:

* Scalability. By having one or more replicas, reads can be spread over multiple servers, reducing the load on the primary. The most common scenario for a high-read, low-write environment is to have one primary, where all the writes occur, replicating to multiple replicas, which handle most of the reads.
* Data analysis. Analyzing data may have too much of an impact on a primary server, and this can similarly be handled on a replica, while the primary continues unaffected by the extra load.
* Backup assistance. [Backups](../../server-usage/backup-and-restore/) can more easily be run if a server is not actively changing the data. A common scenario is to replicate the data to a replica, which is then disconnected from the primary with the data in a stable state. Backup is then performed from this server. See [Replication as a Backup Solution](../../server-usage/backup-and-restore/replication-as-a-backup-solution.md).
* Distribution of data. Instead of being connected to a remote primary, it's possible to replicate the data locally and work from this data instead.

## Common Replication Setups

### Standard Replication

```mermaid
flowchart TD
    accTitle: Standard primary/replica replication
    accDescr {
        A single primary replicates asynchronously to several replicas. One replica in
        turn acts as a primary for a further downstream replica, forming a replication
        chain.
    }
    P[("MariaDB<br/>Primary")]
    R1[("MariaDB<br/>Replica")]
    R2[("MariaDB<br/>Replica")]
    R3[("MariaDB<br/>Replica")]
    R4[("MariaDB<br/>Replica")]
    P --> R1
    P --> R2
    P --> R3
    R3 --> R4
    classDef primary fill:#5cb85c,stroke:#2f7d2f,stroke-width:2px,color:#111;
    classDef replica fill:#f0932b,stroke:#b5701d,stroke-width:2px,color:#111;
    class P primary
    class R1,R2,R3,R4 replica
```

_Standard replication: one primary fans out to multiple replicas; a replica can chain to a further downstream replica._

* Provides infinite read scale out.
* Provides high-availability by upgrading replica to primary.
* [Setting up standard replication](setting-up-replication.md)

### Ring Replication

```mermaid
flowchart LR
    accTitle: Ring replication
    accDescr {
        Four primaries replicate in a closed ring, each forwarding its changes to the
        next node, so writes propagate all the way around. One node additionally
        replicates to a replica outside the ring.
    }
    A[("MariaDB")]
    B[("MariaDB")]
    C[("MariaDB")]
    D[("MariaDB")]
    S[("MariaDB<br/>Replica")]
    A --> B
    B --> C
    C --> D
    D --> A
    D --> S
    classDef n1 fill:#5cb85c,stroke:#2f7d2f,stroke-width:2px,color:#111;
    classDef n2 fill:#e2453c,stroke:#a52a24,stroke-width:2px,color:#111;
    classDef n3 fill:#3aa0e6,stroke:#1f6fa8,stroke-width:2px,color:#111;
    classDef n4 fill:#9b59b6,stroke:#6f3d84,stroke-width:2px,color:#111;
    classDef replica fill:#f0932b,stroke:#b5701d,stroke-width:2px,color:#111;
    class A n1
    class B n2
    class C n3
    class D n4
    class S replica
```

_Ring replication: each primary replicates to the next in a closed loop; here one node also feeds a replica._

* Provides read and write scaling.
* Doesn’t handle conflicts.
* If one primary fails, replication stops.
* [More about Multi-master ring replication](multi-master-ring-replication.md)

### Ring Replication with slaves

```mermaid
flowchart TD
    accTitle: Ring replication with replicas and delayed replicas
    accDescr {
        Two primaries, on separate replication domains, replicate to each other in a
        ring. Each primary also feeds a replica, and each replica feeds a delayed
        replica, which lags intentionally to guard against human error such as an
        accidental DROP TABLE.
    }
    P1[("MariaDB Primary<br/>Domain 1")]
    P2[("MariaDB Primary<br/>Domain 2")]
    P1 <--> P2
    P1 --> S1[("MariaDB<br/>Replica")]
    P2 --> S2[("MariaDB<br/>Replica")]
    S1 --> D1[("MariaDB<br/>Delayed Replica")]
    S2 --> D2[("MariaDB<br/>Delayed Replica")]
    classDef d1 fill:#3aa0e6,stroke:#1f6fa8,stroke-width:2px,color:#111;
    classDef d2 fill:#5cb85c,stroke:#2f7d2f,stroke-width:2px,color:#111;
    class P1,S1,D1 d1
    class P2,S2,D2 d2
```

_Multi-master ring with replicas: two primaries replicate to each other; each also has a replica and a delayed replica._

* Provides read and write scaling.
* Doesn’t handle conflicts.
* If one primary fails, replication stops.
* [More about Multi-master ring replication](multi-master-ring-replication.md)

### Ring Replication with replication through slaves

```mermaid
flowchart TD
    accTitle: Ring replication relayed through replicas
    accDescr {
        Two primaries on separate domains form a ring that is relayed through their
        replicas: each primary feeds a replica, and each replica forwards changes to the
        other domain's primary. Each replica also feeds a delayed replica.
    }
    M1[("MariaDB Primary 1<br/>Domain 1")]
    M2[("MariaDB Primary 2<br/>Domain 2")]
    M1 --> S1[("MariaDB<br/>Replica 1")]
    M2 --> S2[("MariaDB<br/>Replica 2")]
    S1 --> M2
    S2 --> M1
    S1 --> D1[("MariaDB<br/>Delayed Replica 1")]
    S2 --> D2[("MariaDB<br/>Delayed Replica 2")]
    classDef d1 fill:#3aa0e6,stroke:#1f6fa8,stroke-width:2px,color:#111;
    classDef d2 fill:#5cb85c,stroke:#2f7d2f,stroke-width:2px,color:#111;
    class M1,S1,D1 d1
    class M2,S2,D2 d2
```

_Multi-master ring relayed through replicas: each replica forwards to the other domain's primary, closing the ring._

* Provides read and write scaling.
* Doesn’t handle conflicts.
* If one primary fails, replication stops.
* [More about Multi-master ring replication](multi-master-ring-replication.md)

### Star Replication

```mermaid
flowchart TD
    accTitle: Star (all-to-all) replication
    accDescr {
        Four primaries are fully meshed: every node replicates to and from every other
        node, so each node holds all changes. Replication filters are needed to avoid
        duplicating data.
    }
    A[("MariaDB")]
    B[("MariaDB")]
    C[("MariaDB")]
    D[("MariaDB")]
    A <--> B
    A <--> C
    A <--> D
    B <--> C
    B <--> D
    C <--> D
    classDef n1 fill:#5cb85c,stroke:#2f7d2f,stroke-width:2px,color:#111;
    classDef n2 fill:#e2453c,stroke:#a52a24,stroke-width:2px,color:#111;
    classDef n3 fill:#f0932b,stroke:#b5701d,stroke-width:2px,color:#111;
    classDef n4 fill:#3aa0e6,stroke:#1f6fa8,stroke-width:2px,color:#111;
    class A n1
    class B n2
    class C n3
    class D n4
```

_Star replication: every primary replicates with every other, so all nodes converge to the same data._

* Provides read and write scaling.
* Doesn’t handle conflicts.
* Have to use replication filters to avoid duplication of data.
* [MariaDB Galera Cluster](../../architecture/topologies/galera-cluster/README.md), which is a [virtually synchronous](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/readme/about-galera-replication) multi-primary (multi-master) cluster for MariaDB, has a similar configuration and can handle conflicts.

### Multi-Source Replication

```mermaid
flowchart TD
    accTitle: Multi-source replication
    accDescr {
        One replica receives from two primaries on separate replication domains
        (Domain 1 and Domain 2) and applies both domains in parallel. That replica in
        turn replicates to a downstream replica.
    }
    P1[("MariaDB Primary<br/>Domain 1")]
    P2[("MariaDB Primary<br/>Domain 2")]
    R1[("MariaDB<br/>Replica")]
    R2[("MariaDB<br/>Replica")]
    P1 --> R1
    P2 --> R1
    R1 --> R2
    classDef d1 fill:#3aa0e6,stroke:#1f6fa8,stroke-width:2px,color:#111;
    classDef d2 fill:#5cb85c,stroke:#2f7d2f,stroke-width:2px,color:#111;
    classDef replica fill:#f0932b,stroke:#b5701d,stroke-width:2px,color:#111;
    class P1 d1
    class P2 d2
    class R1,R2 replica
```

_Multi-source replication: one replica pulls from two primaries on separate domains and applies them in parallel._

* Allows you to combine data from different sources.
* Different domains executed independently in parallel on all replicas.
* [More about Multi-Source replication](multi-source-replication.md)

## Cross-Version Replication Compatibility

The following table describes replication compatibility between different MariaDB Community Server versions. In general, the replica should be of the same or a later version than the primary. The constraint also applies to minor/patch releases:

| Replica ↓ / Primary → | [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104) | [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105) | [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/what-is-mariadb-106) | [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/what-is-mariadb-1011) | [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/what-is-mariadb-114) | [MariaDB 11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118) | [MariaDB 12.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/12.3/mariadb-12.3-changes-and-improvements) | [MariaDB 13.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/13.0/mariadb-13.0-changes-and-improvements) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [MariaDB 10.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.4/what-is-mariadb-104) | ✅ | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ |
| [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.5/what-is-mariadb-105) | ✅ | ✅ | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ |
| [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.6/what-is-mariadb-106) | ✅ | ✅ | ✅ | ⛔ | ⛔ | ⛔ | ⛔ | ⛔ |
| [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/what-is-mariadb-1011) | ✅ | ✅ | ✅ | ✅ | ⛔ | ⛔ | ⛔ | ⛔ |
| [MariaDB 11.4](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.4/what-is-mariadb-114) | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ | ⛔ | ⛔ |
| [MariaDB 11.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/11.8/what-is-mariadb-118) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ | ⛔ |
| [MariaDB 12.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/12.3/mariadb-12.3-changes-and-improvements) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ⛔ |
| [MariaDB 13.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/13.0/mariadb-13.0-changes-and-improvements) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

* ✅: This combination is supported.
* ⛔: This combination is not supported.

Note: where it is not officially supported to replicate to a server with a lesser minor version, replication can still be safe for:

* DMLs logged in ROW binlog\_format, and
* DMLS logged in STATEMENT format and DDLs where neither use features that do not yet exist on the replica

provided the configurations for each server allow for consistent behavior in the execution of the events (i.e. the execution of the event should not be reliant on newer configuration variables, character sets/collations, etc, that don't exist on the replica). Additionally note, if binlog\_format=MIXED, it may be possible that the higher-versioned server (primary) may consider it safe to log a transaction using STATEMENT binlog format, while the older-versioned replica categorizes it as unsafe, which will result in an error while the replica tries to execute the transaction. See [this page](unsafe-statements-for-statement-based-replication.md#unsafe-statements) for more details on unsafe statements.

The table shows the general version constraint only; it does not mean that every listed combination is separately tested. Individual releases can introduce changes that affect replication — for example, new data types, changed defaults, or changes to how statements are written to the binary log. Before setting up replication between different versions, review the release notes (the "Changes & Improvements" page) for the versions involved. Any change that affects cross-version replication compatibility is called out there.

{% hint style="info" %}
**MariaDB Enterprise Server:** The table above applies to MariaDB Community Server. MariaDB Enterprise Server releases are based on a Community Server version with additional backported features, so cross-version replication combinations are not separately tested for Enterprise Server. The same general rule applies — a replica should run the same or a later version than its primary — but before replicating between different Enterprise Server versions, or between Enterprise Server and Community Server, review the [MariaDB Enterprise Server release notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/all-releases) for the versions involved for any changes that affect replication.
{% endhint %}

For replication compatibility details between MariaDB and MySQL, see [MariaDB versus MySQL - Compatibility: Replication Compatibility](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/mariadb-vs-mysql-compatibility#replication-compatibility).

## See Also

* [Setting Up Replication](setting-up-replication.md)
* [Replication Compatibility Between MariaDB and MySQL](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/mariadb-vs-mysql-compatibility#replication-compatibility)
* [MariaDB Galera Cluster and M/S replication](https://www.youtube.com/watch?v=Nd0nvltLPdQ) (video)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
