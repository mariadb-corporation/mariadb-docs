# About SphinxSE

The Sphinx storage engine (SphinxSE) is a storage engine that talks to searchd (the Sphinx daemon) to enable text searching. Sphinx and SphinxSE is used as a faster and more customizable alternative to MariaDB's [built-in full-text search](../../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/full-text-indexes/).

Sphinx does not depend on MariaDB, and can run independently, but SphinxSE provides a convenient interface to the underlying Sphinx daemon.

## Versions of SphinxSE in MariaDB

| SphinxSE Version                                             | Introduced                                                                                                                                                                                                                                                                                                                            | Maturity |
| ------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| [SphinxSE 2.2.6](https://sphinxsearch.com/docs/current.html) | [MariaDB 10.0.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10015-release-notes)                                                                                                                                                                         | Stable   |
| [SphinxSE 2.1.9](https://sphinxsearch.com/docs/2.1.9/)       | [MariaDB 10.0.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/mariadb-10014-release-notes)                                                                                                                                                                         | Stable   |
| SphinxSE 2.0.4                                               | [MariaDB 5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-5-series/changes-improvements-in-mariadb-5-5)                                                                                                                                                                      |          |
| SphinxSE 0.99                                                | [MariaDB 5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-2-series/changes-improvements-in-mariadb-5-2) and [MariaDB 5.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-5-3-series/changes-improvements-in-mariadb-5-3) |          |

## Enabling SphinxSE in MariaDB

The Sphinx storage engine is included in the source, binaries, and packages of MariaDB. SphinxSE is built as a dynamically loadable .so plugin. To use it, you need to perform a one-time install:

```sql
INSTALL SONAME 'ha_sphinx';
```

Once installed, SphinxSE will show up in the list of installed storage engines:

```sql
SHOW ENGINES;
+------------+---------+--------------------------------------------+--------------+------+------------+
| Engine     | Support | Comment                                    | Transactions | XA   | Savepoints |
+------------+---------+--------------------------------------------+--------------+------+------------+
...
| SPHINX     | YES     | Sphinx storage engine 0.9.9                | NO           | NO   | NO         |
...
+------------+---------+--------------------------------------------+--------------+------+------------+
```

This is a one-time step and will not need to be performed again.

**Note:** SphinxSE is just the storage engine part of Sphinx. You will have to [install Sphinx](installing-sphinx.md) itself in order to make use of\
SphinxSE in MariaDB.

Despite the name, SphinxSE does not actually store any data itself. It is\
actually a built-in client which allows MariaDB to talk to Sphinx, run search\
queries, and obtain search results. All indexing and searching happen outside\
MariaDB.

Some SphinxSE applications include:

* easier porting of MariaDB/MySQL FTS applications to Sphinx
* allowing Sphinx use with programming languages for which native APIs are not\
  available yet
* optimizations when additional Sphinx result set processing on the MariaDB\
  side is required (eg. JOINs with original document tables, additional\
  MariaDB-side filtering, and etc...)

## Using SphinxSE

### Basic Usage

To search via SphinxSE, you would need to create a special`ENGINE=SPHINX` "search table", and then`SELECT` from it with full text query put into the`WHERE` clause for query column.

Here is an example create statement and search query:

```
CREATE TABLE t1
(
    id          BIGINT UNSIGNED NOT NULL,
    weight      INTEGER NOT NULL,
    query       VARCHAR(3072) NOT NULL,
    group_id    INTEGER,
    INDEX(query)
) ENGINE=SPHINX CONNECTION="sphinx://127.0.0.1:9312/test1";

SELECT * FROM t1 WHERE query='test it;mode=any';
```

The first three columns of the search table must have a type of `BIGINT` for the 1st column (document id),`INTEGER` or `BIGINT` for the 2nd column\
(match weight), and `VARCHAR` or `TEXT` for\
the 3rd column (your query), respectively. This mapping is fixed; you cannot\
omit any of these three required columns, or move them around, or change types.\
Also, the query column must be indexed; all the others must be kept unindexed.\
Column names are ignored so you can use arbitrary ones.

Additional columns must be either `INTEGER`,`TIMESTAMP`, `BIGINT`,`VARCHAR`, or `FLOAT`. They are bound to\
the attributes provided in the Sphinx result set by name, so their names must\
match the attribute names specified in `sphinx.conf`. If\
there's no such attribute name in the Sphinx search results, the additional\
columns will have `NULL` values.

Special "virtual" attribute names can also be bound to SphinxSE columns.`_sph_` needs to be used instead of `@` for\
that. For instance, to obtain the values of '`@groupby`',\
'`@count`', or '`@distinct`' virtual\
attributes, use '`_sph_groupby`',\
'`_sph_count`' or '`_sph_distinct`' column\
names, respectively.

The `CONNECTION` string parameter is used to specify the\
default `searchd` host, port, and indexes for queries issued\
using this table. If no connection string is specified in `CREATE TABLE`, index name '`*`' (ie. search all indexes) and\
'`127.0.0.1:9312`' are assumed. The connection string syntax\
is as follows:

```
CONNECTION="sphinx://HOST:PORT/INDEXNAME"
```

You can change the default connection string later like so:

```
ALTER TABLE t1 CONNECTION="sphinx://NEWHOST:NEWPORT/NEWINDEXNAME";
```

You can also override all these parameters per-query.

**Note:** To use Linux sockets you can modify the searchd section of the Sphinx configuration file, setting the listen parameter to a socket file. Instruct SphinxSE about the socket using CONNECTION="unix:_unix/domain/socket\[:index]"._

### Search Options

As seen in the example above, both query text and search options should be put\
into the '`WHERE`' clause of the search query column (i.e. the\
3rd column); the options are separated by semicolons ('`;`') and\
separate names from values using an equals sign ('`=`'). Any\
number of options can be specified. Available options are:

* query - query text;
* mode - matching mode. Must be one of "all", "any", "phrase", "boolean", or\
  "extended". Default is "all";
* sort - match sorting mode. Must be one of "relevance", "attr\_desc",\
  "attr\_asc", "time\_segments", or "extended". In all modes besides "relevance"\
  attribute name (or sorting clause for "extended") is also required after a\
  colon:

```
... WHERE query='test;sort=attr_asc:group_id';
... WHERE query='test;sort=extended:@weight desc, group_id asc';
```

* offset - offset into result set, default is 0;
* limit - amount of matches to retrieve from result set, default is 20;
* index - names of the indexes to search:

```
... WHERE query='test;index=test1;';
... WHERE query='test;index=test1,test2,test3;';
```

* minid, maxid - min and max document ID to match;
* weights - comma-separated list of weights to be assigned to Sphinx full-text\
  fields:

```
... WHERE query='test;weights=1,2,3;';
```

* filter, !filter - comma-separated attribute name and a set of values to\
  match:

```
# only include groups 1, 5 and 19
... WHERE query='test;filter=group_id,1,5,19;';

# exclude groups 3 and 11
... WHERE query='test;!filter=group_id,3,11;';
```

* range, !range - comma-separated attribute name, min and max value to\
  match:

```
# include groups from 3 to 7, inclusive
... WHERE query='test;range=group_id,3,7;';

# exclude groups from 5 to 25
... WHERE query='test;!range=group_id,5,25;';
```

* maxmatches - per-query max matches value:

```
... WHERE query='test;maxmatches=2000;';
```

* groupby - group-by function and attribute:

```
... WHERE query='test;groupby=day:published_ts;';
... WHERE query='test;groupby=attr:group_id;';
```

* groupsort - group-by sorting clause:

```
... WHERE query='test;groupsort=@count desc;';
```

* indexweights - comma-separated list of index names and weights to use when\
  searching through several indexes:

```
... WHERE query='test;indexweights=idx_exact,2,idx_stemmed,1;';
```

* comment - a string to mark this query in query log (mapping to $comment\
  parameter in Query() API call):

```
... WHERE query='test;comment=marker001;';
```

* select - a string with expressions to compute (mapping to SetSelect() API\
  call):

```
... WHERE query='test;select=2*a+3*b as myexpr;';
```

#### Note

It is much more efficient to allow Sphinx to perform sorting,\
filtering, and slicing of the result set than to raise max matches count and\
use '`WHERE`', '`ORDER BY`', and\
'`LIMIT`' clauses on the MariaDB side. This is for two\
reasons:

1. Sphinx does a number of optimizations and performs better than\
   MariaDB/MySQL on these tasks.
2. Less data would need to be packed by `searchd`, and\
   transferred and unpacked by SphinxSE.\
   <>

### SHOW ENGINE SPHINX STATUS

Starting with version 0.9.9-rc1, additional query info besides the result set\
can be retrieved with the '`SHOW ENGINE SPHINX STATUS`'\
statement:

```
SHOW ENGINE SPHINX STATUS;
+--------+-------+-------------------------------------------------+
| Type   | Name  | Status                                          |
+--------+-------+-------------------------------------------------+
| SPHINX | stats | total: 25, total found: 25, time: 126, words: 2 | 
| SPHINX | words | sphinx:591:1256 soft:11076:15945                | 
+--------+-------+-------------------------------------------------+
```

This information can also be accessed through status variables. Note that this\
method does not require super-user privileges.

```
SHOW STATUS LIKE 'sphinx_%';
+--------------------+----------------------------------+
| Variable_name      | Value                            |
+--------------------+----------------------------------+
| sphinx_total       | 25                               | 
| sphinx_total_found | 25                               | 
| sphinx_time        | 126                              | 
| sphinx_word_count  | 2                                | 
| sphinx_words       | sphinx:591:1256 soft:11076:15945 | 
+--------------------+----------------------------------+
```

### JOINs with SphinxSE

You can perform `JOIN`s on a SphinxSE search table and tables using\
other engines. Here's an example with "documents" from example.sql:

```
SELECT content, date_added FROM test.documents docs
    JOIN t1 ON (docs.id=t1.id) 
    WHERE query="one document;mode=any";
+-------------------------------------+---------------------+
| content                             | docdate             |
+-------------------------------------+---------------------+
| this is my test document number two | 2006-06-17 14:04:28 | 
| this is my test document number one | 2006-06-17 14:04:28 | 
+-------------------------------------+---------------------+

SHOW ENGINE SPHINX STATUS;
+--------+-------+---------------------------------------------+
| Type   | Name  | Status                                      |
+--------+-------+---------------------------------------------+
| SPHINX | stats | total: 2, total found: 2, time: 0, words: 2 | 
| SPHINX | words | one:1:2 document:2:2                        | 
+--------+-------+---------------------------------------------+
```

## Building snippets (excerpts) via MariaDB

Starting with version 0.9.9-rc2, SphinxSE also includes a UDF function that\
lets you create snippets through MariaDB. The functionality is fully similar to\
the [BuildExcerprts](https://sphinxsearch.com/docs/current.html#api-func-buildexcerpts)\
API call but is accessible through MariaDB+SphinxSE.

The function name must be '`sphinx_snippets`', you can not use an\
arbitrary name. Function arguments are as follows:

```
Prototype: function sphinx_snippets ( document, index, words, [options] );
```

Document and words arguments can be either strings or table columns. Options\
must be specified like this: `'value' AS option_name`. For a list of\
supported options, refer to the [BuildExcerprts()](https://sphinxsearch.com/docs/current.html#api-func-buildexcerpts)\
API call. The only UDF-specific additional option is named 'sphinx' and lets\
you specify searchd location (host and port).

Usage examples:

```
SELECT sphinx_snippets('hello world doc', 'main', 'world',
    'sphinx://192.168.1.1/' AS sphinx, true AS exact_phrase,
    '[b]' AS before_match, '[/b]' AS after_match)
FROM documents;

SELECT title, sphinx_snippets(text, 'index', 'mysql php') AS text
    FROM sphinx, documents
    WHERE query='mysql php' AND sphinx.id=documents.id;
```

## More Information

More information on Sphinx and SphinxSE is available on the [Sphinx website](https://sphinxsearch.com/docs/current.html).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
