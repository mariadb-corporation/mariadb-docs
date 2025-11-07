# Query Accelerator

{% hint style="warning" %}
MariaDB Query Accelerator is an **Alpha release**. Do not use it in production environments.\
Query Accelerator works only in **ColumnStore 25.10.0** and with **MariaDB Enterprise Server 11.8.3+**.
{% endhint %}

## What is Query Accelerator

Query Accelerator allows MariaDB to use ColumnStore to execute queries that are otherwise executed by InnoDB. Under the hood, Columnstore:

* receives a query;
* searches for applicable Engine Independent statistics for InnoDB table index column;
* applies RBO[^1] rule to transform its InnoDB tables into a number of `UNION` queries over non-overlapping ranges of a suitable InnoDB table index;
* retrieves the data in parallel from MariaDB, and runs it using Columnstore runtime.

## Queries Benefitting From Query Accelerator

Query Accelerator improves the performance of queries that use aggregation functions, for instance `SUM`, `AVG`, `MIN`, `MAX`, and `GROUP BY`, where the performance overhead of pulling the data out of InnoDB can be overcome by the performance optimization of running in the ColumnStore engine.

This avoids the bottleneck/pipeline of having to move data out of InnoDB and into ColumnStore. Query Accelerator strives to parallelize data out of InnoDB, by utilizing table statistics to optimize multiple threads to data ranges on disk. If the InnoDB table in question uses an index, Query Accelerator is able to get the data much faster.

Example of a query benefitting from Query Accelerator (assuming `column_a` is indexed):

```sql
SELECT column_a, SUM(column_b) FROM innodb_table GROUP BY column_a
```

The effectiveness of Query Accelerator can vary depending on the type of queries you run and the specific characteristics of your database schema. Certain types of queries or configurations may not benefit from Query Accelerator, or could potentially experience decreased performance. It's essential to understand when Query Accelerator is most advantageous and when traditional InnoDB operations might be more efficient. Consider the following points to optimize query performance with Query Accelerator:

* Make sure your query uses tables that are indexed, and the index key has the first integer column.
* Also, run `ANALYZE TABLE` before running Query Accelerator.

## Queries not to run in Query Accelerator

### Performance Issues

Performance issues occur for queries like this:

```sql
 SELECT column_a FROM tbl WHERE column_a = column_b 
```

InnoDB handles such comparison much better than ColumnStore in general, and in Query Accelerator, that would be even worse.

* Generally, if your query takes longer than a minute in InnoDB, try Query Accelerator.

### Queries not Working in Query Accelerator

Query Accelerator has the same limitations as ColumnStore in general, in that it has a limited set of [functions](../reference/columnstore-distributed-functions.md) and [data types](../reference/columnstore-data-types.md) it can handle. Therefore, be aware of

* syntax or functions that Columnstore does not support;
* data types ColumnStore does not support.

## Enabling Query Accelerator

{% stepper %}
{% step %}
**Edit the MariaDB configuration file (my.cnf or my.ini)**

Locate (or create) the mariadb section, and add a line enabling Query Accelerator, like this:

```ini
[mariadb]
columnstore_innodb_queries_use_mcs = on
```

Restart MariaDB Server for the change to take effect.
{% endstep %}

{% step %}
**Run queries to turn on Query Accelerator**

Set these parameters in a client session:

```sql
SET columnstore_unstable_optimizer=ON;
SET optimizer_switch="index_merge=off,index_merge_union=off,index_merge_sort_union=off,index_merge_intersection=off,index_merge_sort_intersection=off,index_condition_pushdown=off,derived_merge=off,derived_with_keys=off,firstmatch=off,loosescan=off,materialization=on,in_to_exists=off,semijoin=off,partial_match_rowid_merge=off,partial_match_table_scan=off,subquery_cache=off,mrr=off,mrr_cost_based=off,mrr_sort_keys=off,outer_join_with_cache=off,semijoin_with_cache=off,join_cache_incremental=off,join_cache_hashed=off,join_cache_bka=off,optimize_join_buffer_size=off,table_elimination=off,extended_keys=off,exists_to_in=off,orderby_uses_equalities=off,condition_pushdown_for_derived=on,split_materialized=off,condition_pushdown_for_subquery=off,rowid_filter=off,condition_pushdown_from_having=on,not_null_range_scan=off,hash_join_cardinality=off,cset_narrowing=off,sargable_casefold=off";
```

