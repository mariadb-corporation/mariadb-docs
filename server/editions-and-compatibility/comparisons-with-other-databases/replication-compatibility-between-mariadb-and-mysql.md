# Replication Compatibility Between MariaDB and MySQL

This page describes replication compatibility between MariaDB and MySQL. For replication compatibility details between different MariaDB versions, see [Cross-Version Replication Compatibility](../../ha-and-performance/standard-replication/replication-overview.md#cross-version-replication-compatibility).

## Replication Compatibility

[Replication](../../ha-and-performance/standard-replication/replication-overview.md) compatibility depends on:

* The MariaDB version
* The MySQL version
* The role of each server

## Replicating from MySQL to MariaDB

### MySQL 5.7 to MariaDB

[MariaDB 10.2]({release-notes}/community-server/old-releases/10.2/what-is-mariadb-102) and later can replicate from a MySQL 5.7 primary server.

MariaDB does not support the MySQL implementation of Global Transaction IDs (GTIDs), so the MariaDB replica server must use the binary log file and position for replication. If GTID mode is enabled on the MySQL primary server, the MariaDB replica server will remove the MySQL GTID events and replace them with MariaDB GTID events.

You can disable `GTID` and use logfile name and position in MariaDB by executing on the slave:

```sql
CHANGE MASTER ... MASTER_LOG_FILE=file_name MASTER_LOG_POS=# MASTER_USE_GTID=no
```

Although MariaDB and MySQL 5.7 are compatible at the replication level, they may have some incompatibilities at the SQL level. Those differences can cause replication failures in some cases. To decrease the risk of compatibility issues, it is recommended to set [binlog\_format](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_format) to `ROW` in MySQL. When you want to replicate from MySQL 5.7 to MariaDB, it is recommended to test your application, so that any compatibility issues can be found and fixed. See [Incompatibilities and Feature Differences](incompatibilities-and-feature-differences-between-mariadb-and-mysql-unmaint/) between the specific versions.

### MySQL 8.0 to MariaDB

Prior to [MariaDB 10.6.21]({release-notes}/community-server/10.6/10.6.21), [MariaDB 10.11.11]({release-notes}/community-server/10.11/10.11.11), [MariaDB 11.4.5]({release-notes}/community-server/11.4/11.4.5) and [MariaDB 11.7.2]({release-notes}/community-server/old-releases/11.7/11.7.2), MariaDB Server could not replicate from a MySQL 8.0 primary server, because MySQL 8.0 has a binary log format that includes new events which makes it incompatible.

[MariaDB 10.6.21]({release-notes}/community-server/10.6/10.6.21), [MariaDB 10.11.11]({release-notes}/community-server/10.11/10.11.11), [MariaDB 11.4.5]({release-notes}/community-server/11.4/11.4.5), [MariaDB 11.7.2]({release-notes}/community-server/old-releases/11.7/11.7.2) and newer can replicate from a MySQL 8.0 server with the following conditions:

* Prior to [MariaDB 11.4.9]({release-notes}/community-server/11.4/11.4.9), [MariaDB 11.8.4]({release-notes}/community-server/11.8/11.8.4) and [MariaDB 12.1.1]({release-notes}/community-server/old-releases/12.1/12.1.1), MariaDB does not support the MySQL default authentication caching\_sha2\_password, so one has to add another replication user using the mysql\_native\_password protocol and use this with [CHANGE MASTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) in MariaDB when using an older version.
* Columns of type JSON are not supported. One should change these to `TEXT` in MySQL. MySQL will work fine with JSON as TEXT, except for a minor performance degradation when using JSON expressions.
* `binlog-row-value-options` should be set to `""` should be set. This disables the incompatible `PARTIAL_UPDATE_ROWS_EVENT` event.
* `binlog_transaction_compression` should be set to `0`. This disables binlog compression and the incompatible `TRANSACTION_PAYLOAD_EVENT` event.
* MySQL 8.0 utf8mb4\_ja\_0900\_ collations can not be used when replicating to [MariaDB 10.6]({release-notes}/community-server/10.6/what-is-mariadb-106) - [MariaDB 11.4.4]({release-notes}/community-server/11.4/11.4.4). [MariaDB 11.4.5]({release-notes}/community-server/11.4/11.4.5) and above will support [most of the MySQL 8.0 utf8mb4\_ja\_0900\_... collations](../../reference/data-types/string-data-types/character-sets/supported-character-sets-and-collations.md#collations).
* For differences at the SQL level that may cause replication failures, see [Incompatibilities and Feature Differences](./) between the specific versions. When using [binlog\_format](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#binlog_format) this almost exclusively affects DDL'sm, where MariaDB is very compatible with MySQL.

Here are the changes one should do in the config files for MySQL 8.0:

```
binlog-row-value-options=""
binlog_transaction_compression=0
# Not required, but recommended for cross-replication
binlog_format=row
```

## Replicating from MariaDB to MySQL

Here are some issues to be aware of when replicating from MariaDB to MySQL.

On the MySQL side, one should:

* Not use binlog with [global transaction ids](../../ha-and-performance/standard-replication/gtid/README.md) (CHANGE SOURCE\_AUTO\_POSITION=no)

On the MariaDB side, one should:

* Not use [binlog encryption](../../security/encryption/data-at-rest-encryption/managing-binary-log-encryption.md) ([--encrypt-binlog](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#encrypt_binlog) should be 0)
* Not use [binary log compression](../../server-management/server-monitoring-logs/binary-log/compressing-events-to-reduce-size-of-the-binary-log.md) ([--log-bin-compress](../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin_compress) should be 0)
* Ensure that one uses a [character set](../../reference/data-types/string-data-types/character-sets/README.md) and [collations](../../reference/data-types/string-data-types/character-sets/supported-character-sets-and-collations.md#collations) that MySQL supports. The MariaDB default collations for utf8mb4 is not supported by MySQL. Note that if you just have upgraded from MySQL to MariaDB then you are probably already using the MySQL character sets and collations for your old tables! If you want replication to also work for new tables, the best option is to set the character set and collation in the MariaDB config file.

Example of changes to add to the MariaDB config file:

```ini
encrypt-binlog=0
log-bin-compress=0
# Not required, but recommended for cross-replication
binlog_format=row
# Character set to be able to replicate new tables to  MySQL 8.0
character-set-server=utf8mb4
collation-server=utf8mb4_0900_ai_ci
```

For differences at the SQL level that may cause replication failures, see [Incompatibilities and Feature Differences](./) between the specific versions.

## See also

* [Upgrading from MySQL to MariaDB](../../server-management/install-and-upgrade-mariadb/migrating-to-mariadb/moving-from-mysql/README.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formid="4316" formId="4316" %}
