# Release Notes for MariaDB Enterprise Server 10.4.31-21

MariaDB Enterprise Server 10.4.31-21 is a maintenance release of [MariaDB Enterprise Server](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-enterprise-server/README.md) 10.4. This release includes a variety of fixes.

MariaDB Enterprise Server 10.4.31-21 was released on 2023-09-11.

## Backports

* [JSON\_OVERLAPS()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_overlaps) has been backported. (MENT-1853)
  * The `JSON_OVERLAPS()` function can be used to compare two JSON documents to determine if they have any key-value pairs or array elements in common.

```sql
SELECT JSON_OVERLAPS('{"A": 1, "B": {"C":2}}', '{"A": 2, "B": {"C":2}}') AS is_overlap;
```

```
+---------------------+
| is_overlap          |
+---------------------+
| 1                   |
+---------------------+
```

* [JSON\_SCHEMA\_VALID()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_schema_valid) has been backported. (MENT-1796)
  * The `JSON_SCHEMA_VALID()` function can be used to validate a JSON document against a JSON schema, as documented by the [JSON Schema Draft 2020](https://json-schema.org/draft/2020-12/release-notes.html).
  * This function can also be used in a `CHECK` constraint to verify that JSON documents are only stored in the database if they include required items and that the values are within a given range and length.

## Notable Changes

* The package for the `cracklib_password_check` plugin includes an SELinux policy, allowing the plugin to work with SELinux. ([MDEV-18374](https://jira.mariadb.org/browse/MDEV-18374))
* With Optimizer Trace, a `sel_arg_alloc_limit_hit` record is written when `MAX_SEL_ARGS` is reached. ([MDEV-30964](https://jira.mariadb.org/browse/MDEV-30964))
  * `MAX_SEL_ARGS` is one of the limits in the optimizer that triggers short-cut of time-intensive or memory-intensive analysis for complex `WHERE` clauses.
  * For example:

```sql
SELECT
 JSON_DETAILED(JSON_EXTRACT(trace, '$**.setup_range_conditions'))
 FROM information_schema.OPTIMIZER_TRACE;
```

```json
[
   [
       {
           "sel_arg_alloc_limit_hit":
           {
              "alloced_sel_args": 16001
           }
       }
   ]
]
```

* `ANALYZE FORMAT=JSON` output includes InnoDB statistics. ([MDEV-31577](https://jira.mariadb.org/browse/MDEV-31577))
  * For example:

```json
table": {
 "table_name": "t1",
 ...
 "r_engine_stats": {
 "pages_accessed": integer,
 "pages_updated" : integer,
 "pages_read_count" : integer,
 "pages_read_time_ms" : double_val,
 "old_rows_read" : integer,
 },
```

* Slow query log output includes InnoDB engine information. ([MDEV-31558](https://jira.mariadb.org/browse/MDEV-31558))
  * InnoDB engine information output is enabled with `--log-slow-verbosity=innodb`
  * Sample output:

```
# Pages_accessed: 184 Pages_read: 95 Pages_updated: 0 Undo_rows_read: 1\\

# Pages_read_time: 17.0204 Engine_time: 248.1297

```

* `Engine_time` is the time in milliseconds spent inside engine calls.
* `Page_*` variables are supported for the InnoDB storage engine.
* For the Spider storage engine, the default values and behavior of some system variables has changed: ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
  * Prior to this release:
    * These variables used a value of -1 (the default) to indicate that Spider would use the default table value, and this value was not user visible.
    * Spider table parameters could set values, but these values would be overridden with the system variable value if the system variable was set to a value other than -1.
  * Starting with this release:
    * The default value for these system variables has been updated to reflect the actual default table value, rather than -1.
    * Where a value is set by a table parameter, this value overrides the system default and the value set by Spider system variable.
    * If a table parameter is not set, the Spider system variable's value is used. This behavior is unchanged.
  * See "Interface Changes" for a full list of updated default values.

## Issues Fixed

### Can result in data loss

* With parallel replication, in some rare cases when the sequence of `FLUSH TABLE WITH READ LOCKS`, `UNLOCK TABLES`, and `STOP REPLICA` is executed, data can be lost on the replica. ([MDEV-31509](https://jira.mariadb.org/browse/MDEV-31509))

### Can result in a hang or crash

* With Aria storage engine, when Aria encryption is enabled and used but an encryption plugin is not loaded, the server can crash. ([MDEV-26258](https://jira.mariadb.org/browse/MDEV-26258))
* With Galera Cluster, when `wsrep_sst_donor` and `wsrep_cluster_address` are set to `NULL` rather than an empty string, the server can crash. ([MDEV-28433](https://jira.mariadb.org/browse/MDEV-28433))
* When `optimizer_switch='optimize_join_buffer_size=off'` is set, the server can crash. ([MDEV-31348](https://jira.mariadb.org/browse/MDEV-31348))
* When executing a `SELECT` query using an index for `GROUP BY` and filesort, the server can crash. ([MDEV-30143](https://jira.mariadb.org/browse/MDEV-30143))
* With MariaDB Connector/C, when the `mysql_list_fields()` function is called against a view, the server can crash. ([MDEV-30159](https://jira.mariadb.org/browse/MDEV-30159))
* With Aria storage engine, changing `aria_sort_buffer_size` settings to huge numbers and executing `INSERT/UPDATE` can result in a crash. ([MDEV-28054](https://jira.mariadb.org/browse/MDEV-28054))
* With parallel replication, when a replica thread gets killed, the replica node can crash. ([MDEV-31448](https://jira.mariadb.org/browse/MDEV-31448))
* With InnoDB storage engine, when `slave_parallel_mode` is `optimistic` and `slave_parallel_threads` is greater than 0, an `ALTER SEQUENCE` can fail with an `out-of-order` binlog error if the `SEQUENCE` uses InnoDB. ([MDEV-31503](https://jira.mariadb.org/browse/MDEV-31503))
  * Prior to this release, the following error can be raised:
    1. Last\_Error: Error 'An attempt was made to binlog GTID 0-1-100 which would create an out-of-order sequence number with existing GTID 0-1-100 and gtid stric mode is enabled' on query. Default database: 'test'. Query: 'alter sequence s1 restart with 1' will be shown.\`\`
* With replication, when `gtid_seq_no` is set to `DEFAULT` in a session, the server can crash. ([MDEV-31723](https://jira.mariadb.org/browse/MDEV-31723))
* With InnoDB storage engine, when a `BINARY(0)` or `VARBINARY(0)` column in an InnoDB table is indexed, the server can crash. ([MDEV-19216](https://jira.mariadb.org/browse/MDEV-19216))
* Setting `session_track_system_variables` globally to an invalid value can cause the server to crash. ([MDEV-25237](https://jira.mariadb.org/browse/MDEV-25237))
* Replication from an older MariaDB Server version to a newer MariaDB Server version can break, and the server may crash. (MENT-1935)
  * A mismatch in hash values was caused by use of different hash functions, causing rows in tables having explicit or implicit unique hash indexes to be treated as different rows between different versions of MariaDB Server even though the data in the rows was the same.

### Can result in unexpected behavior

* For a System Versioned table with non-versioned columns, if the initial `INSERT` includes a versioned column, an "on duplicate key update" for the non-versioned column generates a history record. ([MDEV-23100](https://jira.mariadb.org/browse/MDEV-23100))
* With Spider storage engine, setting a system variable overrides the value set as a table parameter. ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* The "pam\_user\_map" module does not correctly handle usernames or group names containing the "@" character. ([MDEV-31336](https://jira.mariadb.org/browse/MDEV-31336))
* With some Unicode collations, JSON functions can return incorrect results. ([MDEV-23187](https://jira.mariadb.org/browse/MDEV-23187))
* Stored routines with ROW variables set by subselects can produce incorrect results. ([MDEV-31250](https://jira.mariadb.org/browse/MDEV-31250))
* Integer multiplication, `DIV, MOD, or ROUND/TRUNCATE` could return unexpected results when an argument is evaluated as `-9223372036854775808` ([MDEV-30932](https://jira.mariadb.org/browse/MDEV-30932))
* With Galera Cluster, creating a `TEMPORARY SEQUENCE` can cause inconsistency. ([MDEV-31335](https://jira.mariadb.org/browse/MDEV-31335))
* With Galera Cluster, the state of the cluster can only be retrieved from the primary component. ([MDEV-21479](https://jira.mariadb.org/browse/MDEV-21479))
* `information_schema.PARAMETERS` can include outdated data when a stored routine is changed in one session while the stored routine is being used in a second session. ([MDEV-31064](https://jira.mariadb.org/browse/MDEV-31064))
* Queries that use multiple `RANK` window functions can produce the wrong result. ([MDEV-20010](https://jira.mariadb.org/browse/MDEV-20010))
* Queries that use the < "less than" operator to compare a string with a prefixed BLOB key produce the wrong result. ([MDEV-31800](https://jira.mariadb.org/browse/MDEV-31800))
* Recursive CTE execution is interrupted without errors or warnings when `max_recursive_iterations` is reached. ([MDEV-31214](https://jira.mariadb.org/browse/MDEV-31214))
  * Starting with this release, a warning occurs when `max_recursive_iterations` is reached:`Warning 1931 Query execution was interrupted. The query exceeded max_recursive_iterations = 1000. The query result may be incomplete.`
* On Microsoft Windows, when `lower_case_table_names=2`, `SHOW TABLES` does not work properly. ([MDEV-30765](https://jira.mariadb.org/browse/MDEV-30765))
* When the system is busy, `STOP REPLICA` can take a long time. ([MDEV-13915](https://jira.mariadb.org/browse/MDEV-13915))
* With parallel replication, `Seconds_Behind_Master` can show a wrong value. ([MDEV-30619](https://jira.mariadb.org/browse/MDEV-30619))
* With replication for System Versioned tables, having a parent table and a child table `WITH SYSTEM VERSIONING` where child table has a Foreign Key `CASCADE` generates orphan rows on replica. ([MDEV-31313](https://jira.mariadb.org/browse/MDEV-31313))
* `mariadb-dump --force` can stop with the error `Couldn't execute 'SHOW CREATE FUNCTION` object`':` even though `--force` should cause the error to be ignored. ([MDEV-31092](https://jira.mariadb.org/browse/MDEV-31092))
* With the ColumnStore storage engine and Federated storage engine, `ANALYZE` can return the incorrect value `0` for `r_rows` ([MDEV-29284](https://jira.mariadb.org/browse/MDEV-29284))
* `ALTER TABLE .. MODIFY COLUMN` can break foreign key constraints and lead to unrestorable dumps. ([MDEV-31086](https://jira.mariadb.org/browse/MDEV-31086))
* With InnoDB storage engine, three concurrent `DELETE` by a `UNIQUE` key can cause an unexpected deadlock. ([MDEV-10962](https://jira.mariadb.org/browse/MDEV-10962))
* With InnoDB storage engine, `innochecksum` fails with `Floating point exception` error. ([MDEV-31641](https://jira.mariadb.org/browse/MDEV-31641))
* With HashiCorp key management plugin, possible memory leaks. (MENT-1874)
* Using functions `MAX()` or `MIN()` with functions `ROUND(time)`, `CEILING(time)`, or `FLOOR(time)` as an argument can return wrong results. ([MDEV-23838](https://jira.mariadb.org/browse/MDEV-23838))
* For transaction precise System Versioned tables, UPDATE can return an unexpected error: ERROR 1761 (23000): `Foreign key constraint for table 'xxx', record 'yyy' would lead to a duplicate entry in table 'xxx', key 'PRIMARY'` ([MDEV-25644](https://jira.mariadb.org/browse/MDEV-25644))
* Assertion `const_item_cache == true` failed in `Item_func::fix_fields` when a flow control statement (such as `IF()`) was used in a generated column. ([MDEV-31319](https://jira.mariadb.org/browse/MDEV-31319))
* Creating a table with a foreign key (with a cascade action) defined on a base column of a virtual column is not rejected. ([MDEV-18114](https://jira.mariadb.org/browse/MDEV-18114), [MDEV-31322](https://jira.mariadb.org/browse/MDEV-31322))
  * Starting with this release, it is no longer possible to create `STORED` generated columns and `CHECK` constraints when values of the affected columns can be changed by foreign key constraint actions, such as `SET NULL` or `ON UPDATE CASCADE`.
    * Starting with this release, this results in an error like: `ERROR 1901 (HY000): Function or expression 'f_id' cannot be used in the GENERATED ALWAYS AS clause of 'v_id'`
  * Starting with this release, for existing tables with STORED generated columns, `SET NULL` and `ON UPDATE CASCADE` are ignored.

### Related to performance

* With partitioning, possible slow down of queries. ([MDEV-24712](https://jira.mariadb.org/browse/MDEV-24712))

### Interface Changes

* [aria\_sort\_buffer\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/aria/aria-system-variables) system variable maximum value changed from `18446744073709551615` to `1152921504606846975` ([MDEV-28054](https://jira.mariadb.org/browse/MDEV-28054))
* [aria\_sort\_buffer\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/aria/aria-system-variables) system variable minimum value changed from `4096` to `16376` ([MDEV-28054](https://jira.mariadb.org/browse/MDEV-28054))
* [ER\_JSON\_INVALID\_VALUE\_FOR\_KEYWORD](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4100-to-4199/e4193) error code added (MENT-1796)
* [ER\_JSON\_SCHEMA\_KEYWORD\_UNSUPPORTED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-4100-to-4199/e4194) error code added (MENT-1796)
* [ER\_QUERY\_EXCEEDED\_ROWS\_EXAMINED\_LIMIT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-code-reference) error code removed ([MDEV-31214](https://jira.mariadb.org/browse/MDEV-31214))
* [ER\_QUERY\_RESULT\_INCOMPLETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-1900-to-1999/e1931) error code added ([MDEV-31214](https://jira.mariadb.org/browse/MDEV-31214))
* [ER\_QUERY\_TIMEOUT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-code-reference) error code removed
* [ER\_UNUSED\_1](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/mariadb-internals/using-mariadb-with-your-programs-api/error-codes/mariadb-error-codes-1900-to-1999/e1928) error code added
* [JSON\_OVERLAPS()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_overlaps) function added (MENT-1853)
* [JSON\_SCHEMA\_VALID()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_schema_valid) function added (MENT-1796)
* [myisam\_sort\_buffer\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/myisam-storage-engine/myisam-system-variables) system variable maximum value changed from `18446744073709551615` to `1152921504606846975` ([MDEV-28054](https://jira.mariadb.org/browse/MDEV-28054))

### Spider Storage Engine

* [spider\_auto\_increment\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_auto_increment_mode) system variable default value changed from `-1` to `0` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_bgs\_first\_read](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_bgs_first_read) system variable default value changed from `-1` to `2` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_bgs\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_bgs_mode) system variable default value changed from `-1` to `0` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_bgs\_second\_read](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_bgs_second_read) system variable default value changed from `-1` to `100` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_bka\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_bka_mode) system variable default value changed from `-1` to `1` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_bka\_table\_name\_type](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_bka_table_name_type) system variable default value changed from `-1` to `0` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_buffer\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_buffer_size) system variable default value changed from `-1` to `16000` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_bulk\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_bulk_size) system variable default value changed from `-1` to `16000` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_bulk\_update\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_bulk_update_mode) system variable default value changed from `-1` to `0` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_bulk\_update\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_bulk_update_size) system variable default value changed from `-1` to `16000` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_casual\_read](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_casual_read) system variable default value changed from `-1` to `0` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_connect\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_connect_timeout) system variable default value changed from `-1` to `6` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_crd\_bg\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_crd_bg_mode) system variable default value changed from `-1` to `2` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_crd\_interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_crd_interval) system variable default value changed from `-1` to `51` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_crd\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_crd_mode) system variable default value changed from `-1` to `1` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_crd\_sync](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_crd_sync) system variable default value changed from `-1` to `0` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_crd\_type](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_crd_type) system variable default value changed from `-1` to `2` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_crd\_weight](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_crd_weight) system variable default value changed from `-1` to `2` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_delete\_all\_rows\_type](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_delete_all_rows_type) system variable default value changed from `-1` to `1` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_direct\_dup\_insert](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_direct_dup_insert) system variable default value changed from `-1` to `0` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_direct\_order\_limit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_direct_order_limit) System Variable system variable default value changed from `-1` to 9223372036854775807 ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_error\_read\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_error_read_mode) system variable default value changed from `-1` to `0` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_error\_write\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_error_write_mode) system variable default value changed from `-1` to `0` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_first\_read](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_first_read) system variable default value changed from `-1` to `0` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_init\_sql\_alloc\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_init_sql_alloc_size) system variable default value changed from `-1` to 1024 ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_internal\_limit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_internal_limit) system variable default value changed from `-1` to `9223372036854775807` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_internal\_offset](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_internal_offset) system variable default value changed from `-1` to `0` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_internal\_optimize](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_internal_optimize) system variable default value changed from `-1` to `0` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_internal\_optimize\_local](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_internal_optimize_local) system variable default value changed from `-1` to `0` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_load\_crd\_at\_startup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_load_crd_at_startup) system variable default value changed from `-1` to `1` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_load\_sts\_at\_startup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_load_sts_at_startup) system variable default value changed from `-1` to `1` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_low\_mem\_read](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_low_mem_read) system variable default value changed from `-1` to `1` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_max\_order](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_max_order) system variable default value changed from `-1` to `32767` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_multi\_split\_read](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_multi_split_read) system variable default value changed from `-1` to `100` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_net\_read\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_net_read_timeout) system variable default value changed from `-1` to `600` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_net\_write\_timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_net_write_timeout) system variable default value changed from `-1` to `600` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_quick\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_quick_mode) system variable default value changed from `-1` to `3` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_quick\_page\_byte](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_quick_page_byte) system variable default value changed from `-1` to `10485760`([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_quick\_page\_size](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_quick_page_size) system variable default value changed from `-1` to `1024` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_read\_only\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_read_only_mode) system variable default value changed from `-1` to `0` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_reset\_sql\_alloc](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_reset_sql_alloc) system variable default value changed from `-1` to `1``([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))`
* [spider\_second\_read](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_second_read) system variable default value changed from `-1` to `0` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_select\_column\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_select_column_mode) system variable default value changed from `-1` to `1` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_selupd\_lock\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_selupd_lock_mode) system variable default value changed from `-1` to `1` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_semi\_split\_read](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_semi_split_read) system variable default value changed from `-1` to `2` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_semi\_split\_read\_limit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_semi_split_read_limit) system variable default value changed from `-1` to `9223372036854775807` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_semi\_table\_lock](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_semi_table_lock) system variable default value changed from `1` to `0` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_semi\_table\_lock\_connection](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_semi_table_lock_connection) system variable default value changed from `-1` to `1` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_skip\_default\_condition](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_skip_default_condition) system variable default value changed from `-1` to `0` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_skip\_parallel\_search](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_skip_parallel_search) system variable default value changed from `-1` to `0` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_split\_read](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_split_read) system variable default value changed from `-1` to `9223372036854775807` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_store\_last\_crd](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_store_last_crd) system variable default value changed from `-1` to `1` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_store\_last\_sts](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_store_last_sts) system variable default value changed from `-1` to `1` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_sts\_bg\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_sts_bg_mode) system variable default value changed from `-1` to `2` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_sts\_interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_sts_interval) system variable default value changed from `-1` to `10` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_sts\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_sts_mode) system variable default value changed from `-1` to `1` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_sts\_sync](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_sts_sync) system variable default value changed from `-1` to `0` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_udf\_ct\_bulk\_insert\_interval](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_udf_ct_bulk_insert_interval) system variable default value changed from `-1` to `10` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_udf\_ct\_bulk\_insert\_rows](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_udf_ct_bulk_insert_rows) system variable default value changed from `-1` to `100` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_udf\_ds\_bulk\_insert\_rows](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_udf_ds_bulk_insert_rows) system variable default value changed from `-1` to `3000` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_udf\_ds\_table\_loop\_mode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_udf_ds_table_loop_mode) system variable default value changed from `-1` to `0` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_udf\_ds\_use\_real\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_udf_ds_use_real_table) system variable default value changed from `-1` to `0` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_use\_handler](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_use_handler) system variable default value changed from `-1` to `0` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))
* [spider\_use\_table\_charset](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/spider/spider-system-variables#spider_use_table_charset) system variable default value changed from `-1` to `1` ([MDEV-31524](https://jira.mariadb.org/browse/MDEV-31524))

## Platforms

In alignment with the [enterprise lifecycle](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/~/changes/32/mariadb-enterprise-server-release-notes/enterprise-server-lifecycle), MariaDB Enterprise Server 10.4.31-21 is provided for:

* CentOS 7 (x86\_64)
* Debian 10 (x86\_64, ARM64)
* Microsoft Windows (x86\_64) (MariaDB Enterprise Cluster excluded)
* Red Hat Enterprise Linux 7 (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64 Red Hat Enterprise Linux 8 packages)
* SUSE Linux Enterprise Server 12 (x86\_64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 20.04 (x86\_64, ARM64)

Some components of MariaDB Enterprise Server might not support all platforms. For additional information, see [MariaDB Corporation Engineering Policies".](https://mariadb.com/engineering-policies).

## Installation Instructions

* [MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server)
* [Enterprise Cluster Topology with MariaDB Enterprise Server ](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)[10](broken-reference)[.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Primary/Replica Topology with MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/primary-replica)
* [Enterprise Spider Sharded Topology with MariaDB Enterprise Server 10.4](broken-reference)
* [Enterprise Spider Federated Topology with MariaDB Enterprise Server 10.4](broken-reference)

## Upgrade Instructions

* [Upgrade to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/mariadb-community-server-upgrade-paths/upgrading-to-unmaintained-mariadb-releases/upgrading-from-mariadb-10-4-to-mariadb-10-5)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 10.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/platform-specific-upgrade-guides/upgrading-on-linux/upgrading-between-major-mariadb-versions)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
