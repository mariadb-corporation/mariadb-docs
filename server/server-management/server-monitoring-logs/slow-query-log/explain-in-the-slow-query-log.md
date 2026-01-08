---
description: >-
  Describes how to configure MariaDB to automatically write the `EXPLAIN` plan
  for slow queries to the log using the `log_slow_verbosity` system variable.
---

# EXPLAIN in the Slow Query Log

### Switching it On

[EXPLAIN](../../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain.md) output can be switched on by specifying the `explain` keyword in the [log\_slow\_verbosity](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#log_slow_verbosity) system variable. Alternatively, you can set with the `log-slow-verbosity` command line argument.

```ini
[mysqld]
log-slow-verbosity=query_plan,explain
```

EXPLAIN output will only be recorded if the slow query log is written to a file (and not to a table - see [Writing logs into tables](../writing-logs-into-tables.md)). This limitation also applies to other extended statistics that are written into the slow query log.

### What it Looks Like

When explain recording is on, slow query log entries look like this:

```
# Time: 131112 17:03:32
# User@Host: root[root] @ localhost []
# Thread_id: 2  Schema: dbt3sf1  QC_hit: No
# Query_time: 5.524103  Lock_time: 0.000337  Rows_sent: 1  Rows_examined: 65633
#
# explain: id   select_type     table   type    possible_keys   key     key_len ref     rows    Extra
# explain: 1    SIMPLE  nation  ref     PRIMARY,n_name  n_name  26      const   1       Using where; Using index
# explain: 1    SIMPLE  customer        ref     PRIMARY,i_c_nationkey   i_c_nationkey   5       dbt3sf1.nation.n_nationkey      3145    Using index
# explain: 1    SIMPLE  orders  ref     i_o_custkey     i_o_custkey     5       dbt3sf1.customer.c_custkey      7       Using index
#
SET TIMESTAMP=1384261412;
SELECT COUNT(*) FROM customer, orders, nation WHERE c_custkey=o_custkey AND c_nationkey=n_nationkey AND n_name='GERMANY';
```

`EXPLAIN` lines start with `explain:`.

### See Also

* [MDEV-407](https://jira.mariadb.org/browse/MDEV-407)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
