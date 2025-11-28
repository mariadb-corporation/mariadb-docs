---
cover: broken-reference
coverY: 0
---

# MariaDB Overview

_This Quickstart Guide overviews the MariaDB Enterprise Platform's components. It details MariaDB Enterprise Server (core database), MaxScale (proxy for load balancing, security, testing), and extensions like Galera (replication) and ColumnStore (analytics). It also covers enterprise tools and cloud-native components, illustrating their integrated function for streamlined, robust database solutions._

### Quickstart Guide: MariaDB Products and Their Interoperation

The MariaDB Enterprise Platform is designed to provide a comprehensive database solution, integrating various components to deliver enterprise-grade capabilities.

#### Key Components:

* **MariaDB Enterprise Server:** This is the foundational database engine that provides core data storage and management functionality, designed with an emphasis on security, performance, and reliability for business-critical operations.
* **MariaDB MaxScale:** This advanced database proxy acts as an intermediary between client applications and MariaDB servers. It offers capabilities such as:
  * **Load Balancing:** Distributes database connections across multiple servers to optimize resource utilization and improve responsiveness.
  * **Security Features:** Provides enhanced security through features like firewalling and query filtering.
  * **Routing:** Directs database queries to appropriate servers based on predefined rules.
  * **Workload Capture and Replay (WCAR):** Facilitates the recording of production database interactions and their accurate replay in testing environments for analysis and troubleshooting.
  * **Diff Router:** Allows for behavior comparison between different server versions, aiding in testing and validation of upgrades or changes.
* **Optional Extensions:** The platform supports specialized extensions to address specific database requirements:
  * **Galera:** Enables multi-master synchronous replication, ensuring high availability and fault tolerance across multiple database nodes.
  * **ColumnStore:** A columnar storage engine optimized for analytical workloads, providing efficient processing of large datasets for business intelligence and reporting.
* **Enterprise Tools:** A collection of tools designed to simplify the management, monitoring, and maintenance of MariaDB deployments, helping to ensure operational efficiency.
* **Cloud-Native Components:** For modern deployment strategies, the platform includes:
  * **Docker Images:** Pre-packaged images for containerized deployments, enabling consistent and portable environments.
  * **Kubernetes Operator:** An automated component that acts as a database administrator within Kubernetes environments, handling tasks such as backups, security configurations, and point-in-time recovery.

#### How They Work Together:

The MariaDB Enterprise Platform integrates these components to offer a unified and cohesive database environment. This integrated approach simplifies deployment, management, and support, providing a consistent set of technologies for various use cases, from transactional processing to analytical workloads and cloud deployments. The core server provides data persistence, while MaxScale enhances scalability and security, and specialized extensions address specific performance or availability needs. The accompanying tools and cloud-native components streamline operations and facilitate modern infrastructure integration.

For further details, you can refer to the MariaDB blog post on the Enterprise Platform release:

* [Announcing New Release of MariaDB Enterprise Platform](https://mariadb.com/resources/blog/announcing-new-release-of-mariadb-enterprise-platform/)

{% @marketo/form formId="4316" %}
