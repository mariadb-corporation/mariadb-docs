---
description: >-
  Introduction to GridGain as an in-memory computing platform: what you can do
  with it, its editions, and how to migrate from Apache Ignite.
---

# What Is GridGain?

GridGain is a middleware-class product developed by the company of the same name.

As a middleware, GridGain is an in-memory computing platform that is designed to tackle speed and scale challenges. But
what does that mean? In practice, it signifies that GridGain is capable of storing and processing your data right in RAM
across a cluster of interconnected machines. GridGain APIs are developed in a way to minimize network traffic
between cluster nodes and your applications. Not only complex SQL queries with JOINs can perform at scale, but your
custom Java/.NET/C++ logic can be executed in-place on the cluster machines resulting in an unprecedented performance
boost.

As a company, GridGain developed the software that became Apache Ignite, donating the original code to the
Apache Software Foundation (ASF) in 2014. Apache Ignite, one of the fastest ASF projects to graduate to top-level status,
is now a top 5 ASF project in terms of contributions and dev-list activity and is downloaded millions of times annually.
GridGain is among the major ASF contributors who are striving to increase adoption of Apache Ignite across
open source community and companies with "the open-source first" policy. Besides the commitment to open source, GridGain powers mission-critical deployments of large enterprises that benefit from extra features available in GridGain
platform only as well as from production support, professional and managed services.

## What Can You Do with GridGain?

We've seen many usage scenarios of GridGain with various
[deployment modes](../gridgain8-management/installation/deployment-modes.md#cluster-deployment-modes) and
architectures. However, the most typical two are GridGain as an in-memory data grid (IMDG) and GridGain as a
system of records. As an IMDG, GridGain solves speed and scale problems of existing solutions that are usually powered
by relational or NoSQL databases. A GridGain in-memory cluster is deployed between the existing application and
database. Once the data from the underlying database loads into the IMDG, the IMDG processes all the reads and writes,
ensuring transactional consistency for RDBMS-backed architectures. As a system of records, GridGain is used by
green-field and modern applications that are looking for both speed and scale with guarantees of durability and
data consistency for disk-based databases.

It's important to note that even though GridGain belongs to the class of in-memory products, it can store anywhere
from 0 to 100% of the data in memory and keep the total data set in a broad range of non-volatile memory: from disk or
SSD to the latest persistent memory such as Intel Optane. This allows companies to combine in-memory speed with the
lower cost and durability of non-volatile storage.

So how do companies, large and small, use GridGain? Our customers use GridGain to add speed and scale to a broad range
of real-time applications, including:

- Existing custom real-time or batch-based applications
- New core banking systems including credit cards authorization and payment systems
- Web-scale and mobile applications and APIs
- Equity and other securities trading and analytics
- High performance computing (HPC)
- Fraud detection and regulatory compliance
- eCommerce and healthcare benefits management
- Voice over IP (VoIP) routing and management
- The Internet of Things (IoT)
- Streaming analytics
- Machine learning (ML) and deep learning (DL)

## GridGain Editions

GridGain is available in two editions: Enterprise and Ultimate. Both come with a 30-day trial license.

GridGain Enterprise Edition includes enterprise features such as enterprise-grade security, data center replication, and connectors for enterprise storage and streaming technologies.

GridGain Ultimate Edition adds everything in the Enterprise Edition plus cluster-wide snapshots, backups, and recovery management tools. Choose this edition when you deploy GridGain as a system of records that keeps all the data in persistent storage.

Production support and professional services are available for all GridGain editions, as well as for Apache Ignite deployments.

## Migrating From Apache Ignite

For the most part, you can migrate from Apache Ignite to GridGain without major issues.

To migrate, stop your server and replace Apache Ignite binaries with GridGain binaries. Data will be preserved when you restart servers, but you may need to account for differences in some features. Here are some possible issues:

### Snapshots

GridGain snapshots were developed separately from Apache Ignite. The implementations are not compatible. If you used Apache Ignite snapshots in your project, you will need to implement [GridGain snapshots](../gridgain8-management/snapshots/full-incremental-snapshots.md) instead.

### Ignite CDC

Ignite CDC (Change Data Capture) is an experimental feature in Apache Ignite, and as such it does not have exact counterpart in GridGain. Instead, GridGain Enterprise and Ultimate editions offer [Data Center Replication](../gridgain8-management/data-center-replication/introduction.md) to replicate cache data.

If you used Apache Ignite CDC, you will need to implement Data Center Replication or use an alternative solution.

### Calcite SQL Support

Calcite SQL engine is not supported in GridGain and there are currently no plans to implement it in GridGain 8.x versions. GridGain 9 release is planned to include full support for Calcite SQL.

### Cellular Affinity

Cellular affinity is an experimental mode in Apache Ignite. As such, it is not implemented in GridGain.

### Service Intercepors

Service interceptors ("middleware") are an experimental feature in Apache Ignite. It is currently not available in GridGain.

### Custom Execution Context

It is currently not possible to set up a custom execution context in GridGain.

### Service Call Context

In GridGain, you cannot retrieve arrays of custom objects.

### Read-Repair

Read-Repair  is an experimental API in Apache Ignite. Due to losses in performance it was not transferred to GridGain.

## Additional Information

From here, you may want to:

- Learn about key [concepts](concepts.md) in GridGain.

- Learn how to [install](../gridgain8-management/installation/README.md) GridGain.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
