---
description: >-
  Implement multi-master ring replication in MariaDB Server. This section covers
  configuring a circular replication topology for high availability and load
  balancing across multiple active master server
---

# Multi-Master Ring Replication

{% hint style="info" %}
The terms _master_ and _slave_ have historically been used in replication, and MariaDB has begun the process of adding _primary_ and _replica_ synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.
{% endhint %}

## What is Multi-Master Ring Replication

Multi-Master "Ring" Replication means that you have two or more masters where each master is replicating its data to another master asynchronously. This is not to be confused with [MariaDB Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/) which is a [virtually synchronous](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/readme/about-galera-replication) multi-primary cluster for MariaDB.

The benefit of asynchronous replication compared to [Galera Cluster](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/), is that Ring Replication is resilient against bad network connections between the master servers. If a connection goes down, all masters will continue to serve its clients locally and data will automatically be synced when the link is available again.

The following picture shows one of the more advanced Multi-Master setups that is resilient against any master going down but can also handle 'human failures', like an accidental drop table, thanks to the addition of [delayed slaves](delayed-replication.md).

![](../../.gitbook/assets/multi-master-ring-replication1.png)

One should [setup replication](setting-up-replication.md) on each master like one does in [standard MariaDB replication](./). The replication setup among the masters should be a ring. In other words, each master should replicate to one other master and each master should only have one other master as a slave.

Each master can of course have one or more normal slaves. A master could also be a [slave of another master](multi-source-replication.md) that is not in the ring setup.

All MariaDB servers support Multi-Master Ring Replication. In fact, when MySQL replication was originally designed around the year 2000, it was to be a Multi-Master Ring Replication solution for Yahoo to replicate from the East Coast to the West Coast.

### Configuring the Masters

First, follow the instructions in [setup replication](setting-up-replication.md). The main thing to remember is to use the [master\_use\_gtid=current\_pos](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_use_gtid) option for [CHANGE MASTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md).

The main things that are different for Multi-Master Ring Replication are:

