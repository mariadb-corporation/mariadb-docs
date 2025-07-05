# Building the best INDEX for a given SELECT

## The problem

You have a SELECT and you want to build the best INDEX for it. This blog is a "cookbook" on how to do that task.

* A short algorithm that works for many simpler SELECTs and helps in complex queries.
* Examples of the algorithm, plus digressions into exceptions and variants
* Finally a long list of "other cases".

The hope is that a newbie can quickly get up to speed, and his/her INDEXes will no longer smack of "newbie".

Many edge cases are explained, so even an expert may find something useful here.

## Algorithm

Here's the way to approach creating an INDEX, given a SELECT. Follow the steps below, gathering columns to put in the INDEX in order. When the steps give out, you usually have the 'perfect' index.

1. Given a WHERE with a bunch of expressions connected by AND: Include the columns (if any), in any order, that are compared to a constant and not hidden in a function.
2. You get one more chance to add to the INDEX; do the first of these that applies:

* 2a. One column used in a 'range' -- BETWEEN, '>', LIKE w/o leading wildcard, etc.
* 2b. All columns, in order, of the GROUP BY.
* 2c. All columns, in order, of the ORDER BY if there is no mixing of ASC and DESC.

## Digression

This blog assumes you know the basic idea behind having an INDEX. Here is a refresher on some of the key points.

Virtually all INDEXes in MySQL are structured as BTrees\
BTrees allow very efficient for

* Given a key, find the corresponding row(s);
* "Range scans" -- That is start at one value for the key and repeatedly find the "next" (or "previous") row.

A PRIMARY KEY is a UNIQUE KEY; a UNIQUE KEY is an INDEX. ("KEY" == "INDEX".)

InnoDB "clusters" the PRIMARY KEY with the data. Hence, given the value of the PK ("PRIMARY KEY"), after drilling down the BTree to find the index entry, you have all the columns of the row when you get there. A "secondary key" (any UNIQUE or INDEX other than the PK) in InnoDB first drills down the BTree for the secondary index, where it finds a copy of the PK. Then it drills down the PK to find the row.

Every InnoDB table has a PRIMARY KEY. While there is a default if you do not specify one, it is best to explicitly provide a PK.

For completeness: MyISAM works differently. All indexes (including the PK) are in separate BTrees. The leaf node of such BTrees have a pointer (usually a byte offset) into the data file.

All discussion here assumes InnoDB tables, however most statements apply to other Engines.

## First, some examples

Think of a list of names, sorted by last\_name, then first\_name. You have undoubtedly seen such lists, and they often have other information such as address and phone number. Suppose you wanted to look me up. If you remember my full name ('James' and 'Rick'), it is easy to find my entry. If you remembered only my last name ('James') and first initial ('R'). You would quickly zoom in on the Jameses and find the Rs in them. There, you might remember 'Rick' and ignore 'Ronald'. But, suppose you remembered my first name ('Rick') and only my last initial ('J'). Now you are in trouble. You would be scanning all the Js -- Jones, Rick; Johnson, Rick; Jamison, Rick; etc, etc. That's much less efficient.

Those equate to

```sql
INDEX(last_name, first_name) -- the order of the list.
    WHERE last_name = 'James' AND first_name = 'Rick'  -- best case
    WHERE last_name = 'James' AND first_name LIKE 'R%' -- pretty good
    WHERE last_name LIKE 'J%' AND first_name = 'Rick'  -- pretty bad
```

Think about this example as I talk about "=" versus "range" in the Algorithm, below.

## Algorithm, step 1 (WHERE "column = const")

* `WHERE aaa = 123 AND ...` : an INDEX starting with aaa is good.
* `WHERE aaa = 123 AND bbb = 456 AND ...` : an INDEX starting with aaa and bbb is good. In this case, it does not matter whether aaa or bbb comes first in the INDEX.
* `xxx IS NULL` : this acts like "= const" for this discussion.
* `WHERE t1.aa = 123 AND t2.bb = 456` -- You must only consider columns in the current table.

