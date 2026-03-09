# Conversion of Big IN Predicates Into Subqueries

Starting from [MariaDB 10.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/what-is-mariadb-103), the optimizer converts certain big IN predicates into IN subqueries.

That is, an IN predicate in the form

```sql
COLUMN [NOT] IN (const1, const2, .... )
```

is converted into an equivalent IN-subquery:

```
column [NOT] IN (select ... from temporary_table)
```

which opens new opportunities for the query optimizer.

The conversion happens if the following conditions are met:

* the IN list has more than 1000 elements (One can control it through the [in\_predicate\_conversion\_threshold](../../system-variables/server-system-variables.md#in_predicate_conversion_threshold) parameter).
* the \[NOT] IN condition is at the top level of the WHERE/ON clause.

## Controlling the Optimization

* The optimization is on by default. [MariaDB 10.3.18](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.3/10.3.18) (and debug builds prior to that) introduced the [in\_predicate\_conversion\_threshold](../../system-variables/server-system-variables.md#in_predicate_conversion_threshold) variable. Set to `0` to disable the optimization.

## Benefits of the Optimization

If `column` is a key-prefix, MariaDB optimizer will process the condition

```sql
COLUMN [NOT] IN (const1, const2, .... )
```

by trying to construct a range access. If the list is large, the analysis may take a lot of memory and CPU time. The problem gets worse when `column` is a part of a multi-column index and the query has conditions on other parts of the index.

Conversion of IN predicates into subqueries bypass the range analysis, which means the query optimization phase will use less CPU and memory.

Possible disadvantages of the conversion are are:

* The optimization may convert 'IN LIST elements' key accesses to a table scan (if there is no other usable index for the table)
* The estimates for the number of rows matching the `IN (...)` are less precise.

## See Also

* [IN operator](../../../../reference/sql-structure/operators/comparison-operators/in.md)

## Links

[MDEV-12176](https://jira.mariadb.org/browse/MDEV-12176)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
