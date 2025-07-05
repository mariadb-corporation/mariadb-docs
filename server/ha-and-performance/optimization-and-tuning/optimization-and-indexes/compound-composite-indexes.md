# Compound (Composite) Indexes

## A mini-lesson in "compound indexes" ("composite indexes")

This document starts out trivial and perhaps boring, but builds up to more interesting information, perhaps things you did not realize about how MariaDB and MySQL indexing works.

This also explains [EXPLAIN](../../../reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain.md) (to some extent).

(Most of this applies to other databases, too.)

## The query to discuss

The question is "When was Andrew Johnson president of the US?".

The available table `Presidents` looks like:

```sql
+-----+------------+----------------+-----------+
| seq | last_name  | first_name     | term      |
+-----+------------+----------------+-----------+
|   1 | Washington | George         | 1789-1797 |
|   2 | Adams      | John           | 1797-1801 |
...
|   7 | Jackson    | Andrew         | 1829-1837 |
...
|  17 | Johnson    | Andrew         | 1865-1869 |
...
|  36 | Johnson    | Lyndon B.      | 1963-1969 |
...
```

("Andrew Johnson" was picked for this lesson because of the duplicates.)

What index(es) would be best for that question? More specifically, what would be best for

```sql
SELECT  term
        FROM  Presidents
        WHERE  last_name = 'Johnson'
          AND  first_name = 'Andrew';
```

Some INDEXes to try...

* No indexes
* INDEX(first\_name), INDEX(last\_name) (two separate indexes)
* "Index Merge Intersect"
* INDEX(last\_name, first\_name) (a "compound" index)
* INDEX(last\_name, first\_name, term) (a "covering" index)
* Variants

## No indexes

Well, I am fudging a little here. I have a PRIMARY KEY on `seq`, but that has no advantage on the query we are studying.

```sql
SHOW CREATE TABLE Presidents \G
CREATE TABLE `presidents` (
  `seq` TINYINT(3) UNSIGNED NOT NULL AUTO_INCREMENT,
  `last_name` VARCHAR(30) NOT NULL,
  `first_name` VARCHAR(30) NOT NULL,
  `term` VARCHAR(9) NOT NULL,
  PRIMARY KEY (`seq`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8

EXPLAIN  SELECT  term
   FROM  Presidents
   WHERE  last_name = 'Johnson'
   AND  first_name = 'Andrew';
+----+-------------+------------+------+---------------+------+---------+------+------+-------------+
| id | select_type | table      | type | possible_keys | key  | key_len | ref  | rows | Extra       |
+----+-------------+------------+------+---------------+------+---------+------+------+-------------+
|  1 | SIMPLE      | Presidents | ALL  | NULL          | NULL | NULL    | NULL |   44 | Using where |
+----+-------------+------------+------+---------------+------+---------+------+------+-------------+

# Or, using the other form of display:  EXPLAIN ... \G
           id: 1
  select_type: SIMPLE
        table: Presidents
         type: ALL        <-- Implies table scan
possible_keys: NULL
          key: NULL       <-- Implies that no index is useful, hence table scan
      key_len: NULL
          ref: NULL
         rows: 44         <-- That's about how many rows in the table, so table scan
        Extra: Using where
```

## Implementation Details

First, let's describe how InnoDB stores and uses indexes.

* The data and the PRIMARY KEY are "clustered" together in on BTree.
* A BTree lookup is quite fast and efficient. For a million-row table there might be 3 levels of BTree, and the top two levels are probably cached.
* Each secondary index is in another BTree, with the PRIMARY KEY at the leaf.
* Fetching 'consecutive' (according to the index) items from a BTree is very efficient because they are stored consecutively.
* For the sake of simplicity, we can count each BTree lookup as 1 unit of work, and ignore scans for consecutive items. This approximates the number of disk hits for a large table in a busy system.

For MyISAM, the PRIMARY KEY is not stored with the data, so think of it as being a secondary key (over-simplified).

## INDEX(first\_name), INDEX(last\_name)

The novice, once he learns about indexing, decides to index lots of columns, one at a time. But...

MariaDB rarely uses more than one index at a time in a query. So, it will analyze the possible indexes.

* first\_name -- there are 2 possible rows (one BTree lookup, then scan consecutively)
* last\_name -- there are 2 possible rows\
  Let's say it picks last\_name. Here are the steps for doing the SELECT:

1. Using INDEX(last\_name), find 2 index entries with last\_name = 'Johnson'.
2. Get the PRIMARY KEY (implicitly added to each secondary index in InnoDB); get (17, 36).
3. Reach into the data using seq = (17, 36) to get the rows for Andrew Johnson and Lyndon B. Johnson.
4. Use the rest of the WHERE clause filter out all but the desired row.
5. Deliver the answer (1865-1869).

```sql
EXPLAIN  SELECT  term
  FROM  Presidents
  WHERE  last_name = 'Johnson'
  AND  first_name = 'Andrew'  \G
  select_type: SIMPLE
        table: Presidents
         type: ref
possible_keys: last_name, first_name
          key: last_name
      key_len: 92                 <-- VARCHAR(30) utf8 may need 2+3*30 bytes
          ref: const
         rows: 2                  <-- Two 'Johnson's
        Extra: Using where
```

