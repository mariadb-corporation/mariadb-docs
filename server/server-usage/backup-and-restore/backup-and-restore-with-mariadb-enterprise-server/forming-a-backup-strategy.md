---
description: >-
  Learn how to design a robust backup strategy tailored to your business needs,
  balancing recovery time objectives and data retention policies.
---

# Forming a Backup Strategy

## Overview

The strategy applied when implementing data backups depends on business needs.

Data backup strategy depends on business needs. Business needs can be evaluated by performing a data inventory, determining data [recovery objectives](forming-a-backup-strategy.md#recovery-objectives), considering the [replication environment](forming-a-backup-strategy.md#replication-considerations), and considering [encryption requirements](forming-a-backup-strategy.md#encryption-considerations). Also critical is a [backup storage strategy](forming-a-backup-strategy.md#backup-storage-considerations) and [testing backup and recovery procedures](forming-a-backup-strategy.md#backup-testing).

## Data Inventory

Backup strategy requirements flow from the understanding you build by performing a data inventory. A data inventory is established by asking questions such as:

1. What data is housed in the databases?
2. What business purpose does this data serve?
3. How long does the data needed to be retained in order to meet this business purpose?
4. Are there any legal or regulatory requirements, which would limit the length of data retention?

## Recovery Objectives

Data recovery requirements are often defined in terms of Recovery Point Objective (RPO) and Recovery Time Objective (RTO). RTO and RPO are considered in the context of the data identified in the [data inventory](forming-a-backup-strategy.md#data-inventory).

**Recovery Point Objective (RPO)** defines the maximum amount of data a business is willing to lose. For example, a business can define a RPO of 24 hours.

**Recovery Time Objective (RTO)** defines how quickly a business needs to restore service in the event of a fault. For example, a business can define a RTO of 8 hours.

Backup strategy plays a substantial role in achieving RPO and RTO.

## Achieving RPO

RPO depends on completion of backups, which provide a viable recovery point. Since RPO is measured at backup completion, not backup initiation, backup jobs must be scheduled at an interval smaller than the RPO.

Techniques for achieving RPO include:

* Frequent incremental backups and less frequent full backups.
* Performing backups in conjunction with replication and clustering to eliminate impact on production workloads, allowing a higher backup frequency.
* Automated monitoring of backup status.
* Automated testing of backups.

## Achieving RTO

The RTO window typically commences at the point when a decision is made by the business to recover from backups, not at the start of an incident.

Techniques for achieving RTO include:

* Leveraging information produced during incident response, which can reduce the set of data to restore from backups, or identify specific data validation requirements dependent on the nature of the incident.
* Having fast access to backup data. Performance requirements of backup infrastructure should be understood for both backup and restoration workloads.
* Using delayed replication, either within the same data center or to a different data center, can provide shorter path to recovery. This is particularly true when coupled with robust application monitoring, which allows intervention before the window of delay elapses.
* Applying written and tested recovery procedures, which designate the systems and commands to be used during recovery.
* Performing drills and exercises that periodically test recovery procedures to confirm readiness.

## Replication Considerations

MariaDB Enterprise Server supports several implementations of replication, which accurately duplicates data from one Server to one or more other Servers. The use of a dedicated replica as a source for backups can minimize workload impact.

MariaDB Enterprise Cluster implements virtually synchronous replication, where each Server instance contains a replica of all of the data for the Cluster. Backups can be performed from any node in the Cluster.

## Encryption Considerations

MariaDB Enterprise Server supports encryption on disk (data-at-rest encryption) and on the network (data-in-transit encryption).

MariaDB Enterprise Backup copies tablespaces from disk. When data-at-rest encryption is enabled, backups contain encrypted data.

MariaDB Enterprise Backup supports TLS encryption for communications with MariaDB Enterprise Server. To enable TLS encryption, set TLS options from the command-line or in the configuration file:

```bash
mariadb-backup --backup \
      --target-dir=/data/backups/full \
      --user=mariadb-backup \
      --password=mbu_passwd \
      --ssl-ca=/etc/my.cnf.d/certs/ca.pem \
      --ssl-cert=/etc/my.cnf.d/certs/client-cert.pem \
      --ssl-key=/etc/my.cnf.d/certs/client-key.pem
```

## Backup Storage Considerations

How backups are stored can impact backup viability. Backup storage also presents separate risks. These risks need to be carefully considered:

* Backup data should always be stored separately from the system being backed up, and separate from the system used for recovery.
* Backup data should be subject to equal or more controls than data in production databases. For example, backup data should generally be encrypted even where a decision has bee made that a production database will not use data-at-rest encryption.
* Business requirements may define a need for offsite storage of backups as a means of guaranteeing delivery on RPO. In these cases you should also consider onsite storage of backups as a means of guaranteeing delivery on RTO.
* Retention requirements and the run-rate of new data production can aid in capacity planning.

## Backup Testing

Testing has been identified as a critical success factor for the successful operation of data systems.

Backups should be tested. Recovery using backups and recovery procedures should be tested.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
