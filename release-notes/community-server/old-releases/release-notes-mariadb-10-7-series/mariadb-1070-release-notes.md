# MariaDB 10.7.0 Release Notes

The most recent release of [MariaDB 10.7](what-is-mariadb-107.md) is:[**MariaDB 10.7.8**](mariadb-10-7-8-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.7.8/)

[Download 10.7.0](https://mariadb.org/download/?tab=mariadb\&release=10.7.0\&product=mariadb) | [Release Notes](mariadb-1070-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-100-series/mariadb-1007-changelog.md) | [Overview of 10.7](what-is-mariadb-107.md)

**Release date:** 17 Sep 2021

**Do not use&#x20;**_**alpha**_**&#x20;releases in production!**

[MariaDB 10.7](what-is-mariadb-107.md) is the current development series of MariaDB. It is an evolution\
of [MariaDB 10.6](../../10.6/what-is-mariadb-106.md) with several entirely new features.

[MariaDB 10.7.0](mariadb-1070-release-notes.md) is not a single release, but is instead a number of feature preview releases based on feature branches. Each should be considered as having a maturity of an [_**Alpha**_](../../about/release-criteria.md) release. Read more about feature preview releases [here](https://mariadb.org/preview-releases/).

Thanks, and enjoy MariaDB!

Remember, these features are in separate _preview packages_. The subsection header text corresponds to the preview package name.

Notable changes of this series of releases include:

## Provider Plugins

* Five provider plugins (bzip2, lzma, lz4, lzo, snappy) provide [compression capabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins) to the server and storage engines ([MDEV-12933](https://jira.mariadb.org/browse/MDEV-12933), [blog post](https://mariadb.org/10-7-preview-feature-provider-plugins)).

## SFORMAT

* [SFORMAT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/sformat) function for arbitrary text formatting ([MDEV-25015](https://jira.mariadb.org/browse/MDEV-25015), [blog post](https://mariadb.org/10-7-preview-feature-sformat/)).

## UUID

* New [UUID data type](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/uuid-data-type) ([MDEV-4958](https://jira.mariadb.org/browse/MDEV-4958), [blog post](https://mariadb.org/10-7-preview-feature-uuid-data-type/))

## Natural Sort

* [NATURAL\_SORT\_KEY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/natural_sort_key) function ([MDEV-4742](https://jira.mariadb.org/browse/MDEV-4742), [blog post](https://mariadb.org/10-7-preview-feature-natural-sort/)).

## JSON Histograms

* Histograms in the statistics tables are more precise and stored as JSON, not binary ([MDEV-21130](https://jira.mariadb.org/browse/MDEV-21130), [MDEV-26519](https://jira.mariadb.org/browse/MDEV-26519), [blog post](https://mariadb.org/10-7-preview-feature-json-histograms/)). Note that this feature was not included in [MariaDB 10.7.1](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1071-release-notes).

## Convert Partitions

* ALTER TABLE ... CONVERT PARTITION .. TO TABLE ([MDEV-22166](https://jira.mariadb.org/browse/MDEV-22166), [blog post](https://mariadb.org/10-7-preview-feature-convert-partition/)), and
* ALTER TABLE ... CONVERT TABLE ... TO PARTITION ... ([MDEV-22165](https://jira.mariadb.org/browse/MDEV-22165)) as an easy way to convert tables to partitions and back in one command, instead of a sequence of CREATE/EXCHANGE/DROP
* ALTER TABLE .. ADD PARTITION allows to omit the redundant PARTITION keyword ([MDEV-26471](https://jira.mariadb.org/browse/MDEV-26471))

## Password Reuse

* The [password\_reuse\_check plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/password-reuse-check-plugin) is a new password validation plugin that prevents the new password from being the same as the one being used during the configurable retention period. ([MDEV-9245](https://jira.mariadb.org/browse/MDEV-9245), [blog post](https://mariadb.org/10-7-preview-feature-password-reuse-check-plugin/)).

## InnoDB Bulk Insert

* In bulk insert, pre-sort and build indexes one page at a time ([MDEV-24621](https://jira.mariadb.org/browse/MDEV-24621))

## Misc. Features

* [JSON\_EQUALS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_equals) function to check for equality between JSON objects ([MDEV-23143](https://jira.mariadb.org/browse/MDEV-23143)).
* [JSON\_NORMALIZE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_normalize) function, which recursively sorts keys and removes spaces ([MDEV-16375](https://jira.mariadb.org/browse/MDEV-16375))
* Improve simple multibyte collation performance on the ASCII range ([MDEV-26572](https://jira.mariadb.org/browse/MDEV-26572)).
* Add option to [dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqldump) [system versioned table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/system-versioned-tables) as of specified timestamp ([MDEV-16355](https://jira.mariadb.org/browse/MDEV-16355)).
* Multi-source replication supports MySQL-style CHANNEL syntax ([MDEV-26307](https://jira.mariadb.org/browse/MDEV-26307))
* [GET DIAGNOSTICS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-diagnostics/get-diagnostics) supports a new condition property name `ERROR_INDEX`. In multi-row inserts it allows to retrieve a number of a row that has caused the error ([MDEV-10075](https://jira.mariadb.org/browse/MDEV-10075))
* [wsrep\_replicate\_myisam](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_replicate_myisam) and [wsrep\_strict\_ddl](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_strict_ddl) deprecated system variables were removed ([MDEV-24947](https://jira.mariadb.org/browse/MDEV-24947), [MDEV-24843](https://jira.mariadb.org/browse/MDEV-24843))

**Do not use&#x20;**_**alpha**_**&#x20;releases on production systems!**\
For a complete list of changes made in [MariaDB 10.7.0](mariadb-1070-release-notes.md), with links to detailed\
information on each push, see the [changelog](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1070-changelog/README.md).

**Do not use&#x20;**_**alpha**_**&#x20;releases in production!**

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
