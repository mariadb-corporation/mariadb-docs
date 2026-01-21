# Optimizer Trace Guide

## Optimizer Trace Guide

The optimizer trace uses the JSON format. It is basically a structured log file showing what actions were taken by the query optimizer.

### A Basic Example

Let's take a simple query:

```
MariaDB> explain select * from t1 where a<10;
+------+-------------+-------+-------+---------------+------+---------+------+------+-----------------------+
| id   | select_type | table | type  | possible_keys | key  | key_len | ref  | rows | Extra                 |
+------+-------------+-------+-------+---------------+------+---------+------+------+-----------------------+
|    1 | SIMPLE      | t1    | range | a             | a    | 5       | NULL | 10   | Using index condition |
+------+-------------+-------+-------+---------------+------+---------+------+------+-----------------------+
```

One can see the full trace [here](basic-optimizer-trace-example.md). Taking only the component names, one gets:

```
MariaDB> select * from information_schema.optimizer_trace limit 1\G
*************************** 1. row ***************************
                            QUERY: select * from t1 where a<10
                            TRACE: 
{
  "steps": [
    {
      "join_preparation": { ... }
    },
    {
      "join_optimization": {
        "select_id": 1,
        "steps": [
          { "condition_processing": { ... } },
          { "table_dependencies": [ ... ] },
          { "ref_optimizer_key_uses": [ ... ] },
          { "rows_estimation": [
              {
                "range_analysis": {
                   "analyzing_range_alternatives" : { ... },
                  "chosen_range_access_summary": { ... },
                },
                "selectivity_for_indexes" : { ... },
                "selectivity_for_columns" : { ... }
              }
            ]
          },
          { "considered_execution_plans": [ ... ] },
          { "attaching_conditions_to_tables": { ... } }
         ]
      }
    },
    {
      "join_execution": { ... }
    }
  ]
}
```

### Trace Structure

For each SELECT, there are two "Steps":

* `join_preparation`
* `join_optimization`

Join preparation shows early query rewrites. `join_optmization` is where most of the query optimizations are done. They are:

* `condition_processing` - basic rewrites in WHERE/ON conditions.
* `ref_optimizer_key_uses` - Construction of possible ways to do ref and eq\_ref accesses.
* `rows_estimation` - Consideration of range and index\_merge accesses.
* `considered_execution_plans` - Join optimization itself, that is, choice of the join order.
* `attaching_conditions_to_tables` - Once the join order is fixed, parts of the WHERE clause are "attached" to tables to filter out rows as early as possible.

The above steps are for just one SELECT. If the query has subqueries, each SELECT will have these steps, and there will be extra steps/rewrites to handle the subquery construct itself.

### Extracting Trace Components

If you are interested in some particular part of the trace, MariaDB has two functions that come in handy:

* [JSON\_EXTRACT](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/sql-functions/special-functions/json-functions/json_extract.md) extracts a part of JSON document
* [JSON\_DETAILED](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/sql-functions/special-functions/json-functions/json_detailed.md) presents it in a user-readable way.

For example, the contents of the `analyzing_range_alternatives` node can be extracted like so:

```
MariaDB> select JSON_DETAILED(JSON_EXTRACT(trace, '$**.analyzing_range_alternatives')) 
   ->   from INFORMATION_SCHEMA.OPTIMIZER_TRACE\G
*************************** 1. row ***************************
JSON_DETAILED(JSON_EXTRACT(trace, '$**.analyzing_range_alternatives')): [
    {
        "range_scan_alternatives": 
        [
            {
                "index": "a_b_c",
                "ranges": 
                [
                    "(1) <= (a,b) < (4,50)"
                ],
                "rowid_ordered": false,
                "using_mrr": false,
                "index_only": false,
                "rows": 4,
                "cost": 6.2509,
                "chosen": true
            }
        ],
        "analyzing_roworder_intersect": 
        {
            "cause": "too few roworder scans"
        },
        "analyzing_index_merge_union": []
    }
]
```

### Examples of Various Information in the Trace

#### Basic Rewrites

A lot of applications construct database query text on the fly, which sometimes means that the query has constructs that are repetitive or redundant. In most cases, the optimizer will be able to remove them. One can check the trace to be sure:

```
explain select * from t1 where not (col1 >= 3);
```

Optimizer trace will show:

```
"steps": [
  {
    "join_preparation": {
      "select_id": 1,
      "steps": [
        {
          "expanded_query": "select t1.a AS a,t1.b AS b,t1.col1 AS col1 from t1 where t1.col1 < 3"
        }
```

