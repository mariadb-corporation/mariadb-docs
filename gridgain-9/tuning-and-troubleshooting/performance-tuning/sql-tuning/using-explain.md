---
description: >-
  How to use the GridGain 9 SQL EXPLAIN command to read query execution plans,
  diagnose common performance issues, and improve query performance.
---

# How to Improve Queries With EXPLAIN Command

The SQL `EXPLAIN` command is a powerful tool used to analyze and understand the execution plan of a query without actually executing it.

When you use the EXPLAIN command, it returns the query execution plan, which includes details such as:

- The order in which tables are accessed.
- The type of join operations used (for example, nested loops, hash joins, or merge joins).
- Any indexes that are used to speed up data retrieval.
- Estimated costs and row counts for different parts of the query.

This information is crucial for optimizing query performance, identifying bottlenecks, and making informed decisions about database schema design and indexing strategies.

## EXPLAIN Command Syntax

GridGain 9 supports two variations of the `EXPLAIN` command:

```sql
EXPLAIN [PLAN | MAPPING] FOR <query>
```

If neither `PLAN` nor `MAPPING` is specified, then `PLAN` is implicit.

Parameters:

- `PLAN` - explains query in terms of relational operators tree. This representation is suitable for investigation of performance issues related to the optimizer.
- `MAPPING` - explains query in terms of mapping of query fragment to a particular node of the cluster. This representation is suitable for investigation of performance issues related to the data colocation.

Examples:

```sql
EXPLAIN SELECT * FROM lineitem;
EXPLAIN PLAN FOR SELECT * FROM lineitem;
EXPLAIN MAPPING FOR SELECT * FROM lineitem;
```

## Understanding The Output

Each query plan is represented as a tree-like structure composed of relational operators.

A node in the plan includes:

- A **name**, indicating the relational operator (e.g., `TableScan`, `IndexScan`, `Sort`, `Join` types)
- A set of **attributes**, relevant to that specific operator

```
OperatorName
    attribute1: value1
    attribute2: value2
```

### Operator Naming

The operator name reflects the specific algorithm or strategy used. For example:

- `TableScan` – Full scan of a base table.
- `IndexScan` – Access via index, possibly sorted.
- `Sort` – Explicit sorting step.
- `HashJoin`, `MergeJoin`, `NestedLoopJoin` – Types of join algorithms.
- `Limit`, `Project`, `Exchange` – Execution-related transformations and controls.
- `SearchBounds` - Shows index lookup constraints: `searchBounds: <v1, v2, ...>` for an exact lookup, `[<l1, l2>..<u1, u2>)` for a range look up.

### Hierarchical Plan Structure

The plan is structured as a **tree**, where:

- **Leaf nodes** represent data sources (e.g., `TableScan`)
- **Internal nodes** represent data transformations (e.g., `Join`, `Sort`)
- **The root node** (topmost) is the final operator that produces the result

## Common Query Optimization Issues

SQL EXPLAIN output analysis can help you optimize slow query execution. You can avoid common bottlenecks in SQL execution by following these guidelines:

- Avoid scanning an entire table.
- Avoid scanning non-optimal indexes.
- Avoid suboptimal join ordering or join algorithm.
- Ensure optimal data colocation for your queries.

In the following sections, we will see some common issues with queries and ways to identify and fix them.

## Full Scan Instead of Index Scan

Suppose related sql execution flow looks like:

```sql
CREATE TABLE t (id INT PRIMARY KEY, col1 VARCHAR);
CREATE INDEX t_col1_idx ON t(col1);

SELECT id FROM t WHERE col1 = '1';
```

The planner chooses between a full scan (**TableScan** operator) and a scan through an index (**IndexScan** operator) based on the estimated cost. Here, the planner uses the index:

```
   IndexScan
       table: PUBLIC.T
       index: T_COL1_IDX
       type: SORTED
       predicate: =(COL1, _UTF-8'1')
       searchBounds: <_UTF-8'1'>
       fieldNames: [ID]
       est: (rows=3330)
```

