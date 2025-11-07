---
icon: cloud-sun
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
---

# MariaDB Cloud

## Overview

MariaDB Cloud (previously called SkySQL) is an AI-driven, fully managed Database-as-a-Service (DBaaS), designed to deploy MariaDB and MySQL-compatible workloads across diverse environments including multiple data centers, regions, and cloud providers. It now offers both traditional provisioned and serverless deployment options, catering to a wide range of use cases and workload patterns while preventing over-provisioning. With the addition of the no-code AI Agent builder, developers can easily provide natural language interfaces to their end users to ask questions of the data without SQL expertise.

Originally developed by [MariaDB](http://mariadb.com), MariaDB Cloud is aimed to be the most comprehensive cloud platform for MariaDB. Its robust feature set is the result of years of insights gathered from hundreds of customers running mission-critical workloads.

MariaDB Cloud provides MariaDB and MySQL-compatible workloads with enterprise-grade and production-ready features:

* [Serverless deployment for instant autoscaling](broken-reference)
* [Integrated AI agents for database interaction](cloud-ai/copilot-guide.md)
* [Automated complex database configurations](cloud-management/config/)
* [Cloud-native capabilities with auto-scaling](cloud-management/autonomously-scale-compute-storage.md)
* [Global replication](<High Availability, DR/Setup Global Replication.md>)
* [Automated backups](cloud-data-handling/backup-and-restore/mariadb-backup.md)
* [Advanced security with end-to-end encryption and private connectivity](Security/)
* Compliance and governance features
* Numerous additional powerful capabilities

## MariaDB Cloud: Autonomous, Resilient, End-to-End Secure

It has:

* Sensible defaults
* Consistent configuration
* MariaDB Remote DBA

So you can:

* Start small
* Grow to extreme read-scale
* HA with load balancing
* Security by design
* Purpose-built monitoring
* Adapt to any workload

```mermaid
---
config:
  theme: neutral
  layout: dagre
---
flowchart LR
 subgraph cloud["MariaDB Cloud"]
    direction LR
        nodeId["MaxScale<br>(SQL Proxy)"]
        n1["Replicas<br>in other zones, regions"]
        n2["MariaDB Primary<br>+ replicas"]
  end
 subgraph s1["User Interfaces"]
        n3["MariaDB Cloud<br>Portal UI"]
        n4["MariaDB Cloud<br>Monitoring UI"]
  end
 subgraph s2["Developer API"]
        n6["MariaDB SQL"]
        n7["NoSQL"]
        n8["REST API"]
  end
    nodeId <-.-> n1 & n2
    s1 <--> cloud
    s2 <--> cloud
    cloud --> n9["Alerts<br>Autoscale<br>Monitor"] & n10["Cloud backups"]
    n11["MariaDB Cloud<br>Unified, automated, simple"]
    nodeId@{ shape: hex}
    n1@{ shape: cyl}
    n2@{ shape: cyl}
    n6@{ shape: rect}
    n7@{ shape: rect}
    n8@{ shape: rect}
    n9@{ shape: stored-data}
    n10@{ shape: stored-data}
    n11@{ shape: text}
    style n3 stroke-width:1px,stroke-dasharray: 0,fill:#FFF9C4,stroke:none
    style n4 stroke:none,fill:#FFF9C4
    style n6 stroke-width:1px,stroke-dasharray: 0,fill:#C8E6C9,stroke:none
    style n7 fill:#C8E6C9,stroke:none
    style n8 fill:#C8E6C9,stroke:none
    style cloud fill:#BBDEFB,stroke:#000000
    style n9 fill:#FFE0B2
    style n10 fill:#FFE0B2
    style n11 color:#616161
```
