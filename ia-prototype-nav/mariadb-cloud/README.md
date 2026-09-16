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

**Launch and connect.** The portal is the fastest start, walking through creating a database, sizing it, and collecting connection details. The API provisions a database programmatically, which is the path to creating databases from a deployment pipeline. Then point your application at the connection details and run a query.

**Configure it for production.** The guides cover a replicated topology for surviving node loss, the network and access controls that decide who can reach the database, and the backup settings. Enabling replication early costs little while the application is still easy to change.

**Bring your data in.** There are loading paths for an existing database, including a dedicated one for moving an Amazon RDS for MariaDB instance.

Create a database in the portal and connect to it. That confirms your credentials and network path before any application code changes.

## Get Started

{% content-ref url="get-started/install-mariadb-cloud.md" %}
[install-mariadb-cloud.md](get-started/install-mariadb-cloud.md)
{% endcontent-ref %}

{% content-ref url="get-started/connect-to-mariadb-cloud.md" %}
[connect-to-mariadb-cloud.md](get-started/connect-to-mariadb-cloud.md)
{% endcontent-ref %}

## Tutorials

{% content-ref url="tutorials/mariadb-cloud-tutorial.md" %}
[mariadb-cloud-tutorial.md](tutorials/mariadb-cloud-tutorial.md)
{% endcontent-ref %}

## How-To Guides

{% content-ref url="how-to-guides/configure-mariadb-cloud.md" %}
[configure-mariadb-cloud.md](how-to-guides/configure-mariadb-cloud.md)
{% endcontent-ref %}

{% content-ref url="how-to-guides/secure-mariadb-cloud.md" %}
[secure-mariadb-cloud.md](how-to-guides/secure-mariadb-cloud.md)
{% endcontent-ref %}

## Concepts

{% content-ref url="overview/what-is-mariadb-cloud.md" %}
[what-is-mariadb-cloud.md](overview/what-is-mariadb-cloud.md)
{% endcontent-ref %}

{% content-ref url="concepts/how-mariadb-cloud-works.md" %}
[how-mariadb-cloud-works.md](concepts/how-mariadb-cloud-works.md)
{% endcontent-ref %}

## Reference

{% content-ref url="reference/mariadb-cloud-reference.md" %}
[mariadb-cloud-reference.md](reference/mariadb-cloud-reference.md)
{% endcontent-ref %}

{% content-ref url="release-notes/mariadb-cloud-releases.md" %}
[mariadb-cloud-releases.md](release-notes/mariadb-cloud-releases.md)
{% endcontent-ref %}
