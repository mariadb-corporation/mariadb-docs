---
description: >-
  MariaDB Cloud is an AI-driven fully managed DBaaS for MariaDB and MySQL
  workloads, supporting provisioned and serverless deployments, AI agents,
  automated backups, and global replication.
icon: cloud-sun
---

# MariaDB Cloud

{% hint style="info" %}
📄 Read offline: [mariadb-mariadb-cloud.pdf](https://github.com/mariadb-corporation/mariadb-docs/releases/latest/download/mariadb-mariadb-cloud.pdf) (~300 pages, 5.5 MB). The PDF is a point-in-time snapshot; this site is always current.
{% endhint %}

## Overview

MariaDB Cloud (previously called SkySQL) is an AI-driven, fully managed Database-as-a-Service (DBaaS), designed to deploy MariaDB and MySQL-compatible workloads across diverse environments including multiple data centers, regions, and cloud providers. It now offers both traditional provisioned and serverless deployment options, catering to a wide range of use cases and workload patterns while preventing over-provisioning. With the addition of the no-code AI Agent builder, developers can easily provide natural language interfaces to their end users to ask questions of the data without SQL expertise.

Originally developed by [MariaDB](http://mariadb.com), MariaDB Cloud is aimed to be the most comprehensive cloud platform for MariaDB. Its robust feature set is the result of years of insights gathered from hundreds of customers running mission-critical workloads.

MariaDB Cloud provides MariaDB and MySQL-compatible workloads with enterprise-grade and production-ready features:

* [Serverless deployment for instant autoscaling](readme/serverless.md#intelligent-scaling)
* [Integrated AI agents for database interaction](cloud-ai/copilot-guide.md)
* [Automated complex database configurations](cloud-management/config/)
* [Cloud-native capabilities with auto-scaling](cloud-management/autonomously-scale-compute-storage.md)
* [Global replication](high-availability-dr/setup-global-replication.md)
* [Automated backups](cloud-data-handling/backup-and-restore/mariadb-backup.md)
* [Advanced security with end-to-end encryption and private connectivity](security/)
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
graph TD
    accTitle: MariaDB Cloud architecture overview
    accDescr {
        Four groups are drawn, holding ten boxes in total. User Interfaces holds
        two boxes: MariaDB Cloud Portal UI and MariaDB Cloud Monitoring UI.
        Developer API holds three boxes: MariaDB SQL, NoSQL and REST API. MariaDB
        Cloud holds three boxes: MaxScale SQL Proxy, MariaDB Primary + replicas,
        and Replicas in other zones, regions. External Services holds two boxes:
        Alerts / Autoscale / Monitor and Cloud backups. The User Interfaces group
        and the Developer API group are each joined to the MariaDB Cloud group by
        a line with arrows in both directions. Inside MariaDB Cloud, the MaxScale
        SQL Proxy is joined to the MariaDB Primary + replicas box and to the
        Replicas in other zones, regions box, each by a line with arrows in both
        directions. Arrows lead one way from the MariaDB Cloud group to Alerts /
        Autoscale / Monitor and to Cloud backups.
    }
    subgraph UI [User Interfaces]
        Portal[MariaDB Cloud Portal UI]
        MonitorUI[MariaDB Cloud Monitoring UI]
    end

    subgraph API [Developer API]
        SQL[MariaDB SQL]
        NoSQL[NoSQL]
        REST[REST API]
    end

    subgraph Cloud [MariaDB Cloud]
        MaxScale{MaxScale SQL Proxy}
        Primary[MariaDB Primary + replicas]
        Replicas[Replicas in other zones, regions]
    end

    subgraph External [External Services]
        Alerts[Alerts / Autoscale / Monitor]
        Backups[Cloud backups]
    end

    %% Entry points at the top
    UI <--> Cloud
    API <--> Cloud
    
    %% Internal Cloud Logic
    MaxScale <--> Primary
    MaxScale <--> Replicas
    
    %% Force External Services to the bottom
    Cloud ~~~ External
    Cloud --> Alerts
    Cloud --> Backups
```

## See Also

* [MariaDB Cloud Datasheet](https://mariadb.com/resources/datasheets/mariadb-cloud/)

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