Here, one can see that `NOT` was removed.

Similarly, one can also see that `IN(...)` with one element is the same as equality:

```
explain select * from t1 where col1  in (1);
```

will show

```
"join_preparation": {
    "select_id": 1,
    "steps": [
      {
        "expanded_query": "select t1.a AS a,t1.b AS b,t1.col1 AS col1 from t1 where t1.col1 = 1"
```

On the other hand, converting an UTF-8 column to UTF-8 is not removed:

```
explain select * from t1 where convert(utf8_col using utf8) = 'hello';
```

will show

```
"join_preparation": {
    "select_id": 1,
    "steps": [
      {
        "expanded_query": "select t1.a AS a,t1.b AS b,t1.col1 AS col1,t1.utf8_col AS utf8_col from t1 where convert(t1.utf8_col using utf8) = 'hello'"
          }
```

so redundant `CONVERT` calls should be used with caution.

#### VIEW Processing

MariaDB has two algorithms to handle VIEWs: merging and materialization. If you run a query that uses a VIEW, the trace will have either

```
"view": {
              "table": "view1",
              "select_id": 2,
              "algorithm": "merged"
            }
```

or

```
{
            "view": {
              "table": "view2",
              "select_id": 2,
              "algorithm": "materialized"
            }
          },
```

depending on which algorithm was used.

#### Range Optimizer - What Ranges Will Be Scanned

The MariaDB optimizer has a complex part called the Range Optimizer. This is a module that examines WHERE (and ON) clauses and constructs index ranges that need to be scanned to answer the query. The rules for constructing the ranges are quite complex.

An example: Consider a table

```
CREATE TABLE some_events ( 
  start_date DATE, 
  end_date DATE, 
  ...
  key (start_date, end_date)
);
```

and a query:

```
explain select * from some_events where start_date >= '2019-09-10' and end_date <= '2019-09-14';
+------+-------------+-------------+------+---------------+------+---------+------+------+-------------+
| id   | select_type | table       | type | possible_keys | key  | key_len | ref  | rows | Extra       |
+------+-------------+-------------+------+---------------+------+---------+------+------+-------------+
|    1 | SIMPLE      | some_events | ALL  | start_date    | NULL | NULL    | NULL | 1000 | Using where |
+------+-------------+-------------+------+---------------+------+---------+------+------+-------------+
```

One might think that the optimizer would be able to use the restrictions on both _start\_date_ and _end\_date_ to construct a narrow range to be scanned. But this is not so, one of the restrictions creates a left-endpoint range and the other one creates a right-endpoint range, hence they cannot be combined.

```
select 
   JSON_DETAILED(JSON_EXTRACT(trace, '$**.analyzing_range_alternatives')) as trace 
from information_schema.optimizer_trace\G
*************************** 1. row ***************************
trace: [
    {
        "range_scan_alternatives": 
        [
            {
                "index": "start_date",
                "ranges": 
                [
                    "(2019-09-10,NULL) < (start_date,end_date)"
                ],
...
```

the potential range only uses one of the bounds.

#### Ref Access Options

Index-based Nested-loops joins are called "ref access" in the MariaDB optimizer.

The optimizer analyzes the WHERE/ON conditions and collects all equality conditions that can be used by ref access using some index.

The list of conditions can be found in the `ref_optimizer_key_uses` node.\
(TODO example)

#### Join Optimization

The join optimizer's node is named `considered_execution_plans`.

The optimizer constructs the join orders in a left-to-right fashion. That is, if the query is a join of three tables:

```
SELECT * FROM t1, t2, t3 WHERE ...
```

then the optimizer will

* Pick the first table (say, it is t1),
* consider adding another table (say, t2), and construct a prefix "t1, t2"
* consider adding the third table (t3), and constructing a prefix "t1, t2, t3", which is a complete join plan\
  Other join orders will be considered as well.

The basic operation here is: "given a join prefix of tables A,B,C ..., try adding table X to it".\
In JSON, it looks like this:

```
{
        "plan_prefix": ["t1", "t2"],
        "table": "t3",
        "best_access_path": {
          "considered_access_paths": [
            {
              ...
            }
          ]
        }
      }
```

(search for `plan_prefix` followed by `table`).

If you are interested in how the join order of #t1,t2,t3

## was constructed (or not constructed), you need to search for these patterns:

* `"plan_prefix":[], "table":"t1"`
* `"plan_prefix":["t1"], "table":"t2"`
* `"plan_prefix":["t1", "t2"], "table":"t3"`

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
