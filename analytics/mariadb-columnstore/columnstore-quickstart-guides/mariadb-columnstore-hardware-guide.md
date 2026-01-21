---
description: >-
  This page details MariaDB ColumnStore hardware requirements (CPU, RAM,
  storage, and network).
---

# MariaDB ColumnStore Hardware Guide

## Overview

MariaDB ColumnStore is designed for analytical workloads and scales linearly with hardware resources. While the performance generally improves with more CPU cores, memory, and servers, understanding the minimum hardware specifications is crucial for successful deployment, especially in development and production environments.

MariaDB ColumnStore's performance directly benefits from additional hardware resources:

* **More CPU cores** enable greater parallel processing, improving query processing time.
* **More memory** allows for more data caching (reducing I/O), and more servers enable a larger distributed architecture.
* **HDDs vs. SSDs:** SSD[^1]s don't deliver as much benefit as you might assume because ColumnStore is optimized towards block streaming, which usually performs well enough on HDD[^2]s.
* **Bare metal vs. virtual servers:** Bare metal servers are recommended — they provide additional performance because ColumnStore can fully consume CPU cores and memory.

## Minimum Hardware Recommendations

The specifications differentiate between a basic development environment and a production-ready setup:

### **For Development Environments**

* **CPU:** A minimum of **8 CPU cores**.
* **Memory (RAM):** A minimum of **32 GB**.
* **Storage:** Local disk storage is acceptable for development purposes.

### **For Production Environments**

* **CPU:** A minimum of **64 CPU cores**.
  * This recommendation underscores the highly parallel nature of ColumnStore, which can effectively utilize a large number of cores for analytical processing.
* **Memory (RAM):** A minimum of **128 GB**.
  * Adequate memory is critical for caching data and intermediate results, directly impacting query performance.
* **Storage:** **StorageManager (S3)** is recommended.
  * This implies leveraging cloud-object storage (like AWS S3 or compatible services) for scalable and durable data persistence in production.

## Network Interconnectivity

Network interconnectivity plays a role for multi-server deployments.

* **Minimum Network:** A minimum of a **1 Gigabit (1G) network** is recommended.
  * This facilitates efficient data transfer between nodes via TCP/IP for replication and query processing across the distributed architecture. For optimal performance in heavy-load scenarios, higher bandwidth (for instance, 10G or more) is highly beneficial.

Adhering to these minimum specifications will provide a baseline for ColumnStore functionality. For specific workload requirements, it's always advisable to conduct performance testing and scale hardware accordingly.

## AWS Instance Sizes <a href="#aws-instance-sizes" id="aws-instance-sizes"></a>

For AWS, ColumnStore internal testing generally uses `m4.4xlarge` instance types as a cost-effective middle ground. The `R4.8xlarge` has also been tested, and performs about twice as fast for about twice the price.

## See Also

* [MariaDB ColumnStore Minimum Hardware Specification Documentation](/broken/pages/ksFdboCNE70th9VaY7pM)
* [MariaDB ColumnStore Overview](https://mariadb.com/products/columnstore/)
* [MariaDB documentation: MariaDB ColumnStore](../)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}

[^1]: Solid state drive

[^2]: Hard disk drive