{% hint style="info" %}
For simplicity, here and below, information that is not related to the example is omitted from the EXPLAIN output.
{% endhint %}

The **searchBounds** attribute shows that the index is used for a lookup, not for a full index scan.

If you see a **TableScan** operator with a predicate on an indexed column, and you expect that an index scan is preferable, you can use the `FORCE_INDEX` hint to force the `IndexScan` approach:

```sql
SELECT /*+ FORCE_INDEX(t_col1_idx) */ id FROM t WHERE col1 = '1';
```

## Suboptimal Indexes

When several indexes can serve a query, the planner chooses one by cost. For example, the schema and query may look as follows:

```sql
CREATE TABLE t (id INT PRIMARY KEY, col1 VARCHAR, col2 VARCHAR);
CREATE INDEX t_col1_col2_idx ON t(col1, col2);
CREATE INDEX t_col1_idx ON t(col1);

SELECT id FROM t WHERE col1 = '1' AND col2 = '2';
```

The planner uses the index that covers both predicates:

```
   IndexScan
       table: PUBLIC.T
       index: T_COL1_COL2_IDX
       type: SORTED
       predicate: AND(=(COL1, _UTF-8'1'), =(COL2, _UTF-8'2'))
       searchBounds: <_UTF-8'1', _UTF-8'2'>
       ...
```

Check that the **searchBounds** attribute lists a bound for every column you filter on. If the plan instead shows an index that covers fewer of the predicate columns, for example **T_COL1_IDX**, you can use the `FORCE_INDEX` hint to choose the index yourself:

```sql
SELECT /*+ FORCE_INDEX(t_col1_col2_idx) */ id FROM t WHERE col1 = '1' AND col2 = '2';
```

## Unexpected Sort Operation

By default, sorted indexes store their entries in ascending order.
You can adjust the ordering of a sorted index by including the options ASC or DESC.

Let's suppose the schema and related query look like this:

```sql
CREATE TABLE t1 (id INT PRIMARY KEY, col1 VARCHAR);
CREATE TABLE t2 (id INT PRIMARY KEY, col1 VARCHAR);
CREATE INDEX t1_col1_desc_idx ON t1(col1 DESC);
CREATE INDEX t2_col1_idx ON t2(col1);

SELECT t1.id as t1id, t2.id as t2id FROM t1 JOIN t2 USING (col1);
```

And the possible execution plan looks like this:

```
   MergeJoin
         ...
       Sort
           collation: [COL1 ASC]
           ...
         TableScan
             table: PUBLIC.T1
             ...
       IndexScan
           index: T2_COL1_IDX
           ...
```

In the example above, the planner does not use the descending **T1_COL1_DESC_IDX** index, because the merge join requires ascending order.
Instead, it scans the whole **T1** table and adds the **Sort** operation.

Extra **Sort** operations adds performance costs, and we can avoid it by creating an index with the appropriate sort ordering:

```sql
CREATE INDEX t1_col1_idx ON t1(col1);
```

And the plan will no longer display the **Sort** operation or the full table scan, improving query execution speed:

```
   MergeJoin
         ...
       IndexScan
           index: T1_COL1_IDX
           ...
       IndexScan
           index: T2_COL1_IDX
           ...
```

## Performance Impact of Correlated Subqueries

The SQL-99 standard allows for nested subqueries at nearly all places within a query, so Ignite 3 supports nested subqueries, both correlated and not.
Performance of certain complex correlated subqueries may be insufficient. Let's consider a correlated query:

```sql
CREATE TABLE emp(dept_id INTEGER PRIMARY KEY, name VARCHAR, salary INTEGER);
CREATE TABLE dept(id INTEGER PRIMARY KEY, name VARCHAR);

SELECT emp.name, (SELECT dept.name FROM dept WHERE emp.dept_id=dept.id)
FROM emp
WHERE emp.salary > 1000;
```

