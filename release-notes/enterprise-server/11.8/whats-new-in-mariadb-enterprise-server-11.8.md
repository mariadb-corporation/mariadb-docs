# What's New in MariaDB Enterprise Server 11.8

{% include "../../.gitbook/includes/latest-es-11.8.md" %}

MariaDB Enterprise Server 11.8 introduces a wide range of enhancements spanning developer productivity, security, compatibility, observability, and support for modern workloads like vector search. The MariaDB Enterprise Server 11.8.2-0 Technical Preview adds the innovations from the MariaDB Community Server releases 11.5 to 11.8 to MariaDB Enterprise Server 11.4.

## Vector Search <a href="#vector-search" id="vector-search"></a>

MariaDB Enterprise Server 11.8 continues to expand its native vector search capabilities, positioning MariaDB for AI-powered applications such as semantic search and recommendation systems. Already available in the MariaDB Enterprise Server 11.4 are:

* **New Data Type**: `VECTOR(N)` to store multi-dimensional embeddings.
* **Vector Indexing**: Efficient similarity search with `VECTOR INDEX`.
* **Distance Functions**:
  * `VEC_DISTANCE_EUCLIDEAN()` for L2 distance.
  * `VEC_DISTANCE_COSINE()` for angular similarity.
* **Conversion Functions**:
  * `Vec_FromText(json_array)` and `Vec_ToText(vector_column)` transform between the text and binary vector formats.
* [**System Variables**](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables) **for Index Tuning**:
  * `mhnsw_max_cache_size`, `mhnsw_default_distance`, `mhnsw_default_m`, `mhnsw_ef_search`.

### Added to MariaDB Enterprise Server 11.8 <a href="#added-to-mariadb-enterprise-server-118" id="added-to-mariadb-enterprise-server-118"></a>

* **Distance Functions**:
  * `VEC_DISTANCE()` auto-selects the best distance function based on the index configuration.
