# Release Notes for MariaDB Enterprise Server 10.4.34-24

MariaDB Enterprise Server 10.4.34-24 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.4. This release includes a variety of fixes.

MariaDB Enterprise Server 10.4.34-24 was released on 2024-06-11.

## Notable Changes

* Galera has been updated to `26.4.18`
  * The GCS protocol version has been changed, preventing a downgrade of individual nodes of a MariaDB Enterprise Cluster

## Issues Fixed

### Can result in data loss

* With `--gtid-ignore-duplicate` set a transaction can be double-applied from another replication source if at applying the transaction from the initial source required retrying in parallel execution. ([MDEV-33475](https://jira.mariadb.org/browse/MDEV-33475))
* Backups of server with `innodb_encrypt_tables=1` can become corrupted in `mariadb-backup --prepare` ([MDEV-33334](https://jira.mariadb.org/browse/MDEV-33334))
* Galera-replicated events can in some cases contain the wrong time when versioning is used ([MDEV-18590](https://jira.mariadb.org/browse/MDEV-18590))

### Can result in hang or crash

* Using current MariaDB Enterprise Backup against an older server can result in a crash, as the system variable `@@aria_log_dir_path` does not exist ([MDEV-31251](https://jira.mariadb.org/browse/MDEV-31251))
* For encrypted table spaces an ALTER operation can hang when an encryption thread works on the same tablespace ([MDEV-33770](https://jira.mariadb.org/browse/MDEV-33770))
* EXPLAIN statement that uses a subquery which has a query plan that A) will examine less than `@@expensive_subquery_limit` rows and B) will use join buffer could cause a crash. ([MDEV-21102](https://jira.mariadb.org/browse/MDEV-21102))
* MariaDB Enterprise Backup fails with the following error message if the prepare step of the backup encounters a data directory which happens to store wsrep xid position in TRX SYS page: ([MDEV-33540](https://jira.mariadb.org/browse/MDEV-33540))

```
InnoDB: Crash recovery is broken due to insufficient innodb_log_file_size
```

### Can result in unexpected behavior

* Spider/ODBC passed double quotes for names, in ANSI style (MENT-958)
* Default charset doesn't work with PHP MySQLi extension ([MDEV-32975](https://jira.mariadb.org/browse/MDEV-32975))
* Spider returns parsing failure on valid left join select by translating the on expression to () ([MDEV-33679](https://jira.mariadb.org/browse/MDEV-33679))
* Original IP not shown in network related error messages when `proxy_protocol` is in use ([MDEV-33506](https://jira.mariadb.org/browse/MDEV-33506))
* Incorrect DEFAULT expression evaluated in UPDATE ([MDEV-33790](https://jira.mariadb.org/browse/MDEV-33790))

### Related to performance

* Table is getting rebuild with `ALTER TABLE ADD COLUMN` although it should be an instant operation not requiring a rebuild ([MDEV-33214](https://jira.mariadb.org/browse/MDEV-33214))

## Changelog

* For the complete list of changes in this release, see the [changelog](changelog-for-mariadb-enterprise-server-10-4-34-24.md).

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.4.34-24 is provided for:

* CentOS 7 (x86\_64)
* Debian 10 (x86\_64)
* Microsoft Windows (x86\_64) (MariaDB Enterprise Cluster excluded)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)

Some of the components of MariaDB Enterprise Server are supported on a subset of platforms. See [MariaDB Engineering Policies](https://mariadb.com/engineering-policies) for details.

## Installation Instructions

* [MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server)
* [Enterprise Cluster Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[10](broken-reference)[.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Primary/Replica Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/primary-replica)
* [Enterprise Spider Sharded Topology with MariaDB Enterprise Server 10.4](broken-reference)
* [Enterprise Spider Federated Topology with MariaDB Enterprise Server 10.4](broken-reference)

## Upgrade Instructions

* [Upgrade to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-4-to-mariadb-10-5)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-between-major-mariadb-versions)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
