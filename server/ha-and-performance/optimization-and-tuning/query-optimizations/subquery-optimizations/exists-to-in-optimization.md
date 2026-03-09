# EXISTS-to-IN Optimization

MySQL (including MySQL 5.6) has only one execution strategy for EXISTS subqueries. The strategy is essentially the straightforward, "naive" execution, without any rewrites.

[MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/changes-improvements-in-mariadb-5-3) introduced a rich set of optimizations for IN subqueries. Since then, it makes sense to convert an EXISTS subquery into an IN so that the new optimizations can be used.

`EXISTS` will be converted into `IN` in two cases:

1. Trivially correlated EXISTS subqueries
2. Semi-join EXISTS

We will now describe these two cases in detail

## Trivially-correlated EXISTS subqueries

Often, EXISTS subquery is correlated, but the correlation is trivial. The subquery has form

```sql
EXISTS (SELECT ...  FROM ... WHERE outer_col= inner_col AND inner_where)
```

and "outer\_col" is the only place where the subquery refers to outside fields.\
In this case, the subquery can be re-written into uncorrelated IN:

```sql
outer_col IN (SELECT inner_col FROM ... WHERE inner_where)
```

(`NULL` values require some special handling, see below). For uncorrelated IN subqueries, MariaDB is able a cost-based choice between two execution strategies:

* [IN-to-EXISTS](non-semi-join-subquery-optimizations.md#the-in-to-exists-transformation) (basically, convert back into EXISTS)
* [Materialization](non-semi-join-subquery-optimizations.md#materialization-for-non-correlated-in-subqueries)

That is, converting trivially-correlated `EXISTS` into uncorrelated `IN` gives query optimizer an option to use Materialization strategy for the subquery.

Currently, EXISTS->IN conversion works only for subqueries that are at top level of the WHERE clause, or are under NOT operation which is directly at top level of the WHERE clause.

## Semi-join EXISTS subqueries

If `EXISTS` subquery is an AND-part of the `WHERE` clause:

```sql
SELECT ... FROM outer_tables WHERE EXISTS (SELECT ...) AND ...
```

then it satisfies the main property of [semi-join subqueries](semi-join-subquery-optimizations.md):

_with semi-join subquery, we're only interested in records of outer\_tables that have matches in the subquery_

Semi-join optimizer offers a rich set of execution strategies for both correlated and uncorrelated subqueries. The set includes FirstMatch strategy which is an equivalent of how EXISTS suqueries are executed, so we do not lose any opportunities when converting an EXISTS subquery into a semi-join.

In theory, it makes sense to convert all kinds of EXISTS subqueries: convert both correlated and uncorrelated ones, convert irrespectively of whether the subquery has inner=outer equality.

In practice, the subquery will be converted only if it has inner=outer equality. Both correlated and uncorrelated subqueries are converted.

## Handling of NULL values

TODO: rephrase this:

* IN has complicated NULL-semantics. NOT EXISTS doesn't.
* EXISTS-to-IN adds IS NOT NULL before the subquery predicate, when required

## Control

The optimization is controlled by the `exists_to_in` flag in [optimizer\_switch](../../system-variables/server-system-variables.md#optimizer_switch). Before [MariaDB 10.0.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.12), the optimization was OFF by default. Since [MariaDB 10.0.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/10.0.12), it has been ON by default.

## Limitations

EXISTS-to-IN doesn't handle

* subqueries that have GROUP BY, aggregate functions, or HAVING clause
* subqueries are UNIONs
* a number of degenerate edge cases

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
