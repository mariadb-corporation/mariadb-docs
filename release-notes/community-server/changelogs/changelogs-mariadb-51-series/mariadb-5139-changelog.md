# MariaDB 5.1.39 Changelog

[Download](https://askmonty.org/wiki/MariaDB:Download:MariaDB_5.1.39) | [Release Notes](../../old-releases/5.1/5.1.39.md) | **Changelog** |[Overview of 5.1](../../old-releases/5.1/changes-improvements-in-mariadb-5-1.md)

**Release date:** 15 Nov 2009

Generally: MariaDB-5.1.39 Beta is based on MySQL-5.1.39, but has these\
additional changes and bug fixes.

* Includes MySQL 5.1.39 (check [MySQL release notes](https://dev.mysql.com/doc/refman/5.1/en/news-5-1-39.html)\
  for details of changes since MySQL 5.1.38)
* Includes XtraDB 1.0.3-8 (check [XtraDB release notes](https://www.percona.com/docs/wiki/percona-xtradb:info:xtradb_changelog#release_1.0.3-8)\
  for details of changes since XtraDB 1.0.3-6)
* RPMs for Centos 5 [now available](https://downloads.askmonty.org/).
* Includes [FederatedX](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/federatedx-storage-engine) as replacement for\
  old Federated storage engine.
* Test suite speedups.
* Binary tarballs now build on Ubuntu Hardy, so now depends on glibc 2.7 rather\
  than 2.9 and so should work on more systems.
* Some (still not all) compiler warnings eliminated.
* [Bug #443014](https://bugs.launchpad.net/bugs/443014) Too many 'skipped' messages in mysql-test-run

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
