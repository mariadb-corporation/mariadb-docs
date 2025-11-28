---
description: >-
  Define simple temporary result sets. Non-recursive CTEs act like query-local
  views, improving readability by allowing you to define and reuse subqueries
  within a single statement.
---

# Non-Recursive Common Table Expressions Overview

Common Table Expressions (CTEs) are a standard SQL feature, and are essentially temporary named result sets. There are two kinds of CTEs: Non-Recursive, which this article covers; and [Recursive](recursive-common-table-expressions-overview.md).

## Non-Recursive CTEs

The [WITH](with.md) keyword signifies a CTE. It is given a name, followed by a body (the main query):

![cte\_syntax](/broken/files/MFZE3zCsU3RNoysbwrNB)

CTEs are similar to derived tables:

```sql
WITH engineers AS 
   ( SELECT * FROM employees
     WHERE dept = 'Engineering' )

SELECT * FROM engineers
WHERE ...
```

```sql
SELECT * FROM
   ( SELECT * FROM employees
     WHERE dept = 'Engineering' ) AS engineers
WHERE
...
```

A non-recursive CTE is basically a query-local [VIEW](../../../../../server-usage/views/). There are several advantages and caveats to them. The syntax is more readable than a nested `FROM (SELECT ...)`.\
A CTE can refer to another and it can be referenced from multiple places.

### A CTE referencing Another CTE

Using this format makes for a more readable SQL than a nested `FROM(SELECT ...)` clause:

```sql
WITH engineers AS (
SELECT * FROM employees
WHERE dept IN('Development','Support') ),
eu_engineers AS ( SELECT * FROM engineers WHERE country IN('NL',...) )
SELECT
...
FROM eu_engineers;
```

### Multiple Uses of a CTE

This can be an 'anti-self join', for example:

```sql
WITH engineers AS (
SELECT * FROM employees
WHERE dept IN('Development','Support') )

SELECT * FROM engineers E1
WHERE NOT EXISTS
   (SELECT 1 FROM engineers E2
    WHERE E2.country=E1.country
    AND E2.name <> E1.name );
```

Or, for year-over-year comparisons, for example:

```sql
WITH sales_product_year AS (
SELECT product, YEAR(ship_date) AS year,
SUM(price) AS total_amt
FROM item_sales
GROUP BY product, year )

SELECT *
FROM sales_product_year CUR,
sales_product_year PREV,
WHERE CUR.product=PREV.product 
AND  CUR.year=PREV.year + 1 
AND CUR.total_amt > PREV.total_amt
```

Another use is to compare individuals against their group. Below is an example of how this might be executed:

```sql
WITH sales_product_year AS (
SELECT product,
YEAR(ship_date) AS year,
SUM(price) AS total_amt
FROM item_sales
GROUP BY product, year
)

SELECT * 
FROM sales_product_year S1
WHERE
total_amt > 
    (SELECT 0.1 * SUM(total_amt)
     FROM sales_product_year S2
     WHERE S2.year = S1.year)
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
