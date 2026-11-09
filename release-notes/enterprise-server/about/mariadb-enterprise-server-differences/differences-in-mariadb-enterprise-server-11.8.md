---
description: >-
  Features that are in MariaDB Enterprise Server 11.8 but not in MariaDB
  Community Server 11.8
---

# Differences in MariaDB Enterprise Server 11.8

MariaDB Enterprise Server is a premium version of MariaDB Community Server that focuses on stability, robustness, and predictability.

In addition to different release cycles, QA, etc, there are also feature differences. MariaDB Enterprise Server has different default settings to be more secure from the start, and also only includes features that are fully supported and maintained.

In addition to this, there are Enterprise Features and some backported features. The following are features that are in MariaDB Enterprise Server 11.8 but not in MariaDB Community Server 11.8:

## Enterprise Features

* [MariaDB Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup)
* [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-enterprise-audit)
* Index limit increased to 128 indexes.
* [Slow master shutdown]({server}/server-management/variables-and-modes/server-system-variables#shutdown_wait_for_slaves) as default
* [MariaDB Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/)
  * XA Support
  * [Non-Blocking Operations (NBO) for DDLs]({galera}/galera-management/general-operations/performing-schema-upgrades-in-galera-cluster#non-blocking-operations-nbo)
  * TLS certificate expiration monitoring, with the [wsrep\_certificate\_expiration\_hours\_warning]({galera}/reference/wsrep-variable-details/wsrep_certificate_expiration_hours_warning) system variable
  * [SSL/TLS enabled by default]({galera}/galera-security/mariadb-enterprise-cluster-security#wsrep-tls-modes)
  * Performance Schema tables `galera_group_members` and `galera_group_member_stats`, with the cluster's configuration and each node's performance
  * [WSREP\_BF\_ABORTS]({server}/reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_bf_aborts) Information Schema table, with the history of brute force aborts
  * [WSREP\_CERT\_KEYS]({server}/reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_cert_keys) and [WSREP\_CERT\_KEYS\_HISTORY]({server}/reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_cert_keys_history) Information Schema tables, with the certification keys of current and recent transactions
  * [WSREP\_CONNECTIONS]({server}/reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_connections) Information Schema table, to verify that connections between nodes use TLS
  * [WSREP\_THD\_STATE]({server}/reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_thd_state) and [WSREP\_THD\_STATE\_HISTORY]({server}/reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_thd_state_history) Information Schema tables, with the wsrep execution state of each thread
* [Enhanced Enterprise Data-at-Rest Encryption](mariadb-enterprise-server-data-at-rest-encryption/)
* Dynamic resize of [InnoDB redo log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-redo-log)
* Dynamic change of [InnoDB purge](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-purge) threads
* Sybase SQL mode for extended aliases

## **Backported Features**

{% include "../../../.gitbook/includes/backports-11.8.5-2-and-11.4.9-6.md" %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
