# MariaDB 10.9.4 Release Notes

The most recent release of [MariaDB 10.9](what-is-mariadb-109.md) is:[**MariaDB 10.9.8**](mariadb-10-9-8-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.9.8/)

[Download 10.9.4](https://downloads.mariadb.org/mariadb/10.9.4/)[Release Notes](mariadb-10-9-4-release-notes.md)[Changelog](../../changelogs/changelogs-mariadb-109-series/mariadb-10-9-4-changelog.md)[Overview of 10.9](what-is-mariadb-109.md)

**Release date:** 7 Nov 2022

[MariaDB 10.9](what-is-mariadb-109.md) is the current short-term maintenance stable series of MariaDB, maintained until August 2023. It is an evolution of [MariaDB 10.8](../release-notes-mariadb-10-8-series/what-is-mariadb-108.md) with several entirely new features.

[MariaDB 10.9.4](mariadb-10-9-4-release-notes.md) is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For an overview of** [**MariaDB 10.9**](what-is-mariadb-109.md) **see the**[**What is MariaDB 10.9?**](what-is-mariadb-109.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Items

### SSL

* The server no longer tolerates incorrectly configured SSL ([MDEV-29811](https://jira.mariadb.org/browse/MDEV-29811)). If you have enabled SSL in `my.cnf` but have not configured it properly (for example, a certificate file is missing), MariaDB used to silently disable SSL, leaving you under impression that everything was fine and connections were secure. Since this release, MariaDB will fail to start if SSL is enabled, but cannot be switched on.

### Backup

* Assertion on info.page\_size failed in xb\_delta\_open\_matching\_space ([MDEV-18589](https://jira.mariadb.org/browse/MDEV-18589))
* [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariadb-backup) locks database for minutes ([MDEV-28772](https://jira.mariadb.org/browse/MDEV-28772))

### InnoDB

* Adaptive hash index [MDEV-27700](https://jira.mariadb.org/browse/MDEV-27700), [MDEV-29384](https://jira.mariadb.org/browse/MDEV-29384)
* MVCC and locking ([MDEV-29666](https://jira.mariadb.org/browse/MDEV-29666), [MDEV-27927](https://jira.mariadb.org/browse/MDEV-27927), [MDEV-28709](https://jira.mariadb.org/browse/MDEV-28709), [MDEV-29635](https://jira.mariadb.org/browse/MDEV-29635))
* Virtual columns ([MDEV-29299](https://jira.mariadb.org/browse/MDEV-29299), [MDEV-29753](https://jira.mariadb.org/browse/MDEV-29753))
* InnoDB crash recovery fixes ([MDEV-29559](https://jira.mariadb.org/browse/MDEV-29559))
* Race condition between KILL and transaction commit ([MDEV-29368](https://jira.mariadb.org/browse/MDEV-29368))
* Implement [CHECK TABLE…EXTENDED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/check-table) for InnoDB ([MDEV-24402](https://jira.mariadb.org/browse/MDEV-24402))
* [InnoDB persistent statistics](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics) fail to update after bulk insert ([MDEV-28327](https://jira.mariadb.org/browse/MDEV-28327))
* InnoDB bulk insert bug fixes ([MDEV-29570](https://jira.mariadb.org/browse/MDEV-29570), [MDEV-29761](https://jira.mariadb.org/browse/MDEV-29761))

### Galera

* [Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera-cluster/README.md) updated to 26.4.13
* Galera server crashes after 10.3 > 10.4 upgrade ([MDEV-29375](https://jira.mariadb.org/browse/MDEV-29375))
* [wsrep\_incoming\_addresses](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables#wsrep_incoming_addresses) status variable prints 0 as port number if the port is not mentioned in [wsrep\_node\_incoming\_address](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_node_incoming_address) system variable ([MDEV-28868](https://jira.mariadb.org/browse/MDEV-28868))

### Replication

* XA COMMIT is not binlogged when the [XA transaction](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/xa-transactions) has not updated any transaction engine ([MDEV-25616](https://jira.mariadb.org/browse/MDEV-25616))
* Concurrent [CREATE TRIGGER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/triggers-events/triggers/create-trigger) statements made to binlog without any mixup ([MDEV-25606](https://jira.mariadb.org/browse/MDEV-25606))

### Repositories

* Beginning with the next release (Q1 2023), our Yum, DNF, and Zypper repositories for Red Hat, Fedora, and SUSE will be migrated to being signed with a new [GPG key](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/gpg). The key we are migrating to is the same one we already use for our Debian and Ubuntu Repositories.
  * The short Key ID is: `0xC74CD1D8`
  * The long Key ID is: `0xF1656F24C74CD1D8`
  * The full fingerprint of the key is: `177F 4010 FE56 CA33 3630 0305 F165 6F24 C74C D1D8`
  * The key can be imported now in preparation for this change using the following command:

```bash
sudo rpm --import https://supplychain.mariadb.com/MariaDB-Server-GPG-KEY
```

### Docker Official Image

The following changes have been made to the `docker.io/library/mariadb` container image.

* The number of gpg packages has been removed, leaving enough to `apt-get update`, but `dirmngr` that would fetch keys has been removed. (inspired by [issue #469](https://github.com/MariaDB/mariadb-docker/issues/469))
* The environment variable `LANG=C.UTF-8` has been added for those that exec into containers and copy paste UTF8 characters (fixes [issue #468](https://github.com/MariaDB/mariadb-docker/issues/468)).
* Adds OCI labels to image (fixes [issue 436](https://github.com/MariaDB/mariadb-docker/issues/436) and [users need for version](https://github.com/MariaDB/mariadb-docker/commit/942cd5347b86c84cc4d493147b17c3e3b93fbee3))
* MariaDB config: skip-host-cache and skip-name-resolve moved to `/etc/mysql/mariadb.conf.d/05-skipcache.cnf`

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-`-``#`

## Changelog

For a complete list of changes made in [MariaDB 10.9.4](mariadb-10-9-4-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-109-series/mariadb-10-9-4-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.9.4](mariadb-10-9-4-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-9-4-10-8-6-10-7-7-10-6-11-10-5-18-10-4-27-and-10-3-37-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
