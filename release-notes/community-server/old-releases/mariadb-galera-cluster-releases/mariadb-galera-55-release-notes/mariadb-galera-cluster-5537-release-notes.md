# MariaDB Galera Cluster 5.5.37 Release Notes

The most recent [MariaDB Galera Cluster 5.5](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 5.5.63**](mariadb-galera-cluster-5563-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/5.5.63)

[Download](https://downloads.mariadb.org/mariadb-galera/5.5.37) |**Release Notes** |[Changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5537-changelog.md) |[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 30 Apr 2014

MariaDB Galera Cluster 5.5.37 is a [_**Stable**_](../../../about/release-criteria.md) (GA) release.\
It is a merge of [MariaDB 5.5.37](../../release-notes-mariadb-5-5-series/mariadb-5537-release-notes.md) and [Galera Cluster](https://codership.com/content/using-galera-cluster) with\
additional bug fixes.

Various articles about MariaDB Galera Cluster, including [known limitations](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/mariadb-galera-cluster-known-limitations) and [how to get started](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster) are\
available in the [**Galera**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) section of the documentation.

For a list of changes made in MariaDB Galera Cluster 5.5.37, with links to detailed\
information on each push, see the [MariaDB Galera Cluster 5.5.37 Changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5537-changelog.md).

## Notes about this release

* MariaDB Galera Cluster 5.5.37 includes [MariaDB 5.5.37](../../release-notes-mariadb-5-5-series/mariadb-5537-release-notes.md) with Codership\
  additions (`lp:codership-mysql/5.5` till revision `3980`) and [Galera 25.3.5](https://codership.com/content/using-galera-cluster).
* This version of MariaDB Galera Cluster supports `wsrep` API v25 which means\
  MariaDB Galera Cluster can be used with either a 25.2.x or 25.3.x\
  Galera `wsrep` provider. A 25.3.x `wsrep` provider is included in the\
  MariaDB repositories and both 25.3.x and 25.2.x wsrep providers are available\
  on the downloads page.
* This release includes a new method for snapshot state\
  transfer, `wsrep_sst_xtrabackup-v2`. This method of state snapshot transfer\
  can be configured using the `--wsrep_sst_method=xtrabackup-v2`\
  option. Its use requires [Percona Xtrabackup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview) (>= 2.1.6) and other software packages\
  like socat, nc, and tar.

See the [MariaDB 5.5.37 Release Notes](../../release-notes-mariadb-5-5-series/mariadb-5537-release-notes.md) and [Changelog](../../../changelogs/changelogs-mariadb-55-series/mariadb-5537-changelog.md) for more information on the changes in\
MariaDB.

Note: If Galera 25.2.x and 25.3.x are both being used in the cluster, MariaDB\
with Galera 25.3.x must be started with`wsrep_provider_options='socket.checksum=1'` in order to make it backward\
compatible with Galera v2. Galera wsrep providers other than 25.3.x or 25.2.x\
are not supported.

Important: wsrep\_sst\_rsync (sst script) in MariaDB Galera Cluster 5.5.37 uses `lsof` which might not be installed by default on some linux distributions. It has to be installed if the `wsrep_sst_method` is set to `rsync` (default). Future MariaDB Galera Cluster releases will address this by adding a dependency on lsof.

## Bug Fixes

This release contains fixes for bugs, compiler errors/warnings and improvements\
in existing scripts.

A list of all the bugs fixed can be found in the [changelog](../mariadb-galera-55-changelogs/mariadb-galera-cluster-5537-changelog.md).

* Fixes for the following security vulnerabilities:
  * [CVE-2014-2436](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-2436)
  * [CVE-2014-2440](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-2440)
  * [CVE-2014-2430](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-2430)
  * [CVE-2014-2431](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-2431)
  * [CVE-2019-2481](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-2481)

Thanks, and enjoy MariaDB Galera Cluster!

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
