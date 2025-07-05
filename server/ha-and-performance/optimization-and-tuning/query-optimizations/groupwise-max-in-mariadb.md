# Groupwise Max in MariaDB

## The problem

You want to find the largest row in each group of rows. An example is looking for the largest city in each state. While it is easy to find the MAX(population) ... GROUP BY state, it is hard to find the name of the `city` associated with that `population`. Alas, MySQL and MariaDB do not have any syntax to provide the solution directly.

This article is under construction, mostly for cleanup. The content is reasonably accurate during construction.

The article presents two "good" solutions. They differ in ways that make neither of them 'perfect'; you should try both and weigh the pros and cons.

Also, a few "bad" solutions will be presented, together with why they were rejected.

MySQL manual\
gives 3 solutions; only the "Uncorrelated" one is "good", the other two are "bad".

## Sample data

To show how the various coding attempts work, I have devised this simple task: Find the largest city in each Canadian province. Here's a sample of the source data (5493 rows):

```
+------------------+----------------+------------+
| province         | city           | population |
+------------------+----------------+------------+
| Saskatchewan     | Rosetown       |       2309 |
| British Columbia | Chilliwack     |      51942 |
| Nova Scotia      | Yarmouth       |       7500 |
| Alberta          | Grande Prairie |      41463 |
| Quebec           | Sorel          |      33591 |
| Ontario          | Moose Factory  |       2060 |
| Ontario          | Bracebridge    |       8238 |
| British Columbia | Nanaimo        |      84906 |
| Manitoba         | Neepawa        |       3151 |
| Alberta          | Grimshaw       |       2560 |
| Saskatchewan     | Carnduff       |        950 |
...
```

Here's the desired output (13 rows):

```
+---------------------------+---------------+------------+
| province                  | city          | population |
+---------------------------+---------------+------------+
| Alberta                   | Calgary       |     968475 |
| British Columbia          | Vancouver     |    1837970 |
| Manitoba                  | Winnipeg      |     632069 |
| New Brunswick             | Saint John    |      87857 |
| Newfoundland and Labrador | Corner Brook  |      18693 |
| Northwest Territories     | Yellowknife   |      15866 |
| Nova Scotia               | Halifax       |     266012 |
| Nunavut                   | Iqaluit       |       6124 |
| Ontario                   | Toronto       |    4612187 |
| Prince Edward Island      | Charlottetown |      42403 |
| Quebec                    | Montreal      |    3268513 |
| Saskatchewan              | Saskatoon     |     198957 |
| Yukon                     | Whitehorse    |      19616 |
+---------------------------+---------------+------------+
```

## Duplicate max

One thing to consider is whether you want -- or do not want -- to see multiple rows for tied winners. For the dataset being used here, that would imply that the two largest cities in a province had identical populations. For this case, a duplicate would be unlikely. But there are many groupwise-max use cases where duplictes are likely.

The two best algorithms differ in whether they show duplicates.

## Using an uncorrelated subquery

Characteristics:

* Superior performance or medium performance
* It will show duplicates
* Needs an extra index
* Probably requires 5.6
* If all goes well, it will run in O(M) where M is the number of output rows.

An 'uncorrelated subquery':

```sql
SELECT  c1.province, c1.city, c1.population
    FROM  Canada AS c1
    JOIN
      ( SELECT  province, MAX(population) AS population
            FROM  Canada
            GROUP BY  province
      ) AS c2 USING (province, population)
    ORDER BY c1.province;
```

But this also 'requires' an extra index: INDEX(province, population). In addition, MySQL has not always been able to use that index effectively, hence the "requires 5.6". (I am not sure of the actual version.)

Without that extra index, you would need 5.6, which has the ability to create indexes for subqueries. This is indicated by \<auto\_key0> in the EXPLAIN. Even so, the performance is worse with the auto-generated index than with the manually generated one.

With neither the extra index, nor 5.6, this 'solution' would belong in 'The Duds' because it would run in O(N\*N) time.

## Using @variables

Characteristics:

* Good performance
* Does not show duplicates (picks one to show)
* Consistent O(N) run time (N = number of input rows)
* Only one scan of the data

```sql
SELECT
        province, city, population   -- The desired columns
    FROM
      ( SELECT  @prev := '' ) init
    JOIN
      ( SELECT  province != @prev AS first,  -- `province` is the 'GROUP BY'
                @prev := province,           -- The 'GROUP BY'
                province, city, population   -- Also the desired columns
            FROM  Canada           -- The table
            ORDER BY
                province,          -- The 'GROUP BY'
                population DESC    -- ASC for MIN(population), DESC for MAX
      ) x
    WHERE  first
    ORDER BY  province;     -- Whatever you like
```

For your application, change the lines with comments.

## The duds

\*\*\* 'correlated subquery' (from MySQL doc):\*\*

