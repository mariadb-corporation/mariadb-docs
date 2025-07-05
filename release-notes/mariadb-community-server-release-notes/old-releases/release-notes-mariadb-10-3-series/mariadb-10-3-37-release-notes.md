# MariaDB 10.3.37 Release Notes

The most recent release of [MariaDB 10.3](what-is-mariadb-103.md) is:[**MariaDB 10.3.39**](mariadb-10-3-39-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.3.39/)

[Download 10.3.37](https://downloads.mariadb.org/mariadb/10.3.37/)[Release Notes](mariadb-10-3-37-release-notes.md)[Changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10-3-37-changelog.md)[Overview of 10.3](what-is-mariadb-103.md)

**Release date:** 7 Nov 2022

[MariaDB 10.3](what-is-mariadb-103.md) is a previous stable series of MariaDB, maintained until May 2023, and an evolution of[MariaDB 10.2](../release-notes-mariadb-10-2-series/what-is-mariadb-102.md) with several entirely new features not found anywhere else and\
with backported and reimplemented features from MySQL.

[MariaDB 10.3.37](mariadb-10-3-37-release-notes.md) is a [_**Stable (GA)**_](../../../mariadb-release-criteria.md) release.

**For an overview of MariaDB Server 10.3 see the** [**What is MariaDB 10.3?**](what-is-mariadb-103.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Items

### SSL

* The server no longer tolerates incorrectly configured SSL ([MDEV-29811](https://jira.mariadb.org/browse/MDEV-29811)). If you have enabled SSL in `my.cnf` but have not configured it properly (for example, a certificate file is missing), MariaDB used to silently disable SSL, leaving you under impression that everything was fine and connections were secure. Since this release, MariaDB will fail to start if SSL is enabled, but cannot be switched on.

### Backup

* [mariadb-backup --compress](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariadb-backup/mariadb-backup-options#-compress) hangs ([MDEV-29043](https://jira.mariadb.org/browse/MDEV-29043))

### InnoDB

* InnoDB unnecessarily extends data files ([MDEV-13013](https://jira.mariadb.org/browse/MDEV-13013))
* Adaptive hash index [MDEV-27700](https://jira.mariadb.org/browse/MDEV-27700), [MDEV-29384](https://jira.mariadb.org/browse/MDEV-29384)
* MVCC and locking [MDEV-29666](https://jira.mariadb.org/browse/MDEV-29666), [MDEV-27927](https://jira.mariadb.org/browse/MDEV-27927)
* Virtual columns [MDEV-29299](https://jira.mariadb.org/browse/MDEV-29299), [MDEV-29753](https://jira.mariadb.org/browse/MDEV-29753)

### JSON

* [JSON\_VALUE()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_value) does not parse NULL properties properly ([MDEV-27151](https://jira.mariadb.org/browse/MDEV-27151))

### Replication

* minor correction in unsafe warning message ([MDEV-28827](https://jira.mariadb.org/browse/MDEV-28827))
* False replication error-stop of [REVOKE PRIVILEGES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/revoke) from a non-existing user on primary ([MDEV-28530](https://jira.mariadb.org/browse/MDEV-28530)) in combination with a filtering replica is corrected
* [SET DEFAULT ROLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/set-default-role) replication is mended on a replica that filters system tables ([MDEV-28294](https://jira.mariadb.org/browse/MDEV-28294))

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

When upgrading from [MariaDB 10.3.8](mariadb-1038-release-notes.md) or earlier to [MariaDB 10.3.9](mariadb-1039-release-notes.md) or higher,\
running [mysql\_upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade) is **required** due to changes introduced in[MDEV-14637](https://jira.mariadb.org/browse/MDEV-14637).

## Changelog

For a complete list of changes made in [MariaDB 10.3.37](mariadb-10-3-37-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-10-3-series/mariadb-10-3-37-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.3.37](mariadb-10-3-37-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-9-4-10-8-6-10-7-7-10-6-11-10-5-18-10-4-27-and-10-3-37-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
