## Query Block Naming

Optimizer hints can address certain named query blocks within the query. Query block is either a top-level `SELECT`/`UPDATE`/`DELETE` statement or a subquery within the statement.

There are three ways to address query blocks:

* by an explicit name assigned using `QB_NAME()` hint
* by implicit name based on position of the query block in the query
* by implicit name based on alias of derived table, view or CTE

### Explicit query block names

* `QB_NAME(query_block_name)` hint is used to assign a name to a query block in which this hint is placed.

#### Examples
Assigning a name to a top-level `SELECT` statement:
```sql
SELECT /*+ QB_NAME(foo) */ * FROM t1 ...;
```
Assigning a name to a subquery:
```sql
SELECT * FROM (SELECT /*+ QB_NAME(subq) */* FROM t1 ...) dt ...;
```
Assigning names to multiple query blocks:
```sql
SELECT /*+ QB_NAME(qb_outer) */ ...
  FROM (SELECT /*+ QB_NAME(dt1) */ ...
  FROM (SELECT /*+ QB_NAME(dt2) */ ... FROM ...) dt2) dt1 ...
```

The assigned name can then be used to refer to the query block in optimizer hints, for example:
```sql
SELECT /*+ QB_NAME(qb_outer) NO_ICP(@qb1 t1) BNL(@dt1) INDEX(t2@dt2 idx1) */ ...
  FROM t1, (SELECT /*+ QB_NAME(dt1) */ ...
      FROM (SELECT /*+ QB_NAME(dt2) */ ... FROM t2 ...) dt2) dt1 ...
```

The scope of a query block name is the whole statement. It is invalid to use the same name for multiple query blocks. You can refer to the query block "down into subquery", "down into derived table", "up to the parent" and "to a right sibling in the `UNION`". You cannot refer "to a left sibling in a `UNION`".

#### Limitations
Query block names declared inside view definitions (`CREATE VIEW ...`) are only visible inside the view. They are not accessible from outside the view.

### Explicit query block names with path
{% hint style="info" %}
Available from MariaDB 13.0.
{% endhint %}

* `QB_NAME(query_block_name, query_block_path)` hint is used to assign names to query blocks nested within views, derived tables, and CTEs

#### Syntax
```sql
QB_NAME(name, query_block_path)
```
where
```sql
query_block_path ::= query_block_path_element
                      [ {. query_block_path_element }... ]
query_block_path_element ::= @ qb_path_element_select_num |
                                qb_path_element_view_sel
qb_path_element_view_sel ::= qb_path_element_view_name
                              [ @ qb_path_element_select_num ]
```

`query_block_path` is similar to a path in filesystem in some sense. Each next element descends further into the query blocks structure. Path elements are separated with dots (`.`).

Each path element can be either a:

* View/derived table/CTE name
* Select number in the current query block, such as `@SEL_1`, `@SEL_2`, etc.
* Combination of view/derived table/CTE name and select number, such as `v1@SEL_1`, `dt1@SEL_2`, etc.

#### Examples

```sql
CREATE VIEW v1 AS SELECT * FROM t1 WHERE a < 1000;

-- The name `qb_v1` is assigned to the inner query block of the view `v1`
SELECT /*+ qb_name(qb_v1, v1) no_index(t1@qb_v1)*/* FROM v1;

-- This means the same but specifies that `v1` is present in @SEL_1
-- of the current query block. So, @SEL_1 can be omitted here
SELECT /*+ qb_name(qb_v1, v1@SEL_1) no_index(t1@qb_v1)*/* FROM v1;

-- However, here we have two occurrences of `v1` in different query blocks
-- (@SEL_1 and @SEL_2), so specifying @SEL_1 is essential
SELECT /*+ qb_name(qb_v1, v1@SEL_1) no_index(t1@qb_v1)*/* FROM v1 WHERE a < 10
UNION
SELECT * FROM v1 WHERE b > 100;
```

Path consisting of two elements:
```sql
-- The view has two query blocks
CREATE VIEW v1 AS SELECT * FROM t1 WHERE a < 10 
                  UNION
                  SELECT * FROM t2 WHERE b > 20;

-- This hint means that SELECT#2 of view `v1`, which is present in 
-- SELECT#1 of the current query block, gets the name `qb_v1`.
SELECT /*+ qb_name(qb_v1, v1@sel_1 .@sel_2) */ * FROM v1;
```

Views and derived tables may be nested on multiple levels, for example:
```sql
-- The path follows `dt1` -> `dt2` -> `v2` -> `@SEL_2` of `v2`
SELECT /*+ qb_name(dt2_dt1_v1_1, dt1 .dt2 .v2 .@SEL_2)
           no_index(t1@dt2_dt1_v1_1)*/ v1.*
FROM v1 
     JOIN (SELECT v1.* FROM v1 
           JOIN (SELECT * FROM v2) dt2
          ) dt1
```

#### Limitations
* Only SELECT statements support QB names with path. DML operations
  (UPDATE, DELETE, INSERT) do not support them
