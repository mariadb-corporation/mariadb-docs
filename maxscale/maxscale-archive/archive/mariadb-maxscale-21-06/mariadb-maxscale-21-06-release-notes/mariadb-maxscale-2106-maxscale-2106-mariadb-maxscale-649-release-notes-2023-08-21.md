# MariaDB MaxScale 6.4.9 Release Notes -- 2023-08-21

Release 6.4.9 is a GA release.

This document describes the changes in release 6.4.9, when compared to the\
previous release in the same series.

If you are upgrading from an older major version of MaxScale, please read the [upgrading document](https://mariadb.com/kb/Upgrading/Upgrading-To-MaxScale-6) for\
this MaxScale version.

For any problems you encounter, please consider submitting a bug\
report on [our Jira](https://jira.mariadb.org/projects/MXS).

### Bug fixes

* [MXS-4722](https://jira.mariadb.org/browse/MXS-4722) Case-sensitiveness of enumerations is not documented
* [MXS-4721](https://jira.mariadb.org/browse/MXS-4721) Galeramon does not update replication lag of replicating servers
* [MXS-4720](https://jira.mariadb.org/browse/MXS-4720) Implement an option to switch to the old "ping" behaviour in MaxScale
* [MXS-4719](https://jira.mariadb.org/browse/MXS-4719) Connection init sql file execution can hang
* [MXS-4714](https://jira.mariadb.org/browse/MXS-4714) qc\_sqlite does not properly parse a RENAME statement
* [MXS-4708](https://jira.mariadb.org/browse/MXS-4708) Update maxscale.cnf default file
* [MXS-4704](https://jira.mariadb.org/browse/MXS-4704) SHOW TABLE STATUS FROM some\_schema Fails with SchemaRouter
* [MXS-4701](https://jira.mariadb.org/browse/MXS-4701) GTID update may block the REST-API
* [MXS-4700](https://jira.mariadb.org/browse/MXS-4700) Binlogrouter treats GTID sequences as 32-bit integers
* [MXS-4696](https://jira.mariadb.org/browse/MXS-4696) Readwritesplit does not detect unrecoverable situations
* [MXS-4695](https://jira.mariadb.org/browse/MXS-4695) Binlogrouter always opens a new binlog on startup
* [MXS-4691](https://jira.mariadb.org/browse/MXS-4691) Binlogrouter cannot write binlog files larger than 4GiB
* [MXS-4690](https://jira.mariadb.org/browse/MXS-4690) Binlogrouter runs out of memory on very large transactions
* [MXS-4684](https://jira.mariadb.org/browse/MXS-4684) Detect ALTER EVENT failure on MariaDB 11.0
* [MXS-4681](https://jira.mariadb.org/browse/MXS-4681) Encrypted passwords are persisted in plaintext
* [MXS-4680](https://jira.mariadb.org/browse/MXS-4680) Session idleness diagnostic is wrong
* [MXS-4677](https://jira.mariadb.org/browse/MXS-4677) MaxScale BinlogRouter skips large transactions causing data Inconsistency on attached slave
* [MXS-4675](https://jira.mariadb.org/browse/MXS-4675) Switchover fails with 'Unknown thread id' error
* [MXS-4672](https://jira.mariadb.org/browse/MXS-4672) Document grants needed for MariaDB 11.1
* [MXS-4613](https://jira.mariadb.org/browse/MXS-4613) binlogrouter shows MaxScale's binary log coordinates in SHOW SLAVE STATUS

### Known Issues and Limitations

There are some limitations and known issues within this version of MaxScale.\
For more information, please refer to the [Limitations](../mariadb-maxscale-21-06-about/mariadb-maxscale-2106-maxscale-2106-limitations-and-known-issues-within-mariadb-maxscale.md) document.

### Packaging

RPM and Debian packages are provided for the supported Linux distributions.

Packages can be downloaded [here](https://mariadb.com/downloads/#mariadb_platform-mariadb_maxscale).

### Source Code

The source code of MaxScale is tagged at GitHub with a tag, which is identical\
with the version of MaxScale. For instance, the tag of version X.Y.Z of MaxScale\
is `maxscale-X.Y.Z`. Further, the default branch is always the latest GA version\
of MaxScale.

The source code is available [here](https://github.com/mariadb-corporation/MaxScale).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
