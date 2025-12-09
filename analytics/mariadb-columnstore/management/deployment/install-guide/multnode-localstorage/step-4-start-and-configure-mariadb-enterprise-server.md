---
description: 'Step 4: Start and Configure MariaDB Enterprise Server'
---

# Step 4: Start and Configure MariaDB Enterprise Server

## Overview

This page details step 4 of the 9-step procedure "Deploy ColumnStore Shared Local Storage Topology".

This step starts and configures MariaDB Enterprise Server, and MariaDB Enterprise ColumnStore.

{% include "../../../../../.gitbook/includes/the-instructions-were-teste....md" %}

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Stop the Enterprise ColumnStore Services

The installation process might have started some of the ColumnStore services. The services should be stopped prior to making configuration changes.

1. On each Enterprise ColumnStore node, stop the MariaDB Enterprise Server service:

```bash
$ sudo systemctl stop mariadb
```

2. On each Enterprise ColumnStore node, stop the MariaDB Enterprise ColumnStore service:

```bash
$ sudo systemctl stop mariadb-columnstore
```

3. On each Enterprise ColumnStore node, stop the CMAPI service:

```bash
$ sudo systemctl stop mariadb-columnstore-cmapi
```

## Configure Enterprise ColumnStore

**On each Enterprise ColumnStore node**, configure Enterprise Server.

<table><thead><tr><th width="212">Connector</th><th>MariaDB Connector/R2DBC</th></tr></thead><tbody><tr><td><a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#character_set_server">character_set_server</a></td><td>Set this system variable to utf8</td></tr><tr><td><a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#collation_server">collation_server</a></td><td>Set this system variable to utf8_general_ci</td></tr><tr><td>columnstore_use_import_for_batchinsert</td><td>Set this system variable to ALWAYS to always use cpimport for LOAD DATA INFILE and INSERT...SELECT statements.</td></tr><tr><td><a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/gtid#gtid_strict_mode">gtid_strict_mode</a></td><td>Set this system variable to ON.</td></tr><tr><td><a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#log_bin">log_bin</a></td><td>Set this option to the file you want to use for the Binary Log. Setting this option enables binary logging.</td></tr><tr><td><a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#log_bin_index">log_bin_index</a></td><td>Set this option to the file you want to use to track binlog filenames.</td></tr><tr><td><a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#log_slave_updates">log_slave_updates</a></td><td>Set this system variable to ON.</td></tr><tr><td><a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#relay_log">relay_log</a></td><td>Set this option to the file you want to use for the Relay Logs. Setting this option enables relay logging.</td></tr><tr><td><a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#relay_log_index">relay_log_index</a></td><td>Set this option to the file you want to use to index Relay Log filenames.</td></tr><tr><td><a href="https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables#server_id">server_id</a></td><td>Sets the numeric Server ID for this MariaDB Enterprise Server. The value set on this option must be unique to each node.</td></tr></tbody></table>

Mandatory system variables and options for ColumnStore Object Storage include:

Example Configuration

```sql
[mariadb]
bind_address                           = 0.0.0.0
log_error                              = mariadbd.err
character_set_server                   = utf8
collation_server                       = utf8_general_ci
log_bin                                = mariadb-bin
log_bin_index                          = mariadb-bin.index
relay_log                              = mariadb-relay
relay_log_index                        = mariadb-relay.index
log_slave_updates                      = ON
gtid_strict_mode                       = ON

# This must be unique on each Enterprise ColumnStore node
server_id                              = 1
```

## Start the Enterprise ColumnStore Services

1. On each Enterprise ColumnStore node, start and enable the MariaDB Enterprise Server service, so that it starts automatically upon reboot:

```bash
$ sudo systemctl start mariadb
```

```bash
$ sudo systemctl enable mariadb
```

2. On each Enterprise ColumnStore node, stop the MariaDB Enterprise ColumnStore service:

```bash
$ sudo systemctl stop mariadb-columnstore
```

After the CMAPI service is installed in the next step, CMAPI will start the Enterprise ColumnStore service as needed on each node. CMAPI disables the Enterprise ColumnStore service to prevent systemd from automatically starting Enterprise ColumnStore upon reboot.

