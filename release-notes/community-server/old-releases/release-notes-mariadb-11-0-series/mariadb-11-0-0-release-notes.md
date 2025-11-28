# MariaDB 11.0.0 Release Notes

The most recent release of [MariaDB 11.0](what-is-mariadb-110.md) is:[**MariaDB 11.0.6**](mariadb-11-0-6-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/11.0.6/)

[Download](https://downloads.mariadb.org/mariadb/11.0.0) | [Release Notes](mariadb-11-0-0-release-notes.md) | [Changelog](../../changelogs/11.0/) | [Overview of 11.0](what-is-mariadb-110.md)

**Release date:** 27 Dec 2022

**Do not use&#x20;**_**alpha**_**&#x20;releases in production!**

[MariaDB 11.0](what-is-mariadb-110.md) is a current development series of MariaDB, and will be maintained for one year after its Generally Available release. It is an evolution of [MariaDB 10.11](../../10.11/what-is-mariadb-1011.md) with several entirely new features.

[MariaDB 11.0.0](mariadb-11-0-0-release-notes.md) is a single preview release. Features are to be considered preview, and none are guaranteed to make it into [MariaDB 11.0](what-is-mariadb-110.md).

The preview is available as a container **quay.io/mariadb-foundation/mariadb-devel:10.11-preview**.

**For an overview of** [**MariaDB 11.0**](what-is-mariadb-110.md) **see the**[**What is MariaDB 11.0?**](what-is-mariadb-110.md) **page.**

Thanks, and enjoy MariaDB!

## New optimizer cost model

This is the main change that practically defines this release. Read about new optimizer cost model on its own page

## Galera

* [MDEV-22570](https://jira.mariadb.org/browse/MDEV-22570) Implement wsrep\_provider\_options as plugin
* [MDEV-29281](https://jira.mariadb.org/browse/MDEV-29281) Add details about node eviction status to the JSON file with Galera node status

## Removing/Deprecating old code

* [MDEV-29694](https://jira.mariadb.org/browse/MDEV-29694) Remove the [InnoDB change buffer](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-change-buffering)
* [MDEV-30136](https://jira.mariadb.org/browse/MDEV-30136) Deprecate [innodb\_flush\_method](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_flush_method)
* [MDEV-29983](https://jira.mariadb.org/browse/MDEV-29983) Deprecate [innodb\_file\_per\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_file_per_table)
* [MDEV-30128](https://jira.mariadb.org/browse/MDEV-30128) remove support for 5.1- replication events
* [MDEV-29582](https://jira.mariadb.org/browse/MDEV-29582) deprecate mysql\* names
* [MDEV-29227](https://jira.mariadb.org/browse/MDEV-29227) deprecate [explicit\_defaults\_for\_timestamp=0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#explicit_defaults_for_timestamp)
* [MDEV-28910](https://jira.mariadb.org/browse/MDEV-28910) remove the 5.5.5- version hack
* [MDEV-29668](https://jira.mariadb.org/browse/MDEV-29668) SUPER no longer allows actions that have fine-grained dedicated privileges

## Other changes

* [MDEV-30203](https://jira.mariadb.org/browse/MDEV-30203) Move mysql compatibility symlinks to different package
* [MDEV-30153](https://jira.mariadb.org/browse/MDEV-30153) ad hoc client versions are confusing
* [MDEV-29986](https://jira.mariadb.org/browse/MDEV-29986) Set [innodb\_undo\_tablespaces=3](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_undo_tablespaces) by default

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
