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
* Option to make `SHUTDOWN` wait for all replicas by default, with the `shutdown_wait_for_slaves` system variable
* [MariaDB Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7)
  * XA Support
  * Non-Blocking operation for DDLs
  * TLS certificate expiration monitoring
  * SSL/TLS enabled by default
* [MariaDB Raft Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/AmWSwHTrMJB8ojX2p6gW)
* [Conflict Detection and Resolution (CDR)](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/conflict-detection-and-resolution-triggers)
* [Password-less authentication with TLS certificates](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-tls-certificate), with the `tls_certificate` authentication plugin
* [Enhanced Enterprise Data-at-Rest Encryption](mariadb-enterprise-server-data-at-rest-encryption/)
* Sybase SQL mode for extended aliases

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