3. On each Enterprise ColumnStore node, start and enable the CMAPI service, so that it starts automatically upon reboot:

```bash
$ sudo systemctl start mariadb-columnstore-cmapi
```

```bash
$ sudo systemctl enable mariadb-columnstore-cmapi
```

For additional information, see "Start and Stop Services".

## Create User Accounts

The ColumnStore Object Storage topology requires several user accounts. Each user account should be created on the primary server, so that it is replicated to the replica servers.

### Create the Utility User

Enterprise ColumnStore requires a mandatory utility user account to perform cross-engine joins and similar operations.

1. On the primary server, create the user account with the CREATE USER statement:

```sql
CREATE USER 'util_user'@'127.0.0.1'
IDENTIFIED BY 'util_user_passwd';
```

2. On the primary server, grant the user account SELECT privileges on all databases with the GRANT statement:

```sql
GRANT SELECT, PROCESS ON *.*
TO 'util_user'@'127.0.0.1';
```

3. On each Enterprise ColumnStore node, configure the ColumnStore utility user:

```bash
$ sudo mcsSetConfig CrossEngineSupport Host 127.0.0.1
```

```bash
$ sudo mcsSetConfig CrossEngineSupport Port 3306
```

```bash
$ sudo mcsSetConfig CrossEngineSupport User util_user
```

4. On each Enterprise ColumnStore node, set the password:

```bash
$ sudo mcsSetConfig CrossEngineSupport Password util_user_passwd
```

For details about how to encrypt the password, see "[Credentials Management for MariaDB Enterprise ColumnStore](https://app.gitbook.com/s/rBEU9juWLfTDcdwF3Q14/managing-columnstore/enterprise-columnstore-credentials-management)".

Passwords should meet your organization's password policies. If your MariaDB Enterprise Server instance has a password validation plugin installed, then the password should also meet the configured requirements.

### Create the Replication User

ColumnStore Object Storage uses MariaDB Replication to replicate writes between the primary and replica servers. As MaxScale can promote a replica server to become a new primary in the event of node failure, all nodes must have a replication user.

The action is performed **on the primary server**.

Create the replication user and grant it the required privileges:

1. Use the CREATE USER statement to create replication user.

```sql
CREATE USER 'repl'@'192.0.2.%' IDENTIFIED BY 'repl_passwd';
```

Replace the referenced IP address with the relevant address for your environment.

Ensure that the user account can connect to the primary server from each replica.

2. Grant the user account the required privileges with the GRANT statement.

```sql
GRANT REPLICA MONITOR,
   REPLICATION REPLICA,
   REPLICATION REPLICA ADMIN,
   REPLICATION MASTER ADMIN
ON *.* TO 'repl'@'192.0.2.%';
```

### Create MaxScale User

ColumnStore Object Storage 23.10 uses MariaDB MaxScale 22.08 to load balance between the nodes.

This action is performed on the primary server.

1. Use the [CREATE USER](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/create-user) statement to create the MaxScale user:

```sql
CREATE USER 'mxs'@'192.0.2.%'
IDENTIFIED BY 'mxs_passwd';
```

Replace the referenced IP address with the relevant address for your environment.

Ensure that the user account can connect from the IP address of the MaxScale instance.

2. Use the [GRANT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant) statement to grant the privileges required by the router:

```sql
GRANT SHOW DATABASES ON *.* TO 'mxs'@'192.0.2.%';

GRANT SELECT ON mysql.columns_priv TO 'mxs'@'192.0.2.%';

GRANT SELECT ON mysql.db TO 'mxs'@'192.0.2.%';

GRANT SELECT ON mysql.procs_priv TO 'mxs'@'192.0.2.%';

GRANT SELECT ON mysql.proxies_priv TO 'mxs'@'192.0.2.%';

GRANT SELECT ON mysql.roles_mapping TO 'mxs'@'192.0.2.%';

GRANT SELECT ON mysql.tables_priv TO 'mxs'@'192.0.2.%';

GRANT SELECT ON mysql.user TO 'mxs'@'192.0.2.%';
```

