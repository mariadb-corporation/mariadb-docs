# Google Summer of Code 2021

In 2021, we again participated in the [Google Summer of Code](https://summerofcode.withgoogle.com/). The [MariaDB Foundation](https://www.mariadb.org) believes we are making a better database that remains application compatible with MySQL. We also work on making LGPL connectors (currently [C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c), [ODBC](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc), [Java](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j), [Node.js](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/nodejs-connector/README.md)) and on [MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/galera/README.md), which allows you to scale your reads & writes. And we have [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/mariadb-columnstore/README.md), which is a columnar storage engine, designed to process petabytes of data with real-time response to analytical queries.

## Where to Start

Please join us on [Zulip](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/irc-chat-servers-and-zulip-instance/README.md) to mingle with the community. You should also subscribe to [maria-developers@lists.launchpad.net](https://launchpad.net/~maria-developers) (this is the main list where we discuss development).

To improve your chances of being accepted, it is a good idea to submit a pull request with a bug fix to the server.

Also see the [List of beginner friendly issues](https://jira.mariadb.org/issues/?jql=status%20%3D%20Open%20AND%20resolution%20%3D%20Unresolved%20AND%20labels%20%3D%20beginner-friendly%20ORDER%20BY%20updated%20DESC) and [issues labelled gsoc21](https://jira.mariadb.org/issues/?jql=labels=gsoc21) from the MariaDB Issue Tracker.

## List of Tasks

#### Support for GTID in mysqlbinlog

The mysqlbinlog client program needs to be updated to support GTID.\
Here is a suggested list of things to be done:

* The `--start-position` and `--stop-position` options should be able to take\
  GTID positions; or maybe there should be new `--start-gtid` and `--stop-gtid`\
  options. Like `--start-gtid=0-1-100,1-2-200,2-1-1000`.
* A GTID position means the point just _after_ that GTID. So starting from\
  GTID 0-1-100 and stopping at GTID 0-1-200, the first GTID output will\
  probably be 0-1-101 and the last one 0-1-200. Note that if some domain is\
  not specified in the position, it means to start from the begining,\
  respectively stop immediately in that domain.
* Starting and stopping GTID should work both with local files, and with`--read-from-remote-server`. For the latter, there are a couple of extra\
  things that need doing in the master-slave protocol, see`get_master_version_and_clock()` in `sql/slave.cc`.
* At the end of the dump, put these statements, to reduce the risk of those session variables incorrectly spilling into subsequent statements run in the same session:

```
SET session.server_id = @@global.server_id,
       session.gtid_domain_id=@@global.gtid_domain_id;
```

Probably some more things will come up during the work, but this looks like a\
reasonable start.

| Details: | Mentor:                                                |
| -------- | ------------------------------------------------------ |
| Details: | [MDEV-4989](https://jira.mariadb.org/browse/MDEV-4989) |
| Mentor:  | Brandon Nesterenko                                     |

#### Granted to PUBLIC

Implement the standard behavior for

```
GRANT xxx TO PUBLIC;
REVOKE xxx FROM PUBLIC;
```

Also, this statement is supposed to work:

```
SHOW GRANTS FOR PUBLIC;
```

And these should not

```
CREATE ROLE PUBLIC;
DROP ROLE PUBLIC;
SET ROLE PUBLIC;
GRANT PUBLIC TO xxx;
REVOKE PUBLIC FROM xxx;
```

Note that

```
SHOW GRANTS FOR xxx;
```

should not list roles and privileges granted to PUBLIC (unless granted to xxx too), but

```
SHOW GRANTS;
```

should, arguably, list them.

| Details: | Mentor:                                                |
| -------- | ------------------------------------------------------ |
| Details: | [MDEV-5215](https://jira.mariadb.org/browse/MDEV-5215) |
| Mentor:  | Oleksandr Byelkin                                      |

#### Control over memory allocated for SP/PS

SP/PS (Stored Procedures / Prepared Statements) allocates memory till the PS cache of SP will be destroyed. There is no way to see how many memory allocated and if it grows with each execution (first 2 execution can lead to new memory allocation but not more)**Task minimum:**\
Status variables which count the memory used/allocated for SP/PS by thread and/or for the server.**Other ideas:**

* Automatic stop allocation in debugging version after second execution and call exception on attempt.
* Information schema by threads and SP/PS with information about allocated and used memory

Information can be collected in MEM\_ROOTs of SP/PS. Storing info about status of mem\_root before execution then checking after new allocated memory can be found.\
MEM\_ROOT can be changed to have debug mode which make it read only which can be switched on after second execution.

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-14959](https://jira.mariadb.org/browse/MDEV-14959) |
| Mentor:  | Oleksandr Byelkin                                        |

#### Add JSON\_NORMALIZE function to normalize JSON values

Background is this question on stackexchange:[mariadb-compare-json](https://dba.stackexchange.com/questions/208481/mariadb-compare-json)\
The task is to provide a function that can be used to compare 2 json documents for equality, then name can be e.g JSON\_NORMALIZE\
JSON\_COMPACT already takes care of removing spaces, but this is not sufficient.\
Keys need to be (recursively) sorted , and if spaces are removed, then documents can be compared as binary strings.

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-16375](https://jira.mariadb.org/browse/MDEV-16375) |
| Mentor:  | Vicențiu Ciorbaru                                        |

#### Add linear regression functions

The following linear regression functions exist in a number of other DBMSs, such as Oracle, PostgreSQL:

```
REGR_SLOPE
    REGR_INTERCEPT
    REGR_COUNT
    REGR_R2
    REGR_AVGX
    REGR_AVGY
    REGR_SXX
    REGR_SYY
    REGR_SXY
```

Some have also been added to Columnstore.

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-17467](https://jira.mariadb.org/browse/MDEV-17467) |
| Mentor:  | Nikita Malyavin                                          |

#### Create utility to parse frm files and print their DDL

It would be useful if MariaDB had a utility that was able to parse frm files and print the DDL associated with the table.\
For example, it would be useful for users who performed a partial backup with mariadb-backup:[partial-backup-and-restore-with-mariadb-backup](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/contributing-participating/google-summers-of-code/broken-reference/README.md)\
But they forgot to also backup the table DDL, so they can't restore the tables using the following process:[innodb-file-per-table-tablespaces](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces)\
mysqlfrm is a tool that already exists that does similar things:[mysqlfrm.py](https://github.com/mysql/mysql-utilities/blob/master/scripts/mysqlfrm.py)\
But it doesn't seem very user-friendly. It needs to be able to contact the local MariaDB server, and it also needs to be able to spawn a server instance, and it seems to need to be able to create a bunch of files during this process. e.g.:

```
[ec2-user@ip-172-30-0-249 ~]$ cd /tmp
[ec2-user@ip-172-30-0-249 tmp]$ sudo mysqlfrm --server=root:@localhost:3306 /var/lib/mysql/db1/tab.frm --port=12345 --user=mysql
# Source on localhost: ... connected.
# Spawning server with --user=mysql.
# Starting the spawned server on port 12345 ... done.
# Reading .frm files
#
# Reading the tab.frm file.
#
# CREATE statement for /var/lib/mysql/db1/tab.frm:
#

CREATE TABLE `db1`.`tab` (
  `id` int(11) NOT NULL,
  `str` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1

#...done.
```

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-18827](https://jira.mariadb.org/browse/MDEV-18827) |
| Mentor:  | Vicențiu Ciorbaru                                        |

#### JSON\_DETAILED output unnecessarily verbose

JSON\_DETAILED function ([json\_detailed](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_detailed) ) is described as

```
Represents JSON in the most understandable way emphasizing nested structures.
```

We now got a use case for it: Optimizer Trace output. Optimizer trace is too large to be copied in full, instead we use expressions like

```
select 
JSON_DETAILED(JSON_EXTRACT(trace, '$**.analyzing_range_alternatives')) 
from INFORMATION_SCHEMA.OPTIMIZER_TRACE;
```

Our experience is that `JSON_DETAILED` has some room for improvement when it comes to the quality of automatic JSON formatting.\
Example:

```
source mdev19160-data.sql
mysql> select JSON_DETAILED(JSON_EXTRACT(a, '$**.analyzing_range_alternatives')) from t200\G
*************************** 1. row ***************************
JSON_DETAILED(JSON_EXTRACT(a, '$**.analyzing_range_alternatives')): [

    {
        "range_scan_alternatives": 
        [

            {
                "index": "a_b",
                "ranges": 
                [
                    "2 <= a <= 2 AND 4 <= b <= 4"
                ],
                "rowid_ordered": true,
                "using_mrr": false,
                "index_only": true,
                "rows": 1,
                "cost": 1.1752,
                "chosen": true
            }
        ],
        "analyzing_roworder_intersect": 
        {
            "cause": "too few roworder scans"
        },
        "analyzing_index_merge_union": 
        [
        ]
    }
]
```

Things to note:

* empty lines at the start (right before/after the "range\_scan\_alternatives")
* `"analyzing_index_merge_union":[]` occupies 3 lines where one would be sufficient.
* the same goes for "ranges"

One can look at the JSON pretty-printer that is used by EXPLAIN FORMAT=JSON and optimizer trace. It produces a better result (but it has room for improvement, too.)\
Extra: in MySQL, the function is called JSON\_PRETTY. We should add ability to use this name as an alias.

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-19160](https://jira.mariadb.org/browse/MDEV-19160) |
| Mentor:  | Vicențiu Ciorbaru                                        |

#### Histograms: use JSON as on-disk format

Currently, histograms are stored as array of 1-byte bucket bounds (SINGLE\_PREC\_HB) or 2-byte bucket bounds (DOUBLE\_PREC\_HB).\
The table storing the histograms supports different histogram formats but limits them to 256 bytes (hist\_size is tinyint).

```
CREATE TABLE mysql.column_stats (
  min_value varbinary(255) DEFAULT NULL, 
  max_value varbinary(255) DEFAULT NULL, 
  ...
  hist_size tinyint unsigned, 
  hist_type enum('SINGLE_PREC_HB','DOUBLE_PREC_HB'), 
  histogram varbinary(255), 
  ...
```

This prevents us from supporting other kinds of histograms.\
The first low-hanging fruit would be to store the histogram bucket bounds precisely (like MySQL and PostgreSQL do, for example).\
The idea of this MDEV is to switch to JSON as storage format for histograms.\
If we do that, it will:

* Improve the histogram precision
* Allow the DBAs to examine the histograms
* Enable other histogram types to be collected/used.\
  h2. Milestone-1:\
  Let histogram\_type have another possible value, tentative name "JSON"\
  when that is set, let ANALYZE TABLE syntax collect a JSON "histogram"

```
{ "hello":"world"}
```

that is, the following should work:

```
set histogram_type='json';
analyze table t1 persisent for all;
select histogram from mysql.column_stats where table_name='t1' ;
```

this should produce {"hello":"world"}.\
h2. Milestone-2: produce JSON with histogram(_)._\
&#xNAN;_(_)- the exact format is not specified, for now, print the bucket endpoints and produce output like this:

```
[
  "value1",
  "value2",
  ...
]
```

Milestone-2, part#2: make mysql.column\_stats.histogram a blob.\
h2. Milestone-3: Parse the JSON back into an array\
Figure out how to use the JSON parser.\
Parse the JSON data produced in Milestone-2 back. For now, just print the parsed values to stderr.\
(Additional input provided on Zulip re parsing valid/invalid JSON histograms)\
h2. Milestone-4: Make the code support different kinds of Histograms\
Currently, there's only one type of histogram.\
smaller issue: histogram lookup functions assume the histogram stores fractions, not values.\
bigger issue: memory allocation for histograms is de-coupled from reading the histograms. See alloc\_statistics\_for\_table, read\_histograms\_for\_table.\
The histogram object lives in a data structure that is bzero'ed first and then filled later (IIRC there was a bug (fixed) where the optimizer attempted to use bzero'ed histogram)\
Can histograms be collected or loaded in parallel by several threads? This was an (unintentional?) possibility but then it was disabled (see TABLE\_STATISTICS\_CB object and its use)\
h3. Step #0: Make Histogram a real class\
Here's the commit:[3ac32917ab6c42a5a0f9ed817dd8d3c7e20ce34d](https://github.com/MariaDB/server/commit/3ac32917ab6c42a5a0f9ed817dd8d3c7e20ce34d)\
h3. Step 1: Separate classes for binary and JSON histograms\
Need to introduce

```
class Histogram -- interface, no data members.
class Histogram_binary : public Histogram
class Histogram_json : public Histogram
```

and a factory function

```
Histogram *create_histogram(Histogram_type)
```

for now, let Histogram\_json::point\_selectivity() and Histogram\_json::range\_selectivity() return 0.1 and 0.5, respectively.\
h3. Step 2: Demonstrate saving/loading of histograms\
Now, the code already can:

* collect a JSON histogram and save it.
* when loading a histogram, figure from `histogram_type` column that this is JSON histogram being loaded, create Histogram\_json and invoke the parse function.\
  Parse function at the moment only prints to stderr.\
  However, we should catch parse errors and make sure they are reported to the client.\
  The test may look like this:

```
INSERT INTO mysql.column_stats VALUES('test','t1','column1', .... '[invalid, json, data']);
FLUSH TABLES;
# this should print some descriptive test
--error NNNN
select * from test.t1;
```

h2. Milestone-5: Parse the JSON data into a structure that allows lookups.\
The structure is

```
std::vector<std::string>
```

and it holds the data in KeyTupleFormat (See the comments for reasoning. There was a suggestion to use `in_vector` (This is what IN subqueries use) but it didn't work out)\
h2. Milestone 5.1 (aka Milestone 44)\
Make a function to estimate selectivity using the data structure specified in previous milestone.\
h2. Make range\_selectivity() accept key\_range parameters.\
(currently, they accept fractions, which is only suitable for binary histograms)\
This means Histogram\_binary will need to have access to min\_value and max\_value to compute the fractions.

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-21130](https://jira.mariadb.org/browse/MDEV-21130) |
| Mentor:  | Sergei Petrunia                                          |

#### make my\_vsnprintf to use gcc-compatible format extensions

`my_vsnprintf()` is used internally in the server as a portable `printf` replacement. And it's also exported to plugins as a service.\
It supports a subset of `printf` formats and three extensions:

* `%`s\` means that a string should be quoted like an `identifier`
* `%b` means that it's a binary string, not zero-terminated; printing won't stop at `\0`, so one should always specify the field width (like `%.100b`)
* `%M` is used in error messages and prints the integer (errno) and the corresponding `strerror()` for it

gcc knows `printf` formats and check whether actual arguments match the format string and issue a warning if they don't. Unfortunately there seems to be no easy way to teach gcc our extensions, so for now we have to disable `printf` format checks.\
An better approach would be to use gcc compatible format extensions, like Linux kernel does. We should migrate to a different syntax for our extensions

* `%sI` to mean "print as an identifier"
* `%sB` to mean "print a binary string"
* `%uE` to mean "print an errno"
* `%sT` to put a "..." as truncation indicator

old formats can still be supported or they can be removed and in the latter case the major version of the service should be increased to signal an incompatible change.\
All error messages and all usages of `my_vsnprintf` should be changed to use the new syntax and gcc `printf` format checks should be enabled.

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-21978](https://jira.mariadb.org/browse/MDEV-21978) |
| Mentor:  | Sergei Golubchik                                         |

#### Add JSON\_EQUALS function to check JSON equality

JSON\_CONTAINS can be used to test for JSON object equality in some cases, but we seem to lack a clear JSON\_EQUALS function.

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-23143](https://jira.mariadb.org/browse/MDEV-23143) |
| Mentor:  | Vicențiu Ciorbaru                                        |

#### Concurrent multi-reader, multi-writer buffer for IO\_CACHE

IO\_CACHE has basically three read/write modes: only read, only write, and a sequential read/write FIFO mode `SEQ_READ_APPEND`.\
While some performance-sensitive places, like replication slave thread, use SEQ\_READ\_APPEND, that may be a bottleneck. since reads and writes are sequential (and co-sequential i.e. reads and writes block each other).\
The task is to implement a non-blocking mode or multi-reader, multi-writer use-case through a concurrent ring buffer implementation.\
h2. Possible approaches\
h3. Lock-free n-consumer, m-producer ring buffer\
This implementation requires limiting a number of simultaneous accessors and reserving slots for them.\
Lock-free implementations can contain busy waits, but no locks, except when a number of consumers or producers is exceeded. This can be controlled by a semaphore with a capacity of a number of cores.\
This is an ideal way, but can be an overhaul because of complicated busy loops and slot management.\
This is also hard because writes can be bigger than a buffer. See buffer excess.\
h3. Simple rwlock-based non-blocking approach\
The bottleneck basically occurs because SEQ\_READ\_APPEND blocks the whole time during buffer copy.\
We can avoid it by moving the pointers first, thus allocating a place for copying, and then make a copy from/to the buffer without a lock.\
rwlock will be used to access the pointers, i.e. reads access IO\_CACHE::end\_of\_file with read lock to make ensure the borders, but writers access it with write lock.\
h2. Buffer excess\
Excesses make things work sequential.\
When the buffer is full, a separate write buffer is created. When the write buffer is full, a flush happens.\
Flushes wait for all writers to finish first, then lock the write buffer for flushing.\
The read buffer can be flushed in a more relaxed way: no need to need to lock for flushing, but we have to lock for buffer allocation and wait for all writers.\
Waiting for writers can be done with another rwlock.\
h2. Single-readerness\
The real-world cases are mostly single-consumer, and it is essential for IO\_CACHE: it is variable-lengthed, and has no underlying data format,\
so the reader always has to make at least two sequential reads (one to read size and another to read the body)\
Single-readerness considerations can relax some conditions and ease the implementation\
h2. io\_cache\_reserve api\
We can add a function to reserve the space to writing for the case of writing big objects (both bigger then the write cache\
and smaller then the latter, but big enough to not fit to the external buffer), for the cases like copying one cache to another.\
The function should return future-like object, since we have to notify IO\_CACHE back that the writing is finished (to make flush for example)

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-24676](https://jira.mariadb.org/browse/MDEV-24676) |
| Mentor:  | Nikita Malyavin                                          |

#### Custom formatting of strings in MariaDB queries

Formatting more complex strings in a `SELECT` statement can get awkward when there are many `concat()`, `format()`, etc calls involved.\
It would be very cool and helpful to have a function that takes an input string and a formatting specification and returns string formatted using the rules the user passed in the specification.\
A great example for such a function is the classic `C printf` function, which, in this context, would look something like:`SELECT printf('%s %s, %s', first_name, last_name, job_title) from employees;`\
But it doesn't necessarily need to look this way, an alternative syntax could be Python-ish, which would leverage the fact that the server already knows the datatype of each field used in the formatting scheme:`SELECT sformat('arg1: {}, arg2: {}', col1, col2) from table;`\
In that syntax one passes formatting options within the curly braces:

```
-- Print 'arg1: col1, arg2: col2'  where col1 from table is of datetime type and should be printed as: 'Sunday November 2021'
SELECT sformat('arg1: {%W %M %Y}, arg2: {}', col1, col2) from table;
```

Ideally, this new function should use, behind the scenes, the existing builtin formatting functions in MariaDB (e.g. `date_format()`, `format()`) and even future formatting functions (e.g. MySQL's `format_bytes()`, `format_pico_time()`), so the syntax has to be designed in a smart way to accommodate easily future additions.

| Details: | Mentor:                                                  |
| -------- | -------------------------------------------------------- |
| Details: | [MDEV-25015](https://jira.mariadb.org/browse/MDEV-25015) |
| Mentor:  | Sergei Golubchik                                         |

#### Add autocompletion capabilities to the MariaDB Jupyter kernel

As part of the [Jupyter Messaging](https://jupyter-client.readthedocs.io/en/stable/messaging.html) protocol, the Jupyter frontend sends a `complete_request` message to the MariaDB kernel when the user invokes the code completer in a Jupyter notebook.\
This message is handled in the [do\_complete](https://github.com/MariaDB/mariadb_kernel/blob/eadfbedbba93c0ea1146165580d86b050414e32a/mariadb_kernel/kernel.py#L111) function from the `MariaDBKernel` class.\
In simpler words, whenever the user hits the key shortcut for code autocompletion in a notebook, the MariaDB kernel's do\_complete function is called with a number of arguments that help the kernel understand what the user wants to autocomplete.\
So the autocompletion infrastructure in the MariaDB kernel is already kindly provided by Jupyter, we only need to send back to Jupyter a list of suggestions based on the arguments that `do_complete` receives :-).\
Ideally we should aim to enable at least database, table and column name completion and also SQL keyword completion.\
But no worries, there are plenty of possibilities to extend the functionality even more if the accepted student turns out to be very productive :D

| Details: | Mentor:                                                             |
| -------- | ------------------------------------------------------------------- |
| Details: | [Project Issue](https://github.com/MariaDB/mariadb_kernel/issues/5) |
| Mentor:  | Robert Bindar                                                       |

#### Implement interacting editing of result sets in the MariaDB Jupyter kernel

At this moment the MariaDB kernel is only capable of getting the results sets from the MariaDB client in `HTML` format and packing them in a Jupyter compatible format. Jupyter then displays them in notebooks like it would display Python Pandas dataframes.\
Sure, the users can easily write `SQL` code to modify the content of a table like they would write in a classical command line database client.\
But we want to go a bit further, we would love to have the capability to edit a result set returned by a `SELECT` statement (i.e. double click on table cells and edit) and have a button that users can press to generate a `SQL` statement that will update the content of the table via the MariaDB server.\
Apart from interacting with the Jupyter frontend for providing this UI capability, we also have to implement a field integrity functionality so that we make sure users can't enter data that is not compatible with the datatype of the column as it is seen by the MariaDB server.\
The project should start with a fair bit of research to understand how we can play with the [Jupyter Messaging](https://jupyter-client.readthedocs.io/en/stable/messaging.html) protocol to create the UI functionality and also to check other Jupyter kernels and understand what's the right and best approach for tackling this.

| Details: | Mentor:                                                              |
| -------- | -------------------------------------------------------------------- |
| Details: | [Project Issue](https://github.com/MariaDB/mariadb_kernel/issues/12) |
| Mentor:  | Andreia Hendea                                                       |

#### Make the MariaDB Jupyter kernel capable of dealing with huge SELECTs

Currently the MariaDB kernel doesn't impose any internal limits for the number of rows a user can `SELECT` in a notebook cell. Internally the kernel gets the result set from MariaDB and stores it in a pandas DataFrame, so users can use it with magic commands to chart data.\
But this DataFrame is stored in memory, so if you `SELECT` a huge number of rows, say 500k or 1M, it's probably not a very good idea to create such a huge DataFrame.\
We tested with 500k rows, and the DataFrame itself is not the biggest problem, it consumed around 500MB of memory. The problem is the amount of rows the browser needs to render, for 500k rows the browser tab with the notebook consumes around 2GB of memory, so the Jupyter frontend (JupyterLab, Jupyter Notebook) slows down considerably.\
A potential solution is to introduce a two new config options which would specify:

* a limit for the number of rows the Jupyter notebook should render, a reasonable default value for this could 50 rows for instance (`display_max_rows`)
* a limit for each `SELECT` statement, `limit_max_rows`, that the kernel would use to determine whether it should store the result set in memory in a DataFrame or store the result set on disk. A reasonable default value might be 100k rows.

The trickiest part of the project though is that, once the kernel writes a result set on disk, the charting magic commands need to detect that the data is not in memory, it is on disk, and they should find a smart mechanism for generating the chart from the disk data without loading the entire data in memory (which would defeat the whole purpose of the project). This might involve finding a new Python plotting library (instead of current matplotlib) that can accomplish the job.

| Details: | Mentor:                                                             |
| -------- | ------------------------------------------------------------------- |
| Details: | [Project Issue](https://github.com/MariaDB/mariadb_kernel/issues/9) |
| Mentor:  | Vlad Bogolin                                                        |

## Suggest a Task

Do you have an idea of your own, not listed above? Do let us know!

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
