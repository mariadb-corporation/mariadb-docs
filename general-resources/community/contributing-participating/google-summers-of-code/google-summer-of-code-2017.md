# Google Summer of Code 2017

We participated in the [Google Summer of Code 2017](https://summerofcode.withgoogle.com/) (we have participated previously in [2016](google-summer-of-code-2016.md), [2015](google-summer-of-code-2015.md), [2014](google-summer-of-code-2014.md), and [2013](google-summer-of-code-2013.md)). The [MariaDB Foundation](https://www.mariadb.org) believes we are making a better database that remains application compatible with MySQL. We also work on making LGPL connectors (currently C, ODBC, Java) and on [MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/en/galera/README.md), which allows you to scale your reads & writes. Lately, we also have [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-server/blob/test/en/mariadb-columnstore/README.md), which is a columnar storage engine, designed to process petabytes of data with real-time response to analytical queries.

## Where to start

Please join us at `irc.freenode.net` at #maria to mingle with the community. Don't forget to subscribe to [maria-developers@lists.launchpad.net](https://launchpad.net/~maria-developers) (this is the main list where we discuss development).

A few handy tips for any interested students who are unsure which projects to choose:[Blog post from former GSoC student & mentor](https://vicentiu.ciorbaru.io/mariadb-participates-in-gsoc-2017/)

## List of tasks

The complete list of tasks suggested for GSoC 2017 is located in the [**MariaDB Jira**](https://jira.mariadb.org/issues/?jql=labels%3Dgsoc17). A subset is listed below.

### Support for GTID in mysqlbinlog

The [mysqlbinlog](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-binlog) tool needs to be updated to understand the replication feature called [Global Transaction IDs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid) (GTIDs) in MariaDB 10. The current version does not support GTIDs and the MySQL variant does not speak MariaDB 10's GTIDs.

| Details:             | Skills:                                                | Mentor: | Students Interested: |
| -------------------- | ------------------------------------------------------ | ------- | -------------------- |
| Details:             | [MDEV-4989](https://jira.mariadb.org/browse/MDEV-4989) |         |                      |
| Skills:              | C/C++                                                  |         |                      |
| Mentor:              |                                                        |         |                      |
| Students Interested: | 2                                                      |         |                      |

### Automatic provisioning of slave

The purpose of this task is to create an easy-to-use facility for setting up a new MariaDB [replication](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/contributing-participating/google-summers-of-code/broken-reference/README.md) slave.

| Details:             | Skills:                                                | Mentor: | Students Interested: |
| -------------------- | ------------------------------------------------------ | ------- | -------------------- |
| Details:             | [MDEV-7502](https://jira.mariadb.org/browse/MDEV-7502) |         |                      |
| Skills:              | C/C++                                                  |         |                      |
| Mentor:              |                                                        |         |                      |
| Students Interested: | 3                                                      |         |                      |

### GIS enhancements

[GIS](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-structure/geometry) enhancements for 10.1 that we want to work on include adding support for altitude (the third coordinate), converters (eg. ST\_GeomFromGeoJSON - ST\_AsGeoJSON, ST\_GeomFromKML - ST\_AsKML, etc.), Getting data from SHP format (shp2sql converter), as well as making sure we are fully OpenGIS compliant.

| Details:             | Skills:                                                | Mentor: | Students Interested: |
| -------------------- | ------------------------------------------------------ | ------- | -------------------- |
| Details:             | [MDEV-5813](https://jira.mariadb.org/browse/MDEV-5813) |         |                      |
| Skills:              | C/C++                                                  |         |                      |
| Mentor:              | Holyfoot                                               |         |                      |
| Students Interested: | 1                                                      |         |                      |

### mysqltest improvements

`mysqltest` is a client utility that runs tests in the [mysql-test](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-test) framework. It sends sql statements to the server, compares the results with the expected results, and uses a special small [DSL](https://en.wikipedia.org/wiki/Domain-specific_language) for loops, assignments, and so on. It's pretty old and very ad hoc with many strange limitations. It badly needs a proper parser and a consistent logical grammar.

| Details:             | Skills:                                                  | Mentor: | Students Interested: |
| -------------------- | -------------------------------------------------------- | ------- | -------------------- |
| Details:             | [MDEV-12130](https://jira.mariadb.org/browse/MDEV-12130) |         |                      |
| Skills:              | C/C++                                                    |         |                      |
| Mentor:              | Sergei Golubchik                                         |         |                      |
| Students Interested: | 3                                                        |         |                      |

### Allow multiple alternative authentication methods for the same user

Currently one can specify only one authentication method per user. It would make a lot of sense to support multiple authentication methods per user. PAM-style. For example, one may want to authenticate using unix\_socket when connecting locally, but ask for a password if connecting remotely or if unix\_socket authentication failed.

| Details:             | Skills:                                                  | Mentor: | Students Interested: |
| -------------------- | -------------------------------------------------------- | ------- | -------------------- |
| Details:             | [MDEV-11340](https://jira.mariadb.org/browse/MDEV-11340) |         |                      |
| Skills:              | C/C++                                                    |         |                      |
| Mentor:              | Sergei Golubchik                                         |         |                      |
| Students Interested: | 4                                                        |         |                      |

### connection encryption plugins

Encrypting the client-server communications is closely related to authentication. Normally SSL is used for the on-the-wire encryption, and SSL can be used to authenticate the client too. GSSAPI can be used for authentication, and it has support for on-the-wire encryption. This task is about making on-the-wire encryption pluggable.

| Details:             | Skills:                                                | Mentor: | Students Interested: |
| -------------------- | ------------------------------------------------------ | ------- | -------------------- |
| Details:             | [MDEV-9090](https://jira.mariadb.org/browse/MDEV-9090) |         |                      |
| Skills:              | C/C++                                                  |         |                      |
| Mentor:              | Sergei Golubchik                                       |         |                      |
| Students Interested: | 2                                                      |         |                      |

### OSS-Fuzz configuration for MariaDB

This would involve randomizing a bunch of queries (RQG based?), configurations and replication setups to search for segfaults, race conditions and perhaps invalid results.

| Details:             | Skills:                                                  | Mentor: | Students Interested: |
| -------------------- | -------------------------------------------------------- | ------- | -------------------- |
| Details:             | [MDEV-12178](https://jira.mariadb.org/browse/MDEV-12178) |         |                      |
| Skills:              | C, SQL                                                   |         |                      |
| Mentor:              | Daniel Black                                             |         |                      |
| Students Interested: | 1                                                        |         |                      |

### NUMA for MariaDB

This would involve organising a bunch of memory and threads to run on the same NUMA node. Attention to detail to ensure no additional race conditions get added in the process. A good understanding of systems programming would be useful. Ability to implement WIndows NUMA support at the same time as Linux NUMA support would be advantageous.

| Details:             | Skills:                                                                                  | Mentor: | Students Interested: |
| -------------------- | ---------------------------------------------------------------------------------------- | ------- | -------------------- |
| Details:             | [MDEV-12213](https://jira.mariadb.org/browse/MDEV-12213)                                 |         |                      |
| Skills:              | C, locking and threads, Windows system programming and Innodb internals would be a plus. |         |                      |
| Mentor:              | Daniel Black                                                                             |         |                      |
| Students Interested: | 1                                                                                        |         |                      |

### Cassandra Storage Engine V2

Current Cassandra Storage Engine was developed against Cassandra 1.1 and it uses Thrift API to communicate with Cassandra.\
However, starting from Cassandra 1.2, the preferred way to access Cassandra database is use CQL (Cassandra Query Language) and DataStax C++ Driver ([cpp-driver](https://github.com/datastax/cpp-driver)). Thrift-based access is deprecated and places heavy constraints on the schema.

This task is about re-implementing Cassandra Storage Engine using DataStax C++ Driver and CQL.

| Details:             | Skills:                                                  | Mentor: | Students Interested: |
| -------------------- | -------------------------------------------------------- | ------- | -------------------- |
| Details:             | [MDEV-12296](https://jira.mariadb.org/browse/MDEV-12296) |         |                      |
| Skills:              | C/C++                                                    |         |                      |
| Mentor:              | Sergei Petrunia                                          |         |                      |
| Students Interested: | 1                                                        |         |                      |

### ColumnStore: Add proper NULL support

At the moment NULL is just the maximum integer for a column (or empty string\
for VARCHAR/CHAR). We need a mechanism to store NULLs separately to give us\
full type ranges.

### ColumnStore: Add full support for DECIMAL

Right now it is cast to double which is not great for obvious reasons. It will\
mean modifying a lot of ColumnStore's version of MariaDB's function\
implementations and allowing column files to store more than 8 bytes per\
field.

| Details:             | Skills:                                              | Mentor: | Students Interested: |
| -------------------- | ---------------------------------------------------- | ------- | -------------------- |
| Details:             | [MCOL-641](https://jira.mariadb.org/browse/MCOL-641) |         |                      |
| Skills:              | C/C++                                                |         |                      |
| Mentor:              | Andrew Hutchings                                     |         |                      |
| Students Interested: | 1                                                    |         |                      |

### ColumnStore: Full UTF8 support.

This includes collations and anything that works on the length of the string.

## Suggest a task

Do you have an idea of your own, not listed above or in Jira? Do let us know!

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
