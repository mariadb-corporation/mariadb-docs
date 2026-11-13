# Function Differences Between MariaDB 10.2 and MySQL 5.6

The following is a list of all function differences between [MariaDB 10.2]({release-notes}/community-server/old-releases/10.2/what-is-mariadb-102) and MySQL 5.6. It is based on functions available in the stable version [MariaDB 10.2.25]({release-notes}/community-server/old-releases/10.2/10.2.25).

## Present in MariaDB Only

### Dynamic Columns

* [COLUMN\_ADD](../../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_add.md)
* [COLUMN\_CHECK](../../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_check.md)
* [COLUMN\_CREATE](../../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_create.md)
* [COLUMN\_DELETE](../../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_delete.md)
* [COLUMN\_EXISTS](../../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_exists.md)
* [COLUMN\_GET](../../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_get.md)
* [COLUMN\_JSON](../../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_json.md)
* [COLUMN\_LIST](../../../../reference/sql-functions/special-functions/dynamic-columns-functions/column_list.md)

### JSON

* [JSON\_ARRAY](../../../../reference/sql-functions/special-functions/json-functions/json_array.md)
* [JSON\_ARRAY\_APPEND](../../../../reference/sql-functions/special-functions/json-functions/json_array_append.md)
* [JSON\_ARRAY\_INSERT](../../../../reference/sql-functions/special-functions/json-functions/json_array_insert.md)
* [JSON\_COMPACT](../../../../reference/sql-functions/special-functions/json-functions/json_compact.md)
* [JSON\_CONTAINS](../../../../reference/sql-functions/special-functions/json-functions/json_contains.md)
* [JSON\_CONTAINS\_PATH](../../../../reference/sql-functions/special-functions/json-functions/json_contains_path.md)
* [JSON\_DEPTH](../../../../reference/sql-functions/special-functions/json-functions/json_depth.md)
* [JSON\_DETAILED](../../../../reference/sql-functions/special-functions/json-functions/json_detailed.md)
* [JSON\_EXISTS](../../../../reference/sql-functions/special-functions/json-functions/json_exists.md)
* [JSON\_EXTRACT](../../../../reference/sql-functions/special-functions/json-functions/json_extract.md)
* [JSON\_INSERT](../../../../reference/sql-functions/special-functions/json-functions/json_insert.md)
* [JSON\_KEYS](../../../../reference/sql-functions/special-functions/json-functions/json_keys.md)
* [JSON\_LENGTH](../../../../reference/sql-functions/special-functions/json-functions/json_length.md)
* [JSON\_LOOSE](../../../../reference/sql-functions/special-functions/json-functions/json_loose.md)
* [JSON\_MERGE](../../../../reference/sql-functions/special-functions/json-functions/json_merge.md)
* [JSON\_MERGE\_PATCH](../../../../reference/sql-functions/special-functions/json-functions/json_merge_patch.md)
* [JSON\_MERGE\_PRESERVE](../../../../reference/sql-functions/special-functions/json-functions/json_merge_preserve.md)
* [JSON\_OBJECT](../../../../reference/sql-functions/special-functions/json-functions/json_object.md)
* [JSON\_QUERY](../../../../reference/sql-functions/special-functions/json-functions/json_query.md)
* [JSON\_QUOTE](../../../../reference/sql-functions/special-functions/json-functions/json_quote.md)
* [JSON\_REMOVE](../../../../reference/sql-functions/special-functions/json-functions/json_remove.md)
* [JSON\_REPLACE](../../../../reference/sql-functions/special-functions/json-functions/json_replace.md)
* [JSON\_SEARCH](../../../../reference/sql-functions/special-functions/json-functions/json_search.md)
* [JSON\_SET](../../../../reference/sql-functions/special-functions/json-functions/json_set.md)
* [JSON\_TYPE](../../../../reference/sql-functions/special-functions/json-functions/json_type.md)
* [JSON\_UNQUOTE](../../../../reference/sql-functions/special-functions/json-functions/json_unquote.md)
* [JSON\_VALID](../../../../reference/sql-functions/special-functions/json-functions/json_valid.md)
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
* SQL\_THREAD\_WAIT\_AFTER\_GTIDS()
* WAIT\_UNTIL\_SQL\_THREAD\_AFTER\_GTIDS()

### Miscellaneous

* RANDOM\_BYTES
* VALIDATE\_PASSWORD\_STRENGTH

## See Also

* [Function Differences Between MariaDB 10.2 and MySQL 5.7](function-differences-between-mariadb-102-and-mysql-57.md)
* [System Variable Differences Between MariaDB 10.2 and MySQL 5.6](../../system-variable-differences-between-mariadb-and-mysql/system-variable-differences-between-mariadb-and-mysql-unmaintained-series/system-variable-differences-between-mariadb-10-2-and-mysql-5-6.md)
* [MariaDB versus MySQL - Compatibility](../../mariadb-vs-mysql-compatibility.md)
* [MariaDB versus MySQL - Features](../../mariadb-vs-mysql-features.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formid="4316" formId="4316" %}
