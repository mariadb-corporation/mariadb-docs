# Introduction to State Snapshot Transfers (SSTs)

In a State Snapshot Transfer (SST), the cluster provisions nodes by transferring a full data copy from one node to another. When a new node joins the cluster, the new node initiates a State Snapshot Transfer to synchronize its data with a node that is already part of the cluster.

## Types of SSTs

There are two conceptually different ways to transfer a state from one MariaDB server to another:

1. **Logical**: The only SST method of this type is the `mysqldump` SST method, which uses the [mysqldump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqldump) utility to get a logical dump of the donor. This SST method requires the joiner node to be fully initialized and ready to accept connections before the transfer. This method is, by definition, blocking, in that it blocks the donor node from modifying its state for the duration of the transfer. It is also the slowest of all, and that might be an issue in a cluster with a lot of loads.
2. **Physical**: SST methods of this type physically copy the data files from the donor node to the joiner node. This requires that the joiner node be initialized after the transfer. The [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup) SST method and a few other SST methods fall into this category. These SST methods are much faster than the `mysqldump` SST method, but they have certain limitations. For example, they can be used only on server startup, and the joiner node must be configured very similarly to the donor node (e.g., [innodb\_file\_per\_table](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_file_per_table) should be the same, and so on). Some of the SST methods in this category are non-blocking on the donor node, meaning that the donor node is still able to process queries while donating the SST (e.g. the [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup) SST method is non-blocking).

## SST Methods

SST methods are supported via a scriptable interface. New SST methods could potentially be developed by creating new SST scripts. The scripts usually have names of the form `wsrep_sst_<method>` where `<method>` is one of the SST methods listed below.

