# Primary/Replica

## Overview

<table><thead><tr><th valign="top">Software Version</th><th>Diagram</th><th>Features</th></tr></thead><tbody><tr><td valign="top"><ul><li>Enterprise Server 10.4</li><li>Enterprise Server 10.5</li><li>Enterprise Server 10.6</li><li>Enterprise Server 11.4</li></ul></td><td><img src="../../../../analytics/.gitbook/assets/es-primary-replica-topology-no-title%20(1).png" alt=""></td><td><p><strong>MariaDB Replication</strong></p><ul><li>Highly available</li><li>Asynchronous or semi-synchronous replication</li><li>Automatic failover via MaxScale</li><li>Manual provisioning of new nodes from backup</li><li>Scales reads via MaxScale</li><li>Enterprise Server 10.3+, MaxScale 2.5+</li></ul></td></tr></tbody></table>

This procedure describes the deployment of the **Primary/Replica topology** with MariaDB Enterprise Server and MariaDB MaxScale.

Primary/Replica topology provides read scalability and fault tolerance through asynchronous or semi-synchronous single-primary replication.

This procedure has 7 steps, which are executed in sequence.

MariaDB products can be deployed in many different topologies to suit specific use cases. The Primary/Replica topology can be deployed on its own or integrated with MariaDB Enterprise Cluster.

This procedure represents basic product capability with 3 Enterprise Server nodes and 1 MaxScale node.

This page provides an overview of the topology, requirements, and deployment procedure.

Please read and understand this procedure before executing.

## Procedure Steps

<table><thead><tr><th width="204.5184326171875">Step</th><th>Description</th></tr></thead><tbody><tr><td><a href="step-1-install-mariadb-enterprise-server.md">Step 1</a></td><td>Install MariaDB Enterprise Server</td></tr><tr><td><a href="step-2-start-and-configure-mariadb-enterprise-server-on-primary-server.md">Step 2</a></td><td>Start and Configure MariaDB Enterprise Server on Primary Server</td></tr><tr><td><a href="step-3-start-and-configure-mariadb-enterprise-server-on-replica-servers.md">Step 3</a></td><td>Start and Configure MariaDB Enterprise Server on Replica Servers</td></tr><tr><td><a href="step-4-test-mariadb-enterprise-server.md">Step 4</a></td><td>Test MariaDB Enterprise Server</td></tr><tr><td><a href="step-5-install-mariadb-maxscale.md">Step 5</a></td><td>Install MariaDB MaxScale</td></tr><tr><td><a href="step-6-start-and-configure-mariadb-maxscale.md">Step 6</a></td><td>Start and Configure MariaDB MaxScale</td></tr><tr><td><a href="step-7-test-mariadb-maxscale.md">Step 7</a></td><td>Test MariaDB MaxScale</td></tr></tbody></table>

## Components

The following components are deployed during this procedure:

| Component                                                                                  | Function                                                                                                   |
| ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| [MariaDB Enterprise Server](../single-node-topologies/enterprise-server.md)                | Modern SQL RDBMS with high availability, pluggable storage engines, hot online backups, and audit logging. |
| [MariaDB MaxScale](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/) | Database proxy that extends the availability, scalability, and security of MariaDB Enterprise Servers      |

### MariaDB Enterprise Server Components

| Component                                               | Description                                                                                 |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| [InnoDB](../../../server-usage/storage-engines/innodb/) | <ul><li>General purpose storage engine</li><li>ACID-compliant</li><li>Performance</li></ul> |

### MariaDB MaxScale Components

<table><thead><tr><th width="234.1480712890625">Component</th><th>Description</th></tr></thead><tbody><tr><td>Listener</td><td>Listens for client connections to MaxScale, then passes them to the router service associated with the listener</td></tr><tr><td>MariaDB Monitor</td><td>Tracks changes in the state of MariaDB Enterprise Servers.</td></tr><tr><td>Read Connection Router</td><td>Routes connections from the listener to any available Enterprise Server node</td></tr><tr><td>Read/Write Split Router</td><td>Routes read operations from the listener to any available Enterprise Server node, and routes write operations from the listener to a specific server operating as the primary server</td></tr><tr><td>Server Module</td><td>Connection configuration in MaxScale to an Enterprise Server node</td></tr></tbody></table>

## Topology

