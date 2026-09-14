---
description: >-
  MariaDB Cloud service tiers — Foundation, Power, and PowerPlus: what each
  tier includes, tier comparison tables, uptime SLAs, and how to upgrade.
icon: layer-group
---

# Service Tiers

MariaDB Cloud is offered in three service tiers — **Foundation**, **Power**, and **PowerPlus**. The tier is a property of your organization's subscription, not of an individual database. It determines which database engine you get, how large a service can grow, which topologies and connectivity options you can launch, how long backups are retained, and which uptime SLA and support entitlements apply to you.

Every MariaDB Cloud organization is on the **Foundation** tier unless Power or PowerPlus has been specifically purchased. Foundation requires no commitment and includes a perpetually free serverless database.

## Which Tier Is Right for You

| Tier           | Best for                                                                                    | In short                                                                                                  |
| -------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Foundation** | Development, test, proofs of concept, and small to medium production workloads              | Fully managed MariaDB Community Server with sensible defaults, automated backups, and a free serverless database |
| **Power**      | Mission-critical production workloads with strict uptime, performance, and support requirements | MariaDB Enterprise Server, an elevated uptime SLA, large instances, point-in-time restore, and private connectivity |
| **PowerPlus**  | Regulated or globally distributed workloads that cannot tolerate replica lag or any data loss | Everything in Power, plus synchronous Enterprise Cluster topologies and the longest backup retention        |

Foundation is the starting point, and moving up a tier is additive: Power includes the Foundation capabilities, and PowerPlus includes the Power capabilities.

## Tier Comparison

### Service Features

| Feature            | Foundation                                | Power                                     | PowerPlus                                                  |
| ------------------ | ----------------------------------------- | ----------------------------------------- | ----------------------------------------------------------- |
| Database           | MariaDB Community Server                  | MariaDB Enterprise Server                 | MariaDB Enterprise Server                                   |
| AI                 | Developer and DBA Copilots, AI Agents     | Developer and DBA Copilots, AI Agents     | Developer and DBA Copilots, AI Agents                       |
| Topologies         | Single Node, Primary-Replica              | Single Node, Primary-Replica              | Single Node, Primary-Replica, Enterprise Cluster (Galera)   |
| HTAP (MariaDB Exa) | Not available                             | Available (technical preview)             | Available (technical preview)                               |
| Uptime SLA         | 99.95% (multi-node)                       | 99.995% (multi-node)                      | 99.995% (multi-node)                                        |
| Support            | Basic and Standard support                | Basic, Standard, and Remote DBA (RDBA) support | Basic, Standard, and Remote DBA (RDBA) support         |

### Cloud Resources

| Feature                 | Foundation                                                       | Power                                                                | PowerPlus                                                            |
| ----------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Cloud availability      | AWS, Google Cloud, Azure — 40+ regions                           | AWS, Google Cloud, Azure — 40+ regions                                | AWS, Google Cloud, Azure — 40+ regions                                |
| Compute (provisioned)   | Up to 16 vCPU, 128 GB RAM                                        | Up to 128 vCPU, 1024 GB RAM                                           | Up to 128 vCPU, 1024 GB RAM                                           |
| Custom instance sizes   | No                                                               | Yes, on request                                                       | Yes, on request                                                       |
| Compute scaling         | On demand (provisioned); autoscaling up to 8 MCU (serverless)    | On demand and autoscaling (provisioned); autoscaling up to 12 MCU (serverless) | On demand and autoscaling (provisioned); autoscaling up to 12 MCU (serverless) |
| Storage                 | Up to 1000 GB                                                    | Up to 9000 GB                                                         | Up to 9000 GB                                                         |
| Storage scaling         | On demand (provisioned); autoscaling (serverless)                | On demand and autoscaling                                             | On demand and autoscaling                                             |
| Read replicas           | Up to 1                                                          | Up to 4                                                               | Up to 4                                                               |
| Redundant MaxScale      | No                                                               | Yes                                                                   | Yes                                                                   |
| Bring Your Own Account  | No                                                               | Yes                                                                   | Yes                                                                   |

{% hint style="info" %}
One MCU (MariaDB Cloud Compute Unit) is equivalent to 0.5 vCPU and 2 GB of memory. Serverless services size themselves automatically, so you do not select an instance size when launching one.
{% endhint %}

### Backup and Recovery

| Feature            | Foundation                                              | Power                                                   | PowerPlus                                               |
| ------------------ | ------------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------- |
| Backup types       | Nightly; self-service snapshot, full, incremental, logical | Nightly; self-service snapshot, full, incremental, logical | Nightly; self-service snapshot, full, incremental, logical |
| Backup storage     | MariaDB Cloud managed                                   | Managed or your own bucket                              | Managed or your own bucket                              |
| Snapshot retention | 7 days default, up to 15 days                           | 7 days default, up to 30 days                           | 7 days default, up to 45 days                           |
| Recovery           | Backup restore                                          | Backup restore, point-in-time restore                   | Backup restore, point-in-time restore                   |

### Security and Connectivity

| Feature             | Foundation                        | Power                                                                          | PowerPlus                                                                      |
| ------------------- | --------------------------------- | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| Portal RBAC         | Yes                               | Yes                                                                            | Yes                                                                            |
| Encryption          | In transit and at rest, including backups | In transit and at rest, including backups                              | In transit and at rest, including backups                                      |
| Secure connectivity | IP allowlist                      | IP allowlist; AWS PrivateLink, GCP Private Service Connect, Azure Private Link | IP allowlist; AWS PrivateLink, GCP Private Service Connect, Azure Private Link |

## About the Features

