# Reporting Software Bugs

For reporting documentation bugs specifically, see [Reporting Documentation Bugs](../../../about/readme/reporting-documentation-bugs.md).

MariaDB's bug and feature tracker is found at [jira.mariadb.org](https://jira.mariadb.org).

This page contains general guidelines for the community for reporting bugs and feature requests in MariaDB products. If you want to discuss a problem or a new feature with other MariaDB developers, you can find the email lists and forums here.

## Known Issues

First, check that the bug or feature request isn't already filed in the [MariaDB bugs database](https://jira.mariadb.org/browse/MDEV).

For the MariaDB issue database, use JIRA search to check if a report you are going to submit already exists. You are not expected to be a JIRA search guru, but please at least make some effort.

* Choose `Issues => Search for issues`;
* If the form opens for you with a long blank line at top, press `Basic` on the right to switch to a simpler mode;
* In the `Project` field, choose the related project, (`MDEV` for generic MariaDB server and clients);
* In the `Contains text` text field, enter the most significant key words from your future report;
* Press `Enter` or the magnifying glass icon to search.

If you see issue reports which are already closed, pay attention to the 'Fix version/s' field -- it is possible that they were addressed in the _upcoming_ release. If they are said to be addressed in the release that you are currently using or earlier, you can ignore them and file a new one (although please mention in your report that you found them, it might be useful).

If you find an open issue report, please vote/add a comment that the issue also interests you along with any additional information you have that may help us to find and address the issue.

If the issue is not in the MariaDB issue database yet, then it's time to file a report. If you're filing a report about an issue that's already in the [MySQL issue database](https://bugs.mysql.com/), please indicate so at the start of the report. Filing issue reports from MySQL in the MariaDB issue database makes sense, because:

* It shows the MariaDB team that there is interest in having this issue addressed in MariaDB.
* It allows work to start on addressing the issue in MariaDB - assigning versions, assigning MariaDB developers to the issue, etc.

## Reporting an Issue

