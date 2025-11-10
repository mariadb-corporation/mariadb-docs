---
description: >-
  Utilize read-only replicas in MariaDB Server for enhanced performance. This
  section explains how to configure replicas to offload read traffic from the
  master, improving scalability.
---

# Read-Only Replicas

A common [replication](./) setup is to have the replicas [read-only](../optimization-and-tuning/system-variables/server-system-variables.md#read_only) to ensure that no one\
accidentally updates them. If the replica has [binary logging enabled](setting-up-replication.md) and [gtid\_strict\_mode](gtid.md#gtid_strict_mode) is used, then any update that causes changes to the [binary log](../../server-management/server-monitoring-logs/binary-log/) will stop replication.

When the variable `read_only` is set to 1, no updates are permitted except from users with the [SUPER](../../reference/sql-statements/account-management-sql-statements/grant.md#super) privilege (<= [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1051-release-notes)) or [READ ONLY ADMIN](../../reference/sql-statements/account-management-sql-statements/grant.md#read_only-admin) privilege (>= [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1052-release-notes)) or replica servers updating from a primary. Inserting rows to log tables, updates to temporary tables and [OPTIMIZE TABLE](../optimization-and-tuning/optimizing-tables/optimize-table.md) or [ANALYZE TABLE](../../reference/sql-statements/table-statements/analyze-table.md) statements on temporary tables are excluded from this limitation.

If read\_only is set to 1, then the [SET PASSWORD](../../reference/sql-statements/account-management-sql-statements/set-password.md) statement is limited only to users with the [SUPER](../../reference/sql-statements/account-management-sql-statements/grant.md#super) privilege (<= [MariaDB 10.5.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1051-release-notes)) or [READ ONLY ADMIN](../../reference/sql-statements/account-management-sql-statements/grant.md#read_only-admin) privilege (>= [MariaDB 10.5.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1052-release-notes)).

Attempting to set the `read_only` variable to 1 will fail if the current session has table locks or transactions pending.

The statement will wait for other sessions that hold table locks. While the attempt to set read\_only is waiting, other requests for table locks or transactions will also wait until read\_only has been set.

### Older MariaDB Versions

If you are using an older MariaDB version with read-only replicas and binary logging enabled on the replica, and you need to do some changes but don't want to have them logged to the binary log, the easiest way to avoid the logging is to [disable binary logging](../../server-management/server-monitoring-logs/binary-log/activating-the-binary-log.md) while running as root during maintenance:

```sql
SET sql_log_bin=0;
ALTER TABLE test ENGINE=rocksdb;
```

The above changes the test table on the replica to rocksdb without registering\
the change in the binary log.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
