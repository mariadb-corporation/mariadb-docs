---
description: >-
  An overview of changes, improvements, and what's new in MariaDB Enterprise
  Server 10.4
---

# What's New in MariaDB Enterprise Server 10.4?

MariaDB Enterprise Server 10.4 introduces the following new features:

## Enterprise Lifecycle

MariaDB Enterprise Server uses an [enterprise lifecycle](../../enterprise-server-lifecycle.md) that provides optimized builds, predictable release behavior, and vendor support.

## InnoDB Instant ALTER

[Instant ALTER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-instant-alter-algorithm) enables reliable and predictable schema change behavior.

## Optimizer Trace

[Optimizer Trace](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/index-hints-how-to-force-query-plans) collects trace data to aid query optimization and diagnosis of query execution issues.

## Temporal Data

[Temporal data table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables) support has been expanded from system-versioned tables to also include application-time period and bitemporal tables.

## Enterprise Audit Plugin

[MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-enterprise-audit) provides support for auditing resource access to MariaDB Enterprise Server.

## Enterprise Backup

[MariaDB Enterprise Backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-enterprise-backup) enables non-blocking backups of MariaDB Enterprise Server.

## Data-at-Rest Encryption

With [data-at-rest encryption](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/cve), data is encrypted before writing to the disk and decrypted when read from disk. MariaDB Enterprise Server extends data-at-rest encryption support to include:

* Encryption of Spatial indexes
* Key rotation when encrypting the InnoDB Redo Log
* Encryption of MariaDB Enterprise Cluster's write-set cache (GCache)

## MariaDB Enterprise Cluster

MariaDB Enterprise Server includes support for [MariaDB Enterprise Cluster](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/), which incorporates Galera Cluster 4. New features include:

