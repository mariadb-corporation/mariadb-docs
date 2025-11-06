# MariaDB 10.11 Changes & Improvements

{% include "../../.gitbook/includes/latest-10-11.md" %}

[MariaDB 10.11](what-is-mariadb-1011.md) is a long-term maintenance release series, [maintained until](https://mariadb.org/about/#maintenance-policy) February 2028.

## Upgrading

* See [Upgrading Between Major MariaDB Versions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions) and [Upgrading from MariaDB 10.6 to MariaDB 10.11](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-from-mariadb-10-6-to-mariadb-10-11).

## New Features & Improvements

This list includes features from the short-term releases [MariaDB 10.7](../old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107.md), [MariaDB 10.8](../old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108.md), [MariaDB 10.9](../old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109.md) and [MariaDB 10.10](../old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010.md).

### Authentication

* [GRANT to PUBLIC](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#to-public) ([MDEV-5215](https://jira.mariadb.org/browse/MDEV-5215)) ([blog post](https://mariadb.org/grant-to-public-in-mariadb/))
* Separate [SUPER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#super) and [READ ONLY ADMIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#read_only-admin) privileges ([MDEV-29596](https://jira.mariadb.org/browse/MDEV-29596))
* [bind\_address](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#bind_address) now accepts a comma-separated list of addresses to bind to ([MDEV-24377](https://jira.mariadb.org/browse/MDEV-24377))
* password\_reuse\_check plugin is a new password validation plugin that prevents the new password from being the same as the one being used during the configurable retention period. ([MDEV-9245](https://jira.mariadb.org/browse/MDEV-9245), [MariaDB 10.7](../old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107.md))

### Optimizer

* Make [ANALYZE FORMAT=JSON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/analyze-format-json) show time spent in the query optimizer ([MDEV-28926](https://jira.mariadb.org/browse/MDEV-28926))
* Improve optimization of joins with many tables, including eq\_ref tables ([MDEV-28852](https://jira.mariadb.org/browse/MDEV-28852), [MariaDB 10.10](../old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010.md))
* Table elimination does not work across derived tables ([MDEV-26278](https://jira.mariadb.org/browse/MDEV-26278), [MariaDB 10.10](../old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010.md))
* Histograms in the statistics tables are more precise and stored as JSON, not binary ([MDEV-21130](https://jira.mariadb.org/browse/MDEV-21130), [MDEV-26519](https://jira.mariadb.org/browse/MDEV-26519), [blog post](https://mariadb.org/10-7-preview-feature-json-histograms/), [MariaDB 10.8](../old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108.md)).
* Improve simple multibyte collation performance on the ASCII range ([MDEV-26572](https://jira.mariadb.org/browse/MDEV-26572), [MariaDB 10.7](../old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107.md)).

#### Descending Indexes

* Individual columns in the [index](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-indexes) can now be explicitly sorted in the ascending or descending order. This can be useful for optimizing certain [ORDER BY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/order-by) cases ([MDEV-13756](https://jira.mariadb.org/browse/MDEV-13756), [MDEV-26938](https://jira.mariadb.org/browse/MDEV-26938), [MDEV-26939](https://jira.mariadb.org/browse/MDEV-26939), [MDEV-26996](https://jira.mariadb.org/browse/MDEV-26996), [MariaDB 10.8](../old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108.md)).

### Replication

* Change defaults for CHANGE MASTER TO so that GTID-based replication is used by default if master supports it ([MDEV-19801](https://jira.mariadb.org/browse/MDEV-19801), [MariaDB 10.10](../old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010.md))
* Added [global.slave\_max\_statement\_time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#slave_max_statement_time) system variable for SQL thread to limit maximum execution time per query replicated ([MDEV-27161](https://jira.mariadb.org/browse/MDEV-27161), [MariaDB 10.10](../old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010.md))
* Deprecate [MASTER\_USE\_GTID=Current\_Pos](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to#master_use_gtid) to favor new [MASTER\_DEMOTE\_TO\_SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to#master_demote_to_slave) option ([MDEV-20122](https://jira.mariadb.org/browse/MDEV-20122), [MariaDB 10.10](../old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010.md))
* Implement the --do-domain-ids, --ignore-domain-ids, and --ignore-server-ids options for [mariadb-binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog) ([MDEV-20119](https://jira.mariadb.org/browse/MDEV-20119), [MariaDB 10.9](../old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109.md))
* Semisync-slave server recovery is extended to work on new server\_id server ([MDEV-27342](https://jira.mariadb.org/browse/MDEV-27342), [MariaDB 10.9](../old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109.md))
* [mariadb-binlog --stop-never --raw](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog/mariadb-binlog-options) now flushes the result file to disk after each processed event so the file can be listed with the actual bytes ([MDEV-14608](https://jira.mariadb.org/browse/MDEV-14608), [MariaDB 10.9](../old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109.md))
* Normally, [ALTER TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) gets fully executed on the primary first and only then it is [replicated](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication) and starts executing on replicas. With this feature `ALTER TABLE` gets replicated and starts executing on replicas when it starts executing on the primary, not when it finishes. This way the replication lag caused by a heavy `ALTER TABLE` can be completely eliminated ([MDEV-11675](https://jira.mariadb.org/browse/MDEV-11675), [MariaDB 10.8](../old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108.md)).
* Multi-source replication supports MySQL-style CHANNEL syntax ([MDEV-26307](https://jira.mariadb.org/browse/MDEV-26307), [MariaDB 10.7](../old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107.md))

#### mysqlbinlog GTID support

* [mariadb-binlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/logging-tools/mariadb-binlog) (or `mysqlbinlog` as it was called back when the task was created) now supports both filtering events by GTID ranges through `--start-position` and `--stop-position,` and validating a binary log's ordering of GTIDs through `--gtid-strict-mode` ([MDEV-4989](https://jira.mariadb.org/browse/MDEV-4989), [MariaDB 10.8](../old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108.md)).

### Galera

* Implement a method to add IPs to allowlist for Galera Cluster node addresses that can make SST/IST requests ([MDEV-27246](https://jira.mariadb.org/browse/MDEV-27246), [MariaDB 10.10](../old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010.md))
* JSON file interface to wsrep node state / SST progress logging ([MDEV-26971](https://jira.mariadb.org/browse/MDEV-26971), [MariaDB 10.9](../old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109.md))

### JSON

* [JSON\_OVERLAPS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_overlaps) function ([MDEV-27677](https://jira.mariadb.org/browse/MDEV-27677), [MariaDB 10.9](../old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109.md))
* Implement range notation for [JSONPath](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/jsonpath-expressions) ([MDEV-27911](https://jira.mariadb.org/browse/MDEV-27911), [MariaDB 10.9](../old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109.md))
* Support [JSONPath](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/jsonpath-expressions) negative index ([MDEV-22224](https://jira.mariadb.org/browse/MDEV-22224), [MariaDB 10.9](../old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109.md))
* [JSON\_EQUALS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_equals) function to check for equality between JSON objects ([MDEV-23143](https://jira.mariadb.org/browse/MDEV-23143), [MariaDB 10.7](../old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107.md)).
* [JSON\_NORMALIZE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_normalize) function, which recursively sorts keys and removes spaces ([MDEV-16375](https://jira.mariadb.org/browse/MDEV-16375), [MariaDB 10.7](../old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107.md))

### UUID

* New [UUID data type](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/uuid-data-type) ([MDEV-4958](https://jira.mariadb.org/browse/MDEV-4958), [MariaDB 10.7](../old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107.md))

### SHOW ANALYZE FORMAT=JSON

* Extend [SHOW EXPLAIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-explain) to support SHOW ANALYZE \[FORMAT=JSON] ([MDEV-27021](https://jira.mariadb.org/browse/MDEV-27021), [MariaDB 10.9](../old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109.md))
* Add EXPLAIN FOR CONNECTION syntax support to [SHOW EXPLAIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-explain) ([MDEV-10000](https://jira.mariadb.org/browse/MDEV-10000), [MariaDB 10.9](../old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109.md))

### Information Schema

* Performance Issues reading the [Information Schema Parameters table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-parameters-table) ([MDEV-29104](https://jira.mariadb.org/browse/MDEV-29104))
* Full table scan in the [Information Schema Parameters](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-parameters-table) and [Information Schema Routines](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-routines-table) tables ([MDEV-20609](https://jira.mariadb.org/browse/MDEV-20609))

### System versioning

* [System versioning](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/system-versioned-tables) setting, [system\_versioning\_insert\_history](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/system-versioned-tables#system_versioning_insert_history), to allow history modification ([MDEV-16546](https://jira.mariadb.org/browse/MDEV-16546))
* [mariadb-dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqldump): dump and restore historical data ([MDEV-16029](https://jira.mariadb.org/browse/MDEV-16029))
* Add option to [dump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/backup-restore-and-import-clients/mariadb-dump) [system versioned table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/temporal-tables/system-versioned-tables) as of specified timestamp ([MDEV-16355](https://jira.mariadb.org/browse/MDEV-16355), [MariaDB 10.7](../old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107.md)).

### InnoDB

* InnoDB performance improvements ([MDEV-27557](https://jira.mariadb.org/browse/MDEV-27557), [MDEV-28185](https://jira.mariadb.org/browse/MDEV-28185), [MDEV-27767](https://jira.mariadb.org/browse/MDEV-27767), [MDEV-28313](https://jira.mariadb.org/browse/MDEV-28313), [MDEV-28137](https://jira.mariadb.org/browse/MDEV-28137), [MDEV-28465](https://jira.mariadb.org/browse/MDEV-28465), [MDEV-26789](https://jira.mariadb.org/browse/MDEV-26789), [MariaDB 10.9](../old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109.md))
* In bulk insert, pre-sort and build indexes one page at a time ([MDEV-24621](https://jira.mariadb.org/browse/MDEV-24621), [MariaDB 10.7](../old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107.md))

#### InnoDB Redo Log Improvements

* autosize [innodb\_buffer\_pool\_chunk\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_buffer_pool_chunk_size) ([MDEV-25342](https://jira.mariadb.org/browse/MDEV-25342), [MariaDB 10.8](../old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108.md)).
* Improve the [redo log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-redo-log) for concurrency ([MDEV-14425](https://jira.mariadb.org/browse/MDEV-14425), [MariaDB 10.8](../old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108.md)).
* Remove FIL\_PAGE\_FILE\_FLUSH\_LSN ([MDEV-27199](https://jira.mariadb.org/browse/MDEV-27199), [MariaDB 10.8](../old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108.md)).

### UCA14 Collation

* Add UCA-14.0.0 [collations](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets) ([MDEV-27009](https://jira.mariadb.org/browse/MDEV-27009), [MariaDB 10.10](../old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010.md))
* Improve contraction performance in UCA collations ([MDEV-27265](https://jira.mariadb.org/browse/MDEV-27265), [MariaDB 10.10](../old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010.md))
* Improve UCA collation performance for utf8mb3 and utf8mb4 ([MDEV-27266](https://jira.mariadb.org/browse/MDEV-27266), [MariaDB 10.10](../old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010.md))

### Windows

* [Passwordless login](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi) for mariadb root user, for OS admin users ([MDEV-26715](https://jira.mariadb.org/browse/MDEV-26715))
* On newer versions of Windows (Windows 10 1903 or later), the `mariadb` client defaults to the utf8mb4 character set. Several problems with Unicode input and output in client were fixed. Command line utilities now accept all Unicode characters in user names, database names, file names etc (in the past, characters were restricted to the current ANSI codepage) ([MariaDB 10.8](../old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108.md)).

### Spider Storage Engine

* This was mostly internal refactoring work. As a result one can now declare [Spider](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider) connections using the `REMOTE_SERVER`, `REMOTE_DATABASE`, and `REMOTE_TABLE` attributes and not abuse the `COMMENT` field for that. This works both for the whole table and per partition ([MDEV-5271](https://jira.mariadb.org/browse/MDEV-5271), [MDEV-27106](https://jira.mariadb.org/browse/MDEV-27106), [MariaDB 10.8](../old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108.md)).

### Convert Partitions

* ALTER TABLE ... CONVERT PARTITION .. TO TABLE ([MDEV-22166](https://jira.mariadb.org/browse/MDEV-22166), [MariaDB 10.7](../old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107.md)), and
* ALTER TABLE ... CONVERT TABLE ... TO PARTITION ... ([MDEV-22165](https://jira.mariadb.org/browse/MDEV-22165)) as an easy way to convert tables to partitions and back in one command, instead of a sequence of CREATE/EXCHANGE/DROP ([MariaDB 10.7](../old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107.md))

### Miscellaneous

* Add [RANDOM\_BYTES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/random_bytes) function ([MDEV-25704](https://jira.mariadb.org/browse/MDEV-25704), [MariaDB 10.10](../old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010.md))
* The [INET4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/inet4) data type ([MDEV-23287](https://jira.mariadb.org/browse/MDEV-23287), [MariaDB 10.10](../old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010.md))
* Re-design the upper level of handling UPDATE and DELETE statements ([MDEV-28883](https://jira.mariadb.org/browse/MDEV-28883), [MariaDB 10.10](../old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010.md))
* Deprecate the [DES\_ENCRYPT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/des_encrypt)/[DECRYPT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/des_decrypt) functions ([MDEV-27104](https://jira.mariadb.org/browse/MDEV-27104), [MariaDB 10.10](../old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010.md))
* [Hashicorp Key Management Plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/hashicorp-key-management-plugin) for implementing [encryption](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption) using keys stored in the Hashicorp Vault KMS ([MDEV-19281](https://jira.mariadb.org/browse/MDEV-19281), [MariaDB 10.9](../old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109.md))
* Stored procedures already have support for the [IN, OUT and INOUT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/stored-routines/stored-procedures/create-procedure#inoutinout) parameter qualifiers. Added as well for [stored functions](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-function#in-out-inout-in-out) and (IN only) [cursors](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-cursors/declare-cursor#in) ([MDEV-10654](https://jira.mariadb.org/browse/MDEV-10654)). This was a [contribution](https://github.com/MariaDB/server/pull/1931) by [ManoharKB](https://github.com/ManoharKB) ([MariaDB 10.8](../old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108.md)).
* Add an optional argument to the [CRC32()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/numeric-functions/crc32) function, as well as the [CRC32C()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/numeric-functions/crc32c) function, which uses the Castagnoli polynomial. ([MDEV-27208](https://jira.mariadb.org/browse/MDEV-27208)). Note: The order of the 2-ary arguments was swapped after the preview release: `crc32('MariaDB')=crc32(crc32('Maria'),'DB')` ([MariaDB 10.8](../old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108.md))
* [my\_print\_defaults](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/administrative-tools/my_print_defaults) now handles `--default-*` options in exactly the same way as other MariaDB tools ([MDEV-26238](https://jira.mariadb.org/browse/MDEV-26238), [MariaDB 10.8](../old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108.md)).
* UCA [collations](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets) are now notably faster ([MDEV-27266](https://jira.mariadb.org/browse/MDEV-27266), [MDEV-27265](https://jira.mariadb.org/browse/MDEV-27265), [MariaDB 10.8](../old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108.md)).
* [NATURAL\_SORT\_KEY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/natural_sort_key) function ([MDEV-4742](https://jira.mariadb.org/browse/MDEV-4742), [MariaDB 10.7](../old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107.md)).
* Five provider plugins (bzip2, lzma, lz4, lzo, snappy) provide [compression capabilities](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/optimization-and-tuning-compression/compression-plugins) to the server and storage engines ([MDEV-12933](https://jira.mariadb.org/browse/MDEV-12933), [blog post](https://mariadb.org/10-7-preview-feature-provider-plugins), [MariaDB 10.7](../old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107.md)).
* [SFORMAT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/sformat) function for arbitrary text formatting ([MDEV-25015](https://jira.mariadb.org/browse/MDEV-25015), [MariaDB 10.7](../old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107.md))
* [GET DIAGNOSTICS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-diagnostics/get-diagnostics) supports a new condition property name `ROW_NUMBER`. In multi-row inserts it allows one to retrieve a number of a row that has caused the error ([MDEV-10075](https://jira.mariadb.org/browse/MDEV-10075), [MDEV-26611](https://jira.mariadb.org/browse/MDEV-26611), [MariaDB 10.7](../old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107.md))

### Variables

* For a list of all new variables, see [System Variables Added in MariaDB 10.11](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/system-and-status-variables-added-by-major-release/system-variables-added-in-mariadb-10-11).
* Rename [slow queries](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/slow-query-log) variables ([MDEV-7567](https://jira.mariadb.org/browse/MDEV-7567))
  * [log\_slow\_min\_examined\_row\_limit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#log_slow_min_examined_row_limit) (min\_examined\_row\_limit)
  * [log\_slow\_query](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#log_slow_query) (slow\_query\_log)
  * [log\_slow\_query\_file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#log_slow_query_file) (slow\_query\_log\_file). This was named [log\_slow\_query\_file\_name](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#log_slow_query_file) in the [MariaDB 10.11.0](10.11.0.md) preview release.
  * [log\_slow\_query\_time](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#log_slow_query_time) (long\_query\_time)
* [replicate\_rewrite\_db](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#replicate_rewrite_db) is now a system variable, no longer just an option ([MDEV-15530](https://jira.mariadb.org/browse/MDEV-15530))
* Change default of [explicit\_defaults\_for\_timestamp](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#explicit_defaults_for_timestamp) to ON ([MDEV-28632](https://jira.mariadb.org/browse/MDEV-28632), [MariaDB 10.10](../old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010.md))
* \--ssl option set as default for mariadb CLI ([MDEV-27105](https://jira.mariadb.org/browse/MDEV-27105), [MariaDB 10.10](../old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010.md))
* Merge (and deprecate) [old](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#old) to [old\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#old_mode) sql variable ([MDEV-24920](https://jira.mariadb.org/browse/MDEV-24920), [MariaDB 10.9](../old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109.md))
* Deprecate the [keep\_files\_on\_create](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#keep_files_on_create) variable ([MDEV-23570](https://jira.mariadb.org/browse/MDEV-23570), [MariaDB 10.8](../old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108.md)).
* Deprecate [wsrep\_replicate\_myisam](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_replicate_myisam) ([MDEV-24947](https://jira.mariadb.org/browse/MDEV-24947), [MariaDB 10.7](../old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107.md))
* Deprecate [wsrep\_strict\_ddl](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_strict_ddl) ([MDEV-24843](https://jira.mariadb.org/browse/MDEV-24843), [MariaDB 10.7](../old-releases/release-notes-mariadb-10-7-series/what-is-mariadb-107.md))

#### InnoDB Variables

* [innodb\_write\_io\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_write_io_threads) and [innodb\_read\_io\_threads](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_read_io_threads) are now dynamic, and their values can be changed without restarting the server ([MDEV-11026](https://jira.mariadb.org/browse/MDEV-11026))
* Removed [innodb\_version](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_version) ([MDEV-28554](https://jira.mariadb.org/browse/MDEV-28554), [MariaDB 10.10](../old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010.md))
* Deprecated [innodb\_prefix\_index\_cluster\_optimization](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_prefix_index_cluster_optimization) ([MariaDB 10.10](../old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010.md))
* Deprecated [innodb\_change\_buffering](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_change_buffering) ([MariaDB 10.9](../old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109.md))
* [innodb\_disallow\_writes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_disallow_writes) removed ([MDEV-25975](https://jira.mariadb.org/browse/MDEV-25975), [MariaDB 10.9](../old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109.md))
* [innodb\_log\_file\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_log_file_size) is now dynamic ([MDEV-27812](https://jira.mariadb.org/browse/MDEV-27812), [MariaDB 10.9](../old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109.md))

#### Spider Variables

The following deprecated variables have been removed ([MariaDB 10.10](../old-releases/release-notes-mariadb-10-10-series/what-is-mariadb-1010.md)):

* [spider\_udf\_ct\_bulk\_insert\_interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables)
* [spider\_udf\_ct\_bulk\_insert\_rows](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables)
* [spider\_udf\_ds\_bulk\_insert\_rows](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables)
* [spider\_udf\_ds\_table\_loop\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables)
* [spider\_udf\_ds\_use\_real\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables)
* [spider\_use\_handle](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables)
* [spider\_udf\_table\_mon\_mutex\_count](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables)
* [spider\_use\_handler](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/spider/spider-system-variables)

## Security Vulnerabilities Fixed in [MariaDB 10.11](what-is-mariadb-1011.md)

For a complete list of security vulnerabilities (CVEs) fixed across all\
versions of MariaDB, see the [Security Vulnerabilities Fixed in MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/security)\
page.

* [CVE-2025-30722](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30722): [MariaDB 10.11.12](10.11.12.md)
* [CVE-2025-30693](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-30693): [MariaDB 10.11.12](10.11.12.md)
* [CVE-2025-21490](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2025-21490): [MariaDB 10.11.11](10.11.11.md)
* [CVE-2024-21096](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21096): [MariaDB 10.11.8](10.11.8.md)
* [CVE-2023-52971](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52971): [MariaDB 10.11.12](10.11.12.md)
* [CVE-2023-52970](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52970): [MariaDB 10.11.12](10.11.12.md)
* [CVE-2023-52969](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52969): [MariaDB 10.11.12](10.11.12.md)
* [CVE-2023-22084](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22084): [MariaDB 10.11.6](10.11.6.md)
* [CVE-2022-47015](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-47015): [MariaDB 10.11.3](10.11.3.md)

## List of All [MariaDB 10.11](what-is-mariadb-1011.md) Releases

| Date        | Release                                                                                                                                                                              | Status      | Release Notes                                                                                                                                                                      | Changelog                                    |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| 6 Aug 2025  | [MariaDB 10.11.14](10.11.14.md)                                                                                                                                                      | Stable (GA) | [Release Notes](10.11.14.md)                                                                                                                                                       | [Changelog](../changelogs/10.11/10.11.14.md) |
| 22 May 2025 | [MariaDB 10.11.13](10.11.13.md)                                                                                                                                                      | Stable (GA) | [Release Notes](10.11.13.md)                                                                                                                                                       | [Changelog](../changelogs/10.11/10.11.13.md) |
| 6 May 2025  | [MariaDB 10.11.12](10.11.12.md)                                                                                                                                                      | Stable (GA) | [Release Notes](10.11.12.md)                                                                                                                                                       | [Changelog](../changelogs/10.11/10.11.12.md) |
| 4 Feb 2025  | [MariaDB 10.11.11](10.11.11.md)                                                                                                                                                      | Stable (GA) | [Release Notes](10.11.11.md)                                                                                                                                                       | [Changelog](../changelogs/10.11/10.11.11.md) |
| 1 Nov 2024  | [MariaDB 10.11.10](10.11.10.md)                                                                                                                                                      | Stable (GA) | [Release Notes](10.11.10.md)                                                                                                                                                       | [Changelog](../changelogs/10.11/10.11.10.md) |
| 8 Aug 2024  | [MariaDB 10.11.9](10.11.9.md)                                                                                                                                                        | Stable (GA) | [Release Notes](10.11.9.md)                                                                                                                                                        | [Changelog](../changelogs/10.11/10.11.9.md)  |
| 16 May 2024 | [MariaDB 10.11.8](10.11.8.md)                                                                                                                                                        | Stable (GA) | [Release Notes](10.11.8.md)                                                                                                                                                        | [Changelog](../changelogs/10.11/10.11.8.md)  |
| 7 Feb 2024  | [MariaDB 10.11.7](10.11.7.md)                                                                                                                                                        | Stable (GA) | [Release Notes](10.11.7.md)                                                                                                                                                        | [Changelog](../changelogs/10.11/10.11.7.md)  |
| 13 Nov 2023 | [MariaDB 10.11.6](10.11.6.md)                                                                                                                                                        | Stable (GA) | [Release Notes](10.11.6.md)                                                                                                                                                        | [Changelog](../changelogs/10.11/10.11.6.md)  |
| 14 Aug 2023 | [MariaDB 10.11.5](10.11.5.md)                                                                                                                                                        | Stable (GA) | [Release Notes](10.11.5.md)                                                                                                                                                        | [Changelog](../changelogs/10.11/10.11.5.md)  |
| 7 Jun 2023  | [MariaDB 10.11.4](10.11.4.md)                                                                                                                                                        | Stable (GA) | [Release Notes](10.11.4.md)                                                                                                                                                        | [Changelog](../changelogs/10.11/10.11.4.md)  |
| 10 May 2023 | [MariaDB 10.11.3](10.11.3.md)                                                                                                                                                        | Stable (GA) | [Release Notes](10.11.3.md)                                                                                                                                                        | [Changelog](../changelogs/10.11/10.11.3.md)  |
| 16 Feb 2023 | [MariaDB 10.11.2](10.11.2.md)                                                                                                                                                        | Stable (GA) | [Release Notes](10.11.2.md)                                                                                                                                                        | [Changelog](../changelogs/10.11/10.11.2.md)  |
| 17 Nov 2022 | [MariaDB 10.11.1](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/mariadb-10-11-series/broken-reference/README.md) | RC          | [Release Notes](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/mariadb-community-server-release-notes/mariadb-10-11-series/broken-reference/README.md) | [Changelog](../changelogs/10.11/10.11.1.md)  |
| 26 Sep 2022 | [MariaDB 10.11.0](10.11.0.md)                                                                                                                                                        | Alpha       | [Release Notes](10.11.0.md)                                                                                                                                                        |                                              |

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
