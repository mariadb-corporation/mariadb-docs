---
description: >-
  An overview of changes, improvements, and what's new in MariaDB Enterprise
  Server 10.2
---

# What's New in MariaDB Enterprise Server 10.2?

MariaDB Enterprise Server 10.2 introduces the following new features:

## Enterprise Lifecycle

MariaDB Enterprise Server uses an [Enterprise Lifecycle](../../enterprise-server-lifecycle.md) which provides optimized builds, predictable release behavior, and vendor support.

## Enterprise Backup

[MariaDB Enterprise Backup](../10-2/broken-reference/) enables non-blocking backups of MariaDB Enterprise Server.

## Security Vulnerabilities (CVE) Fixed in MariaDB Enterprise Server 10.2

For a complete list of security vulnerabilities (CVE) fixed across all versions of MariaDB Enterprise Server, see the [Security Vulnerabilities Fixed in MariaDB Enterprise Server](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/cve/enterprise-server) page.

| CVE ID (with cve.org link)                                        | CVSS base score | Enterprise Server 11.4 Release |
| ----------------------------------------------------------------- | --------------- | ------------------------------ |
| [CVE-2021-46668](https://www.cve.org/CVERecord?id=CVE-2021-46668) | 5.5             | [10.2.43-15](10.2.43-15.md)    |
| [CVE-2021-46665](https://www.cve.org/CVERecord?id=CVE-2021-46665) | 5.5             | [10.2.43-15](10.2.43-15.md)    |
| [CVE-2021-46664](https://www.cve.org/CVERecord?id=CVE-2021-46664) | 5.5             | [10.2.43-15](10.2.43-15.md)    |
| [CVE-2021-46663](https://www.cve.org/CVERecord?id=CVE-2021-46663) | 5.5             | [10.2.43-15](10.2.43-15.md)    |
| [CVE-2021-46661](https://www.cve.org/CVERecord?id=CVE-2021-46661) | 5.5             | [10.2.43-15](10.2.43-15.md)    |
| [CVE-2021-46659](https://www.cve.org/CVERecord?id=CVE-2021-46659) | 5.5             | [10.2.43-15](10.2.43-15.md)    |
| [CVE-2022-21595](https://www.cve.org/CVERecord?id=CVE-2022-21595) | 4.4             | [10.2.43-15](10.2.43-15.md)    |
| [CVE-2021-46667](https://www.cve.org/CVERecord?id=CVE-2021-46667) | 7.5             | [10.2.41-14](10.2.41-14.md)    |
| [CVE-2022-31624](https://www.cve.org/CVERecord?id=CVE-2022-31624) | 6.5             | [10.2.41-14](10.2.41-14.md)    |
| [CVE-2021-35604](https://www.cve.org/CVERecord?id=CVE-2021-35604) | 5.5             | [10.2.41-14](10.2.41-14.md)    |
| [CVE-2021-2389](https://www.cve.org/CVERecord?id=CVE-2021-2389)   | 5.9             | [10.2.40-13](10.2.40-13.md)    |
| [CVE-2021-46666](https://www.cve.org/CVERecord?id=CVE-2021-46666) | 5.5             | [10.2.40-13](10.2.40-13.md)    |
| [CVE-2021-46658](https://www.cve.org/CVERecord?id=CVE-2021-46658) | 5.5             | [10.2.40-13](10.2.40-13.md)    |
| [CVE-2021-46657](https://www.cve.org/CVERecord?id=CVE-2021-46657) | 5.5             | [10.2.40-13](10.2.40-13.md)    |
| [CVE-2021-2372](https://www.cve.org/CVERecord?id=CVE-2021-2372)   | 4.4             | [10.2.40-13](10.2.40-13.md)    |
| [CVE-2021-2166](https://www.cve.org/CVERecord?id=CVE-2021-2166)   | 4.9             | [10.2.38-12](10.2.38-12.md)    |
| [CVE-2021-2154](https://www.cve.org/CVERecord?id=CVE-2021-2154)   | 4.9             | [10.2.38-12](10.2.38-12.md)    |
| [CVE-2021-27928](https://www.cve.org/CVERecord?id=CVE-2021-27928) | N/A (Critical) [<sup>#1</sup>](#id-1) | [10.2.37-11](10.2.37-11.md) |
| [CVE-2020-14765](https://www.cve.org/CVERecord?id=CVE-2020-14765) | 6.5             | [10.2.36-10](10.2.36-10.md)    |
| [CVE-2020-14812](https://www.cve.org/CVERecord?id=CVE-2020-14812) | 4.9             | [10.2.36-10](10.2.36-10.md)    |
| [CVE-2020-14789](https://www.cve.org/CVERecord?id=CVE-2020-14789) | 4.9             | [10.2.36-10](10.2.36-10.md)    |
| [CVE-2020-14776](https://www.cve.org/CVERecord?id=CVE-2020-14776) | 4.9             | [10.2.36-10](10.2.36-10.md)    |
| [CVE-2020-28912](https://www.cve.org/CVERecord?id=CVE-2020-28912) | N/A (Critical) [<sup>#1</sup>](#id-1) | [10.2.36-10](10.2.36-10.md) |
| [CVE-2020-15180](https://www.cve.org/CVERecord?id=CVE-2020-15180) | N/A (Critical) [<sup>#1</sup>](#id-1) | [10.2.34-9](10.2.34-9.md) |
| [CVE-2021-2022](https://www.cve.org/CVERecord?id=CVE-2021-2022)   | 4.4             | [10.2.33-8](10.2.33-8.md)      |
| [CVE-2020-2760](https://www.cve.org/CVERecord?id=CVE-2020-2760)   | 5.5             | [10.2.32-7](10.2.32-7.md)      |
| [CVE-2020-2752](https://www.cve.org/CVERecord?id=CVE-2020-2752)   | 5.3             | [10.2.32-7](10.2.32-7.md)      |
| [CVE-2020-2814](https://www.cve.org/CVERecord?id=CVE-2020-2814)   | 4.9             | [10.2.32-7](10.2.32-7.md)      |
| [CVE-2020-2812](https://www.cve.org/CVERecord?id=CVE-2020-2812)   | 4.9             | [10.2.32-7](10.2.32-7.md)      |
| [CVE-2020-13249](https://www.cve.org/CVERecord?id=CVE-2020-13249) | N/A (Medium) [<sup>#1</sup>](#id-1) | [10.2.32-7](10.2.32-7.md) |
| [CVE-2020-2574](https://www.cve.org/CVERecord?id=CVE-2020-2574)   | 5.9             | [10.2.31-6](10.2.31-6.md)      |
| [CVE-2020-2780](https://www.cve.org/CVERecord?id=CVE-2020-2780)   | 6.5             | [10.2.29-4](10.2.29-4.md)      |
| [CVE-2019-2974](https://www.cve.org/CVERecord?id=CVE-2019-2974)   | 6.5             | [10.2.29-4](10.2.29-4.md)      |
| [CVE-2019-2938](https://www.cve.org/CVERecord?id=CVE-2019-2938)   | 4.4             | [10.2.29-4](10.2.29-4.md)      |
| [CVE-2019-2805](https://www.cve.org/CVERecord?id=CVE-2019-2805)   | 6.5             | [10.2.26-2](10.2.26-2.md)      |
| [CVE-2019-2740](https://www.cve.org/CVERecord?id=CVE-2019-2740)   | 6.5             | [10.2.26-2](10.2.26-2.md)      |
| [CVE-2019-2758](https://www.cve.org/CVERecord?id=CVE-2019-2758)   | 5.5             | [10.2.26-2](10.2.26-2.md)      |
| [CVE-2019-2739](https://www.cve.org/CVERecord?id=CVE-2019-2739)   | 5.1             | [10.2.26-2](10.2.26-2.md)      |
| [CVE-2019-2737](https://www.cve.org/CVERecord?id=CVE-2019-2737)   | 4.9             | [10.2.26-2](10.2.26-2.md)      |
| [CVE-2021-2007](https://www.cve.org/CVERecord?id=CVE-2021-2007)   | 3.7             | [10.2.26-2](10.2.26-2.md)      |
| [CVE-2020-2922](https://www.cve.org/CVERecord?id=CVE-2020-2922)   | 3.7             | [10.2.26-2](10.2.26-2.md)      |

#### #1:

MariaDB CVEs are assigned a word rating instead of a CVSS base score. See the [MariaDB Engineering Policy](https://mariadb.com/engineering-policies/) for details.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
