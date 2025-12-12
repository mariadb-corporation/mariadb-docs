---
description: >-
  Discover the capabilities of MariaDB MaxScale. This overview explains how the
  proxy manages high availability, load balancing, and security for your
  database infrastructure.
---

# MariaDB MaxScale Guide

### Quickstart Guide: MariaDB MaxScale Overview

MariaDB MaxScale is an advanced, open-source database proxy, router, and load balancer designed to enhance the scalability, high availability, and security of your MariaDB deployments. It acts as an intelligent intermediary between your applications and your MariaDB servers, abstracting the underlying database topology.

#### 1. What is MariaDB MaxScale?

MaxScale is not a database itself, but a sophisticated gateway that understands the MariaDB protocol. It intercepts client connections and routes them to the appropriate backend MariaDB servers based on configured rules, health checks, and workload types. This allows for flexible and dynamic management of database traffic without requiring changes to the application code.

#### 2. Core Functionalities and Benefits

MariaDB MaxScale provides several key functionalities that contribute to optimizing MariaDB environments:

* **Intelligent Routing and Load Balancing:**
  * **ReadWriteSplit Router:** This is a primary feature that automatically distinguishes between read (SELECT) and write (INSERT, UPDATE, DELETE, DDL) statements. It intelligently routes all write statements to the designated primary server and distributes read statements across multiple replica servers, significantly improving read scalability and reducing the load on the primary.
  * **Other Routers:** MaxScale offers various routers for different use cases, such as routing to specific databases, connection-based routing, or custom routing logic.
* **High Availability and Automated Failover:**
  * MaxScale constantly monitors the health of your MariaDB servers. In a replication setup (e.g., primary-replica or Galera Cluster), if the primary server fails, MaxScale can automatically detect the failure, promote a healthy replica to become the new primary, and seamlessly redirect client connections to the newly promoted server. This minimizes downtime and ensures continuous operation.
* **Seamless Server Maintenance:**
  * MaxScale provides built-in mechanisms to place backend servers into maintenance mode without interrupting connected applications or clients. This allows administrators to perform tasks like patching, upgrades, or reconfigurations on individual servers while MaxScale intelligently redirects traffic away from them. Management can be done via the `maxctrl` command-line interface, MaxGUI (web interface), or REST API.
* **Security and Traffic Control:**
  * MaxScale can implement granular security policies and traffic controls for database connections and queries. This includes features like firewalling, query filtering, and authentication proxying.
  * **QLAfilter (Query Log Anonymizer Filter):** This filter can be used to create an audit trail by logging all queries, with options to anonymize sensitive data, aiding in security audits and performance analysis.
* **Protocol Compatibility:** MaxScale is designed to be compatible with standard MariaDB and MySQL client protocols, making it transparent to most applications.

By abstracting the database topology and intelligently managing connections, MariaDB MaxScale helps organizations achieve higher availability, better performance, and enhanced security for their MariaDB deployments.

#### Further Resources:

* [MariaDB MaxScale Documentation](../maxscale-use-cases/maxscale-overview.md)
* [MariaDB MaxScale GitHub Repository](https://github.com/mariadb-corporation/MaxScale)
