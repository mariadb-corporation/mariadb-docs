# Step 2: Start and Configure MariaDB Enterprise Server

## Overview

This page details step 2 of the 6-step procedure "[Deploy Galera Cluster Topology](./)".

This step configures MariaDB Enterprise Servers to operate as Enterprise Cluster nodes and starts MariaDB Enterprise Cluster.

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Stop the Enterprise Server Service

The installation process might have started the Enterprise Server service. The service should be stopped prior to making configuration changes.

On each Enterprise Cluster node, stop the MariaDB Enterprise Server service:

```bash
$ sudo systemctl stop mariadb
```

## Acquire TLS Certificate

By default, MariaDB Enterprise Cluster requires data-in-transit encryption to secure Galera replication traffic.

MariaDB Enterprise Cluster encrypts the data using the Transport Layer Security (TLS) protocol, which is a newer version of the Secure Socket Layer (SSL) protocol.

In MariaDB Enterprise Cluster 10.5 and earlier, TLS was supported, but not required. For backward compatibility, MariaDB Enterprise Cluster supports the Provider WSREP TLS Mode, which is equivalent to Enterprise Cluster's TLS implementation in ES 10.5 and earlier. For additional information, see "WSREP TLS Modes".

TLS configuration requires 3 files.

| Example Filename | Description                      |
| ---------------- | -------------------------------- |
| ca-cert.pem      | Certificate Authority (CA) file. |
| server-cert.pem  | X.509 certificate file.          |
| server-key.pem   | X.509 key file.                  |

Self-signed certificates are supported. However, in environments where security is critical, it is recommended to use certificates signed by a trusted Certificate Authority (CA).

For additional information, see "Data-in-Transit Encryption".

## Configure Enterprise Cluster

MariaDB Enterprise Server installations support MariaDB Enterprise Cluster, powered by Galera. MariaDB Enterprise Cluster uses the Galera Enterprise 4 wsrep provider plugin. The path to the wsrep provider plugin must be configured using the [wsrep\_provider](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_provider) system variable.

### Required System Variables and Options

Enterprise Cluster nodes require that you set the following system variables and options:

| System Variable/Option                                                                                                                    | Description                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bind\_address                                                                                                                             | The network socket Enterprise Cluster listens on for incoming TCP/IP client connections. On Debian or Ubuntu, this system variable must be set to override the 127.0.0.1 default configuration.                                                                                       |
| binlog\_format                                                                                                                            | Enterprise Cluster requires use of the ROW Binary Log format.                                                                                                                                                                                                                         |
| innodb\_autoinc\_lock\_mode                                                                                                               | Enterprise Cluster requires an auto-increment lock mode of 2.                                                                                                                                                                                                                         |
| ssl\_ca                                                                                                                                   | Certificate Authority (CA) file in PEM format.                                                                                                                                                                                                                                        |
| ssl\_cert                                                                                                                                 | X.509 certificate file in PEM format.                                                                                                                                                                                                                                                 |
| ssl\_key                                                                                                                                  | X.509 key file in PEM format.                                                                                                                                                                                                                                                         |
| [wsrep\_cluster\_address](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_cluster_address) | Sets the Group Communications back-end (usually gcomm:), followed by a comma-separated list of IP addresses or domain names for each Cluster Node. It is best practice to include all Enterprise Cluster nodes in this list.                                                          |
| [wsrep\_cluster\_name](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_cluster_name)       | Sets the logical name for the cluster. Must be the same on all Cluster Nodes.                                                                                                                                                                                                         |
| wsrep\_on                                                                                                                                 | Enables Enterprise Cluster.                                                                                                                                                                                                                                                           |
| [wsrep\_provider](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_provider)                | Path to the Galera Enterprise 4 wsrep provider plugin. In MariaDB Enterprise Cluster 11.4, the path is /usr/lib/galera/libgalera\_enterprise\_smm.so on Debian and Ubuntu and /usr/lib64/galera/libgalera\_enterprise\_smm.so on CentOS, RHEL, and SLES.                              |
| [wsrep\_provider\_options](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/wsrep-variable-details/wsrep_provider_options)        | Accepts options for the Galera Enterprise 4 wsrep provider plugin. Multiple options can be specified, separated by a semi-colon (;). For example, can be used to configure Galera cache size or to enable TLS. For a complete list of available options, see wsrep\_provider\_options |

## Example Configuration

Edit a configuration file and set these system variables and options:

