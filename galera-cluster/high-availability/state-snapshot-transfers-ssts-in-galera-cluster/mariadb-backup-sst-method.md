---
description: >-
  Configure State Snapshot Transfers for Galera. Learn to use mariadb-backup for
  non-blocking data transfer when a new node joins a cluster.
---

# mariadb-backup SST Method

The `mariabackup` SST method uses the [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup) utility for performing SSTs. It is one of the methods that does not block the donor node. `mariadb-backup` was originally forked from [Percona XtraBackup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/clients-and-utilities/legacy-clients-and-utilities/backing-up-and-restoring-databases-percona-xtrabackup), and similarly, the `mariabackup` SST method was originally forked from the xtrabackup-v2 SST method.

{% hint style="warning" %}
If you use the `mariadb-backup` SST method, then you also need to have [socat](mariadb-backup-sst-method.md#socat-dependency) installed on the server. This is needed to stream the backup from the donor node to the joiner node. This is a limitation that was inherited from the xtrabackup-v2 SST method.
{% endhint %}

## Choosing mariadb-backup for SSTs <a href="#choosing-mariabackup-for-ssts" id="choosing-mariabackup-for-ssts"></a>

To use the mariadb-backup SST method, you must set the [`wsrep_sst_method=mariabackup`](../../reference/wsrep-variable-details/wsrep_sst_method.md) on both the donor and joiner node. It can be changed dynamically with [`SET GLOBAL`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/set-commands/set) on the node that you intend to be an SST donor. For example:

```sql
SET GLOBAL wsrep_sst_method='mariabackup';
```

It can be set in a server [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files) prior to starting up a node:

```ini
[mariadb]
...
wsrep_sst_method = mariabackup
```

For an SST to work properly, the donor and joiner node must use the same SST method. Therefore, it is recommended to set [`wsrep_sst_method`](../../reference/wsrep-variable-details/wsrep_sst_method.md) to the same value on all nodes, since any node will usually be a donor or joiner node at some point.

## Major Version Upgrades <a href="#major-version-upgrades" id="major-version-upgrades"></a>

{% hint style="warning" %}
The InnoDB redo log format has been changed in [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105) and [MariaDB 10.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-8-series/what-is-mariadb-108) in a way that will not allow the crash recovery or the preparation of a backup from an older major version. Because of this, the `mariabackup` SST method cannot be used for some major-version upgrades, unless you temporarily edit the `wsrep_sst_mariadbbackup` script so that the `--prepare` step on the newer-major-version joiner will be executed using the older-major-version `mariadb-backup` tool.
{% endhint %}

The default method `wsrep_sst_method=rsync` works for major-version upgrades; see [MDEV-27437](https://jira.mariadb.org/browse/MDEV-27437).

## Configuration Options

The `mariabackup` SST method is configured by placing options in the `[sst]` section of a MariaDB configuration file (e.g., `/etc/my.cnf.d/server.cnf`). These settings are parsed by the `wsrep_sst_mariabackup` and `wsrep_sst_common` scripts.

{% hint style="success" %}
The command-line utility is `mariadb-backup`; this tool was previously called `mariabackup`. The SST method itself retains the original name `mariabackup` (as in `wsrep_sst_method=mariabackup`).
{% endhint %}

### Primary Transfer and Format Options

These options control the core data transfer mechanism.

| Option        | Default Value | Description                                                                                  |
| ------------- | ------------- | -------------------------------------------------------------------------------------------- |
| `streamfmt`   | `mbstream`    | Specifies the backup streaming format. `mbstream` is the native format for `mariadb-backup`. |
| `transferfmt` | `socat`       | Defines the network utility for data transfer.                                               |
| `sockopt`     |               | A string of socket options passed to the `socat` utility.                                    |
| `rlimit`      |               | Throttles the data transfer rate in bytes per second. Supports `K`, `M`, and `G` suffixes.   |

### Compression Options

These options configure on-the-fly compression to reduce network bandwidth.

| Option         | Description                                                                                 |
| -------------- | ------------------------------------------------------------------------------------------- |
| `compressor`   | The command-line string for compressing the data stream on the donor (e.g., `"lz4 -z"`).    |
| `decompressor` | The command-line string for decompressing the data stream on the joiner (e.g., `"lz4 -d"`). |

### Authentication and Security (TLS)

These options manage user authentication and stream encryption.

| Option           | Description                                                                                                                                     |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `wsrep-sst-auth` | The authentication string in `user:password` format. The user requires `RELOAD`, `PROCESS`, `LOCK TABLES`, and `REPLICATION CLIENT` privileges. |
| `tcert`          | Path to the TLS certificate file for securing the transfer.                                                                                     |
| `tkey`           | Path to the TLS private key file.                                                                                                               |
| `tca`            | Path to the TLS Certificate Authority (CA) file.                                                                                                |

### Logging and Miscellaneous Options

| Option                | Default Value | Description                                                                     |
| --------------------- | ------------- | ------------------------------------------------------------------------------- |
| `progress`            |               | Set to `1` to show transfer progress (requires `pv` utility).                   |
| `sst-initial-timeout` | `300`         | Timeout in seconds for the initial connection.                                  |
| `sst-log-archive`     | `1`           | Set to `1` to archive the previous SST log.                                     |
| `cpat`                |               | A space-separated list of extra files/directories to copy from donor to joiner. |

### Pass-through `mariadb-backup` Options

This feature allows `mariadb-backup` specific options to be passed through the SST script.

| Option      | Default Value | Description                                              |
| ----------- | ------------- | -------------------------------------------------------- |
| `use-extra` | `0`           | Must be set to `1` to enable pass-through functionality. |

### **Example: Using Native Encryption and Threading**

```ini
[sst]
# Enable pass-through functionality
use-extra=1

# mariadb-backup native options
encrypt=AES256
encrypt-key-file=/etc/mysql/encrypt/keyfile.key
compress-threads=4
```

## Authentication and Privileges <a href="#authentication-and-privileges" id="authentication-and-privileges"></a>

To use the `mariadb-backup` SST method, the utility must be able to authenticate locally on the donor node to create a backup stream. There are two ways to manage this authentication:

### Automatic User Account Management (ES 11.4+)

Starting with MariaDB Enterprise Server 11.4, the cluster can automatically manage the SST user account. This method is more secure and requires less configuration because it avoids storing plain-text passwords in configuration files.

When this feature is used:

1. The donor node automatically creates a temporary internal user (e.g., `'wsrep.sst. <timestamp>_<node_id>'@localhost`) with a generated password when the SST process begins.
2. The necessary privileges (`RELOAD`, `PROCESS`, `LOCK TABLES`, etc.) are automatically granted to this temporary user.
3. Once the SST process completes, the donor node automatically drops the user.

To enable automatic user management:

Ensure that the [wsrep\_sst\_auth](../../reference/wsrep-variable-details/wsrep_sst_method.md) system variable is not set (or is left blank) in your configuration file.

```ini
[mariadb]
...
# Do not set wsrep_sst_auth to use automatic user management
# wsrep_sst_auth =
```

{% hint style="warning" %}
If you explicitly define `wsrep_sst_auth` in your configuration, the server will revert to the manual behavior and attempt to authenticate using the credentials provided in that variable.
{% endhint %}

### Manual User Configuration

For versions prior to 11.4, or if you prefer to manage the user manually, you must create a user and provide the credentials to the server.

You can tell the donor node what username and password to use by setting the [wsrep\_sst\_auth](../../reference/wsrep-variable-details/wsrep_sst_method.md) system variable. It can be changed dynamically with `SET GLOBAL` on the node that you intend to be an SST donor:

```sql
SET GLOBAL wsrep_sst_auth = 'mariadbbackup:mypassword';
```

It can also be set in a server [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#global-options-related-to-option-files) prior to starting up a node:

```ini
[mariadb]
...
wsrep_sst_auth = mariadbbackup:mypassword
```

Some [authentication plugins](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins) do not require a password. For example, the `unix_socket` and `gssapi` authentication plugins do not require a password. If you are using a user account that does not require a password in order to log in, then you can just leave the password component of [wsrep\_sst\_auth](../../reference/wsrep-variable-details/wsrep_sst_method.md) empty. For example:

```ini
[mariadb]
...
wsrep_sst_auth = mariadbbackup:
```

The user account that performs the backup for the SST needs to have the same privileges as [mariadb-backup](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-usage/backup-and-restore/mariadb-backup/mariadb-backup-overview), which are the `RELOAD`, `PROCESS`, `LOCK TABLES` and `BINLOG MONITOR`, `REPLICA MONITOR` [global privileges](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/show/show-privileges). To be safe, ensure that these privileges are set on each node in your cluster. `mariadb-backup` connects locally on the donor node to perform the backup, so the following user should be sufficient:

```sql
CREATE USER 'mariadbbackup'@'localhost' IDENTIFIED BY 'mypassword';
GRANT RELOAD, PROCESS, LOCK TABLES, 
BINLOG MONITOR ON *.* TO 'mariadbbackup'@'localhost';
```

### Passwordless Authentication - Unix Socket <a href="#passwordless-authentication-unix-socket" id="passwordless-authentication-unix-socket"></a>

It is possible to use the [`unix_socket`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-unix-socket) authentication plugin for the user account that performs SSTs. This would provide the benefit of not needing to configure a plain-text password in [`wsrep_sst_auth`](../../reference/wsrep-variable-details/wsrep_sst_method.md).

The user account would have to have the same name as the operating system user account that is running the `mysqld` process. On many systems, this is the user account configured as the `user` option, and it tends to default to `mysql`.

For example, if the [`unix_socket`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-unix-socket) authentication plugin is already installed, then you could execute the following to create the user account:

```sql
CREATE USER 'mysql'@'localhost' IDENTIFIED VIA unix_socket;
GRANT RELOAD, PROCESS, LOCK TABLES, 
REPLICATION CLIENT ON *.* TO 'mysql'@'localhost';
```

To configure [`wsrep_sst_auth`](../../reference/wsrep-variable-details/wsrep_sst_method.md), set the following in a server [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files) prior to starting up a node:

```ini
[mariadb]
...
wsrep_sst_auth = mysql:
```

### Passwordless Authentication - GSSAPI <a href="#passwordless-authentication-gssapi" id="passwordless-authentication-gssapi"></a>

It is possible to use the [`gssapi`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/authentication-with-enterprise-server/authentication-with-gssapi) authentication plugin for the user account that performs SSTs. This would provide the benefit of not needing to configure a plain-text password in [`wsrep_sst_auth`](../../reference/wsrep-variable-details/wsrep_sst_method.md).

The following steps would need to be done beforehand:

* You need a KDC running [MIT Kerberos](https://web.mit.edu/Kerberos/krb5-1.12/doc/index.html) or [Microsoft Active Directory](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview).
* You will need to [create a keytab file](https://web.mit.edu/Kerberos/krb5-1.12/doc/admin/install_appl_srv.html#the-keytab-file) for the MariaDB server.
* You will need to [install the package](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi#installing-the-plugins-package) containing the [`gssapi`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi) authentication plugin.
* You will need to [install the plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi#installing-the-plugin) in MariaDB, so that the [`gssapi`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi) authentication plugin is available to use.
* You will need to [configure the plugin](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi#configuring-the-plugin).
* You will need to [create a user account](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/security/authentication-with-enterprise-server/authentication-with-gssapi#create-user) [`gssapi`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/plugins/authentication-plugins/authentication-plugin-gssapi)

For example, you could execute the following to create the user account in MariaDB:

```sql
CREATE USER 'mariadbbackup'@'localhost' IDENTIFIED VIA gssapi;
GRANT RELOAD, PROCESS, LOCK TABLES, 
BINLOG MONITOR ON *.* TO 'mariadbbackup'@'localhost';
```

To configure [`wsrep_sst_auth`](../../reference/wsrep-variable-details/wsrep_sst_method.md), set the following in a server [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files) prior to starting up a node:

```ini
[mariadb]
...
wsrep_sst_auth = mariadbbackup:
```

## Choosing a Donor Node <a href="#choosing-a-donor-node" id="choosing-a-donor-node"></a>

When mariadb-backup is used to create the backup for the SST on the donor node, mariadb-backup briefly requires a system-wide lock at the end of the backup. This is done with [`BACKUP STAGE BLOCK_COMMIT`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/backup-commands/backup-stage).

If a specific node in your cluster is acting as the _primary_ node by receiving all of the application's write traffic, then this node should not usually be used as the donor node, because the system-wide lock could interfere with the application. In this case, you can define one or more preferred donor nodes by setting the [`wsrep_sst_donor`](../../reference/galera-cluster-system-variables.md#wsrep_sst_donor) system variable.

For example, let's say that we have a 5-node cluster with the nodes `node1`, `node2`, `node3`, `node4`, and `node5`, and let's say that `node1` is acting as the _primary_ node. The preferred donor nodes for `node2` could be configured by setting the following in a server [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files) prior to starting up a node:

```ini
[mariadb]
...
wsrep_sst_donor=node3,node4,node5,
```

The trailing comma tells the server to allow any other node as donor when the preferred donors are not available. Therefore, if `node1` is the only node left in the cluster, the trailing comma allows it to be used as the donor node.

## Socat Dependency <a href="#socat-dependency" id="socat-dependency"></a>

During the SST process, the donor node uses `socat` to stream the backup to the joiner node. Then the joiner node prepares the backup before restoring it. The `socat` utility must be installed on both the donor node and the joiner node in order for this to work. Otherwise, the MariaDB error log will contain an error like:

{% code overflow="wrap" %}
```sql
WSREP_SST: [ERROR] socat not found in path: /usr/sbin:/sbin:/usr//bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin (20180122 14:55:32.993)
```
{% endcode %}

#### Installing Socat on RHEL/CentOS <a href="#installing-socat-on-rhelcentos" id="installing-socat-on-rhelcentos"></a>

On RHEL/CentOS, `socat` can be installed from the [Extra Packages for Enterprise Linux (EPEL)](https://docs.fedoraproject.org/en-US/epel/) repository.

## TLS <a href="#tls" id="tls"></a>

This SST method supports three different TLS methods. The specific method can be selected by setting the `encrypt` option in the `[sst]` section of the MariaDB configuration file. The options are:

* TLS using OpenSSL encryption built into `socat` (`encrypt=2`)
* TLS using OpenSSL encryption with Galera-compatible certificates and keys (`encrypt=3`)
* TLS using OpenSSL encryption with standard MySQL/MariaDB SSL certificates (`encrypt=4`)

{% hint style="warning" %}
Note that `encrypt=1` refers to a TLS encryption method that has been deprecated and removed.
{% endhint %}

### TLS Using OpenSSL Encryption Built into Socat <a href="#tls-using-openssl-encryption-built-into-socat" id="tls-using-openssl-encryption-built-into-socat"></a>

To generate keys compatible with this encryption method, follow [these directions](http://www.dest-unreach.org/socat/doc/socat-openssltunnel.html).

First, generate the keys and certificates:

```bash
FILENAME=sst
openssl genrsa -out $FILENAME.key 1024
openssl req -new -key $FILENAME.key -x509 -days 3653 -out $FILENAME.crt
cat $FILENAME.key $FILENAME.crt >$FILENAME.pem
chmod 600 $FILENAME.key $FILENAME.pem
```

On some systems, you may also have to add `dhparams` to the certificate:

```bash
openssl dhparam -out dhparams.pem 2048
cat dhparams.pem >> sst.pem
```

Next, copy the certificate and keys to all nodes in the cluster.

When done, configure the following on all nodes in the cluster:

```ini
[sst]
encrypt=2
tca=/etc/my.cnf.d/certificates/sst.crt
tcert=/etc/my.cnf.d/certificates/sst.pem
```

{% hint style="warning" %}
Make sure to replace the paths with whatever is relevant on your system. This should allow your SSTs to be encrypted.
{% endhint %}

### TLS Using OpenSSL Encryption With Galera-Compatible Certificates and Keys <a href="#tls-using-openssl-encryption-with-galera-compatible-certificates-and-keys" id="tls-using-openssl-encryption-with-galera-compatible-certificates-and-keys"></a>

To generate keys compatible with this encryption method, follow [these directions](https://galeracluster.com/library/documentation/ssl-cert.html).

First, generate the keys and certificates:

```bash
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

Next, copy the certificate and keys to all nodes in the cluster.

When done, configure the following on all nodes in the cluster:

```ini
[sst]
encrypt=3
tkey=/etc/my.cnf.d/certificates/server1-key.pem
tcert=/etc/my.cnf.d/certificates/server1-cert.pem
```

{% hint style="warning" %}
Make sure to replace the paths with whatever is relevant on your system. This should allow your SSTs to be encrypted.
{% endhint %}

## Logs <a href="#logs" id="logs"></a>

The `mariadb-backup` SST method has its own logging outside of the MariaDB Server logging.

### Logging to SST Logs <a href="#logging-to-sst-logs" id="logging-to-sst-logs"></a>

Logging for mariadb-backup SSTs works the following way.

By default, on the donor node, it logs to `mariadb-backup.backup.log`. This log file is located in the [`datadir`](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#datadir).

By default, on the joiner node, it logs to `mariadb-backup.prepare.log` and `mariadb-backup.move.log` These log files are also located in the `datadir`.

By default, before a new SST is started, existing `mariadb-backup` SST log files are compressed and moved to `/tmp/sst_log_archive`. This behavior can be disabled by setting `sst-log-archive=0` in the `[sst]` [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files). Similarly, the archive directory can be changed by setting `sst-log-archive-dir`:

```ini
[sst]
sst-log-archive=1
sst-log-archive-dir=/var/log/mysql/sst/
```

See [MDEV-17973](https://jira.mariadb.org/browse/MDEV-17973) for more information.

### Logging to Syslog <a href="#logging-to-syslog" id="logging-to-syslog"></a>

Redirect the SST logs to the syslog instead, by setting the following in the `[sst]` [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files):

```ini
[sst]
sst-syslog=1
```

You can also redirect the SST logs to the syslog by setting the following in the `[mysqld_safe]` [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files):

```ini
[mysqld_safe]
syslog
```

## Performing SSTs With IPv6 Addresses <a href="#performing-ssts-with-ipv6-addresses" id="performing-ssts-with-ipv6-addresses"></a>

If you are performing [mariadb-backup ](mariadb-backup-sst-method.md)SSTs with IPv6 addresses, then the `socat` utility needs to be passed the `pf=ip6` option. This can be done by setting the `sockopt` option in the `[sst]` [option group](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files#option-groups) in an [option file](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files):

```ini
[sst]
sockopt=",pf=ip6"
```

See [MDEV-18797](https://jira.mariadb.org/browse/MDEV-18797) for more information.

## Manual SST With mariadb-backup <a href="#manual-sst-with-mariabackup" id="manual-sst-with-mariabackup"></a>

If Galera Cluster's automatic SSTs repeatedly fail, it can be helpful to perform a "manual SST"; see: [Manual SST of Galera Cluster node with ](manual-sst-of-galera-cluster-node-with-mariadb-backup.md)[mariadb-backup](mariadb-backup-sst-method.md)

## See Also <a href="#see-also" id="see-also"></a>

* [Percona XtraBackup SST Configuration](https://www.percona.com/doc/percona-xtradb-cluster/5.7/manual/xtrabackup_sst.html)
* [Encrypting PXC Traffic: ENCRYPTING SST TRAFFIC](https://docs.percona.com/percona-xtradb-cluster/5.7/security/encrypt-traffic.html#encrypt-sst)
* [XTRABACKUP PARAMETERS](https://galeracluster.com/library/documentation/xtrabackup-options.html)
* [SSL FOR STATE SNAPSHOT TRANSFERS: ENABLING SSL FOR XTRABACKUP](https://galeracluster.com/library/documentation/ssl-sst.html#ssl-xtrabackup)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/7hzG0V6AUK8DqF4oiVaW/" %}

{% @marketo/form formId="4316" %}
