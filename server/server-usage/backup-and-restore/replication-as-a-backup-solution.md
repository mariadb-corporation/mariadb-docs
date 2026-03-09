---
description: >-
  Explore how to use replication as part of your backup strategy, allowing you
  to offload backup tasks to a replica server to reduce load on the primary.
---

# Replication as a Backup Solution

[Replication](../../ha-and-performance/standard-replication/) can be used to support the [backup](./) strategy.

{% hint style="danger" %}
Replication alone is _not_ sufficient for backup. It assists in protecting against hardware failure on the primary server, but does not protect against data loss. An accidental or malicious `DROP DATABASE` or `TRUNCATE TABLE` statement are replicated onto the replica as well. Care needs to be taken to prevent data getting out of sync between the primary and the replica.
{% endhint %}

{% hint style="info" %}
The terms _master_ and _slave_ have historically been used in replication, and MariaDB has begun the process of adding _primary_ and _replica_ synonyms. The old terms will continue to be used to maintain backward compatibility - see [MDEV-18777](https://jira.mariadb.org/browse/MDEV-18777) to follow progress on this effort.
{% endhint %}

Replication is most commonly used to support backups as follows:

* A primary server replicates to a replica
* Backups are then run off the replica without any impact on the primary.

Backups can have a significant effect on a server, and a high-availability primary may not be able to be stopped, locked or simply handle the extra load of a backup. Running the backup from a replica has the advantage of being able to shutdown or lock the replica and perform a backup without any impact on the primary server.

Note that when backing up off a replica server, it is important to ensure that the servers keep the data in sync. See for example [Replication and Foreign Keys](../../ha-and-performance/standard-replication/replication-and-foreign-keys.md) for a situation when identical statements can result in different data on a replica and a primary.

### Setting Up a Dedicated Backup Replica

To set up a replica specifically for backup purposes, you will need to configure outbound replication from your primary server to the replica. Here is a step-by-step guide to establishing this connection securely:

#### 1. Create a User for Replication

On the **primary server**, create a dedicated user for replication and grant it the necessary privileges:

```sql
CREATE USER 'backup_replica'@'replica_ip_or_hostname' IDENTIFIED BY 'strong_password';
GRANT REPLICATION SLAVE ON *.* TO 'backup_replica'@'replica_ip_or_hostname';
```

_(Optional: Confirm the grants by executing `SHOW GRANTS FOR 'backup_replica'@'replica_ip_or_hostname';`)_

#### 2. Obtain the GTID Position

On the primary server, obtain the current GTID position from which the replica should start replicating. If you want to start from the most recent transaction, query the `gtid_current_pos`:

```sql
SHOW GLOBAL VARIABLES LIKE 'gtid_current_pos';
```

#### 3. Configure the GTID Position on the Replica

On the replica server, configure the starting GTID position using the value obtained in the previous step:

SQL

```sql
SET GLOBAL gtid_slave_pos='<gtid_value_from_primary>';
```

#### 4. Configure Replication

On the replica server, configure the connection to the primary server using the `CHANGE MASTER TO` statement:

```sql
CHANGE MASTER TO
   MASTER_HOST='primary_domain_or_ip',
   MASTER_PORT=3306,
   MASTER_USER='backup_replica',
   MASTER_PASSWORD='strong_password',
   MASTER_SSL=1,
   MASTER_USE_GTID=slave_pos;
```

_(Note: Adjust the `MASTER_PORT`, `MASTER_SSL`, and add `MASTER_SSL_CA` parameters as necessary depending on your network and security configuration)._

#### 5. Start Replication

On the replica server, start the replication process:

```sql
START REPLICA;
```

#### 6. Check Replication Status

On the replica server, verify that replication is running smoothly:

```sql
SHOW REPLICA STATUS \G
```

Ensure that both `Slave_IO_Running` and `Slave_SQL_Running` are `Yes`. Once the replica is fully synced, you can safely pause it or run your backup tools (`mariadb-backup` or `mariadb-dump`) directly against this replica without affecting the primary server's performance.

## See Also

* [Replication](../../ha-and-performance/standard-replication/)
* [Replication Compatibility](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/mariadb-vs-mysql-compatibility#replication-compatibility)
* [Backup & Restore](./)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
