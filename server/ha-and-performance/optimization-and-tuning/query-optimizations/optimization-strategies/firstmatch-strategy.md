# FirstMatch Strategy

`FirstMatch` is an execution strategy for [Semi-join subqueries](../subquery-optimizations/semi-join-subquery-optimizations.md).

## The Idea

It is similar to how `IN/EXISTS` subqueries were executed in MySQL 5.x.

Let's take the usual example of a search for countries with big cities:

```sql
SELECT * FROM Country 
WHERE Country.code IN (SELECT City.Country 
                       FROM City 
                       WHERE City.Population > 1*1000*1000)
      AND Country.continent='Europe'
```

Suppose our execution plan is to find countries in Europe, and then, for each found country, check if it has any big cities. Regular inner join execution will look as follows:

![firstmatch-inner-join](../../../../.gitbook/assets/firstmatch-inner-join.png)

Since Germany has two big cities (in this diagram), it will be put into the query output twice. This is not correct, `SELECT ... FROM Country` should not produce the same country record twice. The `FirstMatch` strategy avoids the production of duplicates by short-cutting execution as soon as the first genuine match is found:

![firstmatch-firstmatch](../../../../.gitbook/assets/firstmatch-firstmatch.png)

Note that the short-cutting has to take place after `Using where` has been applied. It would have been wrong to short-cut after we found _Trier_.

## FirstMatch in Action

The `EXPLAIN` for the above query looks as follows:

```sql
MariaDB [world]> EXPLAIN SELECT * FROM Country WHERE Country.code IN 
  (select City.Country from City where City.Population > 1*1000*1000)
    AND Country.continent='Europe';
+----+-------------+---------+------+--------------------+-----------+---------+--------------------+------+----------------------------------+
| id | select_type | table   | type | possible_keys      | key       | key_len | ref                | rows | Extra                            |
+----+-------------+---------+------+--------------------+-----------+---------+--------------------+------+----------------------------------+
|  1 | PRIMARY     | Country | ref  | PRIMARY,continent  | continent | 17      | const              |   60 | Using index condition            |
|  1 | PRIMARY     | City    | ref  | Population,Country | Country   | 3       | world.Country.Code |   18 | Using where; FirstMatch(Country) |
+----+-------------+---------+------+--------------------+-----------+---------+--------------------+------+----------------------------------+
2 rows in set (0.00 sec)
```

`FirstMatch(Country)` in the Extra column means that _as soon as we have produced one matching record combination, short-cut the execution and jump back to the Country_ table.

The `FirstMatch` query plan is similar to one you would get in MySQL:

```sql
MySQL [world]> EXPLAIN SELECT * FROM Country  WHERE Country.code IN 
  (select City.Country from City where City.Population > 1*1000*1000) 
   AND Country.continent='Europe';
+----+--------------------+---------+----------------+--------------------+-----------+---------+-------+------+------------------------------------+
| id | select_type        | table   | type           | possible_keys      | key       | key_len | ref   | rows | Extra                              |
+----+--------------------+---------+----------------+--------------------+-----------+---------+-------+------+------------------------------------+
|  1 | PRIMARY            | Country | ref            | continent          | continent | 17      | const |   60 | Using index condition; Using where |
|  2 | DEPENDENT SUBQUERY | City    | index_subquery | Population,Country | Country   | 3       | func  |   18 | Using where                        |
+----+--------------------+---------+----------------+--------------------+-----------+---------+-------+------+------------------------------------+
2 rows in set (0.01 sec)
```

These two particular query plans will execute in the same time.

## Difference between FirstMatch and IN->EXISTS

The general idea behind the `FirstMatch` strategy is the same as the one behind the `IN->EXISTS` transformation, however, `FirstMatch` has several advantages:

* Equality propagation works across semi-join bounds, but not subquery bounds. Therefore, converting a subquery to semi-join and using `FirstMatch` can still give a better execution plan.
* There is only one way to apply the `IN->EXISTS` strategy and MySQL will do it unconditionally. With `FirstMatch`, the optimizer can make a choice between whether it should run the `FirstMatch` strategy as soon as all tables used in the subquery are in the join prefix, or at some later point in time.

## FirstMatch Factsheet

* The `FirstMatch` strategy works by executing the subquery and short-cutting its execution as soon as the first match is found.
* This means, subquery tables must be after all of the parent select's tables that are referred from the subquery predicate.
* `EXPLAIN` shows `FirstMatch` as "`FirstMatch(tableN)`".
* The strategy can handle correlated subqueries.
* But it cannot be applied if the subquery has meaningful `GROUP BY` and/or aggregate functions.
* Use of the `FirstMatch` strategy is controlled with the `firstmatch=on|off` flag in the [optimizer\_switch](../../system-variables/server-system-variables.md#optimizer_switch) variable.

## See Also

* [Semi-join subquery optimizations](../subquery-optimizations/semi-join-subquery-optimizations.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
