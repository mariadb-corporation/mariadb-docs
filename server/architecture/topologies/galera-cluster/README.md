# Galera Cluster

## Overview

| **Software Version**                                                                                                                  | **Diagram**                                                                                | **Features**                                                                                                                                                                                                                                                                                                                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <ul><li>Enterprise Server 10.4</li><li>Enterprise Server 10.5</li><li>Enterprise Server 10.6</li><li>Enterprise Server 11.4</li></ul> | ![](../../../../analytics/.gitbook/assets/es-galera-cluster-topology-no-title%20\(1\).png) | <p><strong>Multi-Primary Cluster Powered by Galera for Transactional/OLTP Workloads</strong></p><ul><li>InnoDB Storage Engine</li><li>Highly available</li><li>Virtually synchronous, certification-based replication</li><li>Automated provisioning of new nodes (IST/SST)</li><li>Scales reads via MaxScale</li><li>Enterprise Server 10.3+, MariaDB Enterprise Cluster (powered by Galera), MaxScale 2.5+</li></ul> |

This procedure describes the deployment of the **Galera Cluster topology** with MariaDB Enterprise Server 11.4 and MariaDB MaxScale 25.01.

MariaDB Enterprise Cluster is powered by Galera.

MariaDB Enterprise Cluster provides read scalability and fault tolerance through virtually synchronous multi-primary certification-based write-set replication (wsrep).

This procedure has 6 steps, which are executed in sequence.

MariaDB products can be deployed in many different topologies to suit specific use cases. Enterprise Cluster can be deployed on its own, or integrated with MariaDB Replication to integrate with other clusters or topologies.

This procedure represents basic product capability with 3 Enterprise Cluster nodes and 1 MaxScale node.

This page provides an overview of the topology, requirements, and deployment procedures.

Please read and understand this procedure before executing.

Procedure Steps

<table><thead><tr><th width="176.07403564453125">Step</th><th>Description</th></tr></thead><tbody><tr><td>Step 1</td><td><a href="step-1-install-mariadb-enterprise-server.md">Install MariaDB Enterprise Server</a></td></tr><tr><td>Step 2</td><td><a href="step-2-start-and-configure-mariadb-enterprise-server.md">Start and Configure MariaDB Enterprise Server</a></td></tr><tr><td>Step 3</td><td><a href="step-3-test-mariadb-enterprise-server.md">Test MariaDB Enterprise Server</a></td></tr><tr><td>Step 4</td><td><a href="step-4-install-mariadb-maxscale.md">Install MariaDB MaxScale</a></td></tr><tr><td>Step 5</td><td><a href="step-5-start-and-configure-mariadb-maxscale.md">Start and Configure MariaDB MaxScale</a></td></tr><tr><td>Step 6</td><td><a href="step-6-test-mariadb-maxscale.md">Test MariaDB MaxScale</a></td></tr></tbody></table>

## Support

Customers can obtain support by submitting a support case.

## Components

The following components are deployed during this procedure:

<table><thead><tr><th width="241.25927734375" valign="top">Component</th><th>Function</th></tr></thead><tbody><tr><td valign="top"><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/SsmexDFPv2xG2OTyO5yV/">MariaDB Enterprise Server</a></td><td>Modern SQL RDBMS with high availability, pluggable storage engines, hot online backups, and audit logging.</td></tr><tr><td valign="top"><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/">MariaDB MaxScale 25.01</a></td><td>Database proxy that extends the availability, scalability, and security of MariaDB Enterprise Servers</td></tr></tbody></table>

### MariaDB Enterprise Server Components

<table><thead><tr><th width="199.7777099609375" valign="top">Component</th><th>Description</th></tr></thead><tbody><tr><td valign="top"><a href="https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/3VYeeVGUV4AMqrA3zwy7/">Enterprise Cluster</a></td><td><p>MariaDB Enterprise Server leverages the Galera Enterprise 4 wsrep provider plugin</p><ul><li>Provides virtually synchronous multi-primary replication for MariaDB Enterprise Server</li><li>All nodes can handle both reads and writes</li><li>Replicates write-sets to all other nodes in the cluster</li><li>Supports data-at-rest encryption of the write-set cache</li></ul></td></tr><tr><td valign="top"><a href="../../../server-usage/storage-engines/innodb/">InnoDB</a></td><td><ul><li>General purpose storage engine</li><li>ACID-compliant</li><li>Performance</li><li>Required for Enterprise Cluster</li></ul></td></tr></tbody></table>

### MariaDB MaxScale Components

<table><thead><tr><th width="232.962890625">Component</th><th>Description</th></tr></thead><tbody><tr><td>Galera Monitor</td><td>Tracks changes in the state of MariaDB Enterprise Servers operating as Enterprise Cluster nodes.</td></tr><tr><td>Listener</td><td>Listens for client connections to MaxScale, then passes them to the router service associated with the listener</td></tr><tr><td>Read Connection Router</td><td>Routes connections from the listener to any available Enterprise Cluster node</td></tr><tr><td>Read/Write Split Router</td><td>Routes read operations from the listener to any available Enterprise Cluster node, and routes write operations from the listener to a specific server that MaxScale uses as the primary server</td></tr><tr><td>Server Module</td><td>Connection configuration in MaxScale to an Enterprise Cluster node</td></tr></tbody></table>

