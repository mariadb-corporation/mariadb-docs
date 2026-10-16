---
description: >-
  Hands-on tutorials that teach GridGain 9 by building and operating working examples, organized into learning paths.
---

# Tutorials

Tutorials teach by doing: each one builds or operates something end to end on a local cluster. Use the reference sections of this documentation for complete configuration details, and use these tutorials to learn how the pieces fit together.

New to GridGain 9? Run the [Quick Start](../gridgain9-get-started/quick-start.md) first, then follow a learning path below. The tutorials use a shared Music Store dataset that you load in the first tutorial.

## Learning Paths

| Path | Level | Start here when |
| ---- | ----- | --------------- |
| [Distributed SQL Foundations](distributed-sql-foundations/README.md) | Beginner | You are new to GridGain 9 and want to go from a running cluster to SQL, the Java thin client, and transactions. |
| [Schema Design for Distributed SQL](schema-design-for-distributed-sql/README.md) | Intermediate | You are designing tables and want colocation, distribution zones, and data access to work together. |
| [Data Pipeline APIs](data-pipeline-apis/README.md) | Intermediate | You need to load large volumes of data at high throughput. |

Complete Distributed SQL Foundations before the other paths, because they build on the cluster and dataset it sets up.

## How-To Guides

Task-focused guides live next to the reference pages they extend:

* **Development:** [Configuring Logging for the Java Thin Client](../gridgain9-development/configuring-java-client-logging.md)
* **Management:** [Starting a Cluster With Docker Compose](../gridgain9-management/installation/start-cluster-docker-compose.md), [Working With the CLI Step by Step](../gridgain9-management/cli-tool-step-by-step.md), [Managing the Cluster Lifecycle With the REST API](../gridgain9-management/manage-cluster-lifecycle-rest-api.md), [Monitoring With Prometheus and Grafana](../gridgain9-management/monitoring/prometheus-grafana-step-by-step.md)
