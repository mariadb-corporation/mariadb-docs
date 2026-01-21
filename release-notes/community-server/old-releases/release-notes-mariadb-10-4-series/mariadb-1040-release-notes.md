# MariaDB 10.4.0 Release Notes

The most recent release of [MariaDB 10.4](what-is-mariadb-104.md) is:[**MariaDB 10.4.34**](mariadb-10-4-34-release-notes.md) Stable (GA) [Download Now](https://downloads.mariadb.org/mariadb/10.4.34/)

[Download](https://downloads.mariadb.org/mariadb/10.4.0/) | [Release Notes](mariadb-1040-release-notes.md) | [Changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-1040-changelog.md) | [Overview of 10.4](what-is-mariadb-104.md)

**Release date:** 9 Nov 2018

[MariaDB 10.4](what-is-mariadb-104.md) is the current _development_ series of MariaDB. It is an evolution\
of [MariaDB 10.3](../release-notes-mariadb-10-3-series/what-is-mariadb-103.md) with several entirely new features not found anywhere else\
and with backported and reimplemented features from MySQL.

[MariaDB 10.4.0](mariadb-1040-release-notes.md) is an [_**Alpha**_](../../about/release-criteria.md) release.

**Do not use&#x20;**_**alpha**_**&#x20;releases in production!**

**For an overview of** [**MariaDB 10.4**](what-is-mariadb-104.md) **see the**[**What is MariaDB 10.4?**](what-is-mariadb-104.md) **page.**

Thanks, and enjoy MariaDB!

## Notable Changes

This will be the first alpha release in the [MariaDB 10.4](what-is-mariadb-104.md) series.

Notable changes of this release include:

### InnoDB

* Added instant [DROP COLUMN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table#drop-column) and changing of the order of columns ([MDEV-15562](https://jira.mariadb.org/browse/MDEV-15562))
* Reduced redo log volume for undo tablespace initialization ([MDEV-17138](https://jira.mariadb.org/browse/MDEV-17138))
* Removed crash-upgrade support for pre-10.2.19 TRUNCATE TABLE ([MDEV-13564](https://jira.mariadb.org/browse/MDEV-13564))
* Added key rotation for [innodb\_encrypt\_log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb/innodb-system-variables) ([MDEV-12041](https://jira.mariadb.org/browse/MDEV-12041))

### Optimizer

* [Push conditions into materialized IN subqueries](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/query-optimizations/subquery-optimizations/condition-pushdown-into-in-subqueries) ([MDEV-12387](https://jira.mariadb.org/browse/MDEV-12387))

### Variables

* Added the [tcp\_nodelay](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#tcp_nodelay) system variable ([MDEV-16277](https://jira.mariadb.org/browse/MDEV-16277))
* Removed the global [Innodb\_pages0\_read](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/innodb-status-variables) status variable ([MDEV-15705](https://jira.mariadb.org/browse/MDEV-15705)).

### General

* `IF NOT EXISTS` clause added to [INSTALL PLUGIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/plugin-sql-statements/install-plugin) and `IF EXISTS` clause added to [UNINSTALL PLUGIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-plugin) and [UNINSTALL SONAME](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/plugin-sql-statements/uninstall-soname) ([MDEV-16294](https://jira.mariadb.org/browse/MDEV-16294))
* The obsolete [mysql.host table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/the-mysql-database-tables/obsolete-mysql-database-tables/mysql-host-table) is no longer created ([MDEV-15851](https://jira.mariadb.org/browse/MDEV-15851))
* Support of brackets (parentheses) for specifying precedence in [UNION](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/set-operations/union)/[EXCEPT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/set-operations/except)/[INTERSECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/set-operations/intersect) operations ([MDEV-11953](https://jira.mariadb.org/browse/MDEV-11953))
* Crash safe [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/aria)-based [system tables](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables) ([MDEV-16421](https://jira.mariadb.org/browse/MDEV-16421))
* Added Linux abstract socket support ([MDEV-15655](https://jira.mariadb.org/browse/MDEV-15655))
* Enabled C++11 ([MDEV-16410](https://jira.mariadb.org/browse/MDEV-16410))
* [SET PASSWORD](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/set-password) support for [ed25519](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-ed25519) and other [authentication plugins](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins) ([MDEV-12321](https://jira.mariadb.org/browse/MDEV-12321))
* Performance improvements in [Unicode](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/character-sets/unicode) collations ([MDEV-17534](https://jira.mariadb.org/browse/MDEV-17534), [MDEV-17511](https://jira.mariadb.org/browse/MDEV-17511), [MDEV-17502](https://jira.mariadb.org/browse/MDEV-17502), [MDEV-17474](https://jira.mariadb.org/browse/MDEV-17474))
* User data type plugins ([MDEV-4912](https://jira.mariadb.org/browse/MDEV-4912), in progress)
* Improvements with SQL standard INTERVAL support to help functions [TIMESTAMP()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/date-and-time-data-types/timestamp)\
  and [ADDTIME()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/addtime) return more predictable results.
  * Historically, MariaDB uses the TIME data type for both "time of the day"\
    values and "duration" values. In the first meaning the natural value range\
    is from '00:00:00' to '23:59:59.999999', in the second meaning the range is\
    from '-838:59:59.999999' to '+838:59:59.999999'.
  * To remove this ambiguity and for the SQL standard conformance we plan to\
    introduce a dedicated data type INTERVAL that will be able to store values\
    in the range at least from '-87649415:59:59.999999' to\
    '+87649415:59:59.999999', which will be enough to represent the time\
    difference between TIMESTAMP'0001-01-01 00:00:00' and TIMESTAMP'9999-12-31\
    23:59:59.999999'.
  * As a first step we support this range of values for intermediate\
    calculations when TIME-alike string and numeric values are used in INTERVAL\
    (i.e. duration) context, e.g. as the second argument of SQL functions\
    TIMESTAMP(ts,interval) and ADDTIME(ts,interval), so the following can now be\
    calculated:

```sql
SELECT ADDTIME(TIMESTAMP'0001-01-01 00:00:00', '87649415:59:59.999999');
-> '9999-12-31 23:59:59.999999'  

SELECT TIMESTAMP(DATE'0001-01-01', '87649415:59:59.999999')
-> '9999-12-31 23:59:59.999999'  

SELECT ADDTIME(TIME'-838:59:59.999999', '1677:59:59.999998');
-> '838:59:59.999999'
```

## Changelog

For a complete list of changes made in [MariaDB 10.4.0](mariadb-1040-release-notes.md), with links to detailed\
information on each push, see the [changelog](../../changelogs/changelogs-mariadb-10-4-series/mariadb-1040-changelog.md).

## Contributors

For a full list of contributors to [MariaDB 10.4.0](mariadb-1040-release-notes.md), see the [MariaDB Foundation release announcement](https://mariadb.org/first-mariadb-10-4-alpha-release/).

**Do not use&#x20;**_**alpha**_**&#x20;releases in production!**

{% include "../../../.gitbook/includes/announce.md" %}

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formid="4316" formId="4316" %}
