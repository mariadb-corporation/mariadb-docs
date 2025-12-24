---
description: >-
  Process hierarchical data using recursive CTEs. These expressions reference
  themselves to repeatedly execute a subquery, perfect for traversing tree
  structures or generating sequences.
---

# Recursive Common Table Expressions Overview

Common Table Expressions (CTEs) are a standard SQL feature, and are essentially temporary named result sets. They are defined using the `WITH` clause and can be referenced like tables within the main query. CTEs first appeared in the SQL standard in 1999, and the first implementations began appearing in 2007. 

MariaDB supports two types of CTEs:

* [Non-recursive](non-recursive-common-table-expressions-overview.md);
* Recursive, which this article covers.

## Recursive CTE
A recursive CTE will repeatedly execute subsets of the data until it obtains the complete result set. This makes it particularly useful for handling hierarchical or tree-structured data, such as organizational charts, category trees, or parent-child relationships. [max\_recursive\_iterations](../../../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_recursive_iterations) avoids infinite loops. CTEs permit a query to reference itself.
SQL is generally poor at recursive structures.

![trees\_and\_graphs](../../../../../.gitbook/assets/trees_and_graphs.png)

### Recursive CTE Syntax

[WITH RECURSIVE](with.md) signifies a recursive CTE. It is given a name, followed by a body (the main query).
The body consists of two parts: 

* An anchor member (the initial query)
* A recursive member (which references the CTE itself).

![rcte\_syntax](../../../../../.gitbook/assets/rcte_syntax.png)

### Computation

Given the following structure:

![rcte\_computation](../../../../../.gitbook/assets/rcte_computation.png)

1. First execute the anchor part of the query:

![rcte1](../../../../../.gitbook/assets/rcte1.png)

2. Next, execute the recursive part of the query:

![rcte\_computation\_2](../../../../../.gitbook/assets/rcte_computation_2.png)

![](../../../../../.gitbook/assets/rcte_computation_2b.png)

![](../../../../../.gitbook/assets/rcte_computation_3.png)

![](../../../../../.gitbook/assets/rcte_computation_3b.png)

![](../../../../../.gitbook/assets/rcte_computation_4.png)

### Summary

```sql
WITH RECURSIVE R AS (
  SELECT anchor_data
  UNION [all]
  SELECT recursive_part
  FROM R, ...
)
SELECT ...
```

1. Compute anchor\_data.
2. Compute recursive\_part to get the new data.
3. If (new data is non-empty) go to 2.

### Recursive CTE Examples

#### Transitive closure - determining bus destinations

Sample data:

![tc\_1](../../../../../.gitbook/assets/tc_1.png)

```sql
CREATE TABLE bus_routes (origin VARCHAR(50), dst VARCHAR(50));
INSERT INTO bus_routes VALUES 
  ('New York', 'Boston'), 
  ('Boston', 'New York'), 
  ('New York', 'Washington'), 
  ('Washington', 'Boston'), 
  ('Washington', 'Raleigh');
```

Now, we want to return the bus destinations with New York as the origin:

```sql
WITH RECURSIVE bus_dst as ( 
    SELECT origin as dst FROM bus_routes WHERE origin='New York' 
  UNION
    SELECT bus_routes.dst FROM bus_routes JOIN bus_dst ON bus_dst.dst= bus_routes.origin 
) 
SELECT * FROM bus_dst;
+------------+
| dst        |
+------------+
| New York   |
| Boston     |
| Washington |
| Raleigh    |
+------------+
```

The above example is computed as follows:

First, the anchor data is calculated:

* Starting from New York.
* Boston and Washington are added.

Next, the recursive part:

* Starting from Boston and then Washington.
* Raleigh is added.
* UNION excludes nodes that are already present.

#### Computing paths - determining bus routes

This time, we are trying to get bus routes such as “New York -> Washington -> Raleigh”.

Using the same sample data as the previous example:

```sql
WITH RECURSIVE paths (cur_path, cur_dest) AS (
    SELECT origin, origin FROM bus_routes WHERE origin='New York' 
  UNION
    SELECT CONCAT(paths.cur_path, ',', bus_routes.dst), bus_routes.dst 
     FROM paths
     JOIN bus_routes 
       ON paths.cur_dest = bus_routes.origin AND 
         NOT FIND_IN_SET(bus_routes.dst, paths.cur_path)
) 
SELECT * FROM paths;
+-----------------------------+------------+
| cur_path                    | cur_dest   |
+-----------------------------+------------+
| New York                    | New York   |
| New York,Boston             | Boston     |
| New York,Washington         | Washington |
| New York,Washington,Boston  | Boston     |
| New York,Washington,Raleigh | Raleigh    |
+-----------------------------+------------+
```
## Type Resolution and Data Truncation

