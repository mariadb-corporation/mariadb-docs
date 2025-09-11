# MariaDB Galera Cluster 5.5.55 Release Notes

The most recent [MariaDB Galera Cluster 5.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) release is:[**MariaDB Galera Cluster 5.5.63**](mariadb-galera-cluster-5563-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/5.5.63)

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.55)[Release Notes](mariadb-galera-cluster-5555-release-notes.md)[Changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5555-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 22 Apr 2017

MariaDB Galera Cluster 5.5.55 is a [_**Stable**_](../../../about/release-criteria.md) (GA)\
release. It is a merge of [MariaDB 5.5.55](../../release-notes-mariadb-5-5-series/mariadb-5555-release-notes.md) and [Galera Cluster](https://codership.com/content/using-galera-cluster) with\
additional bug fixes.

Various articles about MariaDB Galera Cluster, including [known limitations](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/mariadb-galera-cluster-known-limitations) and [how to get started](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster) are\
available in the [**Galera**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) section of the documentation.

## Updates and fixes in this version

* This release is a bug-fix release.
* Codership changes:[github.com/codership/mysql-wsrep/tree/5.5](https://github.com/codership/mysql-wsrep/tree/5.5)\
  (till commit `9949137`)
* The [Galera library](https://codership.com/content/using-galera-cluster) used\
  by MariaDB Galera Cluster and included in the MariaDB repositories is\
  currently at version 25.3.19.
* As per the [MariaDB Deprecation Policy](../../../about/platform-deprecation-policy.md), this will be\
  the last release of MariaDB Galera Cluster 5.5 for Ubuntu 12.04 LTS\
  "Precise" and Mint 13 LTS "Maya"
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2017-3302](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3302)
  * [CVE-2017-3313](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3313)
  * [CVE-2017-3308](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3308)
  * [CVE-2017-3309](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3309)
  * [CVE-2017-3453](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3453)
  * [CVE-2017-3456](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3456)
  * [CVE-2017-3464](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-3464)

See the [MariaDB 5.5.55 Release Notes](../../release-notes-mariadb-5-5-series/mariadb-5555-release-notes.md) for more\
information on fixes in this version.

## Changelog

A full list of all changes is in the [MariaDB Galera Cluster 5.5.55 Changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5555-changelog.md)\
and the [MariaDB 5.5.55 Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5555-changelog.md).

## Notes

* Running MariaDB Galera Cluster 5.5 and 10.0 nodes in a cluster is not\
  supported ([MDEV-6257](https://jira.mariadb.org/browse/MDEV-6257))
* This version of MariaDB Galera Cluster supports `wsrep` API v25 which means\
  MariaDB Galera Cluster can be used with either a 25.2.x or 25.3.x

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
