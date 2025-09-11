# MariaDB Galera Cluster 10.0.10 Release Notes

The most recent [MariaDB Galera Cluster 10.0](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) release is:[**MariaDB Galera Cluster 10.0.38**](mariadb-galera-cluster-10038-release-notes.md) [Download Now](https://downloads.mariadb.org/mariadb-galera/10.0.38)

[Download](https://downloads.mariadb.org/mariadb-galera/10.0.10) |**Release Notes** |[Changelog](../mariadb-galera-100-changelogs/mariadb-galera-cluster-10010-changelog.md) |[Overview of MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/what-is-mariadb-galera-cluster/README.md)

**Release date:** 22 Apr 2014

This is the 2nd release in the MariaDB Galera Cluster 10.0 series. It is a [_**Beta**_](../../../about/release-criteria.md) release. It is a merge of [MariaDB 10.0.10](../../release-notes-mariadb-10-0-series/mariadb-10010-release-notes.md)\
and [Galera Cluster](https://codership.com/content/using-galera-cluster) with\
additional bug fixes. It is being released now to get it into the hands of any\
who might want to test it. **Do not run Beta releases on production systems!**

Various articles about MariaDB Galera Cluster, including [known limitations](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/mariadb-galera-cluster-known-limitations) and [how to get started](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/galera-management/installation-and-deployment/getting-started-with-mariadb-galera-cluster) are\
available in the [**Galera**](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera/README.md) section of the documentation.

For a list of changes made in MariaDB Galera Cluster 10.0.10, with links to\
detailed information on each push, see the [MariaDB Galera Cluster 10.0.10 Changelog](../mariadb-galera-100-changelogs/mariadb-galera-cluster-10010-changelog.md).

## Updates and fixes in this version

* Codership changes: `lp:codership-mysql/5.5` (till rev `3968`) & `lp:codership-mysql/5.6` (till rev `4065`).
* [Galera library](https://codership.com/content/using-galera-cluster) versions: 25.3.5, 25.2.9
* Supported wsrep interface version: 25

## Notes

* Compatibility: Wsrep providers (Galera libraries) other than version 25.x.xx are not supported.
* New: This release includes a new method for snapshot state transfer, `wsrep_sst_xtrabackup-v2`. This method of state snapshot transfer can be configured using the `--wsrep_sst_method=xtrabackup-v2` option. Its use requires Xtrabackup (>= 2.1.6) and other software packages like socat, nc, and tar.
* Note: Completely uninstall broken/partially installed 10.0.7-galera deb packages prior to installing this version, as they may conflict with 10.0.10-galera packages.

See the [MariaDB 10.0.10 Release Notes](../../release-notes-mariadb-10-0-series/mariadb-10010-release-notes.md) and [Changelog](../../../changelogs/changelogs-mariadb-100-series/mariadb-10010-changelog.md) for more information on the changes in\
MariaDB.

Note: If Galera v2 and v3 are both being used in the cluster, MariaDB with\
Galera v3 must be started with `wsrep_provider_options='socket.checksum=1'`\
in order to make it backward compatible with Galera v2.

Thanks, and enjoy MariaDB Galera Cluster!

Be notified of new MariaDB Server releases automatically by [subscribing](https://lists.mariadb.org/postorius/lists/announce.lists.mariadb.org/) to the MariaDB Foundation community announce 'at' lists.mariadb.org announcement list (this is a low traffic, announce-only list). MariaDB plc customers will be notified for all new releases, security issues and critical bug fixes for all MariaDB plc products thanks to the Notification Services.

MariaDB may already be included in your favorite OS distribution. More\
information can be found on the [Distributions which Include MariaDB](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/distributions-including-mariadb)\
page.

{% include "../../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
