# Function Differences Between MariaDB 10.3 and MySQL 5.7

The following is a list of all function differences between [MariaDB 10.3](../../../../old-releases/10.3/what-is-mariadb-103.md) and MySQL 5.7. It is based on functions available in the stable versions MySQL 5.7.18 and [MariaDB 10.3.29](../../../../old-releases/10.3/10.3.29.md).

For a description of all differences, see [Incompatibilities and Feature Differences Between MariaDB 10.3 and MySQL 5.7](../../incompatibilities-and-feature-differences-between-mariadb-and-mysql-unmaint/compatibility-differences-incompatibilities-and-feature-differences-between.md).

## Present in MariaDB Only

### Dynamic Columns

* [COLUMN\_ADD](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/dynamic-columns-functions/column_add)
* [COLUMN\_CHECK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/dynamic-columns-functions/column_check)
* [COLUMN\_CREATE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/dynamic-columns-functions/column_create)
* [COLUMN\_DELETE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/dynamic-columns-functions/column_delete)
* [COLUMN\_EXISTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/dynamic-columns-functions/column_exists)
* [COLUMN\_GET](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/dynamic-columns-functions/column_get)
* [COLUMN\_JSON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/dynamic-columns-functions/column_json)
* [COLUMN\_LIST](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/dynamic-columns-functions/column_list)

### General

* [CHR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/chr)
* [DECODE\_ORACLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/decode)
* [LENGTHB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/lengthb)
* [NVL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/control-flow-functions/ifnull) (Synonym for IFNULL)
* [NVL2](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/control-flow-functions/nvl2)
* [TRIM\_ORACLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/trim)
* [VALUE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/miscellaneous-functions/values-value) - the VALUES() function was renamed after MariaDB introduced Table Value Constructors.

### JSON

* [JSON\_COMPACT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_compact)
* [JSON\_DETAILED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_detailed)
* [JSON\_EXISTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_exists)
* [JSON\_LOOSE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_loose)
* [JSON\_MERGE\_PATCH](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_merge_patch)
* [JSON\_MERGE\_PRESERVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_merge_preserve)
* [JSON\_QUERY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_query)
* [JSON\_VALUE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_value)

### Regular Expressions

* [REGEXP\_INSTR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/regexp_instr)
* [REGEXP\_REPLACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/regexp_replace)
* [REGEXP\_SUBSTR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/regexp_substr)

### Sequences

* [LASTVAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/sequence-functions/previous-value-for-sequence_name)
* [NEXTVAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/sequence-functions/next-value-for-sequence_name)
* [SETVAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/sequences/sequence-functions/setval)

### Window Functions

* [CUME\_DIST](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/cume_dist)
* [DENSE\_RANK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/dense_rank)
* [LAG](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/lead)
* [LAST\_VALUE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/information-functions/last_value)
* [LEAD](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/lead)
* [MEDIAN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/median)
* [NTH\_VALUE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/nth_value)
* [NTILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/ntile)
* [PERCENT\_RANK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/percent_rank)
* [PERCENTILE\_CONT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/percentile_cont)
* [PERCENTILE\_DISC](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/percentile_disc)
* [RANK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/rank)
* [ROW\_NUMBER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/row_number)

## Present in MySQL Only

### GTID

MariaDB and MySQL have differing [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) implementations.

* GTID\_SUBSET
* GTID\_SUBTRACT
* WAIT\_FOR\_EXECUTED\_GTID\_SET
* WAIT\_UNTIL\_SQL\_THREAD\_AFTER\_GTIDS()

### Geographic

* DISTANCE
* MBRCOVEREDBY
* ST\_BUFFER\_STRATEGY
* ST\_GeoHash
* ST\_IsValid
* ST\_LatFromGeoHash
* ST\_LongFromGeoHash
* ST\_PointFromGeoHash
* ST\_SIMPLIFY
* ST\_VALIDATE

### Miscellaneous

* ANY\_VALUE
* RANDOM\_BYTES
* RELEASE\_ALL\_LOCKS
* VALIDATE\_PASSWORD\_STRENGTH

## See Also

* [Incompatibilities and Feature Differences Between MariaDB 10.3 and MySQL 5.7](../../incompatibilities-and-feature-differences-between-mariadb-and-mysql-unmaint/compatibility-differences-incompatibilities-and-feature-differences-between.md)
* [System Variable Differences Between MariaDB 10.3 and MySQL 5.7](../../system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-and-mysql-unmaintained-series/system-variable-differences-between-mariadb-10-3-and-mysql-5-7.md)
* [Function Differences Between MariaDB 10.2 and MySQL 5.7](function-differences-between-mariadb-102-and-mysql-57.md)

{% @marketo/form formid="4316" formId="4316" %}
