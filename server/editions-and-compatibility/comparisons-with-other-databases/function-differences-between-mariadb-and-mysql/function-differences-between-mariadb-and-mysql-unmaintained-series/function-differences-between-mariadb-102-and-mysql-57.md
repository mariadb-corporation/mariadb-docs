# Function Differences Between MariaDB 10.2 and MySQL 5.7

The following is a list of all function differences between [MariaDB 10.2]({release-notes}/community-server/old-releases/10.2/what-is-mariadb-102) and MySQL 5.7. It is based on functions available in the stable versions MySQL 5.7.18 and [MariaDB 10.2.38]({release-notes}/community-server/old-releases/10.2/10.2.38).

For a description of all differences, see [Incompatibilities and Feature Differences Between MariaDB 10.2 and MySQL 5.7](../../incompatibilities-and-feature-differences-between-mariadb-and-mysql-unmaint/incompatibilities-and-feature-differences-between-mariadb-10-2-and-mysql-5.md).

## Present in MariaDB Only

### Dynamic columns

* [COLUMN\_ADD](../../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_add.md)
* [COLUMN\_CHECK](../../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_check.md)
* [COLUMN\_CREATE](../../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_create.md)
* [COLUMN\_DELETE](../../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_delete.md)
* [COLUMN\_EXISTS](../../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_exists.md)
* [COLUMN\_GET](../../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_get.md)
* [COLUMN\_JSON](../../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_json.md)
* [COLUMN\_LIST](../../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_list.md)

### JSON

* [JSON\_COMPACT](../../../../reference/sql-functions/special-functions/json-functions/json_compact.md)
* [JSON\_DETAILED](../../../../reference/sql-functions/special-functions/json-functions/json_detailed.md)
* [JSON\_EXISTS](../../../../reference/sql-functions/special-functions/json-functions/json_exists.md)
* [JSON\_LOOSE](../../../../reference/sql-functions/special-functions/json-functions/json_loose.md)
* [JSON\_MERGE\_PATCH](../../../../reference/sql-functions/special-functions/json-functions/json_merge_patch.md)
* [JSON\_MERGE\_PRESERVE](../../../../reference/sql-functions/special-functions/json-functions/json_merge_preserve.md)
* [JSON\_QUERY](../../../../reference/sql-functions/special-functions/json-functions/json_query.md)
* [JSON\_VALUE](../../../../reference/sql-functions/special-functions/json-functions/json_value.md)

### Regular Expressions

* [REGEXP\_INSTR](../../../../reference/sql-functions/string-functions/regular-expressions-functions/regexp_instr.md)
* [REGEXP\_REPLACE](../../../../reference/sql-functions/string-functions/regular-expressions-functions/regexp_replace.md)
* [REGEXP\_SUBSTR](../../../../reference/sql-functions/string-functions/regular-expressions-functions/regexp_substr.md)

### Window Functions

* [CUME\_DIST](../../../../reference/sql-functions/special-functions/window-functions/cume_dist.md)
* [DENSE\_RANK](../../../../reference/sql-functions/special-functions/window-functions/dense_rank.md)
* [LAG](../../../../reference/sql-functions/special-functions/window-functions/lead.md)
* [LAST\_VALUE](../../../../reference/sql-functions/secondary-functions/information-functions/last_value.md)
* [LEAD](../../../../reference/sql-functions/special-functions/window-functions/lead.md)
* [NTH\_VALUE](../../../../reference/sql-functions/special-functions/window-functions/nth_value.md)
* [NTILE](../../../../reference/sql-functions/special-functions/window-functions/ntile.md)
* [PERCENT\_RANK](../../../../reference/sql-functions/special-functions/window-functions/percent_rank.md)
* [RANK](../../../../reference/sql-functions/special-functions/window-functions/rank.md)
* [ROW\_NUMBER](../../../../reference/sql-functions/special-functions/window-functions/row_number.md)

## Present in MySQL Only

### GTID

MariaDB and MySQL have differing [GTID](../../../../ha-and-performance/standard-replication/gtid/README.md) implementations.

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

* [Incompatibilities and Feature Differences Between MariaDB 10.2 and MySQL 5.7](../../incompatibilities-and-feature-differences-between-mariadb-and-mysql-unmaint/incompatibilities-and-feature-differences-between-mariadb-10-2-and-mysql-5.md)
* [System Variable Differences Between MariaDB 10.2 and MySQL 5.7](../../system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-and-mysql-unmaintained-series/system-variable-differences-between-mariadb-10-2-and-mysql-5-7.md)
* [Function Differences Between MariaDB 10.3 and MySQL 5.7](function-differences-between-mariadb-103-and-mysql-57.md)
* [Function Differences Between MariaDB 10.2 and MySQL 5.6](function-differences-between-mariadb-102-and-mysql-56.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formid="4316" formId="4316" %}
