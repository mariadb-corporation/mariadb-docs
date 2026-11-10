---
description: >-
  MariaDB Cloud key features: advanced scalability, intelligent load
  balancing, flexible consistency models, integrated AI agents, automated
  configuration, and custom query routing.
icon: clouds
---

# Key Features & Capabilities

## Key Features of MariaDB Cloud

### Advanced Scalability

* **Serverless Scaling:** Provides near instantaneous scaling from zero to defined upper limit and back down to zero, adapting dynamically to workloads without manual intervention.
* **Intelligent Load Balancing:** Maintains consistency via smart proxy-based load balancing and read-write splitting.
* **Flexible Consistency:** Offers both causal and strong global consistency models.
* **Custom Query Routing:** Allows fine-tuned performance optimization through customizable routing rules.

### AI Services

* **AI Retrieval (Public Preview):** Ask questions about your documents or your MariaDB databases in natural language, and call the knowledge base from your applications through a REST API. A document knowledge base returns passages or generated answers from your files, and a database knowledge base turns a question into SQL and returns the rows. See [AI Retrieval](cloud-ai/ai-retrieval/).
* **Built-in AI Agents:** The Developer Agent, the Data Agent, and the DBA Agent help with general MariaDB Cloud questions, querying your data, query performance tuning, and troubleshooting guidance.
* **MariaDB Cloud MCP Server:** Connects AI-enabled development tools to your MariaDB Cloud databases. See [MariaDB Cloud MCP Server](cloud-ai/mcp-server.md).

### Global Multi-Cloud Presence

* Available in 40+ regions across AWS, GCP, and Azure, offering unparalleled flexibility and reach.

### Robust High Availability (HA)

* **Resilient Infrastructure:** Multi-layered protection across disks, compute, zones/regions, network, and load balancing.
* **Intelligent Proxy through MaxScale:** Ensures seamless failover and monitors replication lag, maintaining service continuity.
* **Rapid Failover:** Employs real-time health checks for swift, automated recovery.
* **Synchronous Replication:** Provision multi-node MariaDB Enterprise cluster for workloads demanding absolute data consistency, multi-primary capabilities, and zero data loss. _(Available exclusively on the PowerPlus tier)._

{% hint style="info" %}
**Single-Writer Routing**&#x20;

For [MariaDB Enterprise Cluster](quickstart/enterprise-cluster.md), MaxScale is configured to route all write traffic to a single active writer node to ensure maximum stability.
{% endhint %}

### Disaster Recovery

* **Multi-Region Replication:** Spans across regions and cloud providers for maximum resilience.
* **Flexible External Replication:** Supports custom external replica setups for enhanced redundancy and disaster recovery.

### State-of-the-Art Data Protection

* **Comprehensive Backup Solutions:** Goes beyond nightly backups with incremental, snapshot, and binlog backup options to both MariaDB Cloud and customer-managed storage.
* **Near-Zero RPO:** Achieves minimal data loss with continuous binlog streaming.

### Dynamic Auto-scaling

* **Predictive Scaling:** Anticipates and adjusts storage needs based on usage patterns.
* **Cost-Efficient Scaling:** Proactively scales resources up and down to match demand and optimize costs.

### Cloud DBA Service

* **Cloud DBA Service:** Provides access to skilled DBAs for proactive database optimization.
* **Continuous Performance Monitoring:** Ensures peak efficiency through ongoing monitoring and rapid issue resolution.

### Versatile Interoperability

* **Multi-Protocol Support:** Supports both JSON and SQL operations from a single data source.
* **Native MongoDB/MariaDB/MySQL Support:** Seamlessly integrates with existing applications via native MongoDB and MariaDB/MySQL protocol support.

For more detailed information, you can refer to this [blog post](https://skysql.com/2024/03/12/optimizing-database-resilience-and-cost-a-deep-dive-into-skysqls-unique-features/).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
