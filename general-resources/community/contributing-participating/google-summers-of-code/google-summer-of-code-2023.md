# Google Summer of Code 2023



In 2023, MariaDB participated in the [Google Summer of Code](https://summerofcode.withgoogle.com/). The [MariaDB Foundation](https://www.mariadb.org) believes we are making a better database that remains application compatible with MySQL. We also work on making LGPL connectors (currently [C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c), [C++](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/company-and-community/contributing-participating/google-summers-of-code/mariadb-connector-c++/README.md), [ODBC](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc), [Java](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j), [Node.js](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/nodejs-connector/README.md)) and on [MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/galera/README.md), which allows you to scale your reads & writes. And we have [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/mariadb-columnstore/README.md), which is a columnar storage engine, designed to process petabytes of data with real-time response to analytical queries.

## Where to Start

Please join us on [Zulip](https://github.com/mariadb-corporation/docs-server/blob/test/kb/en/irc-chat-servers-and-zulip-instance/README.md) to mingle with the community. You should also subscribe to [maria-developers@lists.launchpad.net](https://launchpad.net/~maria-developers) (this is the main list where we discuss development).

To improve your chances of being accepted, it is a good idea to submit a pull request with a bug fix to the server.

Also see the [List of beginner friendly issues](https://jira.mariadb.org/issues/?jql=status%20%3D%20Open%20AND%20resolution%20%3D%20Unresolved%20AND%20labels%20%3D%20beginner-friendly%20ORDER%20BY%20updated%20DESC) from the MariaDB Issue Tracker.

## List of Tasks

### MariaDB Server

#### [MDEV-30610](https://jira.mariadb.org/browse/MDEV-30610) Update RocksDB to the latest upstream version

**Full-time project 350h**

Our version of RocksDB is lagging behind the current upstream and needs to be updated. This isn't a case of simply updating the submodule, there have been significant API changes. It will likely require porting the latest MyRocks code over to the MariaDB storage API.

**Skills needed**: Understanding of C/C++ development. Preferably some experience with the MariaDB or MySQL codebase (but not essential).**Mentor:** Andrew Hutchings

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

#### [GH-457](https://github.com/MariaDB/mariadb-docker/issues/457#issue-1360064494) MariaDB ColumnStore in Docker Official OCI Image

**Part-time project 175h / Full-time project 350h - depending on scope**

MariaDB ships with ColumnStore as a storage engine. However the architecture of ColumnStore is not like a traditional storage engine. Instead it relies on multiple database nodes working in unison. This means that starting up a ColumnStore enabled MariaDB service is not a trivial endeavour. This project seeks to create the necessary tooling around starting MariaDB with ColumnStore inside a OCI containers. You will be writing Dockerfiles, configuration files as well as bash scripts to achieve this.

The challenge of this project lies in:

1. Limited documentation around ColumnStore. There will be some time spent on the discovery process.
2. Formulating a clear plan to facilitate:
3. Starting MariaDB with ColumnStore
4. Upgrading MariaDB with ColumnStore on a version upgrade
5. Creating health checks to validate the health of the ColumnStore service nodes
6. Setting configuration variables via environment switches where appropriate
7. Declaratively (likely docker-compose yml file) state the system's architecture.
8. Documenting the necessary steps to deployment
9. Producing a blog of its operation
10. Optionally enable deployment via Kubernetes
11. Implementing the plan and creating a CI/CD pipeline for testing.

**Skills needed**: Ability to develop durable bash scripts, understanding of container runtime and ability to confirm to container best practices. Able to incrementally develop and test functionality.**Mentors**: Daniel Black (primary - containers) / Andrew Hutchings (secondary - ColumnStore)

#### [MDEV-6166](https://jira.mariadb.org/browse/MDEV-6166) LOAD DATA INFILE - store all warnings

**Part-time project 175h**

The main focus of this project is around developer / sysadmin experience. We want to improve the quality of life of those using MariaDB. Migrating large datasets is one of these challenges. As is described in the MDEV, a simple limitation related to LOAD DATA INFILE can severely hamper developer productivity.\
A related problem is discussed in [MDEV-13046](https://jira.mariadb.org/browse/MDEV-13046).

The goal of this project is to come up with a solution for storing warnings during LOAD DATA INFILE. This will require modifying the existing server codebase to create an SQL interface for processing the generated warnings.

Challenges:

* LOAD DATA INFILE can process large datasets. That means that the server must not just store all warnings in memory. You will need to make use of already existing mechanisms (creating temporary tables) so one can spill to disk.

**Skills needed**: Understanding of C++ development.**Mentors**: Anel Husakovic (primary) / Daniel Black (secondary)

### Buildbot (CI/CD)

#### [MDBF-320](https://jira.mariadb.org/browse/MDBF-320) Better Grid view for buildbot.mariadb.org (Python / Javascript / Web Dev

**Full-time project 350h**

Our CI/CD infrastructure uses a recent version of Buildbot. The GRID view plugin that comes with Buildbot is not adequate for our needs. In this project, you will discuss with your mentor as well as other MariaDB developers on how to best improve the User Experience of Buildbot's grid view for what MariaDB Developers needs to accomplish.

**Skills needed: Understanding of web-dev technologies like Angular, React, and Javascript related libraries. Python may also be required.Mentor**: Vlad Bogolin

### MariaDB Columnstore

MariaDB Columnstore is a columnar engine for MariaDB Server for OLAP workload. MCS is also a distributed multithreaded application written in C++. C++20 is currently used for development. There is a number of interesting MCS projects to be part of in both research and production programming areas.

#### JIT compiled SQL expressions

**Part-time project 175h / Full-time project 350h - depending on scope**

MCS uses interpreted execution to calculate SQL expressions results. Here is an example of a SQL expression 'table1.col1 + FLOOR(table2.col1)'. Given that table1.col1 is DECIMAL and table2.col1 is DOUBLE there is a number of conditions that drives the calculation of this relatively simple example in runtime. Given that SQL types and expression tree are known before the query begins it is possible to replace interpretation with JIT to produce specialized compiled bytecode that is:

1. small
2. has no or almost no branches
3. optimized for the specific platform it is run at

This is a research mostly project which goal is to produce a set of microbenchmarks that:

1. leverages any JIT compiler available, e.g. LLVM, MIR
2. demonstrates a negative and positive effects of using JIT

**Skills needed**:

1. C++
2. at least basic compilers internals knowledge

**Mentor**: Roman Nozdrin

#### Parquet support in cpimport

**Full-time project 350h**

cpimport in MCS is a standalone tool that does bulk ingestion outside SQL interface. It takes a source data as an input and puts it into MCS cluster. This put is an atomic operation that supports rollback. The sources can either local files or files on S3.\
The only format cpimport now reads is CSV with custom:

1. delimiters
2. quotation signs
3. NULL symbol

The goal of this project is to either teach cpimport to support parquet format as input format or introduce a modular framework to add input formats.\
This project is mostly about reading/writing production code where the challenges are:

1. to learn a codebase
2. produce a feature
3. support the feature with unit and integration tests using existing frameworks

cpimport consist of:

1. a buffer where parsed data lines goes in a form of low-level representation of SQL datatypes
2. a set of parser threads that populates the buffer
3. a set of writer threads that takes values that makes a single SQL record and puts them into the corresponding files

Parser threads now has a fixed Delimiter Separated Values parser that can be parametrized only with:

1. escape character
2. 'enclosed by' characters

The suggested approach is to replace this DSV parser with a modular one that understands how to read popular formats, e.g. parquet, Arrow, Avro, JSON

**Skills needed**:

1. C++
2. production development tooling like git, Cmake

**Mentor**: Gagan Goel

#### SIMD for SQL expressions

**Part-time project 175h / Full-time project 350h - depending on scope**

MCS uses scalar processing to calculate SQL expressions results. The expressions can be in projection or filtering part of a SQL query. Here is an example of a SQL expression 'table1.col1 + FLOOR(table2.col1)'. In most cases scalar processing can be replaced with a vectorized execution that reduces a number of cycles to render the result of an expression. The challenge of this project is that in-memory representation ca be both vertical and horizontal.

This is a research mostly project which goal is to produce a set of microbenchmarks that:

1. unveils limitations or problems applying vectorization for expressions
2. compares performance for cases:
3. vectorized execution with vertical data
4. vectorized execution with horizontal data
5. scalar execution with horizontal data

**Skills needed**:

1. C++
2. ASM knowledge to manage with low-level part of this project

**Mentor**: Andrey Piskunov

#### Fuzzing infrastructure for Columnstore engine.

**Full-time project 350h - depending on scope**

Fuzzing is a well-known technique for finding various types of bugs.\
This task is to integrate libFuzzer, sanitizers (ASan, TSan, UBSan) and MCS Columnstore into one fuzzing pipeline and create a fuzzing infrastructure.\
This task requires:

1. Add support to the Columnstore for building with sanitizers (ASan, TSan, UBSan)
2. Write a code which integrates C++ MariaDB Connectors and libFuzzer.
3. Prepare a valid corpus with SQL scripts suitable for Columnstore.
4. Create a fuzzing infrastructure.

Skills needed:

1. Basic knowledge how to work with C++ build tools (CMake, clang, ld, rtld).
2. Basic C++.

**Mentor**: Denis Khalikov

## Suggest a Task

Do you have an idea of your own, not listed above? Do let us know!

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