Note that the expression must be of the form of `column_name` = (constant). These do not apply to this step in the Algorithm: DATE(dt) = '...', LOWER(s) = '...', CAST(s ...) = '...', x='...' COLLATE...

(If there are no "=" parts AND'd in the WHERE clause, move on to step 2 without any columns in your putative INDEX.)

## Algorithm, step 2

Find the first of 2a / 2b / 2c that applies; use it; then quit. If none apply, then you are through gathering columns for the index.

In some cases it is optimal to do step 1 (all equals) plus step 2c (ORDER BY).

## Algorithm, step 2a (one range)

A "range" shows up as

* `aaa >= 123` -- any of <, <=, >=, >; but not <>, !=
* `aaa BETWEEN 22 AND 44`
* `sss LIKE 'blah%'` -- but not `sss LIKE '%blah'`
* `xxx IS NOT NULL`\
  Add the column in the range to your putative INDEX.

If there are more parts to the WHERE clause, you must stop now.

Complete examples (assume nothing else comes after the snippet)

* `WHERE aaa >= 123 AND bbb = 1 ⇒ INDEX(bbb, aaa)` (WHERE order does not matter; INDEX order does)
* `WHERE aaa >= 123 ⇒ INDEX(aaa)`
* `WHERE aaa >= 123 AND ccc > 'xyz' ⇒ INDEX(aaa) or INDEX(ccc)` (only one range)
* `WHERE aaa >= 123 ORDER BY aaa ⇒ INDEX(aaa)` -- Bonus: The ORDER BY will use the INDEX.
* `WHERE aaa >= 123 ORDER BY aaa ⇒ INDEX(aaa) DESC` -- Same Bonus.

## Algorithm, step 2b (GROUP BY)

If there is a GROUP BY, all the columns of the GROUP BY should now be added, in the specified order, to the INDEX you are building. (I do not know what happens if one of the columns is already in the INDEX.)

If you are GROUPing BY an expression (including function calls), you cannot use the GROUP BY; stop.

Complete examples (assume nothing else comes after the snippet)

* `WHERE aaa = 123 AND bbb = 1 GROUP BY ccc ⇒ INDEX(bbb, aaa, ccc) or INDEX(aaa, bbb, ccc)` (='s first, in any order; then the GROUP BY)
* `WHERE aaa >= 123 GROUP BY xxx ⇒ INDEX(aaa)` (You should have stopped with Step 2a)
* `GROUP BY x,y ⇒ INDEX(x,y)` (no WHERE)
* `WHERE aaa = 123 GROUP BY xxx, (a+b) ⇒ INDEX(aaa)` -- expression in GROUP BY, so no use including even xxx.

## Algorithm, step 2c (ORDER BY)

If there is a ORDER BY, all the columns of the ORDER BY should now be added, in the specified order, to the INDEX you are building.

If there are multiple columns in the ORDER BY, and there is a mixture of ASC and DESC, do not add the ORDER BY columns; they won't help; stop.

If you are ORDERing BY an expression (including function calls), you cannot use the ORDER BY; stop.

Complete examples (assume nothing else comes after the snippet)

* `WHERE aaa = 123 GROUP BY ccc ORDER BY ddd ⇒ INDEX(aaa, ccc)` -- should have stopped with Step 2b
* `WHERE aaa = 123 GROUP BY ccc ORDER BY ccc ⇒ INDEX(aaa, ccc)` -- the ccc will be used for both GROUP BY and ORDER BY
* `WHERE aaa = 123 ORDER BY xxx ASC, yyy DESC ⇒ INDEX(aaa)` -- mixture of ASC and DESC.

The following are especially good. Normally a LIMIT cannot be applied until after lots of rows are gathered and then sorted according to the ORDER BY. But, if the INDEX gets all they way through the ORDER BY, only (OFFSET + LIMIT) rows need to be gathered. So, in these cases, you win the lottery with your new index:

* `WHERE aaa = 123 GROUP BY ccc ORDER BY ccc LIMIT 10 ⇒ INDEX(aaa, ccc)`
* `WHERE aaa = 123 ORDER BY ccc LIMIT 10 ⇒ INDEX(aaa, ccc)`
* `ORDER BY ccc LIMIT 10 ⇒ INDEX(ccc)`
* `WHERE ccc > 432 ORDER BY ccc LIMIT 10 ⇒ INDEX(ccc)` -- This "range" is compatible with ORDER BY

(It does not make much sense to have a LIMIT without an ORDER BY, so I do not discuss that case.)

## Algorithm end

You have collected a few columns; put them in INDEX and ADD that to the table. That will often produce a "good" index for the SELECT you have. Below are some other suggestions that may be relevant.

An example of the Algorithm being 'wrong':

```sql
SELECT ... FROM t WHERE flag = true;
```

This would (according to the Algorithm) call for INDEX(flag). However, indexing a column that has two (or a small number of) values is almost always useless. This is called 'low cardinality'. The Optimizer would prefer to do a table scan than to bounce between the index BTree and the data.

On the other hand, the Algorithm is 'right' with

```sql
SELECT ... FROM t WHERE flag = true AND date >= '2015-01-01';
```

That would call for a compound index starting with a flag: INDEX(flag, date). Such an index is likely to be very beneficial. And it is likely to be more beneficial than INDEX(date).

If your resulting INDEX include column(s) that are likely to be UPDATEd, note that the UPDATE will have extra work to remove a 'row' from one place in the INDEX's BTree and insert a 'row' back into the BTree. For example:

```sql
INDEX(x)
UPDATE t SET x = ... WHERE ...;
```

There are too many variables to say whether it is better to keep the index or to toss it.

In this case, shortening the index may be beneficial:

```sql
INDEX(z, x)
UPDATE t SET x = ... WHERE ...;
```

Changing to INDEX(z) would make for less work for the UPDATE, but might hurt some SELECT. It depends on the frequency of each, plus many more factors.

## Limitations

(There are exceptions to some of these.)

* You may not create an index bigger than 3KB.
* You may not include a column that equates to bigger than some value (767 bytes -- VARCHAR(255) CHARACTER SET utf8).
* You can deal with big fields using "prefix" indexing; but see below.
* You should not have more than 5 columns in an index. (This is just a Rule of Thumb; nothing prevents having more.)
* You should not have redundant indexes. (See below.)

## Flags and low cardinality

`INDEX(flag)` is almost never useful if `flag` has very few values. More specifically, when you say WHERE flag = 1 and "1" occurs more than 20% of the time, such an index will be shunned. The Optimizer would prefer to scan the table instead of bouncing back and forth between the index and the data for more than 20% of the rows.

("20%" is really somewhere between 10% and 30%, depending on the phase of the moon.)

## "Covering" indexes

A "Covering" index is an index that contains all the columns in the SELECT. It is special in that the SELECT can be completed by looking only at the INDEX BTree. (Since InnoDB's PRIMARY KEY is clustered with the data, "covering" is of no benefit when considering at the PRIMARY KEY.)

Mini-cookbook:

1. Gather the list of column(s) according to the "Algorithm", above.
2. Add to the end of the list the rest of the columns seen in the SELECT, in any order.

Examples:

* `SELECT x FROM t WHERE y = 5; ⇒ INDEX(y,x)` -- The algorithm said just INDEX(y)
* `SELECT x,z FROM t WHERE y = 5 AND q = 7; ⇒ INDEX(y,q,x,z)` -- y and q in either order (Algorithm), then x and z in either order (covering).
* `SELECT x FROM t WHERE y > 5 AND q > 7; ⇒ INDEX(y,q,x)` -- y or q first (that's as far as the Algorithm goes), then the other two fields afterwards.

The speedup you get might be minor, or it might be spectacular; it is hard to predict.

But...

* It is not wise to build an index with lots of columns. Let's cut it off at 5 (Rule of Thumb).
* Prefix indexes cannot 'cover', so don't use them anywhere in a 'covering' index.
* There are limits (3KB?) on how 'wide' an index can be, so "covering" may not be possible.

## Redundant/excessive indexes

INDEX(a,b) can find anything that INDEX(a) could find. So you don't need both. Get rid of the shorter one.

If you have lots of SELECTs and they generate lots of INDEXes, this may cause a different problem. Each index must be updated (sooner or later) for each INSERT. More indexes ⇒ slower INSERTs. Limit the number of indexes on a table to about 6 (Rule of Thumb).

Notice in the cookbook how it says "in any order" in a few places. If, for example, you have both of these (in different SELECTs):

* `WHERE a=1 AND b=2` begs for either INDEX(a,b) or INDEX(b,a)
* `WHERE a>1 AND b=2` begs only for INDEX(b,a)\
  Include only INDEX(b,a) since it handles both cases with only one INDEX.

Suppose you have a lot of indexes, including (a,b,c,dd) and (a,b,c,ee). Those are getting rather long. Consider either picking one of them, or having simply (a,b,c). Sometimes the selectivity of (a,b,c) is so good that tacking on 'dd' or 'ee' does make enough difference to matter.

## Optimizer picks ORDER BY

The main cookbook skips over an important optimization that is sometimes used. The optimizer will sometimes ignore the WHERE and, instead, use an INDEX that matches the ORDER BY. This, of course, needs to be a perfect match -- all columns, in the same order. And all ASC or all DESC.

This becomes especially beneficial if there is a LIMIT.

But there is a problem. There could be two situations, and the Optimizer is sometimes not smart enough to see which case applies:

* If the WHERE does very little filtering, fetching the rows in ORDER BY order avoids a sort and has little wasted effort (because of 'little filtering'). Using the INDEX matching the ORDER BY is better in this case.
* If the WHERE does a lot of filtering, the ORDER BY is wasting a lot of time fetching rows only to filter them out. Using an INDEX matching the WHERE clause is better.

What should you do? If you think the "little filtering" is likely, then create an index with the ORDER BY columns in order and hope that the Optimizer uses it when it should.

## OR

Cases...

* `WHERE a=1 OR a=2` -- This is turned into WHERE a IN (1,2) and optimized that way.
* `WHERE a=1 OR b=2` usually cannot be optimized.
* `WHERE x.a=1 OR y.b=2` This is even worse because of using two different tables.

A workaround is to use UNION. Each part of the UNION is optimized separately. For the second case:

```sql
( SELECT ... WHERE a=1 )   -- and have INDEX(a)
   UNION DISTINCT -- "DISTINCT" is assuming you need to get rid of dups
   ( SELECT ... WHERE b=2 )   -- and have INDEX(b)
   GROUP BY ... ORDER BY ...  -- whatever you had at the end of the original query
```

Now the query can take good advantage of two different indexes. Note: "Index merge" might kick in on the original query, but it is not necessarily any faster than the UNION. Sister blog on compound indexes, including 'Index Merge'

The third case (OR across 2 tables) is similar to the second.

If you originally had a LIMIT, UNION gets complicated. If you started with ORDER BY z LIMIT 190, 10, then the UNION needs to be

```sql
( SELECT ... LIMIT 200 )   -- Note: OFFSET 0, LIMIT 190+10
   UNION DISTINCT -- (or ALL)
   ( SELECT ... LIMIT 200 )
   LIMIT 190, 10              -- Same as originally
```

## TEXT / BLOB

You cannot directly index a TEXT or BLOB or large VARCHAR or large BINARY column. However, you can use a "prefix" index: INDEX(foo(20)). This says to index the first 20 characters of `foo`. But... It is rarely useful.

Example of a prefix index:

```sql
INDEX(last_name(2), first_name)
```

The index for me would contain 'Ja', 'Rick'. That's not useful for distinguishing between 'Jamison', 'Jackson', 'James', etc., so the index is so close to useless that the optimizer often ignores it.

Probably never do UNIQUE(foo(20)) because this applies a uniqueness constraint on the first 20 characters of the column, not the whole column!

[More on prefix indexing](https://dev.mysql.com/doc/refman/5.6/en/create-index.html)

## Dates

DATE, DATETIME, etc. are tricky to compare against.

Some tempting, but inefficient, techniques:

`date_col LIKE '2016-01%'` -- must convert date\_col to a string, so acts like a function`LEFT(date_col, 4) = '2016-01'` -- hiding the column in function`DATE(date_col) = 2016` -- hiding the column in function

All must do a full scan. (On the other hand, it can handy to use GROUP BY LEFT(date\_col, 7) for monthly grouping, but that is not an INDEX issue.)

This is efficient, and can use an index:

```sql
date_col >= '2016-01-01'
    AND date_col  < '2016-01-01' + INTERVAL 3 MONTH
```

This case works because both right-hand values are converted to constants, then it is a "range". I like the design pattern with INTERVAL because it avoids computing the last day of the month. And it avoids tacking on '23:59:59', which is wrong if you have microsecond times. (And other cases.)

## EXPLAIN Key\_len

Perform EXPLAIN SELECT... (and EXPLAIN FORMAT=JSON SELECT... if you have 5.6.5). Look at the Key that it chose, and the Key\_len. From those you can deduce how many columns of the index are being used for filtering. (JSON makes it easier to get the answer.) From that you can decide whether it is using as much of the INDEX as you thought. Caveat: Key\_len only covers the WHERE part of the action; the non-JSON output won't easily say whether GROUP BY or ORDER BY was handled by the index.

## IN

`IN (1,99,3)` is sometimes optimized as efficiently as "=", but not always. Older versions of MySQL did not optimize it as well as newer versions. (5.6 is possibly the main turning point.)

IN ( SELECT ... )

From version 4.1 through 5.5, IN ( SELECT ... ) was very poorly optimized. The SELECT was effectively re-evaluated every time. Often it can be transformed into a JOIN, which works much faster. Heres is a pattern to follow:

```sql
SELECT  ...
    FROM  a
    WHERE  test_a
      AND  x IN (
        SELECT  x
            FROM  b
            WHERE  test_b
                );
⇒
SELECT  ...
    FROM  a
    JOIN  b USING(x)
    WHERE  test_a
      AND  test_b;
```

The SELECT expressions will need "a." prefixing the column names.

Alas, there are cases where the pattern is hard to follow.

5.6 does some optimizing, but probably not as good as the JOIN.

If there is a JOIN or GROUP BY or ORDER BY LIMIT in the subquery, that complicates the JOIN in new format. So, it might be better to use this pattern:

```sql
SELECT  ...
    FROM  a
    WHERE  test_a
      AND  x IN ( SELECT  x  FROM ... );
⇒
SELECT  ...
    FROM  a
    JOIN        ( SELECT  x  FROM ... ) b
        USING(x)
    WHERE  test_a;
```

Caveat: If you end up with two subqueries JOINed together, note that neither has any indexes, hence performance can be very bad. (5.6 improves on it by dynamically creating indexes for subqueries.)

There is work going on in MariaDB and Oracle 5.7, in relation to "NOT IN", "NOT EXISTS", and "LEFT JOIN..IS NULL"; here is an old discussion on the topic\
So, what I say here may not be the final word.

## Explode/Implode

When you have a JOIN and a GROUP BY, you may have the situation where the JOIN exploded more rows than the original query (due to many:many), but you wanted only one row from the original table, so you added the GROUP BY to implode back to the desired set of rows.

This explode + implode, itself, is costly. It would be better to avoid them if possible.

Sometimes the following will work.

Using DISTINCT or GROUP BY to counteract the explosion

```sql
SELECT  DISTINCT
        a.*,
        b.y
    FROM a
    JOIN b
⇒
SELECT  a.*,
        ( SELECT GROUP_CONCAT(b.y) FROM b WHERE b.x = a.x ) AS ys
    FROM a
```

When using second table just to check for existence:

```sql
SELECT  a.*
    FROM a
    JOIN b  ON b.x = a.x
    GROUP BY a.id
⇒
SELECT  a.*,
    FROM a
    WHERE EXISTS ( SELECT *  FROM b  WHERE b.x = a.x )
```

[Another variant](https://dba.stackexchange.com/questions/115059/mysql-query-causing-high-cpu-and-taking-forever-to-execute/115120#115120)

## Many-to-many mapping table

Do it this way.

```sql
CREATE TABLE XtoY (
        # No surrogate id for this table
        x_id MEDIUMINT UNSIGNED NOT NULL,   -- For JOINing to one table
        y_id MEDIUMINT UNSIGNED NOT NULL,   -- For JOINing to the other table
        # Include other fields specific to the 'relation'
        PRIMARY KEY(x_id, y_id),            -- When starting with X
        INDEX      (y_id, x_id)             -- When starting with Y
    ) ENGINE=InnoDB;
```

Notes:

* Lack of an AUTO\_INCREMENT id for this table -- The PK given is the 'natural' PK; there is no good reason for a surrogate.
* "MEDIUMINT" -- This is a reminder that all INTs should be made as small as is safe (smaller ⇒ faster). Of course the declaration here must match the definition in the table being linked to.
* "UNSIGNED" -- Nearly all INTs may as well be declared non-negative
* "NOT NULL" -- Well, that's true, isn't it?
* "InnoDB" -- More effecient than MyISAM because of the way the PRIMARY KEY is clustered with the data in InnoDB.
* "INDEX(y\_id, x\_id)" -- The PRIMARY KEY makes it efficient to go one direction; this index makes the other direction efficient. No need to say UNIQUE; that would be extra effort on INSERTs.
* In the secondary index, saying justINDEX(y\_id) would work because it would implicit include x\_id. But I would rather make it more obvious that I am hoping for a 'covering' index.

To conditionally INSERT new links, use [IODKU](https://dev.mysql.com/doc/refman/5.6/en/insert-on-duplicate.html)

Note that if you had an AUTO\_INCREMENT in this table, IODKU would "burn" ids quite rapidly.

## Subqueries and UNIONs

Each subquery SELECT and each SELECT in a UNION can be considered separately for finding the optimal INDEX.

Exception: In a "correlated" ("dependent") subquery, the part of the WHERE that depends on the outside table is not easily factored into the INDEX generation. (Cop out!)

## JOINs

The first step is to decide what order the optimizer will go through the tables. If you cannot figure it out, then you may need to be pessimistic and create two indexes for each table -- one assuming the table will be used first, one assiming that it will come later in the table order.

The optimizer usually starts with one table and extracts the data needed from it. As it finds a useful (that is, matches the WHERE clause, if any) row, it reaches into the 'next' table. This is called NLJ ("Nested Loop Join"). The process of filtering and reaching to the next table continues through the rest of the tables.

The optimizer usually picks the "first" table based on these hints:

* STRAIGHT\_JOIN forces the table order.
* The WHERE clause limits which rows needed (whether indexed or not).
* The table to the "left" in a LEFT JOIN usually comes before the "right" table. (By looking at the table definitions, the optimizer may decide that "LEFT" is irrelevant.)
* The current INDEXes will encourage an order.
* etc.

Running EXPLAIN tells you the table order that the Optimizer is very likely to use today. After adding a new INDEX, the optimizer may pick a different table order. You should anticipate the order changing, guess at what order makes the most sense, and build the INDEXes accordingly. Then rerun EXPLAIN to see if the Optimizer's brain was on the same wavelength you were on.

You should build the INDEX for the "first" table based on any parts of the WHERE, GROUP BY, and ORDER BY clauses that are relevant to it. If a GROUP/ORDER BY mentions a different table, you should ignore that clause.

The second (and subsequent) table will be reached into based on the ON clause. (Instead of using commajoin, please write JOINs with the JOIN keyword and ON clause!) In addition, there could be parts of the WHERE clause that are relevant. GROUP/ORDER BY are not to be considered in writing the optimal INDEX for subsequent tables.

## PARTITIONing

PARTITIONing is rarely a substitute for a good INDEX.

PARTITION BY RANGE is a technique that is sometimes useful when indexing fails to be good enough. In a two-dimensional situation such as nearness in a geographical sense, one dimension can partially be handled by partition pruning; then the other dimension can be handled by a regular index (preferrably the PRIMARY KEY). This goes into more detail: [Find nearest 10 pizza parlors](../../../server-usage/partitioning-tables/partition-maintenance.md).

## FULLTEXT

FULLTEXT is now implemented in InnoDB as well as MyISAM. It provides a way to search for "words" in TEXT columns. This is much faster (when it is applicable) than col LIKE '%word%'.

```sql
WHERE x = 1
      AND MATCH (...) AGAINST (...)
```

always(?) uses the FULLTEXT index first. That is, the whole Algorithm is invalidated when one of the ANDs is a MATCH.

## Signs of a Newbie

* No "compound" (aka "composite") indexes
* No PRIMARY KEY
* Redundant indexes (especially blatant is PRIMARY KEY(id), KEY(id))
* Most or all columns individually indexes ("But I indexed everything")
* "Commajoin" -- That is `FROM a, b WHERE a.x=b.x` instead of `FROM a JOIN b ON a.x=b.x`

## Speeding up wp\_postmeta

The published table (see Wikipedia) is

```sql
CREATE TABLE wp_postmeta (
      meta_id BIGINT(20) UNSIGNED NOT NULL AUTO_INCREMENT,
      post_id BIGINT(20) UNSIGNED NOT NULL DEFAULT '0',
      meta_key VARCHAR(255) DEFAULT NULL,
      meta_value LONGTEXT,
      PRIMARY KEY (meta_id),
      KEY post_id (post_id),
      KEY meta_key (meta_key)
    ) ENGINE=InnoDB  DEFAULT CHARSET=utf8;
```

The problems:

* The AUTO\_INCREMENT provides no benefit; in fact it slows down most queries and clutters disk.
* Much better is PRIMARY KEY(post\_id, meta\_key) -- clustered, handles both parts of usual JOIN.
* BIGINT is overkill, but that can't be fixed without changing other tables.
* VARCHAR(255) can be a problem in 5.6 with utf8mb4; see workarounds below.
* When would `meta_key` or `meta_value` ever be NULL?

The solutions:

```sql
CREATE TABLE wp_postmeta (
        post_id BIGINT UNSIGNED NOT NULL,
        meta_key VARCHAR(255) NOT NULL,
        meta_value LONGTEXT NOT NULL,
        PRIMARY KEY(post_id, meta_key),
        INDEX(meta_key)
        ) ENGINE=InnoDB;
```

## Postlog

Initial posting: March, 2015; Refreshed Feb, 2016; Add DATE June, 2016; Add WP example May, 2017.

The tips in this document apply to MySQL, MariaDB, and Percona.

## See also

* [Percona 2015 Tutorial Slides](https://mysql.rjweb.org/slides/IndexCookbook.pdf)
* Some info in the MySQL manual: [ORDER BY Optimization](https://dev.mysql.com/doc/refman/5.6/en/order-by-optimization.html)
* A short, but complicated, [example](https://stackoverflow.com/questions/28974572/mysql-index-for-order-by-with-date-range-in-where)
* [MySQL manual page on range accesses in composite indexes](https://dev.mysql.com/doc/refman/5.7/en/range-optimization.html#range-access-multi-part)
* [Some discussion of JOIN](https://dba.stackexchange.com/questions/120551/very-slow-query-not-sure-if-mysql-index-is-being-used)
* [Indexing 101: Optimizing MySQL queries on a single table](https://www.percona.com/blog/2015/04/27/indexing-101-optimizing-mysql-queries-on-a-single-table/)\
  (Stephane Combaudon - Percona)
* [A complex query, well explained.](https://stackoverflow.com/a/37024870/1766831)

This blog is the consolidation of a Percona tutorial I gave in 2013, plus many years of experience in fixing thousands of slow queries on hundreds of systems.\
I apologize that this does not tell you how create INDEXes for all SELECTs. Some are just too complex.

Rick James graciously allowed us to use this article in the documentation.

[Rick James' site](https://mysql.rjweb.org/) has other useful tips, how-tos,\
optimizations, and debugging tips.

Original source: [random](https://mysql.rjweb.org/doc.php/random)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
