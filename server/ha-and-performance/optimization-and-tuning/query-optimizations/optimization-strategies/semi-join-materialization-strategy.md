# Semi-join Materialization Strategy

Semi-join Materialization is a special kind of subquery materialization used for [Semi-join subqueries](../subquery-optimizations/semi-join-subquery-optimizations.md). It actually includes two strategies:

* Materialization/lookup
* Materialization/scan

## The idea

Consider a query that finds countries in Europe which have big cities:

```sql
SELECT * FROM Country 
WHERE Country.code IN (SELECT City.Country 
                       FROM City 
                       WHERE City.Population > 7*1000*1000)
      AND Country.continent='Europe'
```

The subquery is uncorrelated, that is, we can run it independently of the upper query. The idea of semi-join materialization is to do just that, and fill a temporary table with possible values of the City.country field of big cities, and then do a join with countries in Europe:

```mermaid
flowchart LR
    accTitle: Building and joining the semi-join materialized table
    accDescr { The City table has six rows pairing a city with a country code: Berlin-DEU, Paris-FRA, Munich-DEU, Koln-DEU, Beijing-CHN, and Shanghai-CHN. All six rows feed into a materialized temporary table that keeps only the distinct country codes: DEU, FRA, and CHN. This materialized table is joined with the Country table, filtered to countries in Europe, to produce the result. }
    City["city<br/>Berlin | DEU<br/>Paris | FRA<br/>Munich | DEU<br/>Koln | DEU<br/>Beijing | CHN<br/>Shanghai | CHN"]:::file
    Mat["materialized temporary table<br/>DEU<br/>FRA<br/>CHN"]:::proc
    Country["country"]:::file
    Join(("JOIN")):::node
    Result["Result"]:::node

    City --> Mat
    Mat --> Join
    Country -->|"countries in Europe"| Join
    Join --> Result

    classDef node fill:#e2f0f2,stroke:#0a5a6b,stroke-width:2px,color:#111;
    classDef proc fill:#fbe5d6,stroke:#c15911,stroke-width:2px,color:#111;
    classDef file fill:#eaf2fb,stroke:#2f5b8f,stroke-width:2px,color:#111;
```

_City rows feed a materialized temporary table of distinct country codes, which is joined with countries in Europe to produce the result._

The join can be done in two directions:

1. From the materialized table to countries in Europe
2. From countries in Europe to the materialized table

The first way involves doing a full scan on the materialized table, so we call it "Materialization-scan".

If you run a join from Countries to the materialized table, the cheapest way to find a match in the materialized table is to make a lookup on its primary key (it has one: we used it to remove duplicates). Because of that, we call the strategy "Materialization-lookup".

## Semi-join materialization in action

### Materialization-Scan

If we chose to look for cities with a population greater than 7 million, the optimizer will use Materialization-Scan and `EXPLAIN` will show this:

```sql
MariaDB [world]> EXPLAIN SELECT * FROM Country WHERE Country.code IN 
  (select City.Country from City where  City.Population > 7*1000*1000);
+----+--------------+-------------+--------+--------------------+------------+---------+--------------------+------+-----------------------+
| id | select_type  | table       | type   | possible_keys      | key        | key_len | ref                | rows | Extra                 |
+----+--------------+-------------+--------+--------------------+------------+---------+--------------------+------+-----------------------+
|  1 | PRIMARY      | <subquery2> | ALL    | distinct_key       | NULL       | NULL    | NULL               |   15 |                       |
|  1 | PRIMARY      | Country     | eq_ref | PRIMARY            | PRIMARY    | 3       | world.City.Country |    1 |                       |
|  2 | MATERIALIZED | City        | range  | Population,Country | Population | 4       | NULL               |   15 | Using index condition |
+----+--------------+-------------+--------+--------------------+------------+---------+--------------------+------+-----------------------+
3 rows in set (0.01 sec)
```

Here, you can see:

* There are still two `SELECT`s (look for columns with `id=1` and `id=2`)
* The second select (with `id=2`) has `select_type=MATERIALIZED`. This means it will be executed and its results will be stored in a temporary table with a unique key over all columns. The unique key is there to prevent the table from containing any duplicate records.
* The first select received the table name `subquery2`. This is the table that we got as a result of the materialization of the select with `id=2`.

The optimizer chose to do a full scan over the materialized table, so this is an example of a use of the Materialization-Scan strategy.

As for execution costs, we're going to read 15 rows from table City, write 15 rows to materialized table, read them back (the optimizer assumes there won't be any duplicates), and then do 15 eq\_ref accesses to table Country. In total, we'll do 45 reads and 15 writes.

By comparison, if you run the `EXPLAIN` with semi-join optimizations disabled, you'll get this:

```sql
MariaDB [world]> EXPLAIN SELECT * FROM Country WHERE Country.code IN 
  (select City.Country from City where  City.Population > 7*1000*1000);
+----+--------------------+---------+-------+--------------------+------------+---------+------+------+------------------------------------+
| id | select_type        | table   | type  | possible_keys      | key        | key_len | ref  | rows | Extra                              |
+----+--------------------+---------+-------+--------------------+------------+---------+------+------+------------------------------------+
|  1 | PRIMARY            | Country | ALL   | NULL               | NULL       | NULL    | NULL |  239 | Using where                        |
|  2 | DEPENDENT SUBQUERY | City    | range | Population,Country | Population | 4       | NULL |   15 | Using index condition; Using where |
+----+--------------------+---------+-------+--------------------+------------+---------+------+------+------------------------------------+
```

...which is a plan to do `(239 + 239*15) = 3824` table reads.

### Materialization-Lookup

Let's modify the query slightly and look for countries which have cities with a population over one million (instead of seven):

