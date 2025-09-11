# MariaDB Galera Cluster 10.0.11 Release Notes

The most recent [MariaDB Galera Cluster 10.0](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 10.0.38**](mariadb-galera-cluster-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/10.0.38)

[Download](https://downloads.mariadb.org/mariadb-galera/10.0.11)[Release Notes](mariadb-galera-cluster-10011-release-notes.md)[Changelog](../mariadb-galera-100-changelogs/mariadb-galera-cluster-10011-changelog.md)[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 11 Jun 2014

This is the 3rd release in the MariaDB Galera Cluster 10.0 series. It is a [_**Beta**_](../../../about/release-criteria.md) release. It is a merge of [MariaDB 10.0.10](../../release-notes-mariadb-10-0-series/mariadb-10010-release-notes.md)\
and [Galera Cluster](https://codership.com/content/using-galera-cluster) with\
additional bug fixes. It is being released now to get it into the hands of any\
who might want to test it. **Do not run Beta releases on production systems!**

Various articles about MariaDB Galera Cluster, including [known limitations](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/mariadb-galera-cluster-known-limitations) and [how to get started](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster) are\
available in the [**Galera**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) section of the documentation.

For a list of changes made in MariaDB Galera Cluster 10.0.11, with links to\
detailed information on each push, see the [MariaDB Galera Cluster 10.0.11 Changelog](../mariadb-galera-100-changelogs/mariadb-galera-cluster-10011-changelog.md).

## Updates and fixes in this version

* Galera `garbd` and `libgalera` are now included in the binary tarballs ([MDEV-4463](https://jira.mariadb.org/browse/MDEV-4463))
* Codership changes: `lp:codership-mysql/5.5` (till rev `3991`) & `lp:codership-mysql/5.6` (till rev `4091`).
* [Galera library](https://codership.com/content/using-galera-cluster) versions: 25.3.5, 25.2.9
* Supported wsrep interface API version: 25
* Fixes for the following security vulnerabilities:
  * [CVE-2014-2436](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-2436)
  * [CVE-2014-2440](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-2440)
  * [CVE-2014-2430](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-2430)
  * [CVE-2014-2431](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-2431)
  * [CVE-2019-2481](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2481)

## Notes

* Compatibility: Wsrep providers (Galera libraries) other than version 25.x.xx are not supported.
* See the [MariaDB 10.0.11 Release Notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/mariadb-galera-cluster-releases/mariadb-galera-100-release-notes/mariadb-galera-cluster-10011-release-notes) and [Changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-10011-changelog.md) for more information on the changes in\
  MariaDB.
* If Galera v2 and v3 are both being used in the cluster, MariaDB with\
  Galera v3 must be started with [wsrep\_provider\_options='socket.checksum=1'](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/wsrep-variable-details/wsrep_provider_options#socketchecksum)\
  in order to make it backward compatible with Galera v2.

Thanks, and enjoy MariaDB Galera Cluster!

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
