# Google Summer of Code 2024

In 2024, MariaDB again participated in the [Google Summer of Code](https://summerofcode.withgoogle.com/). We believe we are making a better database that remains application compatible with MySQL. We also work on making LGPL connectors (currently [C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c), [C++](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/company-and-community/contributing-participating/google-summers-of-code/mariadb-connector-c++/README.md), [ODBC](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc), [Java](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j), [Node.js](https://github.com/mariadb-corporation/docs-server/blob/test/en/nodejs-connector/README.md)) and on [MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/en/galera/README.md), which allows you to scale your reads & writes. And we have [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-server/blob/test/en/mariadb-columnstore/README.md), which is a columnar storage engine, designed to process petabytes of data with real-time response to analytical queries.

## Where to Start

Please join us on [Zulip](https://github.com/mariadb-corporation/docs-server/blob/test/en/irc-chat-servers-and-zulip-instance/README.md) to mingle with the community. You should also subscribe to the [developers mailing list](https://lists.mariadb.org/postorius/lists/developers.lists.mariadb.org) (this is the main list where we discuss development - there are also [other mailing lists](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/contributing-participating/google-summers-of-code/broken-reference/README.md)).

To improve your chances of being accepted, it is a good idea to submit a pull request with a bug fix to the server.

Also see the [List of beginner friendly issues](https://jira.mariadb.org/issues/?jql=status%20%3D%20Open%20AND%20resolution%20%3D%20Unresolved%20AND%20labels%20%3D%20beginner-friendly%20ORDER%20BY%20updated%20DESC) from the MariaDB Issue Tracker.

## List of Tasks

### MariaDB Server

#### Implement IVFFlat indexing strategy for MariaDB Vector and evaluate performance

**Part-time (175h) or full-time project (350h) - depending on scope**\
MariaDB Vector is coming to MariaDB Server to serve AI Workloads. The current indexing strategy will use HNSW, but IVFFlat is a possible alternative that costs fewer resources to create. Having it as an option is desirable.

#### [MDEV-17398](https://jira.mariadb.org/browse/MDEV-17398) Spatial (GIS) functions in MariaDB

**Part-time (175h) or full-time project (350h) - depending on scope**

Our GIS functionality is limited compared to other DBMSes. Given that MariaDB looks to facilitate migration from MySQL, we should be on par. We have a list of functions that are missing in MariaDB compared to MySQL, as described in [function-differences-between-mariadb-10-10-and-mysql-8-0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/function-differences-between-mariadb-and-mysql/function-differences-between-mariadb-and-mysql-unmaintained-series/function-differences-between-mariadb-10-10-and-mysql-8-0).\
Our goal is to have as many of these functions available within MariaDB. Some of the functionality can be ported from MySQL, while others might require implementation from scratch.

**Skills needed**: Understanding of C++ development. Ability to navigate a large codebase (with help from mentor).**Mentors:** Anel Husakovic (primary) / Vicențiu Ciorbaru (secondary)

#### [MDEV-16482](https://jira.mariadb.org/browse/MDEV-16482) MariaDB Oracle mode misses Synonyms

**Full-time project 350h**

Synonyms are an important feature, particularly as it helps smooth migration from other databases. While the initial project scope seems straightforward, there are a number of aspects that must be considered:

1. Grammar extension
2. Where will the synonyms definitions be stored?
3. How do synonyms map to the underlying privilege system? Who can create a synonym? Who can access a synonym?
4. Do we enforce the underlying object to exists before creating a synonym? What if the underlying object gets dropped?
5. What kind of error messages do we present to the user in various corner cases?
6. How do synonyms interact with replication (row based vs statement based)
7. How do synonyms interact with views (and views execution)
8. How to present synonyms to users (as part of INFORMATION\_SCHEMA for instance?)
9. Performance considerations for multiple connections to the database.

**Skills needed:** Understanding of C++ development. Able to write and discuss various tradeoffs such that we achieve a feature set that makes sense given the database's priorities.**Mentors:** Vicențiu Ciorbaru (primary) / Michael Widenius (secondary)

#### [MDEV-30645](https://jira.mariadb.org/browse/MDEV-30645) CREATE TRIGGER FOR { STARTUP | SHUTDOWN }

**Full-time project 350h**

Support generalized triggers like

```
CREATE TRIGGER ... AFTER STARTUP ...
CREATE TRIGGER ... BEFORE SHUTDOWN ...
CREATE TRIGGER ... ON SCHEDULE ...
```

the latter being a synonym for `CREATE EVENT`.

* should STARTUP/SHUTDOWN triggers run exclusively? that is, STARTUP trigger is run before any connection is allowed or in parallel with them? Same for SHUTDOWN.

**Skills needed:** Understanding of C++ development. Able to write and discuss various tradeoffs such that we achieve a feature set that makes sense given the database's priorities.**Mentors:** Sergei Golubchik

#### [MDEV-21978](https://jira.mariadb.org/browse/MDEV-21978) make my\_vsnprintf to use gcc-compatible format extensions

**Part-time project 175h**

`my_vsnprintf()` is used internally in the server as a portable `printf` replacement. And it's also exported to plugins as a service.

It supports a subset of `printf` formats and three extensions:

* `%`s`means that a string should be quoted like an`identifier\`
* `%b` means that it's a binary string, not zero-terminated; printing won't stop at \0, so one should always specify the field width (like %.100b)
* `%M` is used in error messages and prints the integer (errno) and the corresponding strerror() for it
* `%T` takes string and print it like `%s` but if the string should be truncated puts "..." at the end

`gcc` knows `printf` formats and check whether actual arguments match the format string and issue a warning if they don't. Unfortunately there seems to be no easy way to teach `gcc` our extensions, so for now we have to disable `printf` format checks.

An better approach would be to use `gcc` compatible format extensions, like Linux kernel does. We should migrate to a different syntax for our extensions

* `%sI` to mean "print as an identifier"
* `%sB` to mean "print a binary string"
* `%uE` to mean "print an errno"
* `%sT` to put a "..." as truncation indicator

old formats can still be supported or they can be removed and in the latter case the major version of the service should be increased to signal an incompatible change.

All error messages and all usages of `my_vsnprintf` should be changed to use the new syntax. One way to do it is to disable old syntax conditionally, only in debug builds. All `gcc` `printf` format checks should be enabled.

**Skills needed:** Understanding of C development.**Mentors:** Sergei Golubchik

#### [MCOL-5688](https://jira.mariadb.org/browse/MCOL-5688) Parallel CSV read leveraging Apache Arrow

**Full-time project 350h**

cpimport is a binary that ingests data into MCS in an efficient manner reducing ingest timings significantly whilst preserving transaction isolation levels.

cpimport is relatively complex facility that reads data from local file/S3 parses it, converts and put into MCS-specific files.\
cpimport is unable to read a big-sized single CSV file from disk in parallel.\
Apache Arrow has a CSV read faciilty that can do parallel CSV read.\
The goal of the project is to replace an existing homebrew CSV parser implemented in cpimport with the one from Apache Arrow.

**Skills needed**: modern C++.**Mentors**: Leonid Fedorov

#### [MCOL-4889](https://jira.mariadb.org/browse/MCOL-4889) Manual vacuum cleaning for on-disk data empty records

**Full-time project 350h**

Here extent is a unit of group of columnar values and partition is a group of extents that stores all column values for a specific portion of a table.\
MCS has a notion of an empty value for columnar segment/token files and dictionaries. Empty values are marked with a bit in the special 1 byte auxiliary column that is created for every table.\
When DELETE removes records from a table the records are marked with empty bit in the auxiliary column. The deleted records become a wasted disk space.\
The goal of the project is to reclaim the wasted disk space either re-creating the whole partition or moving partition values.

**Skills needed**: modern C++**Mentors**: Roman Nozdrin

## Suggest a Task

Do you have an idea of your own, not listed above? Do let us know in the comments below (Click 'Login' on the top of the page first)!

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
