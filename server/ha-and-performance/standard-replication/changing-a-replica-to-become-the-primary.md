---
description: >-
  Follow the procedure to promote a replica to a primary role. This guide
  details the steps for planned failovers or topology reorganization with
  minimal downtime.
---

# Changing a Replica to Become the Primary

{% hint style="info" %}
The terms _master_ and _slave_ have historically been used in replication, and MariaDB has begun the process of adding _primary_ and _replica_ synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.
{% endhint %}

This article describes how to change a replica to become a primary and optionally to set the old primary as a replica for the new primary.

A typical scenario of when this is useful is if you have set up a new\
version of MariaDB as a replica, for example for testing, and want to\
upgrade your primary to the new version.

In MariaDB replication, a replica should be of a version same or newer than the primary. Because of this, one should first upgrades all replicas to the latest version before changing a replica to be a primary. In some cases one can have a replica to be of an older version than the primary, as long as one doesn't execute on the primary any SQL commands that the replica doesn't understand. This is however not guaranteed between all major MariaDB versions.

Note that in the examples below, `[connection_name]` is used as the [name of the connection](multi-source-replication.md). If you are not using named connections you can ignore this.

### Stopping the Original Master.

First one needs to take down the original primary in such a way that the replica\
has all information on the primary.

If you are using [Semisynchronous Replication](semisynchronous-replication.md) you can just stop the server with the [SHUTDOWN](../../reference/sql-statements/administrative-sql-statements/shutdown.md) command as the replicas should be automatically up to date.

If you are using [MariaDB MaxScale proxy](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/), then you [can use MaxScale](https://mariadb.com/resources/blog/mariadb-maxscale-2-2-introducing-failover-switchover-and-automatic-rejoin) to handle the whole process of taking down the primary and replacing it with one of the replicas.

If neither of the above is true, you have to do this step manually:

#### Manually Take Down the Primary

First we have to set the primary to read only to ensure that there are no new updates on the primary:

```sql
FLUSH TABLES WITH READ LOCK;
```

Note that you should not disconnect this session as otherwise the read lock will disappear and you have to start from the beginning.

Then you should check the current position of the primary:

```sql
SHOW MASTER STATUS;
+--------------------+----------+--------------+------------------+
| File               | Position | Binlog_Do_DB | Binlog_Ignore_DB |
+--------------------+----------+--------------+------------------+
| mariadb-bin.000003 |      343 |              |                  |
+--------------------+----------+--------------+------------------+
SELECT @@global.gtid_binlog_pos;
+--------------------------+
| @@global.gtid_binlog_pos |
+--------------------------+
| 0-1-2                    |
+--------------------------+
```

And wait until you have the same position on the replica:\
(The following should be expected on the replica)

```sql
SHOW SLAVE [connection_name] STATUS;
+-------------------+-------------------+
Master_Log_File     | narttu-bin.000003 +
Read_Master_Log_Pos | 343               +
Exec_Master_Log_Pos | 343               +
...
Gtid_IO_Pos          0-1-2              +
+-------------------+-------------------+
```

The most important information to watch are `Master_Log_File` and`Exec_Master_Log_Pos` as when this matches the primary, it signals\
that all transactions have been committed on the replica.

Note that `Gtid_IO_Pos` on replica can contain many different positions\
separated with ',' if the replica has been connected to many different\
primaries. What is important is that all the sequences that are on the\
primary is also on the replica.

When replica is up to date, you can then take the **PRIMARY** down. This should be on the same connection where you executed [FLUSH TABLES WITH READ LOCK](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md).

```sql
SHUTDOWN;
```

### Preparing the Replica to be a Primary

Stop all old connections to the old primary(s) and reset **read only**\
**mode**, if you had it enabled. You also want to save the values of [SHOW MASTER STATUS](../../reference/sql-statements/administrative-sql-statements/show/show-binlog-status.md) and `gtid_binlog_pos`, as\
you may need these to setup new replicas.

```sql
STOP ALL SLAVES;
RESET SLAVE ALL;
SHOW MASTER STATUS;
SELECT @@global.gtid_binlog_pos;
SET @@global.read_only=0;
```

### Reconnect Other Replicas to the New Primary

On the other replicas you have point them to the new primary (the replica you promoted to a primary).

```sql
STOP SLAVE [connection_name];
CHANGE MASTER [connection_name] TO 
 MASTER_HOST="new_master_name",
 MASTER_PORT=3306, 
 MASTER_USER='root', 
 MASTER_USE_GTID=current_pos,
 MASTER_LOG_FILE="XXX", 
 MASTER_LOG_POS=XXX;
START SLAVE;
```

The `XXX` values for `MASTER_LOG_FILE` and `MASTER_LOG_POS` should be the values you got from the `SHOW MASTER STATUS` command you did when you finished setting up the replica.

### Changing the Old Primary to be a Replica

Now you can upgrade the old primary to a newer version of MariaDB and then\
follow the same procedure to connect it as a replica.

When starting the original primary, it's good to start the `mysqld`\
executable with the `--with-skip-slave-start` and `--read-only`\
options to ensure that no old replica configurations could cause any\
conflicts.

For the same reason it's also good to execute the following commands\
on the old primary (same as for other replicas, but with some extra\
security). The `read_only` option below is there to ensure that old\
applications doesn't by accident try to update the old primary by mistake.\
It only affects normal connections to the replica, not changes from the\
new primary.

```sql
SET @@global.read_only=1;
STOP ALL SLAVES;
RESET MASTER;
RESET SLAVE ALL;
CHANGE MASTER [connection_name] TO 
 MASTER_HOST="new_master_name",
 MASTER_PORT=3306, 
 MASTER_USER='root', 
 MASTER_USE_GTID=current_pos,
 MASTER_LOG_FILE="XXX", 
 MASTER_LOG_POS=XXX;
START SLAVE;
```

### Moving Applications to Use New Primary

You should now point your applications to use the new primary.\
If you are using the [MariaDB MaxScale proxy](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/), then you don't\
have to do this step as MaxScale will take care of sending write request\
to the new primary.

### See Also

* [CHANGE MASTER TO](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md) command
* [MaxScale Blog about using Switchover to swap a primary and replica](https://mariadb.com/resources/blog/mariadb-maxscale-2-2-introducing-failover-switchover-and-automatic-rejoin)
* [Percona blog about how to upgrade replica to primary](https://www.percona.com/blog/2015/12/01/upgrade-master-server-minimal-downtime)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