* QB names with path are not supported inside view definitions (`CREATE VIEW ...`)


### Implicit names based on position
{% hint style="info" %}
Available from MariaDB 12.2.
{% endhint %}

Besides the given name, any query block has an implicit name `select_#n` (where `#n` stands for a number). You can see these numbers in the column `id` of the `EXPLAIN` output:

```sql
-- `select#1` addresses the topmost query block joining tables `e` and `s`.
-- The hint disables merging of derived table `(select * from salaries) s`
EXPLAIN
SELECT /*+ NO_MERGE(s@`select#1`) */ e.emp_name, s.salary
FROM employees e JOIN (select * from salaries) s ON e.emp_id = s.emp_id
WHERE s.salary > (SELECT AVG(salary) FROM salaries);
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
| id | select_type | table |  type | possible_keys | key      | key_len |  ref | rows |  filtered   |     Extra
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
|  1 | PRIMARY     | e     | ALL   | PRIMARY       | NULL     | NULL    | NULL |    5 |   100.00    | NULL
|  1 | PRIMARY     | <derived2> | ref | key0          | key0     | 5       | test.e.emp_id |    1 |   100.00    | Using where
|  3 | SUBQUERY    | salaries | ALL | NULL          | NULL     | NULL    | NULL |    5 |   100.00    | NULL
|  2 | DERIVED     | salaries | ALL | NULL          | NULL     | NULL    | NULL |    5 |   100.00    | NULL
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
```

```sql
-- `select#2` addresses the query block corresponding to derived table `T`
EXPLAIN SELECT /*+ JOIN_ORDER(@`select#2` twenty,ten) */  * 
FROM (SELECT ten.a AS a FROM (ten JOIN twenty)
      WHERE (ten.a = twenty.a) LIMIT 1000 ) T;
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
| id | select_type | table |  type | possible_keys | key      | key_len |  ref | rows |  filtered   |     Extra
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
|  1 | PRIMARY     | <derived2> | ALL | NULL          | NULL     | NULL    | NULL |  200 |   100.00    | NULL
|  2 | DERIVED     | twenty  | ALL | NULL          | NULL     | NULL    | NULL |   20 |   100.00    | NULL
|  2 | DERIVED     | ten     | ALL | NULL          | NULL     | NULL    | NULL |   10 |   100.00    | Using where; Using join buffer (flat, BNL join)
+----+-------------+-------+-------+---------------+----------+---------+------+------+-----------------------+
```

#### Limitations
* The positional numbers of query blocks are not stable and can change if the query is modified or its execution plan changes (for example, due to statistics re-collection). If a more stable query block addressing is needed then [explicit naming](#explicit-query-block-names) is probably a better choice.
* Implicit names based on position are not supported inside view definitions (`CREATE VIEW ...`).

### Implicit names based on aliases
{% hint style="info" %}
Available from MariaDB 13.0
{% endhint %}

It is possible to address a query block corresponding to a derived table, view or CTE using its name or an alias in the query.

#### Examples
```sql
-- Addressing a table inside a derived table using implicit QB name
SELECT /*+ no_index(t1@dt) */ *
  FROM (SELECT * FROM t1 WHERE a > 10) AS DT;
-- this is an equivalent to:
SELECT /*+ no_index(t1@dt) */ * FROM
  (SELECT /*+ qb_name(dt)*/ * FROM t1 WHERE a > 10) AS DT;
-- Addressing a query block corresponding to the derived table
SELECT /*+ no_bnl(@dt) */ *
  FROM (SELECT * FROM t1, t2 WHERE t1.a > t2.a) AS DT;

-- View
CREATE VIEW v1 AS SELECT * FROM t1 WHERE a > 10 AND b > 100;

-- referencing a table inside a view by implicit QB name:
SELECT /*+ index_merge(t1@v1 idx_a, idx_b) */ *
  FROM v1, t2 WHERE v1.a = t2.a;
-- could be equivalent to, if query blocks names specified inside view definition
-- were accessible from the outer query:
CREATE VIEW v1 AS SELECT /*+ qb_name(qb_v1) */ *
  FROM t1 WHERE a > 10 AND b > 100;
SELECT /*+ index_merge(t1@qb_v1 idx_a, idx_b) */ *
  FROM v1, t2 WHERE v1.a = t2.a;

-- CTE
WITH aless100 AS (SELECT a FROM t1 WHERE b <100)
  SELECT /*+ index(t1@aless100) */ * FROM aless100;
-- equivalent to:
WITH aless100 AS (SELECT /*+ qb_name(aless100) */ a FROM t1 WHERE b <100)
  SELECT /*+ index(t1@aless100) */ * FROM aless100;
```
#### Limitations
* Only SELECT statements support implicit QB names based on aliases. DML operations
  (UPDATE, DELETE, INSERT) do not support them.
* Implicit names based on aliases are not supported inside view definitions (`CREATE VIEW ...`).