* **Free serverless database** — every account gets one free [serverless database](serverless.md) with a 0.5 vCPU / 2 GB baseline that autoscales up to 2 MCU. No credit card is required. The free database is capped at 10 MCU-hours per month; once that threshold is reached it stays inactive until the limit resets at the start of the next month.
* **AI** — built-in Developer and DBA Copilot agents, the no-code [AI Agent builder](../cloud-ai/copilot-guide.md), and support for the [MariaDB Cloud MCP Server](../cloud-ai/mcp-server.md), on every tier.
* **Redundant MaxScale** — with [MaxScale Redundancy](../reference/maxscale-redundancy.md), MaxScale nodes are deployed active-active behind round-robin load balancing, with a selectable MaxScale instance size.
* **Point-in-time restore (PITR)** — [restores a service to a moment in time](../cloud-data-handling/backup-and-restore/restore-examples/point-in-time-restore.md); it requires additional binary log retention to be configured in advance.
* **Private connectivity** — [AWS PrivateLink, Google Cloud Private Service Connect, and Azure Private Link](../security/private-vpc-connections.md), in addition to IP allowlisting.
* **[Bring Your Own Account (BYOA)](../quickstart/bring-your-own-account-byoa.md)** — database nodes run in your own cloud account, and infrastructure costs are billed directly by your cloud provider. On PowerPlus, BYOA extends to advanced topologies, including running Enterprise Cluster inside your own cloud account.
* **[MariaDB Enterprise Cluster](../quickstart/enterprise-cluster.md)** (PowerPlus) — synchronous, Galera-powered clustering with write-set certification, quorum management, and automated failover with no data loss (RPO 0). Enterprise Cluster requires a minimum of 3 nodes to maintain quorum. During the technical preview, MaxScale routes all writes to a single active writer node.
* **[HTAP using MariaDB Exa](../quickstart/htap-mariadb-exa.md)** — adds an in-memory columnar analytics engine behind the same entry point as your OLTP database.
* **[Support](../reference/support.md)** — Basic support is included with every subscription; Standard support adds Problem Resolution Support, Engineering Support, and 24×7 handling of the most severe issues. The [Remote DBA (RDBA) add-on](../reference/clouddba.md) is available on Power and PowerPlus.

{% hint style="warning" %}
**Technical preview features**

MariaDB Enterprise Cluster, HTAP using MariaDB Exa, and BYOA are currently available as technical previews. Preview features receive limited Problem Resolution Support on a best-effort basis and are excluded from the standard support SLAs; HTAP using MariaDB Exa is not intended for production use. BYOA is currently available on AWS and Microsoft Azure, with Google Cloud support to follow.
{% endhint %}

## Uptime SLA and Service Credits

Assess the availability requirements of your application and choose the tier that meets them. Multi-node configurations on Foundation target 99.95% availability per billing month — a maximum of 21 minutes and 54 seconds of downtime in a 30-day month. Multi-node configurations on Power and PowerPlus target 99.995%, a maximum of 2 minutes and 11 seconds in the same period. The uptime SLA applies to multi-node configurations in general availability; single-node services and technical-preview topologies are excluded.

Service credits are calculated as a percentage of the fees paid for the affected service in the month the downtime occurred:

| Tier             | Monthly uptime percentage                             | Credit |
| ---------------- | ----------------------------------------------------- | ------ |
| Foundation       | Less than 99.95% but greater than or equal to 99.0%   | 10%    |
| Foundation       | Less than 99.0%                                       | 25%    |
| Power, PowerPlus | Less than 99.995% but greater than or equal to 99.0%  | 10%    |
| Power, PowerPlus | Less than 99.0%                                       | 25%    |

Credits must be requested within 60 days of the end of the affected billing period, and a support ticket must be logged within 60 minutes of first becoming aware of the event. See the [MariaDB Cloud Uptime SLA](../reference/uptime-sla.md) page for measurement details, exclusions, and customer obligations.

## Selecting a Tier

The tier applies to your whole organization, so services you launch inherit it. When you launch a service through the [MariaDB Cloud Portal](https://app.skysql.com), the options presented to you on the [Launch Page](../cloud-usage/launch-page.md) — instance sizes, node counts, topologies, MaxScale redundancy, connectivity — reflect your organization's tier.

When you launch through the REST API, the tier is passed in the request body:

```bash
curl --location 'https://api.skysql.com/provisioning/v1/services' \
  --header 'Content-Type: application/json' \
  --header "X-API-Key: ${API_KEY}" \
  --data '{
    "tier": "power",
    "service_type": "transactional",
    "topology": "es-replica",
    "provider": "aws",
    "region": "us-east-2",
    "name": "example-service",
    "nodes": 3,
    "size": "sky-4x32",
    "architecture": "amd64",
    "storage": 100,
    "version": "11.4.10-7.1-standard",
    "ssl_enabled": true
  }'
```

The [`/provisioning/v1/sizes` API endpoint](https://apidocs.skysql.com/#/Offering/get_provisioning_v1_sizes) also returns tier-specific results, so the [instance sizes](../reference/mariadb-cloud-instance-sizes.md) it lists depend on whether your account is Foundation, Power, or PowerPlus.

## Upgrading Your Tier

Moving to Power or PowerPlus is a commercial change to your subscription. Submit a request from the MariaDB Cloud Portal or contact your account representative. Discounts are typically available for one-year and three-year commitments, and MariaDB Cloud can be procured through the AWS, Google Cloud, and Azure marketplaces, including as a private offer.

BYOA has additional prerequisites beyond the tier: Power or PowerPlus, Standard Support with the Remote DBA add-on enabled, and an annual contract or minimum spend commitment.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
