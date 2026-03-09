# Function Differences Between MariaDB 10.2 and MySQL 5.6

The following is a list of all function differences between [MariaDB 10.2](../../../../old-releases/10.2/what-is-mariadb-102.md) and MySQL 5.6. It is based on functions available in the stable version [MariaDB 10.2.25](../../../../old-releases/10.2/10.2.25.md).

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

### JSON

* [JSON\_ARRAY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_array)
* [JSON\_ARRAY\_APPEND](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_array_append)
* [JSON\_ARRAY\_INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_array_insert)
* [JSON\_COMPACT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_compact)
* [JSON\_CONTAINS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_contains)
* [JSON\_CONTAINS\_PATH](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_contains_path)
* [JSON\_DEPTH](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_depth)
* [JSON\_DETAILED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_detailed)
* [JSON\_EXISTS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_exists)
* [JSON\_EXTRACT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_extract)
* [JSON\_INSERT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_insert)
* [JSON\_KEYS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_keys)
* [JSON\_LENGTH](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_length)
* [JSON\_LOOSE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_loose)
* [JSON\_MERGE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_merge)
* [JSON\_MERGE\_PATCH](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_merge_patch)
* [JSON\_MERGE\_PRESERVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_merge_preserve)
* [JSON\_OBJECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_object)
* [JSON\_QUERY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_query)
* [JSON\_QUOTE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_quote)
* [JSON\_REMOVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_remove)
* [JSON\_REPLACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_replace)
* [JSON\_SEARCH](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_search)
* [JSON\_SET](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_set)
* [JSON\_TYPE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_type)
* [JSON\_UNQUOTE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_unquote)
* [JSON\_VALID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_valid)
* [JSON\_VALUE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_value)

### Regular Expressions

* [REGEXP\_INSTR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/regexp_instr)
* [REGEXP\_REPLACE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/regexp_replace)
* [REGEXP\_SUBSTR](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/regular-expressions-functions/regexp_substr)

### Window Functions

* [CUME\_DIST](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/cume_dist)
* [DENSE\_RANK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/dense_rank)
* [LAG](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/lead)
* [LAST\_VALUE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/information-functions/last_value)
* [LEAD](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/lead)
* [NTH\_VALUE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/nth_value)
* [NTILE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/ntile)
* [PERCENT\_RANK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/percent_rank)
* [RANK](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/rank)
* [ROW\_NUMBER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/window-functions/row_number)

## Present in MySQL Only

### GTID

MariaDB and MySQL have differing [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) implementations.

* GTID\_SUBSET
* GTID\_SUBTRACT
* SQL\_THREAD\_WAIT\_AFTER\_GTIDS()
* WAIT\_UNTIL\_SQL\_THREAD\_AFTER\_GTIDS()

### Miscellaneous

* RANDOM\_BYTES
* VALIDATE\_PASSWORD\_STRENGTH

## See Also

* [Function Differences Between MariaDB 10.2 and MySQL 5.7](function-differences-between-mariadb-102-and-mysql-57.md)
* [System Variable Differences Between MariaDB 10.2 and MySQL 5.6](../../system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-and-mysql-unmaintained-series/system-variable-differences-between-mariadb-10-2-and-mysql-5-6.md)
* [MariaDB versus MySQL - Compatibility](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/compatibility-and-differences/function-differences-between-mariadb-and-mysql/function-differences-between-mariadb-and-mysql-unmaintained-series/broken-reference/README.md)
* [MariaDB versus MySQL - Features](../../mariadb-vs-mysql-features.md)

{% @marketo/form formid="4316" formId="4316" %}
