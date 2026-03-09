# Google Summer of Code 2025

This year we are again participating in the [Google Summer of Code](https://summerofcode.withgoogle.com/). We, joined with the [MariaDB Foundation](https://www.mariadb.org), believe we are making a better database that remains application compatible with MySQL. We also work on making LGPL connectors (currently [C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c), [C++](https://mariadb.com/kb/en/mariadb-connector-c%2B%2B), [ODBC](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc), [Java](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j), [Node.js](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/nodejs-connector/README.md)) and on [MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/galera/README.md), which allows you to scale your reads & writes. And we have [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/mariadb-columnstore/README.md), which is a columnar storage engine, designed to process petabytes of data with real-time response to analytical queries.

## Where to Start

Please join us on [Zulip](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/irc-chat-servers-and-zulip-instance/README.md) to mingle with the community. You should also subscribe to the [developers mailing list](https://lists.mariadb.org/postorius/lists/developers.lists.mariadb.org) (this is the main list where we discuss development - there are also [other mailing lists](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/contributing-participating/google-summers-of-code/broken-reference/README.md)).

To improve your chances of being accepted, it is a good idea to submit a pull request with a bug fix to the server.

Also see the [List of beginner friendly issues](https://jira.mariadb.org/issues/?jql=status%20%3D%20Open%20AND%20resolution%20%3D%20Unresolved%20AND%20labels%20%3D%20beginner-friendly%20ORDER%20BY%20updated%20DESC) from the MariaDB Issue Tracker.

## List of Tasks

### MariaDB Server

#### [MDEV-28395](https://jira.mariadb.org/browse/MDEV-28395) LOAD DATA plugins

**Full-time project 350h**

`LOAD DATA INFILE` can flexibly load data into a table from CSV-like files accessible by the mariadbdb process. `LOAD XML INFILE` can do it for XML files. `LOAD DATA LOCAL INFILE` and `LOAD XML LOCAL INFILE` can do it with files accessible by the client, but not by the server. But there are requests to suport loading more file formats and from other locations, for example, from S3.

This project is to implement support for LOAD plugins and refactor the current LOAD code accordingly. There are two kind of plugins — data parser plugin (CSV-like and XML) and transfer plugin (file and LOCAL). Implementing new plugins is not in the scope of this task, this task is mainly about moving existing code around, creating a _possibility_ for new plugins (like JSON or S3).

**Skills needed:** C++, bison**Mentors:** Sergei Golubchik

#### [MDEV-36100](https://jira.mariadb.org/browse/MDEV-36100) Generate vector embeddings automatically on INSERT

**Full-time project 350h**

Implement a syntax and a plugin API that the server will use to generate embeddings for documents that the user stores in the database. This should allow to simplify significantly the vector pipeline. mariadbd will not generate embeddings internally, it will invoke a plugin to do that.

**Skills needed:** C++**Mentors:** Sergei Golubchik

#### [MDEV-36107](https://jira.mariadb.org/browse/MDEV-36107) expressions in mysqltest

**Part-time project 175h**

extend mysqltest language to support

* standard arithmetic `+`, `-`, `*`, `/`, `%`
* comparisons `==`, `!=`, `<`, `<=`, `>`, `>=`
* boolean `&&`, `||`, may be `? :`
* if possible: string repetition, perl-style `x` (to replace `SELECT REPEAT()` in test files)

This should work in commands `if`, `while`

Can be done together with [MDEV-36108](https://jira.mariadb.org/browse/MDEV-36108) as a full-time project.

**Skills needed:** C++**Mentors:** Sergei Golubchik

#### [MDEV-36108](https://jira.mariadb.org/browse/MDEV-36108) variable substitutions in mysqltest

**Part-time project 175h**

extend mysqltest language to support bash-like substitutions:

* `${var}`
* `${parameter:offset:length}`
* `${#parameter}`
* `${parameter/pattern/string/flags}`
* may be `${parameterˆ}`, `${parameterˆˆ}`, `${parameter,}`, `${parameter}`
* may be `${parameter@function}` with functions like `u`, `U`, `Q`, etc

recursive expansion:

* `${${var}}`

Can be done together with [MDEV-36107](https://jira.mariadb.org/browse/MDEV-36107) as a full-time project.

**Skills needed:** C++**Mentors:** Sergei Golubchik

#### [MDEV-18827](https://jira.mariadb.org/browse/MDEV-18827) Create utility to parse frm files and print their DDL

**Full-time project - potential part-time (175 - 350h, depending on scope)**

FRM files are what MariaDB uses to store metadata about tables. These files can be used to generate DDL statements (CREATE TABLE ...). We are lacking a utility to parse these files which could in turn make DBAs lives easier. The task of this project is to have this utility implemented, making use of MariaDB's FRM parsing logic. You may have to carry out some refactoring to extract the parsing code into a reusable library, once for MariaDB Server, once for the FRM parsing tool.

**Skills needed:** C/C++, understanding libraries and APIs.**Mentors:** Vicențiu Ciorbaru / Sergei Golubchik

#### [MDEV-9345](https://jira.mariadb.org/browse/MDEV-9345) Replication to enable filtering on master

**Part-time project 175h**

The current methods of filtering replication events are limited to either 1) at binlog-write time, which can break point-in-time recovery because some committed transactions will be missing from the binary log, or 2) on the replica, which forces all events on the primary server to always be sent to the replica, which can be a security concern and is also not efficient. This task aims to eliminate these limitations by adding in another point at which replication filtering occurs: on the binlog dump threads. This would allow users to both maintain a consistent binary log, and minimize network traffic by guarding events which are never intended for replication.

**Skills needed:** C++**Mentors:** Brandon Nesterenko

#### Buildbot build statistics dashboard

**Part-time project 175h**\
TODO - A more ample description will be created.

**Skills needed:Mentors:** Vlad Radu

#### [MCOL-4889](https://jira.mariadb.org/browse/MCOL-4889) Manual extent vacuuming

**Full-time project 350h**

Here extent is a unit of group of columnar values and partition is a group of extents that stores all column values for a specific portion of a table.\
MCS has a notion of an empty value for columnar segment/token files and dictionaries. Empty values are marked with a bit in the special 1 byte auxiliary column that is created for every table.\
When DELETE removes records from a table the records are marked with empty bit in the auxiliary column. The deleted records become a wasted disk space.\
The goal of the project is to reclaim the wasted disk space either re-creating the whole partition or moving partition values.

**Skills needed:** modern C++**Mentors:** Roman Nozdrin

#### [MCOL-5142](https://jira.mariadb.org/browse/MCOL-5142) Support for recursive CTE

**Full-time project 350h**

MariaDB Columnstore lacks recursive CTE handling, so as of now Columnstore hands over the processing back to MariaDB Server if a query contains recursive CTE.

Here is the info about the feature:[recursive-common-table-expressions-overview](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/common-table-expressions/recursive-common-table-expressions-overview)

**Skills needed:** modern C++**Mentors:** Leonid Fedorov

#### [MCOL-5598](https://jira.mariadb.org/browse/MCOL-5598) Support for EXCEPT and INTERSECT SQL expressions

**Full-time project 350h**

MariaDB Columnstore lacks UNION EXCEPT INTERSECT handling, so as of now Columnstore hands over the processing back to MariaDB Server if a query contains UNION EXCEPT or UNION INTERCEPT

Here is the info about the feature:[except](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/set-operations/except)[intersect](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/set-operations/intersect)

**Skills needed:** modern C++**Mentors:** Alexey Antipovsky

#### MCOL-XXX Bloom-filters for data scanning

**Full-time project 350h**

MariaDB Columnstore lacks indexes so it reads a lot of extra data from disk. This project introduces Bloom-filters to reduce data read from disk during the most IO heavy operation that is scanning.

**Skills needed:** modern C++**Mentors:** Roman Nozdrin

#### [MCOL-5758](https://jira.mariadb.org/browse/MCOL-5758) Reduce the computations in JOINS by simpler Bloom-filter-based pre-joins

**Full-time project 350h**

Joins are very heavy algorithms, both in computation and/or in memory use. They need to hold a substantial amount of data in memory and perform hashing and other operations on that data. Joins can overflow memory limits and keeping balance between memory use and performance is tricky. Thus we have to filter information thaat is going into joins as much as possible. Columnstore already does great work in that regard, pushing WHERE filters before joins. This particular task is also concerned with that, adding Bloom filters' operations that approximate JOIN results and perform a secondary read to feed into joins data that is highly likely will be used in a join.

**Skills needed:** modern C++**Mentors:** Sergey Zefirov

## Suggest a Task

Do you have an idea of your own, not listed above? Do let us know in the comments below (Click 'Login' on the top of the page first)!

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