## "Index Merge Intersect"

OK, so you get really smart and decide that MariaDB should be smart enough to use both name indexes to get the answer. This is called "Intersect".

1. Using INDEX(last\_name), find 2 index entries with last\_name = 'Johnson'; get (7, 17)
2. Using INDEX(first\_name), find 2 index entries with first\_name = 'Andrew'; get (17, 36)
3. "And" the two lists together (7,17) & (17,36) = (17)
4. Reach into the data using seq = (17) to get the row for Andrew Johnson.
5. Deliver the answer (1865-1869).

```sql
id: 1
  select_type: SIMPLE
        table: Presidents
         type: index_merge
possible_keys: first_name,last_name
          key: first_name,last_name
      key_len: 92,92
          ref: NULL
         rows: 1
        Extra: Using intersect(first_name,last_name); Using where
```

The EXPLAIN fails to give the gory details of how many rows collected from each index, etc.

## INDEX(last\_name, first\_name)

This is called a "compound" or "composite" index since it has more than one column.

1. Drill down the BTree for the index to get to exactly the index row for Johnson+Andrew; get seq = (17).
2. Reach into the data using seq = (17) to get the row for Andrew Johnson.
3. Deliver the answer (1865-1869).\
   This is much better. In fact this is usually the "best".

```sql
ALTER TABLE Presidents
        (DROP old indexes AND...)
        ADD INDEX compound(last_name, first_name);

           id: 1
  select_type: SIMPLE
        table: Presidents
         type: ref
possible_keys: compound
          key: compound
      key_len: 184             <-- The length of both fields
          ref: const,const     <-- The WHERE clause gave constants for both
         rows: 1               <-- Goodie!  It homed in on the one row.
        Extra: Using where
```

## "Covering": INDEX(last\_name, first\_name, term)

Surprise! We can actually do a little better. A "Covering" index is one in which _all_ of the fields of the SELECT are found in the index. It has the added bonus of not having to reach into the "data" to finish the task.

1. Drill down the BTree for the index to get to exactly the index row for Johnson+Andrew; get seq = (17).
2. Deliver the answer (1865-1869).\
   The "data" BTree is not touched; this is an improvement over "compound".

```sql
... ADD INDEX covering(last_name, first_name, term);

           id: 1
  select_type: SIMPLE
        table: Presidents
         type: ref
possible_keys: covering
          key: covering
      key_len: 184
          ref: const,const
         rows: 1
        Extra: Using where; Using index   <-- Note
```

Everything is similar to using "compound", except for the addition of "Using index".

## Variants

* What would happen if you shuffled the fields in the WHERE clause?\
  Answer: The order of ANDed things does not matter.
* What would happen if you shuffled the fields in the INDEX?\
  Answer: It may make a huge difference. More in a minute.
* What if there are extra fields on the end?\
  Answer: Minimal harm; possibly a lot of good (eg, 'covering').
* Reduncancy? That is, what if you have both of these: INDEX(a), INDEX(a,b)?\
  Answer: Reduncy costs something on INSERTs; it is rarely useful for SELECTs.
* Prefix? That is, INDEX(last\_name(5). first\_name(5))\
  Answer: Don't bother; it rarely helps, and often hurts. (The details are another topic.)

## More examples:

```sql
INDEX(last, first)
    ... WHERE last = '...' -- good (even though `first` is unused)
    ... WHERE first = '...' -- index is useless

    INDEX(first, last), INDEX(last, first)
    ... WHERE first = '...' -- 1st index is used
    ... WHERE last = '...' -- 2nd index is used
    ... WHERE first = '...' AND last = '...' -- either could be used equally well

    INDEX(last, first)
    Both of these are handled by that one INDEX:
    ... WHERE last = '...'
    ... WHERE last = '...' AND first = '...'

    INDEX(last), INDEX(last, first)
    In light of the above example, don't bother including INDEX(last).
```

## Postlog

Refreshed -- Oct, 2012; more links -- Nov 2016

## See also

* [Cookbook on designing the best index for a SELECT](https://mysql.rjweb.org/doc.php/index_cookbook_mysql)
* [Sheeri's discussing of Indexes](https://technocation.org/files/doc/2013_02_MySQLindexes.pdf)
* [Slides on EXPLAIN](https://www.slideshare.net/phpcodemonkey/mysql-explain-explained)
* [Mysql manual page on range accesses in composite indexes](https://dev.mysql.com/doc/refman/5.7/en/range-optimization.html#range-access-multi-part)
* [Overhead of Composite Indexes](https://stackoverflow.com/questions/32418812/overhead-of-composite-indexes)
* [Size and other limits on Indexes](https://mysql.rjweb.org/doc.php/limits)

Rick James graciously allowed us to use this article in the documentation.

[Rick James' site](https://mysql.rjweb.org/) has other useful tips, how-tos,\
optimizations, and debugging tips.

Original source: [index1](https://mysql.rjweb.org/doc.php/index1)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