We can see nested correlated subquery here. By default, the planner rewrites a simple subquery like this one into a regular join (a left `HashJoin` on `DEPT_ID = ID`), so no correlated join appears. To see the plan that executes the subquery once for every outer row, disable the rewrite with the `disable_decorrelation` hint:

```sql
SELECT /*+ disable_decorrelation */ emp.name, (SELECT dept.name FROM dept WHERE emp.dept_id=dept.id)
FROM emp
WHERE emp.salary > 1000;
```

Lets check the plan:

```
   CorrelatedNestedLoopJoin
         predicate: true
         type: left
         correlates: [$cor1]
         ...
       Exchange
           distribution: single
           ...
         TableScan
             table: PUBLIC.EMP
             predicate: >(SALARY, 1000)
             ...
     HashAggregate
         group: []
         aggregation: [SINGLE_VALUE(NAME)]
         ...
       Exchange
           distribution: single
           ...
         IndexScan
             table: PUBLIC.DEPT
             index: DEPT_PK
             type: HASH
             predicate: =($cor1.DEPT_ID, ID)
             searchBounds: <$cor1.DEPT_ID>
             ...
```

The example above shows the slow **CorrelatedNestedLoopJoin** operation. Queries with this operation may cause a number of issues:

- Such subqueries may become bottlenecks.
- Queries can cause high CPU load.
- Certain queries may perform slower than expected.

If performance issues are found in similar queries, it would be more
efficient to rewrite the query without nested subqueries, for example:

```sql
SELECT emp.name, dept.name
FROM emp, dept
WHERE emp.salary > 1000 AND emp.dept_id=dept.id;
```

And new plan becomes:

```
     HashJoin
         predicate: =(DEPT_ID, ID)
         ...
       TableScan
           table: PUBLIC.EMP
           predicate: >(SALARY, 1000)
           ...
         TableScan
             table: PUBLIC.DEPT
             ...
```

Without the **CorrelatedNestedLoopJoin** operation, the query should perform much better than the previous one.

## Excessive Sorting

Lets explain we have an index involved two columns one of them is participate in predicate and other in ordering, or in sql terms:

```sql
CREATE TABLE emp(dept_id INTEGER PRIMARY KEY, name VARCHAR, salary INTEGER);
CREATE INDEX emp_salary_name_idx ON emp(salary, name);

SELECT dept_id FROM emp WHERE salary = 1 ORDER BY name;
```

Expectations:

- The index needs to be used here.
- No additional sort is needed because index is ordered by **name** column is satisfies initial query ordering.

But the real execution plan still contains a sort:

```
     Sort
         collation: [NAME ASC]
         ...
       IndexScan
           table: PUBLIC.EMP
           index: EMP_SALARY_NAME_IDX
           predicate: =(SALARY, 1)
           searchBounds: <1>
           ...
```

We can see a redundant **Sort** operator on top of the index scan. A bit query refactoring can help to avoid excessive sorting:

```sql
SELECT dept_id FROM emp WHERE salary = 1 ORDER BY salary, name;
```

And the plan becomes as follows:

```
     IndexScan
         table: PUBLIC.EMP
         index: EMP_SALARY_NAME_IDX
         predicate: =(SALARY, 1)
         searchBounds: <1>
         collation: [SALARY ASC, NAME ASC]
         ...
```

## Select Count Optimization

Some queries can be optimized to use more optimal plans which brings performance speed up. For example, plan for:

```sql
SELECT COUNT(*) FROM emp;
```

Can look like this:

```
 SelectCount
     table: PUBLIC.EMP
     fieldNames: [$f0]
     projection: [$COUNT_ALL]
     ...
```

But there are numerous cases where such optimization is not applicable. In such a cases, a plan can be different and the execution may require more time.

The same query as above, but with explicit transaction may produce a different plan, for example:

```
   Project
       projection: [CAST(EXPR$0):BIGINT NOT NULL]
       ...
     StreamAggregate
         phase: FINAL
         group: []
         aggregation: [$SUM0(EXPR$0)]
         ...
       Exchange
           distribution: single
           ...
         StreamAggregate
             phase: PARTIAL
             fieldNames: [EXPR$0]
             group: []
             aggregation: [COUNT()]
             ...
           TableScan
               table: PUBLIC.EMP
               ...
```

The aggregation runs in two phases. A `StreamAggregate` with `phase: PARTIAL` counts the rows of each partition, and a `StreamAggregate` with `phase: FINAL` sums the partial counts after the `Exchange`.

## Index Scan Without Exact Search Bounds

Table scans are available in two implementations: direct table scan and scan through index.
Index scans contain predicate and search bounds.
Predicate provides final rows comparison. If search bounds are absent, the query degenerates into table scan through index scan (requiring an additional store look up), with further predicate comparison that incurs additional performance overhead costs.

Let's suppose we have schema and query like this:

```sql
CREATE TABLE t (id INTEGER PRIMARY KEY, col1 DECIMAL(5, 3));
CREATE INDEX t_col1_idx ON t(col1);

SELECT id FROM t WHERE col1 = 43;
```

The planner converts the literal to the column type, so the plan has both **predicate** and **searchBounds**:

```
   IndexScan
       table: PUBLIC.T
       index: T_COL1_IDX
       type: SORTED
       predicate: =(COL1, 43.000)
       searchBounds: <43.000:DECIMAL(5, 3)>
       ...
```

Both attributes are present, which means that only an exact lookup through the index is involved.

If the **searchBounds** attribute is absent from an **IndexScan**, **all** rows from the index go through the predicate, which brings an additional performance penalty.
Two types of solutions are possible in that case:

- You can prohibit suboptimal index usage;
- You can explicitly help the planner with type derivation.

### Prohibit Index Usage

For the first approach, use the **NO_INDEX** hint to prohibit index usage:

```sql
SELECT /*+ NO_INDEX */ id FROM t WHERE col1 = 43;

-- or with direct index mention:

SELECT /*+ NO_INDEX(t_col1_idx) */ id FROM t WHERE col1 = 43;
```

As a result, you will have a plan similar to this:

```
   TableScan
       table: PUBLIC.T
       predicate: =(COL1, 43.000)
       ...
```

### Manual Type Casting

You can append an explicit cast to a literal to give it the type of the column:

```sql
SELECT id FROM t WHERE col1 = 43::DECIMAL(5, 3);
```

For the literal above, the plan is the same as without the cast.
A cast is more important when the comparison involves an expression whose type differs from the column type.
A cast applied to the **column** itself prevents the use of the index:

```sql
CREATE TABLE t (id INT PRIMARY KEY, col1 INT);
CREATE INDEX t_col1_asc_idx ON t (col1);

SELECT * FROM t WHERE col1::varchar = SUBSTR(CURRENT_DATE::varchar, 4);
```

Possible plan:

```
   TableScan
       table: PUBLIC.T
       predicate: =(CAST(COL1):VARCHAR CHARACTER SET "UTF-8", SUBSTR(CAST(CURRENT_DATE):VARCHAR CHARACTER SET "UTF-8" NOT NULL, 4))
       ...
```

The planner scans the whole table, because the predicate cannot be evaluated through the index.

Try to change it like:

```sql
SELECT * FROM t WHERE col1 = SUBSTR(CURRENT_DATE::varchar, 4)::int;
```

And the possible plan will become:

```
   IndexScan
       table: PUBLIC.T
       index: T_COL1_ASC_IDX
       type: SORTED
       predicate: =(COL1, CAST(SUBSTR(CAST(CURRENT_DATE):VARCHAR CHARACTER SET "UTF-8" NOT NULL, 4)):INTEGER NOT NULL)
       searchBounds: <CAST(SUBSTR(CAST(CURRENT_DATE):VARCHAR CHARACTER SET "UTF-8" NOT NULL, 4)):INTEGER NOT NULL>
       ...
```

We can see that **searchBounds** are present - thus more productive execution flow is expected here.