```sql
SELECT  province, city, population
    FROM  Canada AS c1
    WHERE  population =
      ( SELECT  MAX(c2.population)
            FROM  Canada AS c2
            WHERE  c2.province= c1.province
      )
    ORDER BY  province;
```

O(N\*N) (that is, terrible) performance

\*\*\* LEFT JOIN (from MySQL doc):\*\*

```sql
SELECT  c1.province, c1.city, c1.population
    FROM  Canada AS c1
    LEFT JOIN  Canada AS c2 ON c2.province = c1.province
      AND  c2.population > c1.population
    WHERE  c2.province IS NULL
    ORDER BY province;
```

Medium performance (2N-3N, depending on join\_buffer\_size).

For O(N\*N) time,... It will take one second to do a groupwise-max on a few thousand rows; a million rows could take hours.

## Top-N in each group

This is a variant on "groupwise-max" wherein you desire the largest (or smallest) N items in each group. Do these substitutions for your use case:

* province --> your 'GROUP BY'
* Canada --> your table
* 3 --> how many of each group to show
* population --> your numeric field for determining "Top-N"
* city --> more field(s) you want to show
* Change the SELECT and ORDER BY if you desire
* DESC to get the 'largest'; ASC for the 'smallest'

```sql
SELECT
        province, n, city, population
    FROM
      ( SELECT  @prev := '', @n := 0 ) init
    JOIN
      ( SELECT  @n := if(province != @prev, 1, @n + 1) AS n,
                @prev := province,
                province, city, population
            FROM  Canada
            ORDER BY
                province   ASC,
                population DESC
      ) x
    WHERE  n <= 3
    ORDER BY  province, n;
```

Output:

```sql
+---------------------------+------+------------------+------------+
| province                  | n    | city             | population |
+---------------------------+------+------------------+------------+
| Alberta                   |    1 | Calgary          |     968475 |
| Alberta                   |    2 | Edmonton         |     822319 |
| Alberta                   |    3 | Red Deer         |      73595 |
| British Columbia          |    1 | Vancouver        |    1837970 |
| British Columbia          |    2 | Victoria         |     289625 |
| British Columbia          |    3 | Abbotsford       |     151685 |
| Manitoba                  |    1 | ...
```

The performance of this is O(N), actually about 3N, where N is the number of source rows.

EXPLAIN EXTENDED gives

```sql
+----+-------------+------------+--------+---------------+------+---------+------+------+----------+----------------+
| id | select_type | table      | type   | possible_keys | key  | key_len | ref  | rows | filtered | Extra          |
+----+-------------+------------+--------+---------------+------+---------+------+------+----------+----------------+
|  1 | PRIMARY     | <derived2> | system | NULL          | NULL | NULL    | NULL |    1 |   100.00 | Using filesort |
|  1 | PRIMARY     | <derived3> | ALL    | NULL          | NULL | NULL    | NULL | 5484 |   100.00 | Using where    |
|  3 | DERIVED     | Canada     | ALL    | NULL          | NULL | NULL    | NULL | 5484 |   100.00 | Using filesort |
|  2 | DERIVED     | NULL       | NULL   | NULL          | NULL | NULL    | NULL | NULL |     NULL | No tables used |
+----+-------------+------------+--------+---------------+------+---------+------+------+----------+----------------+
```

Explanation, shown in the same order as the EXPLAIN, but numbered chronologically:\
3\. Get the subquery id=2 (init)\
4\. Scan the output from subquery id=3 (x)\
2\. Subquery id=3 -- the table scan of Canada

1. Subquery id=2 -- `init` for simply initializing the two @variables\
   Yes, it took two sorts, though probably in RAM.

Main Handler values:

```
| Handler_read_rnd           | 39    |
| Handler_read_rnd_next      | 10971 |
| Handler_write              | 5485  |  -- #rows in Canada (+1)
```

## Top-n in each group, take II

This variant is faster than the previous, but depends on `city` being unique across the dataset. (from openark.org)

```sql
SELECT  province, city, population
        FROM  Canada
        JOIN
          ( SELECT  GROUP_CONCAT(top_in_province) AS top_cities
                FROM
                  ( SELECT  SUBSTRING_INDEX(
                                   GROUP_CONCAT(city ORDER BY  population DESC),
                            ',', 3) AS top_in_province
                        FROM  Canada
                        GROUP BY  province
                  ) AS x
          ) AS y
        WHERE  FIND_IN_SET(city, top_cities)
        ORDER BY  province, population DESC;
```

Output. Note how there can be more than 3 cities per province:

```
| Alberta                   | Calgary          |     968475 |
| Alberta                   | Edmonton         |     822319 |
| Alberta                   | Red Deer         |      73595 |
| British Columbia          | Vancouver        |    1837970 |
| British Columbia          | Victoria         |     289625 |
| British Columbia          | Abbotsford       |     151685 |
| British Columbia          | Sydney           |          0 | -- Nova Scotia's second largest is Sydney
| Manitoba                  | Winnipeg         |     632069 |
```

