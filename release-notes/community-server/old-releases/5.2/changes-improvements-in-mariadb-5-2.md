# MariaDB 5.2 Changes & Improvements

[MariaDB 5.2](changes-improvements-in-mariadb-5-2.md) is no longer maintained. Please use a [more recent release](../../../latest-releases.md).

[Download MariaDB 5.2](https://downloads.mariadb.org/mariadb/5.2)

| Date        | Release                     | Status            | Release Notes              | Changelog                                                                                                                                                                                               |
| ----------- | --------------------------- | ----------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 30 Jan 2013 | [MariaDB 5.2.14](5.2.14.md) | Stable (GA)       | [Release Notes](5.2.14.md) | [Changelog](../../changelogs/changelogs-mariadb-52-series/mariadb-5214-changelog.md)                                                                                                                    |
| 29 Nov 2012 | [MariaDB 5.2.13](5.2.13.md) | Stable (GA)       | [Release Notes](5.2.13.md) | [Changelog](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/changelogs/changelogs-mariadb-52-series/mariadb-5213-changelog)                                               |
| 6 Apr 2012  | [MariaDB 5.2.12](5.2.12.md) | Stable (GA)       | [Release Notes](5.2.12.md) | [Changelog](../../changelogs/changelogs-mariadb-52-series/mariadb-5212-changelog.md)                                                                                                                    |
| 2 Apr 2012  | [MariaDB 5.2.11](5.2.11.md) | Stable (GA)       | [Release Notes](5.2.11.md) | [Changelog](../../changelogs/changelogs-mariadb-52-series/mariadb-5211-changelog.md)                                                                                                                    |
| 5 Dec 2011  | [MariaDB 5.2.10](5.2.10.md) | Stable (GA)       | [Release Notes](5.2.10.md) | [Changelog](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/changelogs/changelogs-mariadb-52-series/mariadb-5210-changelog)                                               |
| 22 Sep 2011 | [MariaDB 5.2.9](5.2.9.md)   | Stable (GA)       | [Release Notes](5.2.9.md)  | [Changelog](../../changelogs/changelogs-mariadb-52-series/mariadb-529-changelog.md)                                                                                                                     |
| 18 Aug 2011 | [MariaDB 5.2.8](5.2.8.md)   | Stable (GA)       | [Release Notes](5.2.8.md)  | [Changelog](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-2-series/broken-reference/README.md) |
| 14 Jun 2011 | [MariaDB 5.2.7](5.2.7.md)   | Stable (GA)       | [Release Notes](5.2.7.md)  | [Changelog](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/changelogs/changelogs-mariadb-52-series/mariadb-527-changelog)                                                |
| 12 May 2011 | [MariaDB 5.2.6](5.2.6.md)   | Stable (GA)       | [Release Notes](5.2.6.md)  | [Changelog](../../changelogs/changelogs-mariadb-52-series/mariadb-526-changelog.md)                                                                                                                     |
| 3 Mar 2011  | [MariaDB 5.2.5](5.2.5.md)   | Stable (GA)       | [Release Notes](5.2.5.md)  | [Changelog](../../changelogs/changelogs-mariadb-52-series/mariadb-525-changelog.md)                                                                                                                     |
| 6 Dec 2010  | [MariaDB 5.2.4](5.2.4.md)   | Stable (GA)       | [Release Notes](5.2.4.md)  | [Changelog](../../changelogs/changelogs-mariadb-52-series/mariadb-524-changelog.md)                                                                                                                     |
| 10 Nov 2010 | [MariaDB 5.2.3](5.2.3.md)   | Stable (GA)       | [Release Notes](5.2.3.md)  | [Changelog](../../changelogs/changelogs-mariadb-52-series/mariadb-523-changelog.md)                                                                                                                     |
| 28 Sep 2010 | [MariaDB 5.2.2](5.2.2.md)   | Release Candidate | [Release Notes](5.2.2.md)  | [Changelog](../../changelogs/changelogs-mariadb-52-series/mariadb-522-changelog.md)                                                                                                                     |
| 18 Jun 2010 | [MariaDB 5.2.1](5.2.1.md)   | Beta              | [Release Notes](5.2.1.md)  | [Changelog](../../changelogs/changelogs-mariadb-52-series/mariadb-521-changelog.md)                                                                                                                     |
| 10 Apr 2010 | [MariaDB 5.2.0](5.2.0.md)   | Beta              | [Release Notes](5.2.0.md)  | [Changelog](../../changelogs/changelogs-mariadb-52-series/mariadb-520-changelog.md)                                                                                                                     |

[MariaDB 5.2](changes-improvements-in-mariadb-5-2.md) contains features that didn't have time to go into [MariaDB\
5.1](../5.1/changes-improvements-in-mariadb-5-1.md). For all practical purposes it's a drop in replacement for [MariaDB 5.1](../5.1/changes-improvements-in-mariadb-5-1.md) (and thus MySQL 5.1).

[MariaDB 5.2](changes-improvements-in-mariadb-5-2.md) is based on [MariaDB 5.1](../5.1/changes-improvements-in-mariadb-5-1.md) and thus MySQL 5.1.

The new features in 5.2 are quite isolated and as most have been in use by\
members in the MySQL community for a long time. Current versions of [MariaDB 5.2](changes-improvements-in-mariadb-5-2.md) are [stable](../../about/release-criteria.md) and can be downloaded from [downloads.askmonty.org](https://downloads.askmonty.org).

### New storage engines

* [OQGRAPH](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/oqgraph-storage-engine)
  * Allows you to handle hierarchies (tree structures) and complex graphs (nodes\
    having many connections in several directions)
* [SphinxSE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/sphinx-storage-engine): Text search within MariaDB.
  * A built-in Sphinx client which allows MariaDB to talk to searchd, run search\
    queries, and obtain search results.

### New features

* [Virtual columns](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/generated-columns)
  * Columns that are an expression and are calculated on retrieval.
* [Extended User Statistics](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/user-statistics)
  * Client, User, Index and Table statistics.
* [Segmented MyISAM key cache](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/segmented-key-cache)
  * The key cache's global mutex is split into several mutex which gives a\
    notable speed improvement under multi user load. We have registered up to [250% more performance](/broken/spaces/WCInJQ9cmGjq1lsTG91E/pages/ySaANiCpRqROWwoll9yo) thanks to this.
* [Pluggable Authentication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/pluggable-authentication-overview)
  * Authentication is done via an extensible plugin, which makes it easy to add\
    any kind of authentication to MariaDB.
* [Storage-engine-specific CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/product-development/plugin-development/storage-engines-storage-engine-development/engine-defined-new-tablefieldindex-attributes)
  * Allows one to specify additional attributes per field, index or table to the\
    storage engine.
* [Enhancements to INFORMATION SCHEMA.PLUGINS table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/plugins-table-information-schema)
  * We expose more information about the plugins, like maturity levels.
* [Group commit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria/aria-group-commit) for the [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria) engine.
  * Speeds up multi user inserts.

### Other things

We have also done several smaller speed improvements, bug fixes and code\
cleanups.

### Security Vulnerabilities Fixed in [MariaDB 5.2](changes-improvements-in-mariadb-5-2.md)

For a complete list of security vulnerabilities (CVEs) fixed across all\
versions of MariaDB, see the [Security Vulnerabilities Fixed in MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/cve)\
page.

* [CVE-2013-1531](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-1531): [MariaDB 5.2.14](5.2.14.md)[CVE-2013-0389](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0389): [MariaDB 5.2.14](5.2.14.md)[CVE-2013-0385](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0385): [MariaDB 5.2.14](5.2.14.md)[CVE-2013-0384](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0384): [MariaDB 5.2.14](5.2.14.md)[CVE-2013-0383](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0383): [MariaDB 5.2.14](5.2.14.md)[CVE-2013-0375](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0375): [MariaDB 5.2.14](5.2.14.md)[CVE-2012-5627](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-5627): [MariaDB 5.2.14](5.2.14.md) \[[2](../../changelogs/changelogs-mariadb-52-series/mariadb-5214-changelog.md)][CVE-2012-5615](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-5615): [MariaDB 5.2.14](5.2.14.md) \[[2](../../changelogs/changelogs-mariadb-52-series/mariadb-5214-changelog.md)][CVE-2012-5612](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-5612): [MariaDB 5.2.14](5.2.14.md)[CVE-2012-5611](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-5611): [MariaDB 5.2.14](5.2.14.md), [MariaDB 5.2.13](5.2.13.md)[CVE-2012-4414](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-4414): [MariaDB 5.2.13](5.2.13.md)][CVE-2012-1705](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-1705): [MariaDB 5.2.14](5.2.14.md)[CVE-2012-1702](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-1702): [MariaDB 5.2.14](5.2.14.md)[CVE-2012-0574](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0574): [MariaDB 5.2.14](5.2.14.md)[CVE-2012-0572](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0572): [MariaDB 5.2.14](5.2.14.md)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
