---
description: >-
  MariaDB Exa architecture: MaxScale routes reads and writes while MaxScale CDC
  (binlogrouter) tails the MariaDB binary log and bulk-loads changes into Exasol
  for near real-time analytics on operational data.
icon: house-blank
---

# Architecture

## Overview

MariaDB Exa combines three core components into a single Hybrid Transactional and Analytical Processing (HTAP) system:

| Role | Component | Purpose |
| --- | --- | --- |
| **Router** | MariaDB MaxScale with CDC | Intelligent query routing (SmartRouter + Exasolrouter) and Change Data Capture that synchronizes data from MariaDB to Exasol. |
| **Storage** | MariaDB Enterprise Server | The primary system of record for transactional workloads (OLTP), ensuring data integrity and consistency. |
| **Insights** | Exasol | A high-performance, in-memory, MPP engine purpose-built for extreme OLAP query performance. |

Applications use a single MariaDB connection endpoint for both OLTP and analytics. MaxScale decides, per query, whether MariaDB or Exasol answers faster, and keeps Exasol in sync through asynchronous Change Data Capture (CDC).

{% hint style="info" %}
MaxScale-native CDC to Exasol requires **MaxScale 25.10.3 or later**. Earlier integrations based on Debezium and Kafka are superseded and no longer used.
{% endhint %}

## Data flow (write path)

Writes always go to MariaDB. MaxScale CDC connects to MariaDB as a replica, tails the binary log, and applies committed changes to Exasol in GTID order, so Exasol reflects committed writes with minimal lag. Replication is asynchronous.

```mermaid
flowchart LR
    App["Application<br/>MariaDB connector"]
    subgraph MS["MaxScale"]
        SR["Smart Router<br/>routes writes and reads"]
        CDC["MaxScale CDC<br/>tails binlog, applies to Exasol"]
    end
    MDB["MariaDB<br/>transactional core, binlog, GTID"]
    EXA["Exasol<br/>analytics engine, columnar"]
    App -->|"1 - reads and writes"| SR
    SR ==>|"2 - write committed to binlog"| MDB
    MDB -.->|"3 - CDC tails binlog (async)"| CDC
    CDC -.->|"4 - applies change + GTID"| EXA
    classDef app fill:#eef2f7,color:#0e2a3b,stroke:#0e2a3b;
    classDef ms fill:#0e2a3b,color:#fff,stroke:#0e2a3b;
    classDef maria fill:#2e7d64,color:#fff,stroke:#204d40;
    classDef exa fill:#1f8fa3,color:#fff,stroke:#155f6e;
    class App app;
    class SR,CDC ms;
    class MDB maria;
    class EXA exa;
    style MS fill:#eef2f7,color:#0e2a3b,stroke:#0e2a3b;
```

_Solid arrows show the synchronous write path; dotted arrows show asynchronous CDC replication._

## Query flow (read path)

For reads, the SmartRouter learns which engine answers each query faster and routes accordingly:

{% stepper %}
{% step %}
**Read request**

The application sends a read to the single MaxScale endpoint.
{% endstep %}

{% step %}
**First time: race both engines**

When SmartRouter first sees a query (in its canonical form, with constants replaced by placeholders), it runs it on both MariaDB and Exasol simultaneously.
{% endstep %}

{% step %}
**Fastest wins**

The first engine to respond returns the result; the slower query is cancelled.
{% endstep %}

{% step %}
**Winner cached**

SmartRouter caches the winning engine, so future reads of the same canonical query route straight to it. The decision is re-measured on an escalating schedule (2, 5, 10, then 20 minutes), so routing stays correct as data volume and distribution change.
{% endstep %}
{% endstepper %}

```mermaid
flowchart LR
    App["Application<br/>MariaDB connector"]
    subgraph MS["MaxScale"]
        SR["Smart Router<br/>routes to the faster engine"]
        TC["Token cache<br/>caches the winning engine per query"]
    end
    MDB["MariaDB<br/>transactional core, row store"]
    EXA["Exasol<br/>analytics engine, columnar"]
    App -->|"1 - read request"| SR
    SR -.->|"2 - first time: raced on both"| MDB
    SR -.->|"2 - first time: raced on both"| EXA
    SR --- TC
    classDef app fill:#eef2f7,color:#0e2a3b,stroke:#0e2a3b;
    classDef ms fill:#0e2a3b,color:#fff,stroke:#0e2a3b;
    classDef maria fill:#2e7d64,color:#fff,stroke:#204d40;
    classDef exa fill:#1f8fa3,color:#fff,stroke:#155f6e;
    class App app;
    class SR,TC ms;
    class MDB maria;
    class EXA exa;
    style MS fill:#eef2f7,color:#0e2a3b,stroke:#0e2a3b;
```

## Deployment topologies

MariaDB Exa supports four topologies, differing in scale and how analytics clients reach Exasol:

| Topology | MariaDB / MaxScale / Exasol | Routing strategy | Typical use |
| --- | --- | --- | --- |
| **Micro** | 1 / 1 / 1 | HTAP SmartRouter | Development and functional testing |
| **Standard** | Primary + replicas / 2 / cluster + standby | HTAP SmartRouter | Production HTAP: one endpoint for OLTP and OLAP |
| **Exasol Router** | Primary + replicas / 2 / cluster + standby | Exasolrouter over the MariaDB wire protocol | BI tools querying Exasol through MaxScale's MariaDB endpoint |
| **Exasol Direct** | Primary + replicas / 2 / cluster + standby | Direct via the Exasol connector | BI tools connecting straight to Exasol with its native connector |

In every topology, MaxScale CDC keeps Exasol synchronized from the MariaDB binary log. The **Micro** topology collapses everything to single nodes for testing; **Standard** adds MariaDB replicas, an Exasol cluster with a standby node, and a second MaxScale for high availability. The **Exasol Router** and **Exasol Direct** topologies change only how analytics clients reach Exasol — through MaxScale or directly.

## Change data capture pipeline

MaxScale CDC uses the `binlogrouter` module to read the MariaDB binary log and bulk-load changes into Exasol over the Exasol ODBC driver. Internally each batch runs through four stages before it is applied to Exasol through a staging table and a `MERGE`:

```mermaid
flowchart LR
    C1["01 Capture<br/>tail MariaDB binlog as a replica"]
    C2["02 Compact<br/>collapse row updates to final state"]
    C3["03 Batch<br/>accumulate many rows per write"]
    C4["04 Bulk insert<br/>apply to Exasol in one transaction, matching GTID"]
    C1 --> C2 --> C3 --> C4
    C4 --> M["Staging table + MERGE<br/>bulk-load into _stagingN,<br/>then MERGE inserts, updates, deletes atomically"]
    classDef step fill:#eef4f1,stroke:#2e7d64,color:#0e2a3b;
    classDef merge fill:#0e2a3b,color:#fff,stroke:#0e2a3b;
    class C1,C2,C3,C4 step;
    class M merge;
```

For the full configuration procedure, see the [MariaDB MaxScale Exasolrouter Tutorial](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-tutorials/mariadb-maxscale-exasolrouter). Pipeline tuning parameters are covered in [Performance & Benchmarking](performance-and-benchmarking.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