{% hint style="info" %}
In future versions of Query Accelerator, those `SET` statements will be in stored procedures, allowing to turn Query Accelerator on and off with simpler commands.
{% endhint %}

{% hint style="warning" %}
To use Query Accelerator just for one query, you have to run those `SET` statements per query, not per session. Setting them per session effectively disables the MariaDB Optimizer for subsequent queries that ColumnStore cannot execute.
{% endhint %}
{% endstep %}
{% endstepper %}

## Enabling Processing for InnoDB Tables

There must be engine-independent statistics for an InnoDB table index column so that it can be used for Query Accelerator.

```sql
ANALYZE TABLE table_name PERSISTENT FOR COLUMNS (column_name) indexes();
```

## Control Client Session Variables and Parameters

* `columnstore_unstable_optimizer`\
  \
  enables unstable optimizer that is required for Query Accelerator RBO[^1] rule.
* `columnstore_select_handler` \
  enables/disables ColumnStore processing for InnoDB tables.
* `columnstore_query_accel_parallel_factor`\
  controls the number of parallel ranges to be used for Query Accelerator.

{% hint style="warning" %}
Watch out for `max_connections`. If you set `columnstore_query_accel_parallel_factor` to a high value, you may need to increase `max_connections` to avoid connection pool exhaustion.
{% endhint %}

## Verifying That Query Accelerator is Being Used

There are two ways to verify Query Accelerator is being used:

1. Use `select mcs_get_plan('rules')` to get a list of the rules that were applied to the query.
2. Look for patterns like `derived table - $added_sub_#db_name_#table_name_X` in the optimized plan using `select mcs_get_plan('optimized')`.

