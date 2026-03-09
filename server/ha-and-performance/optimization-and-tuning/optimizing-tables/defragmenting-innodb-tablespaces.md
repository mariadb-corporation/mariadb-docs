# Defragmenting InnoDB Tablespaces

## Overview

When rows are deleted from an [InnoDB](../../../server-usage/storage-engines/innodb/) table, the rows are simply marked as deleted and not physically deleted. The free space is not returned to the operating system for re-use.

The purge thread will physically delete index keys and rows, but the free space introduced is still not returned to operating system. This can lead to gaps in the pages. If you have variable length rows, new rows may be larger than old rows and cannot make use of the available space.

You can run [OPTIMIZE TABLE](optimize-table.md) or [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/)

[ENGINE=InnoDB](../../../reference/sql-statements/data-definition/alter/alter-table/) to reconstruct the table. Unfortunately running `OPTIMIZE TABLE` against an InnoDB table stored in the shared table-space file `ibdata1` does two things:

* Makes the table’s data and indexes contiguous inside `ibdata1`.
* Increases the size of `ibdata1` because the contiguous data and index pages are appended to `ibdata1`.

## InnoDB Defragmentation

The feature described below has been deprecated in [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.0/what-is-mariadb-110) and was removed in [MariaDB 11.1.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/11.1/11.1.0). See [MDEV-30544](https://jira.mariadb.org/browse/MDEV-30544) and [MDEV-30545](https://jira.mariadb.org/browse/MDEV-30545).

[MariaDB 10.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.1/changes-improvements-in-mariadb-10-1) merged Facebook's defragmentation code prepared for MariaDB by Matt, Seong Uck Lee from Kakao. The only major difference to Facebook's code and Matt’s patch is that MariaDB does not introduce new literals to SQL and makes no changes to the server code. Instead, [OPTIMIZE TABLE](optimize-table.md) is used and all code changes are inside the InnoDB/XtraDB storage engines.

The behaviour of `OPTIMIZE TABLE` is unchanged by default, and to enable this new feature, you need to set the [innodb\_defragment](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_defragment) system variable to `1`.

```
[mysqld]
...
innodb-defragment=1
```

No new tables are created and there is no need to copy data from old tables to new tables. Instead, this feature loads `n` pages (determined by [innodb-defragment-n-pages](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_n_pages)) and tries to move records so that pages would be full of records and then frees pages that are fully empty after the operation.

Note that tablespace files (including ibdata1) will not shrink as the result of defragmentation, but one will get better memory utilization in the InnoDB buffer pool as there are fewer data pages in use.

A number of new system and status variables for controlling and monitoring the feature are introduced.

### System Variables

* [innodb\_defragment](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_defragment): Enable InnoDB defragmentation.
* [innodb\_defragment\_n\_pages](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_n_pages): Number of pages considered at once when merging multiple pages to defragment.
* [innodb\_defragment\_stats\_accuracy](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_stats_accuracy): Number of defragment stats changes there are before the stats are written to persistent storage.
* [innodb\_defragment\_fill\_factor\_n\_recs](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_fill_factor_n_recs): Number of records of space that defragmentation should leave on the page.
* [innodb\_defragment\_fill\_factor](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_fill_factor): Indicates how full defragmentation should fill a page.
* [innodb\_defragment\_frequency](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_frequency): Maximum times per second for defragmenting a single index.

### Status Variables

* [Innodb\_defragment\_compression\_failures](../system-variables/innodb-status-variables.md#innodb_defragment_compression_failures): Number of defragment re-compression failures
* [Innodb\_defragment\_failures](../system-variables/innodb-status-variables.md#innodb_defragment_failures): Number of defragment failures.
* [Innodb\_defragment\_count](../system-variables/innodb-status-variables.md#innodb_defragment_count): Number of defragment operations.

## Example

```sql
SET @@global.innodb_file_per_table = 1;
SET @@global.innodb_defragment_n_pages = 32;
SET @@global.innodb_defragment_fill_factor = 0.95;
CREATE TABLE tb_defragment (
pk1 BIGINT(20) NOT NULL,
pk2 BIGINT(20) NOT NULL,
fd4 TEXT,
fd5 VARCHAR(50) DEFAULT NULL,
PRIMARY KEY (pk1),
KEY ix1 (pk2)
) ENGINE=InnoDB;
 
DELIMITER //
CREATE PROCEDURE innodb_insert_proc (repeat_count INT)
BEGIN
  DECLARE current_num INT;
  SET current_num = 0;
  WHILE current_num < repeat_count DO
    INSERT INTO tb_defragment VALUES (current_num, 1, REPEAT('Abcdefg', 20), REPEAT('12345',5));
    INSERT INTO tb_defragment VALUES (current_num+1, 2, REPEAT('HIJKLM', 20), REPEAT('67890',5));
    INSERT INTO tb_defragment VALUES (current_num+2, 3, REPEAT('HIJKLM', 20), REPEAT('67890',5));
    INSERT INTO tb_defragment VALUES (current_num+3, 4, REPEAT('HIJKLM', 20), REPEAT('67890',5));
    SET current_num = current_num + 4;
  END WHILE;
END//
DELIMITER ;
COMMIT;
 
SET autocommit=0;
CALL innodb_insert_proc(50000);
COMMIT;
SET autocommit=1;
```

After these CREATE and INSERT operations, the following information can be seen from the INFORMATION SCHEMA:

```sql
SELECT COUNT(*) AS Value FROM information_schema.innodb_buffer_page 
  WHERE table_name LIKE '%tb_defragment%' AND index_name = 'PRIMARY';
Value
313
 
SELECT COUNT(*) AS Value FROM information_schema.innodb_buffer_page 
  WHERE table_name LIKE '%tb_defragment%' AND index_name = 'ix1';
Value
72
 
SELECT COUNT(stat_value) FROM mysql.innodb_index_stats 
  WHERE table_name LIKE '%tb_defragment%' AND stat_name IN ('n_pages_freed');
COUNT(stat_value)
0
 
SELECT COUNT(stat_value) FROM mysql.innodb_index_stats 
  WHERE table_name LIKE '%tb_defragment%' AND stat_name IN ('n_page_split');
COUNT(stat_value)
0
 
SELECT COUNT(stat_value) FROM mysql.innodb_index_stats 
  WHERE table_name LIKE '%tb_defragment%' AND stat_name IN ('n_leaf_pages_defrag');
COUNT(stat_value)
0
 
SELECT table_name, data_free/1024/1024 AS data_free_MB, table_rows FROM information_schema.tables 
  WHERE engine LIKE 'InnoDB' AND table_name LIKE '%tb_defragment%';
TABLE_NAME data_free_MB table_rows
tb_defragment 4.00000000 50051
 
SELECT table_name, index_name, SUM(number_records), SUM(data_size) FROM information_schema.innodb_buffer_page 
  WHERE table_name LIKE '%tb_defragment%' AND index_name LIKE 'PRIMARY';
TABLE_NAME index_name SUM(number_records) SUM(data_size)
`test`.`tb_defragment` PRIMARY 25873 4739939
 
SELECT table_name, index_name, SUM(number_records), SUM(data_size) FROM information_schema.innodb_buffer_page 
  WHERE table_name LIKE '%tb_defragment%' AND index_name LIKE 'ix1';
TABLE_NAME index_name SUM(number_records) SUM(data_size)
`test`.`tb_defragment` ix1 50071 1051775
```

Deleting three-quarters of the records, leaving gaps, and then optimizing:

```sql
DELETE FROM tb_defragment WHERE pk2 BETWEEN 2 AND 4;
 
OPTIMIZE TABLE tb_defragment;
TABLE	Op	Msg_type	Msg_text
test.tb_defragment	OPTIMIZE	status	OK
SHOW status LIKE '%innodb_def%';
Variable_name	Value
Innodb_defragment_compression_failures	0
Innodb_defragment_failures	1
Innodb_defragment_count	4
```

Now some pages have been freed, and some merged:

```sql
SELECT COUNT(*) AS Value FROM information_schema.innodb_buffer_page 
  WHERE table_name LIKE '%tb_defragment%' AND index_name = 'PRIMARY';
Value
0
 
SELECT COUNT(*) AS Value FROM information_schema.innodb_buffer_page 
  WHERE table_name LIKE '%tb_defragment%' AND index_name = 'ix1';
Value
0
 
SELECT COUNT(stat_value) FROM mysql.innodb_index_stats 
  WHERE table_name LIKE '%tb_defragment%' AND stat_name IN ('n_pages_freed');
COUNT(stat_value)
2
 
SELECT COUNT(stat_value) FROM mysql.innodb_index_stats 
  WHERE table_name LIKE '%tb_defragment%' AND stat_name IN ('n_page_split');
COUNT(stat_value)
2
 
SELECT COUNT(stat_value) FROM mysql.innodb_index_stats 
  WHERE table_name LIKE '%tb_defragment%' AND stat_name IN ('n_leaf_pages_defrag');
COUNT(stat_value)
2
 
SELECT table_name, data_free/1024/1024 AS data_free_MB, table_rows FROM information_schema.tables 
  WHERE engine LIKE 'InnoDB';
TABLE_NAME data_free_MB table_rows
innodb_index_stats 0.00000000 8
innodb_table_stats 0.00000000 0
tb_defragment 4.00000000 12431
 
SELECT table_name, index_name, SUM(number_records), SUM(data_size) FROM information_schema.innodb_buffer_page 
  WHERE table_name LIKE '%tb_defragment%' AND index_name LIKE 'PRIMARY';
TABLE_NAME index_name SUM(number_records) SUM(data_size)
`test`.`tb_defragment` PRIMARY 690 102145
 
SELECT table_name, index_name, SUM(number_records), SUM(data_size) FROM information_schema.innodb_buffer_page 
  WHERE table_name LIKE '%tb_defragment%' AND index_name LIKE 'ix1';
TABLE_NAME index_name SUM(number_records) SUM(data_size)
`test`.`tb_defragment` ix1 5295 111263
```

See [Defragmenting unused space on InnoDB tablespace](https://blog.mariadb.org/defragmenting-unused-space-on-innodb-tablespace/) on the Mariadb.org blog for more details.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
