---
description: >-
  Features that are in MariaDB Enterprise Server 12.3 but not in MariaDB
  Community Server 12.3
---

# Differences in MariaDB Enterprise Server 12.3

MariaDB Enterprise Server is a hardened, secured, and fully supported version of MariaDB Server with added Enterprise-only features. For how it compares with MariaDB Community Server, see [Editions & Compatibility](../README.md).

In addition to different release cycles, QA, etc, there are also feature differences. MariaDB Enterprise Server has different default settings to be more secure from the start, and also only includes features that are fully supported and maintained.

In addition to this, there are Enterprise Features. The following are features that are in MariaDB Enterprise Server 12.3 but not in MariaDB Community Server 12.3:

## Enterprise Features

* [MariaDB Backup](../../server-usage/backup-and-restore/mariadb-backup/README.md)
* [MariaDB Enterprise Audit](../../reference/plugins/mariadb-enterprise-audit/README.md)
  * [JSON-formatted audit log](../../reference/plugins/mariadb-enterprise-audit/mariadb-enterprise-audit-log-destinations-and-format.md#json-format), selected with the `server_audit_log_format` system variable
* Index limit increased to 128 indexes
* Option to make `SHUTDOWN` wait for all replicas by default, with the [`shutdown_wait_for_slaves`](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#shutdown_wait_for_slaves) system variable
* [MariaDB Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7)
  * XA Support
  * [Non-Blocking Operations (NBO) for DDLs](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/galera-management/general-operations/performing-schema-upgrades-in-galera-cluster#non-blocking-operations-nbo)
  * TLS certificate expiration monitoring, with the [wsrep\_certificate\_expiration\_hours\_warning](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/reference/wsrep-variable-details/wsrep_certificate_expiration_hours_warning) system variable
  * [SSL/TLS enabled by default](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/galera-security/mariadb-enterprise-cluster-security#wsrep-tls-modes)
  * Performance Schema tables `galera_group_members` and `galera_group_member_stats`, with the cluster's configuration and each node's performance
  * [WSREP\_BF\_ABORTS](../../reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_bf_aborts.md) Information Schema table, with the history of brute force aborts
  * [WSREP\_CERT\_KEYS](../../reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_cert_keys.md) and [WSREP\_CERT\_KEYS\_HISTORY](../../reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_cert_keys_history.md) Information Schema tables, with the certification keys of current and recent transactions
  * [WSREP\_CONNECTIONS](../../reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_connections.md) Information Schema table, to verify that connections between nodes use TLS
  * [WSREP\_THD\_STATE](../../reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_thd_state.md) and [WSREP\_THD\_STATE\_HISTORY](../../reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_thd_state_history.md) Information Schema tables, with the wsrep execution state of each thread
* [MariaDB Raft Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/AmWSwHTrMJB8ojX2p6gW)
* [Conflict Detection and Resolution (CDR)](../../ha-and-performance/standard-replication/conflict-detection-and-resolution-triggers.md)
* [Password-less authentication with TLS certificates](../../reference/plugins/authentication-plugins/authentication-plugin-tls-certificate.md), with the `tls_certificate` authentication plugin
* [Enhanced Enterprise Data-at-Rest Encryption](mariadb-enterprise-server-data-at-rest-encryption/)
* Sybase SQL mode for extended aliases

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
