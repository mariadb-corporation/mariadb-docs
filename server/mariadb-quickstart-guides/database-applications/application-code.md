# Application Code

Although relational database applications strive to separate application code from database data, this is only possible to a limited extent. That said, there are means to work with database and application design that make maintaining database schema and applications easier. The task at hand then, on the application side of things, is to make the application easy to maintain and as flexible as possible when it comes to integrating with the database on one hand, and on the other hand ensure that the measures taken don’t take a toll on features, functionality or performance.

## Object Relational Mappers (ORM)

Using an ORM, such as Hibernate for Java applications, makes it possible to build applications that do not rely on the lowest detail of the database schema. On the other hand, performance is sometimes an issue and, in some cases, complex relational operations might still need to be hard-coded. Despite this, hibernate is often a good way to create applications and database schemas that are easy to maintain.

## Stored Procedures and Functions

Using database stored procedures is another way of isolating database logic from application logic. One advantage here is that if applications call stored procedures instead of issuing SQL statements, then we can keep a clear differentiator between the database and backend processing and application-level processing. A disadvantage is that the connection between the backend logic and the structure of the data is still there, it is just somewhere else than in the application, but this still makes maintenance easier in many ways.

It is also common not to drive this too far, i.e. complex SQL and code that truly belongs in the backend can be in the database, whereas more basic SQL and simple SELECTs can be kept as they are in the application.

## Views

Views are useful to separate complex processing, such as advanced JOIN operations, from the application. In some cases, VIEWs introduce performance issues, but these cases are rare.

## Application Code

As for database code / SQL in applications, there are several best practices to stick to.

### SELECT \*

Avoid `SELECT *` in applications; these have several bad effects, such as assuming in the application what columns are in a table, no more and no less, and in what order. This is not a good idea. In addition, selecting more columns than necessary does affect performance and may cause the optimizer to use a non-optimal path. Note that `SELECT *` makes two assumptions: first that it assumes which columns exist in a table, and secondly, the order in which these columns are defined. Getting any of these wrong can break things unnecessarily, and using this construct in application code makes schema changes more difficult.

### INSERT Without Column Names

Just as in the case of `SELECT *`, an `INSERT` without column names, such as this ...

```sql
INSERT INTO `orders_t` VALUES(1, ‘2025-06-01 12:00:00’);
```

... is a bad idea. The proper way to write an SQL statement like this is:

```sql
INSERT INTO `orders_t`(`order_id`, `order_date`)
  VALUES(1, ‘2025-06-01 12:00:00’);
```

Not doing this may cause errors in the application if the table is changed, such as when columns are added or the order of the columns is changed.

### Processing of Column Data

When data is returned from a `SELECT` statement, it is sometimes tempting to put processing of values in the SQL statement, like this:

```sql
SELECT YEAR(`order_date`) AS `order_year` FROM `orders_t`;
```

This is not incorrect in any way and is perfectly valid, but sometimes it is better to do this processing in the application. The best is to be consistent and the issue with this kind of construct is that it sometimes makes the SQL less readable than necessary.

### Use of Reserved Words in the Schema

It is possible to use reserved words in names of schema objects and in the SQL itself, as here:

```sql
CREATE TABLE `order`(`order_id` INTEGER NOT NULL PRIMARY KEY);
```

And here:

```sql
SELECT order_id AS `order` FROM orders_t;
```

Both of these are valid constructs, but are not really recommended. The keyword order used above is likely among the most likely reserved words to use in a schema, but there are more. It is best to avoid them completely, even though quoting them makes the schema and SQL syntax valid.

### Relying on Nonexplicit Assumptions

This is an issue that sometimes comes into play, where an application assumes data is processed in a particular order or in a particular way. This really should never be done in an application. One of the best examples is the ordering of rows retrieved; one should not even rely on data being returned in the order of a `PRIMARY KEY` or some index. Example:

```sql
MariaDB> SELECT `order_date` FROM `orders_t`;
+---------------------+
| order_date          |
+---------------------+
| 2024-05-17 18:01:01 |
| 2025-12-12 18:44:08 |
| 2025-12-12 18:44:17 |
| 2025-09-09 14:57:47 |
+---------------------+
4 rows in set (0.000 sec)

MariaDB> ALTER TABLE `orders_t` ADD KEY(`order_date`);
Query OK, 0 rows affected (0.034 sec)
Records: 0  Duplicates: 0  Warnings: 0

MariaDB> SELECT `order_date` FROM `orders_t`;
+---------------------+
| order_date          |
+---------------------+
| 2024-05-17 18:01:01 |
| 2025-09-09 14:57:47 |
| 2025-12-12 18:44:08 |
| 2025-12-12 18:44:17 |
+---------------------+
4 rows in set (0.003 sec)
```

In the example, the order of the rows returned changed after the index was created, as the index can be used to fetch the data, and when the optimizer does that, it processes the index in order, which means the data is returned in the order of the index. Relying on this ordering in the application is not a good idea, though. If you require data to be returned in a particular order, then you have to use an `ORDER BY` clause; if you don’t, the row ordering should be treated as being undetermined.

Another example is the `LIMIT` clause. When using `LIMIT` with a `SELECT`, the rows that are returned are undetermined unless an `ORDER BY` clause is provided. When using a `LIMIT` clause with an `UPDATE` or `DELETE` statement, it is even more important to understand that ordering is not fixed unless an `ORDER BY` statement is used. In general, I’d be careful with using the `LIMIT` clause for `UPDATE` and `DELETE` unless there is a good reason to do so.

There are other assumptions than row ordering, but it is one of the most common issues.

### Code and Schema Standardization

Following some internal standards is really helpful when it comes to building applications that can be maintained. Standardizing how to determine the data type, the column name and how to interact with the database schema is a good first step in making an application easy to maintain over time. This also helps in making application code easy to read, which is also helpful.

### Complex SQL

There are situations where the application-level SQL gets really complex, sometimes too complex, which in turn makes the code hard to maintain. In those cases, it is sometimes useful to break up a very complex SQL `SELECT` into multiple statements. In particular, complex `SELECT JOIN` queries are troublesome in this respect. If a `JOIN` is not a straight equi-join but a more complex one, for example, joining of a part of a database column, say the `YEAR` part of a `DATETIME` field, then things get really complex. An alternative is sometimes to use temporary tables, which are very efficient in MariaDB, instead of a single very complex `SELECT`.

## See Also

* [Stored procedures and functions](../../server-usage/stored-routines/stored-procedures/)
* [Views](../../server-usage/views/)
* [SELECT](../../reference/sql-statements/data-manipulation/selecting-data/select.md)
* [INSERT](../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md)
* [Reserved words](../../reference/sql-structure/sql-language-structure/reserved-words.md)
* [JOIN queries](../../reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/)\
