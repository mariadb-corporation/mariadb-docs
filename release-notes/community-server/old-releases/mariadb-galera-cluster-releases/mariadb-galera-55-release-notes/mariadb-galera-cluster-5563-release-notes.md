# MariaDB Galera Cluster 5.5.63 Release Notes

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.63)[Release Notes](mariadb-galera-cluster-5563-release-notes.md)[Changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5563-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 1 Feb 2019

MariaDB Galera Cluster 5.5.63 is a [_**Stable**_](../../../about/release-criteria.md) (GA)\
release. It is a merge of [MariaDB 5.5.63](../../release-notes-mariadb-5-5-series/mariadb-5563-release-notes.md) and [Galera Cluster](https://codership.com/content/using-galera-cluster) with\
additional bug fixes.

Various articles about MariaDB Galera Cluster, including [known limitations](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/mariadb-galera-cluster-known-limitations) and [how to get started](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster) are\
available in the [**Galera**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/galera/README.md) section of the documentation.

## Updates and fixes in this version

* This release is a maintenance release.
* Codership changes:[github.com/codership/mysql-wsrep/tree/5.5](https://github.com/codership/mysql-wsrep/tree/5.5)
* The [Galera library](https://codership.com/content/using-galera-cluster) used\
  by MariaDB Galera Cluster and included in the MariaDB repositories is\
  currently at version 25.3.25.
* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * [CVE-2019-2529](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2529)

See the [MariaDB 5.5.63 Release Notes](../../release-notes-mariadb-5-5-series/mariadb-5563-release-notes.md) for more\
information on fixes in this version.

## Changelog

A full list of all changes is in the [MariaDB Galera Cluster 5.5.63 Changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5563-changelog.md)\
and the [MariaDB 5.5.63 Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5563-changelog.md).

## Contributors

For a full list of contributors to MariaDB Galera Cluster 5.5.63, see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-galera-cluster-5-5-63-now-available/).

## Notes

* Running MariaDB Galera Cluster 5.5 and 10.0 nodes in a cluster is not\
  supported ([MDEV-6257](https://jira.mariadb.org/browse/MDEV-6257))
* This version of MariaDB Galera Cluster supports `wsrep` API v25 which means\
  MariaDB Galera Cluster can be used with either a 25.2.x or 25.3.x

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
