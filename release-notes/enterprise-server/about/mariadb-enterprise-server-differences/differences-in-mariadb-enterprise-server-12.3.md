---
description: >-
  Features that are in MariaDB Enterprise Server 12.3 but not in MariaDB
  Community Server 12.3
---

# Differences in MariaDB Enterprise Server 12.3

MariaDB Enterprise Server is a premium version of MariaDB Community Server that focuses on stability, robustness, and predictability.

In addition to different release cycles, QA, etc, there are also feature differences. MariaDB Enterprise Server has different default settings to be more secure from the start, and also only includes features that are fully supported and maintained.

In addition to this, there are Enterprise Features. The following are features that are in MariaDB Enterprise Server 12.3 but not in MariaDB Community Server 12.3:

## Enterprise Features

* [MariaDB Backup](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup)
* [MariaDB Enterprise Audit](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-enterprise-audit)
  * [JSON-formatted audit log](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-enterprise-audit/mariadb-enterprise-audit-log-destinations-and-format#json-format), selected with the `server_audit_log_format` system variable
* Index limit increased to 128 indexes
* Option to make `SHUTDOWN` wait for all replicas by default, with the [`shutdown_wait_for_slaves`]({server}/server-management/variables-and-modes/server-system-variables#shutdown_wait_for_slaves) system variable
* [MariaDB Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7)
  * XA Support
  * [Non-Blocking Operations (NBO) for DDLs]({galera}/galera-management/general-operations/performing-schema-upgrades-in-galera-cluster#non-blocking-operations-nbo)
  * TLS certificate expiration monitoring, with the [wsrep\_certificate\_expiration\_hours\_warning]({galera}/reference/wsrep-variable-details/wsrep_certificate_expiration_hours_warning) system variable
  * [SSL/TLS enabled by default]({galera}/galera-security/mariadb-enterprise-cluster-security#wsrep-tls-modes)
  * Performance Schema tables `galera_group_members` and `galera_group_member_stats`, with the cluster's configuration and each node's performance
  * [WSREP\_BF\_ABORTS]({server}/reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_bf_aborts) Information Schema table, with the history of brute force aborts
  * [WSREP\_CERT\_KEYS]({server}/reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_cert_keys) and [WSREP\_CERT\_KEYS\_HISTORY]({server}/reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_cert_keys_history) Information Schema tables, with the certification keys of current and recent transactions
  * [WSREP\_CONNECTIONS]({server}/reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_connections) Information Schema table, to verify that connections between nodes use TLS
  * [WSREP\_THD\_STATE]({server}/reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_thd_state) and [WSREP\_THD\_STATE\_HISTORY]({server}/reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_thd_state_history) Information Schema tables, with the wsrep execution state of each thread
* [MariaDB Raft Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/AmWSwHTrMJB8ojX2p6gW)
* [Conflict Detection and Resolution (CDR)](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/conflict-detection-and-resolution-triggers)
* [Password-less authentication with TLS certificates](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-tls-certificate), with the `tls_certificate` authentication plugin
* [Enhanced Enterprise Data-at-Rest Encryption](mariadb-enterprise-server-data-at-rest-encryption/)
* Sybase SQL mode for extended aliases

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
