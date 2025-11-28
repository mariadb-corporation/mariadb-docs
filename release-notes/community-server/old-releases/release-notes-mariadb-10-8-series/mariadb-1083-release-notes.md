# MariaDB 10.8.3 Release Notes

The most recent release of [MariaDB 10.8](what-is-mariadb-108.md) is:[**MariaDB 10.8.8**](mariadb-10-8-8-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.8.8/)

[Download 10.8.3](https://downloads.mariadb.org/mariadb/10.8.3/) | [Release Notes](mariadb-1083-release-notes.md) | [Changelog](../../changelogs/10.8/10.8.3.md) | [Overview of 10.8](what-is-mariadb-108.md)

**Release date:** 20 May 2022

[MariaDB 10.8](what-is-mariadb-108.md) is a short-term maintenance stable series of MariaDB. It is an evolution\
of [MariaDB 10.7](../release-notes-mariadb-10-7-series/what-is-mariadb-107.md) with several entirely new features.

[MariaDB 10.8.3](mariadb-1083-release-notes.md) will be a [_**Release Candidate (RC)**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 10.8**](what-is-mariadb-108.md) **see the**[**What is MariaDB 10.8?**](what-is-mariadb-108.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Items

### InnoDB

* Reduced scalability bottlenecks. Minimum size of [innodb\_log\_file\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_file_size) increased from 1MB to 4MB to cater for rare error message. ([MDEV-27774](https://jira.mariadb.org/browse/MDEV-27774))
* [innodb\_disallow\_writes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_disallow_writes) removed ([MDEV-25975](https://jira.mariadb.org/browse/MDEV-25975))
* InnoDB gap locking fixes ([MDEV-20605](https://jira.mariadb.org/browse/MDEV-20605), [MDEV-28422](https://jira.mariadb.org/browse/MDEV-28422))
* InnoDB performance improvements ([MDEV-27557](https://jira.mariadb.org/browse/MDEV-27557), [MDEV-28185](https://jira.mariadb.org/browse/MDEV-28185), [MDEV-27767](https://jira.mariadb.org/browse/MDEV-27767), [MDEV-28313](https://jira.mariadb.org/browse/MDEV-28313), [MDEV-28137](https://jira.mariadb.org/browse/MDEV-28137), [MDEV-28465](https://jira.mariadb.org/browse/MDEV-28465), [MDEV-26789](https://jira.mariadb.org/browse/MDEV-26789))
* Backup regression fixes ([MDEV-27919](https://jira.mariadb.org/browse/MDEV-27919))
* InnoDB portability: FreeBSD futexes ([MDEV-26476](https://jira.mariadb.org/browse/MDEV-26476)), POWER and s390x transactional memory ([MDEV-27956](https://jira.mariadb.org/browse/MDEV-27956))
* ALTER TABLE: Fixed bogus duplicate key errors ([MDEV-15250](https://jira.mariadb.org/browse/MDEV-15250))
* DDL and crash recovery fixes ([MDEV-27274](https://jira.mariadb.org/browse/MDEV-27274), [MDEV-27234](https://jira.mariadb.org/browse/MDEV-27234), [MDEV-27817](https://jira.mariadb.org/browse/MDEV-27817))
* Requests to recalculate [persistent statistics](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/innodb-persistent-statistics) were sometimes lost ([MDEV-27805](https://jira.mariadb.org/browse/MDEV-27805))

### Replication

* Semisync-slave server recovery is refined to correctly rollback prepared transaction ([MDEV-28461](https://jira.mariadb.org/browse/MDEV-28461))
* Circular semisync setup endless event circulation is handled ([MDEV-27760](https://jira.mariadb.org/browse/MDEV-27760))
* Semisync-slave server recovery is extended to work on new server\_id server ([MDEV-27342](https://jira.mariadb.org/browse/MDEV-27342))
* Server initialization time gtid\_slave\_pos purge related reason of crashing in binlog background thread is removed ([MDEV-26473](https://jira.mariadb.org/browse/MDEV-26473))
* Shutdown of the semisync master can't produce inconsistent state anymore ([MDEV-11853](https://jira.mariadb.org/browse/MDEV-11853))
* Binlogs disappear after rsync IST ([MDEV-28583](https://jira.mariadb.org/browse/MDEV-28583))
* master crash is eliminated in compressed semisync replication protocol with packet counting amendment ([MDEV-25580](https://jira.mariadb.org/browse/MDEV-25580))
* OPTIMIZE on a sequence does not cause counterfactual ER\_BINLOG\_UNSAFE\_STATEMENT anymore ([MDEV-24617](https://jira.mariadb.org/browse/MDEV-24617))
* Automatically generated Gtid\_log\_list\_event is made to recognize within replication event group as a formal member ([MDEV-28550](https://jira.mariadb.org/browse/MDEV-28550))
* [Replication unsafe](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication) [INSERT .. ON DUPLICATE KEY UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert-on-duplicate-key-update) using two or more unique key values at a time with [MIXED format binlogging](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log/binary-log-formats#mixed-logging) is corrected ([MDEV-28310](https://jira.mariadb.org/browse/MDEV-28310))
* [Replication unsafe](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/unsafe-statements-for-statement-based-replication) [INSERT .. ON DUPLICATE KEY UPDATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/inserting-loading-data/insert-on-duplicate-key-update) stops issuing unnecessary "Unsafe statement" with [MIXED binlog format](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/binary-log/binary-log-formats#mixed-logging) ([MDEV-21810](https://jira.mariadb.org/browse/MDEV-21810))
* Incomplete replication event groups are detected to error out by the slave IO thread ([MDEV-27697](https://jira.mariadb.org/browse/MDEV-27697))
* [mysqlbinlog --stop-never --raw](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog/mariadb-binlog-options) now flushes the result file to disk after each processed event so the file can be listed with the actual bytes ([MDEV-14608](https://jira.mariadb.org/browse/MDEV-14608))

### Backup

* Incorrect binlogs after Galera SST using rsync and [MariaDB Backup](https://mariadb.com/docs/server/server-usage/backup-and-restore/mariadb-backup/) ([MDEV-27524](https://jira.mariadb.org/browse/MDEV-27524))
* [MariaDB Backup](https://mariadb.com/docs/server/server-usage/backup-and-restore/mariadb-backup/) does not detect multi-source replication slave ([MDEV-21037](https://jira.mariadb.org/browse/MDEV-21037))
* Useless warning "InnoDB: Allocated tablespace ID for , old maximum was 0" during backup stage ([MDEV-27343](https://jira.mariadb.org/browse/MDEV-27343))
* [MariaDB Backup](https://mariadb.com/docs/server/server-usage/backup-and-restore/mariadb-backup/) prepare fails for incrementals if a new schema is created after full backup is taken ([MDEV-28446](https://jira.mariadb.org/browse/MDEV-28446))

### Optimizer

* Query performance degradation in newer MariaDB versions when using many tables ([MDEV-28073](https://jira.mariadb.org/browse/MDEV-28073))
* A SEGV in Item\_field::used\_tables/update\_depend\_map\_for\_order... ([MDEV-26402](https://jira.mariadb.org/browse/MDEV-26402))
* ANALYZE FORMAT=JSON fields are incorrect for UNION ALL queries ([MDEV-27699](https://jira.mariadb.org/browse/MDEV-27699))
* Subquery in an UPDATE query uses full scan instead of range ([MDEV-22377](https://jira.mariadb.org/browse/MDEV-22377))
* Assertion \`item1->type() == Item::FIELD\_ITEM ... ([MDEV-19398](https://jira.mariadb.org/browse/MDEV-19398))
* Server crashes in Expression\_cache\_tracker::fetch\_current\_stats ([MDEV-28268](https://jira.mariadb.org/browse/MDEV-28268))
* MariaDB server crash at Item\_subselect::init\_expr\_cache\_tracker ([MDEV-26164](https://jira.mariadb.org/browse/MDEV-26164), [MDEV-26047](https://jira.mariadb.org/browse/MDEV-26047))
* Crash with union of my\_decimal type in ORDER BY clause ([MDEV-25994](https://jira.mariadb.org/browse/MDEV-25994))
* SIGSEGV in st\_join\_table::cleanup ([MDEV-24560](https://jira.mariadb.org/browse/MDEV-24560))
* Assertion \`!eliminated' failed in Item\_subselect::exec ([MDEV-28437](https://jira.mariadb.org/browse/MDEV-28437))

### Spider

The following variables have been deprecated:

* [spider\_crd\_type](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables) and [spider\_crd\_weight](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables) ([MDEV-28010](https://jira.mariadb.org/browse/MDEV-28010))
* [spider\_crd\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables) and [spider\_sts\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables) ([MDEV-28008](https://jira.mariadb.org/browse/MDEV-28008))
* [spider\_internal\_limit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables) ([MDEV-27981](https://jira.mariadb.org/browse/MDEV-27981))
* [spider\_internal\_offset](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables) ([MDEV-28297](https://jira.mariadb.org/browse/MDEV-28297))
* [spider\_store\_last\_crd](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables), [spider\_store\_last\_sts](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables), [spider\_load\_crd\_at\_startup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables) and [spider\_load\_sts\_at\_startup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables) ([MDEV-28007](https://jira.mariadb.org/browse/MDEV-28007))
* [spider\_udf\_ct\_bulk\_insert\_interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables), [spider\_udf\_ct\_bulk\_insert\_rows](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables), [spider\_udf\_ds\_bulk\_insert\_rows](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables), [spider\_udf\_ds\_table\_loop\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables), [spider\_udf\_ds\_use\_real\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables) ([MDEV-28005](https://jira.mariadb.org/browse/MDEV-28005))
* [spider\_use\_handler](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables) ([MDEV-27923](https://jira.mariadb.org/browse/MDEV-27923))
* [spider\_xa\_register\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables) ([MDEV-28244](https://jira.mariadb.org/browse/MDEV-28244))

### General

* Server [error messages](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/broken-reference/README.md) are [now available in Chinese](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets/internationalization-and-localization/setting-the-language-for-error-messages) ([MDEV-28227](https://jira.mariadb.org/browse/MDEV-28227))
* For RHEL/CentOS 7, non x86\_64 architectures are no longer supported upstream and so our support will also be dropped with this release
* Packages for Ubuntu 22.04 LTS "Jammy" and Fedora 36 are now available in this release
* As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will be the last release of [MariaDB 10.8](what-is-mariadb-108.md) for Debian 9 "Stretch", Ubuntu 21.10 "Impish", and Fedora 34

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-\`-\`\`\`

## Changelog

For a complete list of changes made in [MariaDB 10.8.3](mariadb-1083-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/10.8/10.8.3.md).

## Contributors

For a full list of contributors to [MariaDB 10.8.3](mariadb-1083-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-9-1-10-8-3-10-7-4-10-6-8-10-5-16-10-4-25-10-3-35-and-10-2-44-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