You can choose your SST method by setting the [wsrep\_sst\_method](../../reference/galera-cluster-system-variables.md#wsrep_sst_method) system variable. It can be changed dynamically with [SET GLOBAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set#global-session) on the node that you intend to be an SST donor. For example:

```sql
SET GLOBAL wsrep_sst_method='mariadb-backup';
```

It can also be set in a server [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#including-option-files) prior to starting up a node:

```ini
[mariadb]
...
wsrep_sst_method = mariadb-backup
```

For an SST to work properly, the donor and joiner node must use the same SST method. Therefore, it is recommended to set [wsrep\_sst\_method](../../reference/galera-cluster-system-variables.md#wsrep_sst_method) to the same value on all nodes, since any node will usually be a donor or joiner node at some point.

MariaDB Galera Cluster comes with the following built-in SST methods:

### mariadb-backup

This SST method uses the [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup) utility for performing SSTs. It is one of the two non-locking methods. This is the recommended SST method if you require the ability to run queries on the donor node during the SST. Note that if you use the `mariadb-backup` SST method, then you also need to have `socat` installed on the server. This is needed to stream the backup from the donor to the joiner. This is a limitation inherited from the `xtrabackup-v2` SST method.

* This SST method supports [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
* This SST method supports [Data at Rest Encryption](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview).
* This SST method is available from [MariaDB 10.1.26](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10126-release-notes) and [MariaDB 10.2.10](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10210-release-notes).

With this SST method, it is impossible to upgrade the cluster between some major versions; see [MDEV-27437](https://jira.mariadb.org/browse/MDEV-27437).

See [mariadb-backup SST method](mariadb-backup-sst-method.md) for more information.

### rsync / rsync\_wan

`rsync` is the default method. This method uses the [rsync](https://www.samba.org/rsync/) utility to create a snapshot of the donor node. `rsync` should be available by default on all modern Linux distributions. The donor node is blocked with a read lock during the SST. This is the fastest SST method, especially for large datasets since it copies binary data. Because of that, this is the recommended SST method if you do not need to allow the donor node to execute queries during the SST.

The `rsync` method runs `rsync` in `--whole-file` mode, assuming that nodes are connected by fast local network links so that the default delta transfer mode would consume more processing time than it may save on data transfer bandwidth. When having a distributed cluster with slow links between nodes, the `rsync_wan` method runs `rsync` in the default delta transfer mode, which may reduce data transfer time substantially when an older datadir state is already present on the joiner node. Both methods are actually implemented by the same script, `wsrep_sst_rsync_wan` is just a symlink to the `wsrep_sst_rsync` script and the actual `rsync` mode to use is determined by the name the script was called by.

* This SST method supports [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
* This SST method supports [Data at Rest Encryption](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview).

The rsync SST method does not support tables created with the [DATA DIRECTORY or INDEX DIRECTORY](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/tables/create-table#data-directory-index-directory) clause. Use the [mariadb-backup SST method](mariadb-backup-sst-method.md) as an alternative to support this feature.

{% tabs %}
{% tab title="Current" %}
Use of this SST method **could result in data corruption** when using [innodb\_use\_native\_aio](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_use_native_aio) (the default).
{% endtab %}

{% tab title="< 10.7.4 / 10.6.8 / 10.5.16 / 10.4.25 / 10.3.35" %}
Use of this SST method **could result in data corruption** when using [innodb\_use\_native\_aio](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/storage-engines/innodb/innodb-system-variables#innodb_use_native_aio) (the default). `wsrep_sst_method=rsync` is a reliable way to upgrade the cluster to a newer major version.
{% endtab %}
{% endtabs %}

{% tabs %}
{% tab title="Current" %}
[stunnel ](https://www.stunnel.org/)can be used to encrypt data over the wire. Be sure to have `stunnel` installed. You will also need to generate certificates and keys. See [the stunnel documentation](https://www.stunnel.org/howto.html) for information on how to do that. Once you have the keys, you will need to add the `tkey` and `tcert` options to the `[sst]` option group in your MariaDB configuration file, such as:

```ini
[sst]
tkey = /etc/my.cnf.d/certificates/client-key.pem
tcert = /etc/my.cnf.d/certificates/client-cert.pem
```

You also need to run the certificate directory through [openssl rehash](mariadb-backup-sst-method.md).
{% endtab %}

{% tab title="< 10.3.10 / 10.2.18 / 10.1.36" %}
[stunnel](https://www.stunnel.org) **cannot** be used to encrypt data over the wire.
{% endtab %}
{% endtabs %}

### mysqldump

This SST method runs [mysqldump](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqldump) on the donor node and pipes the output to the [mariadb](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/mariadb-client) client connected to the joiner node. The `mysqldump` SST method needs a username/password pair set in the [wsrep\_sst\_auth](../../reference/galera-cluster-system-variables.md#wsrep_sst_auth) variable in order to get the dump. The donor node is blocked with a read lock during the SST. This is the slowest SST method.

* This SST method supports [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid).
* This SST method supports [Data at Rest Encryption](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview).

### xtrabackup-v2

Percona XtraBackup is **not supported** in MariaDB. [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup) is the recommended backup method to use instead of Percona XtraBackup. See [Percona XtraBackup Overview: Compatibility with MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview#compatibility-with-mariadb) for more information.

This SST method uses the [Percona XtraBackup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup) utility for performing SSTs. It is one of the two non-blocking methods. Note that if you use the `xtrabackup-v2` SST method, you also need to have `socat` installed on the server. Since Percona XtraBackup is a third-party product, this SST method requires an additional installation and some additional configuration. Please refer to [Percona's xtrabackup SST documentation](https://www.percona.com/doc/percona-xtradb-cluster/5.7/manual/xtrabackup_sst.html) for information from the vendor.

* This SST method does **not** support [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
* This SST method does **not** support [Data at Rest Encryption](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview).

This SST method is available from MariaDB Galera Cluster 5.5.37 and MariaDB Galera Cluster 10.0.10.

See xtrabackup-v2 SST method for more information.

### xtrabackup

Percona XtraBackup is **not supported** in MariaDB. [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup) is the recommended backup method to use instead of Percona XtraBackup. See [Percona XtraBackup Overview: Compatibility with MariaDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup/percona-xtrabackup-overview#compatibility-with-mariadb) for more information.

This SST method is an older SST method that uses the [Percona XtraBackup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup) utility for performing SSTs. The `xtrabackup-v2` SST method should be used instead of the `xtrabackup` SST method starting from [MariaDB 5.5.33](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-5-5-series/mariadb-5533-release-notes).

* This SST method does **not** support [GTID](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid)
* This SST method does **not** support [Data at Rest Encryption](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview).

## Authentication

All SST methods except `rsync` require authentication via username and password. You can tell the client what username and password to use by setting the [wsrep\_sst\_auth](../../reference/galera-cluster-system-variables.md#wsrep_sst_auth) system variable. It can be changed dynamically with [SET GLOBAL](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set#global-session) on the node that you intend to be a SST donor. For example:

```
SET GLOBAL wsrep_sst_auth = 'mariadb-backup:password';
```

It can also be set in a server [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files) prior to starting up a node:

```
[mariadb]
...
wsrep_sst_auth = mariadb-backup:password
```

Some [authentication plugins](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins) do not require a password. For example, the [unix\_socket](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-unix-socket) and [gssapi](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi) authentication plugins do not require a password. If you are using a user account that does not require a password in order to log in, then you can just leave the password component of [wsrep\_sst\_auth](../../reference/galera-cluster-system-variables.md#wsrep_sst_auth) empty. For example:

```
[mariadb]
...
wsrep_sst_auth = mariadb-backup:
```

See the relevant description or page for each SST method to find out what privileges need to be [granted](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant) to the user and whether the privileges are needed on the donor node or joiner node for that method.

## SSTs and Systemd

MariaDB's [systemd](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/systemd) unit file has a default startup timeout of about 90 seconds on most systems. If an SST takes longer than this default startup timeout on a joiner node, then `systemd` will assume that `mysqld` has failed to startup, which causes `systemd` to kill the `mysqld` process on the joiner node. To work around this, you can reconfigure the MariaDB `systemd` unit to have an infinite timeout, such as by executing one of the following commands:

If you are using `systemd` 228 or older, then you can execute the following to set an infinite timeout:

```
sudo tee /etc/systemd/system/mariadb.service.d/timeoutstartsec.conf <<EOF
[Service]

TimeoutStartSec=0
EOF
sudo systemctl daemon-reload
```

[Systemd 229 added the infinity option](https://lists.freedesktop.org/archives/systemd-devel/2016-February/035748.html), so if you are using `systemd` 229 or later, then you can execute the following to set an infinite timeout:

```
sudo tee /etc/systemd/system/mariadb.service.d/timeoutstartsec.conf <<EOF
[Service]

TimeoutStartSec=infinity
EOF
sudo systemctl daemon-reload
```

See [Configuring the Systemd Service Timeout](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/getting-installing-and-upgrading-mariadb/starting-and-stopping-mariadb/systemd#configuring-the-systemd-service-timeout) for more details.

Note that [systemd 236 added the EXTEND\_TIMEOUT\_USEC environment variable](https://lists.freedesktop.org/archives/systemd-devel/2017-December/039996.html) that allows services to extend the startup timeout during long-running processes. Starting with [MariaDB 10.1.35](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-1-series/mariadb-10135-release-notes), [MariaDB 10.2.17](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-2-series/mariadb-10217-release-notes), and [MariaDB 10.3.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-3-series/mariadb-1038-release-notes), on systems with systemd versions that support it, MariaDB uses this feature to extend the startup timeout during long SSTs. Therefore, if you are using `systemd` 236 or later, then you should not need to manually override `TimeoutStartSec`, even if your SSTs run for longer than the configured value. See [MDEV-15607](https://jira.mariadb.org/browse/MDEV-15607) for more information.

## SST Failure

An SST failure generally renders the joiner node unusable. Therefore, when an SST failure is detected, the joiner node will abort.

Restarting a node after a `mysqldump` SST failure may require manual restoration of the administrative tables.

## SSTs and Data at Rest Encryption

Look at the description of each SST method to determine which methods support [Data at Rest Encryption](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview).

For logical SST methods like `mysqldump`, each node should be able to have different [encryption keys](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview). For physical SST methods, all nodes need to have the same [encryption keys](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/encryption/data-at-rest-encryption/data-at-rest-encryption-overview), since the donor node will copy encrypted data files to the joiner node, and the joiner node will need to be able to decrypt them.

## Minimal Cluster Size

In order to avoid a split-brain condition, the minimum recommended number of nodes in a cluster is 3.

When using an SST method that blocks the donor, there is yet another reason to require a minimum of 3 nodes. In a 3-node cluster, if one node is acting as an SST joiner and one other node is acting as an SST donor, then there is still one more node to continue executing queries.

## Manual SSTs

In some cases, if Galera Cluster's automatic SSTs repeatedly fail, then it can be helpful to perform a "manual SST". See the following pages on how to do that:

* [Manual SST of Galera Cluster node with mariadb-backup](manual-sst-of-galera-cluster-node-with-mariadb-backup.md)
* [Manual SST of Galera Cluster node with Percona XtraBackup](manual-sst-of-galera-cluster-node-with-mariadb-backup.md)

## Known Issues

### mysqld\_multi

SST scripts can't currently read the mysqld<#> [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files) that are read by instances managed by [mysqld\_multi](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/mysqld_multi).

See [MDEV-18863](https://jira.mariadb.org/browse/MDEV-18863) for more information.

## See Also

* [Galera Cluster documentation: STATE SNAPSHOT TRANSFERS](https://galeracluster.com/library/documentation/sst.html)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