Bugs and feature requests are reported to the [MariaDB issue tracker](https://jira.mariadb.org/browse/MDEV).

### JIRA Privacy

Please note that our JIRA entries are public, and JIRA is very good at keeping a record of everything that has been done. What this means is that if you ever include confidential information in the description there will be a log containing it, even after you've deleted it. The only way to get rid of it will be removing the JIRA entry completely.

Attachments in JIRA are also public.

Access to a comment can be restricted to a certain group (e.g. Developers only), but the existing groups are rather wide, so you should not rely on it either.

If you have private information -- SQL fragments, logs, database dumps, etc. -- that you are willing to share with MariaDB team, but not with the entire world, put it into a file, compress if necessary, upload to the [mariadb-ftp-server](../../contributing-participating/mariadb-public-ftp-server.md), and just mention it in the JIRA description. This way only the MariaDB team will have access to it.

### Reporting Security Vulnerabilities

As explained above, all JIRA issues are public. If you believe you have found a security vulnerability, send an email to [security@mariadb.org](mailto:security@mariadb.org) for, please, do not use JIRA for that. We will enter it in JIRA ourselves, following the [responsible disclosure](https://en.wikipedia.org/wiki/Responsible_disclosure) practices.

### Contents of a Good Bug Report

Below is the information we need to be able to fix bugs. The more information we get and the easier we can repeat the bug, the faster it will be fixed.

A good bug report consists of:

1. The environment (Operating system, hardware and MariaDB version) where the bug happened.
2. Any related errors or warnings from the server error log file. Normally it is `hostname.err` file in your database directory, but it can be different depending on the distribution and version; if you cannot find it, run `SELECT @@log_error` on the running server. If either the variable or the file it points at is empty, the error log most likely goes to your system log. If this is systemd you can get the last 50 lines of the MariaDB log with `journalctl -n 50 -u mariadb.service`. If possible, attach the full unabridged error log at least from the last server restart and till the end of the log.,
3. If the problem is related to MariaDB updates, or otherwise changing the version of the server, recovery from a previous crash, and such, then include the previous versions used, and the error log from previous server sessions.
4. The content of your my.cnf file or alternatively the output from `mariadbd --print-defaults` or `SHOW VARIABLES`.
5. Any background information you can provide ([stack trace](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options#stack-trace), tables, table definitions (show-create-table SHOW CREATE TABLE {tablename}), data dumps, query logs).
6. If the bug is about server producing wrong query results: the actual result (what you are getting), the expected result (what you think should be produced instead), and, unless it is obvious, the reason why you think the current result is wrong.
7. If the bug about a performance problem, e.g. a certain query is slower on one version than on another, output of `EXPLAIN EXTENDED <query>` on both servers. If its a `SELECT` query use [analyze-format-json ANALYZE FORMAT=JSON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/analyze-format-json).
8. A test case or some other way to repeat the bug. This should preferably be in plain SQL or in mysqltest format. See mysqltest/README for information about this.
9. If it's impossible to do a test case, then providing us with a [backtrace information](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/product-development/mariadb-fault-finding/how-to-produce-a-full-stack-trace-for-mariadbd#getting-backtraces-with-gdb-on-linux) would be of great help.

### JIRA Fields

The section below describes which JIRA fields need to be populated while filing reports, and what should be put there.\
Apart from what's mentioned below, you don't have to fill or change any fields while creating a new bug report.

#### Project

If you are filing a report for MariaDB server, client programs, or MariaDB Galera cluster, the target project is `MDEV`. Connectors and MaxScale have separate projects with corresponding names. If you choose a wrong project, bug processing can be delayed, but there is no reason to panic -- we'll correct it. If you inform us about the mistake, we'll change it faster.

Some project names include:

* CONC - MariaDB Connector/C
* CONCPP - MariaDB Connector/C++
* CONJ - MariaDB Connector/J
* CONJS - MariaDB Connector/node.js
* CONPY - MariaDB Connector/Python
* MCOL - ColumnStore
* MDBF - MariaDB Foundation Development (anything related to the [mariadb.org domain](https://mariadb.org))
* MDEV - MariaDB server, client programs, or MariaDB Galera Cluster
* MXS - MaxScale
* ODBC - MariaDB Connector/ODBC
* R2DBC - MariaDB Connector/R2DBC

#### Type

Feature requests are not the same as bug reports. Specify a `New feature` type for feature requests in [Jira](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/product-development/server-development/tools/jira), and a `Bug` type for bug reports. Like with the project field, choosing a wrong type will put the request to the wrong queue and can delay its processing, but eventually it will be noticed and amended.

See also [plans for next release](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/product-development/server-development/tools/jira) for things that we are considering to have in the next MariaDB release.

#### Summary

Please make sure the summary line is informative and distinctive. It should always be easy to recognize your report among other similar ones, otherwise a reasonable question arises -- why are they not duplicates?

Examples:

* good summary: Server crash with insert statement containing DEFAULT into view
* not a good summary: mariadbd crash

Generally, we try not to change the original summary without a good reason to do it, so that you can always recognize your own reports easily.

#### Priority

We do not have separate Severity/Priority fields in JIRA, so this Priority field serves a double purpose. For original reports, it indicates the importance of the problem from the reporter's point of view. The default is 'Major'; there are two lower and two higher values. Please set the value accurately. While we do take it into account during initial processing, increasing the value above reasonable won't do any good, the only effect will be the waste of time while somebody will be trying to understand why a trivial problem got such a high priority. After that, the value will be changed, and the report will be processed in its due time anyway.

#### Affected Versions

Put everything you know about which versions are affected. There are both major versions (10.6, 10.5 etc.) and minor versions (10.5.9, 10.4.12, etc.) available for choosing. Please always specify there the exact version(s) (X.Y.Z) which you are working with, and where you experience the problem.

Additionally, If you know the exact version where the problem appeared, please put it as well. If the problem has been present, as far as you know, in all previous releases, you can also put there the major version, e.g. 10.0. Alternatively, you can mention all of it in the description or comments.

Please also note in the description or comments which versions you know as _not_ affected. This information will help to shorten further processing.

#### Environment

Put here environment-related information that might be important for reproducing or analyzing the problem: operating system, hardware, related 3rd-party applications, compilers, etc.

#### Description

The most important part of the description are steps to reproduce the problem. See more details about bug report contents above in the section [Contents of a good bug report](reporting-bugs.md#contents-of-a-good-bug-report).

If in the process of reproducing, you executed some SQL, don't describe it in words such as "I created a table with text columns and date columns and populated it with some rows" -- instead, whenever possible, put the exact SQL queries that you ran. The same goes for problems that you encountered: instead of saying "it did not work, the query failed, I got an error", always paste the exact output that you received.

_Use {noformat}...{noformat} and {code}...{code} blocks for code and console output in the description._

#### Attachments

If you have SQL code, a database dump, a log etc. of a reasonable size, attach them to the report (archive them first if necessary). If they are too big, you can upload them to ftp.askmonty.org/private. It is always a good idea to attach your cnf file(s), unless it is absolutely clear from the nature of the report that configuration is irrelevant.

#### Links

If you found or filed a bug report either in MariaDB or MySQL or Percona bug base which you think is related to yours, you can put them in the `Links` section; same for any external links to 3rd-party resources which you find important to mention. Alternatively, you can just mention them in the description or comments.

#### Tags

You don't have to set any tags, but if you want to use any for your convenience, feel free to do so. However, please don't put too generic values -- for example, the tag `mariadb` is meaningless, because everything there is `mariadb`. Don't be surprised if some tags are removed later during report processing.

### Bugs that also Affect MySQL or Percona

Our normal practice is to report a bug upstream if it's applicable to their version. While we can do it on your behalf, it is always better if you do it yourself -- it will be easier for you to track it further.

If the bug affects MySQL, it should also be reported at [MySQL bugs database](https://bugs.mysql.com).\
If the bug affects Percona server and not MySQL, it should go to [Percona Launchpad](https://bugs.launchpad.net/percona-server).

## Collecting Additional Information for a Bug Report

#### Getting a Stack Trace with Details

See the article [How to produce a stack trace from a core file](/broken/pages/yt4NDbw3wL7QsDjQtA0H).

#### Extracting a Portion of a Binary Log

See the article [here](extracting-entries-from-the-binary-log.md).

## Getting Help with your Servers

If you require personalized assistance, want to ensure that the bug is fixed with high priority, or want someone to login to your server to find out what's wrong, you can always purchase a [Support](https://www.mariadb.com/products/mysql-support) contract from MariaDB plc or use their consulting services.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
