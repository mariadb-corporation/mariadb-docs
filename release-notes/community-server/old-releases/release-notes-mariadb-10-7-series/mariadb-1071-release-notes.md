# MariaDB 10.7.1 Release Notes

The most recent release of [MariaDB 10.7](what-is-mariadb-107.md) is:[**MariaDB 10.7.8**](mariadb-10-7-8-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.7.8/)

[Download 10.7.1](https://downloads.mariadb.org/mariadb/10.7.1/) | [Release Notes](mariadb-1071-release-notes.md) | [Changelog](../../changelogs/10.7/10.7.1.md) | [Overview of 10.7](what-is-mariadb-107.md)

**Release date:** 8 Nov 2021

**Do not use non-stable (non-GA) releases in production!**

[MariaDB 10.7](what-is-mariadb-107.md) is the current development series of MariaDB. It is an evolution\
of [MariaDB 10.6](../../10.6/what-is-mariadb-106.md) with several entirely new features.

[MariaDB 10.7.1](mariadb-1071-release-notes.md) is a [_**Release Candidate (RC)**_](../../about/release-criteria.md) release.

**For an overview of** [**MariaDB 10.7**](what-is-mariadb-107.md) **see the**[**What is MariaDB 10.7?**](what-is-mariadb-107.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Items

This release includes all features from the [MariaDB 10.7.0](mariadb-1070-release-notes.md) preview releases except for the JSON histogram preview feature, which was not ready in time to be included.

### Performance Schema

* Comments have been added for each table column in the [Performance Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema) to improve documentation ([MDEV-25325](https://jira.mariadb.org/browse/MDEV-25325)). For example:

```sql
SELECT column_name, column_comment FROM information_schema.columns 
  WHERE table_schema='performance_schema' AND table_name='file_instances';
```

```
...
*************************** 2. row ***************************
   column_name: EVENT_NAME
column_comment: Instrument name associated with the file.
*************************** 3. row ***************************
   column_name: OPEN_COUNT
column_comment: Open handles on the file. A value of greater than zero means 
                that the file is currently open.
...
```

### Diagnostics

* The [GET DIAGNOSTICS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/programmatic-compound-statements/programmatic-compound-statements-diagnostics/get-diagnostics#row_number) property introduced in [MariaDB 10.7.0](mariadb-1070-release-notes.md) to identify the affected row has been renamed to the more intuitive `ROW_NUMBER` ([MDEV-26611](https://jira.mariadb.org/browse/MDEV-26611), [MDEV-10075](https://jira.mariadb.org/browse/MDEV-10075))

### Provider Plugins

* Five provider plugins (bzip2, lzma, lz4, lzo, snappy) provide [compression capabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins) to the server and storage engines ([MDEV-12933](https://jira.mariadb.org/browse/MDEV-12933), [blog post](https://mariadb.org/10-7-preview-feature-provider-plugins)).

### SFORMAT

* [SFORMAT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/sformat) function for arbitrary text formatting ([MDEV-25015](https://jira.mariadb.org/browse/MDEV-25015), [blog post](https://mariadb.org/10-7-preview-feature-sformat/)).

### UUID

* New [UUID data type](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/uuid-data-type) ([MDEV-4958](https://jira.mariadb.org/browse/MDEV-4958), [blog post](https://mariadb.org/10-7-preview-feature-uuid-data-type/))

### Natural Sort

* [NATURAL\_SORT\_KEY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/natural_sort_key) function ([MDEV-4742](https://jira.mariadb.org/browse/MDEV-4742), [blog post](https://mariadb.org/10-7-preview-feature-natural-sort/)).

### Convert Partitions

* [ALTER TABLE ... CONVERT PARTITION .. TO TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table#convert-table-convert-partition) ([MDEV-22166](https://jira.mariadb.org/browse/MDEV-22166), [blog post](https://mariadb.org/10-7-preview-feature-convert-partition/)), and
* [ALTER TABLE ... CONVERT TABLE ... TO PARTITION ...](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table#convert-table-convert-partition) ([MDEV-22165](https://jira.mariadb.org/browse/MDEV-22165)) as an easy way to convert tables to partitions and back in one command, instead of a sequence of CREATE/EXCHANGE/DROP
* The redundant PARTITION keyword is now optional in the [partition definition](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table#partitions) ([MDEV-26471](https://jira.mariadb.org/browse/MDEV-26471))

### Password Reuse

* The [password\_reuse\_check plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/password-validation-plugins/password-reuse-check-plugin) is a new password validation plugin that prevents the new password from being the same as the one being used during the configurable retention period. ([MDEV-9245](https://jira.mariadb.org/browse/MDEV-9245), [blog post](https://mariadb.org/10-7-preview-feature-password-reuse-check-plugin/)).

### InnoDB

* In bulk insert, pre-sort and build indexes one page at a time ([MDEV-24621](https://jira.mariadb.org/browse/MDEV-24621))
* Linux after kernel version 5.10 has a io-uring regression causing a write to storage to be lost, or not acknowledged. As such [innodb\_use\_native\_aio](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-system-variables#innodb_use_native_aio) will default to 0 (off) until 5.16. If [innodb\_use\_native\_aio](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-system-variables#innodb_use_native_aio) is enabled in your configuration, a warning will be logged, however it will continue with the io-uring enabled, potentially resulting in a hang, or an assertion later. The long term support kernel 5.14.14 we haven't observed failures, and 5.15.0-rc7 failures have been observed, though less frequently. If you have [innodb\_use\_native\_aio](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-system-variables#innodb_use_native_aio) explicitly enabled, and are using watch out for a lack of InnoDB updates followed by a 10 minute timeout. See [MDEV-26674](https://jira.mariadb.org/browse/MDEV-26674) for details.
* `ALTER TABLE…IMPORT TABLESPACE` fixes ([MDEV-18543](https://jira.mariadb.org/browse/MDEV-18543), [MDEV-20931](https://jira.mariadb.org/browse/MDEV-20931), [MDEV-26131](https://jira.mariadb.org/browse/MDEV-26131), [MDEV-26621](https://jira.mariadb.org/browse/MDEV-26621))
* `innodb_undo_log_truncate` fixes ([MDEV-26445](https://jira.mariadb.org/browse/MDEV-26445), [MDEV-26450](https://jira.mariadb.org/browse/MDEV-26450), [MDEV-26672](https://jira.mariadb.org/browse/MDEV-26672), [MDEV-26864](https://jira.mariadb.org/browse/MDEV-26864))
* Page I/O performance fixes ([MDEV-25215](https://jira.mariadb.org/browse/MDEV-25215), [MDEV-26547](https://jira.mariadb.org/browse/MDEV-26547), [MDEV-26626](https://jira.mariadb.org/browse/MDEV-26626), [MDEV-26819](https://jira.mariadb.org/browse/MDEV-26819))
* Replication timeouts with `XA PREPARE` ([MDEV-26682](https://jira.mariadb.org/browse/MDEV-26682))
* Improved DDL and data dictionary ([MDEV-25919](https://jira.mariadb.org/browse/MDEV-25919))
* Performance fixes ([MDEV-26356](https://jira.mariadb.org/browse/MDEV-26356), [MDEV-26467](https://jira.mariadb.org/browse/MDEV-26467), [MDEV-26826](https://jira.mariadb.org/browse/MDEV-26826))

### Replication

* Memory hogging on slave by ROW event applier is eliminated ([MDEV-26712](https://jira.mariadb.org/browse/MDEV-26712))
* `mysql --binary-mode` now properly handles `\\0` in data ([MDEV-25444](https://jira.mariadb.org/browse/MDEV-25444))
* Fixes race condition between `SHOW BINARY LOGS` and `RESET MASTER` ([MDEV-20215](https://jira.mariadb.org/browse/MDEV-20215))

### Packaging & Misc

* Session tracking flag in OK\_PACKET ([MDEV-26868](https://jira.mariadb.org/browse/MDEV-26868))
* Some views force server (and mysqldump) to generate invalid SQL for their definitions ([MDEV-26299](https://jira.mariadb.org/browse/MDEV-26299))
* [JSON\_EQUALS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_equals) function to check for equality between JSON objects ([MDEV-23143](https://jira.mariadb.org/browse/MDEV-23143)).
* [JSON\_NORMALIZE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_normalize) function, which recursively sorts keys and removes spaces ([MDEV-16375](https://jira.mariadb.org/browse/MDEV-16375))
* Improve simple multibyte collation performance on the ASCII range ([MDEV-26572](https://jira.mariadb.org/browse/MDEV-26572)).
* Add option to [dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqldump) [system versioned table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/system-versioned-tables) as of specified timestamp ([MDEV-16355](https://jira.mariadb.org/browse/MDEV-16355)).
* Multi-source replication supports MySQL-style CHANNEL syntax ([MDEV-26307](https://jira.mariadb.org/browse/MDEV-26307))
* [wsrep\_replicate\_myisam](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_replicate_myisam) and [wsrep\_strict\_ddl](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_strict_ddl) deprecated system variables were removed ([MDEV-24947](https://jira.mariadb.org/browse/MDEV-24947), [MDEV-24843](https://jira.mariadb.org/browse/MDEV-24843))

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-\`-\`\`\`

## Changelog

For a complete list of changes made in [MariaDB 10.7.1](mariadb-1071-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/10.7/10.7.1.md).

## Contributors

For a full list of contributors to [MariaDB 10.7.1](mariadb-1071-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-10-7-1-rc-and-mariadb-10-6-5-10-5-13-10-4-22-10-3-32-and-10-2-41-now-available/).

**Do not use non-stable (non-GA) releases in production!**

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
