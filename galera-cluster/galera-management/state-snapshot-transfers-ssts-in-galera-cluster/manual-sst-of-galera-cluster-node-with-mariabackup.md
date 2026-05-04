---
description: >-
  Perform a manual State Snapshot Transfer using mariadb-backup when an
  automatic Galera SST fails, by backing up the donor, restoring it on the
  joiner, and editing the cluster state.
---

# Manual SST of Galera Cluster Node With mariadb-backup

Sometimes it can be helpful to perform a "manual SST" when Galera's [normal SSTs](introduction-to-state-snapshot-transfers-ssts.md) fail. This can be especially useful when the cluster's [datadir](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables#datadir) is very large, since a normal SST can take a long time to fail in that case.

A manual SST essentially consists of taking a backup of the donor, loading the backup on the joiner, and then manually editing the cluster state on the joiner node. This page will show how to perform this process with [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariadb-backup).

## Process

* Check that the donor and joiner nodes have the same mariadb-backup version.

```
mariadb-backup --version
```

* Create backup directory on donor.

```
MYSQL_BACKUP_DIR=/mysql_backup
mkdir $MYSQL_BACKUP_DIR
```

* Take a [full backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariadb-backup/full-backup-and-restore-with-mariadb-backup) the of the donor node with `mariadb-backup`. The [--galera-info](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariadb-backup/mariadb-backup-options#-galera-info) option should also be provided, so that the node's cluster state is also backed up.

```
DB_USER=sstuser
DB_USER_PASS=password
mariadb-backup --backup  --galera-info \
   --target-dir=$MYSQL_BACKUP_DIR \
   --user=$DB_USER \
   --password=$DB_USER_PASS
```

* Verify that the MariaDB Server process is stopped on the joiner node. This will depend on your [service manager](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/running-multiple-mariadb-server-processes#service-managers).

For example, on [systemd](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/systemd) systems, you can execute::

```
systemctl status mariadb
```

* Create the backup directory on the joiner node.

```
MYSQL_BACKUP_DIR=/mysql_backup
mkdir $MYSQL_BACKUP_DIR
```

* Copy the backup from the donor node to the joiner node.

```
OS_USER=dba
JOINER_HOST=dbserver2.mariadb.com
rsync -av $MYSQL_BACKUP_DIR/* ${OS_USER}@${JOINER_HOST}:${MYSQL_BACKUP_DIR}
```

* [Prepare the backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariadb-backup/full-backup-and-restore-with-mariadb-backup#preparing-the-backup) on the joiner node.

```
mariadb-backup --prepare \
   --target-dir=$MYSQL_BACKUP_DIR
```

* Get the Galera Cluster version ID from the donor node's `grastate.dat` file.

```
MYSQL_DATADIR=/var/lib/mysql
cat $MYSQL_DATADIR/grastate.dat | grep version
```

For example, a very common version number is "2.1".

* Get the node's cluster state from the [xtrabackup_galera_info](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/backing-up-and-restoring-databases/mariadb-backup/mariadb-backup-options#-galera-info) file in the backup that was copied to the joiner node.

```
cat $MYSQL_BACKUP_DIR/xtrabackup_galera_info
```

The file contains the values of the [wsrep_local_state_uuid](../../reference/galera-cluster-status-variables.md#wsrep_local_state_uuid) and [wsrep_last_committed](../../reference/galera-cluster-status-variables.md#wsrep_last_committed) status variables.

The values are written in the following format:

```
wsrep_local_state_uuid:wsrep_last_committed
```

For example:

```
d38587ce-246c-11e5-bcce-6bbd0831cc0f:1352215
```

* Create a `grastate.dat` file in the backup directory of the joiner node. The Galera Cluster version ID, the cluster uuid, and the seqno from previous steps will be used to fill in the relevant fields.

For example, with the example values from the last two steps, we could do:

```
sudo tee $MYSQL_BACKUP_DIR/grastate.dat <<EOF
# GALERA saved state
version: 2.1
uuid:    d38587ce-246c-11e5-bcce-6bbd0831cc0f
seqno:   1352215
safe_to_bootstrap: 0
EOF
```

* Remove the existing contents of the [datadir](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables#datadir) on the joiner node.

```
MYSQL_DATADIR=/var/lib/mysql
rm -Rf $MYSQL_DATADIR/*
```

* Copy the contents of the backup directory to the [datadir](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables#datadir) the on joiner node.

```
mariadb-backup --copy-back \
   --target-dir=$MYSQL_BACKUP_DIR
```

* Make sure the permissions of the [datadir](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/replication-cluster-multi-master/optimization-and-tuning/system-variables/server-system-variables#datadir) are correct on the joiner node.

```
chown -R mysql:mysql $MYSQL_DATADIR/
```

* Start the MariaDB Server process on the joiner node. This will depend on your [service manager](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/running-multiple-mariadb-server-processes#service-managers).

For example, on [systemd](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/systemd) systems, you can execute::

```
systemctl start mariadb
```

* Watch the MariaDB [error log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/error-log) on the joiner node and verify that the node does not need to perform a [normal SSTs](introduction-to-state-snapshot-transfers-ssts.md) due to the manual SST.

```
tail -f /var/log/mysql/mysqld.log
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
