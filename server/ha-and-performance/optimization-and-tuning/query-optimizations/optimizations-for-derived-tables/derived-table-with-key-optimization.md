# Derived Table with Key Optimization

## The idea

If a derived table cannot be merged into its parent SELECT, it will be materialized in a temporary table, and then parent select will treat it as a regular base table.

Before [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3)/MySQL 5.6, the temporary table would never have any indexes, and the only way to read records from it would be a full table scan. Starting from the mentioned versions of the server, the optimizer has an option to create an index and use it for joins with other tables.

## Example

Consider a query: we want to find countries in Europe, that have more than one million people living in cities. This is accomplished with this query:

```sql
SELECT * 
FROM
   Country, 
   (SELECT 
       SUM(City.Population) AS urban_population, 
       City.Country 
    FROM City 
    GROUP BY City.Country 
    HAVING 
    urban_population > 1*1000*1000
   ) AS cities_in_country
WHERE 
  Country.Code=cities_in_country.Country AND Country.Continent='Europe';
```

The EXPLAIN output for it will show:

```
+----+-------------+------------+------+-------------------+-----------+---------+--------------------+------+---------------------------------+
| id | select_type | table      | type | possible_keys     | key       | key_len | ref                | rows | Extra                           |
+----+-------------+------------+------+-------------------+-----------+---------+--------------------+------+---------------------------------+
|  1 | PRIMARY     | Country    | ref  | PRIMARY,continent | continent | 17      | const              |   60 | Using index condition           |
|  1 | PRIMARY     | <derived2> | ref  | key0              | key0      | 3       | world.Country.Code |   17 |                                 |
|  2 | DERIVED     | City       | ALL  | NULL              | NULL      | NULL    | NULL               | 4079 | Using temporary; Using filesort |
+----+-------------+------------+------+-------------------+-----------+---------+--------------------+------+---------------------------------+
```

One can see here that

* table `<derived2>` is accessed through `key0`.
* `ref` column shows `world.Country.Code`
* if we look that up in the original query, we find the equality that was used to construct `ref` access: `Country.Code=cities_in_country.Country`.

## Factsheet

* The idea of "derived table with key" optimization is to let the materialized derived table have one key which is used for joins with other tables.
* The optimization is applied then the derived table could not be merged into its parent SELECT
  * which happens when the derived table doesn't meet criteria for mergeable VIEW
* The optimization is ON by default; it can be switched off like so:

```sql
SET optimizer_switch='derived_with_keys=off'
```

## See Also

* [Optimizing Subqueries in the FROM Clause](https://dev.mysql.com/doc/refman/5.6/en/from-clause-subquery-optimization.html) in MySQL 5.6 manual
* [What is MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3)
* [Subquery Optimizations Map](../subquery-optimizations/subquery-optimizations-map.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