3. Use the [GRANT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/account-management-sql-statements/grant) statement to grant privileges required by the MariaDB Monitor.

```sql
GRANT BINLOG ADMIN,
   READ_ONLY ADMIN,
   RELOAD,
   REPLICA MONITOR,
   REPLICATION MASTER ADMIN,
   REPLICATION REPLICA ADMIN,
   REPLICATION REPLICA,
   SHOW DATABASES,
   SELECT
ON *.* TO 'mxs'@'192.0.2.%';
```

## Configure MariaDB Replication

On each replica server, configure MariaDB Replication:

1. Use the CHANGE MASTER TO statement to configure the connection to the primary server:

```sql
CHANGE MASTER TO
   MASTER_HOST='192.0.2.1',
   MASTER_USER='repl',
   MASTER_PASSWORD='repl_passwd',
   MASTER_USE_GTID=slave_pos;
```

2. Start replication using the START REPLICA statement:

```sql
START REPLICA;
```

3. Confirm that replication is working using the SHOW REPLICA STATUS statement:

```sql
SHOW REPLICA STATUS;
```

Ensure that the replica server cannot accept local writes by setting the read\_only system variable to ON using the SET GLOBAL statement:

```sql
SET GLOBAL read_only=ON;
```

## Initiate the Primary Server with CMAPI

Initiate the primary server using CMAPI.

1. Create an API key for the cluster. This API key should be stored securely and kept confidential, because it can be used to add cluster nodes to the multi-node Enterprise ColumnStore deployment.

For example, to create a random 256-bit API key using openssl rand:

```bash
$ openssl rand -hex 32

93816fa66cc2d8c224e62275bd4f248234dd4947b68d4af2b29671dd7d5532dd
```

This document will use the following API key in further examples, but users should create their own:

2. Use CMAPI to add the primary server to the cluster and set the API key.\
   The new API key needs to be provided as part of the X-API-key HTML header.

For example, if the primary server's host name is mcs1 and its IP address is 192.0.2.1, use the following node command:

```bash
$ curl -k -s -X PUT https://mcs1:8640/cmapi/0.4.0/cluster/node \
   --header 'Content-Type:application/json' \
   --header 'x-api-key:93816fa66cc2d8c224e62275bd4f248234dd4947b68d4af2b29671dd7d5532dd' \
   --data '{"timeout":120, "node": "192.0.2.1"}' \
   | jq .
```

```json
{
  "timestamp": "2020-10-28 00:39:14.672142",
  "node_id": "192.0.2.1"
}
```

3. Use CMAPI to check the status of the cluster node:

```bash
$ curl -k -s https://mcs1:8640/cmapi/0.4.0/cluster/status \
   --header 'Content-Type:application/json' \
   --header 'x-api-key:93816fa66cc2d8c224e62275bd4f248234dd4947b68d4af2b29671dd7d5532dd' \
   | jq .
```

```json
{
  "timestamp": "2020-12-15 00:40:34.353574",
  "192.0.2.1": {
    "timestamp": "2020-12-15 00:40:34.362374",
    "uptime": 11467,
    "dbrm_mode": "master",
    "cluster_mode": "readwrite",
    "dbroots": [
      "1"
    ],
    "module_id": 1,
    "services": [
      {
        "name": "workernode",
        "pid": 19202
      },
      {
        "name": "controllernode",
        "pid": 19232
      },
      {
        "name": "PrimProc",
        "pid": 19254
      },
      {
        "name": "ExeMgr",
        "pid": 19292
      },
      {
        "name": "WriteEngine",
        "pid": 19316
      },
      {
        "name": "DMLProc",
        "pid": 19332
      },
      {
        "name": "DDLProc",
        "pid": 19366
      }
    ]
  }
```

## Add Replica Servers with CMAPI

Add the replica servers with CMAPI:

1. For each replica server, use [CMAPI](../../../../architecture/columnstore-architectural-overview.md#cluster-management-api-cmapi-server) to add the replica server to the cluster.\
   The previously set API key needs to be provided as part of the X-API-key HTML header.

For example, if the primary server's host name is mcs1 and the replica server's IP address is 192.0.2.2, use the following node command:

```bash
$ curl -k -s -X PUT https://mcs1:8640/cmapi/0.4.0/cluster/node \
   --header 'Content-Type:application/json' \
   --header 'x-api-key:93816fa66cc2d8c224e62275bd4f248234dd4947b68d4af2b29671dd7d5532dd' \
   --data '{"timeout":120, "node": "192.0.2.2"}' \
   | jq .
```

```json
{
  "timestamp": "2020-10-28 00:42:42.796050",
  "node_id": "192.0.2.2"
}
```

2. After all replica servers have been added, use CMAPI to confirm that all cluster nodes have been successfully added:

```bash
$ curl -k -s https://mcs1:8640/cmapi/0.4.0/cluster/status \
   --header 'Content-Type:application/json' \
   --header 'x-api-key:93816fa66cc2d8c224e62275bd4f248234dd4947b68d4af2b29671dd7d5532dd' \
   | jq .
```

```json
{
  "timestamp": "2020-12-15 00:40:34.353574",
  "192.0.2.1": {
    "timestamp": "2020-12-15 00:40:34.362374",
    "uptime": 11467,
    "dbrm_mode": "master",
    "cluster_mode": "readwrite",
    "dbroots": [
      "1"
    ],
    "module_id": 1,
    "services": [
      {
        "name": "workernode",
        "pid": 19202
      },
      {
        "name": "controllernode",
        "pid": 19232
      },
      {
        "name": "PrimProc",
        "pid": 19254
      },
      {
        "name": "ExeMgr",
        "pid": 19292
      },
      {
        "name": "WriteEngine",
        "pid": 19316
      },
      {
        "name": "DMLProc",
        "pid": 19332
      },
      {
        "name": "DDLProc",
        "pid": 19366
      }
    ]
  },
  "192.0.2.2": {
    "timestamp": "2020-12-15 00:40:34.428554",
    "uptime": 11437,
    "dbrm_mode": "slave",
    "cluster_mode": "readonly",
    "dbroots": [
      "2"
    ],
    "module_id": 2,
    "services": [
      {
        "name": "workernode",
        "pid": 17789
      },
      {
        "name": "PrimProc",
        "pid": 17813
      },
      {
        "name": "ExeMgr",
        "pid": 17854
      },
      {
        "name": "WriteEngine",
        "pid": 17877
      }
    ]
  },
  "192.0.2.3": {
    "timestamp": "2020-12-15 00:40:34.428554",
    "uptime": 11437,
    "dbrm_mode": "slave",
    "cluster_mode": "readonly",
    "dbroots": [
      "2"
    ],
    "module_id": 2,
    "services": [
      {
        "name": "workernode",
        "pid": 17789
      },
      {
        "name": "PrimProc",
        "pid": 17813
      },
      {
        "name": "ExeMgr",
        "pid": 17854
      },
      {
        "name": "WriteEngine",
        "pid": 17877
      }
    ]
  },
  "num_nodes": 3
}
```

## Configure Linux Security Modules (LSM)

The specific steps to configure the security module depend on the operating system.

### Configure SELinux (CentOS, RHEL)

Configure SELinux for Enterprise ColumnStore:

1. To configure SELinux, you have to install the packages required for audit2allow.\
   On CentOS 7 and RHEL 7, install the following:

```bash
$ sudo yum install policycoreutils policycoreutils-python
```

On RHEL 8, install the following:

```bash
$ sudo yum install policycoreutils python3-policycoreutils policycoreutils-python-utils
```

2. Allow the system to run under load for a while to generate SELinux audit events.
3. After the system has taken some load, generate an SELinux policy from the audit events using audit2allow:

```bash
$ sudo grep mysqld /var/log/audit/audit.log | audit2allow -M mariadb_local
```

If no audit events were found, this will print the following:

```bash
$ sudo grep mysqld /var/log/audit/audit.log | audit2allow -M mariadb_local

Nothing to do
```

4. If audit events were found, the new SELinux policy can be loaded using semodule:

```bash
$ sudo semodule -i mariadb_local.pp
```

5. Set SELinux to enforcing mode:

```bash
$ sudo setenforce enforcing
```

6. Set SELinux to enforcing mode by setting SELINUX=enforcing in /etc/selinux/config.

For example, the file will usually look like this after the change:

```systemd
# This file controls the state of SELinux on the system.
# SELINUX= can take one of these three values:
#     enforcing - SELinux security policy is enforced.
#     permissive - SELinux prints warnings instead of enforcing.
#     disabled - No SELinux policy is loaded.
SELINUX=enforcing
# SELINUXTYPE= can take one of three values:
#     targeted - Targeted processes are protected,
#     minimum - Modification of targeted policy. Only selected processes are protected.
#     mls - Multi Level Security protection.
SELINUXTYPE=targeted
```

7. Confirm that SELinux is in enforcing mode:

```bash
$ sudo getenforce
```

```
Enforcing
```

### Configure AppArmor (Ubuntu)

For information on how to create a profile, see [How to create an AppArmor Profile](https://ubuntu.com/tutorials/beginning-apparmor-profile-development#1-overview) on Ubuntu.com.

## Configure Firewalls

The specific steps to configure the firewall service depend on the platform.

### Configure firewalld (CentOS, RHEL)

Configure firewalld for Enterprise Cluster on CentOS and RHEL:

1. Check if the firewalld service is running:

```bash
$ sudo systemctl status firewalld
```

2. If the firewalld service was stopped to perform the installation, start it now:

For example, if your cluster nodes are in the 192.0.2.0/24 subnet:

```bash
$ sudo systemctl start firewalld
```

3. Open up the relevant ports using firewall-cmd:

```bash
$ sudo firewall-cmd --permanent --add-rich-rule='
   rule family="ipv4"
   source address="192.0.2.0/24"
   destination address="192.0.2.0/24"
   port port="3306" protocol="tcp"
   accept'
```

```bash
$ sudo firewall-cmd --permanent --add-rich-rule='
   rule family="ipv4"
   source address="192.0.2.0/24"
   destination address="192.0.2.0/24"
   port port="8600-8630" protocol="tcp"
   accept'
```

```bash
$ sudo firewall-cmd --permanent --add-rich-rule='
   rule family="ipv4"
   source address="192.0.2.0/24"
   destination address="192.0.2.0/24"
   port port="8640" protocol="tcp"
   accept'
```

```bash
$ sudo firewall-cmd --permanent --add-rich-rule='
   rule family="ipv4"
   source address="192.0.2.0/24"
   destination address="192.0.2.0/24"
   port port="8700" protocol="tcp"
   accept'
```

```bash
$ sudo firewall-cmd --permanent --add-rich-rule='
   rule family="ipv4"
   source address="192.0.2.0/24"
   destination address="192.0.2.0/24"
   port port="8800" protocol="tcp"
   accept'
```

4. Reload the runtime configuration:

```
$ sudo firewall-cmd --reload
```

### Configure UFW (Ubuntu)

Configure UFW for Enterprise ColumnStore on Ubuntu:

1. Check if the UFW service is running:

```bash
$ sudo ufw status verbose
```

2. If the UFW service was stopped to perform the installation, start it now:

```bash
$ sudo ufw enable
```

3. Open up the relevant ports using ufw.

For example, if your cluster nodes are in the 192.0.2.0/24 subnet in the range 192.0.2.1 - 192.0.2.3:

```bash
$ sudo ufw allow from 192.0.2.0/24 to 192.0.2.3 port 3306 proto tcp

$ sudo ufw allow from 192.0.2.0/24 to 192.0.2.3 port 8600:8630 proto tcp

$ sudo ufw allow from 192.0.2.0/24 to 192.0.2.3 port 8640 proto tcp

$ sudo ufw allow from 192.0.2.0/24 to 192.0.2.3 port 8700 proto tcp

$ sudo ufw allow from 192.0.2.0/24 to 192.0.2.3 port 8800 proto tcp
```

4. Reload the runtime configuration:

```bash
$ sudo ufw reload
```

## Next Step

Navigation in the procedure "Deploy ColumnStore Shared Local Storage Topology".

This page was step 4 of 9.

[Next: Step 5: Test MariaDB Enterprise Server](step-5-test-mariadb-enterprise-server.md).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