Main Handler values:

```
| Handler_read_next          | 5484  | -- table size
| Handler_read_rnd_next      | 5500  | -- table size + number of provinces
| Handler_write              | 14    | -- number of provinces (+1)
```

## Top-n using MyISAM

(This does not need your table to be MyISAM, but it does need MyISAM tmp table for its 2-column PRIMARY KEY feature.) See previous section for what changes to make for your use case.

```sql
-- build tmp table to get numbering
    -- (Assumes auto_increment_increment = 1)
    CREATE TEMPORARY TABLE t (
        nth MEDIUMINT UNSIGNED NOT NULL AUTO_INCREMENT,
        PRIMARY KEY(province, nth)
    ) ENGINE=MyISAM
        SELECT province, NULL AS nth, city, population
            FROM Canada
            ORDER BY population DESC;
    -- Output the biggest 3 cities in each province:
    SELECT province, nth, city, population
        FROM t
        WHERE nth <= 3
        ORDER BY province, nth;

+---------------------------+-----+------------------+------------+
| province                  | nth | city             | population |
+---------------------------+-----+------------------+------------+
| Alberta                   |   1 | Calgary          |     968475 |
| Alberta                   |   2 | Edmonton         |     822319 |
| Alberta                   |   3 | Red Deer         |      73595 |
| British Columbia          |   1 | Vancouver        |    1837970 |
| British Columbia          |   2 | Victoria         |     289625 |
| British Columbia          |   3 | Abbotsford       |     151685 |
| Manitoba                  |  ...

SELECT FOR CREATE:
+----+-------------+--------+------+---------------+------+---------+------+------+----------------+
| id | select_type | table  | type | possible_keys | key  | key_len | ref  | rows | Extra          |
+----+-------------+--------+------+---------------+------+---------+------+------+----------------+
|  1 | SIMPLE      | Canada | ALL  | NULL          | NULL | NULL    | NULL | 5484 | Using filesort |
+----+-------------+--------+------+---------------+------+---------+------+------+----------------+
Other SELECT:
+----+-------------+-------+-------+---------------+---------+---------+------+------+-------------+
| id | select_type | table | type  | possible_keys | key     | key_len | ref  | rows | Extra       |
+----+-------------+-------+-------+---------------+---------+---------+------+------+-------------+
|  1 | SIMPLE      | t     | index | NULL          | PRIMARY | 104     | NULL |   22 | Using where |
+----+-------------+-------+-------+---------------+---------+---------+------+------+-------------+
```

The main handler values (total of all operations):

```
| Handler_read_rnd_next      | 10970 |
| Handler_write              | 5484  |  -- number of rows in Canada (write tmp table)
```

Both "Top-n" formulations probably take about the same amount of time.

## Windowing functions

Hot off the press from Percona Live... [MariaDB 10.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/what-is-mariadb-102) has "windowing functions", which make "groupwise max" much more straightforward.

The code:

TBD

## Postlog

Developed an first posted, Feb, 2015; Add MyISAM approach: July, 2015; Openark's method added: Apr, 2016; Windowing: Apr 2016

I did not include the technique(s) using GROUP\_CONCAT. They are useful in some situations with small datasets. They can be found in the references below.

## See also

* This has some of these algorithms, plus some others: [Peter Brawley's blog](https://www.artfulsoftware.com/infotree/queries.php?\&bw=1179#101)
* [Jan Kneschke's blog from 2007](https://jan.kneschke.de/projects/mysql/groupwise-max)
* [StackOverflow discussion of 'Uncorrelated'](https://stackoverflow.com/questions/14770671/mysql-order-by-before-group-by)
* Other references: [Inner ORDER BY thrown away](https://mariadb.com/kb/en/mariadb/group-by-trick-has-been-optimized-away/)
* Adding a large LIMIT to a subquery may make things work. [Why ORDER BY in subquery is ignored](https://github.com/mariadb-corporation/docs-server/blob/test/server/ha-and-performance/optimization-and-tuning/query-optimizations/broken-reference/README.md)
* [StackOverflow thread](https://stackoverflow.com/questions/36485072/select-with-order-and-group-by-in-maria-dbmysql)
* [row\_number(), rank(), dense\_rank()](https://kennethxu.blogspot.com/2016/04/analytical-function-in-mysql-rownumber.html)
* \[http://rpbouman.blogspot.de/2008/07/calculating-nth-percentile-in-mysql.html][Perentile blog](https://rpbouman.blogspot.de/2008/07/calculating-nth-percentile-in-mysql.html]\[Perentile_blog)

Rick James graciously allowed us to use this article in the documentation.

[Rick James' site](https://mysql.rjweb.org/) has other useful tips, how-tos,\
optimizations, and debugging tips.

Original source: [groupwise\_max](https://mysql.rjweb.org/doc.php/groupwise_max)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
