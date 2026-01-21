---
description: >-
  Answers to common questions about AUTO_INCREMENT. Learn about gaps in
  sequences, resetting values, and behavior in different storage engines.
---

# AUTO\_INCREMENT FAQ

## How do I get the last inserted auto\_increment value?

Use the [LAST\_INSERT\_ID()](../sql-functions/secondary-functions/information-functions/last_insert_id.md) function:

```sql
SELECT LAST_INSERT_ID();
```

## What if someone else inserts before I select my id?

[LAST\_INSERT\_ID()](../sql-functions/secondary-functions/information-functions/last_insert_id.md) is connection specific, so there is no problem from race conditions.

## How do I get the next value to be inserted?

You don't. Insert, then find out what you did with [LAST\_INSERT\_ID()](../sql-functions/secondary-functions/information-functions/last_insert_id.md).

## How do I change what number auto\_increment starts with?

Run a query, `ALTER TABLE yourTable AUTO_INCREMENT = x;` . The next insert will contain `x` or `MAX(autoField) + 1`, whichever is higher.

As an alternative, run `INSERT INTO yourTable (autoField) VALUES (x);` . The next insert will contain `x+1` or `MAX(autoField) + 1`, whichever is higher.

Issuing [TRUNCATE TABLE](../sql-statements/table-statements/truncate-table.md) will delete all the rows in the table, and will reset the auto\_increment value to 0 in most cases.

## How do I renumber rows once I deleted some in the middle?

Typically, you don't want to. Gaps are hardly ever a problem; if your application can't handle gaps in the sequence, you probably should rethink your application.

## Can I do group-wise auto\_increment?

Yes, if you use the [MyISAM engine](../../server-usage/storage-engines/myisam-storage-engine/).

## How do I get the AUTO\_INCREMENT value in a BEFORE INSERT trigger?

This isn't possible. It's only available after insert.

## How do I assign two fields the same auto\_increment value in one query?

You can't, not even with an `AFTER INSERT` trigger. Insert, then go back and update using `LAST_INSERT_ID()`. Those two statements could be wrapped into one stored procedure if you wish.

However, you can mimic this behavior with a `BEFORE INSERT` trigger and a second table to store the sequence position:

```sql
CREATE TABLE sequence (table_name VARCHAR(255), position INT UNSIGNED);
INSERT INTO sequence VALUES ('testTable', 0);
CREATE TABLE testTable (firstAuto INT UNSIGNED, secondAuto INT UNSIGNED);
DELIMITER //
CREATE TRIGGER testTable_BI BEFORE INSERT ON testTable FOR EACH ROW BEGIN
  UPDATE sequence SET position = LAST_INSERT_ID(position + 1) WHERE table_name = 'testTable';
  SET NEW.firstAuto = LAST_INSERT_ID();
  SET NEW.secondAuto = LAST_INSERT_ID();
END//
DELIMITER ;
INSERT INTO testTable VALUES (NULL, NULL), (NULL, NULL);
SELECT * FROM testTable;

+-----------+------------+
| firstAuto | secondAuto |
+-----------+------------+
|         1 |          1 |
|         2 |          2 |
+-----------+------------+
```

The same sequence table can maintain separate sequences for multiple tables (or separate sequences for different fields in the same table) by adding extra rows.

## Does the auto\_increment field have to be primary key?

No, it only has to be indexed. It doesn't even have to be unique.

## How does InnoDB handle AUTO\_INCREMENT?

See [AUTO\_INCREMENT handling in InnoDB](../../server-usage/storage-engines/innodb/auto_increment-handling-in-innodb.md).

## General Information To Read

[AUTO\_INCREMENT](auto_increment.md)

## Manual Notes

There can be only one `AUTO_INCREMENT` column per table, it must be indexed, and it cannot have a `DEFAULT` value. An `AUTO_INCREMENT` column works properly only if it contains only positive values. Inserting a negative number is regarded as inserting a very large positive number. This is done to avoid precision problems when numbers wrap over from positive to negative and also to ensure that you do not accidentally get an `AUTO_INCREMENT` column that contains 0.

## How to start a table with a set AUTO\_INCREMENT value?

```sql
CREATE TABLE autoinc_test (
  h INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, 
  m INT UNSIGNED 
) AUTO_INCREMENT = 100;

INSERT INTO autoinc_test ( m ) VALUES ( 1 );

SELECT * FROM autoinc_test;
+-----+------+
| h   | m    |
+-----+------+
| 100 |    1 |
+-----+------+
```

## See Also

* [AUTO\_INCREMENT](auto_increment.md)
* [AUTO\_INCREMENT handling in XtraDB/InnoDB](../../server-usage/storage-engines/innodb/auto_increment-handling-in-innodb.md)
* [LAST\_INSERT\_ID()](../sql-functions/secondary-functions/information-functions/last_insert_id.md)
* [BLACKHOLE and AUTO\_INCREMENT](../../server-usage/storage-engines/blackhole.md#blackhole-and-auto_increment)
* [Sequences](../sql-structure/sequences/) - an alternative to `AUTO_INCREMENT`

_The initial version of this article was copied, with permission, from_ [_Autoincrement\_FAQ_](https://hashmysql.org/wiki/Autoincrement_FAQ) _on 2012-10-05._

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
