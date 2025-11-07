# MariaDB 10.7 Changes & Improvements

[MariaDB 10.7](what-is-mariadb-107.md) is no longer maintained. Please use a [more recent release](../../../latest-releases.md).

The most recent release of [MariaDB 10.7](what-is-mariadb-107.md) is:[**MariaDB 10.7.8**](mariadb-10-7-8-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.7.8/)

[MariaDB 10.7](what-is-mariadb-107.md) is a previous short-term maintenance stable series. The first stable release was in February 2022, and it was maintained for one year.

## Upgrading

* See [Upgrading Between Major MariaDB Versions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions) and [Upgrading from MariaDB 10.6 to MariaDB 10.7](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-6-to-mariadb-10-7).

## New Features & Improvements

### UUID

* New [UUID data type](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/uuid-data-type) ([MDEV-4958](https://jira.mariadb.org/browse/MDEV-4958))

### JSON

* [JSON\_EQUALS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_equals) function to check for equality between JSON objects ([MDEV-23143](https://jira.mariadb.org/browse/MDEV-23143)).
* [JSON\_NORMALIZE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_normalize) function, which recursively sorts keys and removes spaces ([MDEV-16375](https://jira.mariadb.org/browse/MDEV-16375))

### Natural Sort

* [NATURAL\_SORT\_KEY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/natural_sort_key) function ([MDEV-4742](https://jira.mariadb.org/browse/MDEV-4742)).

### Optimization

* Improve simple multibyte collation performance on the ASCII range ([MDEV-26572](https://jira.mariadb.org/browse/MDEV-26572)).

### Provider Plugins

* Five provider plugins (bzip2, lzma, lz4, lzo, snappy) provide [compression capabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins) to the server and storage engines ([MDEV-12933](https://jira.mariadb.org/browse/MDEV-12933), [blog post](https://mariadb.org/10-7-preview-feature-provider-plugins)).

### SFORMAT

* [SFORMAT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/sformat) function for arbitrary text formatting ([MDEV-25015](https://jira.mariadb.org/browse/MDEV-25015))

### mariadb-dump

* Add option to [dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqldump) [system versioned table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/system-versioned-tables) as of specified timestamp ([MDEV-16355](https://jira.mariadb.org/browse/MDEV-16355)).

### Convert Partitions

* ALTER TABLE ... CONVERT PARTITION .. TO TABLE ([MDEV-22166](https://jira.mariadb.org/browse/MDEV-22166)), and
* ALTER TABLE ... CONVERT TABLE ... TO PARTITION ... ([MDEV-22165](https://jira.mariadb.org/browse/MDEV-22165)) as an easy way to convert tables to partitions and back in one command, instead of a sequence of CREATE/EXCHANGE/DROP

### Password Reuse

* password\_reuse\_check plugin is a new password validation plugin that prevents the new password from being the same as the one being used during the configurable retention period. ([MDEV-9245](https://jira.mariadb.org/browse/MDEV-9245))

### Replication

* Multi-source replication supports MySQL-style CHANNEL syntax ([MDEV-26307](https://jira.mariadb.org/browse/MDEV-26307))

### InnoDB Bulk Insert

* In bulk insert, pre-sort and build indexes one page at a time ([MDEV-24621](https://jira.mariadb.org/browse/MDEV-24621))

### Diagnostics

* [GET DIAGNOSTICS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-diagnostics/get-diagnostics) supports a new condition property name `ROW_NUMBER`. In multi-row inserts it allows one to retrieve a number of a row that has caused the error ([MDEV-10075](https://jira.mariadb.org/browse/MDEV-10075), [MDEV-26611](https://jira.mariadb.org/browse/MDEV-26611))

### Variables

* For a list of all new variables, see [System Variables Added in MariaDB 10.7](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-and-status-variables-added-by-major-unmaintained-release) and [Status Variables Added in MariaDB 10.7](what-is-mariadb-107.md).

The following deprecated variables have been removed :

* [wsrep\_replicate\_myisam](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_replicate_myisam) ([MDEV-24947](https://jira.mariadb.org/browse/MDEV-24947))
* [wsrep\_strict\_ddl](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_strict_ddl) ([MDEV-24843](https://jira.mariadb.org/browse/MDEV-24843))

## Security Vulnerabilities Fixed in [MariaDB 10.7](what-is-mariadb-107.md)

For a complete list of security vulnerabilities (CVEs) fixed across all\
versions of MariaDB, see the [Security Vulnerabilities Fixed in MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security)\
page.

* [CVE-2023-5157](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-5157): [MariaDB 10.7.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1075-release-notes)
* [CVE-2022-38791](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-38791): [MariaDB 10.7.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1075-release-notes)
* [CVE-2022-32091](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32091): [MariaDB 10.7.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1075-release-notes)
* [CVE-2022-32089](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32089): [MariaDB 10.7.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1075-release-notes)
* [CVE-2022-32088](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32088): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-32087](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32087): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-32086](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32086): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-32085](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32085): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-32084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32084): [MariaDB 10.7.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1075-release-notes)
* [CVE-2022-32083](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32083): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-32082](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32082): [MariaDB 10.7.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1075-release-notes)
* [CVE-2022-32081](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-32081): [MariaDB 10.7.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1075-release-notes)
* [CVE-2022-27458](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27458): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-27457](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27457): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-27456](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27456): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-27455](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27455): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-27452](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27452): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-27451](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27451): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-27449](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27449): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-27448](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27448): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-27447](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27447): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-27446](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27446): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-27445](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27445): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-27444](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27444): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-27387](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27387): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-27386](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27386): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-27384](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27384): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-27383](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27383): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-27382](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27382): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-27381](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27381): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-27380](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27380): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-27379](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27379): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-27378](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27378): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-27377](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27377): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-27376](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-27376): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2022-24052](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24052): [MariaDB 10.7.2](mariadb-1072-release-notes.md)
* [CVE-2022-24051](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24051): [MariaDB 10.7.2](mariadb-1072-release-notes.md)
* [CVE-2022-24050](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24050): [MariaDB 10.7.2](mariadb-1072-release-notes.md)
* [CVE-2022-24048](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-24048): [MariaDB 10.7.2](mariadb-1072-release-notes.md)
* [CVE-2022-21595](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-21595): [MariaDB 10.7.2](mariadb-1072-release-notes.md)
* [CVE-2022-0778](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-0778): [MariaDB 10.7.2](mariadb-1072-release-notes.md)
* [CVE-2021-46669](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46669): [MariaDB 10.7.4](mariadb-1074-release-notes.md)
* [CVE-2021-46668](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46668): [MariaDB 10.7.3](mariadb-1073-release-notes.md)
* [CVE-2021-46665](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46665): [MariaDB 10.7.3](mariadb-1073-release-notes.md)
* [CVE-2021-46664](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46664): [MariaDB 10.7.3](mariadb-1073-release-notes.md)
* [CVE-2021-46663](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46663): [MariaDB 10.7.3](mariadb-1073-release-notes.md)
* [CVE-2021-46661](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46661): [MariaDB 10.7.3](mariadb-1073-release-notes.md)
* [CVE-2021-46659](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-46659): [MariaDB 10.7.2](mariadb-1072-release-notes.md)
* [CVE-2018-25032](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-25032): [MariaDB 10.7.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1075-release-notes)

## List of All [MariaDB 10.7](what-is-mariadb-107.md) Releases

| Date        | Release                                                                                                                                                                                                       | Status      | Release Notes                                                                                                                                                                                                | Changelog                                    |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- |
| 6 Feb 2023  | [MariaDB 10.7.8](mariadb-10-7-8-release-notes.md)                                                                                                                                                             | Stable (GA) | [Release Notes](mariadb-10-7-8-release-notes.md)                                                                                                                                                             | [Changelog](../../changelogs/10.7/10.7.8.md) |
| 7 Nov 2022  | [MariaDB 10.7.7](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-10-7-7-release-notes)                                   | Stable (GA) | [Release Notes](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series)                                                                | [Changelog](../../changelogs/10.7/10.7.7.md) |
| 19 Sep 2022 | [MariaDB 10.7.6](mariadb-1076-release-notes.md)                                                                                                                                                               | Stable (GA) | [Release Notes](mariadb-1076-release-notes.md)                                                                                                                                                               | [Changelog](../../changelogs/10.7/10.7.6.md) |
| 15 Aug 2022 | [MariaDB 10.7.5](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/mariadb-1075-release-notes)                                     | Stable (GA) | [Release Notes](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/broken-reference/README.md) | [Changelog](../../changelogs/10.7/10.7.5.md) |
| 20 May 2022 | [MariaDB 10.7.4](mariadb-1074-release-notes.md)                                                                                                                                                               | Stable (GA) | [Release Notes](mariadb-1074-release-notes.md)                                                                                                                                                               | [Changelog](../../changelogs/10.7/10.7.4.md) |
| 12 Feb 2022 | [MariaDB 10.7.3](mariadb-1073-release-notes.md)                                                                                                                                                               | Stable (GA) | [Release Notes](mariadb-1073-release-notes.md)                                                                                                                                                               | [Changelog](../../changelogs/10.7/10.7.3.md) |
| 9 Feb 2022  | [MariaDB 10.7.2](mariadb-1072-release-notes.md)                                                                                                                                                               | Stable (GA) | [Release Notes](mariadb-1072-release-notes.md)                                                                                                                                                               | [Changelog](../../changelogs/10.7/10.7.2.md) |
| 8 Nov 2021  | [MariaDB 10.7.1](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/broken-reference/README.md) | RC          | [Release Notes](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-7-series/broken-reference/README.md) | [Changelog](../../changelogs/10.7/10.7.1.md) |
| 17 Sep 2021 | [MariaDB 10.7.0](mariadb-1070-release-notes.md)                                                                                                                                                               | Alpha       | [Release Notes](mariadb-1070-release-notes.md)                                                                                                                                                               |                                              |

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
