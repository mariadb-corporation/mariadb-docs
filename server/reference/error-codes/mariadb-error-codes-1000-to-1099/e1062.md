# Error 1062: Duplicate entry for key

| Error Code | SQLSTATE | Error          | Description                     |
| ---------- | -------- | -------------- | ------------------------------- |
| 1062       | 23000    | ER\_DUP\_ENTRY | Duplicate entry '%s' for key %d |

## Possible Causes and Solutions

This error occurs when a key that requires a unique value ([unique](../../../mariadb-quickstart-guides/mariadb-indexes-guide.md#unique-index) or [primary](../../../mariadb-quickstart-guides/mariadb-indexes-guide.md#primary-key)) instead receives a duplicate.\
For example:

```
CREATE TABLE t1 (
  id INT AUTO_INCREMENT PRIMARY KEY,
  f VARCHAR(10) UNIQUE
);

INSERT INTO t1 (f) VALUES ('a'),('b');

SELECT * FROM t1;
+----+------+
| id | f    |
+----+------+
|  1 | a    |
|  2 | b    |
+----+------+

INSERT INTO t1 (f) VALUES ('b'),('c');
ERROR 1062 (23000): Duplicate entry 'b' for key 'f'
```

Solve the error by either not attempting to insert a duplicate value, or not requiring the key to be unique. For example, the below replaces the unique index with an index permitting duplicates:

```
ALTER TABLE t1 DROP INDEX f, ADD INDEX (f);

INSERT INTO t1 (f) VALUES ('b'),('c');

SELECT * FROM t1;
+----+------+
| id | f    |
+----+------+
|  1 | a    |
|  2 | b    |
|  3 | b    |
|  4 | c    |
+----+------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
