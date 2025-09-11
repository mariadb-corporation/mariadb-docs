# MariaDB ColumnStore 1.0.7 GA Release Notes

**Release date:** 23rd January 2017

[MariaDB ColumnStore 1.0.7](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) is a GA release of MariaDB ColumnStore. This release of MariaDB ColumnStore provides improvements over the previous 1.0.6 GA release.

MariaDB ColumnStore 1.0.7 is a [_**GA**_](../../../community-server/about/release-criteria.md) release.

For an overview of [MariaDB ColumnStore](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md) see [MariaDB ColumnStore Architectural Overview](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/architecture/columnstore-architectural-overview)

Please provide feedback in [JIRA](https://jira.mariadb.org/browse/MCOL) for anything that is not working as expected so that we can fix it before we make the release available for the larger community.\
For general "how to questions" ask questions [here](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) or subscribe to mariadb-columnstore@googlegroups.com

## Notable changes

* [MCOL-506](https://jira.mariadb.org/browse/MCOL-506) - The MariaDB server version has been upgraded to version 10.1.21 including key security fixes. See the [Server Release Notes](../../../community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10121-release-notes.md) for further details.
* [MCOL-462](https://jira.mariadb.org/browse/MCOL-462) - The AMI Image now supports utilization of the IAM role to manage keys. Please see the [installing-and-configuring-a-columnstore-system-using-the-amazon-ami](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md) article for more details.
* [MCOL-481](https://jira.mariadb.org/browse/MCOL-481) - For a multi node install with mulitple UMs the installer now prompts you whether you want to install "MariaDB ColumnStore Schema Sync feature". If yes is answered then a default master / slave replication setup will be installed. Answer no if you prefer to perform your own setup or utilize another solution for this.

## Bugs and issues fixed

* [MCOL-163](https://jira.mariadb.org/browse/MCOL-163) - DOUBLE PRECISION synonym for DOUBLE datatype not supported
* [MCOL-301](https://jira.mariadb.org/browse/MCOL-301) - aggregation over boolean expression fails with error 1178
* [MCOL-315](https://jira.mariadb.org/browse/MCOL-315) - switch to using os distribution version of libxml
* [MCOL-389](https://jira.mariadb.org/browse/MCOL-389) - cast of int mod function to char results in trailing decimal points
* [MCOL-449](https://jira.mariadb.org/browse/MCOL-449) - The generated server test DEB package doesn't install
* [MCOL-451](https://jira.mariadb.org/browse/MCOL-451) - findobjectfile should report filename for dictionary oid
* [MCOL-453](https://jira.mariadb.org/browse/MCOL-453) - change mcsadmin to only allow the module add/remove/disable commands from active PM Module
* [MCOL-454](https://jira.mariadb.org/browse/MCOL-454) - columnstore\_info's total\_usage() and table\_usage() reported 0 usage on multi-node configuration
* [MCOL-455](https://jira.mariadb.org/browse/MCOL-455) - redistribute data's 'START REMOVE' option did not move data from the requested dbroot
* [MCOL-461](https://jira.mariadb.org/browse/MCOL-461) - remove the option of 'mp' in postConfigure
* [MCOL-462](https://jira.mariadb.org/browse/MCOL-462) - Amazon ColumnStore AMI support of IAM role with certificates
* [MCOL-467](https://jira.mariadb.org/browse/MCOL-467) - replication setup issues when adding modules in combined setup
* [MCOL-470](https://jira.mariadb.org/browse/MCOL-470) - merge server 10.1.20 code
* [MCOL-475](https://jira.mariadb.org/browse/MCOL-475) - Error in script /usr/local/mariadb/columnstore/bin/rsync.sh
* [MCOL-476](https://jira.mariadb.org/browse/MCOL-476) - postConfigure refers to 'Columnstore' instead of 'ColumnStore' as the product
* [MCOL-477](https://jira.mariadb.org/browse/MCOL-477) - can't reset autoincrement values
* [MCOL-481](https://jira.mariadb.org/browse/MCOL-481) - Add prompt to disable/enable mysql replication in postConfigure
* [MCOL-483](https://jira.mariadb.org/browse/MCOL-483) - Error in shell script
* [MCOL-488](https://jira.mariadb.org/browse/MCOL-488) - create AlarmConfig.installSave file
* [MCOL-493](https://jira.mariadb.org/browse/MCOL-493) - rpm install for multi node combined fails to setup logging on other nodes
* [MCOL-494](https://jira.mariadb.org/browse/MCOL-494) - Cannot execute query on mixed engine tables
* [MCOL-505](https://jira.mariadb.org/browse/MCOL-505) - Performance improvements to ExeMgr
* [MCOL-506](https://jira.mariadb.org/browse/MCOL-506) - merge server 10.1.21 release

## Upgrade

Multi version upgrades are not supported, please upgrade versions prior to 1.0.6 before upgrading to 1.0.7:

* [1.0.6 GA to 1.0.7 upgrade procedure](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md)

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

[MariaDB ColumnStore Documentation](https://github.com/mariadb-corporation/docs-release-notes/blob/test/kb/en/mariadb-columnstore/README.md)

## Packaging

RPM, Debian, and binary packages are provided for the Linux distributions supported by MariaDB ColumnStore 1.0.7 GA version.

* The supported OS for the GA version are CentOS 6, CentOS 7, Debian 8.6, RedHat 6, RedHat 7, and Ubuntu 16.0.4.
* Packages can be downloaded [here](https://mariadb.com/downloads/columnstore)
* An Amazon AWS AMI Image is available for this release, please search for AMI name "MariaDB-ColumnStore-1.0.7". AMI specific installation instructions can be found [here](https://github.com/mariadb-corporation/docs-server/blob/test/release-notes/columnstore/columnstore-1-0/broken-reference/README.md).
* Instructions for setting up OS software repositories as the download mechanism will be published shortly.

## Source code

The source code of MariaDB ColumnStore is tagged at GitHub with a tag, which is identical with the version of MariaDB ColumnStore. For instance, the tag of version X.Y.Z of MariaDB ColumnStore is columnstore-X.Y.Z. Further, master always refers to the latest released non-beta version.

The source code is available at these locations

* Storage Engine - [Source code for engine specific processes on UM and PM node](https://github.com/mariadb-corporation/mariadb-columnstore-engine)
* MariaDB Server - [Source code based on MariaDB Server 10.1.21 modified to support the ColumnStore storage engine](https://github.com/mariadb-corporation/mariadb-columnstore-server)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