<figure><img src="../../../../analytics/.gitbook/assets/es-primary-replica-topology-no-title%20(1).png" alt=""><figcaption></figcaption></figure>

Primary/Replica topology provides read scalability and fault tolerance through asynchronous or semi-synchronous single-primary replication of MariaDB Enterprise Server 11.4

The Primary/Replica topology consists of:

* 1 or more MaxScale nodes
* 1 Enterprise Server node operating as the primary server
* 2 or more Enterprise Server nodes operating as replica servers.

The MaxScale nodes:

* Monitor the health and availability of the Enterprise Server nodes
* Route queries to Enterprise Server nodes using Read/Write Split (`readwritesplit`) and Read Connection (`readconnroute`) routers.
* Promote replica servers in the event that the primary server fails.

The Enterprise Server node is operating as the primary server:

* Receives write queries from MaxScale, logging them to the Binary Log
* Provides Binary Logs to replica servers for replication

The Enterprise Server nodes are operating as replica servers:

* Receive read queries from MaxScale
* Replicate writes asynchronously or semi-synchronously from the primary server

## Requirements

These requirements are for the Primary/Replica topology when deployed with MariaDB Enterprise Server 11.4 and MariaDB MaxScale 25.01.

* [Operating System](./#operating-system)
* [System User Accounts](./#system-user-accounts)

### Operating System

In alignment to the [enterprise lifecycle](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/enterprise-server/about/enterprise-server-lifecycle), the Primary/Replica topology with MariaDB Enterprise Server 11.4 and MariaDB MaxScale 25.01 is provided for:

* AlmaLinux 8 (x86\_64, ARM64)
* AlmaLinux 9 (x86\_64, ARM64)
* Debian 11 (x86\_64, ARM64)
* Debian 12 (x86\_64, ARM64)
* Microsoft Windows (x86\_64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Red Hat Enterprise Linux 9 (x86\_64, PPC64LE, ARM64)
* Red Hat UBI 8 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* Rocky Linux 9 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 20.04 LTS (x86\_64, ARM64)
* Ubuntu 22.04 LTS (x86\_64, ARM64)
* Ubuntu 24.04 LTS (x86\_64, ARM64)

### System User Accounts

<table><thead><tr><th width="301.7037353515625">User Account</th><th>Purpose</th></tr></thead><tbody><tr><td><code>maxscale</code></td><td>MaxScale process owner</td></tr><tr><td><code>mysql</code></td><td>Enterprise Server process owner</td></tr></tbody></table>

## Quick Reference

* [MariaDB Enterprise Server Configuration Management](./#mariadb-enterprise-server-configuration-management)
* [MariaDB Enterprise Server Service Management](./#mariadb-enterprise-server-service-management)
* [MariaDB Enterprise Server Logs](./#mariadb-enterprise-server-logs)
* [MaxScale Configuration Management](./#maxscale-configuration-management)
* [MaxScale Service Management](./#maxscale-service-management)

### MariaDB Enterprise Server Configuration Management

<table><thead><tr><th width="261.4073486328125">Method</th><th>Description</th></tr></thead><tbody><tr><td>Configuration File</td><td>Configuration files (such as <code>/etc/my.cnf</code>) can be used to set system-variables and options. The server must be restarted to apply changes made to configuration files.</td></tr><tr><td>Command-line</td><td>The server can be started with command-line options that set system-variables and options.</td></tr><tr><td>SQL</td><td>Users can set system-variables that support dynamic changes on-the-fly using the SET statement.</td></tr></tbody></table>

MariaDB Enterprise Server packages are configured to read configuration files from different paths, depending on the operating system. Making custom changes to Enterprise Server default configuration files is not recommended because custom changes may be overwritten by other default configuration files that are loaded later.

To ensure that your custom changes will be read last, create a custom configuration file with the `z-` prefix in one of the include directories.

<table><thead><tr><th valign="top">Distribution</th><th valign="top">Example Configuration File Path</th></tr></thead><tbody><tr><td valign="top"><ul><li>CentOS</li><li>Red Hat Enterprise Linux (RHEL)</li><li>SUSE Linux Enterprise Server (SLES)</li></ul></td><td valign="top"><code>/etc/my.cnf.d/z-custom-mariadb.cnf</code></td></tr><tr><td valign="top"><ul><li>Debian</li><li>Ubuntu</li></ul></td><td valign="top"><code>/etc/mysql/mariadb.conf.d/z-custom-mariadb.cnf</code></td></tr></tbody></table>

### MariaDB Enterprise Server Service Management

The `systemctl` command is used to start and stop the MariaDB Enterprise Server service.

<table><thead><tr><th width="260.22216796875">Operation</th><th>Command</th></tr></thead><tbody><tr><td>Start</td><td><code>sudo systemctl start mariadb</code></td></tr><tr><td>Stop</td><td><code>sudo systemctl stop mariadb</code></td></tr><tr><td>Restart</td><td><code>sudo systemctl restart mariadb</code></td></tr><tr><td>Enable during startup</td><td><code>sudo systemctl enable mariadb</code></td></tr><tr><td>Disable during startup</td><td><code>sudo systemctl disable mariadb</code></td></tr><tr><td>Status</td><td><code>sudo systemctl status mariadb</code></td></tr></tbody></table>

For additional information, see "[Starting and Stopping MariaDB](../../../server-management/starting-and-stopping-mariadb/)".

### MariaDB Enterprise Server Logs

MariaDB Enterprise Server produces log data that can be helpful in problem diagnosis.

Log filenames and locations may be overridden in the server configuration. The default location of logs is the data directory. The data directory is specified by the [datadir](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir) system variable.

| Log                                                                                         | System Variable/Option                                                                                                                                    | Default Filename      |
| ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| [MariaDB Error Log](../../../server-management/server-monitoring-logs/error-log.md)         | [log\_error](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#list-of-server-system-variables)             | `<hostname>.err`      |
| [MariaDB Enterprise Audit Log](../../../reference/plugins/mariadb-enterprise-audit.md)      | [server\_audit\_file\_path](../../../reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_file_path)  | `server_audit.log`    |
| [Slow Query Log](../../../server-management/server-monitoring-logs/slow-query-log/)         | [slow\_query\_log\_file](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#list-of-server-system-variables) | `<hostname>-slow.log` |
| [General Query Log](../../../server-management/server-monitoring-logs/general-query-log.md) | [general\_log\_file](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#list-of-server-system-variables)     | `<hostname>.log`      |
| [Binary Log](../../../server-management/server-monitoring-logs/binary-log/)                 | [log\_bin](../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin)                                       | `<hostname>-bin`      |

### MaxScale Configuration Management

MaxScale can be configured using several methods. These methods make use of MaxScale's [REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api).

<table><thead><tr><th width="197.4073486328125">Method</th><th>Benefits</th></tr></thead><tbody><tr><td><a href="https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-management/administrative-tools-for-mariadb-maxscale-maxctrl">MaxCtrl</a></td><td>Command-line utility to perform administrative tasks through the REST API. See MaxCtrl Commands.</td></tr><tr><td><a href="https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/maxscale-management/deployment/maxscale-maxgui-guide">MaxGUI</a></td><td>MaxGUI is a graphical utility that can perform administrative tasks through the REST API.</td></tr><tr><td><a href="https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api">REST API</a></td><td>The REST API can be used directly. For example, the <code>curl</code> utility could be used to make REST API calls from the command-line. Many programming languages also have libraries to interact with REST APIs.</td></tr></tbody></table>

The procedure on these pages configures MaxScale using MaxCtrl.

### MaxScale Service Management

The `systemctl` command is used to start and stop the MaxScale service.

<table><thead><tr><th width="254.2962646484375">Operation</th><th>Command</th></tr></thead><tbody><tr><td>Start</td><td><code>sudo systemctl start maxscale</code></td></tr><tr><td>Stop</td><td><code>sudo systemctl stop maxscale</code></td></tr><tr><td>Restart</td><td><code>sudo systemctl restart maxscale</code></td></tr><tr><td>Enable during startup</td><td><code>sudo systemctl enable maxscale</code></td></tr><tr><td>Disable during startup</td><td><code>sudo systemctl disable maxscale</code></td></tr><tr><td>Status</td><td><code>sudo systemctl status maxscale</code></td></tr></tbody></table>

For additional information, see "[Starting and Stopping MariaDB](../../../server-management/starting-and-stopping-mariadb/)".

### Next Step

Navigation in the procedure ["Deploy Primary/Replica Topology"](./):

* Next: [Step 1: Install MariaDB Enterprise Server](step-1-install-mariadb-enterprise-server.md)

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>\\
