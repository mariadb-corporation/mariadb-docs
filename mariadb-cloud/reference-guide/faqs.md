---
icon: comment-question
---

# FAQs

## Overview

### What is MariaDB Cloud?

MariaDB Cloud is a modern database as a service (DBaaS) solution for production MySQL and MariaDB workloads. It simplifies database management with automated configuration, autonomous scaling, global replication, enterprise-grade security, real-time observability, automated backups and more. MariaDB Cloud delivers ultimate flexibility, reliability, performance and effortless management for your databases allowing you to focus on your application features. MariaDB Cloud provides both provisioned servers and serverless deployment options to handle a variety of use cases from mission-critical, always-on production to experimental, spiky workloads.

### Where is MariaDB Cloud available? What instance and storage options are available?

MariaDB Cloud is available across 40+ global regions on Amazon AWS, Google Cloud and Microsoft Azure. Database services on MariaDB Cloud support a range of instance sizes. Storage starts at 10GB and can scale up to 9000GB. MariaDB Cloud's autonomous scaling takes the guesswork out of provisioning. You can start small and scale automatically as your needs evolve.

### How do I get started?

You can sign up for a free account at [https://app.skysql.com](https://app.skysql.com/). There is no credit card required to start and you get $100 in free credit. Once registered, you can get started right away by [launching a service](broken-reference), [connecting](../connecting-to-mariadb-cloud-dbs/), and [loading data](../cloud-data-handling/migration-data-loading/data-loading/).

### How quickly can I launch a new database?

Launching a new database service with MariaDB Cloud is quick and easy. Serverless database services start in miliseconds. Provisioned Database services start in 2-4 min.

### Is MariaDB Cloud ready for production use?

Yes. MariaDB Cloud delivers enterprise-grade cloud database service for your mission-critical applications. Multi-node databases feature a comprehensive [SLA](uptime-sla.md), High Availability (HA) features, and operations features. [Enterprise support](https://mariadb.com/services/technical-support-services/) options extend support to 24x7, with the additional option of Cloud[DBA](fractionaldba.md) for proactive assistance from a team of expert DBAs.

### What is the history of MariaDB Cloud?

MariaDB Cloud is a database-as-a-service (DBaaS) that was originally developed and managed by MariaDB Corporation. The cloud division was later spun out of MariaDB into a independent company - SkySQL. After a while as an independent company, SkySQL was again merged back to MariaDB as MariaDB Cloud.

## MariaDB Cloud Features

### What services are available on MariaDB Cloud?

MariaDB Cloud is primarily designed for online applications and offers two topologies -

* Replicated: Useful for mission-critical, production workloads requiring read scaling. Replicated services feature 1 primary and up to 4 replicas and uses MariaDB MaxScale for load balancing and automatic zero-interruption failover.
* Single Node: Useful for low-cost development and test transactional workloads. Single Node services cannot be scaled to Replicated topologies.

### What options are available for scaling and right-sizing MariaDB Cloud?

You can choose [topologies](../high-availability-dr/ha-and-replicated-topology.md) to match your workload requirements, cloud regions to match your latency and operating requirements, instance sizes, and [support plan](service-tiers/).

Our platform features:

* Availability in a range of database instance sizes and storage sizes
* Availability from multiple AWS (Amazon Web Services), GCP (Google Cloud Platform), and Azure (Cloud Computing Services) [regions](region-choices.md).
* Load Balancing features included with Replicated Transactions topologies allow for read-scaling through read-write splitting.
* Custom instance sizes (for [Power Tier](service-tiers/) customers)
* Range of [support options](mariadb-server-versions.md)

### What reliability features are available on MariaDB Cloud?

* MariaDB Cloud is operated by a global team of Site Reliability Engineers (SRE), and expert DBAs. Platform problems are escalated to our team 24x7.
* [Service Level Agreement](uptime-sla.md), including an elevated SLA for Power Tier customers
* Kubernetes self-healing - Databases run in containers in kubernetes clusters and auto-heal.
* Load balancing for multi-node configurations using MariaDB MaxScale
* High Availability (HA) for multi-node configurations
* MaxScale Redundancy option
* Inbound and outbound replication - you can replicate to your self managed MariaDB anywhere.

### What operations features are available on MariaDB Cloud?

* Support from MariaDB Cloud Inc, including Enterprise and Platinum tiers optionally with CloudDBA for reactive and proactive assistance
* Vendor managed infrastructure and platform
* MariaDB Cloud Portal and [MariaDB Cloud DBaaS API](https://apidocs.skysql.com/) for instance management
* Compatibility with most programming languages and clients that work with MariaDB or MySQL, for off-the-shelf integration to your stack
* Scheduled upgrades to database software
* Automated nightly backups
* Configuration management
* On-demand backups and Snapshots
* Monitoring
* Ability to deploy additional services to support application migrations and testing on the same configuration used in production
* On-demand tear-down of unneeded services

### What governance, risk, compliance, and information security features are available on MariaDB Cloud?

* Firewall protection, including dedicated IP allowlists to access databases and to access monitoring features
* Data-at-rest encryption
* Data-in-transit encryption by default
* VPC peering, AWS PrivateLink, GCP Private Service Connect and Azure Private Link options
* Standard or enterprise authentication for management portal
* Business Associate Addendum (BAA) for HIPAA
* Data Processing Addendum (DPA) for GDPR

## Pricing

### How much does MariaDB Cloud cost?

You can get started on MariaDB Cloud at no cost for experimenting and early development using the forever-free serverless option. Provisioned database services on MariaDB Cloud are billed based on the topology, cloud region, instance and storage sizes. For example, you can run a single 2 vCPU, 4 GB RAM instance with 100GB storage on AWS us-east-1 region 24/7 for for little over $100 a month.

When you [launch a database service](../cloud-usage/launch-page.md), MariaDB Cloud provides a handy estimate of how much your service selections will cost. Multi-node database services incur charge for running our intelligent proxy. Data Transfer charges associated with your service vary based on the usage and are not included in the estimates. We passthrough data transfer charges levied by cloud providers with no additional markup.

If you stop a service, you will continue to be charged for storage, since your data is not deleted. Instance and egress charges will stop until the instance is started again.

Your database service cost includes Standard support and nightly backups. See the [Pricing](service-tiers/pricing.md) page for additional details on pricing.

### Do I need to purchase a separate MariaDB license or subscription to use MariaDB Cloud?

No additional licenses are necessary to use MariaDB Cloud.

### What is optional in MariaDB Cloud pricing?

Add-ons are available to optimize your MariaDB Cloud experience:

* [MariaDB Cloud Power Tier](service-tiers/) is a premium service offering for MariaDB Cloud customers who have the most critical requirements for uptime, availability, performance, and support.
* While all Foundation Tier services include Standard Support, Power Tier customers are offered the [Enterprise support plan](../broken-reference/).
* An optional add-on, [CloudDBA](fractionaldba.md), further extends the premium support experience and the capabilities of your in-house DBAs with the backing from a global team of expert MariaDB DBAs, available 24/7 for the most severe (P1) issues. SkySQL's SkyDBAs manage your MariaDB Cloud databases both proactively and reactively so you can focus on your core business.

### Is discounted pricing available for a longer-term commitment?

Yes. Discounts are typically offered for one-year and three-year commitments. Please [contact us](https://mariadb.com/services/technical-support-services/) for more information.

## Billing and Payment

### How can I see my current charges?

Current month's estimated charges can be viewed on the [Billing](https://app.skysql.com/billing/usage) page. Billing history for the prior months are available on the [Billing History](https://app.skysql.com/billing/history) page.

### When will I be billed?

Customers are billed monthly and an invoice for your MariaDB Cloud usage will be sent via email. Accounts using credit card will automatically be charged.

### What forms of payment does MariaDB Cloud accept?

MariaDB Cloud accepts payment by [all major credit card and through remittance accounts](../cloud-usage/billing.md). [Contact us](https://mariadb.com/services/technical-support-services/) to have your account set up for payment by wire transfer or ACH.&#x20;

{% hint style="success" %}
MariaDB Cloud does not store any of your credit card information. We use Stripe to manage all credit card transactions. [Stripe](https://stripe.com) is a widely used payment processing platform that enables businesses to accept credit card payments securely
{% endhint %}

### Can I procure MariaDB Cloud through Cloud Marketplaces?

Yes. MariaDB Cloud is available for procurement on Amazon AWS, Google Cloud and Microsoft Azure marketplaces. You can either purchase direct or we can generate a private offer to customize a subscription.

* [Amazon AWS Listing](https://aws.amazon.com/marketplace/pp/prodview-txge2dgyj4ieg)
* [Google Cloud Listing](https://console.cloud.google.com/marketplace/details/skysql-public/skysql-gcp-mp)
* [Microsoft Azure Listing](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/skysqlinc.skysql-fully-managed-cloud-database?tab=Overview)

### Will I be charged VAT or taxes?

MariaDB Cloud will bill for VAT and/or taxes in applicable jurisdictions. Customers are responsible for paying all applicable taxes and fees.&#x20;

## Backup, Restore and Deletion

### How do I backup my data on MariaDB Cloud?

MariaDB Cloud performs full backup of your database services each night. You can also use MariaDB Cloud's [Backup Service](../cloud-data-handling/backup-and-restore/) to schedule backups and perform restores. The Backup Service supports Snapshot, Full, Incremental and Logical Dump backups. You can perform restore on the same database or another database in the same or different region using the Backup Service.

### Are automated backups sent offsite? Will my data be sent to another country?

No. All data is managed within the same region by default where your database is running for data sovereignty.

### Do backup operations impact application performance?

No. MariaDB Backup (mariabackup) is used for Replicated Transactions and Single Node Transactions service backups. MariaDB Backup breaks up backups into non-blocking stages so writes and schema changes can occur during backups.

### How long are backups retained?

SkySQL's nightly backups as well as self-service backups are retained for 7 days.

### Does MariaDB Cloud support Point-in-Time Recovery (PITR)?

By default, full and complete backup restoration is available. To enable point-in-time recovery, services must be configured in advance for additional binary log retention. [Point-in-time recovery (PITR)](../cloud-data-handling/backup-and-restore/restore-examples/point-in-time-restore.md) configuration is available to Power Tier customers.

### How long do you keep my data when I delete a service?

All data residing on a service's storage is deleted at time of service deletion. Backups for deleted services are purged after 7 days.

## Security

### Will all my data be encrypted?

Yes. By default, MariaDB Cloud encrypts all data-in-transit using standard SSL/TSL. While not recommended, you can disable SSL/TLS connections while launching a database service. MariaDB Cloud leverages HashiCorp Vault for certificate and key management. Certificates and keys are not customer-configurable at this time.

All data-at-rest is encrypted using standard cloud encryption options.

* Amazon AWS[Amazon EBS encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSEncryption.html).
* Google Cloud [encryption by default](https://cloud.google.com/security/encryption-at-rest/default-encryption).
* Microsoft Azure [default encryption](https://docs.microsoft.com/en-us/azure/virtual-machines/disk-encryption).

### Are client certificates supported?

No. MariaDB Cloud supports server-side certificates. Database users are authenticated by standard password authentication.

## Support

### How do I contact support?

You can contact Support using the [Support Portal](https://mariadb.com/services/technical-support-services/) or by emailing [support@skysql.com](mailto:support@skysql.com).

### What support options are available for MariaDB Cloud?

All customers with a valid payment profile receive Standard Support which includes 24x5, 2-hours response for P1 incidents. Standard Support is available at no extra charge. Enterprise Support provides 24x7, 30-min response for P1 incidents and is suitable for mission-critical workloads. [CloudDBA](fractionaldba.md) is our premiere fractional DBA service that gives you direct access to our highly skilled DBA team who can provide technical expertise, guidance, and troubleshooting assistance when needed. See the [Support](https://mariadb.com/services/technical-support-services/) page for full details on our support options.

### Is 24x7x365 support available for mission-critical applications?

Yes. [Enterprise Support](mariadb-server-versions.md) levels are available for customers requiring 24x7x365 support (24 hours per day, 7 days per week, 365 (or 366) days per year).

### **What professional services are available for MariaDB Cloud?**

MariaDB Cloud offers a full range of professional services, including:

* [CloudDBA](fractionaldba.md) for proactive and reactive support
* [Migration](../cloud-data-handling/migration-data-loading/data-loading-migration/) assistance
* Assistance with your MariaDB Cloud proof-of-concept
