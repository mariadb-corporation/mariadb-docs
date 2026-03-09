---
description: >-
  Complete SHOW INDEX reference: SHOW {INDEX|INDEXES|KEYS} FROM tbl_name syntax,
  output fields (Key_name, Seq_in_index, Cardinality), and WHERE/LIKE filters.
---

# SHOW INDEX

## Syntax

```sql
SHOW {INDEX | INDEXES | KEYS} 
 FROM tbl_name [FROM db_name]
 [WHERE expr]
```

## Description

`SHOW INDEX` returns table index information. The format resembles that of the SQLStatistics call in ODBC.

You can use `db_name.tbl_name` as an alternative to the`tbl_name FROM db_name` syntax. These two statements are equivalent:

```sql
SHOW INDEX FROM mytable FROM mydb;
SHOW INDEX FROM mydb.mytable;
```

`SHOW KEYS` and `SHOW INDEXES` are synonyms for `SHOW INDEX`.

You can also list a table's indexes with the [mariadb-show](../../../../clients-and-utilities/administrative-tools/mariadb-show.md) command:

```sql
mariadb-show -k db_name tbl_name
```

The [information\_schema.STATISTICS](../../../system-tables/information-schema/information-schema-tables/information-schema-statistics-table.md) table stores similar information.

The following fields are returned by `SHOW INDEX`.

| Field          | Description                                                                                                                                                                                                                                                                                                                 |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Table          | Table name                                                                                                                                                                                                                                                                                                                  |
| Non\_unique    | 1 if the index permits duplicate values, 0 if values must be unique.                                                                                                                                                                                                                                                        |
| Key\_name      | Index name. The primary key is always named PRIMARY.                                                                                                                                                                                                                                                                        |
| Seq\_in\_index | The column's sequence in the index, beginning with 1.                                                                                                                                                                                                                                                                       |
| Column\_name   | Column name.                                                                                                                                                                                                                                                                                                                |
| Collation      | Either A, if the column is sorted in ascending order in the index, or NULL if it's not sorted.                                                                                                                                                                                                                              |
| Cardinality    | Estimated number of unique values in the index. The cardinality statistics are calculated at various times, and can help the optimizer make improved decisions.                                                                                                                                                             |
| Sub\_part      | NULL if the entire column is included in the index, or the number of included characters if not.                                                                                                                                                                                                                            |
| Packed         | NULL if the index is not packed, otherwise how the index is packed.                                                                                                                                                                                                                                                         |
| Null           | NULL if NULL values are permitted in the column, an empty string if NULLs are not permitted.                                                                                                                                                                                                                                |
| Index\_type    | The index type, which can be BTREE, FULLTEXT, HASH or RTREE. See [Storage Engine Index Types](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/storage-engine-index-types.md).                                                                                                               |
| Comment        | Other information, such as whether the index is disabled.                                                                                                                                                                                                                                                                   |
| Index\_comment | Contents of the COMMENT attribute when the index was created.                                                                                                                                                                                                                                                               |
| Ignored        | Whether or not an index will be ignored by the optimizer. See [Ignored Indexes](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/ignored-indexes.md). From [MariaDB 10.6.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/mariadb-1060-release-notes). |

The `WHERE` and `LIKE` clauses can be given to select rows using more general conditions, as discussed in [Extended SHOW](extended-show.md).

## Examples

```sql
CREATE TABLE IF NOT EXISTS `employees_example` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(30) NOT NULL,
  `last_name` VARCHAR(40) NOT NULL,
  `position` VARCHAR(25) NOT NULL,
  `home_address` VARCHAR(50) NOT NULL,
  `home_phone` VARCHAR(12) NOT NULL,
  `employee_code` VARCHAR(25) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `employee_code` (`employee_code`),
  KEY `first_name` (`first_name`,`last_name`)
) ENGINE=Aria;

INSERT INTO `employees_example` (`first_name`, `last_name`, `position`, `home_address`, `home_phone`, `employee_code`)
  VALUES
  ('Mustapha', 'Mond', 'Chief Executive Officer', '692 Promiscuous Plaza', '326-555-3492', 'MM1'),
  ('Henry', 'Foster', 'Store Manager', '314 Savage Circle', '326-555-3847', 'HF1'),
  ('Bernard', 'Marx', 'Cashier', '1240 Ambient Avenue', '326-555-8456', 'BM1'),
  ('Lenina', 'Crowne', 'Cashier', '281 Bumblepuppy Boulevard', '328-555-2349', 'LC1'),
  ('Fanny', 'Crowne', 'Restocker', '1023 Bokanovsky Lane', '326-555-6329', 'FC1'),
  ('Helmholtz', 'Watson', 'Janitor', '944 Soma Court', '329-555-2478', 'HW1');
```

```sql
SHOW INDEXES FROM employees_example\G
*************************** 1. row ***************************
        Table: employees_example
   Non_unique: 0
     Key_name: PRIMARY
 Seq_in_index: 1
  Column_name: id
    Collation: A
  Cardinality: 6
     Sub_part: NULL
       Packed: NULL
         Null: 
   Index_type: BTREE
      Comment: 
Index_comment: 
      Ignored: NO
*************************** 2. row ***************************
        Table: employees_example
   Non_unique: 0
     Key_name: employee_code
 Seq_in_index: 1
  Column_name: employee_code
    Collation: A
  Cardinality: 6
     Sub_part: NULL
       Packed: NULL
         Null: 
   Index_type: BTREE
      Comment: 
Index_comment: 
      Ignored: NO
*************************** 3. row ***************************
        Table: employees_example
   Non_unique: 1
     Key_name: first_name
 Seq_in_index: 1
  Column_name: first_name
    Collation: A
  Cardinality: NULL
     Sub_part: NULL
       Packed: NULL
         Null: 
   Index_type: BTREE
      Comment: 
Index_comment: 
      Ignored: NO
*************************** 4. row ***************************
        Table: employees_example
   Non_unique: 1
     Key_name: first_name
 Seq_in_index: 2
  Column_name: last_name
    Collation: A
  Cardinality: NULL
     Sub_part: NULL
       Packed: NULL
         Null: 
   Index_type: BTREE
      Comment: 
Index_comment: 
      Ignored: NO
```

## See Also

* [Ignored Indexes](../../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/ignored-indexes.md)
* [SHOW INDEX\_STATISTICS](show-index-statistics.md)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
