# MariaDB ColumnStore 1.0.11 GA Release Notes

**Release date:** 18th August 2017

[MariaDB ColumnStore 1.0.11](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) is a maintenance GA release of MariaDB ColumnStore. This release of MariaDB ColumnStore provides improvements over the previous 1.0.10 GA release.

MariaDB ColumnStore 1.0.11 is a [_**GA**_](../../../community-server/about/release-criteria.md) release.

For an overview of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) see [MariaDB ColumnStore Architectural Overview](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview)

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Notable changes

* [MCOL-792](https://jira.mariadb.org/browse/MCOL-792) - Debian 9 is now a supported platform.
* [MCOL-868](https://jira.mariadb.org/browse/MCOL-868) - The base MariaDB server version is now [10.1.26](../../../community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10126-release-notes.md) which include several maintenance and security fixes.

## Bugs and issues fixed

* [MCOL-400](https://jira.mariadb.org/browse/MCOL-400) - On a 2PM combo stack with query stats enabled, one of the PMs returned an error when queries is executed
* [MCOL-515](https://jira.mariadb.org/browse/MCOL-515) - GROUP BY in a cross engine subquery generates bad results
* [MCOL-744](https://jira.mariadb.org/browse/MCOL-744) - primproc crashes sometimes in test001 regression test runs during drop table
* [MCOL-792](https://jira.mariadb.org/browse/MCOL-792) - support debian 9
* [MCOL-812](https://jira.mariadb.org/browse/MCOL-812) - Cross engine join and a filter where the string contains a quote character
* [MCOL-830](https://jira.mariadb.org/browse/MCOL-830) - CrossEngineSupport can not retrieve multi byte fields normally
* [MCOL-835](https://jira.mariadb.org/browse/MCOL-835) - Killing MariaDB connections can crash ExeMgr
* [MCOL-845](https://jira.mariadb.org/browse/MCOL-845) - postConfigure creates a list of dbroots and assigns them device nodes, it starts at 'g' and increments, but it skips 'k'. system fails to start
* [MCOL-849](https://jira.mariadb.org/browse/MCOL-849) - Process Manager leaving files called '+' lying around
* [MCOL-850](https://jira.mariadb.org/browse/MCOL-850) - ProcMgr crashes when too many 'getactivealarm' calls are made.
* [MCOL-857](https://jira.mariadb.org/browse/MCOL-857) - PrimProc thread leak on ByteStream advance
* [MCOL-860](https://jira.mariadb.org/browse/MCOL-860) - temp file error when using yum localinstall
* [MCOL-864](https://jira.mariadb.org/browse/MCOL-864) - Ubuntu columnstoreClusterTester.sh incorrectly raises issue for snappy package
* [MCOL-868](https://jira.mariadb.org/browse/MCOL-868) - merge mariadb server 10.1.26

## Upgrade

Multi version upgrades are not supported, please upgrade versions prior to 1.0.10 before upgrading to 1.0.11:

* [1.0.10 GA to 1.0.11 upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md)

## Known issues and limitations

There are a number bugs and known limitations within this version of MariaDB ColumnStore, the most serious of these are listed below.

* [MCOL-73](https://jira.mariadb.org/browse/MCOL-73): Wide table formatted display causes frontend to return error
  * MariaDB ColumnStore supports wide tables storage
  * Displaying the query results on a large number of columns without formatting the column works
  * Displaying the query results on a large number of columns with formatting causes error at MariaDB Server level
* [MCOL-271](https://jira.mariadb.org/browse/MCOL-271) empty string values are treated as NULL. This means you cannot insert empty values into a NOT NULL string column.
* [MCOL-364](https://jira.mariadb.org/browse/MCOL-364): In a multi UM configuration where the default storage engine has been set to columnstore replicated tables are not created as columnstore tables. Avoid overriding the default storage engine and specify engine=columnstore on all table DDL.
* [MCOL-365](https://jira.mariadb.org/browse/MCOL-365): Log files created by load data infile remain in the bulk/data/log and /tmp directories. If storage is a concern these can safely be removed.
* [MCOL-463](https://jira.mariadb.org/browse/MCOL-463) : gluster storage option in installer fails with an error. The installer option to install optimized for gluster storage will fail with an error. Manually set up gluster volumes can be used with the 'External' storage option.
* [MCOL-540](https://jira.mariadb.org/browse/MCOL-540) : In a non root Ubuntu install with local query enabled, the PM servers crash and restart on table creation.
* [MCOL-892](https://jira.mariadb.org/browse/MCOL-892) : 1.0.11 upgrade failed when base directory is nfs mounted
* The current logging default generates full verbose debug logs. This can be controlled by making logging configuration changes as described [here](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/management/columnstore-system/columnstore-system-monitoring-configuration).
* While Millisecond and Microsecond storage is supported for datetime, time and timestamp columns, at this time the query results cannot return millisecond and microseconds.
* UTF-8 Limitation
  * UTF-8 must be declared at the table level if the instance has been set up with a UTF-8 profile. Tables created with a non-matching character set will yield indeterminate results.
  * Viewing SQL output should be done using client software that supports UTF-8 character sets.
  * UTF-8 characters are not supported in object names.
* Known security issues and fixes are documented [here](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/security/columnstore-security-vulnerabilities).

## Documentation

[MariaDB ColumnStore Documentation](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md)

## Packaging

RPM, Debian, and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.0.11 GA version.

* The supported OS for the GA version are CentOS 6, CentOS 7, Debian 8.6, Debian 9.1, RedHat 6, RedHat 7, SUSE 12, and Ubuntu 16.0.4.
* Packages can be downloaded [here](https://mariadb.com/downloads/columnstore)
* An Amazon AWS AMI Image is available for this release, please search for AMI name "MariaDB-ColumnStore-1.0.11". AMI specific installation instructions can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md).
* Certified to run in Google Cloud Environment in the GA OSs.

## Source code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.

The source code is available at these locations

* Storage Engine - [Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine)
* MariaDB Server - [Source code based on MariaDB Server 10.1.26 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