* Parallel replication and improved performance when blocks of grouped transactions can be committed without conflict.
* The [Streaming replication](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/readme/about-galera-replication#streaming-replication), to eliminate transaction limitations by fragmenting huge transactions for replication.
* Rolling upgrades to permit a smooth transition of MariaDB Cluster deployments to Galera 4 functionality by operating as a Galera 3-compatible node until all nodes are Galera 4-compatible.

## Data Reliability and SQL Functionality

MariaDB Enterprise Server includes changes to improve data reliability and SQL functionality:

* System tables use the Aria storage engine, making them crash-safe.
* UNIQUE index support for the BLOB data type.
* [JSON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/json) data type validation.
* Parentheses in UNION, INTERSECT, and EXCEPT operations to control order of execution.

## Enhanced Credential Management

MariaDB Enterprise Server features [security](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/cve) improvements, including:

* Ability to reload SSL certificates without server restart.
* SET PASSWORD option to specify authentication plugins.
* Improved support for authentication plugins, including the ability to set multiple authentication plugins on individual users. Also supported is fallback on internal methods, such as password authentication.
* ALTER USER option for account locking, to enable MariaDB Enterprise Server to reject all new connections for an account.
* Account blocking based on number of failed login attempts.
* Ability to set password expiration dates.
* Logging of access when passwords are ignored, e.g., for password less authentication by UNIX socket.


## Security Vulnerabilities (CVE) Fixed in MariaDB Enterprise Server 10.4

For a complete list of security vulnerabilities (CVE) fixed across all versions of MariaDB Enterprise Server, see the [Security Vulnerabilities Fixed in MariaDB Enterprise Server](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/cve/enterprise-server) page.

| CVE ID (with cve.org link)                                        | CVSS base score | Enterprise Server 10.4 Release |
| ------------------------------------------------------------------| --------------- | ------------------------------ |
| [CVE-2023-22084](https://www.cve.org/CVERecord?id=CVE-2023-22084) | 4.9             | [10.4.32-22](10.4.32-22.md)    |
| [CVE-2022-47015](https://www.cve.org/CVERecord?id=CVE-2022-47015) | N/A (Medium) [<sup>#1</sup>](#id-1) | [10.4.30-20](10.4.30-20.md) |
| [CVE-2023-5157](https://www.cve.org/CVERecord?id=CVE-2023-5157)   | 7.5             | [10.4.26-17](10.4.26-17.md)    |
| [CVE-2018-25032](https://www.cve.org/CVERecord?id=CVE-2018-25032) | 7.5             | [10.4.26-17](10.4.26-17.md)    |
| [CVE-2022-32091](https://www.cve.org/CVERecord?id=CVE-2022-32091) | 6.5             | [10.4.26-17](10.4.26-17.md)    |
| [CVE-2022-32089](https://www.cve.org/CVERecord?id=CVE-2022-32089) | 6.5             | [10.4.26-17](10.4.26-17.md)    |
| [CVE-2022-32084](https://www.cve.org/CVERecord?id=CVE-2022-32084) | 6.5             | [10.4.26-17](10.4.26-17.md)    |
| [CVE-2022-32081](https://www.cve.org/CVERecord?id=CVE-2022-32081) | 6.5             | [10.4.26-17](10.4.26-17.md)    |
| [CVE-2022-27458](https://www.cve.org/CVERecord?id=CVE-2022-27458) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-27457](https://www.cve.org/CVERecord?id=CVE-2022-27457) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-27456](https://www.cve.org/CVERecord?id=CVE-2022-27456) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-27455](https://www.cve.org/CVERecord?id=CVE-2022-27455) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-27452](https://www.cve.org/CVERecord?id=CVE-2022-27452) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-27451](https://www.cve.org/CVERecord?id=CVE-2022-27451) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-27449](https://www.cve.org/CVERecord?id=CVE-2022-27449) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-27448](https://www.cve.org/CVERecord?id=CVE-2022-27448) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-27447](https://www.cve.org/CVERecord?id=CVE-2022-27447) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-27446](https://www.cve.org/CVERecord?id=CVE-2022-27446) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-27445](https://www.cve.org/CVERecord?id=CVE-2022-27445) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-27444](https://www.cve.org/CVERecord?id=CVE-2022-27444) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-27387](https://www.cve.org/CVERecord?id=CVE-2022-27387) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-27386](https://www.cve.org/CVERecord?id=CVE-2022-27386) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-27384](https://www.cve.org/CVERecord?id=CVE-2022-27384) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-27383](https://www.cve.org/CVERecord?id=CVE-2022-27383) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-27382](https://www.cve.org/CVERecord?id=CVE-2022-27382) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-27381](https://www.cve.org/CVERecord?id=CVE-2022-27381) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-27380](https://www.cve.org/CVERecord?id=CVE-2022-27380) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-27379](https://www.cve.org/CVERecord?id=CVE-2022-27379) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-27378](https://www.cve.org/CVERecord?id=CVE-2022-27378) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-27377](https://www.cve.org/CVERecord?id=CVE-2022-27377) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-27376](https://www.cve.org/CVERecord?id=CVE-2022-27376) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-21451](https://www.cve.org/CVERecord?id=CVE-2022-21451) | 7.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-32088](https://www.cve.org/CVERecord?id=CVE-2022-32088) | 6.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-32087](https://www.cve.org/CVERecord?id=CVE-2022-32087) | 6.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-32086](https://www.cve.org/CVERecord?id=CVE-2022-32086) | 6.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-32085](https://www.cve.org/CVERecord?id=CVE-2022-32085) | 6.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-32083](https://www.cve.org/CVERecord?id=CVE-2022-32083) | 6.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2021-46669](https://www.cve.org/CVERecord?id=CVE-2021-46669) | 6.5             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2022-21427](https://www.cve.org/CVERecord?id=CVE-2022-21427) | 4.9             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2021-46668](https://www.cve.org/CVERecord?id=CVE-2021-46668) | 5.5             | [10.4.24-15](10.4.24-15.md)    |
| [CVE-2021-46665](https://www.cve.org/CVERecord?id=CVE-2021-46665) | 5.5             | [10.4.24-15](10.4.24-15.md)    |
| [CVE-2021-46664](https://www.cve.org/CVERecord?id=CVE-2021-46664) | 5.5             | [10.4.24-15](10.4.24-15.md)    |
| [CVE-2021-46663](https://www.cve.org/CVERecord?id=CVE-2021-46663) | 5.5             | [10.4.24-15](10.4.24-15.md)    |
| [CVE-2021-46661](https://www.cve.org/CVERecord?id=CVE-2021-46661) | 5.5             | [10.4.24-15](10.4.24-15.md)    |
| [CVE-2021-46659](https://www.cve.org/CVERecord?id=CVE-2021-46659) | 5.5             | [10.4.24-15](10.4.24-15.md)    |
| [CVE-2022-21595](https://www.cve.org/CVERecord?id=CVE-2022-21595) | 4.4             | [10.4.24-15](10.4.24-15.md)    |
| [CVE-2022-27385](https://www.cve.org/CVERecord?id=CVE-2022-27385) | 7.5             | [10.4.22-14](10.4.22-14.md)    |
| [CVE-2021-46667](https://www.cve.org/CVERecord?id=CVE-2021-46667) | 7.5             | [10.4.22-14](10.4.22-14.md)    |
| [CVE-2022-31624](https://www.cve.org/CVERecord?id=CVE-2022-31624) | 6.5             | [10.4.22-14](10.4.22-14.md)    |
| [CVE-2021-46662](https://www.cve.org/CVERecord?id=CVE-2021-46662) | 5.5             | [10.4.22-14](10.4.22-14.md)    |
| [CVE-2021-35604](https://www.cve.org/CVERecord?id=CVE-2021-35604) | 5.5             | [10.4.22-14](10.4.22-14.md)    |
| [CVE-2021-2389](https://www.cve.org/CVERecord?id=CVE-2021-2389)   | 5.9             | [10.4.21-13](10.4.21-13.md)    |
| [CVE-2021-46666](https://www.cve.org/CVERecord?id=CVE-2021-46666) | 5.5             | [10.4.21-13](10.4.21-13.md)    |
| [CVE-2021-46658](https://www.cve.org/CVERecord?id=CVE-2021-46658) | 5.5             | [10.4.21-13](10.4.21-13.md)    |
| [CVE-2021-46657](https://www.cve.org/CVERecord?id=CVE-2021-46657) | 5.5             | [10.4.21-13](10.4.21-13.md)    |
| [CVE-2021-2372](https://www.cve.org/CVERecord?id=CVE-2021-2372)   | 4.4             | [10.4.21-13](10.4.21-13.md)    |
| [CVE-2021-2166](https://www.cve.org/CVERecord?id=CVE-2021-2166)   | 4.9             | [10.4.19-12](10.4.19-12.md)    |
| [CVE-2021-2154](https://www.cve.org/CVERecord?id=CVE-2021-2154)   | 4.9             | [10.4.19-12](10.4.19-12.md)    |
| [CVE-2021-27928](https://www.cve.org/CVERecord?id=CVE-2021-27928) | N/A (Critical) [<sup>#1</sup>](#id-1) | [10.4.18-11](10.4.18-11.md) |
| [CVE-2020-14765](https://www.cve.org/CVERecord?id=CVE-2020-14765) | 6.5             | [10.4.17-10](10.4.17-10.md)    |
| [CVE-2022-21427](https://www.cve.org/CVERecord?id=CVE-2022-21427) | 4.9             | [10.4.25-16](10.4.25-16.md)    |
| [CVE-2020-14789](https://www.cve.org/CVERecord?id=CVE-2020-14789) | 4.9             | [10.4.17-10](10.4.17-10.md)    |
| [CVE-2020-14776](https://www.cve.org/CVERecord?id=CVE-2020-14776) | 4.9             | [10.4.17-10](10.4.17-10.md)    |
| [CVE-2020-28912](https://www.cve.org/CVERecord?id=CVE-2020-28912) | N/A (Critical) [<sup>#1</sup>](#id-1) | [10.4.17-10](10.4.17-10.md) |
| [CVE-2020-15180](https://www.cve.org/CVERecord?id=CVE-2020-15180) | N/A (Critical) [<sup>#1</sup>](#id-1) | [10.4.15-9](10.4.15-9.md) |
| [CVE-2021-2022](https://www.cve.org/CVERecord?id=CVE-2021-2022)   | 4.4             | [10.4.14-8](10.4.14-8.md)      |
| [CVE-2020-2760](https://www.cve.org/CVERecord?id=CVE-2020-2760)   | 5.5             | [10.4.13-7](10.4.13-7.md)      |
| [CVE-2020-2752](https://www.cve.org/CVERecord?id=CVE-2020-2752)   | 5.3             | [10.4.13-7](10.4.13-7.md)      |
| [CVE-2020-2814](https://www.cve.org/CVERecord?id=CVE-2020-2814)   | 4.9             | [10.4.13-7](10.4.13-7.md)      |
| [CVE-2020-2812](https://www.cve.org/CVERecord?id=CVE-2020-2812)   | 4.9             | [10.4.13-7](10.4.13-7.md)      |
| [CVE-2020-13249](https://www.cve.org/CVERecord?id=CVE-2020-13249) | N/A (Medium) [<sup>#1</sup>](enterprise-server.md#id-1) | [10.4.13-7](10.4.13-7.md) |
| [CVE-2020-7221](https://www.cve.org/CVERecord?id=CVE-2020-7221)   | 7.8             | [10.4.12-6](10.4.12-6.md)      |
| [CVE-2020-2574](https://www.cve.org/CVERecord?id=CVE-2020-2574)   | 5.9             | [10.4.12-6](10.4.12-6.md)      |
| [CVE-2020-2780](https://www.cve.org/CVERecord?id=CVE-2020-2780)   | 6.5             | [10.4.10-4](10.4.10-4.md)      |
| [CVE-2019-2974](https://www.cve.org/CVERecord?id=CVE-2019-2974)   | 6.5             | [10.4.10-4](10.4.10-4.md)      |
| [CVE-2019-2938](https://www.cve.org/CVERecord?id=CVE-2019-2938)   | 4.4             | [10.4.10-4](10.4.10-4.md)      |
| [CVE-2019-2805](https://www.cve.org/CVERecord?id=CVE-2019-2805)   | 6.5             | [10.4.7-2](10.4.7-2.md)        |
| [CVE-2019-2740](https://www.cve.org/CVERecord?id=CVE-2019-2740)   | 6.5             | [10.4.7-2](10.4.7-2.md)        |
| [CVE-2019-2758](https://www.cve.org/CVERecord?id=CVE-2019-2758)   | 5.5             | [10.4.7-2](10.4.7-2.md)        |
| [CVE-2019-2739](https://www.cve.org/CVERecord?id=CVE-2019-2739)   | 5.1             | [10.4.7-2](10.4.7-2.md)        |
| [CVE-2019-2737](https://www.cve.org/CVERecord?id=CVE-2019-2737)   | 4.9             | [10.4.7-2](10.4.7-2.md)        |
| [CVE-2021-2007](https://www.cve.org/CVERecord?id=CVE-2021-2007)   | 3.7             | [10.4.7-2](10.4.7-2.md)        |
| [CVE-2020-2922](https://www.cve.org/CVERecord?id=CVE-2020-2922)   | 3.7             | [10.4.7-2](10.4.7-2.md)        |

#### #1:

MariaDB CVEs are assigned a word rating instead of a CVSS base score. See the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies/) for details.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
