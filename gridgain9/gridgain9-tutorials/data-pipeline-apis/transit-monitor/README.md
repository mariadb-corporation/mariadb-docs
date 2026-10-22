---
hidden: true
description: >-
  Build a real-time transit monitoring system that ingests GTFS feeds, stores time-series data in Apache Ignite 3, and runs SQL-based monitoring queries.
---

# Build a Real-Time Transit Monitor

{% hint style="info" %}
This tutorial uses Apache Ignite 3. The Java code works unchanged with GridGain 9. The Docker image, the Maven coordinates, and the `cluster init` command differ: in GridGain 9, `cluster init` requires a license (`--license <file>`). Use the GridGain 9 Docker image and Maven coordinates from [How to Start a Cluster with Docker Compose](../../../gridgain9-management/installation/start-cluster-docker-compose.md) if you are using GridGain.
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
