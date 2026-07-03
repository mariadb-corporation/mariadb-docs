# Joining Tables with JOIN

In the absence of a more tutorial-level document, here is a simple example of\
three basic JOIN types, which you can experiment with in order to see what the\
different joins accomplish:

```sql
CREATE TABLE t1 ( a INT );
CREATE TABLE t2 ( b INT );
INSERT INTO t1 VALUES (1), (2), (3);
INSERT INTO t2 VALUES (2), (4);
SELECT * FROM t1 INNER JOIN t2 ON t1.a = t2.b;
SELECT * FROM t1 CROSS JOIN t2;
SELECT * FROM t1 LEFT JOIN t2 ON t1.a = t2.b;
SELECT * FROM t2 LEFT JOIN t1 ON t1.a = t2.b;
```

The first two SELECTs are (unfortunately) commonly written with an older form:

```sql
SELECT * FROM t1, t2 WHERE t1.a = t2.b;
SELECT * FROM t1, t2;
```

What you can see from this is that an **INNER JOIN** produces a result set\
containing only rows that have a match, in both tables (t1 and t2), for the\
specified join condition(s).

A **CROSS JOIN** produces a result set in which every row in each table is\
joined to every row in the other table; this is also called a **cartesian**\
**product**. In MariaDB the CROSS keyword can be omitted, as it does nothing. Any JOIN without an ON clause is a CROSS JOIN.

The **LEFT JOIN** is an **outer join**, which produces a result set with all\
rows from the table on the "left" (t1); the values for the columns in the other\
table (t2) depend on whether or not a match was found. If no match is found,\
all columns from that table are set to NULL for that row.

The **RIGHT JOIN** is similar to the LEFT JOIN, though its resultset contains all rows from the right table, and the left table's columns will be filled with NULLs when needed.

JOINs can be concatenated to read results from three or more tables.

Here is the output of the various SELECT statements listed above:

```sql
SELECT * FROM t1 INNER JOIN t2 ON t1.a = t2.b;
------ ------ 
| a    | b    |
------ ------ 
|    2 |    2 |
------ ------ 
1 row in set (0.00 sec)


SELECT * FROM t1 CROSS JOIN t2;
------ ------ 
| a    | b    |
------ ------ 
|    1 |    2 |
|    2 |    2 |
|    3 |    2 |
|    1 |    4 |
|    2 |    4 |
|    3 |    4 |
------ ------ 
6 rows in set (0.00 sec)


SELECT * FROM t1 LEFT JOIN t2 ON t1.a = t2.b;
------ ------ 
| a    | b    |
------ ------ 
|    1 | NULL |
|    2 |    2 |
|    3 | NULL |
------ ------ 
3 rows in set (0.00 sec)


SELECT * FROM t2 LEFT JOIN t1 ON t1.a = t2.b;
------ ------ 
| b    | a    |
------ ------ 
|    2 |    2 |
|    4 | NULL |
------ ------ 
2 rows in set (0.00 sec)
```

That should give you a bit more understanding of how JOINS work!

## Other References

* [JOINs Tutorial with Examples](https://blog.devart.com/mysql-joins-tutorial-with-examples.html)
* [How to write complex queries](https://blog.devart.com/how-to-write-complex-mysql-queries.html)

## See Also

* [More Advanced JOINs](../reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/more-advanced-joins.md)
* [Comma vs JOIN](../reference/sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/comma-vs-join.md)
* [mysql\_p5.shtml](https://www.keithjbrown.co.uk/vworks/mysql/mysql_p5.shtml) - Nice tutorial.\
  Part 5 covers joins.

_The initial version of this article was copied, with permission, from_ [_Introduction\_to\_Joins_](https://hashmysql.org/wiki/Introduction_to_Joins) _on 2012-10-05._

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
