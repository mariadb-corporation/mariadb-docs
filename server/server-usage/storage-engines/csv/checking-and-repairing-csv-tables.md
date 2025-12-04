---
description: >-
  Learn how to use CHECK TABLE and REPAIR TABLE to identify and fix corruptions
  in CSV tables, discarding rows from the first error onwards.
---

# Checking and Repairing CSV Tables

[CSV tables](./) support the [CHECK TABLE](../../../reference/sql-statements/table-statements/check-table.md) and [REPAIR TABLE](../../../reference/sql-statements/table-statements/repair-table.md) statements.

`CHECK TABLE` marks the table as corrupt if it finds a problem, while `REPAIR TABLE` restores rows until the first corrupted row, discarding the rest.

## Examples

```sql
CREATE TABLE csv_test (
  x INT NOT NULL, y DATE NOT NULL, z CHAR(10) NOT NULL
  ) ENGINE=CSV;

INSERT INTO csv_test VALUES
    (1,CURDATE(),'one'),
    (2,CURDATE(),'two'),
    (3,CURDATE(),'three');
```

```sql
SELECT * FROM csv_test;
+---+------------+-------+
| x | y          | z     |
+---+------------+-------+
| 1 | 2013-07-08 | one   |
| 2 | 2013-07-08 | two   |
| 3 | 2013-07-08 | three |
+---+------------+-------+
```

Using an editor, the actual file will look as follows

```bash
$ cat csv_test.CSV
1,"2013-07-08","one"
2,"2013-07-08","two"
3,"2013-07-08","three"
```

Let's introduce some corruption with an unwanted quote in the 2nd row:

```
1,"2013-07-08","one"
2","2013-07-08","two"
3,"2013-07-08","three"
```

```sql
CHECK TABLE csv_test;
+---------------+-------+----------+----------+
| Table         | Op    | Msg_type | Msg_text |
+---------------+-------+----------+----------+
| test.csv_test | check | error    | Corrupt  |
+---------------+-------+----------+----------+
```

We can repair this, but all rows from the corrupt row onwards are lost:

```sql
REPAIR TABLE csv_test;
+---------------+--------+----------+----------------------------------------+
| Table         | Op     | Msg_type | Msg_text                               |
+---------------+--------+----------+----------------------------------------+
| test.csv_test | repair | Warning  | Data truncated for column 'x' at row 2 |
| test.csv_test | repair | status   | OK                                     |
+---------------+--------+----------+----------------------------------------+

SELECT * FROM csv_test;
+---+------------+-----+
| x | y          | z   |
+---+------------+-----+
| 1 | 2013-07-08 | one |
+---+------------+-----+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
