# Google Summer of Code 2022

In 2022, we again participated in the [Google Summer of Code](https://summerofcode.withgoogle.com/). The [MariaDB Foundation](https://www.mariadb.org) believes we are making a better database that remains application compatible with MySQL. We also work on making LGPL connectors (currently [C](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-c), [C++](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/company-and-community/contributing-participating/google-summers-of-code/mariadb-connector-c++/README.md), [ODBC](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-odbc), [Java](https://app.gitbook.com/s/CjGYMsT2MVP4nd3IyW2L/mariadb-connector-j), [Node.js](https://github.com/mariadb-corporation/docs-server/blob/test/en/nodejs-connector/README.md)) and on [MariaDB Galera Cluster](https://github.com/mariadb-corporation/docs-server/blob/test/en/galera/README.md), which allows you to scale your reads & writes. And we have [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-server/blob/test/en/mariadb-columnstore/README.md), which is a columnar storage engine, designed to process petabytes of data with real-time response to analytical queries.

## Where to Start

Please join us on [Zulip](https://github.com/mariadb-corporation/docs-server/blob/test/en/irc-chat-servers-and-zulip-instance/README.md) to mingle with the community. You should also subscribe to [maria-developers@lists.launchpad.net](https://launchpad.net/~maria-developers) (this is the main list where we discuss development).

To improve your chances of being accepted, it is a good idea to submit a pull request with a bug fix to the server.

Also see the [List of beginner friendly issues](https://jira.mariadb.org/issues/?jql=status%20%3D%20Open%20AND%20resolution%20%3D%20Unresolved%20AND%20labels%20%3D%20beginner-friendly%20ORDER%20BY%20updated%20DESC) from the MariaDB Issue Tracker.

## List of Tasks

### MariaDB Server

* [MDEV-21978](https://jira.mariadb.org/browse/MDEV-21978) make my\_vsnprintf to use gcc-compatible format extensions (Part-time project - 175h)\
  MariaDB has its own implementation of most standard C libraries. This is to ensure compatibility across different platforms. Over time this library has evolved and is currently not behaving exactly like POSIX standard library. Thus we want to attain the principle of "least-surprise" with this library. Everything that is supported by standard printf functions should function the same with MariaDB's compatibility library extension.
  * Skills needed: C/C++. Project difficulty: easy\
    Mentor Sergei Golubchik
* [MDEV-19160](https://jira.mariadb.org/browse/MDEV-19160) JSON\_DETAILED output unnecessarily verbose. (Part Time project - 175h)\
  As is explained in the MDEV in detail, we want to improve JSON\_DETAILED function to better suit our development and debugging purposes. This project will aim to clean up the function's implementation as well as introduce test cases as well as potential "nice-to-have" features to make developer's lives easier.
  * Skills needed: C/C++, understand JSON, OOP. Project difficulty: easy Mentor: Vicențiu Ciorbaru / Sergei Petrunia
* [MDEV-18827](https://jira.mariadb.org/browse/MDEV-18827) Create utility to parse frm files and print their DDL (Full-time project - potential part-time (175 - 350h, depending on scope))\
  FRM files are what MariaDB uses to store metadata about tables. These files can be used to generate DDL statements (CREATE TABLE ...). We are lacking a utility to parse these files which could in turn make DBAs lives easier. The task of this project is to have this utility implemented, making use of MariaDB's FRM parsing logic. You may have to carry out some refactoring to extract the parsing code into a reusable library, once for MariaDB Server, once for the FRM parsing tool.
  * Skills needed: C/C++, understanding libraries and APIs. Project difficulty: medium to hard, depending on time allocated\
    Mentor Vicențiu Ciorbaru / Sergei Golubchik / Monty Widenius
* [MDEV-17467](https://jira.mariadb.org/browse/MDEV-17467) Add linear regression functions (Full-time project - 350h)\
  This project consists of implementing dedicated regression functions within MariaDB. The specification of each function will be decided during the project, based on what other competing databases are offering. We will choose an implementation that best matches user expectations. It is the student's job to perform research into at least one other database and come up with exact semantics for each one of the functions in the MDEV.
  * Skills needed: C/C++, understanding of regression functions and mathematics, APIs, OOP. Project difficulty: medium\
    Mentor Vicențiu Ciorbaru
* [MDEV-23251](https://jira.mariadb.org/browse/MDEV-23251) Client compatible delimiter for mysqltest (Full-time project - potential part-time (175 - 350h, depending on scope))\
  We have a DELIMITER command that has a different syntax in client and mysqltest\
  mysqltest needs an additional (previous) delimiter in the end of the DELIMITER expression,\
  which confuses and makes it hard to copy and paste simple scripts with stored procedures\
  from one to another.\
  We would like to have a new command (--delimiter=client|mysqltest) with current behavior as default.
  * Expected outcomes: You will learn the C command line tools development minors. You'll get familiar with a part of MariaDB server infrastructure -- testing framework, which is written in C and Perl.
  * Skills required: good C knowledge; ability to use console terminal, ability to build from console. Project difficulty: easy\
    Mentor Nikita Malyavin
* [MDEV-25774](https://jira.mariadb.org/browse/MDEV-25774) Improve build speed of the server code base (Full-time project - 350h)\
  We have already learned that precompiling the headers\
  improves the build speed five times, however, the\
  standard CMake solution doesn't fit for our comfort of\
  development: CMake PCH generates one "header of headers"\
  and pre-includes it into the each of compilation units.\
  This makes everything that wasn't included by the unit\
  itself be available across the precompiled set.\
  There are the alternative ways of unit precompiling:\
  clang modules and gcc .gch files. We want to prefer\
  it on the per-comiler header.
  * Expected outcomes:\
    You will make a strong practical impact of a high need\
    and show off your mix of analysis and programming skills.
  * Skills required: good C knowledge, some CMake knowledge; ability to use console terminal, ability to build from console. Project difficulty: medium\
    Mentor Nikita Malyavin
* [MDEV-12130](https://jira.mariadb.org/browse/MDEV-12130) Improve mysqltest language(Full-time project - 350h)\
  mysqltest has a lot of historical problems: ad hoc parser, weird limitations commands added as needed with no view over the total language structure, etc. The purpose of this work would be improvement of the language.
  * Expected outcomes : Rewrite mysqltest interpreter using either a real parser generator, e.g bison, or cleanly hand-written parser, e. recursive descent, that can be easily extended with new functionality. Added missing control structures, for example "else" for an existing "if". Simple expression evaluations without contacting server, i.e math and string comparisons. Added functionality for minimal string manipulation ,e.g substr function.
  * Skills required: good C/C++ knowledge, interest in parsers/interpreter. Project difficulty: medium\
    Mentor Vladislav Vaintroub
* [MDEV-26182](https://jira.mariadb.org/browse/MDEV-26182) Create a function to check for JSON intersection (Part-time project - 175h)\
  This project aims at implementing JSON\_INTERSECT() function between two JSON objects or two JSON arrays. If the two documents are json arrays then we want to return all the common elements between the two arrays. And in case of objects, we want to return all common key value pairs.
  * Skills required: C/C++, OOP, basic understanding of JSON. Project difficulty: easy\
    Mentor Rucha Deodhar, Oleksandr Byelkin

### ColumnStore

* [MCOL-4995](https://jira.mariadb.org/browse/MCOL-4995) Research/implement basic vectorized filtering for ARM platforms (Full-time project - 350h)\
  AS of 6.2.2 Columnstore(MCS) supports vectorization on x86\_64 platforms only.\
  The goal of the project is to implement a vectorized low-level filtering for ARM platforms using 128bit ARM NEON extention(SVE is optional). Low-level filtering in the context is the simple predicate WHERE filters, e.g. WHERE c1 = 5 AND c2 in (10, 25). Please see the corresponding Jira issue for details.
  * Skills needed: C/C++, understand low-level platform specifics. Project difficulty: medium\
    Mentor Roman Nozdrin
* [MCOL-4994](https://jira.mariadb.org/browse/MCOL-4994) Build/run Columnstore on MacOS (Part-time project - 175h)\
  As of Columnstore(MCS) 6.2.2 there is no way to compile/use the MCS engine on MacOS. The goal of this project is to be able to boostrap MariaDB + basic(maybe rudimentary) MCS on MacOS. There are number of known issues that prevents MCS compilation on MacOS: a number of offending preprocessor macroses/definitions specific for Linux x86\_64 combination; MacOS doesn't provide syslog used by MCS as the only log messages sink. Please see the corresponding Jira issue for details.
  * Skills needed: C/C++, MacOS specifics. Project difficulty: easy\
    Mentor Roman Nozdrin
* [MCOL-785](https://jira.mariadb.org/browse/MCOL-785) Implement DISTRIBUTED JSON functions (Full-time project - 350h)\
  As of 6.2.2 Columnstore there are two query execution modes: relatively slow but compatible Table mode and fast Select Handler mode. Table mode execution supports all JSON\_\* functions and SH mode doesn't support any. We want to add support for JSON\_\* functions family in SH query execution mode. Please see the corresponding Jira issue for details.
  * Skills needed: C/C++, JSON format. Project difficulty: easy\
    Mentor Roman Nozdrin

### Buildbot (CI/CD)

* [MDBF-320](https://jira.mariadb.org/browse/MDBF-320) Better Grid view for buildbot.mariadb.org (Python / Javascript / Web Dev ( Full-time project 350h)\
  Our CI/CD infrastructure uses a recent version of Buildbot. The GRID view plugin that comes with Buildbot is not adequate for our needs. In this project, you will discuss with your mentor as well as other MariaDB developers on how to best improve the User Experience of Buildbot's grid view for what MariaDB Developers needs to accomplish.
  * Skills needed: Understanding of web-dev technologies like Angular, React, and Javascript related libraries. Python may also be required.\
    Mentor Vlad Bogolin / Andreia Hendea

## Suggest a Task

Do you have an idea of your own, not listed above? Do let us know!

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
