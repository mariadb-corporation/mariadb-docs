# MariaDB 5.1 Changes & Improvements

[MariaDB 5.1](changes-improvements-in-mariadb-5-1.md) is no longer maintained. Please use a [more recent release](../../../latest-releases.md).

[Download MariaDB 5.1](https://downloads.mariadb.org/mariadb/5.1)

| Date        | Release             | Status            | Release Notes               | Changelog                                                                             |
| ----------- | ------------------- | ----------------- | --------------------------- | ------------------------------------------------------------------------------------- |
| 30 Jan 2013 | **MariaDB 5.1.67**  | Stable (GA)       | [Release Notes](5.1.67.md)  | [Changelog](../../changelogs/changelogs-mariadb-51-series/mariadb-5167-changelog.md)  |
| 29 Nov 2012 | **MariaDB 5.1.66**  | Stable (GA)       | [Release Notes](5.1.66.md)  | [Changelog](../../changelogs/changelogs-mariadb-51-series/mariadb-5166-changelog.md)  |
| 6 Apr 2012  | **MariaDB 5.1.62**  | Stable (GA)       | [Release Notes](5.1.62.md)  | [Changelog](../../changelogs/changelogs-mariadb-51-series/mariadb-5162-changelog.md)  |
| 2 Apr 2012  | **MariaDB 5.1.61**  | Stable (GA)       | [Release Notes](5.1.61.md)  | [Changelog](../../changelogs/changelogs-mariadb-51-series/mariadb-5161-changelog.md)  |
| 5 Dec 2011  | **MariaDB 5.1.60**  | Stable (GA)       | [Release Notes](5.1.60.md)  | [Changelog](../../changelogs/changelogs-mariadb-51-series/mariadb-5160-changelog.md)  |
| 1 Mar 2011  | **MariaDB 5.1.55**  | Stable (GA)       | [Release Notes](5.1.55.md)  | [Changelog](../../changelogs/changelogs-mariadb-51-series/mariadb-5155-changelog.md)  |
| 6 Dec 2010  | **MariaDB 5.1.53**  | Stable (GA)       | [Release Notes](5.1.53.md)  | [Changelog](../../changelogs/changelogs-mariadb-51-series/mariadb-5153-changelog.md)  |
| 19 Nov 2010 | **MariaDB 5.1.51**  | Stable (GA)       | [Release Notes](5.1.51.md)  | [Changelog](../../changelogs/changelogs-mariadb-51-series/mariadb-5151-changelog.md)  |
| 9 Sep 2010  | **MariaDB 5.1.50**  | Stable (GA)       | [Release Notes](5.1.50.md)  | [Changelog](../../changelogs/changelogs-mariadb-51-series/mariadb-5150-changelog.md)  |
| 9 Aug 2010  | **MariaDB 5.1.49**  | Stable (GA)       | [Release Notes](5.1.49.md)  | [Changelog](../../changelogs/changelogs-mariadb-51-series/mariadb-5149-changelog.md)  |
| 1 Jun 2010  | **MariaDB 5.1.47**  | Stable (GA)       | [Release Notes](5.1.47.md)  | [Changelog](../../changelogs/changelogs-mariadb-51-series/mariadb-5147-changelog.md)  |
| 10 May 2010 | **MariaDB 5.1.44b** | Stable (GA)       | [Release Notes](5.1.44b.md) | [Changelog](../../changelogs/changelogs-mariadb-51-series/mariadb-5144b-changelog.md) |
| 24 Mar 2010 | **MariaDB 5.1.44**  | Stable (GA)       | [Release Notes](5.1.44.md)  | [Changelog](../../changelogs/changelogs-mariadb-51-series/mariadb-5144-changelog.md)  |
| 1 Feb 2010  | **MariaDB 5.1.42**  | Stable (GA)       | [Release Notes](5.1.42.md)  | [Changelog](../../changelogs/changelogs-mariadb-51-series/mariadb-5142-changelog.md)  |
| 13 Jan 2010 | **MariaDB 5.1.41**  | Release Candidate | [Release Notes](5.1.41.md)  | [Changelog](../../changelogs/changelogs-mariadb-51-series/mariadb-5141-changelog.md)  |
| 15 Nov 2009 | **MariaDB 5.1.39**  | Beta              | [Release Notes](5.1.39.md)  | [Changelog](../../changelogs/changelogs-mariadb-51-series/mariadb-5139-changelog.md)  |
| 29 Oct 2009 | **MariaDB 5.1.38**  | Beta              | [Release Notes](5.1.38.md)  | [Changelog](../../changelogs/changelogs-mariadb-51-series/mariadb-5138-changelog.md)  |

In short, [MariaDB 5.1](changes-improvements-in-mariadb-5-1.md) is a binary drop in replacement of MySQL 5.1, but with performance like MySQL 5.5 (thanks to XtraDB), fewer bugs, and more features. Thanks to the extended and improved [mysql\_upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade) program it's also easier to upgrade from MySQL 5.0 to MariaDB 5.1 than to MySQL 5.1.

MariaDB 5.1 is based on MySQL 5.1. We do a merge once a month with MySQL5.1 to ensure all MySQL bug fixes get into MariaDB.

See also:

* [MariaDB versus MySQL - Compatibility](../../about/compatibility-and-differences/mariadb-vs-mysql-compatibility.md)

### New storage engines:

* [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria): A crash-safe storage engine based on MyISAM.
* [XtraDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb): Drop-in replacement for InnoDB based on the InnoDB plugin.
* [pbxt](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/obsolete-replication-information/mariadb-52-replication-feature-preview#pbxt-consistent-commit-ordering)): A transactional storage engine with a lot of nice features.
* [FederatedX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/federatedx-storage-engine): Drop-in replacement for Federated.

### Speed improvements

* [CHECKSUM TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/checksum-table) is faster.
* We have eliminated/improved some not needed character set conversions.\
  Overall speed improvements is 1-5 % (according to sql-bench) but can be\
  higher for big result sets with all characters between 0x00-0x7f.
* Our use of the Aria storage engine enables faster complex queries (queries\
  which normally use disk-based temporary tables). The [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria) storage\
  engine is used for internal temporary tables, which should give you a speedup\
  when doing complex selects. Aria is usually faster for temporary tables when\
  compared to MyISAM because Aria caches row data in memory and normally\
  doesn't have to write the temporary rows to disk.
* There are some improvements to DBUG code to make its execution faster when\
  debug is compiled in but not used.

### Extensions & new features

* [Table Elimination](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/table-elimination) (New optimization) (MWL#17)
* [Pool of Threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-in-mariadb-51-53) (Allows you to have 200,000+ connections\
  to MariadB)
* MariaDB can handle up to 32 key segments per key (up from 16)
* Added `--abort-source-on-error` to the mysql client.
* [Microsecond Precision in Processlist](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/time_ms-column-in-information_schemaprocesslist)
* [mysqltest extensions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/testing-tools/mariadb-test/new-features-for-mysqltest-in-mariadb)

### Easier to upgrade

We have made it [easy to upgrade from MySQL 5.0](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql/migrating-to-mariadb-from-mysql-obsolete-articles/upgrading-to-mariadb-from-mysql-50-or-older)\
to [MariaDB 5.1](changes-improvements-in-mariadb-5-1.md)

* InnoDB and Archive tables are now upgraded properly.
* More options to [mysql\_upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysql_upgrade) and [mysqlcheck](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqlcheck) to find out what's going\
  on.
* Cleaned up wrong warnings from mysqlcheck.

(Upgrading from MySQL 5.1 to MariaDB 5.1 is a trivial 1 min exercise as MariaDB\
is a binary drop in replacement of MySQL. Just remove MySQL and install MariaDB\
and things will **just work** )

### Better Testing

* More tests in the test suite.
* All tests runs now clean without having to restart test. (Oracle re-runs\
  tests 3 times and assumes things are ok if one tests works)
* Test builds with different configure options to get better feature testing.
* Remove invalid tests. (e.g. Don't test feature "X" if that feature is not\
  in the build you are testing.)

### Fewer warnings and bugs

* A build is not regarded ok if there are any errors or compiler warnings.
* We have fixed a lot of bugs in the MySQL code which we have found while\
  merging the MySQL code into MariaDB and by running the extended test suite.

### Security Vulnerabilities Fixed in [MariaDB 5.1](changes-improvements-in-mariadb-5-1.md)

For a complete list of security vulnerabilities (CVEs) fixed across all\
versions of MariaDB, see the [Security Vulnerabilities Fixed in MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/cve)\
page.

* [CVE-2013-1548](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-1548): [MariaDB 5.1.66](5.1.66.md)[CVE-2013-1531](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-1531): [MariaDB 5.1.67](5.1.67.md)[CVE-2013-0389](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0389): [MariaDB 5.1.67](5.1.67.md)[CVE-2013-0385](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0385): [MariaDB 5.1.67](5.1.67.md)[CVE-2013-0384](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0384): [MariaDB 5.1.67](5.1.67.md)[CVE-2013-0383](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0383): [MariaDB 5.1.67](5.1.67.md)[CVE-2013-0375](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2013-0375): [MariaDB 5.1.67](5.1.67.md)[CVE-2012-5612](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-5612): [MariaDB 5.1.67](5.1.67.md)[CVE-2012-5611](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-5611): [MariaDB 5.1.67](5.1.67.md), [MariaDB 5.1.66](5.1.66.md)[CVE-2012-5060](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-5060): [MariaDB 5.1.66](5.1.66.md)[CVE-2012-4414](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-4414): [MariaDB 5.1.66](5.1.66.md) [CVE-2012-3197](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-3197): [MariaDB 5.1.66](5.1.66.md)[CVE-2012-3180](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-3180): [MariaDB 5.1.66](5.1.66.md)[CVE-2012-3177](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-3177): [MariaDB 5.1.66](5.1.66.md)[CVE-2012-3173](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-3173): [MariaDB 5.1.66](5.1.66.md)[CVE-2012-3167](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-3167): [MariaDB 5.1.66](5.1.66.md)[CVE-2012-3166](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-3166): [MariaDB 5.1.66](5.1.66.md)[CVE-2012-3163](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-3163): [MariaDB 5.1.66](5.1.66.md)[CVE-2012-3160](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-3160): [MariaDB 5.1.66](5.1.66.md)[CVE-2012-3158](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-3158): [MariaDB 5.1.66](5.1.66.md)[CVE-2012-3150](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-3150): [MariaDB 5.1.66](5.1.66.md)[CVE-2012-1734](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-1734): [MariaDB 5.1.66](5.1.66.md)[CVE-2012-1705](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-1705): [MariaDB 5.1.67](5.1.67.md)[CVE-2012-1703](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-1703): [MariaDB 5.1.62](5.1.62.md)[CVE-2012-1702](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-1702): [MariaDB 5.1.67](5.1.67.md)[CVE-2012-1690](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-1690): [MariaDB 5.1.62](5.1.62.md)[CVE-2012-1689](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-1689): [MariaDB 5.1.66](5.1.66.md)[CVE-2012-1688](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-1688): [MariaDB 5.1.62](5.1.62.md)[CVE-2012-0574](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0574): [MariaDB 5.1.67](5.1.67.md)[CVE-2012-0572](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0572): [MariaDB 5.1.67](5.1.67.md)[CVE-2012-0540](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0540): [MariaDB 5.1.66](5.1.66.md)[CVE-2009-4484](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2009-4484): [MariaDB 5.1.42](../../changelogs/changelogs-mariadb-51-series/mariadb-5142-changelog.md)

The following CVEs are also fixed in [MariaDB 5.1](changes-improvements-in-mariadb-5-1.md) but the fix is not tied to a specific version number:

* [CVE-2012-0113](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0113)
* [CVE-2011-2262](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2011-2262)
* [CVE-2012-0116](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0116)
* [CVE-2012-0118](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0118)
* [CVE-2012-0087](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0087)
* [CVE-2012-0101](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0101)
* [CVE-2012-0102](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0102)
* [CVE-2012-0115](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0115)
* [CVE-2012-0119](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0119)
* [CVE-2012-0120](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0120)
* [CVE-2012-0484](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0484)
* [CVE-2012-0485](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0485)
* [CVE-2012-0490](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0490)
* [CVE-2012-0112](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0112)
* [CVE-2012-0114](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0114)
* [CVE-2012-0492](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0492)
* [CVE-2012-0075](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2012-0075)

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
