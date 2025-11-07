# MariaDB 10.10.0 Release Notes

The most recent release of [MariaDB 10.10](what-is-mariadb-1010.md) is:[**MariaDB 10.10.7**](mariadb-10-10-7-release-notes.md) **Stable (GA)** [Download Now](https://downloads.mariadb.org/mariadb/10.10.7)

[Download 10.10.0](https://downloads.mariadb.org/mariadb/10.10.0)[Release Notes](mariadb-10100-release-notes.md)[Changelog](../../changelogs/10.10/)[Overview of 10.10](what-is-mariadb-1010.md)

**Release date:** 23 Jun 2022

**Do not use&#x20;**_**alpha**_**&#x20;releases in production!**

[MariaDB 10.10](what-is-mariadb-1010.md) is a current development series of MariaDB. It is an evolution\
of [MariaDB 10.9](../release-notes-mariadb-10-9-series/what-is-mariadb-109.md) with several entirely new features.

[MariaDB 10.10.0](mariadb-10100-release-notes.md) is not a single release, but is instead a number of preview releases based on feature branches. Each should be considered [_**Alpha**_](../../about/release-criteria.md).

**For an overview of** [**MariaDB 10.10**](what-is-mariadb-1010.md) **see the**[**What is MariaDB 10.10?**](what-is-mariadb-1010.md) **page.**

Thanks, and enjoy MariaDB!

Remember, these features are in separate _preview packages_. The subsection header text corresponds to the preview package name.

### Replication

* Change defaults for CHANGE MASTER TO so that GTID-based replication is used by default if master supports it ([MDEV-19801](https://jira.mariadb.org/browse/MDEV-19801))
* Deprecate [MASTER\_USE\_GTID=Current\_Pos](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to#master_use_gtid) to favor new [MASTER\_DEMOTE\_TO\_SLAVE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to#master_demote_to_slave) option ([MDEV-20122](https://jira.mariadb.org/browse/MDEV-20122))

Available as container: quay.io/mariadb-foundation/mariadb-devel:10.10-gtid

### Optimizer

* Improve optimization of joins with many tables, including eq\_ref tables ([MDEV-28852](https://jira.mariadb.org/browse/MDEV-28852))
* Table elimination does not work across derived tables ([MDEV-26278](https://jira.mariadb.org/browse/MDEV-26278))

Available as container: quay.io/mariadb-foundation/mariadb-devel:10.10-optimizer

### UCA14 Collation

* Add UCA-14.0.0 [collations](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets) ([MDEV-27009](https://jira.mariadb.org/browse/MDEV-27009))
* Improve contraction performance in UCA collations ([MDEV-27265](https://jira.mariadb.org/browse/MDEV-27265))
* Improve UCA collation performance for utf8mb3 and utf8mb4 ([MDEV-27266](https://jira.mariadb.org/browse/MDEV-27266))

Available as container: quay.io/mariadb-foundation/mariadb-devel:10.10-uca14

### DDL

* [ALTER ONLINE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table#alter-online-table) ([MDEV-16329](https://jira.mariadb.org/browse/MDEV-16329) not included in [MariaDB 10.10.1](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series/mariadb-10101-release-notes)
* Atomic CREATE OR REPLACE TABLE ([MDEV-25292](https://jira.mariadb.org/browse/MDEV-25292)) (not included in [MariaDB 10.10.1](https://mariadb.com/docs/release-notes/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series/mariadb-10101-release-notes))

Available as container: quay.io/mariadb-foundation/mariadb-devel:10.10-ddl

### Galera

* Implement a method to add IPs to allowlist for Galera Cluster node addresses that can make SST/IST requests ([MDEV-27246](https://jira.mariadb.org/browse/MDEV-27246))

### Miscellaneous

* Change default of [explicit\_defaults\_for\_timestamp](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#explicit_defaults_for_timestamp) to ON ([MDEV-28632](https://jira.mariadb.org/browse/MDEV-28632))
* \--ssl option set as default for mariadb CLI ([MDEV-27105](https://jira.mariadb.org/browse/MDEV-27105))
* Add [RANDOM\_BYTES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/random_bytes) function ([MDEV-25704](https://jira.mariadb.org/browse/MDEV-25704))
* The [INET4](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/inet4) data type ([MDEV-23287](https://jira.mariadb.org/browse/MDEV-23287))
* Re-design the upper level of handling UPDATE and DELETE statements ([MDEV-28883](https://jira.mariadb.org/browse/MDEV-28883))
* Deprecate the [DES\_ENCRYPT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/des_encrypt)/[DECRYPT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/des_decrypt) functions ([MDEV-27104](https://jira.mariadb.org/browse/MDEV-27104))

Available as container: quay.io/mariadb-foundation/mariadb-devel:10.10-misc

**Do not use&#x20;**_**alpha**_**&#x20;releases on production systems!**\
For a complete list of changes made in [MariaDB 10.10.0](mariadb-10100-release-notes.md), with links to detailed\
information on each push, see the [changelog](https://github.com/mariadb-corporation/docs-release-notes/blob/test/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series/mariadb-10100-changelog/README.md).

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
