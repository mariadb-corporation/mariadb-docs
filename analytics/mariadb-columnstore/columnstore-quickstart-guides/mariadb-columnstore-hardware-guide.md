---
description: Quickstart guide for MariaDB ColumnStore hardware requirements
---

# MariaDB ColumnStore Hardware Guide

## Overview

MariaDB ColumnStore is designed for analytical workloads and scales linearly with hardware resources. While the performance generally improves with more CPU cores, memory, and servers, understanding the minimum hardware specifications is crucial for successful deployment, especially in development and production environments.

MariaDB ColumnStore's performance directly benefits from additional hardware resources. More CPU cores enable greater parallel processing, increased memory allows for more data caching (reducing I/O), and more servers enable a larger distributed architecture.

## Minimum Hardware Recommendations

The specifications differentiate between a basic development environment and a production-ready setup:

**1. For Development Environments:**

* **CPU:** A minimum of **8 CPU cores**.
* **Memory (RAM):** A minimum of **32 GB**.
* **Storage:** Local disk storage is acceptable for development purposes.

**2. For Production Environments:**

* **CPU:** A minimum of **64 CPU cores**.
  * _Note:_ This recommendation underscores the highly parallel nature of ColumnStore, which can effectively utilize a large number of cores for analytical processing.
* **Memory (RAM):** A minimum of **128 GB**.
  * _Note:_ Adequate memory is critical for caching data and intermediate results, directly impacting query performance.
* **Storage:** **StorageManager (S3)** is recommended.
  * _Note:_ This implies leveraging cloud-object storage (like AWS S3 or compatible services) for scalable and durable data persistence in production.

## Network Interconnectivity (for Multi-Server Deployments)

* **Minimum Network:** For multi-server ColumnStore deployments, a minimum of a **1 Gigabit (1G) network** is recommended.
  * _Note:_ This facilitates efficient data transfer between nodes via TCP/IP for replication and query processing across the distributed architecture. For optimal performance in heavy-load scenarios, higher bandwidth (e.g., 10G or more) is highly beneficial.

Adhering to these minimum specifications will provide a baseline for ColumnStore functionality. For specific workload requirements, it's always advisable to conduct performance testing and scale hardware accordingly.

## See Also

* [MariaDB ColumnStore Minimum Hardware Specification Documentation](../management/deployment/columnstore-minimum-hardware-specification.md)
* [MariaDB ColumnStore Overview](https://mariadb.com/products/columnstore/)
* [MariaDB documentation: MariaDB ColumnStore](../)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
