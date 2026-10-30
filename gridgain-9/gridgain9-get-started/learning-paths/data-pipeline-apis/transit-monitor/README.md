---
hidden: true
description: >-
  Build a real-time transit monitoring system that ingests GTFS feeds, stores time-series data in Apache Ignite 3, and runs SQL-based monitoring queries.
---

# Build a Real-Time Transit Monitor

<!-- TODO (not tested): This series was not run end to end on GridGain 9. It describes the companion repository maglietti/transit-monitor, which targets Apache Ignite 3.0.0 and needs a live GTFS realtime feed. Compiled against the GridGain 9.1.28 client, the repository fails in 13 places (SchemaSetupExample, MonitorService, ReportingService), all the same ambiguous `sql().execute(null, ...)` call. Fix the repository or point to a GridGain 9 fork, run it against a GridGain 9 cluster, then delete this comment. -->

{% hint style="info" %}
This tutorial uses Apache Ignite 3. The companion repository was written for Apache Ignite 3.0.0. To run it against GridGain 9.1.28, make these changes after cloning it:

- In `pom.xml`, set `ignite.version` to `9.1.28`, change the `ignite-client` group ID from `org.apache.ignite` to `org.gridgain`, and add the GridGain repository (`https://www.gridgainsystems.com/nexus/content/repositories/external`).
- In `SchemaSetupExample`, `MonitorService` and `ReportingService`, cast the null transaction in all 13 `sql().execute(null, ...)` calls: `execute((Transaction) null, ...)`. A bare `null` is ambiguous because `IgniteSql` also has an `execute(String, Object...)` overload. Import `org.apache.ignite.tx.Transaction`.
- Start the cluster with the GridGain 9 Docker image from [How to Start a Cluster with Docker Compose](../../../start-cluster-docker-compose.md), not the Apache Ignite one. In GridGain 9, `cluster init` requires a license (`--license <file>`).
{% endhint %}

Transit data combines real-time streams, time-series storage, geospatial tracking, and complex queries, making it an ideal context for learning Ignite's distributed data capabilities. In this tutorial, you build a real-time transit monitoring system that exercises all of these patterns.

## What You Learn

- Connect to real-time GTFS transit data feeds
- Model time-series data with Ignite 3 schema annotations
- Build a batch ingestion pipeline with transaction support
- Write SQL analytics queries against distributed data
- Detect service anomalies using polling-based monitoring

## What You Build

By the end of this tutorial, the application produces a live console dashboard:

```text
╔══════════════════════════════════════════════════════╗
║            TRANSIT MONITORING DASHBOARD              ║
╚══════════════════════════════════════════════════════╝
Current time: 2023-05-21 14:22:38

SUMMARY VIEW
────────────────────────────────────────────────────────────────
ACTIVE VEHICLES BY ROUTE (last 15 minutes)
• Route 14      : 32 vehicles ↑
• Route 5       : 30 vehicles =
• Route 38      : 28 vehicles ↓
• Route 1       : 26 vehicles =
• Route 8       : 24 vehicles ↑

VEHICLE STATUS DISTRIBUTION
• IN_TRANSIT_TO  : 342 vehicles ↑
• STOPPED_AT     : 198 vehicles ↓

DATA INGESTION STATUS
• Status: Running
• Total records fetched: 45,280
• Total records stored: 45,280
• Last fetch count: 540
• Last fetch time: 876ms
• Running time: 01:23:45
• Ingestion rate: 9.12 records/second

Views rotate automatically every 10 seconds
Press ENTER at any time to exit
```

The application connects to real-time transit data feeds, stores vehicle positions in a distributed Ignite database, analyzes movement patterns, and alerts operators to potential service disruptions. The system architecture includes:

- A clustered Ignite database for distributed storage
- A data ingestion pipeline for real-time updates
- SQL-based analytics for operational insights
- A monitoring system for service disruptions
- A real-time console dashboard for visualization

## Prerequisites

- **Java 11 or later** installed and properly configured
- **Maven 3.6+** for dependency management
- **Docker 20.10+** and Docker Compose for running the Ignite 3 cluster
- **IDE** such as IntelliJ IDEA or VS Code with Java extensions
- **Basic Java knowledge**, including familiarity with classes, interfaces, and collections
- **Some SQL experience** for understanding the query examples

## Tutorial Modules

This tutorial consists of 6 modules that build incrementally:

1. **[Project Setup](project-setup.md)** - Configure environment and dependencies
2. **[Understanding GTFS](understanding-gtfs.md)** - The transit data format and Ignite schema
3. **[GTFS Client](gtfs-client.md)** - Build the data fetching component
4. **[Data Ingestion](data-ingestion.md)** - Create the data pipeline
5. **[Service Monitoring](continuous-query.md)** - Implement analytics and alerts
6. **[Putting It All Together](putting-together.md)** - Complete application integration

## Source Code

The complete source code is available on GitHub:

**Repository:** https://github.com/maglietti/transit-monitor

```bash
git clone https://github.com/maglietti/transit-monitor.git
cd transit-monitor
```

Each module builds on the previous ones, with clear checkpoints to validate progress. Complete the modules in a single session or spread them across multiple days.

Start with [Module 1: Project Setup](project-setup.md) to set up the project structure and configure the Ignite cluster.
