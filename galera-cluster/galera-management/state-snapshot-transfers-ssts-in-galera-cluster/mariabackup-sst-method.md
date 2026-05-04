---
description: >-
  The mariadb-backup SST method performs non-blocking Galera SSTs, configured
  via wsrep_sst_method and wsrep_sst_auth, with socat required to stream the
  backup between donor and joiner nodes.
---

# mariadb-backup SST Method

The `mariadb-backup` SST method uses the [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backing-up-and-restoring-databases/mariadb-backup) utility for performing SSTs. It is one of the methods that does not block the donor node. [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backing-up-and-restoring-databases/mariadb-backup) was originally forked from [Percona XtraBackup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup), and similarly, the `mariadb-backup` SST method was originally forked from the `[xtrabackup-v2]` SST method.

Note that if you use the `mariadb-backup` SST method, then you also need to have [socat](#socat-dependency) installed on the server. This is needed to stream the backup from the donor node to the joiner node. This is a limitation that was inherited from the `[xtrabackup-v2]` SST method.

## Choosing mariadb-backup for SSTs

To use the `mariadb-backup` SST method, you must set the [`wsrep_sst_method=mariadb-backup`](../../reference/galera-cluster-system-variables.md#wsrep_sst_method) on both the donor and joiner node. It can be changed dynamically with [`SET GLOBAL`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set#global-session) on the node that you intend to be a SST donor. For example:

```
SET GLOBAL wsrep_sst_method='mariadb-backup';
```

It can be set in a server [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files) prior to starting up a node:

```
[mariadb]
...
wsrep_sst_method = mariadb-backup
```

For an SST to work properly, the donor and joiner node must use the same SST method. Therefore, it is recommended to set [`wsrep_sst_method`](../../reference/galera-cluster-system-variables.md#wsrep_sst_method) to the same value on all nodes, since any node will usually be a donor or joiner node at some point.

## Major version upgrades

The InnoDB redo log format has been changed in [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-5-series/what-is-mariadb-105) and [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108) in a way that will not allow the crash recovery or the preparation of a backup from an older major version. Because of this, the `mariadb-backup` SST method cannot be used for some major version upgrades, unless you temporarily edit the `wsrep_sst_mariadb-backup` script so that the `--prepare` step on the newer-major-version joiner will be executed using the older-major-version `mariadb-backup` tool.

The default method `wsrep_sst_method=rsync` will work for major version upgrades; see [MDEV-27437](https://jira.mariadb.org/browse/MDEV-27437).

## Authentication and Privileges

To use the `mariadb-backup` SST method, [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backing-up-and-restoring-databases/mariadb-backup) needs to be able to authenticate locally on the donor node, so that it can create a backup to stream to the joiner. You can tell the donor node what username and password to use by setting the [`wsrep_sst_auth`](../../reference/galera-cluster-system-variables.md#wsrep_sst_auth) system variable. It can be changed dynamically with [`SET GLOBAL`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set#global-session) on the node that you intend to be a SST donor. For example:

```
SET GLOBAL wsrep_sst_auth = 'mariadb-backup:mypassword';
```

It can also be set in a server [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files) prior to starting up a node:

```
[mariadb]
...
wsrep_sst_auth = mariadb-backup:mypassword
```

Some [authentication plugins](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins) do not require a password. For example, the [`unix_socket`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-unix-socket) and [`gssapi`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi) authentication plugins do not require a password. If you are using a user account that does not require a password in order to log in, then you can just leave the password component of [`wsrep_sst_auth`](../../reference/galera-cluster-system-variables.md#wsrep_sst_auth) empty. For example:

```
[mariadb]
...
wsrep_sst_auth = mariadb-backup:
```

The user account that performs the backup for the SST needs to have [the same privileges as mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backing-up-and-restoring-databases/mariadb-backup/mariadb-backup-overview#authentication-and-privileges), which are the `RELOAD` , `PROCESS`, `LOCK TABLES` and `BINLOG MONITOR`, `REPLICA MONITOR` [global privileges](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant#global-privileges). To be safe, you should ensure that these privileges are set on each node in your cluster. [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backing-up-and-restoring-databases/mariadb-backup) connects locally on the donor node to perform the backup, so the following user should be sufficient:

```
CREATE USER 'mariadb-backup'@'localhost' IDENTIFIED BY 'mypassword';
GRANT RELOAD, PROCESS, LOCK TABLES, BINLOG MONITOR ON *.* TO 'mariadb-backup'@'localhost';
```

### Passwordless Authentication - Unix Socket

It is possible to use the [`unix_socket`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-unix-socket) authentication plugin for the user account that performs SSTs. This would provide the benefit of not needing to configure a plain-text password in [`wsrep_sst_auth`](../../reference/galera-cluster-system-variables.md#wsrep_sst_auth).

The user account would have to have the same name as the operating system user account that is running the `mysqld` process. On many systems, this is the user account configured as the [`user`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options#user) option, and it tends to default to `mysql`.

For example, if the [`unix_socket`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-unix-socket) authentication plugin is already installed, then you could execute the following to create the user account:

```
CREATE USER 'mysql'@'localhost' IDENTIFIED VIA unix_socket;
GRANT RELOAD, PROCESS, LOCK TABLES, REPLICATION CLIENT ON *.* TO 'mysql'@'localhost';
```

And then to configure [`wsrep_sst_auth`](../../reference/galera-cluster-system-variables.md#wsrep_sst_auth), you could set the following in a server [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files)  prior to starting up a node:

```
[mariadb]
...
wsrep_sst_auth = mysql:
```

### Passwordless Authentication - GSSAPI

It is possible to use the [`gssapi`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi) authentication plugin for the user account that performs SSTs. This would provide the benefit of not needing to configure a plain-text password in [`wsrep_sst_auth`](../../reference/galera-cluster-system-variables.md#wsrep_sst_auth).

The following steps would need to be done beforehand:

* You need a KDC running [MIT Kerberos](https://web.mit.edu/Kerberos/krb5-1.12/doc/index.html) or [Microsoft Active Directory](https://docs.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview).
* You will need to [create a keytab file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi#creating-a-keytab-file-on-a-unix-server) for the MariaDB server.
* You will need to [install the package](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi#installing-the-plugins-package) containing the [`gssapi`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi) authentication plugin.
* You will need to [install the plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi#installing-the-plugin) in MariaDB, so that the [`gssapi`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi) authentication plugin is available to use.
* You will need to [configure the plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi#configuring-the-plugin).
* You will need to [create a user account](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi#creating-users) that authenticates with the [`gssapi`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi) authentication plugin, so that the user account can be used for SSTs. This user account will need to correspond with a user account that exists on the backend KDC.

For example, you could execute the following to create the user account in MariaDB:

```
CREATE USER 'mariadb-backup'@'localhost' IDENTIFIED VIA gssapi;
GRANT RELOAD, PROCESS, LOCK TABLES, BINLOG MONITOR ON *.* TO 'mariadb-backup'@'localhost';
```

And then to configure [`wsrep_sst_auth`](../../reference/galera-cluster-system-variables.md#wsrep_sst_auth), you could set the following in a server [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files)  prior to starting up a node:

```
[mariadb]
...
wsrep_sst_auth = mariadb-backup:
```

## Choosing a Donor Node

When mariadb-backup is used to create the backup for the SST on the donor node, mariadb-backup briefly requires a system-wide lock at the end of the backup. This is done with [`BACKUP STAGE BLOCK_COMMIT`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/backup-commands/backup-stage).

If a specific node in your cluster is acting as the _primary_ node by receiving all of the application's write traffic, then this node should not usually be used as the donor node, because the system-wide lock could interfere with the application. In this case, you can define one or more preferred donor nodes by setting the [`wsrep_sst_donor`](../../reference/galera-cluster-system-variables.md#wsrep_sst_donor) system variable.

For example, let's say that we have a 5-node cluster with the nodes `node1`, `node2`, `node3`, `node4`, and `node5`, and let's say that `node1` is acting as the _primary_ node. The preferred donor nodes for `node2` could be configured by setting the following in a server [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files) prior to starting up a node:

```
[mariadb]
...
wsrep_sst_donor=node3,node4,node5,
```

The trailing comma tells the server to allow any other node as donor when the preferred donors are not available. Therefore, if `node1` is the only node left in the cluster, the trailing comma allows it to be used as the donor node.

## Socat Dependency

During the SST process, the donor node uses [socat](https://www.dest-unreach.org/socat/doc/socat.html) to stream the backup to the joiner node. Then the joiner node prepares the backup before restoring it. The socat utility must be installed on both the donor node and the joiner node in order for this to work. Otherwise, the MariaDB error log will contain an error like:

```
WSREP_SST: [ERROR] socat not found in path: /usr/sbin:/sbin:/usr//bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin (20180122 14:55:32.993)
```

### Installing Socat on RHEL/CentOS

On RHEL/CentOS, `socat` can be installed from the [Extra Packages for Enterprise Linux (EPEL)](https://fedoraproject.org/wiki/EPEL) repository.

## TLS

This SST method supports two different TLS methods. The specific method can be selected by setting the `encrypt` option in the `[sst]` section of the MariaDB configuration file. The options are:

* TLS using OpenSSL encryption built into `socat` (`encrypt=2`)
* TLS using OpenSSL encryption with Galera-compatible certificates and keys (`encrypt=3`)

Note that `encrypt=1` refers to a TLS encryption method that has been deprecated and removed. `encrypt=4` refers to a TLS encryption method in `xtrabackup-v2` that has not yet been ported to `mariadb-backup`. See [MDEV-18050](https://jira.mariadb.org/browse/MDEV-18050) about that.

### TLS Using OpenSSL Encryption Built into Socat

To generate keys compatible with this encryption method, you can follow [these directions](https://www.dest-unreach.org/socat/doc/socat-openssltunnel.html).

For example:

* First, generate the keys and certificates:

```
FILENAME=sst
openssl genrsa -out $FILENAME.key 1024
openssl req -new -key $FILENAME.key -x509 -days 3653 -out $FILENAME.crt
cat $FILENAME.key $FILENAME.crt >$FILENAME.pem
chmod 600 $FILENAME.key $FILENAME.pem
```

* On some systems, you may also have to add dhparams to the certificate:

```
openssl dhparam -out dhparams.pem 2048
cat dhparams.pem >> sst.pem
```

* Then, copy the certificate and keys to all nodes in the cluster.
* Then, configure the following on all nodes in the cluster:

```
[sst]
encrypt=2
tca=/etc/my.cnf.d/certificates/sst.crt
tcert=/etc/my.cnf.d/certificates/sst.pem
```

But replace the paths with whatever is relevant on your system.

This should allow your SSTs to be encrypted.

### TLS Using OpenSSL Encryption with Galera-compatible Certificates and Keys

To generate keys compatible with this encryption method, you can follow [these directions](https://galeracluster.com/library/documentation/ssl-cert.html).

For example:

* First, generate the keys and certificates:

```
# CA
openssl genrsa 2048 > ca-key.pem
openssl req -new -x509 -nodes -days 365000 \
-key ca-key.pem -out ca-cert.pem
 
# server1
openssl req -newkey rsa:2048 -days 365000 \
-nodes -keyout server1-key.pem -out server1-req.pem
openssl rsa -in server1-key.pem -out server1-key.pem
openssl x509 -req -in server1-req.pem -days 365000 \
-CA ca-cert.pem -CAkey ca-key.pem -set_serial 01 \
-out server1-cert.pem
```

* Then, copy the certificate and keys to all nodes in the cluster.
* Then, configure the following on all nodes in the cluster:

```
[sst]
encrypt=3
tkey=/etc/my.cnf.d/certificates/server1-key.pem
tcert=/etc/my.cnf.d/certificates/server1-cert.pem
```

But replace the paths with whatever is relevant on your system.

This should allow your SSTs to be encrypted.

## Logs

The `mariadb-backup` SST method has its own logging outside of the MariaDB Server logging.

### Logging to SST Logs

Logging for `mariadb-backup` SSTs works the following way.

By default, on the donor node, it logs to `mariadb-backup.backup.log`. This log file is located in the [`datadir`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#datadir).

By default, on the joiner node, it logs to `mariadb-backup.prepare.log` and `mariadb-backup.move.log` These log files are also located in the [`datadir`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/optimization-and-tuning/system-variables/server-system-variables#datadir).

By default, before a new SST is started, existing `mariadb-backup` SST log files are compressed and moved to `/tmp/sst_log_archive`. This behavior can be disabled by setting `sst-log-archive=0` in the `[sst]`  [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files).  Similarly, the archive directory can be changed by setting `sst-log-archive-dir`. For example:

```
[sst]
sst-log-archive=1
sst-log-archive-dir=/var/log/mysql/sst/
```

See [MDEV-17973](https://jira.mariadb.org/browse/MDEV-17973) for more information.\
<>

### Logging to Syslog

You can redirect the SST logs to the syslog instead by setting the following in the `[sst]`  [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files):

```
[sst]
sst-syslog=1
```

You can also redirect the SST logs to the syslog by setting the following in the `[mysqld_safe]`  [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files) :

```
[mysqld_safe]
syslog
```

## Performing SSTs with IPv6 Addresses

If you are performing mariadb-backup SSTs with IPv6 addresses, then the `socat` utility needs to be passed the `pf=ip6` option. This can be done by setting the `sockopt` option in the `[sst]`  [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files). For example:

```
[sst]
sockopt=",pf=ip6"
```

See [MDEV-18797](https://jira.mariadb.org/browse/MDEV-18797) for more information.

## Manual SST with mariadb-backup

In some cases, if Galera Cluster's automatic SSTs repeatedly fail, then it can be helpful to perform a "manual SST". See the following page on how to do that:

* [Manual SST of Galera Cluster node with mariadb-backup](manual-sst-of-galera-cluster-node-with-mariadb-backup.md)

## See Also

* [Percona XtraBackup SST Configuration](https://www.percona.com/doc/percona-xtradb-cluster/5.7/manual/xtrabackup_sst.html)
* [Encrypting PXC Traffic:\
  ENCRYPTING SST TRAFFIC](https://www.percona.com/doc/percona-xtradb-cluster/5.7/security/encrypt-traffic.html#encrypt-sst)
* [XTRABACKUP PARAMETERS](https://galeracluster.com/library/documentation/xtrabackup-options.html)
* [SSL FOR STATE SNAPSHOT TRANSFERS: ENABLING SSL FOR XTRABACKUP](https://galeracluster.com/library/documentation/ssl-sst.html#ssl-xtrabackup)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