## Colocation Usage

As mentioned above, right colocated columns choice plays a significant role in query execution performance.
For example, if initially tables are created without any thoughts about further usage columns colocation you can have the following scenario:

```sql
-- by default, the table is implicitly colocated by PRIMARY KEY
CREATE TABLE emp(dept_id INTEGER, name VARCHAR, salary INTEGER, PRIMARY KEY(dept_id, name));

-- implicitly colocated by PRIMARY KEY
CREATE TABLE dept(id INTEGER, name VARCHAR, PRIMARY KEY(name, id));
```

And query as follows:

```sql
SELECT emp.name, dept.name FROM emp JOIN dept ON emp.dept_id = dept.id AND emp.salary > 1000;
```

Bring plan like:

```
   HashJoin
       predicate: =(DEPT_ID, ID)
       ...
     Exchange
         ...
       TableScan
           table: PUBLIC.EMP
           ...
     Exchange
         ...
       TableScan
           table: PUBLIC.DEPT
           ...
```

We can see two **Exchange** operators, which means that all rows are transferred into a single node and then are joined.
This execution flow brings a performance cost and slows down query execution.

Let's try to improve it by adding explicit colocation for the **dept** table by the **ID** column:

```sql
-- implicitly colocated by PRIMARY KEY
CREATE TABLE emp(dept_id INTEGER, name VARCHAR, salary INTEGER, PRIMARY KEY(dept_id, name));
-- explicitly colocated by ID
CREATE TABLE dept(id INTEGER, name VARCHAR, PRIMARY KEY(name, id)) COLOCATE BY (id);
```

Now the dependent rows from **emp** table are transferred into the appropriate
node where **dept** holds the rows according to **DEPT.ID** distribution:

```
   Exchange
       distribution: single
       ...
     Project
         ...
       HashJoin
           predicate: =(DEPT_ID, ID)
           ...
         Exchange
             distribution: table PUBLIC.DEPT in zone "Default" by [DEPT_ID]
             ...
           TableScan
               table: PUBLIC.EMP
               ...
         TableScan
             table: PUBLIC.DEPT
             ...
```

Now there is only one **Exchange** operator below the join. It transfers the rows of the **emp** table to the nodes where the matching **dept** rows are stored.
The **Exchange** at the top of the plan, with `distribution: single`, only gathers the join result on the node that returns it to the client.

And finally, both join predicate related columns are colocated:

{% hint style="info" %}
The following colocation example will only work if the **emp** and **dept** tables belong to the same distribution zone.
{% endhint %}

```sql
-- explicitly colocated by DEPT_ID
CREATE TABLE emp(dept_id INTEGER, name VARCHAR, salary INTEGER, PRIMARY KEY(dept_id, name)) COLOCATE BY(dept_id);
-- explicitly colocated by ID
CREATE TABLE dept(id INTEGER, name VARCHAR, PRIMARY KEY(id, name)) COLOCATE BY(id);
```

Now, the **emp** and **dept** tables are both colocated.

And the final plan will look like this:

```
   Exchange
       distribution: single
       ...
     Project
         ...
       HashJoin
           predicate: =(DEPT_ID, ID)
           ...
         TableScan
             table: PUBLIC.EMP
             ...
         TableScan
             table: PUBLIC.DEPT
             ...
```

There is no **Exchange** operator between the join and the table scans, which means that the rows are joined where they are stored and no excessive rows transfer has occurred.
Only the **Exchange** at the top of the plan remains. It gathers the join result on the node that returns it to the client.

## Comprehensive EXPLAIN Examples

### Example: Complex Join Query

```sql
EXPLAIN PLAN FOR
 SELECT
      U.UserName, P.ProductName, R.ReviewText, R.Rating
   FROM Users U, Reviews R, Products P
  WHERE U.UserID = R.UserID
    AND R.ProductID = P.ProductID
    AND P.ProductName = 'Product_' || ?::varchar
```

The resulting output is:

```
Project
    fieldNames: [USERNAME, PRODUCTNAME, REVIEWTEXT, RATING]
    projection: [USERNAME, PRODUCTNAME, REVIEWTEXT, RATING]
    est: (rows=16650)
  HashJoin
      predicate: =(USERID$0, USERID)
      fieldNames: [PRODUCTID, USERID, REVIEWTEXT, RATING, PRODUCTID$0, PRODUCTNAME, USERID$0, USERNAME]
      type: inner
      est: (rows=16650)
    HashJoin
        predicate: =(PRODUCTID, PRODUCTID$0)
        fieldNames: [PRODUCTID, USERID, REVIEWTEXT, RATING, PRODUCTID$0, PRODUCTNAME]
        type: inner
        est: (rows=16650)
      Exchange
          distribution: single
          est: (rows=50000)
        TableScan
            table: PUBLIC.REVIEWS
            fieldNames: [PRODUCTID, USERID, REVIEWTEXT, RATING]
            est: (rows=50000)
      Exchange
          distribution: single
          est: (rows=1665)
        TableScan
            table: PUBLIC.PRODUCTS
            predicate: =(PRODUCTNAME, ||(_UTF-8'Product_', CAST(?0):VARCHAR CHARACTER SET "UTF-8"))
            fieldNames: [PRODUCTID, PRODUCTNAME]
            est: (rows=1665)
    Exchange
        distribution: single
        est: (rows=10000)
      TableScan
          table: PUBLIC.USERS
          fieldNames: [USERID, USERNAME]
          est: (rows=10000)
```

This execution plan represents a query that joins three tables: `USERS`, `REVIEWS`, and `PRODUCTS`, and selects four fields after filtering by product name.

- **Project** (root node): Outputs the final selected fields — `USERNAME`, `PRODUCTNAME`, `REVIEWTEXT`, and `RATING`.

- **HashJoins** (two levels): Perform the inner joins.
  - The first (bottom-most) joins `REVIEWS` with `PRODUCTS` on `PRODUCTID`.
  - The second joins the result with `USERS` on `USERID`.

- **TableScans**: Each table is scanned:
  - `REVIEWS` is fully scanned.
  - `PRODUCTS` is scanned with a filter on `PRODUCTNAME`.
  - `USERS` is fully scanned.

- **Exchange** nodes: Indicate data redistribution between operators.

Each node includes:

- `fieldNames`: Output columns at that stage.
- `predicate`: Join or filter condition.
- `est`: Estimated number of rows at that point in the plan.

### Example: Query Mapping

A result of EXPLAIN MAPPING command includes additional metadata providing insight at how the query is mapped on cluster topology. So, for the command like below:

```sql
EXPLAIN MAPPING FOR
 SELECT
      U.UserName, P.ProductName, R.ReviewText, R.Rating
   FROM Users U, Reviews R, Products P
  WHERE U.UserID = R.UserID
    AND R.ProductID = P.ProductID
    AND P.ProductName = 'Product_' || ?::varchar
```

The resulting output is:

```
Fragment#3 root
  distribution: single
  executionNodes: [node1]
  tree:
    Project
        fieldNames: [USERNAME, PRODUCTNAME, REVIEWTEXT, RATING]
        projection: [USERNAME, PRODUCTNAME, REVIEWTEXT, RATING]
        est: (rows=1)
      HashJoin
          predicate: =(USERID$0, USERID)
          fieldNames: [PRODUCTID, USERID, REVIEWTEXT, RATING, PRODUCTID$0, PRODUCTNAME, USERID$0, USERNAME]
          type: inner
          est: (rows=1)
        HashJoin
            predicate: =(PRODUCTID, PRODUCTID$0)
            fieldNames: [PRODUCTID, USERID, REVIEWTEXT, RATING, PRODUCTID$0, PRODUCTNAME]
            type: inner
            est: (rows=1)
          Receiver
              fieldNames: [PRODUCTID, USERID, REVIEWTEXT, RATING]
              sourceFragmentId: 4
              est: (rows=1)
          Receiver
              fieldNames: [PRODUCTID, PRODUCTNAME]
              sourceFragmentId: 5
              est: (rows=1)
        Receiver
            fieldNames: [USERID, USERNAME]
            sourceFragmentId: 6
            est: (rows=1)

Fragment#4
  distribution: random
  executionNodes: [node2, node3, node1]
  partitions: [REVIEWS=[node2={1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58}, node3={2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59}, node1={0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57}]]
  tree:
    Sender
        distribution: single
        targetFragmentId: 3
        est: (rows=50000)
      TableScan
          table: PUBLIC.REVIEWS
          fieldNames: [PRODUCTID, USERID, REVIEWTEXT, RATING]
          est: (rows=50000)

Fragment#5
  distribution: table PUBLIC.PRODUCTS in zone "Default"
  executionNodes: [node2, node3, node1]
  partitions: [PRODUCTS=[node2={1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58}, node3={2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59}, node1={0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57}]]
  tree:
    Sender
        distribution: single
        targetFragmentId: 3
        est: (rows=1665)
      TableScan
          table: PUBLIC.PRODUCTS
          predicate: =(PRODUCTNAME, ||(_UTF-8'Product_', CAST(?0):VARCHAR CHARACTER SET "UTF-8"))
          fieldNames: [PRODUCTID, PRODUCTNAME]
          est: (rows=1665)

Fragment#6
  distribution: table PUBLIC.USERS in zone "Default"
  executionNodes: [node2, node3, node1]
  partitions: [USERS=[node2={1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58}, node3={2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50, 53, 56, 59}, node1={0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54, 57}]]
  tree:
    Sender
        distribution: single
        targetFragmentId: 3
        est: (rows=10000)
      TableScan
          table: PUBLIC.USERS
          fieldNames: [USERID, USERNAME]
          est: (rows=10000)
```

Where:

- **Fragment#3** means fragment with id=3. Fragment IDs do not start at 0: they start after the data sources of the plan, so the ID of the root fragment equals the number of scanned sources. This query reads three tables, so the root fragment is 3 and the scan fragments are 4 to 6
- A **root** marks a fragment which is considered as root fragment, i.e. a fragment which represents user's cursor
- A **distribution** attribute provides an insight into which mapping strategy was applied to this particular fragment
- A **executionNodes** attribute provides a list of nodes this fragment will be executed on
- A **partitions** attribute provides an insight into which partitions of which tables will be read from which nodes
- A **tree** attribute specifies which part of the relational tree corresponds to this fragment

The output above shows how the query is broken into multiple execution fragments and distributed across the cluster. It gives insight into both the logical execution plan and how it maps to the physical topology.

The query starts execution in *Fragment#3*, which serves as the root of the plan — this is where the final result is produced. It runs on a single node (`node1`) and contains the main logic of the query, including the projection and two nested hash joins. Instead of scanning tables directly, it receives data from other fragments through `Receiver` operators. These incoming streams correspond to the `REVIEWS`, `PRODUCTS`, and `USERS` tables.

The actual table scans happen in *Fragments 4 through 6*, each responsible for one of the involved tables. These fragments operate in parallel across the cluster. Each performs a scan on its respective table and then sends the results back to Fragment#3.

- *Fragment#4* handles the `REVIEWS` table. It runs on all nodes and uses a random distribution strategy. Data is partitioned across nodes, and after scanning the table, results are sent upstream.
- *Fragment#5* is in charge of the `PRODUCTS` table. It also spans all nodes but follows a zone-based distribution linked to the table's partitioning. There's a filter applied to `PRODUCTNAME`, which limits the amount of data sent to the root.
- *Fragment#6* covers the `USERS` table. Like the others, it's distributed and reads from table partitions spread across the cluster.

Each fragment includes metadata such as the nodes it's executed on, how data is partitioned, and how results are sent between fragments. This layout provides a clear view of not only how the query is logically processed, but also how the workload is split and coordinated in a distributed environment.
