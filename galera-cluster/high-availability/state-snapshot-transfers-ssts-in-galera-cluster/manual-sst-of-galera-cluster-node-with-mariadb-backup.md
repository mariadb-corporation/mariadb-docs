---
description: >-
  Perform a manual node provision. This guide details the steps to manually
  backup a donor and restore it to a joiner node in a Galera Cluster.
---

# Manual SST of Galera Cluster Node With mariadb-backup

Sometimes it can be helpful to perform a "manual SST" when Galera's [normal SSTs](introduction-to-state-snapshot-transfers-ssts.md) fail. This can be especially useful when the cluster's [`datadir`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#datadir) is very large, since a normal SST can take a long time to fail in that case.

A manual SST essentially consists of taking a backup of the donor, loading the backup on the joiner, and then manually editing the cluster state on the joiner node. This page will show how to perform this process with [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup).

## Process <a href="#process" id="process"></a>

{% stepper %}
{% step %}
### Check the nodes

Ensure the donor and joiner nodes have the same `mariadb-backup` version.

```bash
mariadb-backup --version
```
{% endstep %}

{% step %}
### Create backup directory on donor

```bash
MYSQL_BACKUP_DIR=/mysql_backup
mkdir $MYSQL_BACKUP_DIR
```
{% endstep %}

{% step %}
### Take backup

Take a full backup the of the donor node with `mariadb-backup`. The --galera-info option should also be provided, so that the node's cluster state is also backed up.

```bash
DB_USER=sstuser
DB_USER_PASS=password
mariadb-backup --backup  --galera-info \
   --target-dir=$MYSQL_BACKUP_DIR \
   --user=$DB_USER \
   --password=$DB_USER_PASS
```
{% endstep %}

{% step %}
### MariaDB Server process running

Verify that the MariaDB Server process is stopped on the joiner node. This will depend on your [service manager](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb).

For example, on [systemd](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/systemd) systems, you can execute::

```bash
systemctl status mariadb
```
{% endstep %}

{% step %}
### Create the backup directory on the joiner node.

```bash
MYSQL_BACKUP_DIR=/mysql_backup
mkdir $MYSQL_BACKUP_DIR
```
{% endstep %}

{% step %}
### Copy backup

Copy the backup from the donor node to the joiner node.

{% code overflow="wrap" %}
```bash
OS_USER=dba
JOINER_HOST=dbserver2.mariadb.com
rsync -av $MYSQL_BACKUP_DIR/* ${OS_USER}@${JOINER_HOST}:${MYSQL_BACKUP_DIR}
```
{% endcode %}
{% endstep %}

{% step %}
### Prepare backup

[Prepare the backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/full-backup-and-restore-with-mariadb-backup#preparing-the-backup-for-restoration) on the joiner node.

```bash
mariadb-backup --prepare \
   --target-dir=$MYSQL_BACKUP_DIR
```
{% endstep %}

{% step %}
### Get the ID

Get the Galera Cluster version ID from the donor node's `grastate.dat` file.

```bash
MYSQL_DATADIR=/var/lib/mysql
cat $MYSQL_DATADIR/grastate.dat | grep version
```
{% endstep %}
{% endstepper %}

For example, a very common version number is "2.1".

{% stepper %}
{% step %}
### Get the node's cluster state

Get the state from the Galera info file in the backup that was copied to the joiner node.

The name of this file depends on the MariaDB version:

* MariaDB 11.4 and later: `mariadb_backup_galera_info`
* MariaDB 11.3 and earlier: `xtrabackup_galera_info`

For MariaDB 11.4 and later:

```bash
cat $MYSQL_BACKUP_DIR/mariadb_backup_galera_info
```

For MariaDB 11.3 and earlier:

```bash
cat $MYSQL_BACKUP_DIR/xtrabackup_galera_info
```

The file contains the values of the [wsrep\_local\_state\_uuid](../../reference/galera-cluster-status-variables.md#wsrep_local_state_uuid) and [wsrep\_last\_committed](../../reference/galera-cluster-status-variables.md#wsrep_last_committed) status variables. The values are written in the following format:

```ini
wsrep_local_state_uuid:wsrep_last_committed
```

For example:

```uri
d38587ce-246c-11e5-bcce-6bbd0831cc0f:1352215
```
{% endstep %}

{% step %}
### Create a `grastate.dat` file

Create the file in the backup directory of the joiner node. The Galera Cluster version ID, the cluster uuid, and the seqno from previous steps will be used to fill in the relevant fields.

For example, with the example values from the last two steps, we could do:

```bash
sudo tee $MYSQL_BACKUP_DIR/grastate.dat <<EOF
# GALERA saved state
version: 2.1
uuid:    d38587ce-246c-11e5-bcce-6bbd0831cc0f
seqno:   1352215
safe_to_bootstrap: 0
EOF
```
{% endstep %}

{% step %}
### Remove contents

Remove the existing contents of the [`datadir`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#datadir) on the joiner node.

```bash
MYSQL_DATADIR=/var/lib/mysql
rm -Rf $MYSQL_DATADIR/*
```
{% endstep %}

{% step %}
### Copy contents

Copy the contents of the backup directory to the [`datadir`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#datadir) the on joiner node.

```bash
mariadb-backup --copy-back \
   --target-dir=$MYSQL_BACKUP_DIR
```
{% endstep %}

{% step %}
### Check `datadir` permissions

Make sure the permissions of the [`datadir`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#datadir) are correct on the joiner node.

```bash
chown -R mysql:mysql $MYSQL_DATADIR/
```
{% endstep %}

{% step %}
### Start the MariaDB Server process on the joiner node.&#x20;

This will depend on your [service manager](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb). For example, on [systemd](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/systemd) systems, you may execute::

```bash
systemctl start mariadb
```
{% endstep %}

{% step %}
### Watch the MariaDB [error log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/server-monitoring-logs/error-log)&#x20;

On the joiner node, verify that the node does not need to perform a [normal SSTs](introduction-to-state-snapshot-transfers-ssts.md) due to the manual SST.

```bash
tail -f /var/log/mysql/mysqld.log
```
{% endstep %}
{% endstepper %}
