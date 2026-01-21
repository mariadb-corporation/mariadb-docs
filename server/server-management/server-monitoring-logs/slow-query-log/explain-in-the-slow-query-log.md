---
description: >-
  Describes how to configure MariaDB to automatically write the `EXPLAIN` plan
  for slow queries to the log using the `log_slow_verbosity` system variable.
---

# EXPLAIN in the Slow Query Log

### Additional Columns in MariaDB 10.1 and Later

Starting from MariaDB 10.1.0, the `EXPLAIN` output in the slow query log includes two additional columns: `r_rows` and `r_filtered`

When a user manually executes the standard `EXPLAIN` statement, these columns are not displayed. Instead, they come from the `ANALYZE` statement, which runs the query and returns actual runtime statistics.

MariaDB uses `ANALYZE` statement internally to generate the `EXPLAIN` output when a query is stored in the slow query log. As a result, the slow query log may contain both estimated and actual execution statistics.

For more information about `r_rows` and `r_filtered`  columns, see the [ANALYZE Statement](../../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/analyze-statement.md) page.

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
# User@Host: user[user] @ test.domain.com [10.6.184.141]
# Thread_id: 75816 Schema: db QC_hit: No
# Query_time: 420.906319 Lock_time: 0.086885 Rows_sent: 0 Rows_examined: 9734191
# Rows_affected: 0
#
# explain: id select_type table type possible_keys key key_len ref rows r_rows filtered r_filtered Extra
# explain: 1 SIMPLE tab ALL a_timestamp_indx NULL NULL NULL 9330481 9734191.00 100.00 55.55 Using where
#
SET timestamp=1535157447;
delete from tab where a_timestamp < (unix_timestamp(now())-14400)*1000000;
```

`EXPLAIN` lines start with `explain:`.

### See Also

* [MDEV-407](https://jira.mariadb.org/browse/MDEV-407)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
