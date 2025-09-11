# Release Notes for MariaDB Enterprise Server 10.3.39-20

MariaDB Enterprise Server 10.3.39-20 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.3. |This release includes a variety of fixes.

MariaDB Enterprise Server 10.3.39-20 was released on 2023-06-13.

MariaDB Enterprise Server 10.3 is EOL (end-of-life) as of 2023-05-25. Users of this release series should upgrade to a more recent Enterprise Server release series.

## Fixed Security Vulnerabilities

| CVE (with cve.org link)                                                             | CVSS base score                                                           |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| [CVE-2022-47015](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47015) N/A | (Medium)[#1](release-notes-for-mariadb-enterprise-server-10-3-39-20.md#1) |

`#1`:\
MariaDB CVEs are assigned a word rating instead of a CVSS base score. See the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies) for details.

## Issues Fixed

### Can result in data loss

* When [binlog\_row\_image=FULL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is set and [slave\_parallel\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is greater than 0, replica servers can hang if data is inserted into tables with a sequence. ([MDEV-29621](https://jira.mariadb.org/browse/MDEV-29621))

## Platforms

In alignment with the [enterprise lifecycle](../../enterprise-server-lifecycle.md), MariaDB Enterprise Server 10.3.39-20 is provided for:

* CentOS 7 (x86\_64)
* Debian 10 (x86\_64, ARM64)
* Microsoft Windows (x86\_64) (MariaDB Enterprise Cluster excluded)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see ["MariaDB Corporation Engineering Policies"](https://mariadb.com/engineering-policies).

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formid="4316" formId="4316" %}