```sql
MariaDB [world]> EXPLAIN SELECT * FROM Country WHERE Country.code IN 
  (select City.Country from City where  City.Population > 1*1000*1000) ;
+----+--------------+-------------+--------+--------------------+--------------+---------+------+------+-----------------------+
| id | select_type  | table       | type   | possible_keys      | key          | key_len | ref  | rows | Extra                 |
+----+--------------+-------------+--------+--------------------+--------------+---------+------+------+-----------------------+
|  1 | PRIMARY      | Country     | ALL    | PRIMARY            | NULL         | NULL    | NULL |  239 |                       |
|  1 | PRIMARY      | <subquery2> | eq_ref | distinct_key       | distinct_key | 3       | func |    1 |                       |
|  2 | MATERIALIZED | City        | range  | Population,Country | Population   | 4       | NULL |  238 | Using index condition |
+----+--------------+-------------+--------+--------------------+--------------+---------+------+------+-----------------------+
3 rows in set (0.00 sec)
```

The `EXPLAIN` output is similar to the one which used Materialization-scan, except that:

* the `<subquery2>` table is accessed with the `eq_ref` access method
* the access uses an index named `distinct_key`

This means that the optimizer is planning to do index lookups into the materialized table. In other words, we're going to use the Materialization-lookup strategy.

With `optimizer_switch='semijoin=off,materialization=off'`), one will get this `EXPLAIN`:

```sql
MariaDB [world]> EXPLAIN SELECT * FROM Country WHERE Country.code IN 
  (select City.Country from City where  City.Population > 1*1000*1000) ;
+----+--------------------+---------+----------------+--------------------+---------+---------+------+------+-------------+
| id | select_type        | table   | type           | possible_keys      | key     | key_len | ref  | rows | Extra       |
+----+--------------------+---------+----------------+--------------------+---------+---------+------+------+-------------+
|  1 | PRIMARY            | Country | ALL            | NULL               | NULL    | NULL    | NULL |  239 | Using where |
|  2 | DEPENDENT SUBQUERY | City    | index_subquery | Population,Country | Country | 3       | func |   18 | Using where |
+----+--------------------+---------+----------------+--------------------+---------+---------+------+------+-------------+
```

One can see that both plans will do a full scan on the `Country` table. For the second step, MariaDB will fill the materialized table (238 rows read from table City and written to the temporary table) and then do a unique key lookup for each record in table `Country`, which works out to 238 unique key lookups. In total, the second step will cost `(239+238) = 477` reads and `238` temp.table writes.

Execution of the latter (`DEPENDENT SUBQUERY`) plan reads 18 rows using an index on `City.Country` for each record it receives for table `Country`. This works out to a cost of `(18*239) = 4302` reads. Had there been fewer subquery invocations, this plan would have been better than the one with Materialization. By the way, MariaDB has an option to use such a query plan, too (see [FirstMatch Strategy](firstmatch-strategy.md)), but it did not choose it.

## Subqueries with grouping

MariaDB is able to use Semi-join materialization strategy when the subquery has grouping (other semi-join strategies are not applicable in this case).

This allows for efficient execution of queries that search for the best/last element in a certain group.

For example, let's find cities that have the biggest population on their continent:

```sql
EXPLAIN 
SELECT * FROM City 
WHERE City.Population IN (SELECT max(City.Population) FROM City, Country 
                          WHERE City.Country=Country.Code 
                          GROUP BY Continent)
+------+--------------+-------------+------+---------------+------------+---------+----------------------------------+------+-----------------+
| id   | select_type  | table       | type | possible_keys | key        | key_len | ref                              | rows | Extra           |
+------+--------------+-------------+------+---------------+------------+---------+----------------------------------+------+-----------------+
|    1 | PRIMARY      | <subquery2> | ALL  | distinct_key  | NULL       | NULL    | NULL                             |  239 |                 |
|    1 | PRIMARY      | City        | ref  | Population    | Population | 4       | <subquery2>.max(City.Population) |    1 |                 |
|    2 | MATERIALIZED | Country     | ALL  | PRIMARY       | NULL       | NULL    | NULL                             |  239 | Using temporary |
|    2 | MATERIALIZED | City        | ref  | Country       | Country    | 3       | world.Country.Code               |   18 |                 |
+------+--------------+-------------+------+---------------+------------+---------+----------------------------------+------+-----------------+
4 rows in set (0.00 sec)
```

the cities are:

```
+------+-------------------+---------+------------+
| ID   | Name              | Country | Population |
+------+-------------------+---------+------------+
| 1024 | Mumbai (Bombay)   | IND     |   10500000 |
| 3580 | Moscow            | RUS     |    8389200 |
| 2454 | Macao             | MAC     |     437500 |
|  608 | Cairo             | EGY     |    6789479 |
| 2515 | Ciudad de México | MEX     |    8591309 |
|  206 | São Paulo        | BRA     |    9968485 |
|  130 | Sydney            | AUS     |    3276207 |
+------+-------------------+---------+------------+
```

## Factsheet

Semi-join materialization

* Can be used for uncorrelated IN-subqueries. The subselect may use grouping and/or aggregate functions.
* Is shown in `EXPLAIN` as `type=MATERIALIZED` for the subquery, and a line with`table=<subqueryN>` in the parent subquery.
* Is enabled when one has both `materialization=on` and `semijoin=on` in the [optimizer\_switch](../../system-variables/server-system-variables.md#optimizer_switch) variable.
* The `materialization=on|off` flag is shared with [Non-semijoin materialization](../subquery-optimizations/non-semi-join-subquery-optimizations.md#materialization-for-non-correlated-in-subqueries).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