* Give every master and slave in the replication setup a unique server\_id. This can be a number from 1 to 4294967295 or 1-255 if one is using [uuid\_short()](../../reference/sql-functions/secondary-functions/miscellaneous-functions/uuid_short.md). It is a good practice to ensure that you do not have any servers in your system with the same server\_id!
* Use [global transaction id](gtid.md) (as described above)
* Give each master a unique [gtid\_domain\_id](gtid.md#gtid_domain_id). This will allow replication to apply transactions from a different master in parallel independent from other masters.

Add the following into your [my.cnf](../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) file for **all masters** and restart the servers.

```
[mariadb]
# Replace the following with a unique ID. All slaves of this master should have the same
# gtid_domain_id to allow easy failover to a slave if needed
gtid_domain_id=1
#
# Let us assume there will never be more than 10 masters in a Multi-Master ring setup
auto_increment_increment=10
# Set this to a different value 1-10 for each master. Could be the same as gtid_domain_id
# This is to ensure that all masters generate different values for AUTO_INCREMENT keys.
auto_increment_offset=1
#
# The following is needed to ensure the ALTER TABLE on another master will not
# break ring replication
slave_type_conversions=ALL_NON_LOSSY,ALL_LOSSY
#
# We cannot use semi-sync in Ring Replication as the masters need to be resilient against
# bad connections
rpl_semi_sync_master_enabled=0
#
# We have to log updates from other masters to the binary log.
log_slave_updates
```

### Limitations when using Ring Replication

* MariaDB does not yet support conflict resolution for conflicting changes. It is up to the application to ensure that there is never a conflicting insert/update/delete between the masters. The easiest setup is having each master server work on a different database or table. If not, one must:
  * Ensure you have an id (master-unique-id) for each row that unequally identifies the master who is responsible for this row. This should preferably be short and part of the primary key in each table. A good value for this would be the `gtid_domain_id` as this is unique for each local cluster.
  * Never insert rows with `PRIMARY KEY` or `UNIQUE KEY` values that can be same on another master. This can be avoided by
    * Have the master-unique-id part of all primary and unique keys.
    * In case of AUTO\_INCREMENT keys, have a different value for [auto\_increment\_offset](../../reference/data-types/auto_increment.md#replication) on each master.
    * Use [uuid\_short()](../../reference/sql-functions/secondary-functions/miscellaneous-functions/uuid_short.md) to generate unique values, like in `create table t1 (a bigint unsigned default(uuid_short()) primary key)`. Note that if one is using [uuid\_short()](../../reference/sql-functions/secondary-functions/miscellaneous-functions/uuid_short.md) in Multi-Master ring replication, one can only use `server_id` in the range 1-255!
  * Ensure that [UPDATE](../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md) and [DELETE](../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) on each master only update rows generated by this master.
* If several masters are constantly generating and updating rows for common tables, one has to be extra careful with `ALTER TABLE` to ensure that any change one does will not cause conflicts when the `ALTER TABLE` is replicated to other servers. In particular one has to ensure that all masters and their slaves are configured with `slave_type_conversions=ALL_NON_LOSSY,ALL_LOSSY`.
* The `server_id` should be unique for each server. One should not change the `server_id` of an active master, as the ID is used by the master to recognize its own events and stop them from replicating endlessly around the ring (see [replicate\_same\_server\_id](../../server-management/starting-and-stopping-mariadb/mariadbd-options.md#-replicate-same-server-id)).

### How does Multi-Master Ring Replication work

* The main difference between Multi-Master Ring Replication and normal replication is that a change done by a master will eventually replicate back to it. When this happens, the master will see that the binary log event has the same server\_id as the master has and will ignore the event. This is why it is critical to ensure that all server\_id's are unique and that one does not change the server id.
* When doing [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table.md) in a Multi-Master Ring replication setup, you should be aware the while you are running an [ALTER TABLE](../../reference/sql-statements/data-definition/alter/alter-table.md) on one master, another master can generate events that uses the old table definition. You should especially take care to not drop columns that could be in use by any application or still available in the upcoming replication stream.

### How to resolve things if they go wrong in Multi-Master Ring Replication

When used correctly, Multi-Master Ring Replication is as resilient to errors as normal MariaDB master-slave replication. If the connection goes down, the replication will stop and will automatically continue when the connection resumes.

#### What to do when one of the masters dies and has to be replaced by a slave.

* Ensure that the slave is up to date (has digested all relay events).
* Check if there are any events on the old master that have not been sent to the slave. You can use [mariadb-binlog](../../clients-and-utilities/logging-tools/mariadb-binlog/) to read the old master binary log files and apply them to the slave.
* You can now treat the slave as a new master and put it back in the replication ring. The new master will use its replication GTID position to continue replication from the other master in the ring.

If the slave is **not up to date** and one cannot access any information of the old master, then one can continue the following way:

* Enable the option [--gtid-ignore-duplicates](gtid.md#gtid_ignore_duplicates) on the servers.
* Add the slave to the replication ring.
* The two masters (one of which is the old slave now added to the ring) will each replicate the events they are missing from one another. The `--gtid-ignore-duplicates` option is needed to allow the two masters in the ring to start replicating from each other when each server is ahead of the other in one domain and behind in another.

**Error applying events**

As long as each master handles their own set of data, as described above, there should not be any conflicting data coming from the other master.

If there are conflicts, one should resolve them as one resolves issues with normal replication.\
The most common way to solve issues is to skip the conflicting log events with [SET GLOBAL SQL\_SLAVE\_SKIP\_COUNTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/set-global-sql_slave_skip_counter.md).

#### Handling duplicate key errors and other conflicts

If things are setup correctly as described earlier, one should never get duplicate key errors in Multi-Master ring replication. Any duplicate key error or data mismatch is usually an application error where it inserts/updates or deletes something it should not have the right to do.

To fix this:

* Use [SET GLOBAL SQL\_SLAVE\_SKIP\_COUNTER](../../reference/sql-statements/administrative-sql-statements/replication-statements/set-global-sql_slave_skip_counter.md) to skip the error.
* Use \`mariadb-binlog --base64-output=decode-rows --verbose --start-position=

## binlog-name\` to see what is missing and apply the changes missing on the server (minus the conflict).

## Multi-Master Ring Replication through slaves

An alternative setup to use for Multi-master ring replications is to replicate to the other\
masters through slaves. The following setup shows how this can be done.

![](../../.gitbook/assets/multi-master-ring-replication2.png)

### Benefits of replication through slaves

* The slave will never be out of sync compared to other master. This makes failover from master to slave much easier as one does not have to check if slave has all data.
* Slightly less load on the master
* One can use [semisynchronous-replication](semisynchronous-replication.md) between master and slave.
* Slave configuration is consolidated to one place. That is, if a master's immediate slave and replicating master should share the same configuration (e.g. rewrite rules, filters, etc), only the immediate slave needs them configured, as the replicating master will pull in the effects inherently.

### Disadvantages of replication through slaves

* There will be a slightly longer delay for the data to hit the next master as it has to go trough the slave. This can be notable if there is a very large transaction executed on the master.
* If the master OR the slave dies, the replication to other masters will stop.
* A replicating master is subject to the configuration of a slave (e.g. transactions may be incorrectly filtered out).
* Re-setting replication after failover is a bit more complex.

#### Setting things up

* Setup is identical to Multi-Master Ring Replication, except that rpl\_semi\_sync\_master\_enabled=0 is not required.

#### What to do when one of the masters dies and has to be replaced by a slave.

Let assume that master1 in the above picture has failed.

What needs to be done is to replace master1 with slave1 and add a new slave to replace slave1.\
Here follows a step by step description of how to do this.

The new slave that will be added to replace slave1 place will below be called slave3.\
The new master will be called master3 (to simplify explanations).\
Note that in some cases, the failed master can be re-used as the new slave if it did recover properly. If this is the case, reset all replications setups on the failed master.

Note that when one sets up a master->slave replication, all configurations are done only on the slave!

* Promote slave1 as the new master3. Applications should now be moved to use master3. Note [MaxScale](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/) can do this step automatically.
* Setup master3 as a slave of slave2.
  * The ring replication is now active (at least temporarily, until we have slave3 in place).
* Delete the old replication setup in master3 that pointed to the deleted master1.
* Prepare the new slave3 (which can take a while if it based on a backup of master3).
* Setup slave3 as a slave of master3.
* If delayed slave1 exists, redirect it to be a slave of slave3.
* Update master2 to be slave of slave3 (from being a slave of master3).

Some other options:

* For semi-sync setups, the old master1 can be re-used as slave3 if re-started with `--init-rpl-role=SLAVE` during recovery
* For non-semi-synchronous setups, one can use option [CHANGE MASTER TO MASTER\_DEMOTE\_TO\_SLAVE=1](../../reference/sql-statements/administrative-sql-statements/replication-statements/change-master-to.md#master_demote_to_slave) (requires [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/what-is-mariadb-1011) or higher).

### See also

* [Multi-source replication](multi-source-replication.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
