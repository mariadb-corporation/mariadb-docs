---
description: >-
  How to move SQL from the Calcite engine in Apache Ignite 2.18 to the H2 engine
  in GridGain 8.10: queries that return different results, queries that fail,
  changed defaults, and what needs no change.
---

# Migrating SQL From the Calcite Engine

This page is reference material for the [Migration Procedure](migration-procedure.md) and the planning overview in [What to Know Before Migrating](before-you-migrate.md).

Apache Ignite 2 can run SQL on two engines: the default H2 engine, or the optional Calcite engine from the `ignite-calcite` module. GridGain 8 runs only the H2 engine. This page describes what changes for queries that ran on Calcite in Ignite 2.18 and how to rewrite them for GridGain 8.10.

It covers the queries that return different results without an error, the queries that fail, the changed defaults, query hints and plan inspection, and the constructs that need no change.

*Skip this page if your Ignite 2 deployment did not use Calcite: `ignite-calcite` is not in `libs/` or your build dependencies, no node configuration contains `CalciteQueryEngineConfiguration`, and no connection string or query contains `queryEngine=calcite` or `QUERY_ENGINE('calcite')`.*

## Remove the Calcite Configuration

Remove the following before you start GridGain 8:

- The `ignite-calcite` module from `libs/` and from your build dependencies. See [Artifacts and Deployment](artifacts-and-modules.md).
- `CalciteQueryEngineConfiguration` and `SqlConfiguration.queryEnginesConfiguration` from the node configuration. GridGain 8 does not start while they are present. See [Removed Configuration Properties](configuration.md#removed-configuration-properties).
- `queryEngine=calcite` from JDBC and ODBC connection strings. GridGain 8 rejects the connection. See [Clients](apis-and-clients.md#clients).
- `/*+ QUERY_ENGINE('calcite') */` hints from queries. GridGain 8 ignores the hint without an error, so search the code for it.

## Queries That Return Different Results

Every query in this section runs on GridGain 8 without an error and returns different data than it returned on Calcite.

### Non-Colocated Joins and Subqueries

Calcite moves data between nodes automatically, so a join between non-colocated partitioned tables returns the full result. The GridGain 8 engine joins only the data stored on each node unless you enable [non-colocated joins](../../../gridgain8-development/sql/distributed-joins.md#non-collocated-joins). Without them, the result is incomplete, and the number of missing rows grows with the number of nodes.

For example, a join between two `PARTITIONED` tables on a column that is not the affinity key, where the correct result is 6 rows:

| Cluster | Calcite | GridGain 8 | GridGain 8 with `distributedJoins=true` |
|---|---|---|---|
| 2 nodes | 6 | 4 | 6 |
| 3 nodes | 6 | 2 | 6 |

The same applies to `IN (SELECT ...)`, `EXISTS`, `NOT IN`, and correlated subqueries. A `NOT IN` subquery can return extra rows.

For each join or subquery between `PARTITIONED` tables that does not use the affinity key, do one of the following:

- Colocate the tables on the join column. Colocated joins need no extra settings and run faster than non-colocated joins. See [Affinity Colocation](../../../architecture/data-modeling/affinity-colocation.md).

  ```sql
  CREATE TABLE emp (
    emp_id INT, dept_id INT, name VARCHAR,
    PRIMARY KEY (emp_id, dept_id)
  ) WITH "template=partitioned, affinity_key=dept_id";
  ```

- Enable non-colocated joins for the query. The result is correct, but the query is slower because rows are broadcast or looked up on remote nodes.

  {% tabs %}
  {% tab title="Java" %}
  ```java
  SqlFieldsQuery qry = new SqlFieldsQuery(sql).setDistributedJoins(true);
  ```
  {% endtab %}

  {% tab title="JDBC" %}
  ```
  jdbc:ignite:thin://127.0.0.1:10800?distributedJoins=true
  ```
  {% endtab %}
  {% endtabs %}

Non-colocated joins do not fix every query:

| Query | Without `distributedJoins` | With `distributedJoins=true` |
|---|---|---|
| `JOIN`, `IN (SELECT ...)`, or `EXISTS` between tables | Incorrect | Correct |
| Correlated subquery on the same table, for example `(SELECT COUNT(*) FROM emp e2 WHERE e2.dept_id = e.dept_id)` | Incorrect | Still incorrect. Indexes do not help. |
| Self-join with `GROUP BY` | Incorrect | Correct, if the join column is indexed. Without an index, the query fails with `Failed to prepare distributed join query: join condition does not use index`. |
| `JOIN` with a subquery that has its own `GROUP BY` (a derived table) | Correct | Correct |

A correlated subquery on partitioned data cannot be fixed with `distributedJoins`. Colocate the data, or rewrite the subquery as a join with a derived table:

```sql
-- Correlated subquery: incorrect on a multi-node cluster
SELECT e.emp_id,
       (SELECT AVG(salary) FROM emp e2 WHERE e2.dept_id = e.dept_id) AS dept_avg
FROM emp e;

-- Derived table: correct without distributedJoins
SELECT e.emp_id, a.dept_avg
FROM emp e
JOIN (SELECT dept_id, AVG(salary) AS dept_avg FROM emp GROUP BY dept_id) a
  ON a.dept_id = e.dept_id;
```

{% hint style="warning" %}
A staging cluster with fewer nodes than production shows fewer missing rows than production does. Test on a cluster with the production node count.
{% endhint %}

### FILTER Clause on Aggregates

GridGain 8 accepts the `FILTER (WHERE ...)` clause on an aggregate and ignores it. The aggregate is computed over all rows:

| Query | Calcite | GridGain 8 |
|---|---|---|
| `SELECT COUNT(*) FILTER (WHERE dept_id = 10) FROM emp` | 2 | 5 (all rows) |
| `SELECT SUM(qty) FILTER (WHERE dept_id = 10) FROM emp` | 3 | 31 (sum of all rows) |

Rewrite every `FILTER` clause as a `CASE` expression inside the aggregate:

```sql
-- Calcite
SELECT COUNT(*) FILTER (WHERE status = 'PAID') AS paid,
       SUM(amount) FILTER (WHERE status = 'PAID') AS paid_sum
FROM invoice;

-- GridGain 8
SELECT COUNT(CASE WHEN status = 'PAID' THEN 1 END) AS paid,
       SUM(CASE WHEN status = 'PAID' THEN amount END) AS paid_sum
FROM invoice;
```

Do not add `ELSE 0` to the `COUNT` expression: `COUNT` counts non-null values, so `ELSE 0` counts every row.

### Aggregates With OVER

*Skip this section if all your queries come from Ignite 2. Calcite in Ignite 2 does not support window functions, so those queries do not contain them.*

GridGain 8 ignores the `OVER` clause on an aggregate function such as `SUM`, `AVG`, or `COUNT`:

- `SELECT dept_id, SUM(qty) OVER (PARTITION BY dept_id) FROM emp GROUP BY dept_id` runs and returns the total of all rows for every group.
- `SELECT emp_id, AVG(salary) OVER (PARTITION BY dept_id) FROM emp` fails with `Column "__Z0.EMP_ID" must be in the GROUP BY list`. The query has no `GROUP BY`; the message refers to the query that GridGain 8 generates internally.

Ranking functions such as `ROW_NUMBER`, `RANK`, `LEAD`, and `LAG` fail with `Unsupported expression: ... [type=WindowFunction]`.

To replace a window function, use a join with a derived table. Do not use a correlated subquery; see [Non-Colocated Joins and Subqueries](#non-colocated-joins-and-subqueries).

```sql
-- Instead of AVG(salary) OVER (PARTITION BY dept_id)
SELECT e.dept_id, e.emp_id, e.salary, a.dept_avg
FROM emp e
JOIN (SELECT dept_id, AVG(salary) AS dept_avg FROM emp GROUP BY dept_id) a
  ON a.dept_id = e.dept_id;

-- Instead of ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) = 1
SELECT e.emp_id, e.dept_id, e.salary
FROM emp e
JOIN (SELECT dept_id, MAX(salary) AS max_salary FROM emp GROUP BY dept_id) a
  ON a.dept_id = e.dept_id AND e.salary = a.max_salary;
```

Top-N per group and running totals need a self-join, which requires `distributedJoins=true` and an index on the join column:

```sql
-- Instead of ROW_NUMBER() OVER (PARTITION BY dept_id ORDER BY salary DESC) <= 3
CREATE INDEX emp_dept ON emp(dept_id);

SELECT e.emp_id
FROM emp e JOIN emp e2
  ON e2.dept_id = e.dept_id AND e2.salary >= e.salary
GROUP BY e.emp_id
HAVING COUNT(*) <= 3;
```

These rewrites handle ties differently from `ROW_NUMBER`. Add tie-breaking columns to the join condition if the order of tied rows matters.

### Collocated Queries

By default, GridGain 8 runs a query with aggregates in two steps. First, each node computes partial results from the rows that it stores. Then the node that started the query combines the partial results into one result for each group.

The `collocated` flag removes the second step. You set it with `SqlFieldsQuery.setCollocated(true)` or the `collocated=true` JDBC connection property. The flag tells GridGain 8 that all rows of each group are stored on the same node. Each node then computes the final result for its groups, and the node that started the query only collects these results. GridGain 8 does not check whether the rows are actually stored this way.

If the rows of a group are stored on several nodes, each of those nodes returns its own result for the group, computed from its part of the rows, and nothing combines them. The query returns one row for each node that stores rows of the group instead of one row for the group. A query without `GROUP BY` treats the whole table as one group, so on a partitioned table it returns one row per node.

For example, on a three-node cluster where the six rows of `emp` are spread across all three nodes:

```sql
SELECT GROUP_CONCAT(name ORDER BY name SEPARATOR ',') FROM emp;
--   Calcite:                          one row:    n1,n2,n3,n4,n5,n6
--   GridGain 8 with collocated=true:  three rows: n5 | n2,n4 | n1,n3,n6
```

Calcite ignores the `collocated` flag, so a query that sets it returns correct results on Ignite 2 even when the rows of a group are spread across nodes. On GridGain 8, the same query returns incorrect results.

Set `collocated=true` only when the `GROUP BY` columns include the affinity key, so that all rows of each group are stored on one node. See [Affinity Colocation](../../../architecture/data-modeling/affinity-colocation.md).

### Expressions With Different Results

The following expressions return different values on the two engines:

| Expression | Calcite | GridGain 8 | What to do |
|---|---|---|---|
| `CAST('a' AS CHAR(5)) = 'a'` | `false` | `true` | Calcite pads `CHAR(n)` values to their declared length before comparing; GridGain 8 does not. Check `WHERE` conditions on `CHAR(n)` columns, because they can match different rows. |
| `LENGTH(CAST('a' AS CHAR(5)))` | `5` | `1` | Same cause as the previous row. |
| `CONCAT('a', CAST(NULL AS VARCHAR))` | `NULL` | `'a'` | If a null result matters, use `CASE` or `COALESCE`. |
| `SUBSTRING('abcdef', 0, 3)` | `ab` | `abc` | Use a start position of 1 or greater. |
| `SUBSTRING('abcdef', -1, 3)` | `a` | `f` | Use a start position of 1 or greater. |
| `OCTET_LENGTH('abc')` | `3` | `6` | GridGain 8 counts UTF-16 bytes. Use `LENGTH` to count characters. |
| `SOUNDEX('abc')` | `A120` | `a120` | Wrap in `UPPER()` when you compare the result as text. |
| `DIFFERENCE('abc', 'abd')` | `2` | `3` | Re-check any threshold that uses the result. |
| `CAST(10 AS DECIMAL(10,2)) / 3` | 15 fractional digits | 27 fractional digits | Add `CAST(... AS DECIMAL(p,s))` or `ROUND` where the scale matters. |
| `AVG` of a `DECIMAL` column, converted to text | `150.00` | `1.5E+2` | Format the value in the application, or use `CAST(AVG(x) AS DECIMAL(18,2))`. |
| `TO_DATE(...)` | Returns `DATE` | Returns `TIMESTAMP` | Add `CAST(... AS DATE)` where the type matters. |

`GROUP_CONCAT` without `ORDER BY` returns values in an undefined order on both engines. On GridGain 8 the order also changes with the number of nodes, so do not compare the concatenated string in tests.

### Date Format Patterns

`TO_DATE`, `TO_TIMESTAMP`, and `TO_CHAR` exist on both engines and use the same Oracle-style patterns, such as `YYYY-MM-DD HH24:MI:SS`. Neither engine rejects an invalid pattern, and the two engines return different incorrect results for it:

```sql
-- Correct on both engines
SELECT TO_TIMESTAMP('2020-03-04 10:20:30', 'YYYY-MM-DD HH24:MI:SS');  -- 2020-03-04 10:20:30

-- Java-style pattern: no error, incorrect result
SELECT TO_TIMESTAMP('2020-03-04 10:20:30', 'yyyy-MM-dd HH:mm:ss');
--   Calcite:    2021-08-04 10:00:30
--   GridGain 8: 2021-04-04 10:00:30
```

Test every format pattern that your queries use. For Java-style patterns, use `PARSEDATETIME` and `FORMATDATETIME` on GridGain 8:

```sql
SELECT PARSEDATETIME('2020-03-04 10:20:30', 'yyyy-MM-dd HH:mm:ss');
```

## Queries That Fail

Every construct in this section fails with an exception on GridGain 8. To find them all, run your queries prefixed with `EXPLAIN`, as described in [Planning the Migration](#planning-the-migration).

### Queries

| Construct | Error on GridGain 8 | Replacement |
|---|---|---|
| `GROUPING SETS`, `ROLLUP`, `CUBE` | Syntax error, or `Function "ROLLUP" not found` | One `UNION ALL` branch per grouping level. See the example below the table. |
| `INTERSECT ALL`, `EXCEPT ALL` | Syntax error | `INTERSECT` or `EXCEPT` without `ALL`, if duplicates do not matter. Otherwise, a join. |
| `GROUP BY 1` (a column position) | `Column "__Z0.DEPT_ID" must be in the GROUP BY list` | Name the column: `GROUP BY dept_id`. A column alias also works. |
| `GROUP_CONCAT` or `LISTAGG` with `ORDER BY` or `DISTINCT` | `Clauses DISTINCT and ORDER BY are unsupported for GROUP_CONCAT for not collocated data.` | Colocate the data on the group key and set `collocated=true`, or sort and remove duplicates in the application. |
| `SIMILAR TO` | Syntax error | `LIKE`, or `REGEXP_LIKE` for regular expressions. |
| `MAP[...]` or `ROW` constructors | Syntax or internal error | Store the values in separate columns, or as text or JSON. |
| `SELECT ... FOR UPDATE` | `SELECT FOR UPDATE query requires transactional cache with MVCC enabled.` | Key-value transactions. See [Transactional SQL](#transactional-sql). |

`ROLLUP` rewritten as `UNION ALL`:

```sql
-- Calcite
SELECT region, city, SUM(amount) FROM sales GROUP BY ROLLUP (region, city);

-- GridGain 8
SELECT region, city, SUM(amount) FROM sales GROUP BY region, city
UNION ALL
SELECT region, NULL, SUM(amount) FROM sales GROUP BY region
UNION ALL
SELECT NULL, NULL, SUM(amount) FROM sales;
```

`CUBE (a, b)` needs a branch for each of the four combinations, and `GROUPING SETS` needs one branch per set. Each branch is a separate distributed query, so the rewritten query is slower and uses more memory than the original.

### DDL

| Construct | Error on GridGain 8 | Replacement |
|---|---|---|
| `CREATE TABLE ... AS SELECT` | `CREATE TABLE ... AS ... syntax is not supported` | `CREATE TABLE`, then `INSERT INTO ... SELECT`. |
| `DEFAULT CURRENT_TIMESTAMP` or another non-constant default | `Non-constant DEFAULT expressions are not supported [colName=...]` | Set the value in every `INSERT`. Constant defaults such as `DEFAULT 0` work. |
| `ALTER TABLE ... ADD COLUMN ... DEFAULT x` | `ALTER TABLE ADD COLUMN with DEFAULT value is not supported` | Add the column, then run `UPDATE t SET col = x`. |

Calcite in Ignite 2 also rejects `UNIQUE`, `CHECK`, `AUTO_INCREMENT`, `IDENTITY`, computed columns, temporary tables, and the `ENUM` and `TIMESTAMP WITH TIME ZONE` types, so these do not appear in migrated DDL. If your DDL comes from another database, GridGain 8 rejects these too.

### DML

| Construct | Error on GridGain 8 | Replacement |
|---|---|---|
| `DEFAULT` as a value in `INSERT`, `UPDATE`, or `MERGE` | `Explicit DEFAULT values are unsupported for INSERT.` | Supply the value. |
| `MERGE INTO ... USING ... WHEN NOT MATCHED` | `Column "PUBLIC.DEPT._ROWID_" not found` | `MERGE INTO t (columns) VALUES (...)` or `MERGE INTO t (columns) SELECT ...`. |
| `UPDATE` of a column that belongs to a composite key or value | `Update of composite key column is not supported` | Delete the row and insert it again. |

The two engines accept opposite forms of `MERGE`:

```sql
-- Calcite
MERGE INTO dept USING (SELECT 50 AS id, 'd50' AS nm) s ON dept.dept_id = s.id
WHEN NOT MATCHED THEN INSERT (dept_id, dname) VALUES (s.id, s.nm);

-- GridGain 8
MERGE INTO dept (dept_id, dname) VALUES (50, 'd50');
```

### Aggregate Functions

GridGain 8 supports seven aggregate functions: `COUNT(*)`, `COUNT`, `SUM`, `MIN`, `MAX`, `AVG`, and `GROUP_CONCAT` (`LISTAGG` is an alias). Any other aggregate fails with `Unsupported expression: ... [type=Aggregate]`.

| Calcite aggregate | GridGain 8 replacement |
|---|---|
| `EVERY(p)` | `MIN(CASE WHEN p THEN 1 ELSE 0 END) = 1` |
| `SOME(p)` | `MAX(CASE WHEN p THEN 1 ELSE 0 END) = 1` |
| `ANY_VALUE(x)` | `MIN(x)` or `MAX(x)` |
| `ARRAY_AGG(x)`, `ARRAY_CONCAT_AGG(x)` | `GROUP_CONCAT(x SEPARATOR ',')`, or aggregate in the application |
| `BIT_AND(x)`, `BIT_OR(x)`, `BIT_XOR(x)` | Aggregate in the application |

### Scalar Functions

The following Calcite functions have no GridGain 8 equivalent with the same name:

| Calcite function | GridGain 8 replacement |
|---|---|
| `BIT_XOR(a, b)` | `BITXOR(a, b)` |
| `INITCAP(s)` | `UPPER(LEFT(s, 1)) \|\| LOWER(SUBSTRING(s, 2))` for a single word. Handle multiple words in the application. |
| `OVERLAY(s PLACING r FROM p FOR n)` | `SUBSTRING(s, 1, p - 1) \|\| r \|\| SUBSTRING(s, p + n)` |
| `CBRT(x)` | `POWER(x, 1.0 / 3)` |
| `RAND_INTEGER(n)` | `CAST(RAND() * n AS INT)` |
| `ACOSH(x)`, `ASINH(x)`, `ATANH(x)` | `LN(x + SQRT(x * x - 1))`, `LN(x + SQRT(x * x + 1))`, `0.5 * LN((1 + x) / (1 - x))` |
| `SEC`, `SECH`, `CSC`, `CSCH`, `COTH` | `1 / COS(x)`, `1 / COSH(x)`, `1 / SIN(x)`, `1 / SINH(x)`, `1 / TANH(x)` |
| `LAST_DAY(d)` | `DATEADD('DAY', -1, DATEADD('MONTH', 1, DATEADD('DAY', 1 - DAY_OF_MONTH(d), d)))` |
| `UNIX_SECONDS(ts)` | `DATEDIFF('SECOND', TIMESTAMP '1970-01-01 00:00:00', ts)` |
| `TIMESTAMP_SECONDS(n)` | `DATEADD('SECOND', n, TIMESTAMP '1970-01-01 00:00:00')` |
| `UNIX_DATE(d)` | `DATEDIFF('DAY', DATE '1970-01-01', d)` |
| `DATE_FROM_UNIX_DATE(n)` | `DATEADD('DAY', n, DATE '1970-01-01')` |
| `DATE()`, `TIME()`, `DATETIME()` | `CAST`, `PARSEDATETIME`, or date and time literals |
| `MD5(s)`, `SHA1(s)` | If any hash algorithm is acceptable, `CAST(HASH('SHA256', STRINGTOUTF8(s), 1) AS VARCHAR)` returns a hexadecimal SHA-256 digest. Otherwise, compute the hash in the application. |
| `REVERSE`, `STRCMP`, `TO_BASE64`, `FROM_BASE64`, `TYPEOF` | Handle in the application. |
| `EXTRACTVALUE`, `XMLTRANSFORM`, `EXISTSNODE`, and other XML functions | Handle in the application. |
| `JSON_TYPE`, `JSON_EXISTS`, `JSON_DEPTH`, `JSON_KEYS`, `JSON_PRETTY`, `JSON_LENGTH`, `JSON_REMOVE`, `JSON_STORAGE_SIZE`, `IS JSON` | Handle in the application. |

`JSON_VALUE`, `JSON_QUERY`, `JSON_OBJECT`, and `JSON_ARRAY` exist in GridGain 8 under the same names. Check that their arguments and results match your use. See [JSON Functions](../../../reference/sql/functions/json-functions.md).

### Data Types

| Type | Difference | What to do |
|---|---|---|
| `MAP` | Not supported | Store the values in separate columns, or as text or JSON. |
| `ROW` | Not supported | Store the values in separate columns. |
| `ARRAY` | Supported as an object array, with different behavior | Test element access and the type of the returned value. |
| `INTERVAL` | Supported, but returned to the client as a different type | Calcite returns `Period` or `Duration`; GridGain 8 returns a number. Test how your JDBC driver or ORM maps the value. |
| `CHAR(n)` | Compared without padding | See [Expressions With Different Results](#expressions-with-different-results). |

## Changed Defaults

This section applies to every migration, including deployments that did not use Calcite.

### SQL Memory Quota

GridGain 8 limits the memory that SQL queries use on each node. Ignite 2 has no such limit by default.

| Setting | Ignite 2 | GridGain 8 |
|---|---|---|
| Memory for all queries on a node (`sqlGlobalMemoryQuota`) | Unlimited | 60% of the heap |
| Memory for one query (`sqlQueryMemoryQuota`) | Unlimited | Unlimited, so one query can use the whole global quota |
| Writing to disk when the quota is exceeded (`sqlOffloadingEnabled`) | Not applicable | Off, so the query fails |

A query that exceeds the quota fails with `SQL query ran out of memory: Global quota was exceeded.`, error code `3015`. Sorting, grouping, joins, set operations, and large results all count toward the quota. A large query that ran on Ignite 2 can fail on GridGain 8 without any change to the query.

Set the quotas for your expected number of concurrent queries before the cutover, and decide whether to enable offloading. To remove the limit, as in Ignite 2, set `sqlGlobalMemoryQuota` to `0`. The following example sets both quotas and enables offloading:

```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="sqlConfiguration">
        <bean class="org.apache.ignite.configuration.SqlConfiguration">
            <property name="sqlGlobalMemoryQuota" value="300M"/>
            <property name="sqlQueryMemoryQuota" value="50M"/>
            <property name="sqlOffloadingEnabled" value="true"/>
        </bean>
    </property>
</bean>
```

The `UNION ALL` and derived-table rewrites on this page use more memory than the original queries, so size the quotas after you rewrite the queries. See [Memory Quotas for SQL Queries](../../../tuning-and-troubleshooting/performance-tuning/sql-memory-management.md).

### Transactional SQL

*Skip this section if your Ignite 2 configuration does not set `TransactionConfiguration.txAwareQueriesEnabled` to `true`. It is `false` by default.*

With transaction-aware queries enabled, Calcite in Ignite 2 runs SQL inside transactions. GridGain 8 does not:

- DML inside a transaction on a `TRANSACTIONAL` cache is rejected by default.
- Queries do not see a consistent snapshot. A query can read some rows before an update and other rows after it.
- `SELECT ... FOR UPDATE` works only on `TRANSACTIONAL_SNAPSHOT` (MVCC) caches. MVCC is a beta feature and is not recommended for production.

Move read-modify-write logic to key-value transactions:

```java
try (Transaction tx = ignite.transactions().txStart(
        TransactionConcurrency.PESSIMISTIC, TransactionIsolation.REPEATABLE_READ)) {
    // Read, modify, and write the entries.
    tx.commit();
}
```

See also [Features to Replace](features-to-replace.md).

## Query Hints and Plan Inspection

*Hints:* Calcite supports hints such as `FORCE_INDEX`, `NO_INDEX`, `ENFORCE_JOIN_ORDER`, `MERGE_JOIN`, `NL_JOIN`, and `HASH_JOIN`. GridGain 8 ignores them without an error. Search your code for `/*+`, and replace each hint with the GridGain 8 equivalent:

| Calcite hint | GridGain 8 equivalent |
|---|---|
| `FORCE_INDEX`, `NO_INDEX` | [`USE INDEX (index_name)`](../../../tuning-and-troubleshooting/performance-tuning/sql-tuning.md#index-hints) after the table name |
| `ENFORCE_JOIN_ORDER` | [`setEnforceJoinOrder(true)`](../../../tuning-and-troubleshooting/performance-tuning/sql-tuning.md#enforcing-join-order), or the `enforceJoinOrder` JDBC property |
| `MERGE_JOIN`, `NL_JOIN`, `CNL_JOIN`, `HASH_JOIN`, `EXPAND_DISTINCT_AGG`, `DISABLE_RULE` | None. GridGain 8 has no way to force a join algorithm. |

*Plans:* Use `EXPLAIN SELECT ...` instead of `EXPLAIN PLAN FOR SELECT ...`. The output is also different: GridGain 8 returns the SQL that it runs on each node and the SQL that combines the results, not a tree of operators. Rewrite any script or test that reads plan output. See [Using the EXPLAIN Statement](../../../tuning-and-troubleshooting/performance-tuning/sql-tuning.md#using-the-explain-statement).

*Metadata:* GridGain 8 supports `INFORMATION_SCHEMA`, which Calcite does not. The set of `SYS` views differs between the engines; check your monitoring queries against [Monitoring and CLI Changes](operations.md).

## What Does Not Need to Change

The following work the same on both engines:

- `INTERSECT` and `EXCEPT` without `ALL`, including on partitioned tables.
- `NULLS FIRST` and `NULLS LAST` in `ORDER BY`. The default order of nulls is the same on both engines. GridGain 8 rejects these keywords only in `CREATE INDEX`.
- `INTERVAL` literals and arithmetic, including `EXTRACT` from an interval. Only the client-side type differs; see [Data Types](#data-types).
- `LISTAGG` and `STRING_AGG`. You do not need to rename them to `GROUP_CONCAT`.
- `DAYOFMONTH`, `DAYOFWEEK`, and `DAYOFYEAR`. Do not rename them to `DAY_OF_MONTH` or `DAY_OF_WEEK`: Calcite does not accept those names, so the renamed queries fail on Ignite 2 while both clusters are running.
- `TO_DATE`, `TO_TIMESTAMP`, `TO_CHAR`, `TIMESTAMPADD`, and `TIMESTAMPDIFF`. Check format patterns; see [Date Format Patterns](#date-format-patterns).
- `SYSTEM_RANGE`. Use `FROM SYSTEM_RANGE(1, 100)` instead of `FROM TABLE(SYSTEM_RANGE(1, 100))`.
- `UNION`, `UNION ALL`, non-recursive `WITH`, `LIMIT`, `OFFSET`, and `FETCH FIRST n ROWS ONLY`.
- Window functions and `WITH RECURSIVE` are not available on either engine, so no Ignite 2 query uses them.
- A query that contains more than one statement is rejected by both engines.

GridGain 8 also offers SQL features that Calcite does not, including `ILIKE`, `LOCATE`, `DATEADD`, `DATEDIFF`, `PARSEDATETIME`, `FORMATDATETIME`, adding an integer to a `DATE`, `COPY` for bulk loading, `SET STREAMING` for JDBC and ODBC, and full-text search through `TextQuery`.

## Planning the Migration

To estimate the work before you start:

1. *Search the code.* Search your queries, DDL, and connection strings for the constructs on this page, such as `/*+`, `FILTER (WHERE`, `ROLLUP`, `INTERSECT ALL`, `GROUP BY` followed by a number, `MERGE ... USING`, `CHAR(n)`, and the function names in [Scalar Functions](#scalar-functions). Then list every join and subquery between `PARTITIONED` tables that does not use the affinity key. To fix the items on that list, you need to know which tables are colocated.
2. *Find failing queries.* Start one GridGain 8 node, apply your DDL, and run every query prefixed with `EXPLAIN`. `EXPLAIN` plans the query without reading data. Each query that fails is a construct from [Queries That Fail](#queries-that-fail). Error code `1001` means a parsing error, and `1002` means an unsupported operation.
3. *Compare results.* Run every query on the Ignite 2 cluster and on a GridGain 8 cluster with the same data and the same number of nodes as production. Compare the number of rows and a checksum of each result. The [queries that return different results](#queries-that-return-different-results) do not fail, so a comparison is needed to find them. A query that is correct on two nodes can be incorrect on more.
4. *Test memory use.* After you rewrite the queries, run them at production load and set the [SQL memory quota](#sql-memory-quota).

This page describes the Calcite engine in Apache Ignite 2.18. The functions that Calcite supports differ between Ignite 2 releases; Ignite 2.17, for example, lacks `TO_DATE`, `TO_TIMESTAMP`, `TO_CHAR`, and `GROUP BY` by column position. If you run an earlier release, check against that release.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
