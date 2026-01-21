---
description: >-
  A guide outlining essential recommendations for stable MariaDB deployments,
  covering backup strategies, change management, security controls, and
  pre-production testing.
---

# Best Practices

These best practices warrant consideration, but are not expected to apply to every business or in every situation. Recommendations here are not mandatory.

## General Recommendations

We recommend that you:

* Understand business requirements before deployment.
* Adapt deployment practices to align to business requirements.
* Consider to what extent deployed systems should integrate with existing business systems and practices.

## Backups

Addition, removal, and change of database systems are types of production changes. Before undertaking any production changes:

* Perform a backup of existing data and database configurations.
* Establish a plan for data restoration for use in reverting a change.
* Perform a test to confirm your backup is complete and viable.

### Irreversible Changes

Installation of new database servers, change of server configuration, migrations, upgrades, and downgrades can produce irreversible changes which may require you to restore from the last good backup.

Changes to data format on disk, including from upgrades and downgrades, are generally irreversible. A fault during the upgrade or downgrade process may corrupt data. Confirm you have a recent, full, complete, and tested backup before any upgrade or downgrade operation.

When [System-Versioned temporal data tables](../../../reference/sql-structure/temporal-tables/) are in use, downgrade operations will generally require migration of data between servers or restore from a backup made pre-upgrade.

### Full and Complete Backup

Before proceeding with an upgrade, perform a full and complete backup. Confirm successful completion of the backup operation and test the backup.

Business requirements may require you to retain backups made to support upgrade and downgrade operations.

Additional information regarding backing up and restoring MariaDB database products can be found in "[Recovery](../../../server-usage/storage-engines/innodb/innodb-troubleshooting/innodb-recovery-modes.md)".

## Change Management

### Change Management, Automation, Orchestration

Server configuration changes should be done through change management. Accurate records of the time of change and reason for change can enable faster issue diagnosis.

Automation can enable repeatability of change deployment, and can aid Pre-Production and Post-Production testing.

Automation or orchestration can enable repeatability of server deployment, including system provisioning.

## Production Controls

### Dedicated Servers

Database servers exist to run database server software. Database servers should not also run web server software, act as a file server, or run other workloads.

Understand workload and data isolation requirements before server deployment. Isolation requirements are often defined through business requirements, including:

* Data and application security requirements that trigger isolation of one workload from other workloads.
* Separation of Development and Testing environments from Production environments.

### Production Controls

Understand control requirements before server deployment, including records of control implementation needed to support audits.

Control requirements typically follow data:

* Both production and non-production systems may require production-level controls based on the presence of data subject to control.
* Database servers, backup servers, and other systems may require production-level controls based on the presence of data subject to control.

## Testing

Servers should be validated before exposure to production workloads and production data.

It may be appropriate to prevent access to an unconfigured server until configured and validated. Load balancer configuration, firewall rules, or database server configuration are often used to prevent unintended traffic to new servers.

Details assessed during Pre-Production validation can include:

* Server capacity, including performance of disk systems
* Server security configuration and hardening
* Tuning for initial data load vs production workloads
* Alignment to business requirements

## Updates

MariaDB Product Notifications allow you to keep aware of new releases, including security fixes. Customers can manage MariaDB Product Notifications through the [MariaDB Customer Portal](https://customers.mariadb.com/?_ga=2.24188474.1431602578.1740983101-1710706710.1737441288).

Additionally, MariaDB Enterprise Server follows an enterprise lifecycle, that provides a [predictable release schedule](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/about/enterprise-server-release-schedule).

## Obtaining Support

MariaDB Corporation provides commercial support and services for MariaDB database products.

New customers can [contact MariaDB Corporation](https://mariadb.com/contact) for more information.

Existing MariaDB Subscription customers can access technical support via the [MariaDB Customer Portal](https://customers.mariadb.com/?_ga=2.262787980.1431602578.1740983101-1710706710.1737441288) as detailed in [MariaDB Subscription Services Policy](https://mariadb.com/subscription-services-policies).

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
