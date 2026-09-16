---
title: MariaDB Cloud
description: >-
  MariaDB Cloud is the fully managed database service for MariaDB and
  MySQL compatible workloads, in provisioned and serverless forms.
icon: cloud
---

# MariaDB Cloud

MariaDB Cloud is a fully managed database service for MariaDB and MySQL compatible workloads. You provision a database and the service operates the hardware, the patching, the backups, and the availability. It was previously called SkySQL, and you will still find that name in older material.

There are two deployment shapes. A provisioned database has capacity you choose and pay for, which suits a steady workload. A serverless database scales with demand, which suits variable or intermittent traffic and avoids paying for idle capacity. Both run across major cloud providers and regions, so you can place the database near your application.

Compatibility is the same as the self managed products, so existing code, drivers, and tools work unchanged. What changes is the operational boundary: patching, automated backups, and failover are service settings rather than procedures you run.

The service also includes an AI agent builder. It puts a natural language interface over a database, so someone can ask a question of the data without writing the SQL for it.

**Launch and connect.** The portal is the fastest start, walking through creating a database, sizing it, and collecting connection details. The API provisions a database programmatically, which is the path to creating databases from a deployment pipeline. Then point your application at the connection details and run a query.

**Configure it for production.** The guides cover a replicated topology for surviving node loss, the network and access controls that decide who can reach the database, and the backup settings. Enabling replication early costs little while the application is still easy to change.

**Bring your data in.** There are loading paths for an existing database, including a dedicated one for moving an Amazon RDS for MariaDB instance.

Create a database in the portal and connect to it. That confirms your credentials and network path before any application code changes.

{% content-ref url="{mariadb-cloud}/readme/key-features-and-capabilities" %}
[Key Features & Capabilities]({mariadb-cloud}/readme/key-features-and-capabilities)
{% endcontent-ref %}

{% content-ref url="{mariadb-cloud}/readme/serverless" %}
[MariaDB Cloud Serverless]({mariadb-cloud}/readme/serverless)
{% endcontent-ref %}

{% content-ref url="{mariadb-cloud}/readme/architecture" %}
[MariaDB Cloud Serverless Architecture]({mariadb-cloud}/readme/architecture)
{% endcontent-ref %}

{% content-ref url="{mariadb-cloud}/quickstart" %}
[Quickstart Guides]({mariadb-cloud}/quickstart)
{% endcontent-ref %}

{% content-ref url="{mariadb-cloud}/connecting-to-mariadb-cloud-dbs" %}
[Connection Methods]({mariadb-cloud}/connecting-to-mariadb-cloud-dbs)
{% endcontent-ref %}

{% content-ref url="{mariadb-cloud}/cloud-management" %}
[Management & Configuration]({mariadb-cloud}/cloud-management)
{% endcontent-ref %}

{% content-ref url="{mariadb-cloud}/cloud-usage" %}
[Cloud Portal]({mariadb-cloud}/cloud-usage)
{% endcontent-ref %}

{% content-ref url="{mariadb-cloud}/cloud-data-handling" %}
[Data Loading & Backup]({mariadb-cloud}/cloud-data-handling)
{% endcontent-ref %}

{% content-ref url="{mariadb-cloud}/cloud-ai" %}
[AI Agents & Copilot]({mariadb-cloud}/cloud-ai)
{% endcontent-ref %}

{% content-ref url="{mariadb-cloud}/high-availability-dr" %}
[HA & DR]({mariadb-cloud}/high-availability-dr)
{% endcontent-ref %}

{% content-ref url="{mariadb-cloud}/security" %}
[Security]({mariadb-cloud}/security)
{% endcontent-ref %}

{% content-ref url="{mariadb-cloud}/reference" %}
[Reference]({mariadb-cloud}/reference)
{% endcontent-ref %}
