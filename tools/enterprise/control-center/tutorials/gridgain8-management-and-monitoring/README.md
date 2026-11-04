---
description: >-
  Monitor and manage GridGain 8 clusters in production: storage and cluster health, alerts, tracing, and backups with GridGain Control Center.
---

# GridGain 8 Management and Monitoring Guide

This guide shows how to monitor and manage GridGain 8 clusters in production. It covers the core tasks: monitoring storage and cluster health, configuring alerts, tracing operations to troubleshoot performance, and creating cluster backups.

You work through these on a local setup: you deploy a GridGain 8 cluster and connect it to [GridGain Control Center](../../README.md), then run common management and monitoring scenarios. By the end, you understand the main GridGain management and monitoring workflows and have a working local environment.

## Prerequisites

- **Docker 20.10 or later** with Docker Compose V2
- **Git 2.24 or later**
- A **GridGain Ultimate license file** for the cluster
- A **GridGain Control Center license**, which you upload to Control Center the first time you open it

## Tutorial Modules

Start with the demo application, then continue through the monitoring, alerting, tracing, and backup tasks:

1. **[Start the demo application](starting-streaming-demo.md)** - Deploy the cluster, Control Center, and streaming demo
2. **[Monitor storage usage](storage-monitoring.md)** - Build a dashboard for memory and disk metrics
3. **[Monitor cluster health](cluster-health.md)** - Track node membership, JVM health, and data distribution
4. **[Configure alerts](alerts.md)** - Set up notifications for memory usage and node count
5. **[Trace operation performance](performance-tracing.md)** - Use tracing to find bottlenecks in cluster operations
6. **[Create cluster backups](backups.md)** - Take and restore snapshots to recover from data loss
7. **[Stop the demo application](terminating-streaming-demo.md)** - Shut down the demo cleanly

Start with [Part 1: Start the demo application](starting-streaming-demo.md) to deploy the cluster and streaming demo.