##  Query Accelerator Quick Start
```sql
# In MariaDB shell
CREATE DATABASE IF NOT EXISTS test; use test;
CREATE TABLE IF NOT EXISTS test.customer_indexed (  `c_d_id` int(2) NOT NULL, `c_w_id` int(6) NOT NULL, `c_first` varchar(16) , `c_middle` char(2) , `c_last` varchar(16) , `c_street_1` varchar(20) , `c_street_2` varchar(20) , `c_city` varchar(20) , `c_state` char(2) , `c_zip` int(5) , `c_phone` char(16) , `c_since` datetime DEFAULT NULL, `c_credit` char(2) , `c_credit_lim` decimal(12,2) DEFAULT NULL, `c_discount` decimal(4,4) DEFAULT NULL, `c_balance` decimal(12,2) DEFAULT NULL, `c_ytd_payment` decimal(12,2) DEFAULT NULL, `c_payment_cnt` int(8) DEFAULT NULL, `c_delivery_cnt` int(8) DEFAULT NULL, `c_data` varchar(500)) ENGINE=InnoDB DEFAULT CHARSET=latin1;
INSERT INTO test.customer_indexed  SELECT  ROUND(RAND() * 42000, 0), ROUND(RAND() * 42000, 0), substring(MD5(RAND()*1000000000),1,16), substring(MD5(RAND()),1,2), substring(MD5(RAND()*1000000000),1,16), substring(MD5(RAND()*1000000000),1,20), substring(MD5(RAND()*1000000000),1,20), substring(MD5(RAND()*1000000000),1,20), substring(MD5(RAND()),1,2), ROUND(RAND() * 42000, 0), substring(MD5(RAND()),1,16), CURRENT_TIMESTAMP - INTERVAL FLOOR(RAND() * 365 * 24 * 60 *60) SECOND, substring(MD5(RAND()),1,2), ROUND(RAND() * 9999999999, 2), ROUND(RAND() * 0, 4), ROUND(RAND() * 9999999999, 2), ROUND(RAND() * 9999999999, 2), ROUND(RAND() * 42000, 0), ROUND(RAND() * 42000, 0), substring(MD5(RAND()*1000000000),1,500) FROM seq_1_to_8000000; -- 3.5 min
ALTER TABLE test.customer_indexed ADD INDEX idx_fast (`c_zip`, `c_payment_cnt`); -- ~1.5 min
-- baseline 
select c_zip, sum(c_payment_cnt)  from test.customer_indexed group by c_zip order by c_zip ;  --2.6s 

# Turn on Query Accelerator - On CLI
sed -i 's/^#columnstore_innodb_queries_use_mcs = on/columnstore_innodb_queries_use_mcs = on/' /etc/my.cnf.d/columnstore.cnf
systemctl restart mariadb

# In MariaDB shell
use test;
ANALYZE table test.customer_indexed persistent for columns (c_zip,c_payment_cnt) indexes(); --8s
select table_name, column_name, hist_type from mysql.column_stats where table_name="customer_indexed"; show variables like "%columnstore_innodb_queries_use_mcs%";
# Logout of MariaDB shell and relogin 
SET columnstore_unstable_optimizer=ON;
SET optimizer_switch='index_merge=off,index_merge_union=off,index_merge_sort_union=off,index_merge_intersection=off,index_merge_sort_intersection=off,index_condition_pushdown=off,derived_merge=off,derived_with_keys=off,firstmatch=off,loosescan=off,materialization=on,in_to_exists=off,semijoin=off,partial_match_rowid_merge=off,partial_match_table_scan=off,subquery_cache=off,mrr=off,mrr_cost_based=off,mrr_sort_keys=off,outer_join_with_cache=off,semijoin_with_cache=off,join_cache_incremental=off,join_cache_hashed=off,join_cache_bka=off,optimize_join_buffer_size=off,table_elimination=off,extended_keys=off,exists_to_in=off,orderby_uses_equalities=off,condition_pushdown_for_derived=on,split_materialized=off,condition_pushdown_for_subquery=off,rowid_filter=off,condition_pushdown_from_having=on,not_null_range_scan=off,hash_join_cardinality=off,cset_narrowing=off,sargable_casefold=off';
select c_zip, sum(c_payment_cnt)  from test.customer_indexed group by c_zip order by c_zip ; -- 0.7s


# Turn off Query Accelerator - On CLI
sed -i 's/^columnstore_innodb_queries_use_mcs = on/#columnstore_innodb_queries_use_mcs = on/' /etc/my.cnf.d/columnstore.cnf
systemctl restart mariadb
```

##  Quick Verifications

This example shows a sum(x) group by y query run ~2.6s in InnoDB with indexes and run 3x faster via columnstore query acceleration ( ~0.7s ) with enough cpu and a high enough parallel_factor.

1) Tail the ColumnStore log debug.log, and confirm parallel access to innodb
```sql
tail -f /var/log/mariadb/columnstore/debug.log
```
increase or decrease parallelism with columnstore_ces_optimization_parallel_factor
remember to keep in mind you need enough max_connections in mariadb server
```sql
set columnstore_ces_optimization_parallel_factor=100;
```

2) Check execution plan via explain FORMAT=JSON says "Pushed select"
```sql
explain FORMAT=JSON select c_zip, sum(c_payment_cnt)  from test.customer_indexed group by c_zip order by c_zip ;
+------------------------------------------------------------------------------------------------------+
| EXPLAIN                                                                                              |
+------------------------------------------------------------------------------------------------------+
| {
  "query_block": {
    "select_id": 1,
    "table": {
      "message": "Pushed select"
    }
  }
} |
+------------------------------------------------------------------------------------------------------+
```

3) Validate mcs_get_plan shows parallel parallel_ces and detailed columnstore execution plan shows "derived table"
```sql
select mcs_get_plan('rules');
+-----------------------+
| mcs_get_plan('rules') |
+-----------------------+
| parallel_ces          |
+-----------------------+


select mcs_get_plan('optimized');
+-----------------------+
| mcs_get_plan('rules') |
+-----------------------+
...
>>From Tables
  derived table - $added_sub_test_customer_indexed_0
```


{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}

[^1]: Rule-based optimizer
