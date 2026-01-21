---
icon: clouds
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
---

# MariaDB Cloud Serverless

{% hint style="info" %}
"Serverless" refers to a database model where the cloud provider fully manages the underlying database infrastructure, automatically scaling resources and applying a pay-for-what-you-use pricing model. The term "serverless" is a misnomer, as servers are still used, but the user is abstracted away from all server management tasks.
{% endhint %}

## MariaDB Cloud Serverless

MariaDB Cloud Serverless is the first true serverless database solution for the MySQL and MariaDB ecosystem, uniquely built to meet the dynamic demands of modern applications. MariaDB Cloud Serverless combines instant scalability with cost efficiency, scaling down to zero when idle—saving you from paying for unused capacity. When workloads resume, Serverless service is ready in milliseconds, ensuring a seamless, uninterrupted experience for applications and users.

### True Serverless Experience

* **Instant Launch**: Databases ready in milliseconds using pre-fabricated micro databases
* **Scale to Zero**: Complete resource deallocation during idle periods
* **Immediate Cold Start**: No delays during initialization

### Cloud-Native Architecture

* **No Forking**: Built on proven open-source MariaDB/MySQL without modifications
* **Kubernetes-Native**: Leverages custom controllers for fine-grained resource control
* **Multi-Cloud**: Deploy across AWS, Azure, and Google Cloud Platform

### Intelligent Scaling

* **Vertical Auto-Scaling**: CPU and memory adjustments in real-time
* **Horizontal Scaling**: Transparent live migrations for unlimited growth
* **Storage Auto-Scaling**: Dynamic storage expansion based on usage patterns

## Free Developer Tier

Every MariaDB Cloud account includes a perpetually free serverless database perfect for:

* Development and testing environments
* Learning and experimentation
* Proof-of-concept projects
* Small applications with intermittent usage

**Specifications:**

* 0.5 vCPU baseline
* 2GB memory baseline
* Auto-scaling up to 2 SCUs (MariaDB Cloud Compute Units)
* No time limits or restrictions

## Architecture Highlights

### Compute-Storage Approach

MariaDB Cloud takes a different approach from services like AWS Aurora:

* **Preserves Open Source**: No modifications to the mature InnoDB storage engine
* **Native Kubernetes**: Uses standard Kubernetes volume management
* **No Hidden Costs**: Transparent pricing without surprise IOPS charges

### Intelligent Proxy System

* **Always-On Connections**: Applications stay connected even when database scales to zero
* **Session State Management**: Preserves variables, prepared statements, and transaction state
* **Transparent Failover**: Automatic recovery from failures without application impact

### Buffer Pool Management

* **Performance Consistency**: Maintains cache hit ratios during scaling operations
* **Automatic Hydration**: Reloads frequently accessed data after scaling events
* **SSD Offloading**: Temporarily stores hot pages during scale-down operations

## Supported Workloads

MariaDB Cloud Serverless is designed to handle diverse workload types:

### Transactional Workloads (OLTP)

* High-frequency, low-latency operations
* ACID compliance and data consistency
* Connection pooling and session management

### Analytical Workloads (OLAP)

* Complex queries and reporting
* Integration with MariaDB ColumnStore
* On-demand analytics processing

### Semantic Search

* Vector database capabilities
* AI/ML application support
* Natural language query processing

## Getting Started

1. [**Create Account**](https://app.skysql.com) - Sign up for your free MariaDB Cloud account
2. [**Launch Service**](../quickstart/) - Follow our quickstart guide
3. [**Connect Application**](../connecting-to-mariadb-cloud-dbs/#connecting-from-your-application) - Integrate with your applications
4. [**Monitor Performance**](../cloud-management/observability.md) - Use built-in monitoring tools