## Topology

<figure><img src="../../../../analytics/.gitbook/assets/es-galera-cluster-topology-no-title%20(1).png" alt=""><figcaption></figcaption></figure>

MariaDB Enterprise Cluster topology provides read scalability through certification-based write-set replication (wsrep) that is multi-primary and virtually synchronous.

The Enterprise Cluster topology consists of:

* 1 or more MaxScale nodes
* 3 or more MariaDB Enterprise Servers (ES) configured as Enterprise Cluster nodes

The MaxScale nodes:

* Monitor the health and availability of each Enterprise Cluster node using the Galera Monitor (galeramon)
* Accept client and application connections
* Route queries to the Enterprise Cluster nodes using the Read Connection (readconnroute) or the Read/Write Split (readwritesplit) routers.

The Enterprise Cluster nodes:

* Receive queries from MaxScale
* Store data locally using the InnoDB storage engine
* Perform certification-based virtually synchronous replication to other Enterprise Cluster nodes
* Provide State Snapshot Transfers (SST) to bring MariaDB Enterprise Server nodes into sync with the cluster

## Requirements

These requirements are for the Galera Cluster topology when deployed with MariaDB Enterprise Server and MariaDB MaxScale 25.01.

* [Node Count](./#node-count)
* [Operating System](./#operating-system)

### Node Count

* MaxScale nodes, 1 or more are required.
* Enterprise Cluster nodes, 3 or more are required.

To avoid problems in establishing a quorum in the event of a network partition or outage, MariaDB recommends deploying an odd number of Enterprise Cluster nodes. When using multiple network switches, deploy across an odd number of switches, each with an odd number of nodes. When using multiple data centers, deploy across an odd number of data centers, each with an odd number of switches.

### Operating System

In alignment to the enterprise lifecycle, the Galera Cluster topology with MariaDB Enterprise Server and MariaDB MaxScale 25.01 is provided for:

* AlmaLinux 8 (x86\_64, ARM64)
* AlmaLinux 9 (x86\_64, ARM64)
* Debian 11 (x86\_64, ARM64)
* Debian 12 (x86\_64, ARM64)
* Red Hat Enterprise Linux 8 (x86\_64, ARM64)
* Red Hat Enterprise Linux 9 (x86\_64, PPC64LE, ARM64)
* Red Hat UBI 8 (x86\_64, ARM64)
* Rocky Linux 8 (x86\_64, ARM64)
* Rocky Linux 9 (x86\_64, ARM64)
* SUSE Linux Enterprise Server 15 (x86\_64, ARM64)
* Ubuntu 20.04 LTS (x86\_64, ARM64)
* Ubuntu 22.04 LTS (x86\_64, ARM64)
* Ubuntu 24.04 LTS (x86\_64, ARM64)

## Quick Reference

MariaDB Enterprise Server Configuration Management

<table><thead><tr><th width="183.18511962890625">Method</th><th>Description</th></tr></thead><tbody><tr><td>Configuration File</td><td>Configuration files (such as <code>/etc/my.cnf</code>) can be used to set system-variables and options. The server must be restarted to apply changes made to configuration files.</td></tr><tr><td>Command-line</td><td>The server can be started with command-line options that set system-variables and options.</td></tr><tr><td>SQL</td><td>Users can set system-variables that support dynamic changes on-the-fly using the SET statement.</td></tr></tbody></table>

MariaDB Enterprise Server packages are configured to read configuration files from different paths, depending on the operating system. Making custom changes to Enterprise Server default configuration files is not recommended because custom changes may be overwritten by other default configuration files that are loaded later.

To ensure that your custom changes will be read last, create a custom configuration file with the `z-` prefix in one of the include directories.

<table><thead><tr><th width="274.4443359375" valign="top">Distribution</th><th valign="top">Example Configuration File Path</th></tr></thead><tbody><tr><td valign="top"><ul><li>CentOS</li><li>Red Hat Enterprise Linux (RHEL)</li><li>SUSE Linux Enterprise Server (SLES)</li></ul></td><td valign="top"><code>/etc/my.cnf.d/z-custom-mariadb.cnf</code></td></tr><tr><td valign="top"><ul><li>Debian</li><li>Ubuntu</li></ul></td><td valign="top"><code>/etc/mysql/mariadb.conf.d/z-custom-mariadb.cnf</code></td></tr></tbody></table>

## MariaDB Enterprise Server Service Management

The `systemctl` command is used to start and stop the MariaDB Enterprise Server service. The `galera_new_cluster and galera_recovery` scripts are used for Enterprise Cluster-specific operations.

<table><thead><tr><th width="267.333251953125">Operation</th><th>Command</th></tr></thead><tbody><tr><td>Start</td><td><code>sudo systemctl start mariadb</code></td></tr><tr><td>Stop</td><td><code>sudo systemctl stop mariadb</code></td></tr><tr><td>Restart</td><td><code>sudo systemctl restart mariadb</code></td></tr><tr><td>Enable during startup</td><td><code>sudo systemctl enable mariadb</code></td></tr><tr><td>Disable during startup</td><td><code>sudo systemctl disable mariadb</code></td></tr><tr><td>Status</td><td><code>sudo systemctl status mariadb</code></td></tr><tr><td>Bootstrap a cluster node</td><td><code>sudo galera_new_cluster</code></td></tr><tr><td>Recover a cluster node's position</td><td><code>sudo galera_recovery</code></td></tr></tbody></table>

For additional information, see "[Starting and Stopping MariaDB](../../../server-management/starting-and-stopping-mariadb/)".

## MariaDB Enterprise Server Logs

MariaDB Enterprise Server produces log data that can be helpful in problem diagnosis.

Log filenames and locations may be overridden in the server configuration. The default location of logs is the data directory. The data directory is specified by the datadir system variable.

<table><thead><tr><th width="252.77783203125">Log</th><th width="212.25927734375">System Variable/Option</th><th>Default Filename</th></tr></thead><tbody><tr><td><a href="../../../server-management/server-monitoring-logs/error-log.md">MariaDB Error Log</a></td><td><a href="../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#list-of-server-system-variables">log_error</a></td><td><code>&#x3C;hostname>.err</code></td></tr><tr><td><a href="../../../reference/plugins/mariadb-enterprise-audit.md">MariaDB Enterprise Audit Log</a></td><td><a href="../../../reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables.md#server_audit_file_path">server_audit_file_path</a></td><td><code>server_audit.log</code></td></tr><tr><td><a href="../../../server-management/server-monitoring-logs/slow-query-log/">Slow Query Log</a></td><td><a href="../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#list-of-server-system-variables">slow_query_log_file</a></td><td><code>&#x3C;hostname>-slow.log</code></td></tr><tr><td><a href="../../../server-management/server-monitoring-logs/general-query-log.md">General Query Log</a></td><td><a href="../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#list-of-server-system-variables">general_log_file</a></td><td><code>&#x3C;hostname>.log</code></td></tr><tr><td><a href="../../../server-management/server-monitoring-logs/binary-log/">Binary Log</a></td><td><a href="../../../ha-and-performance/standard-replication/replication-and-binary-log-system-variables.md#log_bin">log_bin</a></td><td><code>&#x3C;hostname>-bin</code></td></tr></tbody></table>

## MaxScale Configuration Management

MaxScale can be configured using several methods. These methods make use of MaxScale's [REST API](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/administrative-tools-for-mariadb-maxscale/administrative-tools-for-mariadb-maxscale-rest-api/).

<table><thead><tr><th width="160.6666259765625" valign="top">Method</th><th valign="top">Benefits</th></tr></thead><tbody><tr><td valign="top"><a href="https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/administrative-tools-for-mariadb-maxscale/administrative-tools-for-mariadb-maxscale-maxctrl/">MaxCtrl</a></td><td valign="top">Command-line utility to perform administrative tasks through the REST API. See MaxCtrl Commands.</td></tr><tr><td valign="top"><a href="https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/administrative-tools-for-mariadb-maxscale/maxgui/">MaxGUI</a></td><td valign="top">MaxGUI is a graphical utility that can perform administrative tasks through the REST API.</td></tr><tr><td valign="top"><a href="https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/administrative-tools-for-mariadb-maxscale/administrative-tools-for-mariadb-maxscale-rest-api/">REST API</a></td><td valign="top">The REST API can be used directly. For example, the curl utility could be used to make REST API calls from the command-line. Many programming languages also have libraries to interact with REST APIs.</td></tr></tbody></table>

The procedure on these pages configures MaxScale using MaxCtrl.

## MaxScale Service Management

The systemctl command is used to start and stop the MaxScale service.>

<table><thead><tr><th width="231.7777099609375">Operation</th><th>Command</th></tr></thead><tbody><tr><td>Start</td><td><code>sudo systemctl start maxscale</code></td></tr><tr><td>Stop</td><td><code>sudo systemctl stop maxscale</code></td></tr><tr><td>Restart</td><td><code>sudo systemctl restart maxscale</code></td></tr><tr><td>Enable during startup</td><td><code>sudo systemctl enable maxscale</code></td></tr><tr><td>Disable during startup</td><td><code>sudo systemctl disable maxscale</code></td></tr><tr><td>Status</td><td><code>sudo systemctl status maxscale</code></td></tr></tbody></table>

For additional information, see "[Starting and Stopping MariaDB](../../../server-management/starting-and-stopping-mariadb/)".

## Next Step

Navigation in the procedure "Deploy Galera Cluster Topology":

Next: Step 1: Install MariaDB Enterprise Server

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>
