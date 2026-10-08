---
description: >-
  Explore joins, subqueries, and set operations in MariaDB SQL. This section
  details how to combine data from multiple tables, nest queries, and perform
  set-based operations for complex data retrieval.
---

# Joins, Subqueries, and Set

SQL (Structured Query Language) is a highly potent language used in the realm of databases and data analytics. It allows us to create, manipulate, and retrieve data stored in relational databases. While simple SQL commands can handle straightforward tasks, one must delve into advanced aspects such as multiple joins, subqueries, and set operations to unravel the full potential of SQL.

### Multiple Joins

Joins are fundamental to SQL, as they enable us to combine rows from two or more tables based on related columns. Several types of joins exist, including `INNER JOIN`, `LEFT JOIN`, `RIGHT JOIN`, and `FULL JOIN`.

In real-world scenarios, finding database schemas with multiple tables linked through relationships is common. In such cases, we often need to write SQL queries with multiple joins to fetch the required data.

For instance, consider a database for a bookstore with three tables: Books, Authors, and Publishers. If we want to get a list of books along with their author names and publishers, you would require multiple joins.

```sql
SELECT Books.title, Authors.name, Publishers.name
FROM Books
INNER JOIN Authors ON Books.author_id = Authors.id
INNER JOIN Publishers ON Books.publisher_id = Publishers.id;
```

In that query, we used two `INNER JOIN` operations to combine data from the three tables.

### Subqueries

A subquery, also known as a nested query or inner query, is a query embedded within another SQL query. The result of the subquery can be used in the outer query. Subqueries can be used in `SELECT`, `INSERT`, `UPDATE`, and `DELETE` statements and also in conjunction with WHERE and HAVING clauses.

Subqueries can prove powerful in many scenarios. For example, suppose we want to find books that are above the average price in our bookstore database. We could achieve this using a subquery.

```sql
SELECT title, price
FROM Books
WHERE price > (SELECT AVG(price) FROM Books);
```

In this query, the subquery calculates the average book price, which the outer query then uses to filter books that are priced above average.

### Set Operations

SQL also provides several set operations to combine rows from two or more tables, including `UNION`, `UNION ALL`, `INTERSECT`, and `EXCEPT`. These operations are instrumental when dealing with large databases where data is spread across multiple tables and we need to perform set-based operations.

For example, suppose we have two tables, _Books\_2019_ and _Books\_2020_, listing the books sold in the respective years. If we want to find books sold in both years, we can use the `INTERSECT` operation.

```sql
SELECT title FROM Books_2019
INTERSECT
SELECT title FROM Books_2020;
```

In the above query, INTERSECT returns the common book titles sold in both 2019 and 2020.

### Conclusion

Advanced SQL queries that involve multiple joins, subqueries, and set operations can be daunting at first glance. However, these incredibly powerful tools in our SQL toolkit enable us to craft complex data retrieval and manipulation commands. To truly excel in data analytics, mastering these aspects of SQL is not only beneficial but essential.

Remember, practice is the key to mastering these advanced SQL concepts, like any other technical skill. Write queries, solve problems, make mistakes, and learn from them. Over time, you'll find yourself not only comfortable but proficient in creating intricate SQL queries.

### See Also

* [Joining Tables with JOIN Clauses Guide](../../mariadb-quickstart-guides/mariadb-join-guide.md)
* [More Advanced Joins](../sql-statements/data-manipulation/selecting-data/joins-subqueries/joins/more-advanced-joins.md)
* [JOIN Syntax](../sql-statements/data-manipulation/selecting-data/joins/join-syntax.md)
* [Comma vs JOIN](../sql-statements/data-manipulation/selecting-data/joins/comma-vs-join.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
