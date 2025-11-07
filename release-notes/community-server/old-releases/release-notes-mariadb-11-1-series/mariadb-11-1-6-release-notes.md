# MariaDB 11.1.6 Release Notes

[Download](https://downloads.mariadb.org/mariadb/11.1.6/) | [Release Notes](mariadb-11-1-6-release-notes.md) | [Changelog](../../changelogs/11.1/mariadb-11-1-6-changelog.md) | [Overview of 11.1](what-is-mariadb-111.md)

[_Alternate download from mariadb.org_](https://downloads.mariadb.org/mariadb/11.1.6/)

**Release date:** 8 Aug 2024

[MariaDB 11.1](what-is-mariadb-111.md) is a short-term stable series of MariaDB and will be [maintained until](https://mariadb.org/about/#maintenance-policy) August 2024. It is an evolution of [MariaDB 11.0](../release-notes-mariadb-11-0-series/what-is-mariadb-110.md) with several entirely new features.

[MariaDB 11.1.6](mariadb-11-1-6-release-notes.md) is a [_**Stable (GA)**_](../../about/release-criteria.md) release.

[MariaDB 11.1.6](mariadb-11-1-6-release-notes.md) is the last release of the [MariaDB 11.1](what-is-mariadb-111.md) release series.

**For an overview of** [**MariaDB 11.1**](what-is-mariadb-111.md) **see the**[**What is MariaDB 11.1?**](what-is-mariadb-111.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Items

### Storage Engines

#### InnoDB

* [ALTER TABLE...ALGORITHM=COPY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table#algorithmcopy) now builds indexes more efficiently ([MDEV-33087](https://jira.mariadb.org/browse/MDEV-33087))
  * Unsetting the [innodb\_alter\_copy\_bulk](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_alter_copy_bulk) system variable restores the old behavior.
* Fix unexpected storage read IO for the redo log, reintroduce [innodb\_log\_write\_ahead\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_write_ahead_size) ([MDEV-33894](https://jira.mariadb.org/browse/MDEV-33894))
* Correctly terminate transaction early with ER\_LOCK\_TABLE\_FULL when lock memory is growing ([MDEV-34167](https://jira.mariadb.org/browse/MDEV-34167))
* Alter operation on redundant table no longer aborts the server ([MDEV-34222](https://jira.mariadb.org/browse/MDEV-34222))
* Fix MariaDB crash with SIGILL because the OS does not support AVX512 ([MDEV-34565](https://jira.mariadb.org/browse/MDEV-34565))
* Fix InnoDB: Failing assertion: `stat_n_leaf_pages > 0` in `ha_innobase::estimate_rows_upper_bound` ([MDEV-34474](https://jira.mariadb.org/browse/MDEV-34474))
* wait\_for\_read in buf\_page\_get\_low no longer hurts performance ([MDEV-34458](https://jira.mariadb.org/browse/MDEV-34458))
* Fix InnoDB: Assertion failure in file ./storage/innobase/page/page0zip.cc line 4211 ([MDEV-34357](https://jira.mariadb.org/browse/MDEV-34357))

#### Aria

* Fix [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria) index corruption when doing a REPAIR TABLE that has a size of over 4G ([MDEV-34522](https://jira.mariadb.org/browse/MDEV-34522))

#### Spider

* UBSAN: runtime error: applying non-zero offset in `spider_free_mem` and SIGSEGV in `spider_free_mem` on SELECT ([MDEV-31475](https://jira.mariadb.org/browse/MDEV-31475))
* SIGSEGV in `ha_resolve_storage_engine_name`, UBSAN: runtime error: index 4294967295 out of bounds for type 'st\_plugin\_int \*\[64]' ([MDEV-32487](https://jira.mariadb.org/browse/MDEV-32487))
* SIGSEGV in `spider_db_conn::fin_loop_check`, and ASAN: heap-use-after-free in `spider_db_mbase::fin_loop_check` on SHOW TABLE STATUS ([MDEV-34541](https://jira.mariadb.org/browse/MDEV-34541))
* SIGSEGV in `ha_spider::lock_tables` on BEGIN after table lock ([MDEV-29962](https://jira.mariadb.org/browse/MDEV-29962))
* SIGSEGV in `spider_conn_first_link_idx` and others on DELETE, INSERT and SELECT ([MDEV-32492](https://jira.mariadb.org/browse/MDEV-32492))
* Spider: Crashes, asserts, hangs, memory corruptions and ASAN heap-use-after-free's ([MDEV-27902](https://jira.mariadb.org/browse/MDEV-27902))
* Spider: `@@insert_id 128` to TINYINT: Assertion \`\`!is\_set() || (m\_status == DA\_OK\_BULK && is\_bulk\_op())'\` failed. ([MDEV-28105](https://jira.mariadb.org/browse/MDEV-28105))
* ASAN errors in `spider_db_free_result` after partition DDL ([MDEV-29027](https://jira.mariadb.org/browse/MDEV-29027))
* Server crashes when calling spider UDF after `aria_encrypt_tables` is enabled ([MDEV-34682](https://jira.mariadb.org/browse/MDEV-34682))

### Partitioning

* MariaDB Server crashes with ill-formed partitions ([MDEV-32155](https://jira.mariadb.org/browse/MDEV-32155))
* SIGSEGV in `parse_engine_part_options` on INSERT, SELECT or ALTER ([MDEV-34421](https://jira.mariadb.org/browse/MDEV-34421))
* Assertion \`\`auto\_increment\_value'`failed in`ha\_partition::info\` on INSERT into MEMORY table ([MDEV-24610](https://jira.mariadb.org/browse/MDEV-24610))

### Character Sets

* On startup: UBSAN: applying zero offset to null pointer in `my_copy_fix_mb` from `strings/ctype-mb.c` and other locations ([MDEV-34226](https://jira.mariadb.org/browse/MDEV-34226))
* On startup: UBSAN: runtime error: applying zero offset to null pointer in `skip_trailing_space` and `my_hash_sort_utf8mb3_general1400_nopad_as_ci` ([MDEV-34187](https://jira.mariadb.org/browse/MDEV-34187))
* SHOW CREATE DATABASE statement crashes the server when db name contains some unicode characters, ASAN stack-buffer-overflow ([MDEV-32376](https://jira.mariadb.org/browse/MDEV-32376))
* Wrong result set with `utf8mb4_danish_ci` and BNLH join ([MDEV-34417](https://jira.mariadb.org/browse/MDEV-34417))

### Optimizer

* On startup: UBSAN: runtime error: applying non-zero offset in `JOIN::make_aggr_tables_info` in sql/sql\_select.cc ([MDEV-34227](https://jira.mariadb.org/browse/MDEV-34227))
* Crash after killing query while it is processed by `test_quick_select` ([MDEV-30651](https://jira.mariadb.org/browse/MDEV-30651))
* Extend condition normalization to include `'NOT a'` ([MDEV-19520](https://jira.mariadb.org/browse/MDEV-19520))
* Constant subquery causing a crash in pushdown optimization ([MDEV-29363](https://jira.mariadb.org/browse/MDEV-29363))
* Crash when pushing condition with CHARSET()/COERCIBILITY() into derived table ([MDEV-33010](https://jira.mariadb.org/browse/MDEV-33010))
* 2nd execution name resolution problem with pushdown into unions ([MDEV-34506](https://jira.mariadb.org/browse/MDEV-34506))
* Assertion \`\`(key\_part->key\_part\_flag & 4) == 0'\` failed key\_hashnr ([MDEV-34580](https://jira.mariadb.org/browse/MDEV-34580))
* Crash caused by query containing constant having clause ([MDEV-23983](https://jira.mariadb.org/browse/MDEV-23983))
* Using NAME\_CONST() (or executing query from the stored procedure and referring to a local variable) changes the plan and may make execution slower ([MDEV-33971](https://jira.mariadb.org/browse/MDEV-33971))
* `ORDER BY DESC` causes ROWID Filter optimization performance degradation ([MDEV-33875](https://jira.mariadb.org/browse/MDEV-33875))

### [Replication](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication)

* Auto-generated [DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/changing-deleting-data/delete) from [HEAP](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/memory-storage-engine) table no longer breaks replication ([MDEV-25607](https://jira.mariadb.org/browse/MDEV-25607))
* Fix replication failure when [XA transactions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/transactions/xa-transactions) are used where the replica has [replicate\_do\_db](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#replicate_do_db) set and the client has touched a different database when running DML such as inserts. ([MDEV-33921](https://jira.mariadb.org/browse/MDEV-33921))
* Fix replication error when [CHANGE MASTER TO](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to) is used in conjunction with a password longer than 41 ascii characters ([MDEV-23857](https://jira.mariadb.org/browse/MDEV-23857))
* The [--init-rpl-role](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options#-init-rpl-role) option is utilized to avoid a possible error state in [semisync recovery](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/semisynchronous-replication) ([MDEV-33465](https://jira.mariadb.org/browse/MDEV-33465))

### Backup

* Hide password passed on commandline from `xtrabackup_info` ([MDEV-34434](https://jira.mariadb.org/browse/MDEV-34434))

### Galera

* [Galera](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/galera-cluster/README.md) updated to 26.4.19
  * NOTE: Includes increasing the GCS protocol version, which prevents downgrades of individual nodes in the cluster as soon as all nodes have been updated
* `galera_gtid_2_cluster`: Assertion \`\`thd->wsrep\_next\_trx\_id() != (0x7fffffffffffffffLL \* 2ULL + 1)'\` ([MDEV-32633](https://jira.mariadb.org/browse/MDEV-32633))
* table `gtid_slave_pos` entries never been deleted with `wsrep_gtid_mode = 0` ([MDEV-34170](https://jira.mariadb.org/browse/MDEV-34170))
* Deadlock found when trying to get lock during applying ([MDEV-31658](https://jira.mariadb.org/browse/MDEV-31658))
* Change error code for Galera unkillable threads ([MDEV-12008](https://jira.mariadb.org/browse/MDEV-12008))
* 10.11.8 cluster becomes inconsistent when using composite primary key and partitioning ([MDEV-34269](https://jira.mariadb.org/browse/MDEV-34269))
* `wsrep_sst_mariadb-backup` use `/tmp` dir during SST rather then user defined `tmpdir` ([MDEV-32158](https://jira.mariadb.org/browse/MDEV-32158))

### Error Log

* [server\_uid](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#server_uid) system variable added, and value added to the [error log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/error-log) at startup ([MDEV-34494](https://jira.mariadb.org/browse/MDEV-34494))

### General

* As per the [MariaDB Deprecation Policy](../../about/platform-deprecation-policy.md), this will be the last release of [MariaDB 11.1](what-is-mariadb-111.md) for Debian 10 "Buster", RHEL/CentOS 7, Ubuntu 23.10 "Mantic", and Fedora 38
* Repositories for Ubuntu 24.04 "Noble" have been added
* [IMPORT TABLESPACE](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/import-tablespace/README.md) no longer unnecessarily traverses tablespaces list ([MDEV-34670](https://jira.mariadb.org/browse/MDEV-34670))
* Fix unknown variable `defaults-group-suffix=` with [mariadb-secure-installation](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/deployment-tools/mariadb-secure-installation) ([MDEV-33265](https://jira.mariadb.org/browse/MDEV-33265))
* [mariadb-install-db](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/deployment-tools/mariadb-install-db) no longer hangs on macOS ([MDEV-34129](https://jira.mariadb.org/browse/MDEV-34129))
* Fix transaction termination with ER\_LOCK\_TABLE\_FULL when lock memory is growing ([MDEV-34167](https://jira.mariadb.org/browse/MDEV-34167))
* Disable new connections in case of fatal signal ([MDEV-34475](https://jira.mariadb.org/browse/MDEV-34475))
* Control over memory allocated for SP/PS ([MDEV-14959](https://jira.mariadb.org/browse/MDEV-14959))
* [Triggers](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/triggers-events/triggers) now work correctly with bulk insert ([MDEV-24411](https://jira.mariadb.org/browse/MDEV-24411))
* Fix assertion \`\`table->field\[0]->ptr >= table->record\[0] && table->field\[0]->ptr <= table->record\[0] + table->s->reclength'`failed in`void handler::assert\_icp\_limitations(uchar\*)\` ([MDEV-34632](https://jira.mariadb.org/browse/MDEV-34632))
* [sandbox mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/mariadb-command-line-client#-sandbox) - now compatible with [--binary-mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/mariadb-command-line-client#-binary-mode) ([MDEV-34203](https://jira.mariadb.org/browse/MDEV-34203))

### Security

* Fixes for the following [security vulnerabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security):
  * CVE-\`-\`\`\`

## Changelog

For a complete list of changes made in [MariaDB 11.1.6](mariadb-11-1-6-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/11.1/mariadb-11-1-6-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 11.1.6](mariadb-11-1-6-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/mariadb-11-6-1-11-5-2-11-4-3-11-2-5-11-1-6-10-11-9-10-6-19-and-10-5-26-now-available/).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
