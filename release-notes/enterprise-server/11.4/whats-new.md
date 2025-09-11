# What's New in MariaDB Enterprise Server 11.4

{% include "../../.gitbook/includes/latest-es-11.4.md" %}

MariaDB Enterprise Server 11.4 introduces new features to MariaDB Enterprise. Enhancements include JSON functions for validation and comparison, SQL functions for natural sorting and custom formatting, and a new UUID data type. Operational improvements include an improved cost-based optimizer, a new feature for non-blocking online schema changes, and faster InnoDB imports. Security is strengthened with default SSL encryption, password reuse prevention, and Galera Cluster security improvements. Replication is enhanced with default GTID, binary log size limits, and optimistic ALTER TABLE. Monitoring benefits from JSON histograms, new thread states, and detailed error reporting. These updates aim to improve developer experience, database administration, and overall performance.

This document includes all major features and changes between 10.6 ES and 11.4 ES.

## Upgrading from MariaDB Enterprise Server 10.6

* Upgrading from 10.6 should use take a few seconds with [mariadb-upgrade](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/deployment-tools/mariadb-upgrade) Please ensure that you do a [clean shutdown](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-between-major-mariadb-versions#requirements-for-doing-an-upgrade-between-major-versions) of 10.6 before doing the upgrade.
* The variable [optimizer\_adjust\_secondary\_key\_costs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/optimizer_adjust_secondary_key_costs) has no effect in 11.4 as all the features are already in 11. The variable is deprecated and should be remove from existing config files.

## Compatibility

* As long as no new 11.4 features are used (by CREATE TABLE or DML's) and the new variable [binlog\_alter\_two\_phase](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#binlog_alter_two_phase) is `0` (default) one should be able to use a 10.6 slave of 11.4 master.

## Developer Experience

### JSON Enhancements

* New JSON function `JSON_SCHEMA_VALID` to validate a JSON document against a JSON schema, as documented by the JSON Schema Draft 2020. This function can also be used in a CHECK constraint to verify that only JSON documents are stored in the database which include required items and that the values are within a given range, length, etcetera.
* New JSON functions `JSON_EQUALS()` and `JSON_NORMALIZE()` for easier comparison of two JSON documents and for normalizing JSON objects to be comparable, for example when a unique key based on JSON data is needed.
*   New function `JSON_OVERLAPS()`, which compares JSON documents to determine if they have any key-value pairs or array elements in common.\\

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
* New function `JSON_KEY_VALUE(<json_doc>,<json_path>)`, which extracts key/value pairs from a JSON object. The JSON path parameter is used to only return key/value pairs for matching JSON objects.
  *   Example:\\

      ```sql
      SELECT JSON_KEY_VALUE('[[1, {"key1":"val1", "key2":"val2"}, 3], 2, 3]', '$[0][1]');
      ```

      ```
      +-----------------------------------------------------------------------------+
      | JSON_KEY_VALUE('[[1, {"key1":"val1", "key2":"val2"}, 3], 2, 3]', '$[0][1]') |
      +-----------------------------------------------------------------------------+
      | [{"key": "key1", "value": "val1"}, {"key": "key2", "value": "val2"}]        |
      +-----------------------------------------------------------------------------+
      ```
* The function `JSON_KEY_VALUE()` can be used as an argument to `JSON_TABLE()`, which allows adding the key to a result set.\\
*   Example:\\

    ```sql
    SELECT jt.* FROM JSON_TABLE(
    JSON_KEY_VALUE('[[1, {"key1":"val1", "key2":"val2"}, 3], 2, 3]', '$[0][1]'),'$[*]'
    COLUMNS (
    k VARCHAR(20) PATH '$.key',
    v VARCHAR(20) PATH '$.value',
    id FOR ORDINALITY )) AS jt;
    ```

    ```
    +------+------+------+
    | k    | v    | id   |
    +------+------+------+
    | key1 | val1 |    1 |
    | key2 | val2 |    2 |
    +------+------+------+
    ```
* New function `JSON_ARRAY_INTERSECT(<array1>, <array2>)`, used to find the intersection between two JSON arrays.
  *   Example:\\

      ```sql
      SET @array1= '[1,2,3]';
      SET @array2= '[1,2,4]';
      SELECT json_array_intersect(@array1, @array2) AS result;
      ```

      \\

      ```
      +--------+
      | result |
      +--------+
      | [1, 2] |
      +--------+
      ```

      \\

      ```sql
      SET @json1= '[[1,2,3],[4,5,6],[1,1,1]]';
      SET @json2= '[[1,2,3],[4,5,6],[1,3,2]]';
      SELECT json_array_intersect(@json1, @json2) AS result;
      ```

      \\

      ```
      +------------------------+
      | result                 |
      +------------------------+
      | [[1, 2, 3], [4, 5, 6]] |
      +------------------------+
      ```
* The new JSON function `JSON_OBJECT_TO_ARRAY(<json_doc>)` is used to convert all JSON objects found in a JSON document to JSON arrays where each item in the outer array represents a single key-value pair from the object.
*   Example:\\

    ```sql
    SET @json1= '{ "a" : [1,2,3] , "b": {"key1": "val1", "key2": {"key3": "val3"}} }';
    SELECT JSON_OBJECT_TO_ARRAY(@json1) AS result;
    ```

    \\

    ```
    +-----------------------------------------------------------------------+
    | result                                                                |
    +-----------------------------------------------------------------------+
    | [["a", [1, 2, 3]], ["b", {"key1": "val1", "key2": {"key3": "val3"}}]] |
    +-----------------------------------------------------------------------+
    ```
* Resulting arrays can be compared using `JSON_ARRAY_INTERSECT()`:

```sql
SET @json1='{"a":[1,2,3],"b":{"key1":"val1","key2":{"key3":"val3"}}}';
SET @json2='{"a":[1,2,3]}';
SELECT JSON_OBJECT_TO_ARRAY(@json1) INTO @array1;
SELECT JSON_OBJECT_TO_ARRAY(@json2) INTO @array2;
SELECT JSON_ARRAY_INTERSECT(@array1,@array2) as result;
```

```
+--------------------+
| result             |
+--------------------+
| [["a", [1, 2, 3]]] |
+--------------------+
```

* The new JSON function `JSON_OBJECT_FILTER_KEYS(<json_doc>,<array_keys>)` returns key/value pairs from a JSON string for keys defined in \<array\_keys>.
* Example:

```sql
SET @json1= '{ "a": 1, "b": 2, "c": 3}';
SELECT JSON_OBJECT_FILTER_KEYS (@json1, ' ["b", "c"] ') AS result;
```

```
+------------------+
| result           |
+------------------+
| {"b": 2, "c": 3} |
+------------------+
```

* By using `JSON_ARRAY_INTERSECT()` and `JSON_KEY()` as arguments for `JSON_OBJECT_FILTER_KEYS()`, a comparison of two JSON strings is possible where only the same keys are compared, not the key/value pairs.\\
* Example (only show key/value pairs of json1 where the key exists in json2):

```sql
SET @json1= '{ "a": 1, "b": 2, "c": 3}';
SET @json2= '{"b" : 10, "c": 20, "d": 30}';
SELECT JSON_OBJECT_FILTER_KEYS (@json1, json_array_intersect(json_keys(@json1), json_keys(@json2))) AS result;
```

```
+------------------+
| result           |
+------------------+
| {"b": 2, "c": 3} |
+------------------+
```

* To define the position in a JSON array from the end to the beginning, negative indexes or last can be used as the last element of an array for an JSON array of a JSON path, where the JSON path is used as a parameter in a JSON function.

```sql
SELECT JSON_REMOVE(@json, '$.A[-10]');

SELECT JSON_REMOVE(@json, '$.A[last]');
```

* Range notation for JSON path using the keyword to define a range of elements.

```sql
SELECT JSON_REMOVE(@json, '$.A[1 to 3]');
```

### SQL Functions

* New function `NATURAL_SORT_KEY()` which can be used to sort strings naturally.
  * Example: A string "v10" would be sorted after a string "v9"
* New function `SFORMAT()` for custom formats of strings. The function uses a string including formatting options and a set of given values to generate a custom formatted string.
* New function `RANDOM_BYTES()` which returns a binary string of a length between 1 and 1024 bytes. This nondeterministic value is generated by the random number generator of the SSL library, so it generates an arbitrary length string of cryptographic random bytes that are suitable for cryptographic use.
* The encryption functions `AES_ENCRYPT() / AES_DES_ENCTYPT()` now support adding the two new parameters initialization vector (iv) and block encryption mode (mode).
* Syntax for older release series:

```sql
AES_ENCRYPT(str,key_str)
```

* New syntax:

```sql
AES_ENCRYPT(str, key, [, iv [, mode]])
```

* If no mode is provided it will be used from the new system variable `block_encryption_mode`.\\
* Example (using the mode from system variable block\_encryption\_mode):

```sql
SELECT @@block_encryption_mode;
```

```
+-------------------------+
| @@block_encryption_mode |
+-------------------------+
| aes-128-ecb             |
+-------------------------+
```

```sql
SELECT HEX(AES_ENCRYPT('MariaDB','mykey','vector')) AS result;
```

```
+----------------------------------+
| result                           |
+----------------------------------+
| CD0352A4B2FB18A592C04FF8CDA6C2F2 |
+----------------------------------+
```

```sql
SELECT AES_DECRYPT(x'CD0352A4B2FB18A592C04FF8CDA6C2F2','mykey','vector') AS result;
```

```
+---------+
| result  |
+---------+
| MariaDB |
+---------+
```

* Example (mode provided as argument):

```sql
SELECT HEX(AES_ENCRYPT('MariaDB','mykey','thisismy256vector','aes-256-cbc')) AS result;
```

```
+----------------------------------+
| result                           |
+----------------------------------+
| CD6C47183B89A813557BFD639A893CE3 |
+----------------------------------+
```

```sql
SELECT AES_DECRYPT(x'CD6C47183B89A813557BFD639A893CE3','mykey','thisismy256vector','aes-256-cbc') AS result;
```

```
+---------+
| result  |
+---------+
| MariaDB |
+---------+
```

* The new options `%Z` and `%z` can be used for the format string of the function

```sql
DATE_FORMAT(DATE, format)
```

for adding time zone information to the date string.

* `%Z` Time zone abbreviation
* `%z` Numeric time zone +hhmm or -hhmm presenting the hour and minute offset from UTC
* Example:

```sql
SELECT DATE_FORMAT(NOW(), '%W %d %M %Y %H:%i:%s %Z %z');
```

```
+--------------------------------------------------+
| DATE_FORMAT(NOW(), '%W %d %M %Y %H:%i:%s %Z %z') |
+--------------------------------------------------+
| Tuesday 21 November 2023 13:28:34 EST -0500      |
+--------------------------------------------------+
```

* The SQL function `KDF()` is a key derivation function, useful for generating encryption keys from a user provided password or a passphrase. It can be used to generate encryption keys for encryption functions such as `AES_ENCRYPT`.

```sql
KDF(key_str, salt [, {info | iterations} [, kdf_name [, width ]]])
```

* `kdf_name` is "hkdf" or "pbkdf2\_hmac"
* `width` (in bits) can be any number divisible by 8
* `info` is a non-secret parameter of the hkdf method, it allows to generate different encryption keys for different purposes from the same secret password
* `iterations` is a positive numeric parameter of the pbkdf2\_hmac method, larger values make the password more difficult to brute-force.\
  Example:

```sql
SELECT hex(kdf('foo', 'bar', 'info', 'hkdf'));
```

```
+----------------------------------------+
| hex(kdf('foo', 'bar', 'info', 'hkdf')) |
+----------------------------------------+
| 710583081D40A55F0B573A76E02D8975       |
+----------------------------------------+
insert into tbl values (aes_encrypt(@secret_data, kdf("Passw0rd", "NaCl", "info", 'hkdf'), "iv"));
```

* The function `CONV()` , which converts a number between numeric base systems, now supports conversions up to base 62. This allows conversions to encodings to capital letters A-Z, lower case letters a-z, and numbers 0-9. The old limit was 36, not including lower case letters.
  * Example:

```sql
SELECT CONV(61,10,36);
```

```
+----------------+
| CONV(61,10,36) |
+----------------+
| 1P             |
+----------------+
```

```sql
SELECT CONV(61,10,62);
```

```
+----------------+
| CONV(61,10,62) |
+----------------+
| z              |
+----------------+
```

### Data Types

* New data type UUID for more efficient storage of UUIDs
* New data type INET4 to store IPv4 addresses as 4-byte binary strings. Benefits of storing IPv4 addresses in the INET4 data type are:
  * Validation of incorrect values
  * Comparisons
  * Sorting
  * Functions like CAST
* Changed default behavior `TIMESTAMP` field properties
  * The default for `explicit_defaults_for_timestamp` is set to `ON` resulting in removing the nonstandard behavior for `TIMESTAMP` fields in `CREATE TABLE`
    * The properties `DEFAULT CURRENT_TIMESTAMP` or `ON UPDATE CURRENT_TIMESTAMP` are not set anymore for the first `TIMESTAMP` field in a table if not explicitly set
    * A `TIMESTAMP` field does not get the property NOT NULL set anymore if not explicitly set
    * The old behavior can be achieved by setting the properties explicitly or by setting `explicit_defaults_for_timestamp` to `OFF`

### Stored Routines

* Stored Functions qualifiers for `IN`, `OUT`, `INOUT`, and `IN OUT`. The qualifiers are following the syntax already used for stored procedures and take the differences for Oracle into account when using the Oracle compatibility mode (`sql_mode=ORACLE`).

### Indexes

MariaDB Enterprise Server now supports descending indexes. Composite indexes can be used with differently ordered columns to get a significant performance boost in the corresponding `ORDER BY` use cases.

### **Backported Features**:

* New, Detailed Replication Lag Representation.
* New Information Schema Table For Password Related Data.
* GTID binlog events now include the thread ID.
* Automatic SST user account management for Galera.
* PARSEC authentication plugin.
* Extending timestamp range to 2106.
* Limit the size of created disk temporary files and tables.
* The Software Bill of Materials (SBOM) JSON file is generated in the downloads archive.
* [Vector Search](https://mariadb.com/resources/blog/mariadb-vector-preview-is-out/) capability has been added (MENT-2233).

## Operational Enhancements

### Schema and Partitioning Management / DDL

{% hint style="success" %}
* New server internal [Online Schema Change (OSC)](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table/online-schema-change) which makes all schema changes (`ALTER TABLE` commands) non-blocking.
  * For instant `ALTER TABLE` operations (e.g., where `ALGORITHM=INSTANT` is used) OSC is not needed. However, for all other `ALTER` operations OSC provides significant benefits in reducing the locking time to a bare minimum.
  * The OSC feature works by creating a change buffer for storing changes during the copying of data from the old format to the new one. While data is copied from the old table structure to the new one all changes are stored in the change buffer and the table is fully accessible. Once the copying process is complete the change buffer is applied to the new data structure only requiring a very short locking period.
  * Having an internal OSC in the server eliminates the need for using external command line tools in order to reduce table locks. These external tools often need to create complicated structures in the database (like triggers and stored procedures) and certain race conditions can lead to the operations never finishing.
  * In MariaDB Enterprise Server 11.4 a default `ALTER` operation will be an OSC operation if possible. If the operation cannot be performed as an OSC then another algorithm will be used. If the option `LOCK=NONE` is explicitly specified in the `ALTER` statement, then the operation will fail if it cannot be done as an OSC.
{% endhint %}

* `CONVERT PARTITION` and `CONVERT TABLE` used with `ALTER TABLE` can be used to convert a partition into a table or vise versa
* Exchange a Partition or Convert a Table Without Validation
  * The process of exchanging a partition with a table or converting a table to a partition can be a very slow operation, especially for larger tables because for each new data row, the partitioning definitions need to be verified to validate that the new row should indeed be in this partition.
  * This process can now be sped up by disabling this validation. This new feature should be used with care, as it can lead to inconsistencies if the partitioning rules are not met.
  * The new addition to ALTER TABLE is:

```sql
EXCHANGE PARTITION partition_name WITH TABLE tbl_name [{WITH | WITHOUT} VALIDATION]

CONVERT TABLE normal_table TO partition_definition [{WITH | WITHOUT} VALIDATION]
```

* Syntax extension to not require `PARTITION` keyword in each partition definition
* Stored routines are now taking changes to metadata into account whenever the stored routine is called, done for any object a stored routine depends on.
  * In older release series a reconnect was needed before a stored routine was able to update its metadata from altered objects
  * Example:

```sql
CREATE TABLE t1 (id INT);
INSERT INTO t1 VALUES (100);
CREATE PROCEDURE p1() SELECT * FROM t1;
CALL p1;
```

```
+------+
| id   |
+------+
|  100 |
+------+
```

```sql
ALTER TABLE t1 ADD COLUMN b INT DEFAULT 0;
CALL p1;
```

```
+------+------+
| id   | b    |
+------+------+
|  100 |    0 |
+------+------+
```

* In the above example both calls of the stored procedure p1 would have returned the same result set with the older release series.
* Temporary tables are now included in `information_schema.tables` and included in `SHOW TABLES` and `SHOW TABLE STATUS`
  * Example:

```sql
CREATE DATABASE test;
USE test;
CREATE TABLE t1 (id INT);
CREATE TEMPORARY TABLE t2_temp (id INT);
SHOW FULL TABLE;
```

```
+----------------+-----------------+
| Tables_in_test | Table_type      |
+----------------+-----------------+
| t2_temp        | TEMPORARY TABLE |
| t1             | BASE TABLE      |
+----------------+-----------------+
```

```sql
SELECT table_schema, table_name, table_type FROM information_schema.tables WHERE table_schema='test';
```

```
+--------------+------------+------------+
| table_schema | table_name | table_type |
+--------------+------------+------------+
| test         | t2_temp    | TEMPORARY  |
| test         | t1         | BASE TABLE |
+--------------+------------+------------+
```

* General Support of Packages for Stored Routines
  * Before MariaDB Enterprise Server 11.4, the CREATE PACKAGE feature, as well as CREATE PACKAGE BODY, were only supported with sql\_mode = ORACLE. They can now be used with any SQL mode.
  * Example:

```sql
DELIMITER $$

CREATE OR REPLACE PACKAGE myPkg
  PROCEDURE p1();
  FUNCTION f1() RETURNS INT;
END;

$$

CREATE OR REPLACE PACKAGE BODY myPkg

  -- variable declarations
  DECLARE v1 INT DEFAULT 1;
  DECLARE v2 INT DEFAULT 10;

  -- routine declarations
  PROCEDURE p1()
  BEGIN
    SELECT v1, v2;
  END;

  FUNCTION f1() RETURNS INT
  BEGIN
    RETURN v1;
  END;

  -- package initialization
  SET v1=v1 + 2;
END;
$$

DELIMITER ;

SELECT myPkg.f1();
```

```
+------------+
| myPkg.f1() |
+------------+
|          3 |
+------------+
```

```sql
CALL myPkg.p1();
```

```
+------+------+
| v1   | v2   |
+------+------+
|    3 |   10 |
+------+------+
```

### System-Versioned and Application-time Period Tables

* System-Versioned Tables can automate the creation of new HISTORY partitions partitioned by INTERVAL/LIMIT using the keyword AUTO when creating a table.

```sql
CREATE TABLE t1 (x INT) WITH SYSTEM VERSIONING

PARTITION BY SYSTEM_TIME INTERVAL 1 months AUTO;
```

* In this case a new HISTORY partition will be created on a monthly basis, storing old versions of the table data.
* Information About Application-time Period Tables
  * New views `PERIOD` and `KEY_PERIOD_USAGE` are added to information\_schema.
  * View `PERIODS` includes the columns
    * `TABLE_CATALOG`
    * `TABLE_SCHEMA`
    * `TABLE_NAME`
    * `PERIOD_NAME`
    * `START_COLUMN_NAME`
    * `END_COLUMN_NAME`
    * to list Application-time period tables, the name defined for a period, and the columns used for start and end timestamps.
  * View `KEY_PERIOD_USAGE` includes the columns
    * `CONSTRAINT_CATALOG`
    * `CONSTRAINT_SCHEMA`
    * `CONSTRAINT_NAME`
    * `TABLE_CATALOG`
    * `TABLE_SCHEMA`
    * `TABLE_NAME`
    * `PERIOD_NAME`
* Two new columns are added to the `COLUMNS` view of information\_schema
  * `IS_SYSTEM_TIME_PERIOD_START`
  * `IS_SYSTEM_TIME_PERIOD_END`

### Backup / Restore

* A dump of historical data for system versioned tables is now possible via the new option `--as-of` for mariadb-dump
* System versioned tables can now be dumped and restored by mariadb-dump
  * The new parameter mariadb-dump parameter `--dump-history` dumps all historical data
  * To restore from a dump file the new parameter `system_versioning_insert_history` needs to be enabled to allow direct inserts into `ROW_START` and `ROW_END` columns
  * The existing parameter `secure_timestamp` needs to be set to a value which allows changing session timestamps
* The command-line tool mariadb-dump now supports the new option `--order-by-size`. The new option can be used to create a dump of the tables of a database according to their size, smaller tables first.
* Parallelism for mariadb-dump
  * When mariadb-dump is used with the option `-T / --tab=` to produce tab-separated text-format data files per table, the new option `--parallel` (synonym `--use-threads`) can be used to use several threads in parallel to dump the table data to their .txt files. Parallelism also works if the option `--single-tansaction` is used.
  * The option `--parallel` has been added to mariadb-import as a synonym to `--use-threads`, which has been available before.

#### Character Sets / Collations

* New collations based on the Unicode Collation Algorithm (UCA) 14.0.0 have been added for the character sets utf8mb3, utf8mb4, ucs2, utf16, utf32
  * One neutral and 22 language specific collations have been added
  * Case sensitive, case insensitive, and nopad variants have been added
  * Collations (how to compare characters) are now separated from character sets (how to store characters). Collation names no longer have to include character set names, and the same collation can apply to many character sets
  * Improved contraction performance in UCA collations
  * Improved UCA collation performance for utf8mb3 and utf8mb4
* Full UNICODE support for MariaDB command-line tools on recent versions of Windows (Windows 10 1909 or later, Windows 11, Windows Server 2020 supported). The server my.ini config file is now also encoded in UTF8. Command-line client mariadb.exe uses utf8mb4 by default.
* The default collation used for a character set can now be changed globally or for a session via the new system variable character\_set\_collations. The default collation will be used whenever a character set is defined for a database object without defining the collation.
  * When not defining a character set the default collation is still the one defined with the system variable collation\_server.
  * This is also preparatory work for changing default collations to use the UCA 14.0.0 standard. In particular, this variable will allow replication between servers with different default collations.

```sql
SET @@character_set_collations='utf8mb4=uca1400_ai_ci';
CREATE DATABASE test_with_charset CHARACTER SET utf8mb4;
CREATE DATABASE test;
SELECT SCHEMA_NAME,DEFAULT_COLLATION_NAME FROM SCHEMATA WHERE SCHEMA_NAME LIKE "test%";
```

```
+-------------------+------------------------+
| SCHEMA_NAME       | DEFAULT_COLLATION_NAME |
+-------------------+------------------------+
| test_with_charset | utf8mb4_uca1400_ai_ci  |
| test              | utf8mb4_general_ci     |
+-------------------+------------------------+
```

### Performance

* Optimizations to information schema system tables
  * The information schema provides tables with metadata about stored procedures and stored routines, which are often used by third party tools, and MariaDB Connectors to retrieve details about existing routines. Previously, a high number of rows in these tables would have resulted in a performance impact. We have made a number of internal improvements to eliminate the performance impact completely for use cases, where metadata had to be queried regularly.

### **Optimizer**

{% hint style="success" %}
* New optimizer cost model, a change from a more rule-based to a cost-based model. Huge effort went into improving the calculations of the optimizer costs, taking into account state of the art SSD disks. The new implementation also takes the different characteristics of a storage engine into account.
  * If a key lookup cannot be used, the optimizer can now make better choices when to use index scan, table scan, index merges, or other methods to join data.
  * While one model may work well for a specific use case, it may not be the right model for other use cases. With the changes we've made, it's now possible to fine-tune the optimizer by changing costs for different metrics.
{% endhint %}

* Changes to the optimizer now allow the use of an index for a comparison of a `DATE` function to a constant value.

```sql
DATE(datetime_column) = const
```

* The optimizer also has been enhanced to allow single-table `UPDATE` and `DELETE` to take advantage of semi-join optimization.
* Improved optimizer performance in a case of join with many `eq_ref` tables

### MariaDB Enterprise Cluster (powered by Galera)

* Automatic SST User Account Management for MariaDB Enterprise Cluster
  * The State Snapshot Transfer (SST) method, needed to provide a full data copy to a new node, requires a dedicated account to access the remote server (donor) during the SST process.
  * The new MariaDB Enterprise Cluster (Galera) creates the user internally for the time of an SST, which makes the need to have an account created manually obsolete. This also removes the requirement to have a user and password provided via a configuration file. Having the user created by Galera also ensures that the needed privileges are set.
* For MariaDB Galera Cluster, configurations are set using one system variable as a semicolon separated list of options, the system variable wsrep\_provider\_options. MariaDB Community Server system variables are limited to a length of 2048 characters, which is not sufficient for the Galera options in some use cases, and also hard to maintain as a DBA.
  * A new plugin is available, enabled via the plugin-wsrep-provider option. The options are split into separate options, if the plugin is used. The use of the plugin is optional.

## MariaDB Replication

* _Incompatibility change:_ Replication is now using Global Transaction IDs (GTID) by default to make replicas crash safe
  * The default of `CHANGE MASTER TO` for `master_use_gtid` changes from `no` to `slave_pos`
  * A fresh slave start, a `RESET SLAVE`, or a `CHANGE MASTER TO` without the defining `master_use_gtid` is replicating in the GTID based mode using `gtid_slave_pos` as the position to start downloading transactions from the primary
* Global Limitation of Space Used by Binary Logs
  * The new system variable `max_binlog_total_size` (alias `binlog_space_limit`) enables binary log purging when the total size of all binary logs exceeds the specified threshold. The default for `max_binlog_total_size` is `0`, meaning that there is no limit. The system variable can be changed without restarting the server.
  * The new system variable `--slave-connections-needed-for-purge`, set to `1` by default, assures that binary log purging will not happen until at least that many replicas are connected, and do not need purged binary logs anymore.
  * The new status variable `binlog_disk_use` can be used to query the disk space currently used by the binary logs.
* Index for Binary Log on GTIDs
  * An index is now created on the GTIDs of the binary log, which allows a connecting replica to find the position it should start from without the need to scan the whole binary log.
    * The new system variable `binlog_gtid_index` (default ON) can be used to disable the creation of indexes.
    * The new system variable `binlog_gtid_index_page_size` (default `4096`) defines the page size to use for the binary log GTID index.
    * The new system variable `binlog_gtid_index_span_min` (default `65536`) controls the sparseness of the binary log GTID index.
    * The new status variables `binlog_gtid_index_hit` and `binlog_gtid_index_miss` can be used for monitoring purposes. A miss is an indication that the index file is missing.
* GTID Binlog Events Now Include Thread ID
  * The thread ID and the corresponding statement can now be retrieved from binary logs.
  * The output of mariadb-dump also includes the thread ID.
* A new option '`slave_max_statement_time`' for the SQL thread has been added to allow to set a maximum allowed execution time for a replicated query
  * Allows to control the maximum time a replica can be behind a primary if the primary goal is to have a small replication lack, with the cost to be out of sync. It is therefore disabled by default.
* The binary log filter options `binlog-do-db`, `binlog-ignore-db`, and `binlog-row-event-max-size` are now visible as system variables.
  * Example:

```sql
SHOW GLOBAL VARIABLES WHERE
        Variable_name LIKE 'binlog_do_db' OR
        Variable_name LIKE 'binlog_ignore_db' OR
        Variable_name LIKE 'binlog_row_event_max_size';
```

```
+---------------------------+-------+
| Variable_name             | Value |
+---------------------------+-------+
| binlog_do_db              |       |
| binlog_ignore_db          |       |
| binlog_row_event_max_size | 8192  |
+---------------------------+-------+
```

* New `"SQL_BEFORE_GTIDS"` and `"SQL_AFTER_GTIDS"` for `START REPLICA UNTIL`
  * The new options `SQL_BEFORE_GTIDS` and `SQL_AFTER_GTIDS` for `START REPLICA UNTIL` allow user control of whether the replica stops before or after a provided GTID state. Its syntax is:

```sql
START SLAVE UNTIL (SQL_BEFORE_GTIDS|SQL_AFTER_GTIDS)="<gtid_list>"
```

* When providing `SQL_BEFORE_GTIDS="<gtid_list>"`, for each domain specified in the gtid\_list, the replica will execute transactions up to the GTID found, and immediately stop processing events in that domain without executing the transaction of the specified GTID.
* Once all domains have stopped, the replica will stop. Events originating from domains that are not specified in the list are not replicated.
* `START SLAVE UNTIL SQL_AFTER_GTIDS="<gtid_list>"` is an alias to the default behavior of `START SLAVE UNTIL master_gtid_pos="<gtid_list>"`, the known behavior before MariaDB Enterprise Server 11.4.
* The replica will execute transactions originating from domain ids provided in the list, and will stop once all transactions provided in the UNTIL list have all been executed.
* Example:

If a primary server has a binary log consisting of the following GTIDs:

```
0-1-1
1-1-1
0-1-2
1-1-2
0-1-3
1-1-3
```

Given a fresh replica (i.e., one with an empty GTID position, @@gtid\_slave\_pos=") is started with SQL\_BEFORE\_GTIDS, i.e.,

```sql
START SLAVE UNTIL SQL_BEFORE_GTIDS="1-1-2"
```

the resulting gtid\_slave\_pos of the replica will be "1-1-1" because the replica will execute only events from domain 1. When it sees the transaction with sequence number 2 it immediately stops without executing it.

If the replica is started with SQL\_AFTER\_GTIDS, i.e.,

```sql
START SLAVE UNTIL SQL_AFTER_GTIDS="1-1-2"
```

the resulting gtid\_slave\_pos of the replica will be "1-1-2" because the replica will execute only events from domain 1. But in this case it stops after executing the provided GTID.

* New, detailed replication lag representation
  * The `Seconds_Behind_Master` field of `SHOW REPLICA STATUS` can be complex and confusing, especially when parallel replication, delayed replication, or the option `sql_slave_skip_counter` is used. To help provide a consistent view of replication lag, three new fields have been added to the statement's output to provide specific timing information about the state of the IO and SQL threads.
    * `Master_last_event_time`
      * Timestamp of the last event read from the primary by the IO thread
    * `Slave_last_event_time`
      * Timestamp from the primary of the last event committed on the replica
    * `Master_Slave_time_diff`
      * The difference of the above two timestamps

### Optimistic ALTER TABLE for Replicas

{% hint style="success" %}
* New optimistic `ALTER TABLE` for replicas. When enabled by `binlog_alter_two_phase = 1` (not default), an `ALTER TABLE` is executed on the primary server and is replicated and "started" on the replica server more or less in parallel to the primary server. Thus, the possibly huge replication lag between a primary and replica server due to a long running `ALTER TABLE` on the primary can be avoided.
{% endhint %}

### MariaDB-binlog

* The command line tool mariadb-binlog now supports the use of global transaction IDs (GTID) for the options start-position and stop-position. mariadb-binlog can now be used to produce results filtered by the defined GTIDs.
* The command-line tool mariadb-binlog now supports the new options `--do-domain-ids`, `--ignore-domain-ids`, and `--ignore-server-ids`. mariadb-binlog can now be used to produce results filtered by domain ids server ids.

## Security and Access Control

* Client to Server connection now SSL Encrypted by Default
  * Using SSL/TLS has been simplified with MariaDB Enterprise Server 11.4. Before version 11.4, proper SSL configuration required multiple manual steps for the server, and all the clients connecting to it.
  * Now the client can verify the server self-signed certificate without any configuration whatsoever. The server completely automatically generates the SSL certificate and the client automatically verifies it as needed.
  * This simplification allows the server to now require SSL encrypted connections by default and to refuse unencrypted connections. Additionally, MariaDB Enterprise Server 11.4 allows users to verify SSL certificates using their fingerprints.
* New [Authentication Plugin — PARSEC](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-parsec) (Password Authentication using Response Signed with Elliptic Curves).
  * `PARSEC` improves security over old authentication plugins by introducing salted passwords, time consuming key derivation function, and a client-side scramble to ensure that man-in-the-middle attackers cannot control the client response.
  * Example on how to create a user using the new authentication plugin:

```sql
CREATE USER 'MariaDBUser'@'%' IDENTIFIED VIA PARSEC USING PASSWORD('MyPassword123!');
```

* This will result in:

```sql
SHOW GRANTS FOR MariaDBUser@'%';

Grants FOR MariaDBUser@%
GRANT USAGE ON *.* TO `MariaDBUser`@`%` IDENTIFIED VIA parsec USING 'P0:lhXyNv1cIxpB8EnTxR7ON7S7:1l3rWRW1/jw45yrvYXB8eh02wzk7lcJcz4CMcWw2b+8'
```

* The new plugin `password_reuse_check` can be used to validate that a password cannot be reused. The number of days until a password can be reused can be configured via a new parameter password\_reuse\_check\_interval
* New allowlist for MariaDB Galera Cluster node to restrict the nodes which can join a cluster to increase security .
  * A new system variable `wsrep_allowlist` can be used to define a list of IP addresses. Only nodes from these IP addresses can join a running
* The new SQL syntax `GRANT .. TO PUBLIC` can now be used to easily grant privileges to databases or tables for any user, who has access to the server.
  * `SHOW GRANTS FOR PUBLIC` is an enhancement to the existing `SHOW GRANTS` syntax to retrieve all privileges granted to public
* The fine grained privileges have been removed from the `SUPER` privilege.
  * The `SUPER` privilege is still used for some special cases, like using `DES_ENCRYPT` and `DES_DECRYPT` without an explicit key, for debug settings, and some system variables for changing them with `SET GLOBAL`.
  * With MariaDB Enterprise Server 11.4, changes were made to privileges to allow real read only replicas with no other privileges. This was achieved by removing the `READ ONLY ADMIN` privilege from the `SUPER` privilege and making it a new privilege. Hence the `READ ONLY ADMIN` privilege now needs to be granted explicitly, if this user should have write access to a read only replica (a replica having `read_only=1` set).
* New privilege `SHOW CREATE ROUTINE`
  * Before MariaDB Enterprise Server 11.4 a user only could see the definition of a routine, a stored feature, or function, when either of the following was met:
    * They had been granted the `SELECT` privilege for the `mysql.procs` table
    * The user was the definer of the Stored Procedure
  * The new privilege `SHOW CREATE ROUTINE`, has been introduced to enable any user with this privilege to view the definition of a stored routine.
  * Example without privilege `SHOW CREATE ROUTINE`:

```sql
SHOW grants;
```

```
+--------------------------------------------------+
| Grants for user1@%                               |
+--------------------------------------------------+
| GRANT USAGE ON *.* TO `user1`@`%`                |
| GRANT SELECT, EXECUTE ON `test`.* TO `user1`@`%` |
+--------------------------------------------------+
```

```sql
SHOW CREATE PROCEDURE myProc \G
```

```
*************************** 1. row ***************************
           Procedure: myProc
            sql_mode: STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
    Create Procedure: NULL
character_set_client: utf8mb3
collation_connection: utf8mb3_general_ci
  Database Collation: utf8mb4_general_ci
```

* Example with the new privilege `SHOW CREATE ROUTINE`:

```sql
SHOW grants;
```

```
+-----------------------------------------------------------------------+
| Grants for user1@%                                                    |
+-----------------------------------------------------------------------+
| GRANT USAGE ON *.* TO `user1`@`%`                                     |
| GRANT SELECT, EXECUTE, SHOW CREATE ROUTINE ON `test`.* TO `user1`@`%` |
+-----------------------------------------------------------------------+
```

```sql
SHOW CREATE PROCEDURE myProc \G
```

```
*************************** 1. row ***************************
           Procedure: myProc
            sql_mode: STRICT_TRANS_TABLES,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION
    Create Procedure: CREATE DEFINER=`root`@`localhost` PROCEDURE `myProc`()
BEGIN
    SELECT "My Definiton of a Stored Procedure";
END
character_set_client: utf8mb3
collation_connection: utf8mb3_general_ci
  Database Collation: utf8mb4_general_ci
```

* `SHOW CREATE ROUTINE` privilege can be granted globally, per schema, or on individual routines.
* Retrieve Users Privileges on a Specific Table
  * MariaDB Server provides information about privileges a user has to a table in different views in the `INFORMATION_SCHEMA`, split between global, schema, and table privileges. Before MariaDB Enterprise Server 11.4, there was no easy way to list all the tables a user has access to, this information has to be queried from several tables.
  * MariaDB Enterprise Server 11.4 now provides a new view `privileges_by_table_by_level` in the `SYS` schema that lists the privilege and privilege level per user, schema, and table.
  * Example:

```sql
CREATE DATABASE test;
USE test;
CREATE TABLE t1 (id INT);
CREATE USER user1;
GRANT SELECT, UPDATE ON *.* TO user1;
CREATE USER user2;
GRANT SELECT ON test.* TO user2;
CREATE USER user3;
GRANT SELECT ON test.t1 TO user3;
SELECT * FROM sys.privileges_by_table_by_level WHERE GRANTEE NOT LIKE "'root'@'%'";
```

```
+--------------+------------+-------------+-----------+--------+
| TABLE_SCHEMA | TABLE_NAME | GRANTEE     | PRIVILEGE | LEVEL  |
+--------------+------------+-------------+-----------+--------+
| test         | t1         | 'user1'@'%' | SELECT    | GLOBAL |
| test         | t1         | 'user1'@'%' | UPDATE    | GLOBAL |
| test         | t1         | 'user2'@'%' | SELECT    | SCHEMA |
| test         | t1         | 'user3'@'%' | SELECT    | TABLE  |
+--------------+------------+-------------+-----------+--------+
```

* A new information Schema view, `USERS`, has been added, which DBAs can use to get insights about password related information for a user.
  * This information can be used:
    * by an application to inform a user about a password about to expire or an account which is at risk of being blocked due to the number of wrong passwords entered
    * by DBAs to query users which have been blocked because of too many invalid passwords entered
  * The new view includes the fields:
    * `USER` - A string including user name and host
    * `PASSWORD_ERRORS` - A counter with the current number of wrong passwords entered
      * Reset to 0 when a correct password has been entered
      * An account is blocked, if `max_password_errors` is reached
      * `NULL` for accounts with privilege `CONNECTION ADMIN`
    * `PASSWORD_EXPIRATION_TIME` - The date and time when the password expires or NULL, if the password never expires

## Storage Engines

* Engine-defined attributes can now also be defined per-partition for more flexible configurations.

### InnoDB

* The space occupied by freed pages within the InnoDB system tablespace can be reclaimed by adding an :`#autoshrink` attribute to `#innodb_data_file_path`#, like:

```
[mariadb]
...
innodb_data_file_path=ibdata1:12M;ibdata2:50M:autoextend:autoshrink
```

* This allows the system tablespace to be truncated after the last allocated page within it, all the way to the specified minimum size (here: `12MiB`). In older release series InnoDB data files never shrink in size during normal operation. One could shrink .ibd files by rebuilding tables with `OPTIMIZE TABLE`, or the undo tablespace files by `SET GLOBAL innodb_undo_log_truncate=ON`.
* Shrink temporary InnoDB tablespaces without restart
  * Before MariaDB Enterprise Server 11.4 the only way to reclaim disk space used by temporary InnoDB tablespaces was to restart the server, as temporary tablespaces are deleted when you stop the server, and are recreated with their configured size.
  * Restarting the server is not always possible, while you still need to reclaim disk space. MariaDB Enterprise Server 11.4 can solve this problem by executing

```sql
SET GLOBAL innodb_truncate_temporary_tablespace_now=1;
```

This triggers to reclaim the disk space, but existing tables will not be removed.

* Example:

```sql
CREATE TEMPORARY TABLE t1(f1 INT NOT NULL, f2 INT NOT NULL)ENGINE=InnoDB;
INSERT INTO t1 SELECT seq, seq FROM seq_1_to_65536;
DROP TABLE t1;
SELECT NAME, FILE_SIZE FROM INFORMATION_SCHEMA.INNODB_SYS_TABLESPACES WHERE NAME="innodb_temp
orary";
```

```
+------------------+-----------+
| NAME             | FILE_SIZE |
+------------------+-----------+
| innodb_temporary |  79691776 |
+------------------+-----------+
```

```sql
SET GLOBAL INNODB_TRUNCATE_TEMPORARY_TABLESPACE_NOW= 1;
SELECT NAME, FILE_SIZE FROM INFORMATION_SCHEMA.INNODB_SYS_TABLESPACES WHERE NAME="innodb_temp
orary";
```

```
+------------------+-----------+
| NAME             | FILE_SIZE |
+------------------+-----------+
| innodb_temporary |  12582912 |
+------------------+-----------+
```

* The process to import a InnoDB tablespace is now simplified. While the old process required to first create a table and to discard the tablespace before executing `ALTER TABLE IMPORT TABLESPACE, now ALTER TABLE IMPORT TABLESPACE` is the only command needed.
  * Example:

```sql
FLUSH TABLES t1 FOR EXPORT;
--copy_file $MYSQLD_DATADIR/test/t1.cfg $MYSQLD_DATADIR/test/t2.cfg
--copy_file $MYSQLD_DATADIR/test/t1.frm $MYSQLD_DATADIR/test/t2.frm
--copy_file $MYSQLD_DATADIR/test/t1.ibd $MYSQLD_DATADIR/test/t2.ibd
UNLOCK TABLES;
ALTER TABLE t2 IMPORT TABLESPACE;
```

* The InnoDB storage engine has gone through additional code cleanup and we have removed some configuration parameters used by the InnoDB Change Buffering feature, a feature which was disabled for earlier release series.
  * New system variables like `innodb_log_file_buffering`, `innodb_data_file_buffering`, `innodb_log_file_write_through`, and `innodb_data_file_write_through` have been added to allow better control for log files and data files. They can be set dynamically while the Server is running.
* Changes to the InnoDB redo log format to reduce write amplification, which can result in better performance.
* The system variables innodb\_write\_io\_threads and innodb\_read\_io\_threads are now dynamic, and their values can be changed without restarting the server

### Spider

* The `SPIDER` storage engine now allows the use of engine-defined attributes (table options), similar to other storage engines, and more convenient than the current method of providing parameters via `COMMENT` for a table.

## Analyzing, Tracing, and Monitoring

* Improved error reporting for INSERT that inserts multiple rows. The property `ROW_NUMBER` in `GET DIAGNOSTICS` allows retrieval of the row number that caused the error or warning.
* Implementation of JSON histograms with detailed histogram collection, used when `histogram_type=JSON_HB` (not the default) is set. Using JSON histograms results in more precise data statistics over string data types or when columns have highly-uneven data distribution. More precise statistics allow the optimizer to create better query plans resulting in faster queries.
* `ANALYZE [FORMAT=JSON] <select>` has been extended to allow analyzing a query which is currently running in another connection by running `SHOW ANALYZE FORMAT=JSON for <conn_id>`.
* ANALYZE FORMAT=JSON now shows the time spent in the query optimizer
  * In some cases optimizing the query can take a while. `ANALYZE FORMAT=JSON` now reports time as `"query_optimization"`: { `"r_total_time_ms": NNNN.NNN` } in the JSON string
* `SHOW EXPLAIN` for `<conn_id>`, which returns an `EXPLAIN` for a query running in another connection, has been extended to return the more detailed JSON output by using the syntax `SHOW EXPLAIN [FORMAT=JSON] FOR <conn_id>`.
  * Syntax EXPLAIN `[ FORMAT=JSON] FOR CONNECTION <conn_id>` is also supported.
* New status monitoring features for MariaDB Enterprise Cluster:
  * New thread states in `PROCESSLIST` for MariaDB Galera Cluster allow better tracking of a session status
    * "waiting to execute in isolation"
    * "waiting for TOI DDL"
    * "waiting for flow control"
    * "waiting for certification"
  * MariaDB Enterprise Cluster has added a new feature to save wsrep node status changes in a dedicated machine readable JSON file. This allows an easier way for reading and interpreting the status file by an external monitoring tool. A filename needs to be specified via the option `wsrep_status_file` to enable the feature.
    * This JSON file also includes details about a node eviction status to the JSON file to report that a Galera node needs to be restarted to join the cluster.
  * MariaDB Enterprise Cluster now includes progress reporting of MariaDB Enterprise Backup based SST when `wsrep-debug=1` is set and the tool `pv` is installed. The SST progress report is then written into the server log:

{% code overflow="wrap" %}
```
2022-03-24 13:10:43 0 [Note] WSREP: REPORTING SST PROGRESS: '{ "from": 1, "to": 3, "total": 23106759472, "done": 23106759472, "indefinite": -1 }'
```
{% endcode %}

* The new value `SENT_ROWS` in the information schema table `PROCESSLIST` includes the number of rows sent by the current statement, shown in the processlist.
  * Selects with functions show the total number of rows sent by the main statement and all functions
  * Stored procedures show the total number of rows sent per stored procedure statement
  * `INSERT RETURNING` and `DELETE RETURNING` show the total number of rows sent for the returning data set
  * Example:

```sql
SELECT * FROM processlist\G
```

```
*************************** 1. row ***************************
...
*************************** 2. row ***************************
             ID: 6
           USER: root
           HOST: localhost
             DB: test
        COMMAND: Query
           TIME: 1
          STATE: Sending data
           INFO: select * from t1
        TIME_MS: 1340.406
          STAGE: 0
      MAX_STAGE: 0
       PROGRESS: 0.000
    MEMORY_USED: 89856
MAX_MEMORY_USED: 392544
  EXAMINED_ROWS: 0
      SENT_ROWS: 3895737
       QUERY_ID: 436
    INFO_BINARY: select * from t1
            TID: 100
```

* The SQL Error Log Plugin can be used to log errors sent to clients for later analysis. When option `sql_error_log_with_db_and_thread_info=ON` is set, the log file is now also showing thread id, and the current default schema for the error.

## Available Versions

* [MariaDB Enterprise Server 11.4.5-3](11.4.5-3.md)
* [MariaDB Enterprise Server 11.4.4-2](11.4.4-2.md)
* [MariaDB Enterprise Server 11.4.3-1](11.4.3-1.md)
* [MariaDB Enterprise Server 11.4.0-1](11.4.0-1.md)

## Installation Instructions

* [Deploy MariaDB Enterprise with Repositories](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server)
* [Deploy MariaDB Enterprise with Package Tarballs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/package-tarballs)
* [Deploy MariaDB Enterprise with Docker](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/automated-mariadb-deployment-and-administration/docker-and-mariadb/deploy-mariadb-enterprise-server-with-docker)
* [Enterprise Cluster Topology with MariaDB Enterprise Server](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/galera-cluster)
* [Primary/Replica Topology with MariaDB Enterprise Server](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/primary-replica)
* [ColumnStore Object Storage Topology with MariaDB Enterprise Server and MariaDB Enterprise ColumnStore](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-object-storage)
* [ColumnStore Shared Local Storage Topology with MariaDB Enterprise Server and MariaDB Enterprise ColumnStore](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/columnstore-shared-local-storage)
* [HTAP Topology with MariaDB Enterprise Server and MariaDB Enterprise ColumnStore](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/htap)
* [Single-Node Enterprise ColumnStore with MariaDB Enterprise Server and Object Storage](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-object-storage)
* [Single-Node Enterprise ColumnStore with MariaDB Enterprise Server](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/single-node-topologies/enterprise-server-with-columnstore-local-storage)
* [Enterprise Spider Sharded Topology with MariaDB Enterprise Server](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/spider-sharded)
* [Enterprise Spider Federated Topology with MariaDB Enterprise Server](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/architecture/topologies/spider-federated)

## Upgrade Instructions

* [Upgrade to MariaDB Enterprise Server 11.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrades/upgrade-to-mariadb-enterprise-server-11.4)
* [Upgrade from MariaDB Community Server to MariaDB Enterprise Server 11.4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/upgrading/upgrading-mariadb-community-server-to-enterprise-server/upgrade-from-mariadb-community-server-to-mariadb-enterprise-server-11.4)

## What's new in older release series?

* [What's New in MariaDB Enterprise Server 10.6?](../10.6/whats-new.md)
* [What's New in MariaDB Enterprise Server 10.5?](../old-releases/10-5/whats-new-in-mariadb-enterprise-server-10-5.md)
* [What's New in MariaDB Enterprise Server 10.4?](../old-releases/10-4/whats-new-in-mariadb-enterprise-server-10-4.md)
* [What's New in MariaDB Enterprise Server 10.3?](../old-releases/10-3/whats-new-in-mariadb-enterprise-server-10-3.md)
* [What's New in MariaDB Enterprise Server 10.2?](../old-releases/10-2/whats-new-in-mariadb-enterprise-server-10-2.md)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
