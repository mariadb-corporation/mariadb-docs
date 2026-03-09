# Table Pullout Optimization

Table pullout is an optimization for [Semi-join subqueries](semi-join-subquery-optimizations.md).

## The idea of Table Pullout

Sometimes, a subquery can be re-written as a join. For example:

```sql
SELECT *
FROM City 
WHERE City.Country IN (SELECT Country.Code
                       FROM Country 
                       WHERE Country.Population < 100*1000);
```

If we know that there can be, at most, one country with a given value of `Country.Code` (we can tell that if we see that table Country has a primary key or unique index over that column), we can re-write this query as:

```sql
SELECT City.* 
FROM 
  City, Country 
WHERE
 City.Country=Country.Code AND Country.Population < 100*1000;
```

## Table pullout in action

If one runs [EXPLAIN](../../../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain.md) for the above query in MySQL 5.1-5.6 or [MariaDB 5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.1/changes-improvements-in-mariadb-5-1)-5.2, they'll get this plan:

```sql
MySQL [world]> EXPLAIN SELECT * FROM City WHERE City.Country IN (SELECT Country.Code FROM Country WHERE Country.Population < 100*1000);
+----+--------------------+---------+-----------------+--------------------+---------+---------+------+------+-------------+
| id | select_type        | table   | type            | possible_keys      | key     | key_len | ref  | rows | Extra       |
+----+--------------------+---------+-----------------+--------------------+---------+---------+------+------+-------------+
|  1 | PRIMARY            | City    | ALL             | NULL               | NULL    | NULL    | NULL | 4079 | Using where |
|  2 | DEPENDENT SUBQUERY | Country | unique_subquery | PRIMARY,Population | PRIMARY | 3       | func |    1 | Using where |
+----+--------------------+---------+-----------------+--------------------+---------+---------+------+------+-------------+
2 rows in set (0.00 sec)
```

It shows that the optimizer is going to do a full scan on table `City`, and for each city it will do a lookup in table `Country`.

If one runs the same query in [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/5.3/changes-improvements-in-mariadb-5-3), they will get this plan:

```sql
MariaDB [world]> EXPLAIN SELECT * FROM City WHERE City.Country IN (SELECT Country.Code FROM Country WHERE Country.Population < 100*1000);
+----+-------------+---------+-------+--------------------+------------+---------+--------------------+------+-----------------------+
| id | select_type | table   | type  | possible_keys      | key        | key_len | ref                | rows | Extra                 |
+----+-------------+---------+-------+--------------------+------------+---------+--------------------+------+-----------------------+
|  1 | PRIMARY     | Country | range | PRIMARY,Population | Population | 4       | NULL               |   37 | Using index condition |
|  1 | PRIMARY     | City    | ref   | Country            | Country    | 3       | world.Country.Code |   18 |                       |
+----+-------------+---------+-------+--------------------+------------+---------+--------------------+------+-----------------------+
2 rows in set (0.00 sec)
```

The interesting parts are:

* Both tables have `select_type=PRIMARY`, and `id=1` as if they were in one join.
* The `Country` table is first, followed by the `City` table.

Indeed, if one runs EXPLAIN EXTENDED; SHOW WARNINGS, they will see that the subquery is gone and it was replaced with a join:

```sql
MariaDB [world]> SHOW warnings\G
*************************** 1. row ***************************
  Level: Note
   Code: 1003
Message: SELECT `world`.`City`.`ID` AS `ID`,`world`.`City`.`Name` AS 
`Name`,`world`.`City`.`Country` AS `Country`,`world`.`City`.`Population` AS 
`Population` 

  
   FROM `world`.`City` JOIN `world`.`Country` WHERE 


((`world`.`City`.`Country` = `world`.`Country`.`Code`) and (`world`.`Country`.
`Population` < (100 * 1000)))
1 row in set (0.00 sec)
```

Changing the subquery into a join allows feeding the join to the join optimizer, which can make a choice between two possible join orders:

1. City -> Country
2. Country -> City

as opposed to the single choice of

1. City->Country

which we had before the optimization.

In the above example, the choice produces a better query plan. Without pullout, the query plan with a subquery would read `(4079 + 1*4079)=8158` table records. With table pullout, the join plan would read `(37 + 37 * 18) = 703` rows. Not all row reads are equal, but generally, reading `10` times fewer table records is faster.

## Table pullout fact sheet

* Table pullout is possible only in semi-join subqueries.
* Table pullout is based on `UNIQUE`/`PRIMARY` key definitions.
* Doing table pullout does not cut off any possible query plans, so MariaDB will always try to pull out as much as possible.
* Table pullout is able to pull individual tables out of subqueries to their parent selects. If all tables in a subquery have been pulled out, the subquery (i.e. its semi-join) is removed completely.
* One common bit of advice for optimizing MySQL has been "If possible, rewrite your subqueries as joins". Table pullout does exactly that, so manual rewrites are no longer necessary.

## Controlling table pullout

There is no separate @@optimizer\_switch flag for table pullout. Table pullout can be disabled by switching off all semi-join optimizations with`SET @@optimizer_switch='semijoin=off'` command.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
