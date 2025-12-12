---
description: >-
  Understand when to use subqueries versus joins. This guide explains
  performance implications and how to rewrite subqueries as joins for
  efficiency.
---

# Subqueries and JOINs

A [subquery](./) can quite often, but not in all cases, be rewritten as a [JOIN](../../joins/join-syntax.md).

## Rewriting Subqueries as JOINS

A subquery using `IN` can be rewritten with the `DISTINCT` keyword. Consider this query:

```sql
SELECT * FROM table1 WHERE col1 IN (SELECT col1 FROM table2);
```

It can be rewritten like this:

```sql
SELECT DISTINCT table1.* FROM table1, table2 WHERE table1.col1=table2.col1;
```

`NOT IN` or `NOT EXISTS` queries can also be rewritten. For example, these two queries return the same result:

```sql
SELECT * FROM table1 WHERE col1 NOT IN (SELECT col1 FROM table2);
SELECT * FROM table1 WHERE NOT EXISTS (SELECT col1 FROM table2 
         WHERE table1.col1=table2.col1);
```

They can both be rewritten like this:

```sql
SELECT table1.* FROM table1 LEFT JOIN table2 ON table1.id=table2.id 
       WHERE table2.id IS NULL;
```

Subqueries that can be rewritten as a `LEFT JOIN` are sometimes more efficient.

## Using Subqueries instead of JOINS

There are some scenarios, though, which call for subqueries rather than joins:

* When you want duplicates, but not false duplicates. Suppose `Table_1` has three rows — {`1`,`1`,`2`}\
  — and `Table_2` has two rows\
  — {`1`,`2`,`2`}. If you need to list the rows\
  in `Table_1` which are also in `Table_2`, only this subquery-based `SELECT` statement will give the right answer (`1`,`1`,`2`):

```sql
SELECT Table_1.column_1 
FROM   Table_1 
WHERE  Table_1.column_1 IN 
  (SELECT Table_2.column_1 
    FROM   Table_2);
```

* This SQL statement won't work:

```sql
SELECT Table_1.column_1 
FROM   Table_1,Table_2 
WHERE  Table_1.column_1 = Table_2.column_1;
```

* because the result will be {`1`,`1`,`2`,`2`}\
  — and the duplication of 2 is an error. This SQL statement won't work either:

```sql
SELECT DISTINCT Table_1.column_1 
FROM   Table_1,Table_2 
WHERE  Table_1.column_1 = Table_2.column_1;
```

* because the result will be {`1`,`2`} — and the removal of the duplicated 1 is an error too.
* When the outermost statement is not a query. The SQL statement:

```sql
UPDATE Table_1 SET column_1 = (SELECT column_1 FROM Table_2);
```

* can't be expressed using a join unless some rare SQL3 features are used.
* When the join is over an expression. The SQL statement:

```sql
SELECT * FROM Table_1 
WHERE column_1 + 5 =
  (SELECT MAX(column_1) FROM Table_2);
```

* is hard to express with a join. In fact, the only way we can think of is this SQL statement:

```sql
SELECT Table_1.*
FROM   Table_1, 
      (SELECT MAX(column_1) AS max_column_1 FROM Table_2) AS Table_2
WHERE  Table_1.column_1 + 5 = Table_2.max_column_1;
```

* which still involves a parenthesized query, so nothing is gained from the transformation.
* When you want to see the exception. For example, suppose the question is: Which books are longer than Das Kapital? These two queries are effectively almost the same:

```sql
SELECT DISTINCT Bookcolumn_1.*                     
FROM   Books AS Bookcolumn_1 JOIN Books AS Bookcolumn_2 USING(page_count) 
WHERE  title = 'Das Kapital';

SELECT DISTINCT Bookcolumn_1.* 
FROM   Books AS Bookcolumn_1 
WHERE  Bookcolumn_1.page_count > 
  (SELECT DISTINCT page_count 
  FROM   Books AS Bookcolumn_2 
  WHERE  title = 'Das Kapital');
```

* The difference is between these two SQL statements is, if there are two editions of Das Kapital (with different page counts), then the self-join example will return the books which are longer than the shortest edition of Das Kapital. That might be the wrong answer, since the original question didn't ask for "... longer than `ANY` book named Das Kapital" (it seems to contain a false assumption that there's only one edition).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
