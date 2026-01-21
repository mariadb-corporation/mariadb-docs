---
description: >-
  Details the specific quality assurance processes and testing strategies used
  to validate the MariaDB query optimizer's performance.
---

# Optimizer Quality

{% include "../../../../.gitbook/includes/this-page-contains-backgrou....md" %}

## Generating the Queries <a href="#generating-the-queries" id="generating-the-queries"></a>

There are 5 primary SQL grammars available for testing the Optimizer:

* `optimizer_nosubquery.yy` generates random queries with no subselects, with up to 3-way join and with various SQL clauses such as aggregates, `GROUP BY`, `HAVING`, and `LIMIT` .
* `optimizer_subquery.yy` generates queries with subselects with up to 2 levels of nesting. Subqueries are placed in various locations, such as in the `SELECT` list, in the `ON` clause, etc. Aggregates, `LIMIT`, `HAVING`, etc. are used if allowed by the server.
* `optimizer_subquery.yy` generates outer joins of various depths.
* `range_optimizer.yy` tests the range optimizer by joining several tables and generating various conditions on which range optimization is likely to be applied.
* `range_optimizer2.yy` tests the range optimizer by generating single-table queries that contain a lot of range-optimizable clauses. Avoiding joins allows the single table to be arbitrarily large, this allowing for more interesting range overlaps.

## Validating the Results <a href="#validating-the-results" id="validating-the-results"></a>

The RQG[^1] has two primary modes for validating the results:

* Using a reference implementation. This can be a PostgreSQL, JavaDB or another version or flavor of MySQL/Maria/Drizzle. Testing this way requires trusting external software that is not under our control. Also, it is sometimes difficult to determine which implementation has returned the correct result. Technically, 3 implementations can "vote" as to which is the correct result, but this is not reliable if the implementations all derive from one another.
* Executing the generated query using a different execution plan. This is usually achieved by disabling particular optimizations and thus "downgrading" the plan to a more basic, presumed stable one. It is assumed that a nested-loop-join that takes no advantage of indexes would always provide the correct result. The advantage of this approach is that there is no need for a reference implementation and the source of the wrong result can be obtained by diffing the original and the downgraded execution plan.

In addition to result set validation, there is a module which executes each generated `SELECT` in various contexts, such as as part of a union, stored procedure, trigger, etc. and makes sure that the query returns a correct result. This is most often used for testing subselects.

### Running a Complete Test Cycle <a href="#running-a-complete-test-cycle" id="running-a-complete-test-cycle"></a>

A test cycle is described in a configuration file called the CC file. The CC file contains a list of mysqld options to use, the list of grammars to use and other settings (e.g. storage engines, table sizes, etc.). The testing framework will then take a random permutation from the settings described in the file and run them as a RQG test for a predefined time, such as 10 minutes. This is repeated up to 100 times, each with a different random permutation. The PRNG seed for each run will also be different, so different queries will be generated for each run, in addition to using different mysqld options, engine, etc.

By default, all cycles include MyISAM, Aria and InnoDB, and some percentage are run under Valgrind. Cycles run with both `NULL` and `NOT NULL` fields and with and without simple views.

## Configuration for Join Cache Testing <a href="#configuration-for-join-cache-testing" id="configuration-for-join-cache-testing"></a>

`outer_join_with_cache` is always `ON`. `--join_cache_level` varies from `0` to `8`. `--join_buffer_size` varies between 1, 100, 1K, 10K and 100K. The `optimizer_no_subquery.yy`, `outer_join.yy` and `range_access.yy` grammars are used. Once semijoin is stable, `join_cache` + `semijoin` are tested with `optimizer_subquery.yy`.

## Configuration for MRR/ICP/DS-MRR-CPK Testing <a href="#configuration-for-mrricpds-mrr-cpk-testing" id="configuration-for-mrricpds-mrr-cpk-testing"></a>

`--optimizer_use_mrr` is ON, `mrr_sort_keys` is both `ON` and `OFF`, `index_condition_pushdown` is both ON and OFF, `join_cache_level` is between 0 and 8, `join_buffer_size` and `mrr_buffer_size` are 1, 100, 1K, 10K and 100K. `optimizer_no_subquery.yy`, `outer_join.yy`, `range_access.yy` and `range_access2.yy` grammars are used.

## Configuration for Subquery Testing <a href="#configuration-for-subquery-testing" id="configuration-for-subquery-testing"></a>

The `optimizer_no_subquery.yy` grammar is used. Each individual `optimizer_switch` related to subquery optimization may be disabled so that the "second best" plan is generated.

### See Also <a href="#see-also" id="see-also"></a>

* [RQG Documentation](http://github.com/RQG/RQG-Documentation/wiki/Category:RandomQueryGenerator)
* [RQG Performance Comparisons](benchmarks-and-long-running-tests/benchmarks/rqg-performance-comparisons.md)
* [RQG Extensions for MariaDB Features](rqg-extensions-for-mariadb.md)
* [QA Tools](qa-tools.md)
* [Worklog Quality Checklist Template](worklog-quality-checklist-template.md)

[^1]: Random Query Generator
