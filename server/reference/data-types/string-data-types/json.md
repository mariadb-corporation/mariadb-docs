# JSON Data Type

The JSON alias was added to make it possible to use JSON columns in [statement based](../../../server-management/server-monitoring-logs/binary-log/binary-log-formats.md#statement-based) [replication](../../../ha-and-performance/standard-replication/) from MySQL to MariaDB and to make it possible for MariaDB to read [mysqldumps](../../../clients-and-utilities/legacy-clients-and-utilities/mysqldump.md) from MySQL.

JSON is an alias for `LONGTEXT COLLATE utf8mb4_bin` introduced for compatibility reasons with MySQL's JSON data type. MariaDB implements this as a [LONGTEXT](longtext.md) rather, as the JSON data type contradicts the SQL:2016 standard, and MariaDB's benchmarks indicate that performance is at least equivalent.

In order to ensure that a valid json document is inserted, the [JSON\_VALID](../../sql-functions/special-functions/json-functions/json_valid.md) function can be used as a [CHECK constraint](../../sql-statements/data-definition/constraint.md#check-constraint-expressions). This constraint is automatically included for types using the JSON alias.

The assigned text value is retained verbatim. If a value fails JSON\_VALID(), an error is raised. This CHECK constraint can also be manually added to any LONGTEXT field. When a JSON object contains duplicate keys, only the first key-value pair is accessible via functions like JSON\_EXTRACT()

## Examples

```
CREATE TABLE t (j JSON);

DESC t;
+-------+----------+------+-----+---------+-------+
| Field | Type     | Null | Key | Default | Extra |
+-------+----------+------+-----+---------+-------+
| j     | longtext | YES  |     | NULL    |       |
+-------+----------+------+-----+---------+-------+
```

With validation:

```
CREATE TABLE t2 (
  j JSON 
  CHECK (JSON_VALID(j))
);

INSERT INTO t2 VALUES ('invalid');
ERROR 4025 (23000): CONSTRAINT `j` failed for `test`.`t2`

INSERT INTO t2 VALUES ('{"id": 1, "name": "Monty"}');
Query OK, 1 row affected (0.13 sec)
```

JSON\_Example:

```
CREATE TABLE json_example (
  description VARCHAR(20),
  example JSON
);
```

```
SHOW CREATE TABLE json_example\G
```

```
*************************** 1. row ***************************
       Table: json_example
Create Table: CREATE TABLE `json_example` (
  `description` varchar(20) DEFAULT NULL,
  `example` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`example`))
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

```
INSERT INTO json_example VALUES
  ('Array', '[ 1, 2, 3 ]'),
  ('Dictionary', '{ "a": 1, "b": 2 }'),
  ('Duplicates', '{ "a":1,"b":2, "a":3,"b": 4,"b":5}');
```

```
SELECT * FROM json_example;
```

```
+-------------+------------------------------------+
| description | example                            |
+-------------+------------------------------------+
| Array       | [ 1, 2, 3 ]                        |
| Dictionary  | { "a": 1, "b": 2 }                 |
| Duplicates  | { "a":1,"b":2, "a":3,"b": 4,"b":5} |
+-------------+------------------------------------+
```

```
SELECT description, JSON_EXTRACT(example, '$.b')
FROM json_example;
```

```
+-------------+------------------------------+
| description | JSON_EXTRACT(example, '$.b') |
+-------------+------------------------------+
| Array       | NULL                         |
| Dictionary  | 2                            |
| Duplicates  | 2                            |
+-------------+------------------------------+
```

```
INSERT INTO json_example VALUES
  ('Invalid', '{');
```

```
ERROR 4025 (23000): CONSTRAINT `json_example.example` failed for `test`.`json_example`
```

## Replicating JSON Data Between MySQL and MariaDB

The JSON type in MySQL stores the JSON object in a compact form, not as [LONGTEXT](longtext.md) as in MariaDB.\
This means that row based replication will not work for JSON types from MySQL to MariaDB.

There are a few different ways to solve this:

* Use statement based replication.
* Change the JSON column to type TEXT in MySQL
* If you must use row-based replication and cannot change the MySQL master from JSON to TEXT, you can try to introduce an intermediate MySQL slave and change the column type from JSON to TEXT on it. Then you replicate from this intermediate slave to MariaDB.

## Converting a MySQL TABLE with JSON Fields to MariaDB

MariaDB can't directly access MySQL's JSON format.

There are a few different ways to move the table to MariaDB:

* From [MariaDB 10.5.7](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/mariadb-1057-release-notes), see the you can use the [mysql\_json](../../plugins/other-plugins/mysql_json.md) plugin. See [Making MariaDB understand MySQL JSON](https://mariadb.org/making-mariadb-understand-mysql-json/).
* Change the JSON column to type TEXT in MySQL. After this, MariaDB can directly use the table without any need for a dump and restore.
* [Use mysqldump to copy the table](../../../clients-and-utilities/legacy-clients-and-utilities/mysqldump.md#examples).

## Differences Between MySQL JSON Strings and MariaDB JSON Strings

* In MySQL, JSON is an object and is [compared according to json values](https://dev.mysql.com/doc/refman/8.0/en/json.html#json-comparison). In MariaDB JSON strings are normal strings and compared as strings. One exception is when using [JSON\_EXTRACT()](../../sql-functions/special-functions/json-functions/json_extract.md) in which case strings are unescaped before comparison.

## See Also

* [JSON Functions](../../sql-functions/special-functions/json-functions/)
* [CONNECT JSON Table Type](../../../server-usage/storage-engines/connect/connect-table-types/connect-json-table-type.md)
* [MDEV-9144](https://jira.mariadb.org/browse/MDEV-9144)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