In previous versions of MariaDB, the data type of a Recursive CTE column was entirely determined by the Anchor (non-recursive) part. If the Recursive part carried out calculations that generated a greater value, the data was silently truncated, leading to incorrect results.

Starting with the versions listed below, MariaDB prevents silent data loss. The server now validates that the data generated by the recursive part matches the column types given by the anchor part. If a mismatch that leads to truncation is detected, the query will now fail with an error. See [MDEV-12325](https://jira.mariadb.org/browse/MDEV-12325) for more information.

+----------------+---------------+
| MariaDB Series | Fixed Version |
+--------------------------------+
| 10.3           | 10.3.36       |
| 10.4           | 10.4.26       |
| 10.5           | 10.5.17       |
| 10.6           | 10.6.9        |
| 10.7           | 10.7.5        |
+----------------+---------------+

### Example: Managing Out of Range Errors in Recursive Part

MariaDB now detects an error when a recursive part executes a calculation (such as adding a large offset) that exceeds the anchor part's data type capacity. To ensure that the query succeeds, [CAST](../../../../sql-functions/string-functions/cast.md) can be used in the anchor part to declare a column size that will allow for the expected growth of your recursive calculations. 

Consider a table representing a company employee hierarchy:

```sql
CREATE TABLE t1
(
  id INT,     -- employee ID
  mid INT,    -- manager ID, or NULL if top level employee
  name TEXT   -- employee name
);
INSERT INTO t1 VALUES (0,NULL, 'Name');
INSERT INTO t1 VALUES (1,0,    'Name1');
INSERT INTO t1 VALUES (2,0,    'Name2');
INSERT INTO t1 VALUES (11,1,   'Name11');
INSERT INTO t1 VALUES (12,1,   'Name12');
```
The following recursive CTE attempts to generate hierarchy levels by changing the mid value in the recursive part:

```sql
WITH RECURSIVE
cteReports (level, id, mid, name) AS
(
  SELECT 1, id, mid, name FROM t1 WHERE mid IS NULL
  UNION ALL
  SELECT r.level + 1, e.id, e.mid + 1000000000000, e.name FROM t1 e
  INNER JOIN cteReports r ON e.mid = r.id
)
SELECT
  level, id, mid, name,
  (SELECT name FROM t1 WHERE id= cteReports.mid) AS mname
FROM cteReports 
ORDER BY level, mid;
```

This query fails with an error with MariaDB versions that incorporate the fix for [MDEV-12325](https://jira.mariadb.org/browse/MDEV-12325):

`Error 1690 (22003): Out of range value for column 'mid' in 'cteReports'`

This happens because the anchor member selects `mid` as the standard integer, but the recursive part attempts to add `1000000000000`, which exceeds the `INT` limit. 

To avoid this error, the data type must be widened (for example, to `DOUBLE` or `BIGINT`) in the anchor part, since recursive CTE column types are defined there.

```sql

WITH RECURSIVE 
cteReports (level, id, mid, name) AS 
(
  SELECT 1, id, cast(mid as double), name FROM t1 WHERE mid IS NULL 
  UNION ALL
  SELECT r.level + 1, e.id, e.mid + 1000000000000, e.name FROM t1 e 
   INNER JOIN cteReports r ON e.mid = r.id 
)
SELECT
  level, id, mid, name,
  (SELECT name FROM t1 WHERE id= cteReports.mid) AS mname
FROM cteReports 
ORDER BY level, mid;
```
By explicitly widening the data type in the anchor part, all values generated by the recursive part fit within the defined column type, and the query executes successfully. 

The expected query result would be:

+-------+------+---------------+--------+--------+
| level | id   | mid           | name   | mname  |
+-------+------+---------------+--------+--------+
|     1 |    0 | NULL          | Name   | NULL   |
|     2 |    1 | 1000000000000 | Name1  | NAME   |
|     2 |    2 | 1000000000000 | Name2  | NAME   |
|     3 |   11 | 1000000000001 | Name11 | NAME1  |
|     3 |   12 | 1000000000001 | Name12 | NAME1  |
+-------+------+------------+--------+-----------+

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