* Optimization that makes vector search 30-50% (depending on the data) faster for the same recall. Enabled automatically for applicable vectors. Vectors are applicable if they can be gradually truncated to trade some recall for speed. For example matryoshka embeddings as produced by OpenAI are applicable.
* Namespace support was added to HashiCorp Vault in MariaDB. See the [Hashicorp namespaces documentation](https://developer.hashicorp.com/vault/docs/enterprise/namespaces) for details.
* [Audit logging buffer writes](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-enterprise-audit#audit-logging-buffer-writes) are possible now.

## Indexes, SQL Functions, and Query Enhancements <a href="#indexes-sql-functions-and-query-enhancements" id="indexes-sql-functions-and-query-enhancements"></a>

* **UUID Generation**: New functions `UUID_v4() and UUID_v7()` for modern and time-ordered UUIDs.
* **Multi-Table DELETE Enhancements**: Support for `ORDER BY and LIMIT`.
* **Single-Table DELETE Enhancements**: Now it allows index hints.
* **NEW SHOW CREATE SERVER**: Recreate server objects similar to [SHOW CREATE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-create-table).
* **DBMS\_OUTPUT:** Messages submitted by `DBMS_OUTPUT.PUT_LINE()` are not sent to the client until the sending subprogram or trigger completes.

## Performance Improvements <a href="#data-types-and-compatibility" id="data-types-and-compatibility"></a>

* Optimization that makes vector search 30-50% faster (more details in the [Vector Search](whats-new-in-mariadb-enterprise-server-11.8.md#vector-search) section)
* Segmented key cache for [Aria storage engine](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria)
  * [aria\_pagecache\_segments](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/aria/aria-system-variables#aria_pagecache_segments) system variable
* Add [analyze\_max\_length](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#analyze_max_length) option to not collect statistics for long char/varchars, see [Skipping Long CHAR/VARCHAR Columns](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/analyze-table#skipping-long-char-varchar-columns) for more information

## Data Types and Compatibility <a href="#data-types-and-compatibility" id="data-types-and-compatibility"></a>

* **UTF-8 by Default**: `utf8mb4` replaces `latin1` and legacy `utf8`, ensuring full Unicode support, including emojis.
* **Default Collation**: `utf8mb4_uca1400_ai_ci` is now the standard for Unicode character sets.
* **Extended TIMESTAMP Range**: Increased upper bound to 2106 on 64-bit systems.
* **ROW Type Enhancements**:
  *   ROW types are now usable as stored function return values.\
      The support for `%ROWTYPE, TYPE OF, and RECORD(...)` declarations for Oracle-like compatibility:

      ```sql
      DECLARE
        TYPE DeptRecTyp IS RECORD (
          dept_id    NUMBER(4),
          dept_name  VARCHAR2(30),
          mgr_id     NUMBER(6),
          loc_id     NUMBER(4)
        );
      ```
* **Triggers**:
  *   `BEFORE UPDATE OF col1, col2` limits trigger execution to specific column updates:

      ```sql
      CREATE TRIGGER mytrigger BEFORE UPDATE OF col1, col2 ON t1 FOR EACH ROW …
      ```
* Use of `SIGNAL SQLSTATE '02TRG'` allows skipping a row operation.
*   Stored Procedures: Now support default parameter values:

    ```sql
    CREATE OR REPLACE PROCEDURE p1(param1 INT, param2 INT DEFAULT 1)
    ```
* Associative arrays: `DECLARE TYPE .. TABLE OF .. INDEX BY`
* Added `caching_sha2_password` plugin, see [Authentication Plugin - SHA-256](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-sha-256) for more information

## Enhancements to System Versioned Tables <a href="#enhancements-to-system-versioned-tables" id="enhancements-to-system-versioned-tables"></a>

*   System Versioned Tables is a powerful feature for auditing changes to data. Enabling System Versioned Tables is as easy as creating a table by using

    ```sql
    CREATE TABLE contracts (...) WITH SYSTEM VERSIONING;
    ```

    Or enabling the feature for an existing table by using

    ```sql
    ALTER TABLE contracts ADD SYSTEM VERSIONING;
    ```

    In both cases, invisible fields will be created in the table to track the timestamps and period for which the data is valid. A DBA/DevOps might want these fields to be visible. It is now possible to change such implicit fields to explicit ones by the following types of statements:

    ```sql
    SET @@system_versioning_alter_history= keep;
    ALTER TABLE contracts ADD COLUMN rs TIMESTAMP(6) AS ROW START, ADD COLUMN re TIMESTAMP(6) AS ROW END, ADD PERIOD FOR SYSTEM_TIME (rs,re);
    ```

## Security <a href="#security" id="security"></a>

* **New** [**Authentication Plugin—PARSEC**](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-parsec):
  * Based on elliptic curve cryptography.
  *   Mitigates the replay and man-in-the-middle attacks.\
      Example on how to create a user using the new [authentication plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins):

      ```sql
      CREATE USER 'MariaDBUser'@'%' IDENTIFIED VIA PARSEC USING PASSWORD('MyPassword123!');
      ```

      This will result in:

      ```sql
      SHOW GRANTS FOR MariaDBUser@'%';
      ```

      ```
      Grants for MariaDBUser@%
      GRANT USAGE ON *.* TO `MariaDBUser`@`%` IDENTIFIED VIA parsec USING 'P0:lhXyNv1cIxpB8EnTxR7ON7S7:1l3rWRW1/jw45yrvYXB8eh02wzk7lcJcz4CMc
      Ww2b+8'
      ```

      \\
* Unix Socket Enhancements:
  * Now supports explicit OS user mapping via `IDENTIFIED VIA UNIX_SOCKET AS` `'user'`.
  *   It is also possible to specify more than one OS user with the usual OR syntax:

      ```sql
      CREATE USER dba IDENTIFIED VIA UNIX_SOCKET AS 'jack' OR IDENTIFIED VIA UNIX_SOCKET AS 'jill';
      ```

## Replication & Clustering <a href="#replication-clustering" id="replication-clustering"></a>

* Improved Replication Lag Monitoring:
  *   [SHOW REPLICA STATUS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-replica-status) now includes:\\

      ```
      Master_last_event_time

      Slave_last_event_time

      Master_Slave_time_diff
      ```
*   [Information Schema Table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables) for [Replication Status](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-slave_status-table):\\

    ```sql
    MariaDB [test]> SELECT Master_last_event_time,Slave_last_event_time,Master_Slave_time_diff FROM information_schema.slave_status\G
    *************************** 1. row ***************************
    Master_last_event_time: 2024-08-13 07:32:38
    Slave_last_event_time: 2024-08-13 07:32:37
    Master_Slave_time_diff: 1
    ```
* **New Option – `--slave-abort-blocking-timeout`**: Kills blocking non-replication queries after a timeout.
* **Galera SST Automation**: SST user is now auto-created and managed internally.
* **Backported** [MDEV-35304](https://jira.mariadb.org/browse/MDEV-35304) : Add `{{Connects_Tried}}` & `{{Master_Retry_Count}}` from [CS-12.0](../../community-server/12.0/what-is-mariadb-120.md)

## Key Management <a href="#key-management" id="key-management"></a>

* [**KMS Plugin**](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins) **Enhancement**: The file\_key\_management plugin can now read keys from a **Unix socket**, not just from files.
* **File Key Management Encryption Plugin:** Added key rotation capability; see [this page](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/file-key-management-encryption-plugin#key-rotation) for details. In addition, a new Information Schema table was added, [FILE\_KEY\_MANAGEMENT\_KEYS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-files-table/information-schema-file_key_management_keys).

## Observability & Information Schema <a href="#observability-information-schema" id="observability-information-schema"></a>

* Temporary File Disk Space Limits:
  * `max_tmp_session_space_usage` and `max_tmp_total_space_usage` prevent runaway disk usage.
* New Status Variables: `tmp_space_used, max_tmp_space_used`.
* New [Information Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema) Views:
  * `SLAVE_STATUS` to view replication lag via SQL.
  * [USERS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-users-table) for password state and expiration monitoring.
  *   [SEQUENCES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-sequences-table) to introspect auto-generated sequences:\\

      ```sql
      SELECT * FROM INFORMATION_SCHEMA.SEQUENCES\G
      *************************** 1. row ***************************
             SEQUENCE_CATALOG: def
              SEQUENCE_SCHEMA: test
                SEQUENCE_NAME: s_name
                    DATA_TYPE: tinyint
            NUMERIC_PRECISION: 8
      NUMERIC_PRECISION_RADIX: 2
                NUMERIC_SCALE: 0
                  START_VALUE: 100
                MINIMUM_VALUE: -127
                MAXIMUM_VALUE: 126
                    INCREMENT: 10
                 CYCLE_OPTION: 0
      ```
* **Enhanced ANALYZE FORMAT=JSON**:
  * Includes `r_index_rows, r_icp_filtered`.
* **Thread Naming for Diagnostics**: Thread names are now more descriptive.
* **Galera Information Schema:** New [WSREP\_BF\_ABORTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_bf_aborts) Information Schema table.
* **Galera Information Schema:** New [WSREP\_THD\_STATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_thd_state) and [WSREP\_THD\_STATE\_HISTORY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_thd_state_history) Information Schema tables.
* **Galera Information Schema:** New Information Schema table [WSREP\_CONNECTIONS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_connections).
* **Galera Information Schema:** New Information Schema [WSREP\_CERT\_KEYS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_cert_keys) and [WSREP\_CERT\_KEYS\_HISTORY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/information-schema/information-schema-tables/information-schema-wsrep_cert_keys_history) tables.

## PL/SQL <a href="#tool-improvements" id="tool-improvements"></a>

Support for Oracle-stype `INDEX BY` tables (associative arrays) was backported from [MariaDB 12.1](../../community-server/12.1/changes-and-improvements-in-mariadb-12.1.md) in stored routines and anonymous blocks, with this declaration syntax:

```sql
TYPE type_name TABLE OF rec_type_name INDEX BY idx_type_name;
```

Where:

* `type_name` supports explicit and anchored data types (e.g `t1.col1%TYPE`).
* The `INDEX BY` clause supports integer and string data types.
* `rec_type_name` supports scalar and record data types.

The implementation supports the following associative array methods:

* `FIRST`
* `LAST`
* `NEXT`
* `PRIOR`
* `COUNT`
* `EXISTS`
* `DELETE`

## Tool Improvements <a href="#tool-improvements" id="tool-improvements"></a>

* **mariadb-dump**:
  * The `--dir=<path>` dumps each database to its subdirectory.
  * Supports parallel dumps and restores.
  * New `--update-history` converts `row_end TIMESTAMPs` during export.
* **mariadb-import**:
  * `--dir=<path>` restores from the dumped directory structure.
  * Supports `--database, --table, --ignore-database, --ignore-table` for selective restore.
  * `--innodb-optimize-keys`: defers index creation to speed up data loads.
* **mariadb-test (mtr):**
  * `mtr` can be started with the `--enable_serveroutput` option to enable `DBMS_OUTPUT` messages. See [this section](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/testing-tools/mariadb-test/mariadb-test-overview#options) for details.
* **mariadb (command-line client)**
  * New `--enable_serveroutput` option to enable `DBMS_OUTPUT` messages at start time. See [this section](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/mariadb-command-line-client#options) for details.
  * New `serveroutput` and `noserveroutput` command to enable and disable those messages at runtime. See [this section](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client/mariadb-command-line-client#mariadb-commands) for details.

## Userstat Plugin Enhancements <a href="#userstat-plugin-enhancements" id="userstat-plugin-enhancements"></a>

* Improved Insights:
  * Index usage via `QUERIES` in `INDEX_STATISTICS`.
  * Query operation counts: `ROWS_INSERTED, ROWS_UPDATED, KEY_READ_HITS,` etc.
  * New stats in `CLIENT_STATISTICS and USER_STATISTICS`.
  * Table I/O metrics: `PAGES_ACCESSED, PAGES_READ_FROM_DISK`.

## Available Versions <a href="#available-versions" id="available-versions"></a>

* [MariaDB Enterprise Server 11.8.3-1](11.8.3-1.md)
* MariaDB Enterprise Server 11.8.2-0 Tech Preview

See also: [All MariaDB Enterprise Releases](../all-releases.md)

## Installation Instructions <a href="#installation-instructions" id="installation-instructions"></a>

* [Deploy MariaDB Enterprise with Repositories](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage)
* [Deploy MariaDB Enterprise with Package Tarballs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/package-tarballs)
* [Deploy MariaDB Enterprise with Docker](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/automated-mariadb-deployment-and-administration/docker-and-mariadb/deploy-mariadb-enterprise-server-with-docker)

## Upgrade Instructions <a href="#upgrade-instructions" id="upgrade-instructions"></a>

* [Upgrade to MariaDB Enterprise Server 11.8](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-enterprise-server/mariadb-enterprise-server-upgrade-paths/mariadb-enterprise-server-11.8/upgrade-to-mariadb-enterprise-server-11.8)

## What's new in older release series <a href="#whats-new-in-older-release-series" id="whats-new-in-older-release-series"></a>

* [What's New in MariaDB Enterprise Server 11.4](../11.4/whats-new.md)
* [What's New in MariaDB Enterprise Server 10.6](../10.6/whats-new.md)
* [What's New in MariaDB Enterprise Server 10.5](../old-releases/10-5/whats-new-in-mariadb-enterprise-server-10-5.md)
* [What's New in MariaDB Enterprise Server 10.4](../old-releases/10-4/whats-new-in-mariadb-enterprise-server-10-4.md)
* [What's New in MariaDB Enterprise Server 10.3](../old-releases/10-3/whats-new-in-mariadb-enterprise-server-10-3.md)
* [What's New in MariaDB Enterprise Server 10.2](../old-releases/10-2/whats-new-in-mariadb-enterprise-server-10-2.md)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
