---
title: backports-10.5.12-8
---

This release of MariaDB Enterprise Server includes features backported from MariaDB Enterprise Server 10.6.

* [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) allows database-specific and table-specific filters. (MENT-65)\
  For example:

```
{
 "connect_event" : "ALL",
 "table_event" : ["READ","WRITE",{"ignore_tables" : "mysql.*"}],
 "query_event" : ["DDL",{"tables" : "test.t2"}]
}
```

* [MariaDB Enterprise Audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin) can be configured to not start the server if Audit Filters are invalid. (MENT-1243)
  * Added the new [server\_audit\_load\_on\_error](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables) system variable.
  * To configure server startup to fail if Audit Filters are invalid, set [server\_audit\_load\_on\_error](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables) to `OFF` and set [server-audit](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables) to `FORCE` or `FORCE_PLUS_PERMANENT`.
  * The default value of [server\_audit\_load\_on\_error](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables) is `ON`, so the default behavior is the same as in prior releases.
* Enhanced consistency for Semi-Sync Replication
  * When [rpl\_semi\_sync\_slave\_enabled=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/semisynchronous-replication#rpl_semi_sync_slave_enabled), consistency is guaranteed for a Primary server in an HA (Primary/Replica) topology when using semi-synchronous replication. ([MDEV-21117](https://jira.mariadb.org/browse/MDEV-21117))
  * Prior to this release, when using semi-synchronous replication, if a Primary crashed before sending a transaction to the Replica, on restart the Primary could recover incomplete InnoDB transactions when rejoining as a Replica.
  * With this release, when using semi-synchronous replication and with `rpl_semi_sync_slave_enabled=ON`, incomplete transactions will be rolled-back on the Replica, ensuring the new Primary (former Replica) and new Replica (former Primary) remain in sync.
* Enhanced compatibility with Sybase SQL Anywhere through [sql\_mode=EXTENDED\_ALIASES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode): (MENT-1062)\
  With `sql_mode=EXTENDED_ALIASES`, alias resolution and use of column aliases in the SQL [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) list and `WHERE` clause.\
  With `sql_mode=EXTENDED_ALIASES`, support use of an alias in the SELECT list before the alias is defined.\
  With `sql_mode=EXTENDED_ALIASES`, if the same label is used for an alias and a column, the alias is used.
