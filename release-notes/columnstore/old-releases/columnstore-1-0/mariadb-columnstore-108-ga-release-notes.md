# MariaDB ColumnStore 1.0.8 GA Release Notes

**Release date:** 26th March 2017

[MariaDB ColumnStore 1.0.8](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) is a maintenance GA release of MariaDB ColumnStore. This release of MariaDB ColumnStore provides improvements over the previous 1.0.7 GA release.

MariaDB ColumnStore 1.0.8 is a [_**GA**_](../../../community-server/about/release-criteria.md) release.

For an overview of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md) see [MariaDB ColumnStore Architectural Overview](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview)

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Notable changes

* [MCOL-609](https://jira.mariadb.org/browse/MCOL-609) - ColumnStore has been updated to MariaDB server 10.1.22. This results in some os package dependency changes:
  * 'snappy' library added.
* [MCOL-591](https://jira.mariadb.org/browse/MCOL-591) - The auth\_gssapi plugin is now bundled with ColumnStore enabling kerberos based authentication.\
  auth\_gssapi plugin missing from columnstore package distribution
* [MCOL-592](https://jira.mariadb.org/browse/MCOL-592) - The auth\_pam plugin is now bundled with ColumnStore enabling LDAP based authentication.
* [MCOL-611](https://jira.mariadb.org/browse/MCOL-611) - Bulk cpimport has been optimized to reduce execution overhead in determining completion across multiple nodes.
* [MCOL-640](https://jira.mariadb.org/browse/MCOL-640) - Support Google Cloud Environment

## Bugs and issues fixed

* [MCOL-533](https://jira.mariadb.org/browse/MCOL-533) - table\_usage() has a calculation error
* [MCOL-547](https://jira.mariadb.org/browse/MCOL-547) - enforce limitation of postCfg needing to be run on pm1
* [MCOL-591](https://jira.mariadb.org/browse/MCOL-591) - auth\_gssapi plugin missing from columnstore package distribution
* [MCOL-592](https://jira.mariadb.org/browse/MCOL-592) - auth\_pam plugin missing from columnstore
* [MCOL-604](https://jira.mariadb.org/browse/MCOL-604) - mcsadmin startup changes permission on /dev/shm
* [MCOL-605](https://jira.mariadb.org/browse/MCOL-605) - Crash when running table\_usage
* [MCOL-607](https://jira.mariadb.org/browse/MCOL-607) - post-install change /var/log/mariadb to 777 permissions, causing issues
* [MCOL-609](https://jira.mariadb.org/browse/MCOL-609) - merge server 10.1.22 release
* [MCOL-610](https://jira.mariadb.org/browse/MCOL-610) - warning error reported after upgrade to 1.0.6
* [MCOL-611](https://jira.mariadb.org/browse/MCOL-611) - with 6 PMs, cpimport has an long lag time
* [MCOL-616](https://jira.mariadb.org/browse/MCOL-616) - addmodule failure on ubuntu system after a 1-pm install is done
* [MCOL-617](https://jira.mariadb.org/browse/MCOL-617) - postConfigure/addModule for ubuntu/debian takes too long to perform
* [MCOL-618](https://jira.mariadb.org/browse/MCOL-618) - innodb query crash only happens on columnstore server

## Upgrade

Multi version upgrades are not supported, please upgrade versions prior to 1.0.7 before upgrading to 1.0.8:

* [1.0.7 GA to 1.0.8 upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md)

## Known issues and limitations

There are a number bugs and known limitations within this beta version of MariaDB ColumnStore, the most serious of these are listed below.

* [MCOL-73](https://jira.mariadb.org/browse/MCOL-73): Wide table formatted display causes frontend to return error
  * MariaDB ColumnStore supports wide tables storage
  * Displaying the query results on a large number of columns without formatting the column works
  * Displaying the query results on a large number of columns with formatting causes error at MariaDB Server level
* [MCOL-271](https://jira.mariadb.org/browse/MCOL-271) empty string values are treated as NULL. This means you cannot insert empty values into a NOT NULL string column.
* [MCOL-364](https://jira.mariadb.org/browse/MCOL-364): In a multi UM configuration where the default storage engine has been set to columnstore replicated tables are not created as columnstore tables. Avoid overriding the default storage engine and specify engine=columnstore on all table DDL.
* [MCOL-365](https://jira.mariadb.org/browse/MCOL-365): Log files created by load data infile remain in the bulk/data/log and /tmp directories. If storage is a concern these can safely be removed.
* [MCOL-463](https://jira.mariadb.org/browse/MCOL-463) : gluster storage option in installer fails with an error. The installer option to install optimized for gluster storage will fail with an error. Manually set up gluster volumes can be used with the 'External' storage option.
* The current logging default generates full verbose debug logs. This can be controlled by making logging configuration changes as described [here](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/management/columnstore-system/columnstore-system-monitoring-configuration).
* While Millisecond and Microsecond storage is supported for datetime, time and timestamp columns, at this time the query results cannot return millisecond and microseconds.
* UTF-8 Limitation
  * UTF-8 must be declared at the table level if the instance has been set up with a UTF-8 profile. Tables created with a non-matching character set will yield indeterminate results.
  * Viewing SQL output should be done using client software that supports UTF-8 character sets.
  * UTF-8 characters are not supported in object names.
* Known security issues and fixes are documented [here](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/security/columnstore-security-vulnerabilities).

## Documentation

[MariaDB ColumnStore Documentation](https://github.com/mariadb-corporation/docs-release-notes/blob/test/en/mariadb-columnstore/README.md)

## Packaging

RPM, Debian, and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.0.8 GA version.

* The supported OS for the GA version are CentOS 6, CentOS 7, Debian 8.6, RedHat 6, RedHat 7, SUSE 12, and Ubuntu 16.0.4.
* Packages can be downloaded [here](https://mariadb.com/downloads/columnstore)
* An Amazon AWS AMI Image is available for this release, please search for AMI name "MariaDB-ColumnStore-1.0.8". AMI specific installation instructions can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md).
* Certified to run in Google Cloud Environment in the GA OSs.

## Source code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.

The source code is available at these locations

* Storage Engine - [Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine)
* MariaDB Server - [Source code based on MariaDB Server 10.1.22 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