```
[mariadb]
bind_address             = 0.0.0.0
binlog_format            = ROW
innodb_autoinc_lock_mode = 2
wsrep_cluster_address    = gcomm://192.0.2.101,192.0.2.102,192.0.2.103
wsrep_cluster_name       = example-cluster
wsrep_on                 = ON

# wsrep provider path for Debian and Ubuntu:
wsrep_provider = /usr/lib/galera/libgalera_enterprise_smm.so

# wsrep provider path for CentOS, RHEL, and SLES:
# wsrep_provider = /usr/lib64/galera/libgalera_enterprise_smm.so

wsrep_provider_options = "gcache.size=2G;gcs.fc_limit=128"

# TLS Configuration
ssl_ca   = /path/to/ca-cert.pem
ssl_cert = /path/to/sever-cert.pem
ssl_key  = /path/to/server-key.pem
```

For additional information, see "MariaDB Enterprise Server Configuration Management".

## Configure MariaDB Replication

MariaDB Enterprise Cluster can be deployed alongside MariaDB Replication. Deploying MariaDB Enterprise Cluster with MariaDB Replication enables integrating Enterprise Cluster with other products and clusters, for example as separate clusters in different data centers, or as a small dedicated write cluster with two larger dedicated read clusters.

For additional information, see "Replication Configuration".

## Bootstrap the Primary Component

When an Enterprise Cluster node starts, it checks the addresses in the [wsrep\_cluster\_address](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_cluster_address) system variable to establish connections with other nodes. The node does not become active until it finds a node that belongs to the Primary Component.

To start the cluster when all nodes are down, you must bootstrap the Primary Component on one node. This allows the other nodes to connect to a working cluster.

On one Enterprise Cluster node, when all nodes are down, bootstrap the Primary Component.

1. Bootstrap the Primary Component:

```bash
$ sudo galera_new_cluster
```

For additional information, see "Bootstrap a Galera Cluster".

2. Connect with MariaDB Client:

```bash
$ sudo mariadb
```

The sudo command is used here to connect to the Enterprise Server node using the `root@localhost` user account, which authenticates using the `unix_socket` authentication plugin. Other user accounts can be used by specifying the --user and --password command-line options.

Use the SHOW STATUS statement to check the [wsrep\_cluster\_size](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables#wsrep_cluster_size) status variable:

```sql
SHOW GLOBAL STATUS LIKE 'wsrep_cluster_size';

+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| wsrep_cluster_size |     1 |
+--------------------+-------+
```

The Enterprise Cluster node launches as the Primary Component of a single-node cluster.

## Add Nodes to the Cluster

To add nodes to a cluster that has a Primary Component running, complete the following procedure for each Enterprise Cluster node to be added. Nodes should be added one at a time.

1. On the Enterprise Cluster node being added, start MariaDB Enterprise Server:

```bash
$ sudo systemctl start mariadb
```

For additional information, see "Start and Stop Services".

2. On the Enterprise Cluster node being added, connect with MariaDB Client:

```bash
$ sudo mariadb
```

3. On the bootstrapped Enterprise Cluster node, use the SHOW STATUS statement to check the [wsrep\_cluster\_size](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables#wsrep_cluster_size) status variable:

```sql
SHOW GLOBAL STATUS LIKE 'wsrep_cluster_size';

+--------------------+-------+
| Variable_name      | Value |
+--------------------+-------+
| wsrep_cluster_size |     2 |
+--------------------+-------+
```

4. On the Enterprise Cluster node being added, use the SHOW STATUS statement to check the [wsrep\_local\_state\_comment](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables#wsrep_local_state_comment) status variable. If [wsrep\_local\_state\_comment](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables#wsrep_local_state_comment) is `SYNCED`, the node has been successfully added, and the Add Node procedure can be repeated to add more nodes.

```sql
SHOW GLOBAL STATUS LIKE 'wsrep_local_state_comment';

+---------------------------+--------+
| Variable_name             | Value  |
+---------------------------+--------+
| wsrep_local_state_comment | Synced |
+---------------------------+--------+
```

When each new Enterprise Cluster node joins the cluster, it requests the current cluster position. If the new node is missing transactions, it initiates either a State Snapshot Transfer (SST) or an Incremental State Transfer (IST) from a donor node to synchronize its data with the Primary Component. Depending on the value of [wsrep\_sst\_method](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_sst_method) , the donor node may or may not be blocked during an SST.

When the new Enterprise Cluster node finishes its state transfer, the node updates the [wsrep\_local\_state\_comment](https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-status-variables#wsrep_local_state_comment) status variable to `SYNCED`. MaxScale registers the change and begins routing connections or queries to the new node.

## Next Step

Navigation in the procedure "Deploy Galera Cluster Topology":

This page was step 2 of 6.

Next: Step 3: Test MariaDB Enterprise Server

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
